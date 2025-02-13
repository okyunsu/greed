from flask import Flask, render_template, request, redirect, url_for

from com.okyunsu.bag.bag_controller import BagController
from com.okyunsu.bag.bag_model import BagModel
from com.okyunsu.exchange.exchange_model import ExchangeModel
app = Flask(__name__)
from com.okyunsu.exchange.exchange_controller import ExchangeController


def get_unit_count(change , money_list):
    
    amount = change 
    money_dict = {}
    
    for money in money_list:
        money_dict[money] = amount//money
        amount %= money
    return money_dict

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/won")
def won():
    return render_template("exchange/exchange_won.html")

@app.route("/doller")
def doller():
    return render_template("exchange/exchange_doller.html")

@app.route("/yen")
def yen():
    return render_template("exchange/exchange_yen.html")




@app.route('/exchange', methods = ["POST"])
def exchange():

    print("😀POST 방식 접근")
    price = request.form.get("price")
    paid = request.form.get("paid")
    price, paid = int(price), int(paid)
    print(f"😁지불 해야할 가격{price}")
    print(f"😆지불한 가격{paid}")
    change = paid - price
    print(f"😊거스름 돈 {change}")
    currency = request.form.get("currency")
    print("🐈", currency)
    

    controller = ExchangeController(price = price, paid = paid, 
                                    change = change, currency = currency)
    
    resp : ExchangeModel = controller.getResult()
    
    render_html = '<h1>결과보기</h1>'
    render_html += f'{resp.result}'


    return render_template( resp.page , render_html = render_html)
    

@app.route('/bag', methods = ["POST", "GET"])
def bag():

    if request.method == "POST":
        capacity = request.form.get("capacity")
        num_items = request.form.get("num_items")
        weights = request.form.get("weights")
        profits = request.form.get("profits")

        capacity, num_items = int(capacity), int(num_items)
  

        controller = BagController(capacity = capacity, num_items = num_items, weights = weights
                                   , profits = profits)
        
        resp : BagModel = controller.getResult()
        print(f"🐈총 가치: {resp.total_value}")
        print(f"🐶contents{resp._knapsack_contents}")
        render_html = '<h1>결과보기</h1>'
        render_html += f'{resp.total_value}'

    
        return render_template("bag/bag.html", render_html = render_html )

    else:
        return render_template("bag/bag.html")

 

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True  
