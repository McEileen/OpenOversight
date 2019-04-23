import pytest
from flask import url_for, current_app
from .route_helpers import login_user, login_admin

def test_user_cannot_access_departments_api(mockdata, client, session):
    with current_app.test_request_context():
        login_user(client)

        rv = client.get(url_for('auth.department_api'),
            follow_redirects=True
        )

        assert rv.status_code == 403

def test_admin_can_access_departments_api(mockdata, client, session):
    with current_app.test_request_context():
        login_admin(client)

        rv = client.get(url_for('auth.department_api'),
            follow_redirects=True
        )

        assert rv.status_code == 200