from django.shortcuts import render, redirect

from .models import Post
from users.models import User


def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        author_id = request.POST["author"]
        author = User.objects.get(id=author_id)
        Post.objects.create(title=title, content=content, author=author)
        return redirect("post_list")
    users = User.objects.all()
    return render(request, "posts/post_form.html", {"users": users})
