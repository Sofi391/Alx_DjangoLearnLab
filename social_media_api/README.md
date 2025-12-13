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