from django.urls import path

from . import views

urlpatterns = [
    path("<int:post_id>/", views.comment_list, name="comment_list"),
    path("detail/<int:comment_id>/", views.comment_detail, name="comment_detail"),
    path("<int:post_id>/create/", views.comment_create, name="comment_create"),
]
