from enum import Enum
import lo

class Operations(Enum):
    ADD = "+"
    SUB = "-"

class Calculator:
    ins_count = 0

    def __init__(self, name):
        self.name = name
        self.last_result = None
        Calculator.ins_count += 1

    def calculator(self, op: Operations, a, b):
        if self.is_number(a) and self.is_number(b):
            match op:
                case Operations.ADD: res = a + b
                case Operations.SUB: res = a - b

            self.last_result = res
            return res
    
    @classmethod
    def reset_counter(cls):
        cls.ins_count = 0

    @staticmethod
    def is_number(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    
cal_1 = Calculator("A")
result = cal_1.calculator(Operations.ADD, 10, 20)
cal_2 = Calculator("B")
cal_3 = Calculator("C")
result_2 = cal_2.calculator(Operations.SUB, 300, 234)
result_3 = cal_3.calculator(Operations.ADD, 234, 345)
print(result_3)
Calculator.reset_counter()
print(cal_1.ins_count)

# print(result)
# print(result_2)
