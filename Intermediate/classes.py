class Directrix:

	whill = "there are ......"

	def __init__(self,m1,m2):
		self.m1 = m1
		self.m2 = m2
	
	def addisResp(self):
            c = self.m1 + self.m2
            return c

class Dealing(Directrix): 
	    
    def __init__(self,m3,m4):
        self.m3 = m3
        self.m4 = m4

	def operations(self,m3,m4):
		m3 = int(input("2 Enter some Info related to the salary"))
        m4 = int(input("2 enter the age"))
	    m12 = self.m1 + self.m2
		m34 = self.m3 + self.m4
  

			
			

m1 = int(input("Enter some Info related to the salary"))
m2 = int(input("enter the age"))

m3 = int(input("2 Enter some Info related to the salary"))
m4 = int(input("2 enter the age"))

d1 = Dealing(m1,m2)


print(d1.addisResp(m1,m2))