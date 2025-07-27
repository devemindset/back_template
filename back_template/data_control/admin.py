from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.html import format_html
from .models import Service, BackgroundImage, About, Product, Contact, Project
from django.contrib import messages

# -------- UTILITAIRE : Aperçu image --------
def image_preview(obj):
    if hasattr(obj, "image") and obj.image:
        return format_html('<img src="{}" width="150" style="object-fit:cover;" />', obj.image.url)
    return "-"
image_preview.short_description = 'Preview'

# --- Singleton BaseAdmin ---
class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Empêche l'ajout d'un 2e objet
        count = self.model.objects.count()
        return count == 0

    def changelist_view(self, request, extra_context=None):
        # Redirige vers l'unique instance existante
        opts = self.model._meta
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(reverse(f"admin:{opts.app_label}_{opts.model_name}_change", args=(obj.pk,)))
        return super().changelist_view(request, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Message d'aide visible en haut du formulaire
        extra_context = extra_context or {}
        extra_context['help_message'] = _(
            "This section only accepts one entry. Please fill it carefully."
        )
        return super().change_view(request, object_id, form_url, extra_context)


# -------- Service --------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name", "short_description")
    search_fields = ("service_name", "description", "content")

    def short_description(self, obj):
        return obj.description[:50] + "..."
    short_description.short_description = "Description"


# -------- Product --------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "short_description", image_preview)
    search_fields = ("product_name", "description", "content")

    def short_description(self, obj):
        return obj.description[:50] + "..."
    short_description.short_description = "Description"


# -------- Project --------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "external_link", image_preview)
    search_fields = ("project_name", "description", "content")


# --- About ---
@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    fieldsets = (
        (_("About Section"), {
            'fields': ('image', 'description'),
            'description': _("Image and description about you")
        }),
    )
    verbose_name = _("About Section")

# --- Contact ---
@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
    fieldsets = (
        (_("Contact Info"), {
            'fields': ('address', 'phonenumber', 'email'),
            'description': _("Enter your contact details here.")
        }),
    )
    verbose_name = _("Contact Details")

# --- Background Image ---
@admin.register(BackgroundImage)
class BackgroundImageAdmin(SingletonModelAdmin):
    fieldsets = (
        (_("Homepage Background"), {
            'fields': ('background_image',),
            'description': _("Upload a high quality homepage background image.")
        }),
    )
    verbose_name = _("Homepage Background Image")
