import os						# use system
import itertools				# wordlist generation
import readline					# arrow keys and such
import subprocess				# allows command output capturing
userpath = os.environ['HOME']	# /Users/ path
current_dir = os.environ['PWD']	# current directory
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
exit = ["exit","exit()","quit","quit()","stop","stop()","close","close()"]

print("\nPyTools V1.4 Alpha Starting...")
print("Created by Moros.\n")
# ----------------------------- MAIN ----------------------------- #
def Main():
	toolsec = raw_input("pytools.py> ")
	toolsplit = toolsec.split(' ')
	if toolsplit[0] == "help":
		printHelp(toolsec,toolsplit)
	elif (toolsplit[0] == "bruteforce") or (toolsplit[0] == "bf"):
		execBF(toolsec,toolsplit)
	elif (toolsplit[0] == "seperate_empw") or (toolsplit[0] == "sep_ep"):
		sepPW(toolsec,toolsplit)
	elif (toolsplit[0] == "combine_empw") or (toolsplit[0] == "com_ep"):
		comPW(toolsec,toolsplit)
	elif (toolsplit[0] == "geotrace") or (toolsplit[0] == "geotr"):
		geoTrace(toolsec,toolsplit)
	elif (toolsplit[0] == "test") or (toolsplit[0] == "t"):
		testFunc(toolsec,toolsplit)
	elif toolsec == "":
		Main()
	elif toolsplit[0] in exit:
		print('\nClosing PyTools..\n')
		KeyboardInterrupt
	else:
		print("\n\n\n\n\n\n\n\n\n\n\n\n")
		print("[ERROR]: Command \"" + toolsplit[0] + "\" not found.\n")
		Main()
# ----------------------------- HELP FUNCTION ----------------------------- #
def printHelp(input,inpspl):
	if inpspl[0] != "help":
		print("[ERROR]: Called wrong function. \n")
		Main()
	if len(inpspl) > 1:
		if (inpspl[1] == "help"):
			print("\nhelp - give tips or info on a module")
			print("Info        : Shows information about a module.")
			print("Usage       : help or help (module)")
			print("Example     : help bf")
			print("EX Output   : shows bruteforce module info\n")
			print("Extra Info  : none")
		elif (inpspl[1] == "bf") or (inpspl[1] == "bruteforce"):
			print("\nbruteforce (alias: bf) - bruteforce a command")
			print("Info        : Allows wordlist creation piped to a command.")
			print("Usage       : bruteforce | command bfhere | minlength,maxlength | charset")
			print("Example     : bruteforce | echo bfhere | 1,2 | a,b") 
			print("EX Output   : a,  b, aa, ab, ba, bb\n")
			print("Extra Info  : none")
		elif (inpspl[1] == "sep_ep") or (inpspl[1] == "seperate_empw"):
			print("\nseperate_empw (alias: sep_ep) - seperate usernames from passwords")
			print("Info        : seperates values in email:pw format from a file")
			print("Usage       : seperate_empw file.txt -o output.txt")
			print("Example     : seperate_empw ~/Desktop/dump.txt -o ~/Desktop/sep.txt")
			print("EX Output   : email")
			print("              password")
			print("Extra Info  : dump.txt containing a single line, \'email:password\'\n")
		elif (inpspl[1] == "com_ep") or (inpspl[1] == "seperate_empw"):
			print("\ncombine_empw (alias: com_ep) - undoes seperate_empw")
			print("Info        : combines sep_ep files into a email:pw format")
			print("Usage       : combine_empw seperated.txt -o output.txt")
			print("Example     : combine_empw ~/Desktop/sep.txt -o ~/Desktop/users.txt")
			print("EX Output   : email:password")
			print("Extra Info  : sep.txt contains email and password in sep_pw format\n")
		elif (inpspl[1] == "geotr") or (inpspl[1] == "geotrace"):
			print("\ngeotrace (alias: geotr)      - allows traceroute to print locations")
			print("Info        : gets locations from each IP and displays them")
			print("Usage       : geotrace ip_address")
			print("Example     : geotrace google.com")
			print("EX Output   : ae3.cs1.ord2.us.eth.zayo.com (64.125.29.209)  532.292 ms  487.280 ms  486.956 ms -- Louisville, Colorado, US")
			print("              ae27.cr1.ord2.us.zip.zayo.com (64.125.30.243)  380.132 ms  566.112 ms  565.798 ms -- Louisville, Colorado, US")
			print("Extra Info  : The EX Output was only a fraction of a real traceroute.")
			print("              Requires valid connection to ipinfo.io")
		else:
			error("unknown_mod",inpspl[1])
		Main()
	else:
		print("\nhelp                           - show this menu")
		print("bruteforce (alias: bf)         - bruteforce a command")
		print("seperate_empw (alias: sep_ep)  - seperate emails from passwords")
		print("combine_empw (alias: com_ep)   - combine emails and password from sep_ep")
		print("geotrace (alias: geotr)        - allows traceroute to print locations")
		print("Use help (module) for more help on a module.\n")
	Main()
# ----------------------------- ERRORS ----------------------------- #
def error(which_error,error_arg):
	if which_error == "wrong_func":
		print("[ERROR]: Called wrong function.")
	if which_error == "unknown_mod":
		print("[ERROR]: Unknown module : " + error_arg + ".\n")
	if which_error == "syntax_err":
		print("[ERROR]: Invalid syntax or number of arguments. (" + str(len(error_arg)) + ")\n")
	Main()
# ----------------------------- BRUTEFORCE ----------------------------- #
def execBF(input,inpspl):
	if inpspl[0] != "bf" and inpspl[0] != "bruteforce":
		print("[ERROR]: Called wrong function.\n")
		Main()
	if input == "bf" or input == "bf help":
		printHelp("help bf", ["help","bf"])
	inputs = input.split(" | ")
	if (len(inputs) != 4) or (type(inputs[1]) != str):
		error("syntax_err",inputs)
	i = 0
	bfcommand = inputs[1]
	bfcargs = bfcommand.split('bfhere')
	if len(bfcargs) != 2:
		print("[ERROR]: Please only use 'bfhere' once in the command argument.")
		Main()
	while i < len(inputs[2]):
		inptwothis = (inputs[2])[i]
		if inptwothis not in "0123456789" and inptwothis != ",":
			print("[ERROR]: The 2nd argument (\"" + inputs[2] + "\") needs to be a number set with one comma.\n")
			Main()
		if i == len(inputs[2]):
			inputs[2] = int(inputs[2])
		i += 1
	charset = inputs[3].split(',')
	length = inputs[2]
	minlength = int((length.split(','))[0])
	maxlength = int((length.split(','))[1])
	if minlength > maxlength:
		print("[ERROR]: Minimum length can't be greater than maximum length.")
		Main()
	combinations = 0
	jj = minlength
	while jj <= maxlength:
		thiscombo = len(charset) * (len(charset)**(jj - 1))
		combinations += thiscombo
		jj += 1
	print("\nWordlist Generator will now create and execute " + str(combinations) + " commands.\n")
	raw_input("Press return when you wish to begin.\n")
	wordlist = ''
	for n in range(minlength, maxlength+1):
		for xs in itertools.product(charset, repeat=n):
			os.system(bfcargs[0] + (''.join(xs)) + bfcargs[1])
	print("\nSuccessfully executed " + str(combinations) + " commands.")
	Main()
# ----------------------------- SEPERATE EMPW ----------------------------- #
def sepPW(input,inpspl):
	if inpspl[0] != "sep_ep" and inpspl[0] != "seperate_empw":
		error("wrong_func",'')
	if "seperate_empw" in input:
		args = input.split("seperate_empw")[1]
	else:
		args = input.split("sep_ep")[1]
	if "-o" not in args:
		error("syntax_err",'args')
	inputs = ['','','']
	inputs[1] = (args.split(' -o ')[0])[1:]
	inputs[2] = args.split(' -o ')[1]
	if len(inputs) == 1:
		printHelp('',['help','sep_ep'])
	if len(inputs) != 3:
		error("syntax_err",inpspl)
	print("What's the title of the page?")
	title = raw_input("> ")
	check_tilde_one = 0
	while check_tilde_one < len(inputs[1]):
		if (inputs[1])[check_tilde_one] == "~":
			inponesplit = inputs[1].split("~")
			inputs[1] = inponesplit[0] + userpath + inponesplit[1]	# parse for tilde, change tilde to $HOME for inputs[1]
		check_tilde_one += 1
	check_tilde_two = 0
	while check_tilde_two < len(inputs[2]):
		if (inputs[2])[check_tilde_two] == "~":
			inptwosplit = inputs[2].split("~")
			inputs[2] = inptwosplit[0] + userpath + inptwosplit[1]	# parse for tilde, change tilde to $HOME for inputs[2]
		check_tilde_two += 1
	dump_line = open(inputs[1]).read().split("\n")
	dump_line = filter(lambda a: a != '', dump_line)		# remove empty values like ''
	dump_var = 0
	emails, pws = [], []
	while dump_var < len(dump_line):
		this_line = dump_line[dump_var]
		if ":" not in this_line:
			print("[WARN]: Colon (\':\') not in line " + str(int(dump_var) + 1) + ". Skipping...\n")
			dump_var += 1
			continue
		this_email = this_line.split(':')[0]
		this_pw = this_line.split(':')[1]
		emails.append(this_email)
		pws.append(this_pw)
		dump_var += 1
	sep_end = open(inputs[2], 'w')
	sep_end.write("\n" + title + "\n\n")
	sep_end.write('----------\nEMAILS:\n----------\n')
	email_var = 0
	while email_var < len(emails):
		sep_end.write(emails[email_var] + "\n")
		email_var += 1
	sep_end.write('\n----------\nPASSWORDS:\n----------\n')
	pw_var = 0
	while pw_var < len(pws):
		sep_end.write(pws[pw_var] + "\n")
		pw_var += 1
	sep_end.close()
	print("Finished formatting.")
	view_yn = raw_input("View it? [y/n]: ")
	if view_yn == "y":
		print(open(inputs[2],"r").read())
		print('\n')
	Main()
# ----------------------------- COMBINE EMPW ----------------------------- #
def comPW(input,inpspl):
	if inpspl[0] != "com_ep" and inpspl[0] != "combine_empw":
		error("wrong_func",'')
	if input == "com_ep" or input == "combine_empw":
		printHelp('',['help','com_ep'])
	if "combine_empw" in input:
		args = input.split("combine_empw")[1]
	else:
		args = input.split("com_ep")[1]
	if "-o" not in args:
		error("syntax_err",'args')
	inputs = ['','','']
	inputs[1] = (args.split(' -o ')[0])[1:]
	inputs[2] = args.split(' -o ')[1]
	check_tilde_one = 0
	while check_tilde_one < len(inputs[1]):
		thisone = inputs[1][check_tilde_one]
		if thisone == "~":
			inponesplit = inputs[1].split("~")
			inputs[1] = inponesplit[0] + userpath + inponesplit[1]
		check_tilde_one += 1
	check_tilde_two = 0
	while check_tilde_two < len(inputs[2]):
		thisone = inputs[2][check_tilde_two]
		if thisone == "~":
			inptwosplit = inputs[2].split("~")
			inputs[2] = inptwosplit[0] + userpath + inptwosplit[1]
		check_tilde_two += 1
	sep_file = open(inputs[1]).read()
	if '\n\n----------\nEMAILS:\n----------\n' not in sep_file or '\n----------\nPASSWORDS:\n----------\n' not in sep_file:
		print("[ERROR]: This file isn't formatted by sep_ep.")
		Main()
	sep_split = sep_file.split('\n----------\nPASSWORDS:\n----------\n')
	sep_emails = (sep_split[0].split('\n\n----------\nEMAILS:\n----------\n')[1]).split('\n')
	sep_pw = sep_split[1].split('\n')
	sep_pw = filter(lambda a: a != '', sep_pw)					# remove empty values like ''
	sep_emails = filter(lambda a: a != '', sep_emails)			# remove empty values like ''
	if len(sep_pw) != len(sep_emails):
		print("[ERROR]: Amount of emails not equal to amount of passwords.")
	sep_split = [sep_emails,sep_pw]
	e_p_list = []
	generic_variable = 0
	while generic_variable < len(sep_split[0]):					#
		this_email = sep_split[0][generic_variable]				#
		this_pw = sep_split[1][generic_variable]				# assign emails to designated passwords
		e_p_list.append(this_email + ":" + this_pw + "\n")		#
		generic_variable += 1									#
	os.system('touch ' + inputs[2])
	output_file = open(inputs[2], 'w')
	another_generic_variable = 0
	while another_generic_variable < len(e_p_list):				#
		output_file.write(e_p_list[another_generic_variable])	# write above list to specified output file
		another_generic_variable += 1							#
	output_file.close()
	print("Successfully finished combining credentials.")
	view_yn = raw_input("View the output? [y/n]: ")
	if view_yn == "y":
		print('')
		os.system("cat " + inputs[2])
	print('')
	Main()
# ----------------------------- GEO-TRACEROUTE ----------------------------- #
def geoTrace(input,inpspl):
	print("\nSorry, but this section isn't finished yet.\n")
	Main()
# -------------------------------- TESTFUNC -------------------------------- #
def testFunc(input,inpspl):
	i = 0
	import time
	while True:
		print("Hello there. (" + str(i)w + ")")
		time.sleep(1)
		i += 1
try:
	Main()
except KeyboardInterrupt:
			print('\n\nClosing PyTools..\n')
