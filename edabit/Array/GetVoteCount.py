def get_vote_count(dict1):
   keys = list(dict1.keys())
   return dict1[keys[0]] - dict1[keys[1]]


print(get_vote_count({ "upvotes": 13, "downvotes": 0 })) # 13

print(get_vote_count({ "upvotes": 2, "downvotes": 33 })) # -31

print(get_vote_count({ "upvotes": 132, "downvotes": 132 })) # 0
