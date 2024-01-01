import pandas as pd

# read csv data
df_followers = pd.read_csv('03_results_folder/followers_data.csv')
df_following = pd.read_csv('03_results_folder/following_data.csv')

# count the number of unique usernames
followers_count = df_followers['username'].nunique()
following_count = df_following['username'].nunique()

print('followers and following count:')
print(f"followers count: {followers_count}")
print(f"following count: {following_count}")

print('\ndataframes of followers:')
print(df_followers)

print('\ndataframes of following:')
print(df_following)