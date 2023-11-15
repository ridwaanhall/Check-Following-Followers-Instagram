import os
import csv
import openpyxl
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

    # Extract information about users from HTML
    user_info_divs = soup.find_all('div', class_='x1dm5mii')

    # Write to CSV file
    csv_file_path = os.path.join(current_dir, 'followers_data.csv')
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write header row to CSV file
        csv_writer.writerow(['Username', 'name', 'profile_url'])

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

            # Print the information to the console
            print(f"Username: {username}")
            print(f"Full Name: {full_name}")
            print(f"Profile URL: {profile_url}")
            print("------")

    print(f"Output saved to followers_data.csv")

    # Write to Excel file (xlsx)
    excel_file_path = os.path.join(current_dir, 'followers_data.xlsx')
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write header row to Excel file
    sheet.append(['Username', 'name', 'profile_url'])

    for user_info_div in user_info_divs:
        img_tag = user_info_div.find('img', draggable='false')
        profile_url = img_tag.get('src') if img_tag else "Profile URL not found"

        username_tag = user_info_div.find('span', class_='_ap3a')
        username = username_tag.get_text() if username_tag else "Username not found"

        full_name_tag = user_info_div.find('span', class_='x1lliihq')
        full_name = full_name_tag.text if full_name_tag else "Full name not found"

        # Write the information to the Excel file
        sheet.append([username, full_name, profile_url])

    workbook.save(excel_file_path)
    print(f"Output saved to followers_data.xlsx")

else:
    print(f"File not found: {file_path}")
