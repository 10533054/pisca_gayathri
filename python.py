@app.route('/', methods=['GET', 'POST'])
def index():
    return  render_template('login-page.html')

@app.route('/showList', methods=['GET', 'POST'])
def lpage():
    return  render_template('list-page.html')

@app.route('/showReport', methods=['GET', 'POST'])
def rpage():
    return  render_template('report-page.html')




    
@app.route('/render-user-creation', methods=['GET', 'POST'])
def renderusercreation():
    return  render_template('user-creation.html')

@app.route('/login', methods=['POST'])
def login():
    usr = request.form.get('username')
    passw = request.form.get('password')
    cur = mysql.connection.cursor()
    cur.execute("select * from user_details where username=%s and password=%s",[usr.strip(),passw.strip()])
    data = cur.fetchall()
    cur.close()
    if len(data) > 0:
     return render_template('menu-page.html',useridx = data[0][2])
    else:
     return render_template('login-page-error.html')
    
@app.route('/signup', methods=['POST'])
def signup():
    usr = request.form.get('username')
    passw = request.form.get('password')
    email = request.form.get('email')
    cur = mysql.connection.cursor()
    cur.execute("select * from user_details where username=%s or email=%s",[usr.strip(),email.strip()])
    data = cur.fetchall()

    if len(data) == 0:
        cur.execute("insert into user_details (email,username,password) values (%s,%s,%s)",(email,usr,passw))
        mysql.connection.commit()
        cur.close()
        return render_template('login-page.html')
    else:
        cur.close()
        return render_template('user-creation-error.html')
