a=5
b=2

try:
	print("resource open")
	print(a/b)
	x = int(input("enter a number: "))
	print(x)
	
except ZeroDivisionError as e:
	print("Hey its impossible to devide by Zero ", e)
except ValueError as e:
	print("Invalid Input ")
except Exception as e:
	print("Something Went Wrong.... ")
finally:
	print("resource closed ")
