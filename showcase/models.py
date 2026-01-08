from django.db import models


class Work(models.Model):
    """学员作品模型"""
    
    # 作品分类选项
    CATEGORY_CHOICES = [
        ('multimodal', 'AI多模态创作'),
        ('programming', 'AI编程应用'),
        ('digital_human', 'AI数字人'),
    ]
    
    # 作品类型选项
    TYPE_CHOICES = [
        ('image', '图片'),
        ('video', '视频'),
        ('link', '网页链接'),
    ]
    
    # 基本信息
    title = models.CharField('作品标题', max_length=200)
    category = models.CharField('分类', max_length=20, choices=CATEGORY_CHOICES)
    work_type = models.CharField('作品类型', max_length=10, choices=TYPE_CHOICES)
    student_name = models.CharField('学员姓名', max_length=100)
    description = models.TextField('作品描述', blank=True)
    
    # 封面（必填）
    cover_image = models.ImageField('封面图片', upload_to='works/covers/')
    
    # 内容（根据类型选择性使用）
    media_file = models.FileField('媒体文件', upload_to='works/media/', blank=True, null=True, 
                                  help_text='图片或视频文件')
    content_url = models.URLField('网页链接', blank=True, 
                                  help_text='作品链接URL')
    
    # 控制字段
    is_published = models.BooleanField('是否发布', default=True)
    order = models.IntegerField('排序权重', default=0, 
                                help_text='数字越大越靠前')
    
    # 时间戳
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    
    class Meta:
        verbose_name = '学员作品'
        verbose_name_plural = '学员作品'
        ordering = ['-order', '-created_at']  # 按权重和时间倒序
    
    def __str__(self):
        return f'{self.title} - {self.student_name}'
    
    def get_type_display_icon(self):
        """获取类型图标"""
        icons = {
            'image': '📷',
            'video': '🎬',
            'link': '🔗',
        }
        return icons.get(self.work_type, '📄')

