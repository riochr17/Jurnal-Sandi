import sys
from vigenere import Vigenere

def main():

	# usage:
	# python vigenere.py string sony "WELCOME TO THE JUNGLE"
	# python vigenere.py file "a.txt" "b.txt"

	argc = len(sys.argv)

	if argc < 5:
		print "# Error: argument must take at least 4\n#"
		print "# usage:"
		print "# python vigenere.py string dec \"sony\" \"WELCOME TO THE JUNGLE\""
		print "# python vigenere.py file dec \"a.txt\" \"b.txt\""
		exit()

	if sys.argv[1] != "file" and sys.argv[1] != "string":
		print "# Error: first argument must string or file\n#"
		print "# usage:"
		print "# python vigenere.py string dec \"sony\" \"WELCOME TO THE JUNGLE\""
		print "# python vigenere.py file dec \"a.txt\" \"b.txt\""
		exit()

	if sys.argv[2] != "dec" and sys.argv[2] != "enc":
		print "# Error: second argument must dec or enc\n#"
		print "# usage:"
		print "# python vigenere.py string dec \"sony\" \"WELCOME TO THE JUNGLE\""
		print "# python vigenere.py file   dec \"sony\" \"a.txt\" \"b.txt\""
		exit()

	vg = Vigenere(sys.argv[3])

	if sys.argv[1] == "file":
		if sys.argv[2] == "dec":
			vg.decFile(sys.argv[4], sys.argv[5])
			print "File " + str(sys.argv[4]) + " succesfully decrypted to " + str(sys.argv[5])
		if sys.argv[2] == "enc":
			vg.encFile(sys.argv[4], sys.argv[5])
			print "File " + str(sys.argv[4]) + " succesfully encrypted to " + str(sys.argv[5])

	if sys.argv[1] == "string":
		if sys.argv[2] == "dec":
			print vg.dv(sys.argv[4])
		if sys.argv[2] == "enc":
			print vg.ev(sys.argv[4])

if __name__=="__main__":
	main()