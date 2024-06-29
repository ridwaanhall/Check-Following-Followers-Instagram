import pandas as pd
from datetime import datetime


class SocialMediaData:
    def __init__(self, followers_file, following_file):
        self.df_followers = pd.read_csv(followers_file)
        self.df_following = pd.read_csv(following_file)

    def count_unique_users(self):
        followers_count = self.df_followers['username'].nunique()
        following_count = self.df_following['username'].nunique()
        return followers_count, following_count

    def display_followers(self):
        print('Dataframes of followers:')
        print(self.df_followers)

    def display_following(self):
        print('\nDataframes of following:')
        print(self.df_following)

if __name__ == "__main__":
    date_str = datetime.now().strftime('%Y_%m_%d')
    social_media_data = SocialMediaData('03_results_folder/followers/' + date_str + '_followers.csv', '03_results_folder/following/' + date_str + '_following.csv')
    
    followers_count, following_count = social_media_data.count_unique_users()
    print('Followers and following count:')
    print(f"Followers count: {followers_count}")
    print(f"Following count: {following_count}")

    social_media_data.display_followers()
    social_media_data.display_following()
