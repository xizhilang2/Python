class room:
    def __init__(self,area=120,usedfor='sleep'):
        self.area = area
        self.usedfor = usedfor

    def display(self):
        print("this is my house")

class babyroom(room):
    def __init__(self,area=40,usedfor="son",wallcolor='green'):
        super().__init__(area,usedfor)
        self.wallcolr = wallcolor

    def display(self):
        super().display()
        print("babyroom area:%s wallcollor:%s"%(self.area,self.wallcolr))

class rent:
    def __init__(self,money=1000):
        self.rentmoney = money

    def display(self):
        print("for rent at the price of %s"%self.rentmoney)

class agent(babyroom,rent):
# class agent(rent,babyroom):
    def display(self):
        # super(agent, self).__init__()
        super().display()
        print("rent house agent")

agent().display()
print(agent.__mro__)

# 在理想中我们希望所有类的都能够输出，也就是：
# this is my house
# babyroom area:40 wallcollor:green
# for rent at the price of 1000
# rent house agent
#
# 但是实际输出并不是这样的，看到上面两种写法：
# 写法1的输出：
# this is my house
# babyroom area:40 wallcollor:green
# rent house agent
# 也就是说并没有调用rent类的display方法
#
# 写法二的输出：
# for rent at the price of 1000
# rent house agent
# 也就是说babyroom以及room类的display方法都没有调用
