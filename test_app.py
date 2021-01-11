import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_cat_breeds_json_with_proper_mimetype(client):
    response = client.get('/api/cat_breeds')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_cat_breeds_returns_two_cats(client):
    response = client.get('/api/cat_breeds')
    cat_dict = response.get_json()
    assert len(cat_dict['cat_breeds']) == 2


def test_new_cat_breed_returns_id(client):
    bengal = {"breed": "Bengal", "style": "Wild"}
    response = client.post('/api/cat_breeds', json=bengal)
    breed_response = response.get_json()
    assert isinstance(breed_response['id'], int)


def test_new_cat_breed_without_json_results_in_error(client):
    response = client.post('/api/cat_breeds')
    assert response.status_code == 400


def test_new_cat_breed_without_all_elements_errors(client):
    bengal = {"breed": "Bengal"}
    response = client.post('/api/cat_breeds', json=bengal)
    assert response.status_code == 400


def test_single_cat_breed_with_invalid_id_errors(client):
    response = client.get('/api/cat_breeds/1001')
    assert response.status_code == 404


def test_single_cat_breed_has_expected_elements(client):
    response = client.get('/api/cat_breeds/0')
    cat_dict = response.get_json()
    assert 'breed' in cat_dict
