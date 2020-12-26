import csv

def wirte_into_csv(info_list):
    with open('student_info.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
           writer.writerow("Name", "Class", "Contact", "Email_ID")
           writer.writerow(info_list)

if _name_ == '_main_':
  condition =True
  student_num = 1

while(condition):
    student_info = input("Enter student info for sstudent #{} in following format(name class contact_number email_ID):".format(student_num))
    print("Entered info :" + student_info)

    student_info_list = student_info.split(' ')
    print("Entered info is:" + str(student_info_list))

    print("\nEntered info is- \nName: {}\Class: {}\nContact: {}\nEmail_ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    choice=input("is the input information is correct?(yes/no)")
    if choice =="yes":
       wirte_into_csv(student_info_list)
       condition_check = input("Enter yes or no")
       if condition_check == "yes":
       conndition =True
       student_num = student_num + 1
       elif  condition_check == "no":
       condition = False
    elif choice =="no":
       print("\n ENter again:")
