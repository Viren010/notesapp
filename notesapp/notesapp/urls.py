from django.contrib import admin
from django.urls import path
from notes.views import NoteViewSet
from django.urls import include, re_path

urlpatterns = [
    # the admin path is present by default when you create the Django profject. It is used to access the Django admin panel.
    path('admin/', admin.site.urls),

    # the URLs for your APIs start from here
    re_path(r'^note$', NoteViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    re_path(r'^note/all$', NoteViewSet.as_view(
        {
            'get': 'list',
        }
    )),
]