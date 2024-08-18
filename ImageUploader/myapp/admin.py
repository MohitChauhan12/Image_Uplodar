from django.contrib import admin
from .models import Image

# Register your models here.

@admin.register(Image)
#admin.site.register(Image)

class ImageAdmin(admin.ModelAdmin):
	list_display=['id','photo','date']