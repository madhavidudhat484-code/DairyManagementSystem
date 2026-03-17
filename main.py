from flask import render_template, redirect, url_for, session
from app import create_app

app = create_app()


#  PAGE ROUTING


@app.route("/")
def index():
    return redirect(url_for("login_page"))


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("homepage.html")


@app.route("/customers/add")
def add_customer_page():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("newcustomer.html")


@app.route("/customers/view")
def view_customers_page():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("customerdetails.html")


@app.route("/collection/add")
def add_collection_page():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("addcollection.html")


@app.route("/collection/view")
def view_collection_page():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("viewcollection.html")


@app.route("/rates/add")
def add_rates_page():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("ratechart.html")


@app.route("/rates/view")
def view_rates_page():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("viewratechart.html")


#  RUNNING THE APP

if __name__ == "__main__":
    app.run(debug=True, port=5000)
else:
    app.run(debug=True, port=5000)
