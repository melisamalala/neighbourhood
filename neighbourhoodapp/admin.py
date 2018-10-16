# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Location,tags, Image, Project, Profile, Review


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('project', 'usability_rating', 'content_rating', 'design_rating', 'user', 'comment', 'image',)
    list_filter = ['user',]
    search_fields = ['comment',]

admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Image, ImageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)