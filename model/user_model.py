import mysql.connector
from flask import make_response
import requests
from datetime import datetime, timedelta
import jwt
from config.config import db_config
class user_model:


    def __init__(self):
        # connection establish
        try:
            self.con=mysql.connector.connect(host=db_config["host"], user=db_config["user"], password=db_config["password"], database=db_config["database"])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("connection success")
        except:
            print("connection failed because of error")


    def user_getall_singup(self):
        self.cur.execute("select * from user")
        self.result = self.cur.fetchall()

        if len(self.result) > 0:
            res = make_response({"payload":self.result},200)  
            
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res
        else:
            return make_response({"message":"No data found"} ,204)
        

    def user_getadd_model(self,data):
        self.cur.execute(f"INSERT INTO user(id,name,email,phone,password,avatar,role_id) VALUES('{data['id']}','{data['name']}','{data['email']}','{data['phone']}','{data['password']}.','{data['avatar']}','{data['role_id']}')")
        # print(data)
        return make_response({"message":"user_getall_model successfully"},201)
    

    def user_addmultiple_model(self,data):
        qry = "INSERT INTO user(id,name,email,phone,password,avatar,role_id) VALUES"
        for i in data:
            qry += f"('{i['id']}','{i['name']}','{i['email']}','{i['phone']}','{i['password']}','{i['avatar']}','{i['role_id']}'),"
        final_qry = qry.rstrip(",")
        print(final_qry)
        self.cur.execute(final_qry)
        return make_response({"message":"create multiple user successfully"},201)


    def user_update_model(self,data):
        self.cur.execute(f"UPDATE user SET id='{data['id']}' ,name='{data['name']}',email='{data['email']}',phone='{data['phone']}',password='{data['password']}', WHERE id = '{data['id']}'")
        if self.cur.rowcount > 0:
            return make_response({"message":"user data updated successfully"},201)
        else:
            return make_response({"message":"user data update failed"},202)
        

    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM user WHERE id = '{id}'")
        if self.cur.rowcount > 0:
            return make_response({"message":"user data is deleted successfully"},201)
        else:
            return make_response({"message":"user data deleted failed"},202)


    def user_PATCH_model(self,data,id):
        qry = "UPDATE user SET "

        for key in data:
            qry += f"{key} = '{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {id}"

        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message":"user data updated successfully"},201)
        else:
            return make_response({"message":"user data update failed"},202)
        

    def user_pagination_model(self,limit,page):
        limit = int(limit)
        page = int(page)

        start = (page * limit ) - limit
        qry = f"select * from user limit {start},{limit}"
        self.cur.execute(qry)
        self.result = self.cur.fetchall()

        if len(self.result) > 0:
            res = make_response({"payload":self.result,"page":page,"limit":limit},200)  
            return res
        else:
            return make_response({"message":"No data found"} ,204)


    def user_avtar_model(self,uid,filepath):
        self.cur.execute(f"UPDATE user SET avatar = '{filepath}' WHERE id = '{uid}'")
        if self.cur.rowcount > 0:
            return make_response({"message":"file uploaded successfully","filepath":filepath},201)
        else:
            return make_response({"message":"file upload failed"},202)
       

    def user_login_model(self,data):
        self.cur.execute(f"select id,name,email,phone,avatar,role_id,password from user where email = '{data['email']}' and password = '{data['password']}'")
        result = self.cur.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time = int(exp_time.timestamp())

        payload=  {
            "payload":userdata,
            "exp":exp_epoch_time
        }
        jwt_token = jwt.encode(payload, "vatsaly", algorithm="HS256")
        
        return make_response({"token":jwt_token},200)

        # INSERT INTO `flask_api`.`user` (`id`, `name`, `email`, `phone`, `password`, `role_id`) VALUES ('3', 'hit ', 'hit@gmail.com', '123456783', 'hit123', '12');
