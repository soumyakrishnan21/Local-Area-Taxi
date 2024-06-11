from flask import Flask, redirect, render_template, request, session
from DBConnection import Db

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def hello_world():
    return render_template('login_index.html')


@app.route('/login', methods=['post'])
def login():
    db = Db()
    username = request.form['textfield']
    password = request.form['textfield2']
    qry = "select * from login where user_name='" + username + "' and password='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        type = res['user_type']
        id = res['login_id']
        session['lid'] = id
        session['lg'] = 'lin'
        if type == "admin":
            return redirect('/admin_home')
        else:
            return '''<script>alert("invalid user");window.location="/"</script>'''
    else:
        return '''<script>alert("invalid user");window.location="/"</script>'''


@app.route('/logout')
def logout():
    session['lg'] = ""
    return redirect('/')


@app.route('/admin_home')
def admin_home():
    if session['lg'] == 'lin':
        return render_template("admin/admin_home.html")
    else:
        return redirect('/')


@app.route('/view_driver')
def view_driver():
    if session['lg'] == 'lin':
        db = Db()
        qry = "select * from driver,login where driver.driver_id=login.login_id"
        res = db.select(qry)
        return render_template('admin/accept_reject_driver.html', data=res)
    else:
        return redirect('/')


@app.route('/approve_driver/<id>')
def approve_driver(id):
    if session['lg'] == 'lin':
        db = Db()
        qry = db.update("update login set user_type='driver' where user_type='pending' and login_id='" + id + "'")
        return view_driver()
    else:
        return redirect('/')


@app.route('/reject_driver/<id>')
def reject_driver(id):
    if session['lg'] == 'lin':
        db = Db()
        qry = db.update("update login set user_type='rejected' where user_type='pending' and login_id='" + id + "'")
        return view_driver()
    else:
        return redirect('/')


@app.route('/view_vehicles')
def view_vehicles():
    if session['lg'] == 'lin':
        db = Db()
        qry = "select * from driver,vehicle where driver.driver_id=vehicle.driver_id"
        res = db.select(qry)
        return render_template('admin/view_vehicle.html', data=res)
    else:
        return redirect('/')


@app.route('/view_user')
def view_user():
    if session['lg'] == 'lin':

        db = Db()
        qry = "select * from user"
        res = db.select(qry)
        return render_template('admin/view_user.html', data=res)
    else:
        return redirect('/')


@app.route('/view_complaint')
def view_complaint():
    if session['lg'] == 'lin':
        db = Db()
        qry = db.select(
            "select * from complaint,user where complaint.user_id=user.user_id ")
        return render_template("admin/view_complaint.html", data=qry)
        print(qry)
    else:
        return redirect('/')


@app.route('/send_reply/<v>')
def send_reply(v):
    if session['lg'] == 'lin':
        return render_template("admin/send_reply.html", data=v)
    else:
        return redirect('/')


@app.route('/send_reply_post/<v>', methods=['post'])
def send_reply_post(v):
    if session['lg'] == 'lin':
        db = Db()
        r = request.form['textarea']
        qry = db.update("update complaint set reply='" + r + "',rdate=curdate() where cid='" + v + "'")
        return view_complaint()
    else:
        return redirect('/')


@app.route('/view_rating')
def view_rating():
    if session['lg'] == 'lin':

        db = Db()
        qry = "select * from user,rating where user.user_id=rating.user_id"
        res = db.select(qry)
        return render_template('admin/view_rating.html', data=res)
    else:
        return redirect('/')


@app.route('/view_feedback')
def view_feedback():
    if session['lg'] == 'lin':
        db = Db()
        qry = "select * from user,feedback where user.user_id=feedback.user_id"
        res = db.select(qry)
        return render_template('admin/view_feedback.html', data=res)
    else:
        return redirect('/')


@app.route('/add')
def add():
    return render_template('admin/add_category.html')


@app.route('/add_category',methods=['post'])
def add_category():
    if session['lg'] == 'lin':
        db=Db()
        c=request.form['c']
        qry="insert into category values('','"+c+"')"
        db.insert(qry)
        return add()
    else:
        return redirect('/')

@app.route('/manage_category')
def manage_category():
    if session['lg'] == 'lin':
        db = Db()
        qry = "select * from category"
        res = db.select(qry)
        return render_template('admin/manage_category.html', data=res)
    else:
        return redirect('/')

@app.route('/delete_category/<id>')
def delete_category(id):
    if session['lg'] == 'lin':
        db = Db()
        qry = "delete from category where id='"+id+"'"
        res = db.delete(qry)
        return '''<script>alert("deleted");window.location="/manage_category"</script>'''
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
