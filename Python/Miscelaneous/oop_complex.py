class TestObj:
    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        self.kwargs = kwargs

    def __str__(self) -> str:
        kwarg_str = ''
        if self.kwargs:
            for key, value in self.kwargs.items():
                kwarg_str += f'\n{key}: {value}'
        return f'{"- "*10}\nname: {self.name}\nage: {self.age}{kwarg_str}\n{"- "*10}'

if __name__ == "__main__":
    a: TestObj = TestObj(name='Teste 1', age=15)
    print(a)

    b_json = {"name": "Teste 2", "age": 25}
    b: TestObj = TestObj(**b_json)
    print(b)

    c_json = {"name": "Teste 3", "age": 50, "observation": "Big new thing", "frequency": 15000}
    c: TestObj = TestObj(**c_json)
    print(c)