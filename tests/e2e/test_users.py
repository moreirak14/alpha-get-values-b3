import pytest
from http import HTTPStatus

URL_REGISTER = "/api/users/register"
URL_ME = "/api/users/me"


@pytest.mark.django_db
def test_register_user_invalid(client):
    payload = dict(
            first_name="alpha",
            last_name="invest",
            email="alpha@gmail.com",
            password="123"
    )

    response = client.post(URL_REGISTER, data=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
            first_name="alpha",
            last_name="invest",
            email="alpha@gmail.com",
            password="alpha12645370"
    )

    response = client.post(URL_REGISTER, data=payload)
    data = response.data

    assert response.status_code == HTTPStatus.CREATED
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]
    assert "password" not in data
