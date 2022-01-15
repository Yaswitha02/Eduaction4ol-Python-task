def choices():
    print("For Signing up enter choice as '1'")
    print("For Login enter choice as '2'")
    print("For Forget Password enter choice as '3'")
    print("For Delete Account enter choice as '4'")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        return getdetails()
    elif(choice==2):
        return checkdetails()
    elif(choice==3):
        return modify()
    elif(choice==4):
        return terminate()
    else:
        print("Invalid choice")
def getdetails():
    print("   SIGN UP  ")
    print("Please provide details for signup")
    name=input("Name:")
    password=input("Password:")
    email=input("Please enter valid email id:")
    f=open("User_Data.txt",'+r')
    info = f.read()
    for line in f:
        if name in line:
            return "Name Unavailable.Please Try again"
            f.close()
        else:
            f=open("User_Data.txt",'w')
            info = info + " "+name + " " + password
            f.write(info)
            f.close()
def checkdetails():
    print("  LOG IN  ")
    print("Please provide login details")
    name=input("Name:")
    password=input("Password:")
    f=open("User_Data.txt",'+r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        user_password = info[index]
        if user_password == password:
            return "Welcome Back, "+ name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found.Please Sign up."
def modify():
    print("  FORGET PASSWORD  ")
    f=open("User_Data.txt","+r")
    flag=False
    name=input('Please enter your name: ')
    email=input('Please enter your email id: ')
    for line in f:
        if email in line:
            re_password=input('Please enter the password that you want to change: ')
            f=open("User_Data.txt").read()
            filter_file=open("dup.txt","w+")
            filter_file.write(f)
            f=open("data.txt","w+")
            for line in filter_file:
                if name and email and password not in line:
                    f.write(line)
            f=open("data.txt","a+")
            f.write("Name: "+name)
            f.write("Email_id: "+email)
            f.write("Password: "+re_password+"\r\n")
            f.close()
            print('Sucessfully updated!!!')
            f.close()
            flag=True
            break
    if flag==False:
        print('Invalid email!!!')
def terminate():
    print("  DELETE ACCOUNT  ")
    email=input('Please enter your email id: ')
    f=open("data.txt").read()
    filter_file=open("dup.txt","w+")
    filter_file.write(f)
    f=open("data.txt","w+")
    for line in filter_file:
        if email not in line:
            f.write(line)
        else:
            pass
    print('Sucessfully deleted!!!')
    f.close()
print(choices())                                                                                                      

