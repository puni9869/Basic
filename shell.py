from basic import run

while True:
    text = input("basic > ")
    result, error = run('<stdin>', text)

    if error:
        print(error.as_string())
    if result:
        print(result)
