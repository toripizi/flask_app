from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.orm.exc import NoResultFound
from models.user import db, User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("list.html", users=users)


@user_blueprint.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for(".user_detail", id=user.id))

    return render_template("create.html")


@user_blueprint.route("/user/<int:id>")
def user_detail(id):
    try:
        user = db.session.query(User).filter_by(id=id).one()
    except NoResultFound:
        return render_template("404.html"), 404
    return render_template("detail.html", user=user)


@user_blueprint.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for(".user_list"))

    return render_template("user/delete.html", user=user)
