class Data:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __setitem__(self,key,val):
        self.marks.append(val)       # adds val to the list, we can also use dict 
    def __getitem__(self,key):
        return self.marks[key]

    def __setattr__(self, key, val):
        self.__dict__[key]=val

    def __getattr__(self,name: str):
        print('Attribute Doesnt exist')

    def __len__(self):
        return len(self.marks)  
    def __str__(self):
        return f"student={self.name} and marks={[self.marks]}"      


if __name__=='__main__':
    student1=Data('Raj',[50,89,90])
    student2=Data('suresh',[100,99,99,97])

    student1.attendance        # using __getiter__   # prints warning that attribute not present
    student1.attendance='98%'  # using __setiter__   # sets the new attritbut, not here we use . rather that[]
    print(f'attribute attendence added={student1.attendance}')
    print(student1)   # using __str__    # helps to print what object it is and what it contains, rather that just return class object
    print(student2)
    student1[3]=49   # using __setitem__
    print(f"Total subject of student1 =",len(student1.marks))  # using __len__
    print(f"Total subject of student2 =",len(student2.marks))
    print(student1[2])   #using __getitem__
    print(student2[2])            