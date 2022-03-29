import os.path
import json
from getNewUser import NewUser
from DataVisualisation import Visualize
file_json = 'user_data/user_info.json' # - file with information about users
file_csv = 'visualization_data/user.csv' # - file with data prepared to visualize
# user = NewUser(file_json) - create a file if there is not any
# user.get_new_user() - create new user inside 'file_json'
user_csv = Visualize(file_json) # - prepare data to csv formatting
user_csv.make_visualization(file_csv, 'stars', 'reasons', 'count') # - store data to csv format and plot an animated bar chart