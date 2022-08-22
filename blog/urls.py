from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.conf import settings
from blog import views





urlpatterns = [
        path('',views.PostListView.as_view(),name='post_list'),
        path('about',views.AboutView.as_view(),name = 'about'),
        path('post/(<int:pk>/)',views.PostDetailView.as_view(),name='post_detail'),
        path('post/new',views.CreatePostView.as_view(),name='post_new'),
        path('post/(<int:pk>/)/edit/',views.PostUpdateView.as_view(),name='post_edit'),
        path('post/(<int:pk>/)/remove/',views.PostDeleteView.as_view(),name='post_remove'),
        path('draft',views.DraftListView.as_view(),name='post_draft_list'),

        # path('post/(?P<pk>/)/comment/',views.add_comment_to_post,name='add_comment_to_post'),
        path('post/new/comment/<int:pk>/',views.add_comment_to_post,name='add_comment_to_post'),
        path('comment/(<int:pk>/)/approved/',views.comment_approved,name='comment_approved'),
        path('comment/(<int:pk>/)/remove/',views.comment_remove,name='comment_remove'),
        path('post/(<int:pk>/)/publish/',views.post_publish,name='post_publish'),





]
