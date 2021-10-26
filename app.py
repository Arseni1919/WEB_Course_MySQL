from flask import Flask

from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import session
from flask import jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'


# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #
@app.route('/users')
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=query_result)


# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #
@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # recheck
        query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('insert_user.html', req_method=request.method)


# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    return redirect('/users')


# ------------------------------------------------- #
# ------------------------------------------------- #


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
