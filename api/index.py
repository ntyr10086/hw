from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form.get("x"))
            y = float(request.form.get("y"))
            opt = request.form.get("opt")
            
            if opt == "/" and y == 0:
                result = "除數不能為0"
            else:
                match opt:
                    case "+": result = x + y
                    case "-": result = x - y
                    case "*": result = x * y
                    case "/": result = x / y
        except:
            result = "輸入格式錯誤"
            
    return render_template("index.html", result=result)


app = app