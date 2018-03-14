from django.http import  HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import PostForm, PostModelForm, CommentForm
from .models import Post, Comment

def post_list(request):
    # name="장고"
    # return HttpResponse("""
    #     <h1>Hello Django</h1>
    #     <p>{name}</p>
    # """.format(name=name))

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#글등록(Form)
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #register1
            # post = Post()
            # post.author = request.user
            # post.title = form.cleaned_data['title']
            # post.text = form.cleaned_data['text']
            # post.published_date = timezone.now()
            # post.save()
            #register2
            post = Post.objects.create(
                author = request.user,
                title=form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                published_date=timezone.now())
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})

#글등록(ModelForm)
@login_required
def post_new2(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostModelForm()
    return render(request, 'blog/post_form.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_form.html', {'form':form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
		comment = get_object_or_404(Comment, pk=pk)
		comment.approve()
		return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
		comment = get_object_or_404(Comment, pk=pk)
		post_pk = comment.post.pk
		comment.delete()
		return redirect('post_detail', pk=post_pk)