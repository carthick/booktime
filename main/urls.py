from django.urls import path
from django.views.generic import TemplateView
from main import views
urlpatterns = [
    path(
        "about-me/",
        TemplateView.as_view(template_name="about_me.html"),
        name="about_me",),
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home",),
     path(
        "contact-me/",
        views.ContactUsView.as_view(),
        name="contact_me",
    ),
]