from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Testimonial, Service, Product, Project, BackgroundImage, About, Contact
from .serializers import (
    TestimonialSerializer,
    ServiceSerializer,
    ProductSerializer,
    ProjectSerializer,
    AboutSerializer,
    BackgroundHomeImage,
    ContactSerializer
)

# --- List Views ---
class TestimonialListView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# --- Singleton Views ---
class AboutView(RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()

class BackgroundImageView(RetrieveAPIView):
    queryset = BackgroundImage.objects.all()
    serializer_class = BackgroundHomeImage

    def get_object(self):
        return BackgroundImage.objects.first()

class ContactView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_object(self):
        return Contact.objects.first()

