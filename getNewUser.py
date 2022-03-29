from userinfo import Userinfo
from clearFile import file_clear
import json
import os.path


class NewUser:
    """REPRESENTS NEW USER"""

    def __init__(self, filename):
        # Filename including path "path/to/filename"
        self.filename = filename

    def create_new_file(self):
        """Creates new file"""
        filename = self.filename
        userinfo = Userinfo()
        if not os.path.isfile(filename):
            with open(filename, 'w') as wf:
                json.dump(userinfo.frame, wf)

    def get_new_user(self):
        """Creates new user"""
        userinfo = Userinfo()
        user_func = userinfo.get_user_info()
        filename = self.filename
        if not os.path.isfile(filename):
            self.create_new_file()
        with open(filename, 'r') as user_read:
            content = json.load(user_read)
        content[f"user{len(content)}"] = user_func
        content['amount_of_users'] = int(len(content) - 1)
        user_func['user_id'] = len(content) - 1
        with open(filename, 'w') as u_json:
            json.dump(content, u_json, indent=4)
