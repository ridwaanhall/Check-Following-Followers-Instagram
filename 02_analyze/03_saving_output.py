import pandas as pd
from datetime import datetime

class SocialMediaAnalyzer:
    def __init__(self, followers_file, following_file):
        self.df_followers = pd.read_csv(followers_file)
        self.df_following = pd.read_csv(following_file)
        self.followers_list = self.df_followers['username'].tolist()
        self.following_list = self.df_following['username'].tolist()

    def find_relationships(self):
        followers_of_you = set(self.followers_list)
        following_by_you = set(self.following_list)
        not_following_back = following_by_you - followers_of_you
        not_followed_back = followers_of_you - following_by_you
        follow_each_other = followers_of_you.intersection(following_by_you)
        return followers_of_you, following_by_you, not_following_back, not_followed_back, follow_each_other

    def save_to_file(self, filename):
        followers_of_you, following_by_you, not_following_back, not_followed_back, follow_each_other = self.find_relationships()
        with open(filename, 'w') as file:
            file.write('data : {\n')
            file.write(f"    'followers_of_you': {followers_of_you},\n")
            file.write(f"    'following_by_you': {following_by_you},\n")
            file.write(f"    'not_following_back': {not_following_back},\n")
            file.write(f"    'not_followed_back': {not_followed_back},\n")
            file.write(f"    'follow_each_other': {follow_each_other}\n")
            file.write('}\n')

    def print_summary(self):
        followers_of_you, following_by_you, not_following_back, not_followed_back, follow_each_other = self.find_relationships()
        print('This is the count of users who:')
        print(f"Followers of you                       : {len(followers_of_you)}")
        print(f"Following by you                       : {len(following_by_you)}")
        print(f"You are followed but don't follow back : {len(not_followed_back)}")
        print(f"Follow each other                      : {len(follow_each_other)}")
        print(f"YOU FOLLOW BUT DON'T FOLLOW BACK       : {len(not_following_back)}")

if __name__ == "__main__":
    today = datetime.now().strftime('%Y_%m_%d')
    followers_file = f'03_results_folder/followers/{today}_followers.csv'
    following_file = f'03_results_folder/following/{today}_following.csv'
    output_file = f'03_results_folder/data/{today}_data.txt'

    analyzer = SocialMediaAnalyzer(followers_file, following_file)
    analyzer.save_to_file(output_file)
    analyzer.print_summary()
