import schemathesis
import requests

schema = schemathesis.from_path("openapi.yaml")

@schema.parametrize()
def test_api(case):
    response = case.call()
    case.validate_response(response)
