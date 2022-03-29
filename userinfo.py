import json
from getStars import rate_service


class Userinfo:
    """Collect info about user and his opinion"""

    def __init__(self):
        # Frame
        self.frame = {
            'amount_of_users': int(),

        }
        # Pattern
        self.usr = {
            'user_id': int(),
            'username': 'username',
            'user_location': 'user_location',
            'used_application': 'website_url',
            'stars': int(),
            'good_reasons': 'others',
            'bad_reasons': 'others',
        }
        # Lists of reasons
        self.bad_reasons = ['slow working', 'poor customer support', 'low quality products']
        self.good_reasons = ['fast working', 'good customer support', 'high quality products', 'nothing']

    def get_user_info(self):
        """Asks people for their username and opinion"""
        bad_reasons = self.bad_reasons
        good_reasons = self.good_reasons
        good_other = ''
        bad_other = ''
        new_user = self.usr.copy()
        new_user['username'] = input(f"\nEnter your name: ")
        # user_1['user_info']['user_location'] - DATA COLLECTED FROM WEBSITE
        # user_1['user_info']['used_application'] - THE WEBSITE
        new_user['stars'] = rate_service()
        new_user['user_id'] = len(self.frame)
        print(f"\nWhat did you like the most about our website? (choose from 1 to 4 describe your opinion by words):")
        i = 1
        for greason in good_reasons:
            print(f"{i} - {greason.title()}")
            i += 1
        greason_num = input("Enter your answer: ")
        if greason_num in str(list(range(1, 5))):
            new_user['good_reasons'] = good_reasons[int(greason_num) - 1]
        else:
            good_other = greason_num
            new_user['good_reasons'] = good_other
        choice = input("Is there anything you didn't like about our website?(yes/no): ")
        j = 1
        if choice == 'yes':
            print(f"\nWhat didn't you like about our website? (choose from 1 to 3 or describe your problem by words): ")
            for breason in bad_reasons:
                print(f"{j} - {breason.title()}")
                j += 1
            breason_num = input("Enter your answer: ")
            if breason_num in str(list(range(1, 4))):
                new_user['bad_reasons'] = bad_reasons[int(breason_num) - 1]
            else:
                bad_other = breason_num
                new_user['bad_reasons'] = bad_other

        return new_user
