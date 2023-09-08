from django.contrib import admin
from app.models import Image
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    image=('image')

admin.site.register(Image, ImageAdmin)