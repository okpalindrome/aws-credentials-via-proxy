import requests
import os
import sys
import time

target = sys.argv[1]

if not os.path.isfile(target):
    print(f"{target} does not exists")
    exit(1)

file = open(target, "r")
subdomains = file.readlines()

for subdomain in subdomains:
    subdomain = subdomain.rstrip("\n")

    session = requests.Session()
    headers = {"Host":"aws.ca.fi"}

    try:
        awscheck_http = session.get(f"http://{subdomain}", headers=headers)
        print(f"[Info] - http://{subdomain}")
        time.sleep(0.5)
        awscheck_https = session.get(f"https://{subdomain}", headers=headers)
        print(f"[Info] - https://{subdomain}")
    except requests.exceptions.RequestException as e:
        continue

    if awscheck_http.status_code == 200:
        print(f"[Positive] - {subdomain} - please manually verify!")
        print(f"run: curl -ik -H \"Host:aws.ca.fi\" http://{subdomain}/latest/meta-data/")

    elif awscheck_https.status_code == 200:
        print(f"[Positive] - {subdomain} - please manually verify!")
        print(f"run: curl -ik -H \"Host:aws.ca.fi\" https://{subdomain}/latest/meta-data/")

file.close()
print("[completed] - Scanned all subdomains")
