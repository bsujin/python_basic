import pymysql
from flask import Flask, request, Response, jsonify, render_template, json
import logging
from flask_day02.mylogging import mylogger

app = Flask(__name__)
log = logging.getLogger()
for hdlr in log.handlers[:]:
    log.removeHandler(hdlr)
     
file_log = logging.FileHandler("emp.log")
file_log.setLevel(logging.DEBUG)

mylogger.addHandler(file_log)

# db연동하기 
@app.route('/emp.do')
def db():
    mylogger.debug("debug")
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    curs.execute("select emp_id,emp_nm,nick_nm from emp")
    rows = curs.fetchall()
    conn.close()
    print(rows)
    return render_template('emp.html',db_list=rows)
    

@app.route('/empUp.ajax')
def ajax_upd():
    mylogger.debug("debug")
    emp_id      = request.args.get('emp_id') 
    emp_name    = request.args.get('emp_nm')  
    nickname    = request.args.get('nick_nm')   
    print("emp_id",emp_id)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("update emp set emp_nm='"+emp_name+"', nick_nm='"+nickname+"' where emp_id='"+emp_id+"'")
    conn.commit()
    conn.close()
    obj = {"cnt":cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)
        
    
@app.route('/empDel.ajax')
def ajax_del():
    mylogger.debug("debug")
    emp_id = request.args.get('emp_id') 
    print("emp_id",emp_id)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("delete from emp where emp_id='"+emp_id+"'")
    conn.commit()
    conn.close()
    obj = {"cnt":cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)

@app.route('/empIns.ajax')
def ajax_ins():
    mylogger.debug("debug")
    emp_name    = request.args.get('emp_nm')  
    nickname    = request.args.get('nick_nm')   
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("INSERT INTO emp (emp_nm, nick_nm) VALUES('"+emp_name+"', '"+nickname+"')")
    conn.commit()
    conn.close()
    obj = {"cnt":cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)
    

    
if __name__ == '__main__':
#     app.run(debug=True)
    app.run()
   
    