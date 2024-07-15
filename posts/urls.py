from django.conf import settings
from django.contrib import admin
from posts.views import homepage, post, about, search, category_post_list, allposts
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('postlist/<slug>/', category_post_list, name = 'post_list'),
    path('posts/', allposts, name = 'allposts'),
]