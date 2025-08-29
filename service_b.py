from flask import Flask, jsonify
import os, time, random
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Metrics
REQ_COUNT = Counter("service_b_requests_total", "Total requests to service B")
REQ_LATENCY = Histogram("service_b_latency_seconds", "Latency of requests to service B")
REQ_ERRORS = Counter("service_b_errors_total", "Total error responses from service B")

# Configurable fault injection
LAT_MS = int(os.getenv("LAT_MS", "0"))      
ERR_RATE = float(os.getenv("ERR_RATE", "0")) 
@app.route("/work")
def work():
    REQ_COUNT.inc()
    start = time.time()

    if LAT_MS > 0:
        time.sleep(LAT_MS / 1000.0)

    if ERR_RATE > 0 and random.random() < ERR_RATE:
        REQ_ERRORS.inc()
        return jsonify({"error": "simulated failure"}), 500

    REQ_LATENCY.observe(time.time() - start)
    return jsonify({"result": "ok"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
