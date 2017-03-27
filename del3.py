class college:
    Major = 'CSE'
    def __init__(self,name,ID_no):
        self.name = name
        self.ID_no = ID_no

    def print_name(self):
        print(self.name.title())

    def __call__(self):
        print("called")
a = college('vijay', 125)
a()

print (a.__dict__)
print (a.Major)
