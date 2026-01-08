from django.shortcuts import render

from .models import Work


def showcase(request):
    """作品展示首页"""
    # 获取所有已发布的作品，按分类分组
    works_by_category = {
        'multimodal': Work.objects.filter(category='multimodal', is_published=True),
        'programming': Work.objects.filter(category='programming', is_published=True),
        'digital_human': Work.objects.filter(category='digital_human', is_published=True),
    }
    
    context = {
        'works_by_category': works_by_category,
        'categories': [
            {'key': 'multimodal', 'name': 'AI多模态创作'},
            {'key': 'programming', 'name': 'AI编程应用'},
            {'key': 'digital_human', 'name': 'AI数字人'},
        ]
    }
    
    return render(request, 'showcase/index.html', context)

