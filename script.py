class Dati():
	def __init__(self, title, data):
		self.title = title
		self.data = data

temp=None
listaDati=list()

with open('/Users/marioegidio/Desktop/test', 'r') as reader:
	# Read and print the entire file line by line
	line = reader.readline()
	while line != '':  # The EOF char is an empty string
		
		if not line.startswith("Concorrenza"):
			if line.startswith("Time per request: ") and line.endswith("[ms] (mean)\n"):
				line= line.split(" ")[9]
				temp.data.append(float(line))
				print(line, end='\n')
		else:
			if temp is not None:
				listaDati.append(temp)
				print(temp.title + "--->"+str(temp.data))
			temp=Dati(line.split(".")[0], list())
			print(line, end='')


		line = reader.readline()

stringaFinale=""
oldTitolo=""

for dato in listaDati:

	newTitolo= dato.title.upper().split()[0]+dato.title.upper().split()[1]
	if oldTitolo != newTitolo :
		stringaFinale+="\n"+newTitolo+";\n"
		oldTitolo=newTitolo

	tipoTest=dato.title.split(" ")
	stringaFinale+=tipoTest[2]+" "+tipoTest[3]+" "+tipoTest[4]+";"

	for val in dato.data:
		stringaFinale+=str(val)+";"
	stringaFinale+="\n"
		

print("*********\n"+stringaFinale)


f = open("import.csv", "w")
f.write(stringaFinale)
f.close()