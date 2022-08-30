#Import like db
from like_db import LikeDB

#Create like db
like_db = LikeDB('like_db.json')
#Add a like to the database
user_id = '456'
ans=like_db.add_like(user_id=user_id)
ans=like_db.add_like(user_id=user_id)
ans=like_db.add_like(user_id=user_id)
print(ans)
ans2 = like_db.add_dislike(user_id=user_id)
print(ans2)
