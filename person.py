class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        print(f'{self.fname} {self.lname}')

my_person=Person("daniel","huri")
my_person.full_name()
        
