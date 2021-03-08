from flask import Flask
from flask.templating import render_template
import pymysql

app = Flask(__name__)

# db연동하기 
@app.route('/db.do')
def db(): 
    conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
#     curs = conn.cursor(pymysql.cursors.DictCursor)
    curs = conn.cursor()
    sql = "select s_code, s_name, s_price, in_time from stock order by s_name"
    curs.execute(sql)
    result = curs.fetchall()
    conn.close()
#     return render_template("db.html", result="good", list=[1,2,3], db_list=result)
    return render_template("db.html", result="good", list=[1,2,3])
    
    
if __name__ == '__main__':
#     app.run(debug=True)
    app.run()
    


    