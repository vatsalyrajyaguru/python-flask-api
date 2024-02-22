from app import app
from model.user_model import user_model
from model.auth_model import auth_model
from flask import request,send_file

from datetime import datetime

obj = user_model()
auth = auth_model()

@app.route("/user/getall")
@auth.token_auth()
@auth.token_auth(endpoint="/user/getall")
def singup():
    return obj.user_getall_singup()

@app.route("/user/getone",methods=["POST"])
@auth.token_auth()
def user_getone():
    return obj.user_getadd_model(request.form)

@app.route("/user/addmultiple",methods=["POST"])
def user_addmultiple():
    return obj.user_addmultiple_model(request.json)

@app.route("/user/update",methods=["PUT"])
def user_update():
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_PATCH(id):
    return obj.user_PATCH_model(request.form,id)

@app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"])
def user_pagination(limit,page):
    return obj.user_pagination_model(limit,page)

@app.route("/user/avatar/<uid>/upload",methods=["PUT"])
def user_avtar(uid):
    file = request.files['avatar']
    
    uniq_name = str(datetime.now().timestamp()).replace(".","")
    filename= file.filename.split(".")
    ext = filename[len(filename)-1]

    filepath = f"upload/{uid}_{uniq_name}.{ext}"
    file.save(filepath)

    return obj.user_avtar_model(uid,filepath)

@app.route("/upload/<filename>")
def avatar_controller(filename):
    return send_file(f"/upload/{filename}")

@app.route("/user/login",methods=["POST"])
def user_login():
    return obj.user_login_model(request.form)