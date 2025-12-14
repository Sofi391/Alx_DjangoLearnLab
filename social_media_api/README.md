# Social Media API

A simple **Django REST Framework** API for user registration, login, profile management, posts, comments, likes, follows, and notifications.

---

## Live Demo

[View Live App](https://your-live-link.com)

---

## Features

- **Custom User Model:** username, email, bio, profile picture, followers/following  
- **Authentication:** Token-based login & registration  
- **Posts & Comments:** Create, read, update, delete with search, ordering, and pagination  
- **Follow/Unfollow:** Users can follow/unfollow others and see a personalized feed  
- **Likes & Notifications:** Like/unlike posts, receive notifications for likes, new followers, and comments  

---

## Setup

1. Clone the repository  
2. Create a virtual environment  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
   
---

## API Endpoints Overview

### Users
- **Register:** `POST /register/`
- **Login:** `POST /login/`
- **Profile:** `GET /profile/<username>/`

### Posts
- **List:** `GET /posts/` (supports search & ordering)
- **Create:** `POST /posts/`
- **Retrieve/Update/Delete:** `GET | PUT | DELETE /posts/<id>/`

### Comments
- **List:** `GET /comments/`
- **Create:** `POST /comments/`
- **Retrieve/Update/Delete:** `GET | PUT | DELETE /comments/<comment_id>/`

### Follow & Feed
- **Follow/Unfollow:** `POST /follow/<user_id>/`, `POST /unfollow/<user_id>/`
- **Feed:** `GET /feed/`

### Likes & Notifications
- **Like/Unlike Post:** `POST /posts/<post_id>/like/`, `POST /posts/<post_id>/unlike/`
- **View Notifications:** `GET /notifications/`

---

## Notes
- Only authenticated users can follow/unfollow, like posts, or access the feed.
- Notifications enhance engagement by alerting users to interactions on their posts.

---

## 👩‍💻 About the Developer

Hi! I’m Sofi, a Software Engineering student at **AASTU** and an **ALX Backend Program participant**.  
I’m passionate about Python, web development, and creating full-stack applications that are both functional and user-friendly.

### 🤳 Connect with me:
[<img align="left" alt="LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="GitHub" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />][github] 
