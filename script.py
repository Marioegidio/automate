class Dati():
	def __init__(self, name, data):
		self.name = name
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
				print(temp.name + "--->"+str(temp.data))
			temp=Dati(line.split(".")[0], list())
			print(line, end='')


		line = reader.readline()

stringaFinale=""
oldTitolo=""

for dato in listaDati:

	newTitolo= dato.name.upper().split()[0]+dato.name.upper().split()[1]
	if oldTitolo != newTitolo :
		stringaFinale+="\n"+newTitolo+";\n"
		oldTitolo=newTitolo

	tipoTest=dato.name.split(" ")
	stringaFinale+=tipoTest[2]+" "+tipoTest[3]+" "+tipoTest[4]+";"

	for val in dato.data:
		stringaFinale+=str(val)+";"
	stringaFinale+="\n"
		

print("ENDD \n"+stringaFinale)


# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()