from django.contrib import admin

from .models import Game, Review

class ReviewAdminInline(admin.TabularInline):
    model = Review
    fields = ['user_name','rating','review_text']
    extra = 0

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre','platform','release_date']
    inlines = [ReviewAdminInline]
