def json_reader(file_name):
    import json
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return json.loads(content)
    except Exception:
        return



# print(json_reader('test'))
