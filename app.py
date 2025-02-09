from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

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

@app.route('/won', methods = ["GET","POST"])
def won():
    if request.method == "POST":
        print("😀POST 방식 접근")
        price = request.form.get("price")
        paid = request.form.get("paid")
        price, paid = int(price), int(paid)
        print(f"😁지불 해야할 가격{price}")
        print(f"😆지불한 가격{paid}")
        change = paid - price
        print(f"😊거스름 돈 {change}")
        
      
        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        money_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500, 
                      WON_100, WON_50, WON_10]

        money_dict = get_unit_count(change, money_list)
       
        for won, count in money_dict.items():
            print(f"{won}원: {count}개")

        render_html = '<h1>결과보기</h1>'
        for won, count in money_dict.items():
            render_html += f"{won}원: {count}개<br/>"       


        return render_template("exchange_won.html", render_html = render_html)
        

    else:
        print("😳GET 방식으로 접근")
        return render_template("exchange_won.html")


@app.route("/doller", methods = ["POST", "GET"])
def doller():
    if request.method == "POST":
        paid = request.form.get("paid")
        price = request.form.get("price")
        paid, price = int(paid), int(price)
        change = price / paid
        change = int(change)
        print(f"😆환율: {paid}")
        print(f"😆환전할 금액: {price}")
        print(f"환전한 달러: {change}")


        money_list = [100, 50, 20, 10, 5, 2, 1]

        money_dict = get_unit_count(change , money_list)
        
        render_html = "<h3>계산결과</h3>"
        for doller, Currency in money_dict.items():
            render_html += f"{doller}달러 지폐: {Currency}개</br>"
        
        return render_template("exchange_doller.html", render_html = render_html)


    else:
        return render_template("exchange_doller.html")




if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True  
