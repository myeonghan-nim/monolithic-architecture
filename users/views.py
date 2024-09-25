from django.shortcuts import render, redirect

from .models import User


def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {"users": users})


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    posts = user.posts.all()
    comments = user.comments.all()
    return render(
        request,
        "users/user_detail.html",
        {"user": user, "posts": posts, "comments": comments},
    )


def user_create(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create(username=username, email=email, password=password)
        return redirect("user_list")
    return render(request, "users/user_form.html")
