from functools import wraps
import mysql.connector
from flask import  make_response,request
import re
import jwt
from jwt import ExpiredSignatureError
import json
from config.config import db_config

class auth_model:

    def __init__(self):
        # connection establish
        try:
            self.con=mysql.connector.connect(host=db_config["host"], user=db_config["user"], password=db_config["password"], database=db_config["database"])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("connection success")
        except:
            print("connection failed because of error")


    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func)

            def innner2(*args):

                endpoint = request.url_rule
                

                token = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$",token ):
                    split_token = token.split(" ")[1]
                    # print(split_token)
                    try:
                        jwt_decode = jwt.decode(split_token,key="vatsaly",algorithms=["HS256"])
                        
                    except ExpiredSignatureError:
                        return make_response({"error_message":"token expired"},401)
                    
                    role_id = jwt_decode["payload"]["role_id"]

                    self.cur.execute(f"select roles from accessibility_view where endpoint   = '{endpoint}'")
                    
                    result = self.cur.fetchall()
                    
                    if len(result) > 0:
                        roles = json.loads(result[0]['roles'])
                        if role_id in roles:
                            return func(*args)
                        else:
                             return make_response({"message":"something went wrong your role is not valid"},401)                      
                    else:
                        return make_response({"message":"unauthorized"},401)                   
                else:
                    return make_response({"message":"invalid token"},401)                         
            return innner2
        return inner1