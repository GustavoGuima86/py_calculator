from functools import reduce

from app.model.RequestCalculationModel import RequestCalculationModel
from app.model.ReturnCalculationModel import ReturnCalculationModel


class CalculationService:
    def calculate_values(self, calc_request : RequestCalculationModel) -> ReturnCalculationModel:

        calculation = 0

        if calc_request.calculation_type.value == "SUM":
            calculation = sum(calc_request.numbers)

        if calc_request.calculation_type.value == "SUBTRACTION":
            calculation = reduce(lambda x, y: x - y, calc_request.numbers)

        if calc_request.calculation_type.value == "MULTIPLICATION":
            calculation = 1
            for num in calc_request.numbers:
                calculation *= num

        if calc_request.calculation_type.value == "DIVISION":
            calculation = calc_request.numbers[0]
            for num in calc_request.numbers[1:]:
                if num == 0:
                    raise ValueError("Division by zero encountered in the list.")
                calculation /= num

        return ReturnCalculationModel(result=calculation, calculation_type=calc_request.calculation_type)
