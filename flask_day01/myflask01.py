# from flask import Flask, request
# 
# app = Flask(__name__)
# 
# @app.route('/') # servlet url mapping과 유사 
# def home():
#     return 'Hello, Flask!'
# 
# @app.route('/param') # servlet url mapping과 유사 
# def param():
#     
#     temp = request.args.get('name','하하하')  # @UndefinedVariable
#     return 'param=' + temp
# 
# @app.route('/post', methods=['post'])
# def post():
#     value =  request.form['input']
#     msg = "%s님 환영합니다 " %value
#     return msg
# 
# if __name__ == '__main__':
#     app.run(debug=True)
#     
