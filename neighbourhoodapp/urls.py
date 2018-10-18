from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^$', views.home_projects, name='homePage'),
    url(r'^search/', views.search_businesses, name='search_businesses'),
# url(r'^join/', views.join_neighbourhood, name='join_neighbourhood'),
    url(r'^image(\d+)', views.project, name='project'),
    url(r'^business(\d+)', views.business, name='business'),
    url(r'^neighbourhood/(\d+)', views.neighbourhood, name='neighbourhood'),
    url(r'^users/', views.user_list, name='user_list'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^new/business$', views.new_business, name='new_business'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^new/neighbourhood$', views.new_neighbourhood, name='new_neighbourhood'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile/(?P<username>[0-9]+)$',
        views.individual_profile_page, name='individual_profile_page'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$',
        views.review_detail, name='review_detail'),
    url(r'^project$', views.project_list, name='project_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
