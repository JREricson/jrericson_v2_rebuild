from django.urls import path
from django.views.generic import TemplateView
from . import views as portfolio_views
from .views import ProjectListView, ProjectDetailView


app_name = "portfolio"
urlpatterns = [
    path("", portfolio_views.about, name="about"),
    # path("about/", portfolio_views.about, name="about"),
    path("contact/", portfolio_views.contact, name="contact"),
    path("projects", ProjectListView.as_view(), name="projects"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project"),
    # path("single/<slug:slug>", views.single, name="single"),
]
