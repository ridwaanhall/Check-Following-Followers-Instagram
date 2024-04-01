import pandas as pd
import os
from urllib.request import urlretrieve

class SocialMediaAnalyzer:
    def __init__(self, following_file):
        self.df_following = pd.read_csv(following_file)

    def download_profile_pictures(self, folder_name='04_profile_pictures/images_following'):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for index, row in self.df_following.iterrows():
            username = row['username']
            profile_url = row['profile_url']
            if pd.notnull(profile_url):
                try:
                    filename = f'{folder_name}/{username}.jpg'
                    urlretrieve(profile_url, filename)
                    print(f"Profile picture for {username} downloaded successfully.")
                except Exception as e:
                    print(f"Failed to download profile picture for {username}: {str(e)}")
            else:
                print(f"Skipping {username} because profile URL is not provided.")

if __name__ == "__main__":
    analyzer = SocialMediaAnalyzer('03_results_folder/following_data.csv')
    analyzer.download_profile_pictures()
