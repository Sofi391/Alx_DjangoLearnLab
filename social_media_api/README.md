Social Media API

A simple Django REST Framework API for user registration, login, and profile management.

Features

Custom user model with username, email, bio, profile picture, and followers

User registration with password confirmation

Token-based authentication for secure login

Retrieve user profiles by username

Setup

Clone the repository and create a virtual environment

Install dependencies

Apply migrations and create a superuser if needed

Run the development server

API Endpoints

Register: Create a new user and receive an authentication token

Login: Obtain token using username and password

Profile: Retrieve user profile by username

User Model Overview

username and email are unique identifiers

password is stored securely (hashed)

bio and profile_picture are optional

followers is a many-to-many relationship to other users

Social Media API — Posts & Comments
Posts

List Posts: GET /posts/
Supports search: ?search=keyword
Supports ordering: ?ordering=created_at or ?ordering=-created_at
Pagination applied: ?page=1

Create Post: POST /posts/
Required fields: title, content
Author is automatically assigned (authenticated user)

Retrieve Post: GET /posts/<id>/

Update Post: PUT /posts/<id>/
Only the post author can update

Delete Post: DELETE /posts/<id>/
Only the post author can delete

Comments

List Comments: GET /comments/
Supports search: ?search=keyword
Pagination applied: ?page=1

Create Comment: POST /comments/
Required fields: post (Post ID), content
Author is automatically assigned (authenticated user)

Retrieve Comment: GET /comments/<comment_id>/

Update Comment: PUT /comments/<comment_id>/
Only the comment author can update

Delete Comment: DELETE /comments/<comment_id>/
Only the comment author can delete


User Follow & Feed Features

Follow / Unfollow Users:

Users can follow or unfollow other users.

Endpoint updates the current user’s following list.

Users cannot follow/unfollow themselves.

Feed:

Displays posts from users the current user follows.

Posts are ordered by creation date, newest first.

Helps users stay updated with content from followed accounts.

Changes to User Model:

Added following field (ManyToMany to User) to track users being followed.

Added followers field (ManyToMany to User) to track users following the account.

Usage Notes:

Only authenticated users can follow/unfollow or access the feed.

Feed does not include posts from users the current user does not follow.

Like Posts: Users can like and unlike posts. Each like is unique per user per post.

Notifications: Users receive notifications when:

Someone likes their post

They get a new follower

Someone comments on their post

These features enhance user engagement and interaction on the platform.