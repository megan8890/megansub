import base64

with open("nodes.txt", "r") as f:
    data = f.read()

encoded = base64.b64encode(data.encode()).decode()

with open("sub.txt", "w") as f:
    f.write(encoded)
