from rsa_keygen import RSAKeyGen
from rsa import RSA
from file_handler import FileHandler
import sys
import os

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
	i = 0
	while nbytes >= 1024 and i < len(suffixes)-1:
		nbytes /= 1024.
		i += 1
	f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
	return '%s %s' % (f, suffixes[i])

if sys.argv[1] == "generate key":
	print "Generating key..."
	pub, pri = RSAKeyGen().generate_keypair()
	print "Success: generated key saved as key.pub and key.pri"
	print "---END---"
	print ""

if sys.argv[1] == "rsa":
	if sys.argv[2] == "encrypt":
		pub, pri = RSAKeyGen().read_key(sys.argv[3])

		fh = FileHandler()
		bytesdata = fh.readFileReturnBytes(sys.argv[4])

		print "Encrypting"
		bytesdata = RSA().encrypt(pri, bytesdata)
		# print ''.join(format(x, '02x') for x in bytesdata)
		fh.writeFileByBytes(sys.argv[5], bytesdata)

		print "file: " + sys.argv[5] + ", size: " + humansize(os.path.getsize(sys.argv[5]))

	if sys.argv[2] == "decrypt":
		pub, pri = RSAKeyGen().read_key(sys.argv[3])

		fh = FileHandler()
		bytesdata = fh.readFileReturnBytes(sys.argv[4])

		print "Decrypting"
		bytesdata = RSA().decrypt(pub, bytesdata)
		# print ''.join(format(x, '02x') for x in bytesdata)
		fh.writeFileByBytes(sys.argv[5], bytesdata)

		print "file: " + sys.argv[5] + ", size: " + humansize(os.path.getsize(sys.argv[5]))