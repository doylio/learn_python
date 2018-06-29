import json

from user import User


with open('Shawn.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())