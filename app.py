from flask import Flask, render_template, request, redirect, send_from_directory
import re, pathlib
import pandas as pd
import sqlite3

class database():
    df = pd.read_csv('data.csv', encoding='UTF8')
    conn = sqlite3.connect('crud.db', check_same_thread=False)
    cursor = conn.cursor()

    try: 
        df.to_sql(name='sales', con=conn)
    except:
        pass

app = Flask(__name__)

@app.route("/")
def table():
    query = database.conn.execute("SELECT * From sales")
    cols = [column[0] for column in query.description]
    data = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    data = data.fillna('')

    return render_template('index.html',tables=[re.sub(' mytable', 
    '" id="example', data.to_html(classes='mytable'))],
    titles = ['CRUD'])


@app.route('/insert', methods= ['POST','GET'])
def insert():

    q1 = request.form['num1']
    q2 = request.form['num2']
    q3 = request.form['num3']
    q4 = request.form['num4']
    q5 = request.form['num5']
    q6 = request.form['num6']
    q7 = request.form['num7']
    q8 = request.form['num8']

    database.cursor.execute(f'insert into sales values({q1},{q1},{q2},{q3},{q4},{q5},{q6},{q7},{q8});')
    database.conn.commit()

    return redirect('/')


@app.route('/delete', methods= ['POST','GET'])
def delete():
    q1 = request.form['num1']

    database.cursor.execute(f'''
    DELETE FROM sales
        WHERE i = {q1};
    ''')
    database.conn.commit()

    return redirect('/')


@app.route('/save/<name>', methods=['GET'])
def save(name): 
    return send_from_directory(f'{pathlib.Path(__file__).parent.absolute()}', 
    name, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
