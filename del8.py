class employee:
    def __init__(self,name, last , area):
        self.name = name
        self.last = last
        self.area = area
        self.email = name + '.' + last  + '@gmail.com'

    def gh(self):
        name = "SAB"
        self.name = 'vijay'
        print("local var {}\n class var: {}".format(name, self.name))
emp1 = employee('vetri' , 'vel' , 'Neyveli')

print (emp1.name)
print (emp1.last)
print (emp1.email)
emp1.gh()
print (emp1.name)

def main():
    import pdb
    for x in range(10):
        print(x)
        pdb.set_trace()
