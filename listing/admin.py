from django.contrib import admin
from .models import Category, Listing, Review
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'owner', 'status')
    list_filter = ('status', 'created', 'publish', 'owner')
    search_fields = ('name', 'service')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'listing', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
