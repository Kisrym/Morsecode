def morsecode(text, decode = False):
	"""Codifica/decodifica código morse

	Args:
		text (str): Texto que vai ser modificado.
		decode (bool, opcional): Escolhe se você vai decodificar ou não. Default: False

	Returns:
		str: Texto modificado.
	"""
	morse_code = {
	"a" : ".-",
	"b":"-...",
	"c":"-.-.",
	"d":"-..",
	"e":".",
	"f":"..-.",
	"g":"--.",
	"h":"....",
	"i":"..",
	"j":".---",
	"k":"-.-",
	"l":".-..",
	"m":"--",
	"n":"-.",
	"o":"---",
	"p":".--.",
	"q":"--.-",
	"r":".-.",
	"s":"...",
	"t":"-",
	"u":"..-",
	"v":"...-",
	"w":".--",
	"x":"-..-",
	"y":"-.--",
	"z":"--..",
	" ": "/"
	}
	letters = []
	if decode == False:
		for letter in text.lower():
			for key, value in morse_code.items():
				if letter == key:
					letters.append(value)
		return " ".join(letters)
	elif decode == True:
		text = text.split()
		for letter in text:
			for key, value in morse_code.items():
				if letter == value:
					letters.append(key) 
		return "".join(letters)
