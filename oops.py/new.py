# class student:
#     def __init__(self, name , grade ): 
#      self.name =name
#      self.grade =grade


# student1= student("Harsh" , 12)
# print(student1.name , student1.grade)

# class car:
#     def __init__(self , name,model,year):
#         self.name= name
#         self.model=model
#         self.year=year
#     def car_details(self):
#          print(f"{self.name} {self.model} {self.year}")

# car1= car("toyata" , 20,2022)
# print(car1.name ,car1.model,car1.year)

# print as a key value


# print(student1.__dict__)

# student1.grade =100

# print(student1.grade)
# print(student1.__dict__)

# # del student1.grade

# .................................................................
class Student:
    def __init__(self, name , grade ): 
     self.name =name
     self.grade =grade

    
student1= Student("Harsh" , 12)
print(student1.name , student1.grade)

class GraduateStudent(Student):
    def __init__(self, name, grade,stream):
           super().__init__(name, grade)

           self.stream =stream

    def Student_det(self):
            #   super().student_details
              print(f"{self.name} is in the class{self.grade}and its stream{self.stream}")

              GraduateStudent1 = GraduateStudent1("Harsh", 12,'PCM')

              print(GraduateStudent1.stream)

