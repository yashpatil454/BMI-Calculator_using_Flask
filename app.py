from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = bmi_Calc(weight, height)
    return render_template("index.html",bmi=bmi)

def bmi_Calc(weight, height):
    return round((weight/((height/100)**2)),2)

app.run()