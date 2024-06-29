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
        not_followed_back = followers_of_you - following_by_you
        not_following_back = following_by_you - followers_of_you
        follow_each_other = followers_of_you.intersection(following_by_you)
        return followers_of_you, following_by_you, not_followed_back, not_following_back, follow_each_other

    def print_summary(self):
        followers_of_you, following_by_you, not_followed_back, not_following_back, follow_each_other = self.find_relationships()
        print('This is the count of users who:')
        print(f"Followers of you                       : {len(followers_of_you)}")
        print(f"Following by you                       : {len(following_by_you)}")
        print(f"You are followed but don't follow back : {len(not_followed_back)}")
        print(f"Follow each other                      : {len(follow_each_other)}")
        print(f"YOU FOLLOW BUT DON'T FOLLOW BACK       : {len(not_following_back)}")

    def print_user_lists(self):
        followers_of_you, following_by_you, not_followed_back, not_following_back, follow_each_other = self.find_relationships()
        print('\nThis is the list of users:')
        print('Followers of you (followers):', followers_of_you)
        print('\nFollowing by you (following):', following_by_you)
        print('\nFollowers of you who you don\'t follow back:', not_followed_back)
        print('\nFollow each other:', follow_each_other)
        print('\nUsers who you follow but don\'t follow you back:', not_following_back)

if __name__ == "__main__":
    date_str = datetime.now().strftime('%Y_%m_%d')
    analyzer = SocialMediaAnalyzer('03_results_folder/followers/' + date_str + '_followers.csv', '03_results_folder/following/' + date_str + '_following.csv')
    analyzer.print_summary()
    analyzer.print_user_lists()
