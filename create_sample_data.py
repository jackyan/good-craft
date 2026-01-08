import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from showcase.models import Work

# 创建示例作品
sample_works = [
    {
        'title': '未来城市：赛博朋克之梦',
        'category': 'multimodal',
        'work_type': 'image',
        'student_name': '张小明',
        'description': '使用AI图像生成工具创作的赛博朋克风格未来城市场景。融合了霓虹灯、飞行器和全息广告牌等元素，展现了对未来科技城市的想象。',
        'cover_image': 'works/covers/ai_art_cover.png',
        'media_file': 'works/covers/ai_art_cover.png',
    },
    {
        'title': 'Aura AI - 智能对话助手',
        'category': 'programming',
        'work_type': 'image',
        'student_name': '李华',
        'description': '基于大语言模型开发的AI聊天助手应用。支持自然语言对话、创意设计建议等功能。界面采用现代渐变设计，用户体验流畅。',
        'cover_image': 'works/covers/coding_cover.png',
        'media_file': 'works/covers/coding_cover.png',
    },
    {
        'title': 'Aura - 智能虚拟助手',
        'category': 'digital_human',
        'work_type': 'image',
        'student_name': '王芳',
        'description': '利用3D建模和AI技术打造的虚拟数字人形象。具有友好的外观设计和自然的表情系统，可用于客服、教育等多个场景。',
        'cover_image': 'works/covers/digital_human_cover.png',
        'media_file': 'works/covers/digital_human_cover.png',
    },
    {
        'title': 'AI代码助手 - CodeMate',
        'category': 'programming',
        'work_type': 'link',
        'student_name': '刘强',
        'description': '开发的AI编程辅助工具，可以帮助程序员自动生成代码、检查bug、优化性能。支持多种主流编程语言。',
        'cover_image': 'works/covers/coding_cover.png',
        'content_url': 'https://github.com',
    },
]

for work_data in sample_works:
    Work.objects.create(**work_data)
    print(f'创建作品: {work_data["title"]}')

print('\n示例数据创建完成！')
print(f'共创建 {Work.objects.count()} 个作品')
