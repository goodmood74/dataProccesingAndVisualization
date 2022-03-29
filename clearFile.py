import json
from userinfo import Userinfo

user_json = 'data/user_info.json'
userinfo = Userinfo()
def file_clear():
    with open(user_json, 'w') as main_dict:
        json.dump(userinfo.frame, main_dict, indent=4)