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