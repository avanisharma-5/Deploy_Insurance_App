# Deploy Insurance App to Kubernetes

A complete DevOps implementation for containerizing and deploying an Insurance Application onto a Kubernetes cluster (Minikube) using Docker, GitHub Actions- CI/CD.

---

## Project Overview

This project takes an Insurance Application and deploys it to a production-ready Kubernetes environment. The deployment is fully automated — a single `git push` triggers the entire build, push, and deploy pipeline.


---

## Key Features

- Automated CI/CD pipeline triggered on every `git push`
- Zero-downtime Rolling Updates using Kubernetes Deployment strategy
- Docker containerization with versioned image tagging for full rollback support
- Deployed on Kubernetes (Minikube) with self-healing pod management
- Kubernetes Service exposes the application through a stable external endpoint
- All credentials managed via CI/CD secrets — nothing stored in code or images
- Docker layer caching for faster repeated builds in the pipeline

---

## Tech Stack

| Category | Technology |
|---|---|
| Application | Insurance Web Application |
| Containerization | Docker, Docker Hub |
| Orchestration | Kubernetes (Minikube) |
| CI/CD | GitHub Actions |
| Version Control | Git, GitHub |
| Cluster Management | kubectl, Minikube CLI |

---

## Project Structure

```
Deploy-Insurance-App-to-Kubernetes/
│
├── Dockerfile                        # Defines runtime environment and app dependencies
├── requirements.txt                  # Application dependencies
├── .dockerignore                     # Files excluded from Docker build context
│
├── k8s/
│   ├── deployment.yaml               # Pods, replicas, rolling update strategy config
│   └── service.yaml                  # NodePort/LoadBalancer service for external access
│
└── .github/
    └── workflows/
        └── deploy.yml                # Full CI/CD pipeline definition (GitHub Actions)
```

---

## System Architecture

```
Developer  →  GitHub Repository  →  CI/CD Pipeline ( GitHub Actions)
                                              ↓
                                    Build Docker Image
                                              ↓
                                    Push to Docker Hub
                                              ↓
                               Kubernetes Cluster (Minikube)
                                              ↓
                           Insurance App Pods  →  K8s Service  →  End User
```

---

## Deployment Steps

Follow these steps to deploy this project from scratch.

**Prerequisites**
- Docker Desktop installed and running
- Minikube installed and configured
- kubectl installed
- Docker Hub account
- GitHub account with access to this repository

**Step 1 — Clone this repository**
```bash
git clone https://github.com/avanisharma-5/Deploy_Insurance_App.git
cd Deploy-Insurance-App-to-Kubernetes
```

**Step 2 — Start Minikube**
```bash
minikube start --driver=docker
kubectl get nodes
```

Verify the node is in `Ready` state before proceeding.

**Step 3 — Build and push the Docker image**
```bash
docker build -t <your-dockerhub-username>/insurance-app:latest .
docker login
docker push <your-dockerhub-username>/insurance-app:latest
```

**Step 4 — Add CI/CD Secrets**

Go to your GitHub repo → Settings → Secrets and variables → Actions and add these secrets:
```
DOCKER_USERNAME        → your Docker Hub username
DOCKER_PASSWORD        → your Docker Hub access token
```

**Step 5 — Apply Kubernetes manifests**
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

**Step 6 — Push to trigger the pipeline**
```bash
git push origin main
```

Go to the Actions tab on GitHub and watch all stages complete. The pipeline builds the image, pushes to Docker Hub, and deploys to Minikube automatically.

**Step 7 — Access the application**
```bash
minikube service insurance-app-service
```

Minikube will open the application URL directly in your browser.

**Step 8 — Verify deployment**
```bash
kubectl get pods
kubectl get services
kubectl rollout status deployment/insurance-app
```

---

## CI/CD Pipeline Stages

```
Stage 1 — Checkout
  └─ Pull latest code from GitHub repository

Stage 2 — Docker Login
  └─ Authenticate with Docker Hub using stored CI/CD secrets

Stage 3 — Build Image
  └─ Build Docker image on CI runner using the Dockerfile
  └─ Docker layer caching applied to speed up repeated builds

Stage 4 — Push Image
  └─ Push versioned image to Docker Hub with unique tag for traceability

Stage 5 — Deploy
  └─ kubectl apply k8s/deployment.yaml
  └─ kubectl apply k8s/service.yaml

Stage 6 — Verify
  └─ kubectl rollout status — waits until all pods are healthy
  └─ kubectl get pods + services — confirms live deployment state
```

---



Docker image versioning on Docker Hub ensures every previous version remains available for rollback.

---

## Key Design Considerations

| Consideration | Implementation |
|---|---|

| Scalability | Replica count is adjustable; architecture supports HPA in future iterations |
| Reliability | Kubernetes self-healing auto-restarts crashed pods |
| Portability | Docker ensures consistent runtime across dev, test, and production environments |
| Security | Secrets encrypted in CI/CD; RBAC enforced on the cluster; no root privileges in containers |
| Efficient Resources | CPU and memory limits defined in deployment manifests |

---

## GitHub Secrets Required

Before the pipeline can run, these secrets must be added under Settings → Secrets and variables → Actions: `DOCKER_USERNAME` and `DOCKER_PASSWORD`.

---

## Related Repository

Insurance App Repository → https://github.com/avanisharma-5/Deploy_Insurance_App

---

## Group Members

| Sr No | Name | Enrollment Number |
|---|---|---|
| 01 | Ananya Madanala | EN22CS301119 |
| 02 | Anind Bilthariya | EN22CS301129 |
| 03 | Arpita Solanki | EN22CS301202 |
| 04 | Ashutosh Singh | EN22CS301221 |
| 05 | Avani Sharma | EN22CS301240 |

---

- **Institution** — Medicaps University, Datagami Skill Based Course
- **Academic Year** — 2025–2026
- **University Mentor** — Prof. Akshay Saxena
