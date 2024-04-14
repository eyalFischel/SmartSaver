from datetime import datetime
from tests.conftest import client


def test_transactions_api(client):
    route = "transactions"
    # Create
    transaction_data = {
        "id": "4",
        "client_id": "client_3",
        "transaction_amount": 250.0,
        "transaction_time": datetime(2024, 4, 13, 15, 30).isoformat(),
        "description": "Example transaction 4",
    }
    response = client.post(f"/{route}/", json=transaction_data)
    assert response.status_code == 200
    assert response.json() == transaction_data

    # Read
    response = client.get(f"/{route}/4")
    assert response.status_code == 200
    assert response.json() == transaction_data

    # Update
    updated_transaction_data = {
        "id": "4",
        "client_id": "client_3",
        "transaction_amount": 300.0,
        "transaction_time": datetime(2024, 4, 13, 16, 30).isoformat(),
        "description": "Updated example transaction 4",
    }
    response = client.put(f"/{route}/4", json=updated_transaction_data)
    assert response.status_code == 200
    assert response.json() == updated_transaction_data

    response = client.get(f"/{route}/4")
    assert response.status_code == 200
    assert response.json() == updated_transaction_data

    # Delete
    response = client.delete(f"/{route}/4")
    assert response.status_code == 200
    assert (
        response.json() == updated_transaction_data
    )  # Deleted transaction should match the last updated data
