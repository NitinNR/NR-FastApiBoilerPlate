from env import getValue
from fastapi.responses import JSONResponse

def authenticate_user(req):
    authorization = req.headers.get("Authorization","null")
    if not authorization or not authorization.startswith("Bearer "):
        return {"status":False,"message":"please check bearer token !"}

    access_token = getValue("ACCESS_TOKEN")
    
    if(authorization == "null"):
        return {"status":False,"message":"access token not pass !"}
    
    user_access_token = authorization.split(" ")[1]
    if(user_access_token == access_token):
        return {"status":True,"message":"valid token"}
    else:
        return {"status":False,"message":"invalid token!"}
