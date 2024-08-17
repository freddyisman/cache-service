from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_add_and_read():
    body = {
        "list_1": ["first_string", "second_string", "third_string"],
        "list_2": ["fourth_string", "fifth_string"],
    }
    transformed_value = ", ".join(body["list_1"] + body["list_2"]).upper()

    # test add
    response = client.post(
        "/payload",
        json=body,
    )

    content = response.json()
    assert content["data"]["value"] == transformed_value
    assert content["status"] == 201
    assert content["message"] == "Payload added successfully"

    payload_id = content["data"]["id"]
    # test read and cache
    for _ in range(2):
        response = client.get(
            f"/payload/{payload_id}",
        )

        content = response.json()
        assert content["data"]["id"] == payload_id
        assert content["data"]["value"] == transformed_value
        assert content["status"] == 200
        assert content["message"] == "Payload retrieved successfully"
