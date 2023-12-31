import os
from bs4 import BeautifulSoup

# Get the current working directory
current_dir = os.getcwd()

# Define the path to the HTML file
file_path = os.path.join(current_dir, 'Process', 'html_content.txt')

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # extract information user from HTML
    user_info_divs = soup.find_all('div', class_='x1dm5mii')

    for user_info_div in user_info_divs:
        # find url profile picture
        img_tag = user_info_div.find('img', draggable='false')
        if img_tag:
            profile_url = img_tag.get('src')
        else:
            profile_url = "Profile URL not found"

        # find username
        username_tag = user_info_div.find('span', class_='_ap3a')
        username = username_tag.get_text() if username_tag else "Username not found"

        # find full name
        full_name_tag = user_info_div.find('span', class_='x1lliihq')
        full_name = full_name_tag.text if full_name_tag else "Full name not found"

        print(f"Username: {username}")
        print(f"Full Name: {full_name}")
        print(f"Profile URL: {profile_url}")
        print("------")

else:
    print(f"File not found: {file_path}")
