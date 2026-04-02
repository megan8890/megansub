import requests
import os

GIST_ID = "59f91b32bf75f9ae613ff36a3c72ff6a"
TOKEN = os.environ.get("GIST_TOKEN")

with open("sub.txt", "r") as f:
    content = f.read()

url = f"https://api.github.com/gists/{GIST_ID}"

headers = {
    "Authorization": f"token {TOKEN}"
}

data = {
    "files": {
        "sub.txt": {
            "content": content
        }
    }
}

requests.patch(url, headers=headers, json=data)
