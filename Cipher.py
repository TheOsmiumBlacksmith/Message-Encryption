#pylint:disable=W0312

'''
This code encrypts ny message with a given co-prime key and modulo 100. This uses a block, additive, multiplicative, and exponential cipher collectively.
'''

# create alphabet
from string import printable as alpha

# identity function (used later)
def id_(x,y):
    return x

########

# greatest common divisor of a and b
def egcd(a, b):
    # this works recursively
    if a == 0:
    	# end condition
        return (b, 0, 1)
    else:
    	# another recursion
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# modular inverse of a given m
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# split given number into listed binary form
def binary(num):
    return [int(x) for x in list('{0:0b}'.format(num))]

'''
the repeated square method handles modular arithmetic with very large numbers.
'''
def r_square(a,b):
	# set exponent to 1
    exp=1
    # find binary form of b
    bin_ = binary(b)
    # list of components to be combined
    components = []
    
    for x in range(len(bin_)):
        if bin_[-1-x] == 1:
        	components.append((a**exp)%95)
        # double exponent
        exp *= 2
    # start with multiplicative identity
    ans = 1
    # multiply all elements modulo 95
    for x in components:
        ans = (x*ans)%95
    return ans
    
########

# find inverse key given an encryption method
def inv(x,cipher):
	if cipher == add_:
		return -x
	elif cipher == multi_:
		return modinv(x,95)
	elif cipher == exp_:
		return modinv(x,72)
		
########

# encode every element into numbers
def encode(L):
    for x in range(len(L)):
    	# change element to its index in alphabet
        L[x] = alpha.index(L[x])
    return L

# undo encoding
def decode(L):
    for x in range(len(L)):
    	# number becomes its value in 
        L[x] = alpha[L[x]]
    return L

########

# currently in progress
def block_(key,L):
	return L

########

# additive cipher
def add_(key,L):
    for x in range(len(L)):
    	# add shift key to item
        L[x]= (L[x]+key)%95
    return L

########

# multiplicative cipher
def multi_(key,L):
	# itterate through plain_text
    for x in range(len(L)):
    	# multiply element by key
        L[x] = (L[x]*key)%95
    return L

########

# exponential cipher
def exp_(key,L):
    for x in range(len(L)):
    	# computes element**key
        L[x] = (r_square(L[x],key))%95
    return L

########

def main():
    key = int(input("Shift Key:  "))
    message = list(raw_input("Message:  "))
    ans = raw_input("Encode or Decode?  ").lower()
    
    cipher_lib = [block_, add_, multi_, exp_]
    # encode or decode?
    if ans == "encode":
    	func = id_
    elif ans == "decode":
    	# reverse opperations
    	cipher_lib = cipher_lib[::-1]
    	# invert keys
    	func = inv
    # convert to numbers
    message = encode(message)
    # run through library of ciphers
    for x in cipher_lib:
    	# en/decrypt with each method
    	 message = x(func(key,x),message)
    	 # print final text
    print("".join(decode(message)))


main()
