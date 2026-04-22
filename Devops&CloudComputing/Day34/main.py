# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("data.txt", "w") as file:
#     file.write("Hello World")


with open("data.txt", "a") as file:
    file.write("\n This is devops and cloud computing class")