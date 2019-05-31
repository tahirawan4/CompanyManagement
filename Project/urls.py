# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from core.views import IndexView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('', include('core.urls')),
                  path('', include('products.urls')),
                  path('', include('invoices.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', IndexView.as_view(), name='home'),
                  # path('login', TemplateView.as_view(template_name='admin_app/login.html'), name='home'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
