import requests

def get_container_changes(container_id):
    url = f"http://localhost:2375/containers/{container_id}/changes"
    response = requests.get(url)
    return response.json()