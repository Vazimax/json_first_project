import json

user = {}

with open('user.json') as s:
    user = json.load(s)
print(f" the email is :{user['email']}, And the password is :{user['password']}")

user['password'] = "Sorry i've changed your password"
with open('user.json','w') as w:
    json.dump(user,w)

print(f"the new password is : {user['password']} ")
