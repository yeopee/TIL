from django.urls import path
from .import views as article_views
urlpatterns = [
    path('', article_views.index, name="articles"),
    path('js-test/',article_views.js_test),
    path('jq-test/',article_views.jq_test),
    path('jq-test/boards/',article_views.submit_boards,name="submit_boards"),
    path('jq-test/boards/delete/',article_views.delete_boards, name="delete_boards"),
    path('jq-test/boards/edit',article_views.edit_boards,name="edit_boards"),
    path('articles/<int:article_id>/edit/',article_views.edit,name="edit"),
    path('articles/<int:article_id>/delete/',article_views.delete,name="delete" ),
    path('comments/', article_views.comments,name="comments"),
    path('comments/delete',article_views.delete_comment,name="delete_comment"),
    path('comments/<int:comment_id>/edit',article_views.edit_comment,name="edit_comment"),
    path('articles/likes/',article_views.likes, name="likes")

]