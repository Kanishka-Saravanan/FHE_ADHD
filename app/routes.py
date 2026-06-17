from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
import pandas as pd
from flask import Blueprint, render_template, request
from model.model_runtime import predict_adhd
from app.models import User
from security.auth import hash_password, verify_password
import joblib
import numpy as np
import time
import numpy as np
main = Blueprint("main", __name__)


# -----------------------
# HOME
# -----------------------
@main.route("/")
def home():
    return redirect(url_for("main.login"))

# -----------------------
# LOGOUT
# -----------------------
@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))

# -----------------------
# REGISTER
# -----------------------
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = hash_password(request.form["password"])

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template("register.html")


# -----------------------
# LOGIN
# -----------------------
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and verify_password(user.password, password):
            session["user"] = username
            return redirect(url_for("main.index"))

    return render_template("login.html")


# -----------------------
# PREDICTION PAGE
# -----------------------
@main.route("/index", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("main.login"))

    if request.method == "POST":

        data = {
            "Age": float(request.form["Age"]),
            "Gender": request.form["Gender"],
            "EducationStage": request.form["EducationStage"],
            "InattentionScore": float(request.form["InattentionScore"]),
            "HyperactivityScore": float(request.form["HyperactivityScore"]),
            "ImpulsivityScore": float(request.form["ImpulsivityScore"]),
            "SymptomSum": float(request.form["SymptomSum"]),
            "Daydreaming": float(request.form["Daydreaming"]),
            "RSD": float(request.form["RSD"]),
            "SleepHours": float(request.form["SleepHours"]),
            "ScreenTimeHours": float(request.form["ScreenTimeHours"]),
            "ComorbidAnxiety": float(request.form["ComorbidAnxiety"]),
            "ComorbidDepression": float(request.form["ComorbidDepression"]),
            "FamilyHistoryADHD": float(request.form["FamilyHistoryADHD"]),
            "Medication": request.form["Medication"],
            "SchoolSupport": request.form["SchoolSupport"],
            "AcademicScore": float(request.form["AcademicScore"]),
        }

        # 🚀 CALL THE COMPILED MODEL FUNCTION
        prediction = predict_adhd(data)

        result = "YES" if prediction == 1 else "NO"

        return render_template("result.html", result=result)

    return render_template("index.html")
