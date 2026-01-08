# Good Craft - 学员优秀作品展示系统

一个用于展示学员AI创作优秀作品的Django Web应用，支持多种作品类型和分类展示。

![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ 特性

- 🎨 **多模态作品展示** - 支持图片、视频、网页链接等多种作品类型
- 📂 **智能分类** - AI多模态创作、AI编程应用、AI数字人三大分类
- 🎯 **动态筛选** - 前端动态切换分类无需刷新页面
- 📱 **响应式设计** - 适配桌面和移动设备
- 🔐 **后台管理** - 基于Django Admin的便捷作品管理系统
- 🎬 **弹窗预览** - 点击作品卡片在弹窗中预览详细内容

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip
- virtualenv (推荐)

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd good-craft
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **数据库迁移**
   ```bash
   python manage.py migrate
   ```

5. **创建超级用户（可选）**
   ```bash
   python manage.py createsuperuser
   ```

6. **创建示例数据（可选）**
   ```bash
   python create_sample_data.py
   ```

7. **启动开发服务器**
   ```bash
   python manage.py runserver
   ```

8. **访问应用**
   - 前台展示页面: http://127.0.0.1:8000/
   - 后台管理: http://127.0.0.1:8000/admin/

## 📁 项目结构

```
good-craft/
├── config/              # Django项目配置
│   ├── settings.py     # 项目设置
│   ├── urls.py         # 路由配置
│   └── wsgi.py         # WSGI入口
├── showcase/           # 作品展示应用
│   ├── models.py       # 数据模型
│   ├── views.py        # 视图函数
│   ├── admin.py        # 后台管理配置
│   ├── templates/      # 模板文件
│   └── static/         # 静态文件（CSS/JS）
├── media/              # 用户上传文件
├── docs/               # 项目文档
│   ├── images/         # 文档图片资源
│   └── BUGFIX_*.md     # 问题修复记录
├── requirements.txt    # Python依赖
└── manage.py          # Django管理脚本
```

## 🎯 核心功能

### 作品分类

- **AI多模态创作** - 展示AI生成的图片、视频等多模态创作作品
- **AI编程应用** - 展示学员开发的AI相关应用和项目
- **AI数字人** - 展示数字人相关的创作作品

### 作品类型

每个作品支持以下类型：
- 📷 **图片** - 单张或多张图片展示
- 🎬 **视频** - 视频作品展示
- 🔗 **网页链接** - 在线应用或项目链接

### 数据模型

核心模型是 `Work`（作品），包含以下字段：
- `title` - 作品标题
- `category` - 作品分类（multimodal/programming/digital_human）
- `work_type` - 作品类型（image/video/link）
- `student_name` - 学员姓名
- `description` - 作品描述
- `cover_image` - 封面图片（必填）
- `media_file` - 媒体文件（图片/视频）
- `content_url` - 网页链接
- `is_published` - 是否发布
- `order` - 排序权重

## 🛠️ 后台管理

访问 `/admin/` 进行作品管理：

1. 使用超级用户账号登录
2. 进入"学员作品"管理页面
3. 可以添加、编辑、删除作品
4. 支持批量操作和筛选

### 添加作品注意事项

- **封面图片**（必填）：作品在列表页显示的封面
- **作品类型**：
  - 选择"图片"或"视频"时，上传对应的媒体文件
  - 选择"网页链接"时，填写内容URL
- **排序权重**：数字越大，作品越靠前显示

## 📖 文档中心

### 核心文档
- [🏗️ 系统架构](docs/architecture.md) - 系统设计、组件图与数据模型
- [🚀 部署指南](docs/deployment.md) - 生产环境部署手册 (Nginx/Gunicorn)
- [📘 开发者指南](docs/development.md) - 开发环境搭建与贡献流程
- [👥 用户操作手册](docs/user_guide.md) - 后台管理系统使用说明
- [📜 更新日志](CHANGELOG.md) - 版本历史与变更记录

### 问题记录
- [🐛 模板渲染Bug修复](docs/BUGFIX_TEMPLATE_RENDERING.md) - 修复记录

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📝 许可证

MIT License

## 🔧 技术栈

- **后端框架**: Django 5.1.4
- **数据库**: SQLite (开发环境)
- **前端**: 原生 HTML/CSS/JavaScript
- **图片处理**: Pillow
- **部署**: 支持多种WSGI服务器（Gunicorn, uWSGI等）

## 📞 联系方式

如有问题或建议，欢迎通过Issue联系。
