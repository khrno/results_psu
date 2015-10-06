'''
{
	"items": [
		{
			label:	"j. hartmann",
			type:	"Place",
			ciudad:	"maring",
			pais:	"brasil",
			location:	"maring brasil",
		},
		.....
		
		{ id: 'r. khedri', addressLatLng: '-2.896617,-79.007621' },
		{ id: 'c. velasco', addressLatLng: '-2.896617,-79.007621' },
		{ id: 'e. morales', addressLatLng: '-2.896617,-79.007621' },
		{ id: 'l. gama', addressLatLng: '-2.896617,-79.007621' }
	]
}

'''
'''
types: {
           "Person": {
               pluralLabel:  "People"
           }
       },
       properties: {
           "age": {
               valueType:    "number"
           },
           "parentOf": {
               label:        "parent of",
               reverseLabel: "child of",
               valueType:    "item"
           }
       },
'''


'''
agno,rbd,nombre_establecimiento,nombre_comuna,nombre_deprov,nombre_region,numero_region,dependencia,area_geografica,estado,latitud,longitud,alumnos_psu,psu_lenguaje,psu_matematica,psu_nem,alumnos_psu_lenguaje,alumnos_psu_matematica,alumnos_psu_nem
'''

files = [
	'Establecimiento_PSU_anio_2006.csv',
	'Establecimiento_PSU_anio_2007.csv',
	'Establecimiento_PSU_anio_2008.csv',
	'Establecimiento_PSU_anio_2009.csv',
	'Establecimiento_PSU_anio_2010.csv',
	'Establecimiento_PSU_anio_2011.csv',
	'Establecimiento_PSU_anio_2012.csv',
	]
for f in files:
	outfh = open(f.split(".")[0]+".js","w")
	fh = open(f,"r")
	cont = 0
	'''
		properties: {
           "matematicas" : {
               valueType: "number"
           },
           "lenguaje" : {
           		valueType: "number"
           },
           "nem" : {
           		valueType: "number"
           }
       },
	'''
	outfh.write('{\n')
	outfh.write('\tproperties: {\n')
	outfh.write('\t\t"matematicas" : {\n')
	outfh.write('\t\t\tvalueType: "number"\n')
	outfh.write('\t\t},\n')
	outfh.write('\t\t"lenguaje" :{\n')
	outfh.write('\t\t\tvalueType: "number"\n')
	outfh.write('\t\t},\n')
	outfh.write('\t\t"nem" :{\n')
	outfh.write('\t\t\tvalueType: "number"\n')
	outfh.write('\t\t}\n')
	outfh.write('\t},\n')
	outfh.write('\t"items": [\n')
	for line in fh.readlines():
		if cont>0:
			line = line.split("\n")[0]
			fields = line.replace("'","").split(",")
			if len(fields)>1:
				outfh.write("\t\t{\n")
				outfh.write('\t\t\tlabel: "'+fields[2]+'",\n')	
				outfh.write('\t\t\ttype: "Establecimiento",\n')
				outfh.write('\t\t\tprovincia: "'+fields[4]+'",\n')
				outfh.write('\t\t\tcomuna: "'+fields[3]+'",\n')
				outfh.write('\t\t\tregion: "'+fields[5]+'",\n')
				outfh.write('\t\t\tdependencia: "'+fields[7]+'",\n')
				outfh.write('\t\t\tmatematicas: "'+fields[-5]+'",\n')
				outfh.write('\t\t\tlenguaje: "'+fields[-6]+'",\n')
				outfh.write('\t\t\tnem: "'+fields[-4]+'"\n')
				outfh.write("\t\t},\n")
		cont+=1
	fh.close()
	cont = 0
	fh = open(f,"r")
	for line in fh.readlines():

		if cont>0:
			line = line.split("\n")[0]
			fields = line.replace("'","").split(",")
			if len(fields)>1:
				outfh.write("\t\t{ id: '"+fields[2]+"', addressLatLng: '"+fields[10]+","+fields[11]+"' },\n")
		cont+=1
	outfh.write("\t]\n}")		
	outfh.close()
	
	
		
