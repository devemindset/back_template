from django.db import models
import os 
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from PIL import Image

def upload_image(instance, filename):
    base, ext = os.path.splitext(filename)
    clean_name = slugify(base)
    return f'uploads/{instance.__class__.__name__.lower()}_{clean_name}{ext.lower()}'

class Testimonial(models.Model):
    image = models.ImageField(
        upload_to=upload_image,
        verbose_name="Profile Picture",
        help_text="Upload a square image (max 500x500px, max 1MB)"
    )
    name = models.CharField(
        max_length=50,
        verbose_name="Client Name",
        help_text="Full name of the person giving the testimonial"
    )
    field = models.CharField(
        max_length=255,
        verbose_name="Occupation or Role",
        help_text="Example: Freelancer, UX Designer, CEO..."
    )
    text = models.CharField(
        max_length=255,
        verbose_name="Testimonial Text",
        help_text="The actual testimonial message (minimum 10 characters)"
    )

    def __str__(self):
        return f"{self.name} - {self.field}"

    def clean(self):
        # Basic text validations
        if len(self.name.strip()) == 0:
            raise ValidationError({"name": "Name cannot be empty."})
        if len(self.text.strip()) < 10:
            raise ValidationError({"text": "Testimonial must be at least 10 characters long."})

        # Image size check
        if self.image and self.image.size > 1024 * 1024:  # 1MB max
            raise ValidationError({"image": "Image size must be less than 1MB."})

        # Image dimension check (Pillow)
        if self.image:

            image = Image.open(self.image)
            width, height = image.size
            if width > 500 or height > 500:
                raise ValidationError({
                    "image": "Image dimensions must not exceed 500x500 pixels."
                })

    def save(self, *args, **kwargs):
        self.full_clean()  # Trigger validation
        super().save(*args, **kwargs)

# ------------------- SERVICE -------------------
class Service(models.Model):
    service_name = models.CharField(
        max_length=100,
        verbose_name="Service Name",
        help_text="Enter the name of the service"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Short Description",
        help_text="Minimum 100 characters"
    )
    content = models.TextField(
        verbose_name="Detailed Content",
        help_text="Minimum 255 characters"
    )
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.service_name}'

    def clean(self):
        if not self.service_name.strip():
            raise ValidationError({"service_name": "Service name cannot be empty."})
        if len(self.description.strip()) < 100:
            raise ValidationError({"description": "Description must be at least 100 characters long."})
        if len(self.content.strip()) < 255:
            raise ValidationError({"content": "Content must be at least 255 characters long."})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.service_name)
        self.full_clean()
        super().save(*args, **kwargs)

# ------------------- BACKGROUND IMAGE -------------------
class BackgroundImage(models.Model):
    background_image = models.ImageField(
        upload_to=upload_image,
        verbose_name="Home Background Image",
        help_text="Max size 2MB, max dimensions 1920x1055px"
    )

    def __str__(self):
        return f'Home Background - {self.background_image}'

    def clean(self):
        if self.background_image:
            if self.background_image.size > 2 * 1024 * 1024:
                raise ValidationError({"background_image": "Image size must not exceed 2MB."})
            img = Image.open(self.background_image)
            w, h = img.size
            if w > 1920 or h > 1055:
                raise ValidationError({"background_image": "Image dimensions must not exceed 1920x1055 pixels."})
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

# ------------------- ABOUT -------------------
class About(models.Model):
    image = models.ImageField(
        upload_to=upload_image,
        verbose_name="About Image",
        help_text="Max 1920x1055px"
    )
    description = models.TextField(
        verbose_name="About Description",
        help_text="Write something about you"
    )

    def __str__(self):
        return self.description[:60]

    def clean(self):
        if self.image:
            img = Image.open(self.image)
            w, h = img.size
            if w > 1920 or h > 1055:
                raise ValidationError({"image": "Image dimensions must not exceed 1920x1055 pixels."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

# ------------------- PRODUCT -------------------
class Product(models.Model):
    image = models.ImageField(
        upload_to=upload_image,
        verbose_name="Product Image"
    )
    product_name = models.CharField(
        max_length=100,
        verbose_name="Product Name"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Short Description",
        help_text="Minimum 100 characters"
    )
    content = models.TextField(
        verbose_name="Product Details",
        help_text="Minimum 255 characters"
    )
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.product_name

    def clean(self):
        if not self.product_name.strip():
            raise ValidationError({"product_name": "Product name cannot be empty."})
        if len(self.description.strip()) < 100:
            raise ValidationError({"description": "Description must be at least 100 characters long."})
        if len(self.content.strip()) < 255:
            raise ValidationError({"content": "Content must be at least 255 characters long."})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        self.full_clean()
        super().save(*args, **kwargs)

# ------------------- CONTACT -------------------
class Contact(models.Model):
    address = models.CharField(
        max_length=255,
        verbose_name="Address"
    )
    phonenumber = models.CharField(
        max_length=20,
        verbose_name="Phone Number"
    )
    email = models.EmailField(
        max_length=100,
        verbose_name="Email Address"
    )

    def __str__(self):
        return f"{self.address} | {self.phonenumber} | {self.email}"

# ------------------- PROJECT -------------------
class Project(models.Model):
    image = models.ImageField(
        upload_to=upload_image,
        verbose_name="Project Image"
    )
    project_name = models.CharField(
        max_length=100,
        verbose_name="Project Name"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Short Description",
        help_text="Minimum 100 characters"
    )
    content = models.TextField(
        verbose_name="Project Details",
        help_text="Minimum 255 characters"
    )
    external_link = models.URLField(
        verbose_name="External URL",
        help_text="Link to the live project"
    )

    def __str__(self):
        return self.project_name

    def clean(self):
        if not self.project_name.strip():
            raise ValidationError({"project_name": "Project name cannot be empty."})
        if len(self.description.strip()) < 100:
            raise ValidationError({"description": "Description must be at least 100 characters long."})
        if len(self.content.strip()) < 255:
            raise ValidationError({"content": "Content must be at least 255 characters long."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)