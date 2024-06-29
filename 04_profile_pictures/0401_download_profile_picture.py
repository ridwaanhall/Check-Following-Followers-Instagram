import pandas as pd
import os
from urllib.request import urlretrieve
from datetime import datetime

class SocialMediaAnalyzer:
    def __init__(self, following_file, followers_file):
        self.df_following = pd.read_csv(following_file)
        self.df_followers = pd.read_csv(followers_file)

    def download_profile_pictures(self, df, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for index, row in df.iterrows():
            username = row['username']
            profile_url = row['profile_url']
            if pd.notnull(profile_url):
                try:
                    filename = os.path.join(folder_name, f'{username}.jpg')
                    urlretrieve(profile_url, filename)
                    print(f"Profile picture for {username} downloaded successfully.")
                except Exception as e:
                    print(f"Failed to download profile picture for {username}: {str(e)}")
            else:
                print(f"Skipping {username} because profile URL is not provided.")

    def download_profile_pictures_following(self, folder_name_following):
        self.download_profile_pictures(self.df_following, folder_name_following)

    def download_profile_pictures_followers(self, folder_name_followers):
        self.download_profile_pictures(self.df_followers, folder_name_followers)

if __name__ == "__main__":
    date_str = datetime.now().strftime('%Y_%m_%d')
    
    following_file = f'03_results_folder/following/{date_str}_following.csv'
    followers_file = f'03_results_folder/followers/{date_str}_followers.csv'
    
    analyzer = SocialMediaAnalyzer(following_file, followers_file)
    
    folder_name_following = f"03_results_folder/profile_pict_following/{date_str}_profile_pict_following"
    analyzer.download_profile_pictures_following(folder_name_following)
    
    folder_name_followers = f"03_results_folder/profile_pict_followers/{date_str}_profile_pict_followers"
    analyzer.download_profile_pictures_followers(folder_name_followers)
