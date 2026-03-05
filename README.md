# Notes App - CI/CD + Docker + Kubernetes (K3s)

A simple Flask-based Notes Web Application deployed using a full DevOps pipeline.

## 🏗️ Project Overview

This project demonstrates a real-world CI/CD workflow:

- Code hosted on GitHub
- Jenkins automatically builds on every commit
- Docker image is built and tested
- Image imported into K3s (lightweight Kubernetes)
- Application deployed using Kubernetes Deployment + NodePort Service

## 🚀 Tech Stack

| Layer            | Tools Used            |
| ---------------- | --------------------- |
| Application      | Python Flask + SQLite |
| CI/CD            | Jenkins Pipeline      |
| Containerization | Docker                |
| Orchestration    | Kubernetes (K3s)      |
| OS               | RHEL / CentOS VM      |
| Source Control   | GitHub                |

## 💻 Run Locally

pip install -r requirements.txt
python app.py

shell
Copy code

## 🐳 Build & Run with Docker

docker build -t notes-app .
docker run -p 5000:5000 notes-app

shell
Copy code

## ☸️ Kubernetes Deployment

kubectl apply -f k8s/
kubectl get svc notes-app-service

shell
Copy code

## 🌍 Access the App

http://<VM-IP>:<NodePort>

makefile
Copy code

Example:
http://172.16.2.40:32355
<img width="1366" height="768" alt="noteapp_screenShot" src="https://github.com/user-attachments/assets/f016f771-232d-4d96-8860-64b996e1750e" />

shell
Copy code

## 🧑‍💻 Author

RAHUL JAISWAL
