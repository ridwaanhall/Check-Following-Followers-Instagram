import pandas as pd

# Read CSV data
df_followers = pd.read_csv('03_results_folder/followers_data.csv')
df_following = pd.read_csv('03_results_folder/following_data.csv')

# Get lists of followers and following
followers_list = df_followers['username'].tolist()
following_list = df_following['username'].tolist()

# Find out who follows you
followers_of_you = set(followers_list)

# Find out who you follow
following_by_you = set(following_list)

# Find out who you follow but doesn't follow you back
not_following_back = following_by_you - followers_of_you

# Find out who follows you but you don't follow back
not_followed_back = followers_of_you - following_by_you

# Find out who follows each other
follow_each_other = followers_of_you.intersection(following_by_you)


# Save the data to a text file
with open('03_results_folder/instagram_data.txt', 'w') as file:
    file.write('data : {\n')
    file.write(f"    'followers_of_you': {followers_of_you},\n")
    file.write(f"    'following_by_you': {following_by_you},\n")
    file.write(f"    'not_following_back': {not_following_back},\n")
    file.write(f"    'not_followed_back': {not_followed_back},\n")
    file.write(f"    'follow_each_other': {follow_each_other}\n")
    file.write('}\n')


# Print or use the results as needed
print('this is count of users who:')
print(f"Followers of you                       : {len(followers_of_you)}")
print(f"Following by you                       : {len(following_by_you)}")
print(f"You are followed but don't follow back : {len(not_followed_back)}")
print(f"Follow each other                      : {len(follow_each_other)}")
print(f"YOU FOLLOW BUT DON'T FOLLOW BACK       : {len(not_following_back)}")