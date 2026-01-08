from django.contrib import admin

from django.utils.html import format_html
from .models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    """作品管理后台"""
    
    list_display = [
        'cover_preview', 'title', 'student_name', 
        'category_display', 'type_display', 
        'is_published', 'order', 'created_at'
    ]
    
    list_filter = ['category', 'work_type', 'is_published', 'created_at']
    
    search_fields = ['title', 'student_name', 'description']
    
    list_editable = ['is_published', 'order']
    
    readonly_fields = ['cover_preview_large', 'created_at', 'updated_at']
    
    fieldsets = [
        ('基本信息', {
            'fields': ['title', 'student_name', 'category', 'work_type', 'description']
        }),
        ('封面', {
            'fields': ['cover_image', 'cover_preview_large']
        }),
        ('作品内容', {
            'fields': ['media_file', 'content_url'],
            'description': '根据作品类型选择：图片/视频上传媒体文件，网页链接填写URL'
        }),
        ('发布设置', {
            'fields': ['is_published', 'order']
        }),
        ('时间信息', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]
    
    actions = ['publish_works', 'unpublish_works']
    
    def cover_preview(self, obj):
        """列表页封面缩略图"""
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                obj.cover_image.url
            )
        return '-'
    cover_preview.short_description = '封面'
    
    def cover_preview_large(self, obj):
        """详情页封面预览"""
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px;" />',
                obj.cover_image.url
            )
        return '-'
    cover_preview_large.short_description = '封面预览'
    
    def category_display(self, obj):
        """分类显示"""
        return obj.get_category_display()
    category_display.short_description = '分类'
    
    def type_display(self, obj):
        """类型显示"""
        icon = obj.get_type_display_icon()
        return f'{icon} {obj.get_work_type_display()}'
    type_display.short_description = '类型'
    
    def publish_works(self, request, queryset):
        """批量发布"""
        count = queryset.update(is_published=True)
        self.message_user(request, f'成功发布 {count} 个作品')
    publish_works.short_description = '发布选中的作品'
    
    def unpublish_works(self, request, queryset):
        """批量取消发布"""
        count = queryset.update(is_published=False)
        self.message_user(request, f'成功取消发布 {count} 个作品')
    unpublish_works.short_description = '取消发布选中的作品'

