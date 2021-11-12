from ftplib import FTP
import ftplib
import os
import shutil
with FTP("ftp.heanet.ie") as ftp:
	print("--Rutas disponibles--")
	ftp.login()
	ftp.dir()
    #directorioscan = input("introduzca el directorio a escanear")#  
	directorioscan = "pub"
	print("--Archivos en la ruta--")
	ftp.cwd(directorioscan)
	ftp.dir()
    #ftp.retrlines('LIST') 
	filenames = ftp.nlst()
	ftp.close()
	try:
		os.mkdir("./"+str(directorioscan))
		os.mkdir("./"+str(directorioscan)+"/descargasftp")
		os.mkdir("./"+str(directorioscan)+"/descargasftp/archivostxt")
	except FileExistsError:
        #print("Carpeta "+str(directorioscan)+" ya existe")
		try:
			os.mkdir("./"+str(directorioscan)+"/descargasftp")
			os.mkdir("./"+str(directorioscan)+"/descargasftp/archivostxt")
		except FileExistsError:
			try:
				os.mkdir("./"+str(directorioscan)+"/descargasftp/archivostxt")
			except FileExistsError:
				pass
    #print(os.getcwd())
    #print(os.listdir())
	os.chdir("./"+str(directorioscan)+"/descargasftp")
	for filename in filenames:
		with open(filename, 'wb') as file :
			file.close()

	destination = './descargasftp/archivostxt'
	path = "./"
	ext = ('.txt', '.msg', '.README')
	text_files = []
	rutactual = os.getcwd()
	for f in os.listdir(path):
		if f.endswith(ext):
			text_files.append(f)
            #mover archivos TXT a la carpeta de los txt
            #dest = shutil.move(str(rutactual)+"/"+str(f), destination)
    # instruccion para decirle al sistema que mueva los txt a la carpeta archivostxt solo 
    # Tienes que iterar los nombres de los archivos txt
			os.system("move ./"+f+" ./archivostxt")
	for element in text_files:
		print(element)
	if not text_files:
		print("no hay archivos de texto, msg o readme en la carpeta")