"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.conf.urls import url,patterns,include
from django.contrib import admin
from myblog.blogs import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^$', include(views.blog_list)),
    url(r'^index$', include(views.blog_list)),
    url(r'^admin/', include(views.blog_list)),
    url(r'^blog/list$', views.blog_list),
    url(r'^blog/form$', views.blog_form),
    url(r'^blog/delete$', views.blog_del),
    url(r'^blog/view$', views.blog_view),
    url(r'^blog/edit$', views.blog_edit),
    url(r'^aboutme$', views.aboutme),
    #url(r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'home/desktop/myblog/myblog/blogs/static'}), 
    url(r'/(?P<path>.*)','django.views.static.serve',{'document_root':'/static'}),
)
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()
# #urlpatterns += staticfiles_urlpatterns()