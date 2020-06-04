# This little script has lots of errors.
# Try to find them all.


# Call a function repeatedly:
j = 2	
for i in range(4, 0, -1):
	x = divvy(j, i)


# Tell the user if variable x satisfies a certain condition:
if x >= 3
	print "This is a large value"

	
# Print each element of list A:
A = [2, 4, '6', 8, 10.5]
for i in range(0, len(A)+1):
	print A[i]

	
# Print each element of list A, but provide a little more information:
for i in A:
	print "A[%d] = %.2f" % (A[i])	

		
# Print some calculated values to the screen:
i = 0
while i <= 2:
	print "i = %d.  i/2 = %f" % (i/2.0)	
    print "i = %d.  i/3 = %f" % (i/float(3))
	 i += 1


# Print an error message if 'car' isn't an element of the 'vehicles' list:
vehicles = ['truck', 'airplane', 'bike']
if ('car' in vehicles):
	# No error...nothing to do here.
else:
	print "ERROR: 'car' isn't an element of the 'vehicles' list"


# Print the second element of the first sub-list within A:
A = [[11, 22], [33, 44]]
print A[1, 2]		# We want to print the number "22"
    
		
# This is a function that calculates a fraction for us.
def divvy(a, b):
	x = a/(b-1)
	return x
    