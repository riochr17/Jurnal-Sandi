import sys
from file_handler import FileHandler
from vigenere import Vigenere
from playfair import PlayFair

def main():

	NUMBER_SEPARATED = False
	FILE_OUTPUT = False

	if len(sys.argv) == 7:
		try:
			NUMBER_SEPARATED = int(sys.argv[6])
		except ValueError:
			NUMBER_SEPARATED = 0
			FILE_OUTPUT = sys.argv[6]

	def print_help():
		print "+ "
		print "+ usage:"
		print "- python main.py playfair   string dec \"sony\" \"XXXXXX\""
		print "- python main.py playfair   string enc \"sony\" \"WELCOME TO THE JUNGLE\""
		print "- python main.py playfair   text   dec \"sony\" \"chiper.txt\""
		print "- python main.py playfair   text   enc \"sony\" \"plain.txt\""
		print "- python main.py vigenere   string dec \"sony\" \"XXXXXXX\""
		print "- python main.py vigenere   string enc \"sony\" \"WELCOME TO THE JUNGLE\""
		print "- python main.py vigenere   text   dec \"sony\" \"chiper.txt\""
		print "- python main.py vigenere   text   enc \"sony\" \"plain.txt\""
		print "- python main.py vigenere   file   dec \"sony\" \"a.txt\" \"b.txt\""
		print "- python main.py vigenere   file   enc \"sony\" \"a.txt\" \"b.txt\""
		print "- python main.py vigenere-x string dec \"sony\" \"XXXXXXX\""
		print "- python main.py vigenere-x string enc \"sony\" \"WELCOME TO THE JUNGLE\""
		print "- python main.py vigenere-x text   dec \"sony\" \"chiper.txt\""
		print "- python main.py vigenere-x text   enc \"sony\" \"plain.txt\""

	argc = len(sys.argv)

	if argc < 6:
		print "+ Error: argument must take min. 6"
		print_help()
		exit()

	if sys.argv[1] != "vigenere" and sys.argv[1] != "vigenere-x" and sys.argv[1] != "playfair":
		print "+ Error: use vigenere/vigenere-x/playfair on fisrt argument"
		print_help()
		exit()

	if sys.argv[2] != "file" and sys.argv[2] != "string" and sys.argv[2] != "text":
		print "+ Error: use file/string/text on second argument"
		print_help()
		exit()

	if sys.argv[3] != "dec" and sys.argv[3] != "enc":
		print "+ Error: use enc/dec on third argument"
		print_help()
		exit()

	if sys.argv[1] == "vigenere":
		if sys.argv[2] == "file":
			vg = Vigenere(sys.argv[4])
			if sys.argv[3] == "dec":
				vg.decFile(sys.argv[5], sys.argv[6])
				print "File " + str(sys.argv[5]) + " succesfully decrypted to " + str(sys.argv[6])
			if sys.argv[3] == "enc":
				vg.encFile(sys.argv[5], sys.argv[6])
				ct = "File " + str(sys.argv[5]) + " succesfully encrypted to " + str(sys.argv[6])
				print ct

		elif sys.argv[2] == "string":
			vg = Vigenere(sys.argv[4])
			if sys.argv[3] == "dec":
				print vg.dv(sys.argv[5])
			if sys.argv[3] == "enc":
				ct = vg.ev(sys.argv[5])
				if not FILE_OUTPUT:
					print FileHandler().outputFormatter(ct, NUMBER_SEPARATED) if NUMBER_SEPARATED else ct
				else:
					FileHandler().writeToFile(FILE_OUTPUT, ct)

		elif sys.argv[2] == "text":
			vg = Vigenere(sys.argv[4])
			if sys.argv[3] == "dec":
				print vg.decrypt(open(sys.argv[5], 'r').read())
			if sys.argv[3] == "enc":
				ct = vg.encrypt(open(sys.argv[5], 'r').read())
				if not FILE_OUTPUT:
					print FileHandler().outputFormatter(ct, NUMBER_SEPARATED) if NUMBER_SEPARATED else ct
				else:
					FileHandler().writeToFile(FILE_OUTPUT, ct)

		else:
			print "+ Error: use only file/string/text on Vigenere chiper third argument"

	if sys.argv[1] == "vigenere-x":
		if sys.argv[2] == "string":
			vg = Vigenere(sys.argv[4])
			if sys.argv[3] == "dec":
				print vg.dv(sys.argv[5], is_extended = True)
			if sys.argv[3] == "enc":
				ct = vg.ev(sys.argv[5], is_extended = True)
				if not FILE_OUTPUT:
					print FileHandler().outputFormatter(ct, NUMBER_SEPARATED) if NUMBER_SEPARATED else ct
				else:
					FileHandler().writeToFile(FILE_OUTPUT, ct)

		elif sys.argv[2] == "text":
			vg = Vigenere(sys.argv[4])
			if sys.argv[3] == "dec":
				print vg.decrypt(open(sys.argv[5], 'r').read(), is_extended = True)
			if sys.argv[3] == "enc":
				ct = vg.encrypt(open(sys.argv[5], 'r').read(), is_extended = True)
				if not FILE_OUTPUT:
					print FileHandler().outputFormatter(ct, NUMBER_SEPARATED) if NUMBER_SEPARATED else ct
				else:
					FileHandler().writeToFile(FILE_OUTPUT, ct)

		else:
			print "+ Error: use only string/text on Vigenere extended chiper third argument"

	if sys.argv[1] == "playfair":
		if sys.argv[2] == "string":
			pf = PlayFair(sys.argv[4])
			if sys.argv[3] == "dec":
				print pf.decrypt(sys.argv[5])
			if sys.argv[3] == "enc":
				ct = pf.encrypt(sys.argv[5])
				if not FILE_OUTPUT:
					print FileHandler().outputFormatter(ct, NUMBER_SEPARATED) if NUMBER_SEPARATED else ct
				else:
					FileHandler().writeToFile(FILE_OUTPUT, ct)

		elif sys.argv[2] == "text":
			pf = PlayFair(sys.argv[4])
			if sys.argv[3] == "dec":
				print pf.decrypt(open(sys.argv[5], 'r').read())
			if sys.argv[3] == "enc":
				ct = pf.encrypt(open(sys.argv[5], 'r').read())
				if not FILE_OUTPUT:
					print FileHandler().outputFormatter(ct, NUMBER_SEPARATED) if NUMBER_SEPARATED else ct
				else:
					FileHandler().writeToFile(FILE_OUTPUT, ct)

		else:
			print "+ Error: use only string/text on Playfair chiper third argument"

if __name__=="__main__":
	main()