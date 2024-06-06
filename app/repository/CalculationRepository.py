from app.entity.CalculationEntity import CalculationEntity
from app.model.RequestCalculationModel import RequestCalculationModel
from app.repository.database import get_db

class CalculationRepository:
    def create_calculation(self, calculation_request: RequestCalculationModel, calculation: float) -> CalculationEntity:
        db = get_db()

        calculation_entity = CalculationEntity(numbers=calculation_request.numbers, result=calculation, calculation_type=calculation_request.calculation_type)
        db.add(calculation_entity)
        db.commit()

        return calculation_entity

    def get_calculation_paginated(self):
        db = get_db()
        return db.query(CalculationEntity)