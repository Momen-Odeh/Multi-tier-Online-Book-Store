
api_cache = {}


def get_from_cache(key):
    data = api_cache.get(key, None)
    print("get data: ", data)
    return data


def add_data_to_cache(key, value):
    api_cache[key] = value
    print("add data: ", value)


def delete_data_from_cache(key):
    api_cache.pop(key, None)
    print("delete data: ", key)
