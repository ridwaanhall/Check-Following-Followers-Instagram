import os
import csv
from bs4 import BeautifulSoup
from datetime import datetime

class FollowingDataExtractor:
    def __init__(self, html_file_path, output_folder):
        self.html_file_path = html_file_path
        self.output_folder = output_folder

    def extract_following_data(self):
        if os.path.exists(self.html_file_path):
            with open(self.html_file_path, 'r', encoding='utf-8') as file:
                following_html = file.read()

            soup = BeautifulSoup(following_html, 'html.parser')
            user_info_divs = soup.find_all('div', class_='x1dm5mii')

            # Get today's date
            today = datetime.now().strftime('%Y_%m_%d')

            # Create file names with the current date
            csv_file_path = os.path.join(self.output_folder, f'{today}_following.csv')
            txt_file_path = os.path.join(self.output_folder, f'{today}_following.txt')

            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file, \
                 open(txt_file_path, 'w', encoding='utf-8') as txt_file:

                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['username', 'name', 'profile_url'])

                for user_info_div in user_info_divs:
                    img_tag = user_info_div.find('img', draggable='false')
                    profile_url = img_tag.get('src') if img_tag else "Profile URL not found"

                    username_tag = user_info_div.find('span', class_='_ap3a')
                    username = username_tag.get_text() if username_tag else "Username not found"

                    full_name_tag = user_info_div.find('span', class_='x1lliihq')
                    full_name = full_name_tag.text if full_name_tag else "Full name not found"

                    csv_writer.writerow([username, full_name, profile_url])
                    txt_file.write(f"username: {username}\nname: {full_name}\nprofile_url: {profile_url}\n------\n")
                    print(f'User with username: {username} has been saved')

            print(f"Output saved to {csv_file_path} and {txt_file_path}")
        else:
            print(f"File not found: {self.html_file_path}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    html_file_path = os.path.join(current_dir, '00_html_folder', 'v3_following_html.txt')
    output_folder = os.path.join(current_dir, '03_results_folder', 'following')
    
    extractor = FollowingDataExtractor(html_file_path, output_folder)
    extractor.extract_following_data()
