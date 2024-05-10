from django.contrib.auth.hashers import make_password, check_password
def hashPassword(password):
    hashed_pwd = make_password(password)
    check_password(password,hashed_pwd) 
    print(hashed_pwd)

