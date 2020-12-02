from flask import request, Blueprint

from api.db import database as db

user = Blueprint("user", __name__)


@user.route("/user")
def user_add():
    user = db.users.find_one()
    user["_id"] = str(user["_id"])
    return {"resp": user}, 200
