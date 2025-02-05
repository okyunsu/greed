from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/', methods = ["GET","POST"])
def index():

    




    if request.method == "POST":
        print("POST 방식 접근")
        price = request.form.get("price")
        paid = request.form.get("paid")
        coin500 = 2
        coin100 = 3
        coin50 = 0
        coin10 = 0
        price, paid = int(price), int(paid)
        change = price - paid
        print(f"지불 해야할 가격{price}")
        print(f"지불한 가격{paid}")
        print(f"거스름 돈 {change}")
        print(f"동전 종류와 수")
        print(f"500원{coin500}, 100원{coin100}")
        return render_template("index.html", price = price, paid= paid, change = change,
                               coin500=coin500, coin100=coin100, coin50=coin50, coin10= coin10)


    else:
        print("GET 방식으로 접근")
        return render_template("index.html")


if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True  
