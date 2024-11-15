from django.shortcuts import render, redirect

from .models import Comment
from posts.models import Post
from users.models import User


def comment_list(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    post = Post.objects.get(id=post_id)
    return render(request, "comments/comment_list.html", {"comments": comments, "post": post})


def comment_detail(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        comment.content = request.POST["content"]
        comment.save()
        return redirect("post_detail", post_id=comment.post.id)
    comment = Comment.objects.get(id=comment_id)
    return render(request, "comments/comment_detail.html", {"comment": comment})


def comment_create(request, post_id):
    if request.method == "POST":
        content = request.POST["content"]
        author_id = request.POST["author"]
        author = User.objects.get(id=author_id)
        post = Post.objects.get(id=post_id)
        Comment.objects.create(content=content, author=author, post=post)
        return redirect("post_detail", post_id=post_id)
    users = User.objects.all()
    return render(request, "comments/comment_form.html", {"users": users, "post_id": post_id})
