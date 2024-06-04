from fastapi.testclient import TestClient

from app.main import app
from app.model.CalculationType import CalculationType
from app.model.RequestCalculationModel import RequestCalculationModel

client = TestClient(app)

def test_sum():
    request = RequestCalculationModel(numbers=[2,4], calculation_type=CalculationType.SUM)

    request_data = request.model_dump()
    request_data['calculation_type'] = request_data['calculation_type'].value


    response = client.post("/calculate", json=request_data)

    assert response.status_code == 200
    assert response.json()["result"] == 6.0
    assert response.json()["calculation_type"] == "SUM"

def test_sub():
    request = RequestCalculationModel(numbers=[2,3], calculation_type=CalculationType.SUBTRACTION)

    request_data = request.model_dump()
    request_data['calculation_type'] = request_data['calculation_type'].value


    response = client.post("/calculate", json=request_data)

    assert response.status_code == 200
    assert response.json()["result"] == -1.0
    assert response.json()["calculation_type"] == "SUBTRACTION"

def test_mult():
    request = RequestCalculationModel(numbers=[2,3], calculation_type=CalculationType.MULTIPLICATION)

    request_data = request.model_dump()
    request_data['calculation_type'] = request_data['calculation_type'].value


    response = client.post("/calculate", json=request_data)

    assert response.status_code == 200
    assert response.json()["result"] == 6.0
    assert response.json()["calculation_type"] == "MULTIPLICATION"

def test_div():
    request = RequestCalculationModel(numbers=[2,3], calculation_type=CalculationType.DIVISION)

    request_data = request.model_dump()
    request_data['calculation_type'] = request_data['calculation_type'].value


    response = client.post("/calculate", json=request_data)

    assert response.status_code == 200
    assert response.json()["result"] == 0.6666666666666666
    assert response.json()["calculation_type"] == "DIVISION"

def test_div_zero_error():
    request = RequestCalculationModel(numbers=[3,0], calculation_type=CalculationType.DIVISION)

    request_data = request.model_dump()
    request_data['calculation_type'] = request_data['calculation_type'].value


    response = client.post("/calculate", json=request_data)

    assert response.status_code == 400
    assert response.json() == {'detail': 'Division by zero encountered in the list.'}

def test_wrong_type():
    request = {"numbers": [1,2], "calculation_type":"Other"}
    response = client.post("/calculate", json=request)

    assert response.status_code == 422
    assert response.json() == {'detail': [{'ctx': {'expected': "'SUM', 'SUBTRACTION', 'MULTIPLICATION' or "
                                                               "'DIVISION'"},
                                           'input': 'Other',
                                           'loc': ['body', 'calculation_type'],
                                           'msg': "Input should be 'SUM', 'SUBTRACTION', 'MULTIPLICATION' or "
                                                  "'DIVISION'",
                                           'type': 'enum'}]}
def test_no_payload():
    request = {}
    response = client.post("/calculate", json=request)

    assert response.status_code == 422
    assert response.json() == {'detail': [{'input': {},
                                           'loc': ['body', 'numbers'],
                                           'msg': 'Field required',
                                           'type': 'missing'},
                                          {'input': {},
                                           'loc': ['body', 'calculation_type'],
                                           'msg': 'Field required',
                                           'type': 'missing'}]}

