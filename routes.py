from flask import Blueprint

# creating blueprint to include it into the app factory later
routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def index():
    return "It's fucking works!!!"
