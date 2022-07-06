import re
import requests, json

data = '{"operationName":"FindResultDataByResult","variables":{"result_id":"c06fb779-2094-480a-8b09-c52696fe288d","error_id":"26700fee-61a6-44e3-8e3e-a5e0026ff791"},"query":"query FindResultDataByResult($result_id: uuid!, $error_id: uuid!) {\n  query_results(where: {id: {_eq: $result_id}}) {\n    id\n    job_id\n    runtime\n    generated_at\n    columns\n    __typename\n  }\n  query_errors(where: {id: {_eq: $error_id}}) {\n    id\n    job_id\n    runtime\n    message\n    metadata\n    type\n    generated_at\n    __typename\n  }\n  get_result_by_result_id(args: {want_result_id: $result_id}) {\n    data\n    __typename\n  }\n}\n"}'

res = requests.post('https://core-hsr.duneanalytics.com/v1/graphql', data).json()

with open('test', 'w+') as f:
    json.dump(res, f)
