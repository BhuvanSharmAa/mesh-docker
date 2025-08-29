# Mesh Demo: Microservice Observability & Resilience Overview

This project is a mini service mesh demo with two microservices running on Kubernetes.

## Services

* **Service A:** Acts as a client/load generator.
* **Service B:** Backend service exposing business logic (`/work`) and Prometheus metrics (`/metrics`).

## Project Goal

The goal is to demonstrate:

* Microservice interaction
* Fault injection and resilience testing
* Metrics collection for observability

## Features

### Service B

* `/work` endpoint returns `{"result":"ok"}`.
* `/metrics` endpoint exposes Prometheus metrics:
    * `service_b_requests_total`
    * `service_b_latency_seconds`
    * `service_b_errors_total`
* Supports fault injection via environment variables:
    * `LAT_MS`: artificial latency in ms
    * `ERR_RATE`: error rate (0-1)

### Service A

* Calls Service B internally via Kubernetes DNS.
* Generates load for metrics and testing.

### Controller (`controller.py`)

* Monitors services using `policy.yaml`.
* Performs self-healing/remediation actions.

