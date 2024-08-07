import schemathesis
import requests

schema = schemathesis.from_path("openapi.yaml", base_url="http://localhost:5000")

@schema.parametrize()
def test_api(case):
    response = case.call()
    case.validate_response(response)
