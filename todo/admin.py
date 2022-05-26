from django.contrib import admin
from .models import *

# Register your models here.
class NoteUnitInline(admin.TabularInline):
    model = Note

class VoiceUnitInline(admin.TabularInline):
    model = Voice

@admin.register(Todo)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    inlines = (NoteUnitInline, VoiceUnitInline)


admin.site.register(Category)