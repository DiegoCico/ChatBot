import Response

user = ""
print("Welcome to ChatBot")
print("Type exit to exit the chat")

while user=="exit":
    user = input("> ")
    Response.determineCategory(user)

