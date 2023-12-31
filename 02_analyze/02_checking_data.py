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


# Print or use the results as needed
print('this is count of users who:')
print(f"Followers of you                       : {len(followers_of_you)}")
print(f"Following by you                       : {len(following_by_you)}")
print(f"You are followed but don't follow back : {len(not_followed_back)}")
print(f"Follow each other                      : {len(follow_each_other)}")
print(f"YOU FOLLOW BUT DON'T FOLLOW BACK       : {len(not_following_back)}")


# list of users who follow you
print('\nthis is user who follow you (followers):')
print(followers_of_you)

# list of users who you follow them
print('\nthis is user who you follow them (following):')
print(followers_of_you)

# list of users who follow you, but dont follow back
print('\nthis is user who follow you, but you dont follow back:')
print(not_followed_back)

# list of users who follow each other
print('\nthis is user who follow each other:')
print(follow_each_other)

# list of users who don't follow you back
print('\nthis is user who don\'t follow you back:')
print(not_following_back)