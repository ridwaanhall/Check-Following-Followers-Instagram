from bs4 import BeautifulSoup

html_content = """

"""

soup = BeautifulSoup(html_content, 'html.parser')

# Mengekstrak informasi pengguna dari HTML
user_info_divs = soup.find_all('div', class_='x1dm5mii')

for user_info_div in user_info_divs:
    # Mendapatkan URL profil
    img_tag = user_info_div.find('img', draggable='false')
    if img_tag:
        profile_url = img_tag.get('src')
    else:
        profile_url = "Profile URL not found"

    # Mendapatkan nama pengguna
    username_tag = user_info_div.find('span', class_='_ap3a')
    username = username_tag.get_text() if username_tag else "Username not found"

    # Mendapatkan nama lengkap
    full_name_tag = user_info_div.find('span', class_='x1lliihq')
    full_name = full_name_tag.text if full_name_tag else "Full name not found"

    print(f"Username: {username}")
    print(f"Full Name: {full_name}")
    print(f"Profile URL: {profile_url}")
    print("------")