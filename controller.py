from view import GraphWindow


class Controller:

    def __init__(self, persona: any):
        self.persona = persona
        self.view = GraphWindow(self)

        self.view.show()

    def verification(self) -> str:
        answer: str = self.persona.verification()
        return answer

    # def verification() -> str:
    #     answer: str = verification()
    #     return answer

    @staticmethod
    def matrix_return():
        pass


