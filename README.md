not_a_server_error. The response has 5xx HTTP status;

status_code_conformance. The response status is not defined in the API schema;

content_type_conformance. The response content type is not defined in the API schema;

response_schema_conformance. The response content does not conform to the schema defined for this specific response;

negative_data_rejection. The API accepts data that is invalid according to the schema;

response_headers_conformance. The response headers does not contain all defined headers.

use_after_free. The API returned a non-404 response a successful DELETE operation on a resource. NOTE: Only enabled for new-style stateful testing.