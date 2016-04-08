import zipfile
import optparse

def tryCrack(password):
	try:
		z.extractall(pwd=password)
		print "[+] Found password for archive %s: '%s'" % (zname, password) 
		exit(0)
	except:
		pass
		
def main():
	global z
	global zname
	
	parser = optparse.OptionParser("Usage: python zipAttack.py -f <zipfile> -w <wordlist>")
	parser.add_option("-f", dest="zname", type="string", help="specify zip file")
	parser.add_option("-w", dest="wname", type="string", help="specify word list")
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.wname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		wname = options.wname
	
	z = zipfile.ZipFile(zname)
		
	with open(wname) as f:
		for line in f:
			tryCrack(line.strip())
	print "[-] Could not find password in supplied word list."		

main()