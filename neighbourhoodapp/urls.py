from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^$', views.home_projects, name='homePage'),
    # url(r'^search/', views.search_users, name='search_users'),
    url(r'^search/', views.search_projects, name='search_projects'),
    url(r'^image(\d+)', views.project, name='project'),
    url(r'^users/', views.user_list, name='user_list'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile/(?P<username>[0-9]+)$',
        views.individual_profile_page, name='individual_profile_page'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProfileDescription.as_view()),
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$',
        views.review_detail, name='review_detail'),
    # ex: /project/
    url(r'^project$', views.project_list, name='project_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
