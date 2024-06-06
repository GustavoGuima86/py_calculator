from functools import reduce

from app.model.RequestCalculationModel import RequestCalculationModel
from app.model.ReturnCalculationModel import ReturnCalculationModel
from app.repository.CalculationRepository import CalculationRepository

from fastapi_pagination.ext.sqlalchemy import paginate

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

        calculation_entity = CalculationRepository.create_calculation(self, calc_request, calculation)

        return ReturnCalculationModel(result=calculation, calculation_type=calculation_entity.calculation_type)

    def get_calculation_paginated(self):
        return paginate(CalculationRepository.get_calculation_paginated(self))


