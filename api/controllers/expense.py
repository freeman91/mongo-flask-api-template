from flask import request, Blueprint

expense = Blueprint("expense", __name__)


@expense.route("/expense/create")
def expense_add():
    pass
