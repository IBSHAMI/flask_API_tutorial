from flask import Blueprint

from app.api.views import TestView


api_blueprint = Blueprint("api", __name__)


api_blueprint.add_url_rule(
    "/api/v1/test/", view_func=TestView.as_view('test_view'), methods=["GET"]
)
