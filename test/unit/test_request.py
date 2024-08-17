from domain import request


def test_add_payload_request():
    obj = request.PayloadRequest(
        list_1=["first_string", "second_string", "third_string"],
        list_2=["fourth_string", "fifth_string"],
    )

    assert obj.list_1 == ["first_string", "second_string", "third_string"]
    assert obj.list_2 == ["fourth_string", "fifth_string"]
