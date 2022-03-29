import json
import plotly.express as px
from userinfo import Userinfo
import pandas as pd
from csv import DictWriter, writer
import os.path


class Visualize:

    def __init__(self, filename):
        self.filename = filename
        #  Filename including path "path/to/filename"
        self.stars_dict = {
            '1stars': [],
            '2stars': [],
            '3stars': [],
            '4stars': [],
            '5stars': [],
            '6stars': [],
            '7stars': [],
            '8stars': [],
            '9stars': [],
            '10stars': [],
        }
        self.headers_csv = ['stars', 'reasons', 'count']
        self.reasons_axis = ['slow working', 'poor customer support', 'low quality products', 'fast working',
                             'good customer support', 'high quality products', 'nothing', 'other']

    def make_dict(self):
        """Makes a dict to store information in"""

        stars_dict = self.stars_dict
        with open(self.filename, 'r') as f:
            file_content = json.load(f)
        amount = file_content['amount_of_users']
        bad_reasons = Userinfo().bad_reasons
        good_reasons = Userinfo().good_reasons

        for x in range(1, 11):
            others = 0
            reasons_count = []
            for breason in range(3):
                breason_count = 0
                for user in range(1, amount + 1):
                    if file_content[f"user{user}"]['bad_reasons'] == bad_reasons[breason] and \
                            file_content[f"user{user}"]['stars'] == x:
                        breason_count += 1
                reasons_count.append(breason_count)

            for greason in range(len(good_reasons)):
                greason_count = 0
                for user in range(1, amount + 1):
                    if file_content[f"user{user}"]['good_reasons'] == good_reasons[greason] and \
                            file_content[f"user{user}"]['stars'] == x:
                        greason_count += 1
                reasons_count.append(greason_count)

            for user in range(1, amount + 1):
                if file_content[f"user{user}"]['good_reasons'] not in good_reasons and file_content[f"user{user}"]['stars'] == x:
                    others += 1
                elif file_content[f"user{user}"]['bad_reasons'] not in bad_reasons and file_content[f"user{user}"]['stars'] == x:
                    others += 1

            reasons_count.append(others)
            stars_dict[f"{x}stars"] = reasons_count

        print(stars_dict)

    def make_visualization(self, datafile, info_an, x_axis, y_axis):
        """Creates an animated bar chart"""
        self.make_dict()
        #  Filename including path "path/to/filename"
        if not os.path.isfile(datafile):
            with open(datafile, 'w') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=self.headers_csv)
                dictwriter_object.writeheader()
        with open(datafile, 'w') as f_object:
            writer_object = writer(f_object)
            dictwriter_object = DictWriter(f_object, fieldnames=self.headers_csv)
            # Pass the data in the dictionary as an argument into the writerow() function
            dictwriter_object.writeheader()
            list_of_values = [value for value in self.stars_dict.values()]
            i = 0
            for y in range(1, 11):
                j = 0
                for x in range(1, 9):
                    writer_object.writerow([y, self.reasons_axis[j], list_of_values[i][j]])
                    j += 1
                i += 1
            # Close the file object
            f_object.close()
        df = pd.read_csv(datafile)
        info_animation = df[info_an]
        x_axis = df[x_axis]
        y_axis = df[y_axis]
        # Create Animated Bar Chart and store figure as fig
        fig = px.bar(
            df,
            x=x_axis,
            y=y_axis,
            color=x_axis,
            animation_frame=info_animation,
            animation_group=x_axis,
            range_y=[0, 11]
        )
        fig.show()
