calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    Copybara = str(string)
    result = (len(Copybara), Copybara.upper(), Copybara.lower())
    count_calls()
    return result
def is_contains(string, list_search):
    string = str(string).lower()
    list_search = list(list_search)
    count_calls()
    for i in range(len(list_search)):
        if str(list_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result
print(string_info('Copybara'))
print(string_info('Armagedon'))
print(is_contains('Urban', ['ban', 'BaNaN','urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)








