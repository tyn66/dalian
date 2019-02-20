from flask import Flask,render_template,request
from dlpc.dalianjiaojing import dalianpachong
app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello_world():
    return render_template("sy.html")

@app.route('/1/',methods=["POST"])
def hblongs():
    CarNum = request.form.get("plate_number")
    CarType = request.form.get("car_type")
    CarCode = request.form.get("vin")
    b = dalianpachong(CarType,CarNum,CarCode)
    return b

if __name__ == '__main__':
    app.run()
