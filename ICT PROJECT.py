 # Project: School Management System

# Reading Class room members name from a file
import time
member_file=open("class_member.txt","r")
class_room=[]
count=1
for line in member_file:
    if count==1:
        count=2
    else:
        line=line.strip('\n')
        class_room.append(line)
member_file.close()
# Reading Password from a file
password_file= open("password.txt","r")
for line in password_file:
    password=line
password_file.close()
def change_password():
    password_file= open("password.txt","r")
    for line in password_file:
        password= line
    password_file.close()
    old_password= input("Enter your old Password")
    while old_password!=password:
        print("You Entered wrong password.")
        print("Try again!")
        old_password= input("Enter your old Password")
    if old_password==password:
        check=0
    password= input('Enter password. Your password must contain\n• At least 1 letter between [a-z] and 1 letter between [A-Z].\n• At least 1 number between [0-9].\n• At least 1 character from [$#@].\n• Minimum length 6 characters.\n• Maximum length 16 characters.')
    while check==0:
        #checking length
        condition= True
        if len(password)<6:
            print('Your Password must contain at least 6 characters.')
            condition= False
            check=0
        if len(password)>16:
             print('Your Password must not be more than 16 characters.')
             condition= False
             check=0
        #checking for a digit
        condition1= False
        for char in password:
            if char.isdigit(): 
                condition1= True
                check=0
        if condition1== False:
            print('Your Password does not contains a digit.')

        #checking for upper case
        condition2= False
        for char in password:
            if char.isupper():
                condition2= True
        if condition2== False:
            print('Your Password does not contain upper case letter.')
        #checking for lower case
        condition3= False
        for char in password:
            if char.islower():
                condition3= True
        if condition3== False:
            print('Your Password does not contain lower case letter.')

        # checking for special character
        condition4= False
        for char in password:
            if char=='$' or char=='#' or char=='@':
                condition4= True
        if condition4== False:
            print('Your Password does not contain a special character. (@,#,$)')
        # Desplying final message
        if condition== True and condition1== True and condition2== True and condition3== True and condition4== True:
            print("Password Changed Sucessfully!")
            check=1
        if check==0:
            print("")
            print("")
            password= input('Enter password again!. Your password must contain\n• At least 1 letter between [a-z] and 1 letter between [A-Z].\n• At least 1 number between [0-9].\n• At least 1 character from [$#@].\n• Minimum length 6 characters.\n• Maximum length 16 characters.')
    password_file= open("password.txt","w")
    password_file.write(password)
    password_file.close()
    time.sleep(2)
def login(n):
    if n==1:
        teacher_name = input('Please enter your name:')
        print('Welcome!',teacher_name)
        welcome_teacher()
    elif n==2:
        print("Enter Admin Password")
        entered_password= input("")
        count=1
        while entered_password != password:
            import time
            print("You entered wrong password!")
            print("Enter Password again")
            entered_password= input("Enter:")
            if entered_password==password:
                break
            else:
                count+=1
            if count%3==0:
                print("You have tried too many attempts !")
                print("You are restricted to start entering password for 30 seconds")
                count1=0
                for j in range(30):
                    A=30-count1
                    if len(str(A))==1:
                        print(A," second remaining")
                    else:
                        print(A," seconds remaining")
                    time.sleep(1)
                    count1+=1
        welcome_admin()
def welcome_teacher():
    teacher_input=0
    while teacher_input!=3:
        print("Press 1 to start attendence")
        print("Press 2 to enter marks")
        print("press 3 to log out!")
        teacher_input= eval(input(""))
        if teacher_input==1:
            time.sleep(1)
            A=take_attendence()
        elif teacher_input==2:
            time.sleep(1)
            B=marks()
        elif teacher_input==3:
            time.sleep(1)
            print("Logging out!")  
def marks():
    choice='y'
    from time import ctime
    file=open("marks.txt",'a')
    date_time1=ctime()
    f3=open("class_member.txt",'r')
    count1=1
    file.write("--------------------")
    file.write("\n")
    file.write(date_time1)
    file.write("\n")
    for i in f3:
        if count1==1:
            count1=2
        else:
            i=i.strip("\n")
            file.write(i)
            file.write("  got  ")
            print("Enter quiz marks of the student ",i)
            while choice=='y':
                marks=eval(input("Enter="))
                print("if you want to change marks press y\nOR\n any other key to confirm ")
                choice=input("")
                choice= choice.lower()
            choice='y'
            file.write(str(marks))
            file.write("\n")
    file.write("--------------------")
    file.close()
    time.sleep(1)
def welcome_admin():
    admin_input=10
    count=0
    while admin_input!=0:
        print("Welcome!")
        print("Press:")
        dict={1:("to view the attendence",),2:("to add member to a class",),3:("to remove member from the class",),4:("To check record of a member",),5:("to change admin password",),6:("to view quiz marks of the students",),0:("to logout from admin page",)}
        for i in dict:
            print(i,end=" ")
            for j in dict[i]:
                print(j)
        admin_input= eval(input("Enter:"))
        if admin_input==1:
            view_attendence()
        elif admin_input==2:
            add_member()
        elif admin_input==3:
            remove_member()
        elif admin_input==4:
            view_record()
        elif admin_input==5:
            change_password()
        elif admin_input==6:
            view_marks()
        elif admin_input==0:
            print("Logging out")
        else:
            print("Wrong input!")
            count+=1
            if count%3==0:
                print("You have type a wrong keyword for admin functions")
                print("You are restricted for 30 seconds")
                times=30
                for i in range(times):
                    A=times-i
                    if len(str(A))==2:
                        print("You have",A,"seconds remaining")
                    else:
                        print("you have",A," second remaining")
                    time.sleep(1)
def view_attendence():
    import time
    print("press 1 to print full record of attendence")
    print("Press 2 to print only Last attendence taken")
    attendence=eval(input("Enter:"))
    if attendence==1:
        print("Full attendence is :")
        file_open=open("attendence_file.txt",'r')
        for j in file_open:
            print(j)
        file_open.close()
    elif attendence==2:
        print("--------------------")
        print("Last attendence is :")
        attendence2=open("current_attendence.txt",'r')
        for k in attendence2:
            print(k)
        attendence2.close()
        print("--------------------")
    time.sleep(2)
def view_marks():
    file1=open("marks.txt",'r')
    for i in file1:
        print(i)
    time.sleep(1)
def add_member():
    member_file= open("class_member.txt","a")
    record_file= open("student_record.txt","a")
    print("How many members you want to add to class")
    number_of_stds=eval(input("Enter"))
    for i in range(number_of_stds):
        print("Kindly fill the follwing form.")
        name= input("Enter Student name:")
        name= name.upper()
        class_room.append(name)
        father_name=input("Enter Student's Father name:")
        age= input("Enter Student's age:")
        contact_no= input("Enter Student contact number:")
        member_file.write('\n')
        member_file.write(name)
        record_file.write('\n')
        record_file.write("Name:")
        record_file.write(name)
        record_file.write('\n')
        record_file.write('\t')
        record_file.write('Father Name:')
        record_file.write(father_name)
        record_file.write('\n')
        record_file.write('\t')
        record_file.write("Age:")
        record_file.write(age)
        record_file.write('\n')
        record_file.write('\t')
        record_file.write("Contact:")
        record_file.write(contact_no)
    record_file.close()
    member_file.close()
    time.sleep(2)
def remove_member():
    #print("How many students you want to remove?")
    #remove=eval(input("Enter"))
    #for i in range(remove):
    control='y'
    while control=='y':
        member_file=open("class_member.txt","r")
        class_room=[]
        count=1
        for line in member_file:
            if count==1:
                count=2
            else:
                line=line.strip('\n')
                class_room.append(line)
        member_file.close()
        print(class_room)
        print("Enter Student name to remove him from class.")
        name= input()
        name= name.upper()
        if not name in class_room:
            print("This name does not exist in your record.")
            control= input("Press:\n'y' to remove another member.\nOR\nAny other key to go back.")
        else:
            class_room.remove(name)
            print(class_room)
            #Updating members file
            member_file= open("class_member.txt","w")
            for member in class_room:
                member_file.write('\n')
                member= member.upper()
                member_file.write(member)
            member_file.close()
            # Removing record of removed member
            record_file= open("student_record.txt","r")
            changed_record= []
            check= False
            i=1
            for line in record_file:
                if not('Name:'+name+'\n') in line:
                    if check== False:
                        changed_record.append(line)
                    else:
                        if i>=3:
                            check= False
                        else:
                            i+=1
                else:
                    check= True
            record_file.close()
            record_file= open("student_record.txt","w")
            record_file.writelines(changed_record)
            record_file.close()
            control= input("Press:\n'y' to remove another member.\nOR\nAny other key to go back.")
def view_record():
    flow_control= 'y'
    while flow_control=='y':
        print("Enter:\n'1' to view complete record of class.\n'2'to search record by name.")
        command= eval(input(""))
        record_file= open("student_record.txt","r")
        if command==1:
            count=1
            for line in record_file:
                if count==1: # This is done to ignore first line
                    count=2
                else:
                    print(line)
            #record_file.close()
        elif command==2:
            new_list=[]
            f=open("class_member.txt",'r')
            student_name= input("Enter student name to check his/her record.")
            student_name= student_name.upper()
            for i in f:
                i=i.strip("\n")
                new_list.append(i)
            f.close()
            if student_name not in new_list:
                print("sorry! this student is unavailable in class")
            else:
                count=0
                control=10
                for line in record_file:
                    if line==('Name:'+student_name+'\n'):
                        control= 1
                    if control<=4:
                        print(line)
                        control+=1
        flow_control= input("Enter 'y' to view record again. Or any other key to go back.")
    record_file.close()
                
def take_attendence():
    from time import ctime
    attendence_file=open("attendence_file.txt",'a')
    current_attendence=open("current_attendence.txt",'w')
    date_time=ctime()
    attendence_file.write("--------------------")
    attendence_file.write("\n")
    attendence_file.write(date_time)
    current_attendence.write(date_time)
    attendence_file.write("\n")
    current_attendence.write("\n")
    print("press 'p' if student is present")
    print("press 'a' if student is absent")
    new=open("class_member.txt",'r')
    count=1
    for t in new:
        if count==1:
            count=2
        else:
            t=t.strip("\n")
            print(t,"is present in class or not?")
            attend=input('')
            attendence=attend.upper()
            attendence_file.write(t)
            current_attendence.write(t)
            attendence_file.write(" is ")
            current_attendence.write(" is ")
            attendence_file.write(attendence)
            current_attendence.write(attendence)
            attendence_file.write("\n")
            current_attendence.write("\n")
    attendence_file.write("--------------------")
    attendence_file.close()
    current_attendence.close()
    new.close()
    time.sleep(2)
def main():
    print("Welcome to School Management System")
    print("------------------------------------")
    command= input("To continue press 'y'. To exit press any other key.")
    while command.lower() == 'y':
        print("Press:\n'1' to login as Teacher\n'2' to login as Admin")
        n= eval(input(""))
        login(n)
        command= input("To continue press 'y'. To exit press any other key.")
        if command.lower()!='y':
            break
    print('Exited!')
main()

