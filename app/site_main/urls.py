from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views as site_main_views


from upload.views import image_upload
from portfolio.views import about

urlpatterns = [
    # path("", image_upload, name="upload"),
    path(settings.ADMIN_PAGE, admin.site.urls),
    path("portfolio/", include("portfolio.urls", namespace="portfolio")),
    path("", site_main_views.landing_page, name="site-main-landing"),
    # path("", about, name="about"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
