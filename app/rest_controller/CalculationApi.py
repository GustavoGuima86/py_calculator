from fastapi import APIRouter

from app.model.RequestCalculationModel import RequestCalculationModel
from app.services.CalculationService import CalculationService

router = APIRouter()

@router.post("/calculate")
def calculate_values(numbers: RequestCalculationModel):
    calculation_service = CalculationService()
    return calculation_service.calculate_values(numbers)
