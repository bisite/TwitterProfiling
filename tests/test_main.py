#Perform main tests

import time

from twitterprofiling import TwitterProfiling

consumer_key, consumer_secret, access_token, access_token_secret = ["aaaaaaaaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "cccccccccccccccccccccccccccccccccccccccccccccccccc", "ddddddddddddddddddddddddddddddddddddddddddddd"]

cat = TwitterProfiling('sciencemagazine', consumer_key, consumer_secret, access_token, access_token_secret)
print(cat.get_user_description())
print(cat.get_user_classification())
