import requests

def get_age(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    data = response.json()
    return data["age"]

def get_gender(name):
    response = requests.get(f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    data = response.json()
    return data["gender"]

def get_blogs():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()
    return data
    