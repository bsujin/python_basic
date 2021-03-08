from flask import Flask, Response, jsonify, render_template
from flask import request, json
import pymysql
from flask_day02 import mylogging


app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/param", methods=['GET','POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name', "kimchulsu")
    if request.method == "GET":
        name = request.args.get('name', "kimchulsu")  
    return "param="+name

@app.route("/forward.do")
def forward():
    mylogging.logging()
    title = "Good Morning"
    return render_template('forward.html',title=title)

@app.route("/db.do")
def db():
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    curs.execute("select emp_id,emp_name,nickname from emp")
    rows = curs.fetchall()
    conn.close()
    print(rows)
    return render_template('db.html',title="good",list=[1,2,3],db_list=rows)

@app.route('/upd.ajax')
def ajax_upd():
    emp_id      = request.args.get('emp_id') 
    emp_name    = request.args.get('emp_name')  
    nickname    = request.args.get('nickname')   
    print("emp_id",emp_id)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("update emp set emp_name='"+emp_name+"', nickname='"+nickname+"' where emp_id='"+emp_id+"'")
    conn.commit()
    conn.close()
    obj = {"cnt":cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)



if __name__ == "__main__":
    app.run()