from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        n = request.form.get('ism')
        b = request.form.get('baho')
        sh = request.form.get('sharh')
        if len(n) > 2 and b in '12345' and len(sh) >= 10:
            res = [n, b, sh]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

        return render_template('res.html', res=res)

    return render_template('index.html')    




if __name__ == '__main__':
    app.run(debug=True)
