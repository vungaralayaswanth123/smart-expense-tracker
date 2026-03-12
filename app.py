from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        return redirect("/dashboard")

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", expenses=expenses)


if __name__ == "__main__":
    app.run(debug=True)
