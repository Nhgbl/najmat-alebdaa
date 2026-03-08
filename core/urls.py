from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
import os

urlpatterns = [
    # رابط لوحة التحكم
    path('najmat-admin/', admin.site.urls),
    
    # تضمين روابط تطبيق main (موقعنا)
    path('', include('main.urls')),
]

# إضافة مسارات الميديا للعمل في بيئة الإنتاج على Render
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]

# إضافة مسارات robots.txt و sitemap.xml
urlpatterns += [
    path('robots.txt', serve, {'path': 'robots.txt', 'document_root': settings.BASE_DIR}),
    path('sitemap.xml', serve, {'path': 'sitemap.xml', 'document_root': settings.BASE_DIR}),
]