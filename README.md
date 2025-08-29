Mesh Demo: Microservice Observability & Resilience
Overview

This project is a mini service mesh demo built with two microservices running on Kubernetes:

Service A: Acts as a client/load generator.

Service B: Backend service exposing business logic (/work) and Prometheus metrics (/metrics).

The goal is to demonstrate:

Microservice interaction

Fault injection and resilience testing

Metrics collection for observability

Features

Service B:

/work endpoint returns {"result":"ok"}

/metrics endpoint exposes Prometheus metrics:

service_b_requests_total

service_b_latency_seconds

service_b_errors_total

Supports fault injection via environment variables:

LAT_MS: artificial latency in ms

ERR_RATE: error rate (0-1)

Service A:

Calls Service B internally via Kubernetes DNS

Generates load for metrics and testing

Controller (controller.py):

Monitors services using policy.yaml

Performs self-healing/remediation actions

Project Structure
project-root/
├─ .venv/
├─ .vscode/
├─ k8s/
│   └─ deployment.yaml
├─ manifests/
│   ├─ service-b.yaml
│   └─ service-a.yaml
├─ Dockerfile.service
├─ Dockerfile.service_a
├─ requirements.txt
├─ service_b.py
├─ service_a.py
├─ controller.py
├─ policy.yaml
├─ envoy.yaml
└─ envoy_cb.yaml

Prerequisites

Docker Desktop (Windows/Linux/macOS)

kind (Kubernetes in Docker)

kubectl

Python 3.11+

Virtual environment (.venv) with dependencies:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Setup & Run
1. Build Docker Images
docker build -t service-b:latest -f Dockerfile.service .
docker build -t service-a:latest -f Dockerfile.service_a .

2. Create kind Cluster
kind create cluster --name mesh-demo

3. Load Docker Images into kind
kind load docker-image service-b:latest --name mesh-demo
kind load docker-image service-a:latest --name mesh-demo

4. Deploy Services
kubectl apply -f manifests/service-b.yaml
kubectl apply -f manifests/service-a.yaml
kubectl get pods -w

5. Test Service B
kubectl port-forward svc/service-b 5000:5000
curl http://127.0.0.1:5000/work
curl http://127.0.0.1:5000/metrics

6. Verify Service A → Service B
kubectl exec -it <service-a-pod-name> -- curl http://service-b:5000/work

Next Steps

Add fault injection to Service B:

env:
  - name: LAT_MS
    value: "200"
  - name: ERR_RATE
    value: "0.2"


Run controller.py to monitor and remediate failures.

Integrate Prometheus or a ServiceMonitor to scrape metrics automatically.

Visualize metrics with Grafana.

Skills Demonstrated

Python microservices (Flask)

Docker & Kubernetes deployment

Prometheus metrics and observability

Fault injection & resilience testing

Service mesh concepts