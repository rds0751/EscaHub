from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from EscaHub.blog.forms import BlogForm
from EscaHub.blog.models import Blog, BlogComment, Tag
from EscaHub.decorators import ajax_required

def _blogs(request, blogs):
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    popular_tags = Tag.get_popular_tags()
    return render(request, 'blog/blogs.html', {
        'blogs': blogs,
        'popular_tags': popular_tags
    })


@login_required
def blogs(request):
    all_blogs = Blog.get_published()
    return _blogs(request, all_blogs)


@login_required
def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status=Blog.PUBLISHED)
    return render(request, 'blog/blog.html', {'blog': blog})


@login_required
def tag(request, tag_name):
    tags = Tag.objects.filter(tag=tag_name)
    blogs = []
    for tag in tags:
        if tag.blog.status == Blog.PUBLISHED:
            blogs.append(tag.blog)
    return _blogs(request, blogs)


@login_required
def write(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = Blog()
            blog.create_user = request.user
            blog.title = form.cleaned_data.get('title')
            blog.content = form.cleaned_data.get('content')
            status = form.cleaned_data.get('status')
            if status in [Blog.PUBLISHED, Blog.DRAFT]:
                blog.status = form.cleaned_data.get('status')
            blog.save()
            tags = form.cleaned_data.get('tags')
            blog.create_tags(tags)
            return redirect('/blog/')
    else:
        form = BlogForm()
    return render(request, 'blog/write.html', {'form': form})


@login_required
def drafts(request):
    drafts = Blog.objects.filter(create_user=request.user,
                                    status=Blog.DRAFT)
    return render(request, 'blog/drafts.html', {'drafts': drafts})


@login_required
def edit(request, id):
    tags = ''
    if id:
        blog = get_object_or_404(Blog, pk=id)
        for tag in blog.get_tags():
            tags = '{0} {1}'.format(tags, tag.tag)
        tags = tags.strip()
    else:
        blog = Blog(create_user=request.user)

    if blog.create_user.id != request.user.id:
        return redirect('home')

    if request.POST:
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = BlogForm(instance=blog, initial={'tags': tags})
    return render(request, 'blog/edit.html', {'form': form})


@login_required
@ajax_required
def preview(request):
    try:
        if request.method == 'POST':
            content = request.POST.get('content')
            html = 'Nothing to display :('
            if len(content.strip()) > 0:
                html = markdown.markdown(content, safe_mode='escape')
            return HttpResponse(html)
        else:
            return HttpResponseBadRequest()

    except Exception:
        return HttpResponseBadRequest()


@login_required
@ajax_required
def comment(request):
    try:
        if request.method == 'POST':
            blog_id = request.POST.get('blog')
            blog = Blog.objects.get(pk=article_id)
            comment = request.POST.get('comment')
            comment = comment.strip()
            if len(comment) > 0:
                blog_comment = BlogComment(user=request.user,
                                                 blog=blog,
                                                 comment=comment)
                blog_comment.save()
            html = ''
            for comment in blog.get_comments():
                html = '{0}{1}'.format(html, render_to_string(
                    'blog/partial_blog_comment.html',
                    {'comment': comment}))

            return HttpResponse(html)

        else:
            return HttpResponseBadRequest()

    except Exception:
        return HttpResponseBadRequest()
