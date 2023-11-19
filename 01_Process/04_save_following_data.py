import os
import csv
from bs4 import BeautifulSoup

# Get the current working directory
current_dir = os.getcwd()

# Define the path to the HTML file
file_path = os.path.join(current_dir, '01_process', 'following_html.txt')

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        following_html = file.read()

    soup = BeautifulSoup(following_html, 'html.parser')

    # Extract information about users from HTML
    user_info_divs = soup.find_all('div', class_='x1dm5mii')

    # Open a new CSV file for writing
    csv_file_path = os.path.join(current_dir, 'following_data.csv')
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header row to CSV file
        csv_writer.writerow(['username', 'name', 'profile_url'])

        # Open a new text file for writing
        txt_file_path = os.path.join(current_dir, 'following_data.txt')
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:

            for user_info_div in user_info_divs:
                # Find URL profile picture
                img_tag = user_info_div.find('img', draggable='false')
                if img_tag:
                    profile_url = img_tag.get('src')
                else:
                    profile_url = "Profile URL not found"

                # Find username
                username_tag = user_info_div.find('span', class_='_ap3a')
                username = username_tag.get_text() if username_tag else "Username not found"

                # Find full name
                full_name_tag = user_info_div.find('span', class_='x1lliihq')
                full_name = full_name_tag.text if full_name_tag else "Full name not found"

                # Write the information to the CSV file
                csv_writer.writerow([username, full_name, profile_url])

                # Write the information to the text file
                txt_file.write(f"username: {username}\n")
                txt_file.write(f"name: {full_name}\n")
                txt_file.write(f"profile_url: {profile_url}\n")
                txt_file.write("------\n")
                
                print(f'user with username: {username} has been saved')

        print(f"Output saved to following_data.csv and following_data.txt")

else:
    print(f"File not found: {file_path}")
