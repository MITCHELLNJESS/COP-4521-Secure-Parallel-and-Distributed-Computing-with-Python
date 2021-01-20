import math

def accepts(*args):
	def arg_check(func):
		def new_func(*arg):
			for a, ar in zip(arg, args):
				if type(a) != ar:
					print (a, " is not of type " , ar)
					break
			else:
				func(*arg)
		return new_func
	return arg_check

@accepts(str)
def print_hello(name):
	print("Hello ", name)

@accepts(dict, int)
def avg_temp(records, year):
	for month, temp in records.items():
		print("The average temperature in ",month,year, " was ", temp)

@accepts(complex)
def comp_mag(z):
	print (math.sqrt(z.real**2 + z.imag**2))

if __name__ == "__main__":
	print_hello("Patrick")
	print_hello(24+25j)

	avg_temp({"Jan":57, "Mar":70, "May":90}, 2018)
	avg_temp([("Jan",57), ("Mar",70), ("May",90)],2018)

	comp_mag("Patrick")
	comp_mag(24+25j)

