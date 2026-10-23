from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from . import views as site_main_views

urlpatterns = [
    # path("", image_upload, name="upload"),
    path(settings.ADMIN_PAGE, admin.site.urls),
    path("portfolio/", include("portfolio.urls", namespace="portfolio")),
    path("", site_main_views.landing_page, name="site-main-landing"),
    # path("", about, name="about"),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if bool(settings.DEBUG):
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
