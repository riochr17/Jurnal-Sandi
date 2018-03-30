import random
from large_prime import LargePrime

class RSAKeyGen:
	def __init__(self):
		self.keyA = LargePrime().generateLargePrime(7)
		self.keyB = LargePrime().generateLargePrime(9)

	def save_key(self, filename, data):
		file = open(filename, "w") 
		file.write(str(data))
		file.close()

	def read_key(self, filename):
		f = open(filename + ".pub")
		a = f.read().split('\n')
		f.close()

		f = open(filename + ".pri")
		b = f.read().split('\n')
		f.close()

		return ((int(a[0]), int(a[1])), (int(b[0]), int(b[1])))

	def gcd(self, a, b):
		while b != 0:
			a, b = b, a % b
		return a

	def multiplicative_inverse(self, e, phi):
		d = 0
		x1 = 0
		x2 = 1
		y1 = 1
		temp_phi = phi
		
		while e > 0:
			temp1 = temp_phi/e
			temp2 = temp_phi - temp1 * e
			temp_phi = e
			e = temp2
			
			x = x2- temp1* x1
			y = d - temp1 * y1
			
			x2 = x1
			x1 = x
			d = y1
			y1 = y
		
		if temp_phi == 1:
			return d + phi

	def generate_keypair(self):
		p = self.keyA
		q = self.keyB

		#n = pq
		n = p * q

		#Phi is the totient of n
		phi = (p-1) * (q-1)

		#Choose an integer e such that e and phi(n) are coprime
		e = random.randrange(1, phi)

		#Use Euclid's Algorithm to verify that e and phi(n) are comprime
		g = self.gcd(e, phi)
		while g != 1:
			e = random.randrange(1, phi)
			g = self.gcd(e, phi)

		#Use Extended Euclid's Algorithm to generate the private key
		d = self.multiplicative_inverse(e, phi)

		self.save_key("key.pub", str(e) + "\n" + str(n))
		self.save_key("key.pri", str(d) + "\n" + str(n))

		#Return public and private keypair
		#Public key is (e, n) and private key is (d, n)
		return ((e, n), (d, n))

