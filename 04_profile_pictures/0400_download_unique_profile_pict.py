import pandas as pd
import os
from urllib.request import urlretrieve
from datetime import datetime

class SocialMediaAnalyzer:
    def __init__(self, following_file, followers_file):
        self.df_following = pd.read_csv(following_file)
        self.df_followers = pd.read_csv(followers_file)

    def download_unique_profile_pictures(self, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Combine and drop duplicates
        combined_df = pd.concat([self.df_following, self.df_followers]).drop_duplicates(subset='username')
        
        for index, row in combined_df.iterrows():
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

if __name__ == "__main__":
    date_str = datetime.now().strftime('%Y_%m_%d')
    
    following_file = f'03_results_folder/following/{date_str}_following.csv'
    followers_file = f'03_results_folder/followers/{date_str}_followers.csv'
    
    analyzer = SocialMediaAnalyzer(following_file, followers_file)
    
    folder_name_unique = f"03_results_folder/profile_pict_unique/{date_str}_profile_pict_unique"
    analyzer.download_unique_profile_pictures(folder_name_unique)
