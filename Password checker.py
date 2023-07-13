# Get the password from the user
password = input("What's the password?")
min_lenght = 8
if len(password) < min_lenght:
    print("[-]increase your password lenght")
elif password.lower() == password or password.upper() == password:
    print("[-]mixed check failed")
elif not any([c.isdecimal() for c in password]):
    print("[-] include numbers for better password")
elif password.isalnum():
    print("[-] symbol test failed")
else:
    print("[-]Your password is good")
    