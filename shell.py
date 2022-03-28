from basic import basic

while True:
    text = input("basic > ")
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    if result:
        print(result)
