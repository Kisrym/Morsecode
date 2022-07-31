def morsecode(text, code="code"):
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
	if code == "code":
		for letter in text.lower():
			for key, value in morse_code.items():
				if letter == key:
					letters.append(value)
		return " ".join(letters)
	elif code == "decode":
		text = text.split()
		for letter in text:
			for key, value in morse_code.items():
				if letter == value:
					letters.append(key) 
		return "".join(letters)