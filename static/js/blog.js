document.addEventListener("DOMContentLoaded", function () {
    fetchPosts();

    const createPostForm = document.getElementById("createPostForm");
    if (createPostForm) {
        createPostForm.addEventListener("submit", handlePostSubmit);
    }
});

// 🔹 Fetch posts from Django API
function fetchPosts() {
    fetch('/api/posts/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('posts-container');
            container.innerHTML = '';

            if (data.posts.length === 0) {
                container.innerHTML = '<p>No posts available.</p>';
                return;
            }

            data.posts.forEach(post => {
                const postElement = document.createElement('article');
                postElement.classList.add('post');
                postElement.innerHTML = `
                    <div class="post-header">
                        <h2 class="post-title">${post.title}</h2>
                        <div class="author-info">
                            <span class="author-name">By ${post.author.username}</span>
                            <span class="post-meta">on ${new Date(post.created_at).toLocaleString()}</span>
                        </div>
                    </div>
                    <div class="post-content">
                        <p>${post.content.replace(/\n/g, '<br>')}</p>
                    </div>
                `;
                container.appendChild(postElement);
            });
        })
        .catch(error => console.error("Error fetching posts:", error));
}

// 🔹 Handle New Post Submission via AJAX
function handlePostSubmit(event) {
    event.preventDefault(); // Prevent full page reload

    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/blog/create/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken // ✅ Include CSRF Token
        },
        body: JSON.stringify({ title, content })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            closeModal();
            fetchPosts(); // ✅ Refresh posts dynamically
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error("Error creating post:", error));
}

// 🔹 Open & Close Modal
function openModal() {
    document.getElementById('createPostModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('createPostModal').style.display = 'none';
    document.getElementById('createPostForm').reset();
}
