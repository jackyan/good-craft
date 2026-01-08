// Tab 切换功能
function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.dataset.tab;

            // 移除所有激活状态
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            // 激活当前tab
            btn.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

// 模态框功能
function initModal() {
    const modal = document.getElementById('workModal');
    const modalClose = document.querySelector('.modal-close');
    const workCards = document.querySelectorAll('.work-card');

    workCards.forEach(card => {
        card.addEventListener('click', () => {
            const workId = card.dataset.workId;
            showWorkDetail(workId);
        });
    });

    modalClose.addEventListener('click', () => {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });

    // ESC键关闭
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
}

function showWorkDetail(workId) {
    const card = document.querySelector(`[data-work-id="${workId}"]`);
    const modal = document.getElementById('workModal');

    // 获取作品数据
    const title = card.dataset.title;
    const student = card.dataset.student;
    const type = card.dataset.type;
    const typeDisplay = card.dataset.typeDisplay;
    const category = card.dataset.category;
    const description = card.dataset.description;
    const coverUrl = card.dataset.cover;
    const mediaUrl = card.dataset.media;
    const contentUrl = card.dataset.url;

    // 更新模态框内容
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalStudent').textContent = student;
    document.getElementById('modalType').textContent = typeDisplay;
    document.getElementById('modalCategory').textContent = category;

    if (description) {
        document.getElementById('modalDescription').textContent = description;
        document.getElementById('modalDescription').style.display = 'block';
    } else {
        document.getElementById('modalDescription').style.display = 'none';
    }

    const modalMediaContainer = document.getElementById('modalMediaContainer');
    modalMediaContainer.innerHTML = '';

    // 根据类型显示不同内容
    if (type === 'video') {
        const video = document.createElement('video');
        video.className = 'modal-media';
        video.controls = true;
        video.src = mediaUrl;
        modalMediaContainer.appendChild(video);
    } else if (type === 'image') {
        const img = document.createElement('img');
        img.className = 'modal-media';
        img.src = mediaUrl;
        img.alt = title;
        modalMediaContainer.appendChild(img);
    } else if (type === 'link') {
        const img = document.createElement('img');
        img.className = 'modal-media';
        img.src = coverUrl;
        img.alt = title;
        modalMediaContainer.appendChild(img);
    }

    // 显示/隐藏链接按钮
    const linkBtn = document.getElementById('modalLinkBtn');
    if (contentUrl) {
        linkBtn.href = contentUrl;
        linkBtn.style.display = 'inline-block';
    } else {
        linkBtn.style.display = 'none';
    }

    // 显示模态框
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    initModal();

    // 添加滚动动画
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.work-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(card);
    });
});
