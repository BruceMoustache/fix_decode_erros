def fix_text(given_text):
	text_bytes = b''
	for char in given_text:
		ord_char = ord(char)
		text_bytes += ord_char.to_bytes(1, byteorder='little')
	fixed_text = text_bytes.decode('utf-8')
	return fixed_text

