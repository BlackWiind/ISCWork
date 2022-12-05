from view import GraphWindow
import utils
import random


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = GraphWindow(self)

        self.view.show()

    def verification(self):
        self.view.matrix_radio.setCheckable(True)
        self.view.text_view.clear()
        self.view.text_view.append("Начата верификация:")
        first_question_count: int = 0
        second_question_count: int = 0
        is_verificated = True
        for _ in range(random.randint(1, 20)):
            if random.randint(0, 1) > 0:
                first_question_count += 1
                if not utils.question_one(self.model.all_matrixs(), self.model.rules, self.model.open_key):
                    is_verificated = False
            else:
                second_question_count += 1
                if not utils.question_two():
                    is_verificated = False
        self.view.text_view.append(f"было задано {first_question_count} первых и\n"
                                   f"{second_question_count} вторых вопросов.")
        self.view.text_view.append(f"Верификация пройдена успешно") if is_verificated else f"Верификация провалена"

        # def verification(persona: object) -> str:
        #     answer: str = f"Выполнена верификация:\n"
        #     for _ in range(random.randint(1, 20)):
        #         # person_A = Person(CONSTANT_P, CONSTANT_Q, VARIANT)
        #         persona.create_matrixs(BASE_MATRIX)
        #         if random.randint(0, 1) > 0:
        #             answer += "Выбран первый вопрос, "
        #             answer += "ответ верный\n" if question_one(persona.get_f_matrix(), persona.get_tilda_h_matrix(),
        #                                                        persona.rules, persona.open_key) else "ответ неверный\n"
        #         else:
        #             answer += "Выбран второй вопрос, "
        #             answer += "ответ верный\n" if question_two() else "ответ неверный\n"
        #     return answer

    # def verification() -> str:
    #     answer: str = verification()
    #     return answer

    @staticmethod
    def matrix_return():
        pass
