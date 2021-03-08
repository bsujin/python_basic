from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/') # servlet url mapping과 유사 
def home():
    return 'Hello, Flask!'

@app.route('/param', methods=['GET', 'POST'])
def post():
    if request.method == "POST":
        name = request.args.get('name', 'post방식')
    if request.method == "GET":
        name = request.args.get('name', 'get방식')

    return "param : " + name

# @app.route('/forward.do')
# def forward(): 
#     return render_template('forward.html')
# 
# if __name__ == '__main__':
# #     app.run(debug=True)
#     app.run()
#     
@app.route('/forward.do')
def forward(): 
    title = "Good"
    return render_template('forward.html', title=title)
#     return render_template('layout.html', title=title)

@app.route('/db.do')
def db(): 
    # _code_db select >> 화면에 뿌려주기 
    return render_template('db.html', title="gogo", list=[1,2,3])
#     return render_template('layout.html', title=title)

if __name__ == '__main__':
#     app.run(debug=True)
    app.run()
    



    