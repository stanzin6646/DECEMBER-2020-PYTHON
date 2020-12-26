import csv
condition =True
while(condition):
   student_info = input("Enter student info:")
   print(student_info)

   student_info_list = student_info.split(' ')
   print("Entered info is:" + str(student_info_list))
   
   condition_check = input("Enter yes or no")
   if condition_check == "yes":
      conndition =True
   elif  condition_check == "no":
       condition = False
