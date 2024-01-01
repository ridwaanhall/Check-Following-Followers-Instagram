# Check Following Followers Instagram
![Sample Result](images/checking_data_v.1.0.0.png "This is the result of my awesome project.")

## Confused
if you are confused, just run all scripts from the `01_process` directory to `02_analyze` directory and make sure you change the data in `00_html_folder` with filename `v3_followers_html.txt` and `v3_following_html.txt` with step in 'Before Usage (DON'T SKIP THIS STEP)'. or [message me](https://url.erbyl.repl.co/contact) for the tutorial.


## Description
This project serves as a tool for processing and analyzing data. It provides insights into our followers, following, mutual followers, and users we follow but who don't follow back.

## Installation
1. Make sure you have Python installed on your computer. [Download Python](https://www.python.org/downloads/)
2. Download the project or copy the code into your project.
3. Install the required librarys.

## Install Librarys
1. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) or install with [pip](https://pypi.org/project/beautifulsoup4/)
```bash
pip install beautifulsoup4
```
2. [pandas](https://pandas.pydata.org/) or install with [pip](https://pypi.org/project/pandas/)
```bash
pip install pandas
```
3. You can combine the installation with the following command:
```bash
pip install beautifulsoup4 pandas
```

4. If you got any errors, please [contact me](https://url.erbyl.repl.co/contact).


## Before Usage (DON'T SKIP THIS STEP)
![How to use](images/how_to_use_v.2.0.0.png "How to use")
![How to use](images/how_to_use_v.2.1.0.png "How to use")
1. Open your instagram account and navigate to the following page: https://www.instagram.com/username/
2. Click on the "Followers" button.
3. Inspect the followers page, make to **mobile interface**, and extract the HTML code. Make sure to scroll down to the bottom of the page.
4. Click on the "Following" button.
5. Inspect the following page, make to **mobile interface**, and extract the HTML code. Make sure to scroll down to the bottom of the page.
6. Copy and paste the HTML code into a text file.
7. For followers, place the HTML code in the `00_html_folder` directory with the name `v3_followers_html.txt`.
8. For following, place the HTML code in the `00_html_folder` directory with the name `v3_following_html.txt`.

## Usage
1. Place change data inside the txt file from an Instagram follower and following in the `00_html_folder` directory with the name `v3_followers_html.txt` and `v3_following_html.txt`.
2. Run the script in folder `01_process/03_save_followers_data.py` to extract and save follower data.
3. Run the script in folder `01_process/04_save_following_data.py` to extract and save following data.
4. View the results in foldername `03_results_folder` with filename is `followers_data.csv`, `followers_data.txt`, `following_data.csv`, `following_data.txt`, and `instagram_data.txt` files.
5. In the `02_analyze` directory, run the script `01_knowing_data.py`. This script will analyze the data and show followers and following counts.
6. In the `02_analyze` directory, Run the script `02_checking_data.py`. This script will analyze the data and show users we follow, users who follow us, users who don't follow us back, users we don't follow but follow us, and users who follow each other with us. with add list of users who don't follow back.
7. In the `02_analyze` directory, Run the script `03_saving_output.py`. This script will save the output in the `03_results_folder/instagram_data.txt`.

## Feedback
If you have any feedback or suggestions, please [contact me](https://url.erbyl.repl.co/contact).

## Contribution
If you would like to contribute to this project, please create a pull request and let us know about the proposed changes.

## License
This project is licensed under the MIT License.

---
**Note**: Be sure to replace or adjust certain sections as needed for your project's specifics. For followers and following under 1500.
