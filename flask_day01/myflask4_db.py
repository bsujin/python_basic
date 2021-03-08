from flask import Flask
from flask.templating import render_template
import pymysql

app = Flask(__name__)

@app.route('/') # servlet url mapping과 유사 
def home():
    return 'Hello, Flask!'

# db연동하기 
@app.route('/db.do')
def db(): 
    a = db_select()
    # _code_db select >> 화면에 뿌려주기 
    return render_template('db.html', title=a, list=[1,2,3])
#     return render_template('layout.html', title=title)

@app.route('/select.do')
def db_select():
    conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
#     curs = conn.cursor(pymysql.cursors.DictCursor)
    curs = conn.cursor()
    sql = "select s_code, s_name, s_price, in_time from stock order by s_name"
    curs.execute(sql)
    result = curs.fetchall()

#     for i in result:
#         res = i[0]
#         print("3i : ",i['s_code'], i['s_name'], i['s_price'], i['in_time'])
    
    conn.close()
    return render_template("db.html", result=result)
    
    
if __name__ == '__main__':
#     app.run(debug=True)
    app.run()
    



    