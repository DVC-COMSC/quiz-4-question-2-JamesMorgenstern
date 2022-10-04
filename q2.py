userList = []
userData = input()

while True:
    userList.append(userData)
    userData = input()
    if (userData == "STOP" or userData == "stop"):
        break

smallest = userList[0]
largest = userList[0]
count = 0

for i in range(len(userList)):
    if (len(userList[i]) <= len(smallest)):
        smallest = userList[i]

    if (len(userList[i]) >= len(largest)):
        largest = userList[i]

print(smallest, largest)
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
