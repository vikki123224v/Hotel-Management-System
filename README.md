# ☁️ CloudNest HMS

**CloudNest Hotel Management System** is a premium, cloud-native application designed for modern hospitality. Built with **Python Flask**, **MySQL**, and **Docker**, it demonstrates a scalable microservices-based architecture with a stunning user interface.

![CloudNest Logo](https://img.icons8.com/color/96/cloud-checked.png)

## ✨ Features

### 👑 Premium Experience
- **Stunning UI**: Modern glassmorphism design with premium animations and micro-interactions.
- **Responsive Layout**: Designed for seamless experience across all devices.

### 🔐 Advanced Security & Auth
- **Role-Based Access Control (RBAC)**: Separate flows for Admins and Customers.
- **Secure Sessions**: Protected by robust hashing (Werkzeug/Scrypt) and secret keys.

### 🏨 Full CRUD Management (Admin)
- **Room Control**: Add, Edit, or Delete rooms with real-time status updates.
- **Booking Oversight**: View and manage all guest reservations globally.

### ☁️ Cloud-Native Architecture
- **Containerized**: Fully orchestrated using Docker and Docker Compose.
- **API-First**: RESTful API layer for stateless communication.
- **Event-Driven Simulation**: Integrated Pub/Sub notification patterns for reliable processing.

---

## 🚀 Quick Start

### 1. Prerequisites
- Docker & Docker Compose installed.
- (Optional) Python 3.10+ for local development.

### 2. Configuration
Create a `.env` file in the root directory (or copy from `.env.example`):
```bash
cp .env.example .env
```
Update the `.env` with your preferred database credentials and a secure `SECRET_KEY`.

### 3. Deploy everything
Run the automated deployment script:
```bash
bash deploy/deploy.sh
```
Or start manually:
```bash
docker-compose up --build -d
```

### 4. Access
- **Application**: [http://localhost:5000](http://localhost:5000)
- **Admin Dashboard**: Login with `admin` / `admin123` (default dev credentials).

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask, Flask-MySQLdb
- **Database**: MySQL 8.0
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), JS
- **DevOps**: Docker, Docker Compose

---
© 2026 CloudNest. Built for the Modern Cloud.
