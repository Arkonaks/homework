def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
#inner_function - функция видима только внутри функции test_function()