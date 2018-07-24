from django.contrib import admin
from .models import Yeast, Media, StorageInstance

# Register your models here.
admin.site.register(Yeast)
admin.site.register(Media)
admin.site.register(StorageInstance)