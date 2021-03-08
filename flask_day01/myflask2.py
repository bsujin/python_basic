from flask import Flask, request

app = Flask(__name__)

@app.route('/') # servlet url mapping과 유사 
def home():
    return 'Hello, Flask!'

# @app.route('/param') # servlet url mapping과 유사 
# def param():
#     
#     temp = request.args.get('name','하하하')  # @UndefinedVariable
#     return 'param=' + temp

@app.route('/param', methods=['GET', 'POST'])
def post():
    if request.method == "POST":
        name = request.args.get('name', 'post방식')
    if request.method == "GET":
        name = request.args.get('name', 'get방식')

    return "param : " + name

if __name__ == '__main__':
    app.run(debug=True)
    
