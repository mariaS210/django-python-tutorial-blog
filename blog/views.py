from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, PostImage, PostText
from .forms import PostForm, CommentForm, UploadForm, TextBlockForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', { 'posts': posts })

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__exact=None).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', { 'posts': posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post' : post })

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid :
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', { 'form' : form })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid :
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', { 'form' : form })

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return	redirect('blog.views.post_detail',	pk=pk)

@login_required
def	post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return	redirect('blog.views.post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid :
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', { 'form' : form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    comment.approve()
    return redirect('blog.views.post_detail', pk=post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    comment.delete()
    return redirect('blog.views.post_detail', pk=post.pk)

@login_required
def upload_image(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            postimage = form.save(commit=False)
            postimage.post = post
            postimage.upload_date = timezone.now()
            postimage.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form=UploadForm()
    return render(request, 'blog/upload_image.html', { 'form' : form})
    return redirect('blog.views.post_detail', pk=post.pk)

@login_required
def add_textblock(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form=TextBlockForm(request.POST)
        if form.is_valid():
            textblock = form.save(commit=False)
            textblock.post = post
            textblock.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form=TextBlockForm()
    return render(request, 'blog/add_textblock.html', { 'form' : form})
    #return redirect('blog.views.post_detail', pk=post.pk)
