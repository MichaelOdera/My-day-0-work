# Creat a function which takes n as a parameter
def prime_is(n):
        # check if the number is an integer
        if isinstance n != int():
                return "Only integers are accepted"
        # Check if the number entered is less than two
        if n < 2:
                return "The number is not accepted"
        #Check if the numbers are positive
        elif n < 1:
                return "Negative numbers are not allowed"
        else:
                return True
                
	# Initialize a variable y to 2. This is where prime numbers begin.
	y = 2
	
	# Check if n is greater or equal to 2, so that you proceed to the calculations.
	while y <= n:
		# Loop through the from 2 to the given final digit in the function prime_is
		for i in range(2, y):
			if y%i == 0:
				# Make an increment on y so that it count from 2 onwards.
				# The loop will check every incremented digit so aas to ascertain 
				# it's divisibility by itself starting from 2
				y+=1 
		print "%s" % p,
		y+=1
