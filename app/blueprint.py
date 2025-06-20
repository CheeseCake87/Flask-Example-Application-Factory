from flask import Blueprint

from app.models import Example

example_blueprint = Blueprint("api", __name__, url_prefix="/example-blueprint")

"""
The routes below will be accessible from 'host:port/example-blueprint'
"""


@example_blueprint.get("/")
def get():
    return {"ok": True, "data": "Hello World!"}


@example_blueprint.post("/post")
def post():
    return {"ok": True, "data": "Hello World!"}


@example_blueprint.route("/get-or-post", methods=["GET", "POST"])
def get_or_post():
    return {"ok": True, "data": "Hello World!"}


@example_blueprint.get("/show-table")
def show_table():
    return {"ok": True, "data": f"{Example}"}
