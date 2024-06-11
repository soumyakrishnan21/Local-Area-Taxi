from flask import Flask, redirect, render_template, request, session
import demjson
from DBConnection import Db

app = Flask(__name__)


@app.route('/login', methods=['post'])
def login():
    db = Db()
    username = request.form['username']
    password = request.form['password']
    lati = request.form['lati']
    longi = request.form['longi']
    place = request.form['place']
    qry = "SELECT * FROM `login` WHERE `user_name`='" + username + "' AND `password`='" + password + "'"
    res = db.selectOne(qry)
    print(res)
    res1 = {}
    if res != None:
        type = res['user_type']
        id = res['login_id']
        if type == "admin":
            res1['status'] = "none"
            return demjson.encode(res1)
        elif type == "driver":

            q = "select * from location where driver_id='" + str(id) + "'"
            r = db.selectOne(q)
            if r is not None:
                q1 = "update location set latitude='" + lati + "',longitude='" + longi + "',place='" + place + "' where driver_id='" + str(
                    id) + "'"
                db.update(q1)
                # r1={}
                # r1['status'] = "ok"
                res1['status'] = "ok"
                res1['type1'] = type
                res1['id1'] = id
                return demjson.encode(res1)
                # return demjson.encode(r1)
            else:
                qry1 = "insert into location values('','" + str(
                    id) + "','" + lati + "','" + longi + "','" + place + "')"
                db.insert(qry1)
                r2 = {}
                r2['status'] = "ok"
                return demjson.encode(r2)
            return demjson.encode(res1)
        elif type == "user":
            res1['status'] = "ok"
            res1['type1'] = type
            res1['id1'] = id
            return demjson.encode(res1)
        else:
            res1['status'] = 'none'
            return demjson.encode(res1)
    else:
        res1['status'] = 'none'
        return demjson.encode(res1)


@app.route('/user_register', methods=['post'])
def register():
    db = Db()
    name = request.form['name']
    gender = request.form['gender']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    district = request.form['district']
    phone = request.form['phone']
    email = request.form['email']
    uname = request.form['username']
    password = request.form['password']
    cp = request.form['password1']
    res = db.selectOne("select * from login where user_name='" + uname + "'")
    res2 = {}
    if res is not None:
        res2['status'] = 'Already exist'
        return demjson.encode(res2)
    else:
        # res2['status']='ok'
        if password == cp:
            qry = "insert into login values('','" + uname + "','" + str(password) + "','user')"
            res = db.insert(qry)
            qry1 = "insert into user values('" + str(
                res) + "','" + name + "','" + gender + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phone + "','" + email + "')"
            db.insert(qry1)
            res2['status'] = 'Success'
            return demjson.encode(res2)
        else:
            res2['status'] = 'password doesnot match'
            return demjson.encode(res2)


@app.route('/driver_register', methods=['post'])
def driver_register():
    db = Db()
    name = request.form['name']
    age = request.form['age']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    district = request.form['district']
    lati = request.form['lat']
    longi = request.form['long']
    lic = request.form['lic']
    phone = request.form['phone']
    email = request.form['email']
    uname = request.form['username']
    password = request.form['password']
    cp = request.form['password1']
    import datetime
    img = request.files['pic']
    date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    img.save("C:\\Users\\SOUMYA\\Desktop\\software\\Local_area_taxi\\Local_area_taxi\\static\\" + date + ".jpg")
    path = "/static/" + date + ".jpg"
    res = db.selectOne("select * from login where user_name='" + uname + "'")
    res2 = {}
    if res is not None:
        res2['status'] = 'Already exist'
        return demjson.encode(res2)
    else:
        if password == cp:
            qry = "insert into login values('','" + uname + "','" + str(password) + "','pending')"
            res = db.insert(qry)
            qry1 = "insert into driver values('" + str(
                res) + "','" + name + "','" + age + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + lati + "','" + longi + "','" + str(
                path) + "','" + phone + "','" + email + "','" + lic + "')"
            db.insert(qry1)
            qry2 = db.insert(
                "insert into location values('','" + str(res) + "','" + lati + "','" + longi + "','" + place + "')")
            res2['status'] = 'ok'
            return demjson.encode(res2)
        else:
            res2['status'] = 'none'
            return demjson.encode(res2)


@app.route('/feedback', methods=['get', 'post'])
def sendfeedback():
    db = Db()
    user_id = request.form['lid']
    feedback = request.form['feedback']
    qry = "INSERT INTO feedback VALUES(NULL ,'" + user_id + "','" + feedback + "',curdate())"
    res = db.insert(qry)
    res1 = {}
    res1['status'] = 'feedback send successfully'
    return demjson.encode(res1)


@app.route('/rating', methods=['get', 'post'])
def rating():
    db = Db()
    user_id = request.form['lid']
    rating = request.form['rating']
    qry = "INSERT INTO rating VALUES(NULL ,'" + rating + "','" + user_id + "',curdate())"
    res = db.insert(qry)
    res1 = {}
    res1['status'] = 'feedback send successfully'
    return demjson.encode(res1)


@app.route('/view_reply', methods=['post'])
def view_reply():
    d = Db()
    lid = request.form['lid']
    qr = "SELECT * FROM complaint WHERE user_id='" + lid + "'"
    res = d.select(qr)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    res1['lid'] = lid
    return demjson.encode(res1)


@app.route('/view_rating', methods=['post'])
def view_rating():
    d = Db()
    # lid = request.form['lid']
    qr = "SELECT * FROM rating,user WHERE rating.user_id=user.user_id"
    res = d.select(qr)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/view_driver', methods=['post'])
def view_driver():
    db = Db()
    lati = request.form['lati']
    print(lati)
    longi = request.form['longi']
    print(longi)
    place = request.form['place']
    qry = "select driver.*,location.*,vehicle.*,category.*, (3959 * ACOS ( COS ( RADIANS('" + str(
        lati) + "') ) * COS( RADIANS( location.latitude) ) * COS( RADIANS( location.longitude ) - RADIANS('" + str(
        longi) + "') ) + SIN ( RADIANS('" + str(
        lati) + "') ) * SIN( RADIANS( location.latitude ) ))) AS user_distance FROM location,driver,vehicle,category HAVING user_distance  < 6.2137 and driver.driver_id=vehicle.driver_id and driver.driver_id=location.driver_id and vehicle.category_id=category.id"
    # qry = "select * from driver,vehicle where driver.driver_id=vehicle.driver_id and driver.longitude LIKE and driver.longitude like '%longi%' and driver.place like '%place%'"
    # qry="SELECT driver_id, (6371 * ACOS (COS ( RADIANS(latitude) )* COS( RADIANS( lati ))* COS( RADIANS( longi ) - RADIANS($longitude) )+ SIN ( RADIANS(latitude) )* SIN( RADIANS( lati ) )) AS distance FROM driver HAVING distance < 30 ORDER BY distance LIMIT 0 , 20;"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/complaint', methods=['get', 'post'])
def complaint():
    db = Db()
    user_id = request.form['lid']
    complaint = request.form['complaint']
    qry = "INSERT INTO complaint VALUES(NULL ,'" + complaint + "',curdate(),'" + user_id + "','pending','pending')"
    res = db.insert(qry)
    res1 = {}
    res1['status'] = 'complaint Send successfully'
    return demjson.encode(res1)


@app.route('/Send_request', methods=['post'])
def help():
    db = Db()
    user_id = request.form['lid']
    did = request.form['id']
    latitude = request.form['lati']
    longitude = request.form['longi']
    place = request.form['place']
    qry = "insert into request values('','" + user_id + "','" + did + "',now(),'pending','" + latitude + "','" + longitude + "','" + place + "')"
    res = db.insert(qry)
    # qry1 = "insert into user_location values('','" + user_id + "','" + latitude + "','" + longitude + "')"
    # res2 = db.insert(qry1)
    res1 = {}
    res1['status'] = 'ok'
    return demjson.encode(res1)


@app.route('/approve_request', methods=['post'])
def approve_request():
    db = Db()

    id = request.form['id']
    qry = "update request set status='accepted' where request_id='" + id + "'"
    db.update(qry)
    res1 = {}
    res1['status'] = 'ok'
    return demjson.encode(res1)


@app.route('/reject_request', methods=['post'])
def reject_request():
    db = Db()
    id = request.form['id']
    qry = "update request set status='rejeted' where request_id='" + id + "'"
    db.update(qry)
    res1 = {}
    res1['status'] = 'ok'
    return demjson.encode(res1)


@app.route('/category', methods=['post'])
def category():
    db = Db()
    qry = "select * from category"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/add_vehicle', methods=['post'])
def add_vehicle():
    db = Db()
    vno = request.form['vn']
    vtyp1 = request.form['vt']
    seat = request.form['s']
    cat = request.form['c']
    id = request.form['lid']
    qry = "insert into vehicle values('','" + id + "','" + vtyp1 + "','" + vno + "','" + seat + "','" + cat + "')"
    db.insert(qry)
    res1 = {}
    res1['status'] = 'vehicle added'
    return demjson.encode(res1)


@app.route('/view_request_status', methods=['post'])
def view_request_status():
    db = Db()
    lid = request.form['lid']
    qry = "select * from request,driver,vehicle where driver.driver_id=request.driver_id and driver.driver_id=vehicle.driver_id and request.user_id='" + lid + "'"
    res = db.select(qry)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/View_request_from_user', methods=['post'])
def View_request_from_user():
    db = Db()
    did = request.form['did']
    qry = "select * from user,request where user.user_id=request.user_id and request.driver_id='" + did + "' and request.status='pending'"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)

@app.route('/View_accepted_request_from_user', methods=['post'])
def View_accepted_request_from_user():
    db = Db()
    did = request.form['did']
    qry = "select * from user,request where user.user_id=request.user_id and request.driver_id='" + did + "' and request.status='accepted'"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/view_vehicle', methods=['post'])
def view_vehicle():
    db = Db()
    id = request.form['lid']
    qry = "select * from vehicle where driver_id='" + id + "'"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/delete_v', methods=['post'])
def delete_v():
    db = Db()
    id = request.form['id']
    qry = "delete from vehicle where vehicle_id='" + id + "'"
    db.delete(qry)
    res1 = {}
    res1['status'] = 'ok'
    return demjson.encode(res1)


@app.route('/category1', methods=['post'])
def category1():
    db = Db()
    qry = "select * from category"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/view_driver_cat', methods=['post'])
def view_driver_cat():
    db = Db()
    lati = request.form['lati']
    print(lati)
    longi = request.form['longi']
    print(longi)
    # place=request.form['place']
    cat = request.form['c']
    print(cat)
    qry = "select driver.*,location.*,vehicle.*,category.*, (3959 * ACOS ( COS ( RADIANS('" + str(
        lati) + "') ) * COS( RADIANS( location.latitude) ) * COS( RADIANS( location.longitude ) - RADIANS('" + str(
        longi) + "') ) + SIN ( RADIANS('" + str(
        lati) + "') ) * SIN( RADIANS( location.latitude ) ))) AS user_distance FROM location,driver,vehicle,category HAVING user_distance  < 6.2137 and driver.driver_id=vehicle.driver_id and driver.driver_id=location.driver_id and vehicle.category_id=category.id and vehicle.category_id='" + cat + "'"
    # qry = "select * from driver,vehicle where driver.driver_id=vehicle.driver_id and driver.longitude LIKE and driver.longitude like '%longi%' and driver.place like '%place%'"
    # qry="SELECT driver_id, (6371 * ACOS (COS ( RADIANS(latitude) )* COS( RADIANS( lati ))* COS( RADIANS( longi ) - RADIANS($longitude) )+ SIN ( RADIANS(latitude) )* SIN( RADIANS( lati ) )) AS distance FROM driver HAVING distance < 30 ORDER BY distance LIMIT 0 , 20;"
    res = db.select(qry)
    print(res)
    res1 = {}
    res1['status'] = 'ok'
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/and_del_complaint',methods=['post'])
def and_del_complaint():
    db = Db()
    complaint_id = request.form['cid']
    print(complaint_id)
    qry = "delete from complaint where cid='" + complaint_id + "'"
    db.delete(qry)
    res1 = {}
    res1['status'] = 'ok'
    return demjson.encode(res1)
@app.route('/and_del_request',methods=['post'])
def and_del_request():
    db = Db()
    id = request.form['rid']
    qry = "delete from request where request_id='" + id + "'"
    db.delete(qry)
    res1 = {}
    res1['status'] = 'ok'
    return demjson.encode(res1)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
