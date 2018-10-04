import numpy as np
import sys

#Creating exponential function
def expo(x):
	return np.exp(x)	#sets the function to output e^()
	
#define a subroutine that does not return a value
def show_expo(x):
	for i in range(n):
		print(expo(float(i)))	#call the expo function
		
#define main function
def main():
	n = 10		#provide a default function for n
	
	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#any appended string or value is converted to an integer
		
	show_expo(n)		#call the show_expo subroutine
	
		
#run the main function
if __name__ == "__main__":
	main()