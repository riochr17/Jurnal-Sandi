from math import log, ceil
import time
from file_handler import FileHandler

class RSA:
	def __init__(self):
		self.fh = FileHandler()

	def enc_file(self, filename, publickey):
		return self.encrypt(publickey, self.fh.readFileReturnBytes(filename))

	def dec_file(self, filename, privatekey):
		return self.decrypt(publickey, self.fh.readFileReturnBytes(filename))

	def bytes_to_ints_as_segment(self, pk, bytesdata):
		def get_int_from_bytes(bytesss):
			return int(''.join(format(x, '02x') for x in bytesss), 16)

		key, n = pk
		outbyte = bytearray()
		segment_sz = int(ceil(ceil(log(n, 2)) / 8))
		list_chunked = zip(*[iter(bytesdata)]*segment_sz)
		return [get_int_from_bytes(chint) for chint in list_chunked]

	def ints_to_bytes_as_segment(self, pk, intsdata):
		def get_by_2_char(s):
			if len(s) % 2 == 1:
				s = '0' + s
			temp = s[::-1]
			return [temp[i:i+2][::-1] for i in range(0, len(temp), 2)][::-1]

		def save_byte_segment(segment_length, str_hex_data):
			out_byte = bytearray()
			len_str_hex_data = len(str_hex_data)
			for i in range(segment_length - len_str_hex_data):
				out_byte += '00'.decode('hex')
			for i in range(len_str_hex_data):
				out_byte += str_hex_data[i].decode('hex')

			return out_byte

		# 4 -> 15
		# 8 -> 255 1 byte
		# 12 -> 4095
		# 16 -> 65535 2 byte
		key, n = pk
		outbyte = bytearray()
		segment_sz = int(ceil(ceil(log(n, 2)) / 8))
		for x in intsdata:
			strdata = str(format(x, '02x'))
			outbyte += save_byte_segment(segment_sz, get_by_2_char(strdata))

		return outbyte

	def encrypt(self, pk, plain_bytearr):
		#Unpack the key into it's components
		key, n = pk
		
		# start time elapsed
		start_time = time.time()

		# Generat chiper text
		cipher = [(int(b) ** key) % n for b in plain_bytearr]

		# end time elapsed
		elapsed_time = time.time() - start_time
		print "Encrypt time elapsed: " + str(elapsed_time)

		# Return the array of bytes
		return self.ints_to_bytes_as_segment(pk, cipher)

	def decrypt(self, pk, cipher_bytearr):
		# Unpack the key into its components
		key, n = pk
		
		# start time elapsed
		start_time = time.time()

		# convert segmented bytes to array of int (8 bit)
		cipher_bytearr = self.bytes_to_ints_as_segment(pk, cipher_bytearr)

		# Generate plain text
		plain = [(int(b) ** key) % n for b in cipher_bytearr]

		# end time elapsed
		elapsed_time = time.time() - start_time
		print "Decrypt time elapsed: " + str(elapsed_time)

		# Return the array of bytes
		return bytearray(plain)

# dd = RSA().ints_to_bytes_as_segment((3971, 4559), [1236, 255, 231, 723])
# print ''.join(format(x, '02x') for x in dd)
# print RSA().bytes_to_ints_as_segment((3971, 4559), dd)
