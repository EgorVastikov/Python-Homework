class App:
    def __init__(self):
        self.routes = {}

    def callback(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def get(self, path):
        return self.routes.get(path, None)


app = App()

@app.callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')