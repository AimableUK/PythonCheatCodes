class Directrix:
    whill = "there are ......"

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def addisresp(self):
        c = self.m1 + self.m2
        return c


class Dealing(Directrix):
    def __init__(self, m1, m2, m3, m4):
        super().__init__(m1, m2)
        self.m3 = m3
        self.m4 = m4

    def operations(self):
        # Optional: input values again inside method
        self.m3 = int(input("2 Enter some Info related to the salary: "))
        self.m4 = int(input("2 enter the age: "))
        m12 = self.m1 + self.m2
        m34 = self.m3 + self.m4
        print(f"Sum from parent: {m12}")
        print(f"Sum from child: {m34}")


# Taking inputs
m1 = int(input("Enter some Info related to the salary: "))
m2 = int(input("Enter the age: "))

m3 = int(input("2 Enter some Info related to the salary: "))
m4 = int(input("2 enter the age: "))

# Create instance of Dealing
d1 = Dealing(m1, m2, m3, m4)

# Call parent method
print("Sum from addisResp():", d1.addisresp())

# Call child method
d1.operations()
