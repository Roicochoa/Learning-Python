#string

s = "I am a string."
print(type(s))			#will say str

#boolean

yes =  True
print(type(yes))		#Boolean True

no = False
print(type(no))			#Boolean False

#list -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))			#will say tuple
print(type(alpha_list[0]))		#will say string
alpha_list.append("d")			#adds d to end of the list
print(alpha_list)				#prints list

#Tuple -- ordered and unchangeable

alpha_tuple = ("a", "b","c")	#tuple initialization
print(type(alpha_tuple))		#will say tuple

#attempt following line
try:
	alpha_tuple[2] = "d"		#won't work and will raise TypeError
except TypeError:				#when we get a TypeError
	print("We can't add elements to tuples!")	#print this messsage
print(alpha_tuple)				#prints tuple