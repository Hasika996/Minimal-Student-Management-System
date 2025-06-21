class Student:
    def __init__(self,name,id,branch):
        self.name=name
        self.id=id
        self.branch=branch
class Department:
    def __init__(self,d_name):
        self.d_name=d_name
        self.students=[]
    def add_Student(self,student):
        for s in self.students:
            if s.id==student.id:
                return -1
        self.students.append(student)
        return 1
    def remove_Student(self,student):
        if student not in self.students:
            return -1
        self.students.remove(student)
        return 1
    def get_enrolled_students(self):
        return self.students
class Institution:
    def __init__(self,name):
        self.name=name
        self.depts=[]
    def add_department(self,dept):
        for d in self.depts:
            if d.d_name==dept:
                return -1

        self.depts.append(dept)
        return 1
    def get_dept(self,dept_name):
        for d in self.depts:
            if d.d_name==dept_name:
                return d

        return None
    def get_all_students(self):
        ans=[]
        for d in self.depts:
            ans.extend(d.get_enrolled_students())
        return ans
    def get_students_of_a_dept(self,dept_name):
        dept = self.get_dept("SomeDept")
        if dept:
            print(dept.get_enrolled_students())



