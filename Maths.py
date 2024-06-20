logged =False
if(logged==False):
    user_name = input("What is your name ?")
    logged == True
message=True
msg = (">")

while (message ==True):
    if(message):
       msg = input(">")
       send_msg = (f"[{user_name}] {msg}")
       message = True
       print(send_msg)
    else:
        print("error")




