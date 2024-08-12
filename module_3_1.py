calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False

print(string_info('Phone'))
print(string_info('water'))
print(is_contains('dow', ['low', 'DoW']))
print(is_contains('dow', ['low', 'blow']))
print(calls)