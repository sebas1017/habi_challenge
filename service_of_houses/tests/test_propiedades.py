from fastapi.testclient import TestClient
from constants import (
    INVALID_FILTERS_MESSAGE, RESOURCE_NOT_FOUND_MESSAGE, 
    mock_payload_correct_filter_1, mock_payload_invalid_filters, 
    mock_filter_function_1, mock_filter_function_2,
    mock_filter_function_3, mock_filter_function_4 )
import sys
sys.path.append('.')
from main import app
from functions.functions_data import check_size_filter


client = TestClient(app)

def test_get_all_houses():
    response = client.get("/api/v1/all_houses")
    assert len(response.json()) >= 0
    assert response.status_code == 200

def test_filter_all_houses():
    
    response_invalid_filters = client.post(
                "/api/v1/filter_data_houses", json=mock_payload_invalid_filters)

    response_valid_filters = client.post(
                "/api/v1/filter_data_houses", json=mock_payload_correct_filter_1)

    assert response_invalid_filters.json() == INVALID_FILTERS_MESSAGE
    assert response_invalid_filters.status_code == 400
    assert response_valid_filters.status_code == 200
    assert len(response_valid_filters.json()) >=0 

def test_resource_not_found():
    response_error_resource = client.get("/api/v1/fake_resource")
    assert response_error_resource.status_code == 404
    assert response_error_resource.json() == RESOURCE_NOT_FOUND_MESSAGE


def test_function_check_size_filter():
    test_1 = check_size_filter(mock_filter_function_1)
    test_2 =  check_size_filter(mock_filter_function_2)
    test_3 =  check_size_filter(mock_filter_function_3)
    test_4 =  check_size_filter(mock_filter_function_4)
    assert test_1 == False
    assert test_2 == True
    assert test_3 == False
    assert test_4 == False
    
    