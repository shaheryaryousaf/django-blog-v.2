from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter)
from .models import Category, Post


# ============================
# Category
# ============================

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'meta_title', 'meta_description', 'created_at', 'updated_at')


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['title']}),
        ('SEO Information', {'fields': ['meta_title', 'meta_description']})
    ]

    def category_post_count(self, obj):
        return obj.category_set.count()
    category_post_count.short_description = "Total Posts"

    list_display = ('id', 'title', 'category_post_count', 'slug')
    list_display_links = ('id', 'title', 'slug')
    list_per_page = 25
    search_fields = ['title']
    # prepopulated_fields = {'slug': ('title',)}
    resource_class = CategoryResource
    pass


# ============================
# Posts
# ============================

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'description','is_published', 'author', 'slug', 'meta_title', 'meta_description', 'created_at', 'updated_at')


class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['category', 'title', 'description', 'is_published', 'author']}),
        ('SEO Information', {'fields': ['meta_title', 'meta_description']})
    ]

    list_display = ('id', 'title', 'category', 'is_published', 'author', 'slug')
    list_display_links = ('id', 'title', 'slug')
    list_per_page = 25
    search_fields = ['title']
    autocomplete_fields = ('category',)
    # prepopulated_fields = {'slug': ('title',)}
    resource_class = PostResource
    actions = ('make_post_published', 'make_post_unpublished')
    pass

    def make_post_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, '{} Posts have been published successfully.'.format(count))
    make_post_published.short_description = 'Publish Post'

    def make_post_unpublished(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, '{} Listings are ubpublished now.'.format(count))
    make_post_unpublished.short_description = 'Unpublish Post'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)