# 部署指南

本指南将指导你如何将 Good Craft 部署到生产环境。

## 1. 生产环境要求

- **操作系统**: Linux (Ubuntu 20.04/22.04 推荐) 或 macOS/Windows Server
- **Python**: Python 3.8+
- **数据库**: PostgreSQL (推荐生产环境使用) 或 SQLite (仅限小规模使用)
- **Web 服务器**: Nginx 或 Apache
- **应用服务器**: Gunicorn 或 uWSGI

## 2. 部署前准备

### 2.1 依赖安装

在生产服务器上克隆代码并安装依赖：

```bash
git clone <repository-url>
cd good-craft
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn  # 生产环境需要额外的应用服务器
```

### 2.2 环境变量与安全配置

在生产环境中，**切勿**直接修改 `settings.py` 中的敏感信息。推荐使用环境变量。

你需要确保 `config/settings.py` 中的以下配置针对生产环境进行了调整：

1.  **关闭调试模式**:
    ```python
    DEBUG = False
    ```
    > [!WARNING]
    > 生产环境必须将 `DEBUG` 设置为 `False`，否则会泄露敏感配置信息。

2.  **设置 ALLOWED_HOSTS**:
    ```python
    ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '127.0.0.1']
    ```

3.  **生成新的 SECRET_KEY**:
    不要使用代码库中默认的密钥。可以通过以下 Python 命令生成新的密钥：
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```

### 2.3 静态文件收集

生产环境下，Django 不会直接提供静态文件服务。需要收集所有静态文件到一个目录，由 Nginx 提供服务。

```bash
python manage.py collectstatic
```
这会将所有静态文件复制到 `STATIC_ROOT` 指定的目录（通常是 `staticfiles/`）。

## 3. 数据库迁移

如果是首次部署：

```bash
python manage.py migrate
```

## 4. Gunicorn 配置示例

使用 Gunicorn 启动应用：

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

- `config.wsgi:application` 指向项目的 WSGI 入口。
- `--workers` 建议设置为 CPU 核心数 * 2 + 1。

## 5. Nginx 配置示例

建议使用 Nginx 作为反向代理服务器，处理静态文件并转发请求给 Gunicorn。

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 静态文件服务
    location /static/ {
        alias /path/to/good-craft/staticfiles/;
    }

    # 媒体文件服务 (用户上传)
    location /media/ {
        alias /path/to/good-craft/media/;
    }

    # 转发请求给 Gunicorn
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 6. Docker 部署 (可选)

如果偏好容器化部署，可以参考以下 `Dockerfile` 示例：

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

# 收集静态文件
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 7. 常见问题排查

- **静态文件 404**: 检查 Nginx 的 `/static/` alias 路径是否正确，以及是否执行了 `collectstatic`。
- **媒体文件无法访问**: 检查 `media/` 目录的权限，确保 Nginx 运行用户有读取权限。
- **Server Error (500)**: 检查 Gunicorn 的错误日志。如果此时 `DEBUG=False`，Django 不会显示具体的错误栈信息。
