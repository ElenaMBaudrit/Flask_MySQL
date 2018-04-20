from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql =  MySQLConnector(app, 'fullFriends') #this is the name of the database. In this case, it has not been created yet

@app.route('/')
def friends():
    query = "SELECT concat(first_name, ' ', last_name) AS 'name', age AS 'age', concat(day, ' ', month) AS 'friend_since', year FROM users;"
    friends_names= mysql.query_db(query)
    print friends_names
    return render_template('friendsNames.html', all_friends= friends_names)

# @app.route('/new_friend', methods=['POST'])
# def create_user():
#     session['name'] = request.form['name']
#     session['age'] = request.form['age']
#     return redirect('/friends')

@app.route('/new_friend', methods=['POST'])
def create_user():
    data= {
        'name': request.form['name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    query = "INSERT INTO users (first_name, last_name, age, create_at, update_at) VALUES (:name, :last_name, :age, NOW(), NOW())"
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)



