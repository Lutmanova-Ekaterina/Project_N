import json

def get_category_list(data):
    with open('../data/catalog.json', 'r', encoding='utf-8') as file:
        file_catalog = json.load(file)
        for i in file_catalog:
            print(f"{i['id']}, {i['name']}")
            return {
                "code": 200,
                "data": '\n'.join(data)
            }
    return {
            "code": 400,
            "data": "Some error"
        }
get_category_list({
    "action": 3,
    "data": {}
})