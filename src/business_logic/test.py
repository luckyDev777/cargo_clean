class SomeDAO:
    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b

    def get(self) -> str:
        return self.a


class SomeService:
    def __init__(self, dao: SomeDAO):
        self.dao = dao

    def get(self):
        return self.dao.get()
