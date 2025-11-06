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
| Layer | Tools Used |
|------|------------|
| Application | Python Flask + SQLite |
| CI/CD | Jenkins Pipeline |
| Containerization | Docker |
| Orchestration | Kubernetes (K3s) |
| OS | RHEL / CentOS VM |
| Source Control | GitHub |

## 📦 Run Locally (Optional)
