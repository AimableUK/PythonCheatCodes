from time import sleep
from threading import *

class Hello(Thread):

	def run(self):
		for i in range(4):
			print("hello")
			sleep(1)

class Hi(Thread):

	def run(self):
		for i in range(4):
			print('hi')
			sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Execution finished Good bye")