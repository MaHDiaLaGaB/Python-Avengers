from enum import Enum

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
        match op:
            case Operations.ADD: res = a + b
            case Operations.SUB: res = a - b

        self.last_result = res
        return res

    
cal_1 = Calculator("A")
result = cal_1.calculator(Operations.ADD, 10, 20)
cal_2 = Calculator("B")
result_2 = cal_2.calculator(Operations.SUB, 300, 234)

print(result)
print(result_2)
