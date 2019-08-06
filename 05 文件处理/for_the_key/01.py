

with open('test.py') as f:
    lines = f.readlines()[-10:]
    for line in lines:
        print(line)


