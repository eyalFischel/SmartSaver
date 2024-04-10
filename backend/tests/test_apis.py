import requests

def test_example():
    response = requests.post("http://localhost:8000/example")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
