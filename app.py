from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "POST":
        print("POST 방식 접근")
        price = request.form.get("price")
        paid = request.form.get("paid")
        price, paid = int(price), int(paid)
        print(f"지불 해야할 가격{price}")
        print(f"지불한 가격{paid}")
        change = paid - price
        print(f"거스름 돈 {change}")
        COIN_500 = 500
        coin500 = change//COIN_500
        coin500_nmg = change%COIN_500
        
        COIN_100 = 100
        coin100 = coin500_nmg // COIN_100
        coin100_nmg = coin500_nmg % COIN_100       
        
        COIN_50 = 50
        coin50 = coin100_nmg // COIN_50
        coin50_nmg = coin100_nmg % COIN_50
        
        COIN_10=10
        coin10 = coin50_nmg // COIN_10
        coin10_nmg = coin50_nmg % COIN_10
    
        print(f"동전 종류와 수")
        print(f"500원: {coin500}, 100원: {coin100}, 50원: {coin50}, 10원: {coin10}")
        return render_template("index.html", price = price, paid= paid, change = change,
                               coin500=coin500, coin100=coin100, coin50=coin50, coin10= coin10)


    else:
        print("GET 방식으로 접근")
        return render_template("index.html")


if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True  
