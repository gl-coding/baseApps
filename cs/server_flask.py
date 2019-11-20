from flask import Flask, request
app = Flask(__name__)

@app.route("/get")
def hello():
    return "Hello World!"

@app.route('/post',methods=["POST"])
def get_tasks():
    if request.method=='POST':
        username=request.form['name']
        return username

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80000)
