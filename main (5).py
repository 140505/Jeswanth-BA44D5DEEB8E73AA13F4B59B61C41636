class student:
  def __init__(self,name,roll_number,cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student:student.cgpa,reverse=true)
  return sorted_students
students =[student("hari","A123",7.8),
 student("srikanth","A124",8.9),   
 student("saumya","A125",9.1), 
 student("mahidhar","A126",9.9),
]