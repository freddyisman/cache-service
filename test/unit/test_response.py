from domain import response


def test_add_payload_response():
    obj = response.AddPayloadResponse(
        data={"key": "value"},
        status=201,
        message="Payload added successfully",
    )

    assert obj.data == {"key": "value"}
    assert obj.status == 201
    assert obj.message == "Payload added successfully"


def test_get_payload_response():
    obj = response.GetPayloadResponse(
        data={"key": "value"},
        status=200,
        message="Payload retrieved successfully",
    )

    assert obj.data == {"key": "value"}
    assert obj.status == 200
    assert obj.message == "Payload retrieved successfully"
