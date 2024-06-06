from fastapi import APIRouter

from app.model.RequestCalculationModel import RequestCalculationModel
from app.model.ReturnCalculationModel import ReturnCalculationModel
from app.services.CalculationService import CalculationService
from fastapi_pagination import add_pagination, LimitOffsetPage

router = APIRouter()

@router.post("/calculate")
def calculate_values(numbers: RequestCalculationModel):
    calculation_service = CalculationService()
    return calculation_service.calculate_values(numbers)

@router.get("/calculationspage", response_model=LimitOffsetPage[ReturnCalculationModel])
def get_paginated():
    calculation_service = CalculationService()
    return calculation_service.get_calculation_paginated()

add_pagination(router)