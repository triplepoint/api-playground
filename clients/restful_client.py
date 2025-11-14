import requests

if __name__ == "__main__":
    r = requests.get("http://localhost:8008/restful/pets/scruffy")
    print(r.json())
