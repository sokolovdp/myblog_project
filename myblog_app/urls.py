from django.conf.urls import url
import myblog_app.views


urlpatterns = [
    url(r'^$', myblog_app.views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', myblog_app.views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)/$', myblog_app.views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', myblog_app.views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', myblog_app.views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', myblog_app.views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^drafts/$', myblog_app.views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', myblog_app.views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', myblog_app.views.approve_comment, name='approve_comment'),
    url(r'^comment/(?P<pk>\d+)/remove/$', myblog_app.views.remove_comment, name='remove_comment'),
    url(r'^post/(?P<pk>\d+)/publish/$', myblog_app.views.post_publish, name='post_publish'),
]
