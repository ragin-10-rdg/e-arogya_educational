"""
Django Admin configuration for E-Arogya Health Content
"""
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import HealthCategory, MediaContent, ContentRating, ContentView


@admin.register(HealthCategory)
class HealthCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Health Categories
    """
    list_display = ['name', 'slug', 'icon', 'color_display', 'is_active', 'order', 'content_count', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Display Settings', {
            'fields': ('icon', 'color', 'order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
    
    def color_display(self, obj):
        """Display color as a colored box"""
        return format_html(
            '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #ccc;"></div>',
            obj.color
        )
    color_display.short_description = 'Color'
    
    def content_count(self, obj):
        """Display count of active content"""
        count = obj.active_content_count
        url = reverse('admin:health_content_mediacontent_changelist') + f'?category__id__exact={obj.id}'
        return format_html('<a href="{}">{} items</a>', url, count)
    content_count.short_description = 'Content Count'


@admin.register(MediaContent)
class MediaContentAdmin(admin.ModelAdmin):
    """
    Admin interface for Media Content
    """
    list_display = [
        'title', 'category', 'content_type', 'author', 'is_featured', 
        'is_active', 'is_verified', 'view_count', 'published_date'
    ]
    list_filter = [
        'category', 'content_type', 'difficulty_level', 'target_age_group',
        'is_featured', 'is_active', 'is_verified', 'published_date'
    ]
    search_fields = ['title', 'description', 'author', 'source', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_active', 'is_verified']
    date_hierarchy = 'published_date'
    ordering = ['-published_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'title', 'slug', 'description', 'content_type')
        }),
        ('URLs and Media', {
            'fields': ('url', 'thumbnail_url', 'embed_code')
        }),
        ('Metadata', {
            'fields': ('author', 'source', 'duration', 'language', 'difficulty_level', 'target_age_group')
        }),
        ('Content Management', {
            'fields': ('is_featured', 'is_active', 'is_verified', 'published_date')
        }),
        ('SEO and Tags', {
            'fields': ('tags', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Analytics', {
            'fields': ('view_count', 'like_count', 'share_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at', 'view_count', 'like_count', 'share_count']
    
    actions = ['mark_as_featured', 'mark_as_not_featured', 'mark_as_verified', 'mark_as_active']
    
    def mark_as_featured(self, request, queryset):
        """Mark selected content as featured"""
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} items marked as featured.')
    mark_as_featured.short_description = "Mark selected items as featured"
    
    def mark_as_not_featured(self, request, queryset):
        """Remove featured status from selected content"""
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} items unmarked as featured.')
    mark_as_not_featured.short_description = "Remove featured status"
    
    def mark_as_verified(self, request, queryset):
        """Mark selected content as verified"""
        updated = queryset.update(is_verified=True)
        self.message_user(request, f'{updated} items marked as verified.')
    mark_as_verified.short_description = "Mark selected items as verified"
    
    def mark_as_active(self, request, queryset):
        """Mark selected content as active"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} items marked as active.')
    mark_as_active.short_description = "Mark selected items as active"
    
    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        return super().get_queryset(request).select_related('category')


@admin.register(ContentRating)
class ContentRatingAdmin(admin.ModelAdmin):
    """
    Admin interface for Content Ratings
    """
    list_display = ['content', 'rating', 'user_ip', 'created_at']
    list_filter = ['rating', 'created_at', 'content__category']
    search_fields = ['content__title', 'comment', 'user_ip']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        return super().get_queryset(request).select_related('content', 'content__category')


@admin.register(ContentView)
class ContentViewAdmin(admin.ModelAdmin):
    """
    Admin interface for Content Views (Analytics)
    """
    list_display = ['content', 'user_ip', 'viewed_at']
    list_filter = ['viewed_at', 'content__category', 'content__content_type']
    search_fields = ['content__title', 'user_ip']
    readonly_fields = ['content', 'user_ip', 'user_agent', 'viewed_at']
    date_hierarchy = 'viewed_at'
    ordering = ['-viewed_at']
    
    def has_add_permission(self, request):
        """Disable manual addition of views"""
        return False
    
    def has_change_permission(self, request, obj=None):
        """Make views read-only"""
        return False
    
    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        return super().get_queryset(request).select_related('content', 'content__category')


# Customize admin site header and title
admin.site.site_header = "E-Arogya Health Content Admin"
admin.site.site_title = "E-Arogya Admin"
admin.site.index_title = "Health Content Management"
