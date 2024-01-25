import json

a = User_data = {
    "arman": '1234'
}
dump = json.dumps(a)
with open('pass.json', mode='w') as f:
    f.write(dump)

