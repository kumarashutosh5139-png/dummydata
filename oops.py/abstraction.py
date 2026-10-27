# hide unnecessary  details

class student:
    def __init__(self,name,grade,percentage):
        self.name =name
        self.grade=grade
        self.__percentage=percentage

        student1 =student("harsh",12)
        print(student1.name,student1.grade)



        # def student_details(self):
        #     print(f"{self.name}is in class{self.grade}with({self.percentage+2}%")


        #     student1 =student("harsh",12,80)
        #     print


                                              