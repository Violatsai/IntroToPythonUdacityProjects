class parent():
	def __init__(self,last_name,eye_color):
		print("parent constructor called.")
		self.last_name = last_name
		self.eye_color = eye_color
	def show_info(self):
		print("Last name:" + self.last_name)
		print("Eye color:" + self.eye_color)

class child(parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("child constructor called.")
		parent.__init__(self,last_name,eye_color)
		self.number_of_toys = number_of_toys

#Lily_Potter = parent("Potter", "Green")
#Lily_Potter.show_info()
#print(Lily_Potter.last_name)
#print(Lily_Potter.eye_color)
Harry_Potter = child("Potter","Green",10)
Harry_Potter.show_info()
#print(Harry_Potter.last_name)
#print(Harry_Potter.eye_color)
print("Number of toys:" + str(Harry_Potter.number_of_toys))
