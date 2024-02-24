from django.urls import path
from django.urls import re_path
from django.views.static import serve
from django.conf.urls.static import static
from . import views
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('files/',views.files, name='files'),
    path('login/',auth_view.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/',views.profile, name='profile'),
    path('search_blogs/', views.BlogSearchView.as_view(), name="search_blogs"),
    path('logout/',auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('<int:pk>/',DetailArticleView.as_view(), name='detail_article'),
    path('delete_item/<int:myid>/',delete_item,name="delete_item"),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




