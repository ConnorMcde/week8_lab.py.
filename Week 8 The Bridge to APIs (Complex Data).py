"""Week 8 exercise 3 The Bridge to APIs (Complex Data)"""


fake_api_data = {
"status": "success",
"total_results": 2,
"users": [
{"id": 1, "name": "John", "contact": {"email": "john@test.com"}},
{"id": 2, "name": "Jane", "contact": {"email": "jane@test.com"}}
]
}


print(f"{fake_api_data['users'][1]['contact']}")
