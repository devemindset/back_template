from django.urls import path
from . import views

urlpatterns = [
    path("testimonials/", views.TestimonialListView.as_view(), name="testimonial-list"),
    path("services/", views.ServiceListView.as_view(), name="service-list"),
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("projects/", views.ProjectListView.as_view(), name="project-list"),

    path("about/", views.AboutView.as_view(), name="about-single"),
    path("background-image/", views.BackgroundImageView.as_view(), name="background-image"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
