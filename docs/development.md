# 开发者指南

欢迎加入 Good Craft 项目开发！本文档将帮助你快速搭建开发环境并参与贡献。

## 1. 开发环境搭建

### 1.1 前置要求

- Python 3.8 或更高版本
- Git

### 1.2 初始配置

1. **克隆代码库**
   ```bash
   git clone <repository-url>
   cd good-craft
   ```

2. **创建并激活虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 或 venv\Scripts\activate  (Windows)
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **数据库初始迁移**
   ```bash
   python manage.py migrate
   ```

5. **创建超级用户** (用于登录后台)
   ```bash
   python manage.py createsuperuser
   ```

6. **生成测试数据** (可选)
   ```bash
   python create_sample_data.py
   ```

7. **启动开发服务器**
   ```bash
   python manage.py runserver
   ```
   访问 http://127.0.0.1:8000/ 查看效果。

## 2. 代码规范

- **Python**: 遵循 [PEP 8](https://peps.python.org/pep-0008/) 规范。
- **HTML/CSS**: 保持缩进一致（建议 4 空格或 2 空格），类名使用 kebab-case（如 `work-card`）。
- **注释**: 复杂逻辑请添加注释，公共函数和类请添加 Docstring。

## 3. 项目结构说明

- `config/`: 项目级配置。添加新 App 时需在 `settings.py` 中注册。
- `showcase/`: 主要业务 App。
    - `models.py`: 任何数据结构的变更都需要运行 `makemigrations` 和 `migrate`。
    - `static/showcase/`: 存放 JS/CSS 图片等静态资源。
    - `templates/showcase/`: 存放 HTML 模板。

## 4. 常用命令速查

- **创建迁移文件**: `python manage.py makemigrations`
- **应用迁移**: `python manage.py migrate`
- **收集静态文件**: `python manage.py collectstatic`
- **进入 Shell**: `python manage.py shell`

## 5. 贡献流程

1. Fork 本仓库。
2. 基于 `main` 分支创建特性分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 提交 Pull Request。
