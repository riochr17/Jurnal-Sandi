class FileHandler:
	# read file -> return bytes of file
	def readFileReturnBytes(self, filename):
		# Cast bytes to bytearray
		mutable_bytes = bytearray()
		with open(filename, "rb") as f:
		    # Bytearray allows modification
			byte = f.read(1)
			index = 0
			while byte != b"":
				# Do stuff with byte.
				mutable_bytes.append(byte)
				byte = f.read(1)

		return mutable_bytes

	# write file with input bytes data -> void
	def writeFileByBytes(self, filename, bytes_data):
		open(filename, 'wb').write(bytes_data)

	def writeToFile(self, filename, text):
		file = open(filename, "w") 
		file.write(text)
		file.close()

	def outputFormatter(self, text, number_separated):
		return text if number_separated == 0 else self.outputFormatterRX("", text, 0, number_separated)

	def outputFormatterRX(self, nt, ot, ct, nf):
		if len(ot) == 0:
			return nt

		if ct >= nf:
			if ct % nf == 0:
				nt += ' '

		ct += 1
		return self.outputFormatterRX(nt + ot[:1], ot[1:], ct, nf)
		