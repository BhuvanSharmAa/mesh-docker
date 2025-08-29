import time
import requests
import yaml

POLICY_FILE = "policy.yaml"

def load_policies():
    with open(POLICY_FILE) as f:
        return yaml.safe_load(f)

def check_service(service_url):
    try:
        r = requests.get(service_url, timeout=2)
        return r.status_code == 200
    except:
        return False

def remediate(service_url, action):
    print(f"Remediating {service_url} with action: {action}")

if __name__ == "__main__":
    policies = load_policies()
    while True:
        for service, policy in policies.items():
            if not check_service(policy["url"]):
                remediate(service, policy["action"])
        time.sleep(5)
