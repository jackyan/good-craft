# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-01-08

### Fixed
- **Template Rendering Bug**: Fixed an issue where literal Django template tags (`{{ ... }}`) were displayed on work type badges instead of the rendered values. The root cause was a newline character within the template tag in `index.html`.

### Added
- **Comprehensive Documentation**:
    - `docs/architecture.md`: System design and diagrams.
    - `docs/deployment.md`: Production deployment guide (Nginx/Gunicorn).
    - `docs/user_guide.md`: Admin manual for content management.
    - `docs/development.md`: Developer setup and contribution guide.
- **Documentation Images**: Added screenshots and verification recordings to `docs/images/`.

## [1.0.0] - 2026-01-07

### Added
- Initial release of Good Craft.
- **Showcase Module**:
    - Support for multiple work categories (Multimodal, Programming, Digital Human).
    - Support for different work types (Image, Video, Link).
    - Responsive grid layout for work cards.
    - Detail modal for viewing work information.
- **Admin Interface**: Customized Django Admin for managing `Work` models.
- **Sample Data**: Script `create_sample_data.py` to populate initial content.
