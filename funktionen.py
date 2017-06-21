import platform
import os
import shutil
import time
import hashlib
import xml.dom.minidom
import xml.etree.ElementTree
import re

def nameCount(name, targetPath):
	pathXmlFile = targetPath + os.sep + 'info.xml'
	if os.path.exists(pathXmlFile):
		f = open(pathXmlFile, 'r')
		xmlFileData = f.read()
		f.close()
		dom4 = xml.dom.minidom.parseString(xmlFileData)
		volumeIdPosition = dom4.getElementsByTagName('count')
		volumeId = str(int(volumeIdPosition[0].firstChild.nodeValue) + 1)
		fileName = 'disk' + volumeId + name
	return fileName

## Liste mit Dateien und Ordnern
def contentList(path, listFileName, targetPath):
	content = os.listdir(path)	# in die Klammer den gewünschten Pfad einfügen 
	content.sort() # sortiert Liste alphabetisch!
	openLstFile = targetPath + os.sep + listFileName
	f = open(openLstFile, 'a')				
	ueberschrift = path + ':'
	f.write(ueberschrift + '\n')		# '\n' Zeilenumbruch
	path_size = os.stat(path)			 
	path_size_int = path_size.st_size	 
	path_size_str = str(path_size_int)	# Wichtig um String zu casten
	f.write(path_size_str + '\n')
	for i in range(0,len(content)):
		file = path + os.sep + content[i]
		einstellungen = os.stat(file)			
		speicher_int = einstellungen.st_size
		speicher_str = str(speicher_int)		# nullen / leerzeichen auffüllen! 
		while len(speicher_str) <= 10:
			speicher_str = '0' + speicher_str
		rechte_int = einstellungen.st_mode
		rechte_oc = oct(rechte_int)
		rechte_oc = rechte_oc[-3:]
		rechte_str = str(rechte_oc)
		daten = rechte_str + " " + speicher_str + " " + time.ctime(os.path.getmtime(file)) + " " + content[i]
		print(daten)
		f.write(daten + '\n')
	f.close()
	return content
	
## xml-parser
def volumeMetadata(basicPath, name, media, label, description, remarks):
	path = basicPath + os.sep + 'info.xml'
	print(path)

	f = open(path, 'r')
	data = f.read()
	f.close()
	dom1 = xml.dom.minidom.parseString(data)
	vol = dom1.getElementsByTagName('volume')
	# Attribute finden und in liste speichern
	attributeList = []
	for element in vol:
		for elem in element.attributes.values():
			attributeList.append(elem.firstChild.data)
	newAttribute = len(attributeList) + 1
	print(newAttribute)
	
	count = dom1.getElementsByTagName('count')
	count[0].firstChild.nodeValue = str(newAttribute)
	
	def checkWrittenFile(file, path):
		fileNames = 'disk' + str(len(attributeList) + 1) + file
		filePath = path + os.sep + fileNames
		if os.path.exists(filePath):
			return 'written', fileNames
		else:
			return 'write error', fileNames
	
	statusImg, fileImg = checkWrittenFile('.img', basicPath)
	statusMd5, fileMd5 = checkWrittenFile('.md5', basicPath)
	statusLst, fileLst = checkWrittenFile('.lst', basicPath)
	
	dom2 = xml.dom.minidom.Document()
	# create new vol
	newVol = dom2.createElement('volume')   # create new tag element 'volume'
	newVol.setAttribute('n', str(newAttribute))
	newVolName = dom2.createElement('name')
	newVolNameText = dom2.createTextNode(name)
	newVolMedia = dom2.createElement('media')
	newVolMediaText = dom2.createTextNode(media)
	newVolLabel = dom2.createElement('label')
	newVolLabelText = dom2.createTextNode(label)
	newVolDescription = dom2.createElement('description')
	newVolDescriptionText = dom2.createTextNode(description)
	newVolRemarks = dom2.createElement('remarks')
	newVolRemarksText = dom2.createTextNode(remarks)
	newVolImgfile = dom2.createElement('imgfile')
	newVolImgfile.setAttribute('status', statusImg)
	newVolImgfile.setAttribute('md5', md5Image)
	newVolImgfileText = dom2.createTextNode(fileImg)
	newVolMd5file = dom2.createElement('md5file')
	newVolMd5file.setAttribute('status', statusMd5)
	newVolMd5fileText = dom2.createTextNode(fileMd5)
	newVolLstfile = dom2.createElement('lstfile')
	newVolLstfile.setAttribute('status', statusLst)
	newVolLstfileText = dom2.createTextNode(fileLst)

	newVolName.appendChild(newVolNameText) # append textnode to element newVolName
	newVol.appendChild(newVolName)         # append element newVolName to element newVol
	newVolMedia.appendChild(newVolMediaText)
	newVol.appendChild(newVolMedia)
	newVolLabel.appendChild(newVolLabelText)
	newVol.appendChild(newVolLabel)
	newVolDescription.appendChild(newVolDescriptionText)
	newVol.appendChild(newVolDescription)
	newVolRemarks.appendChild(newVolRemarksText)
	newVol.appendChild(newVolRemarks)
	newVolImgfile.appendChild(newVolImgfileText)
	newVol.appendChild(newVolImgfile)
	newVolMd5file.appendChild(newVolMd5fileText)
	newVol.appendChild(newVolMd5file)
	newVolLstfile.appendChild(newVolLstfileText)
	newVol.appendChild(newVolLstfile)

	root = dom2._get_documentElement()

	dom2.appendChild(newVol)
	dataVol = dom2.toprettyxml()
	dom2 = xml.dom.minidom.parseString(dataVol)

	x = dom1.importNode(dom2.childNodes[0], True)
	dom1.childNodes[0].appendChild(x)
	print(dom1.toxml())

	# count hochzaehlen
	#volumeIdPosition = dom1.getElementsByTagName('count')
	#volumeId = str(int(volumeIdPosition[0].firstChild.nodeValue) + 1)
	#volumeIdTag = '<count>' + volumeId + '</count>'
#	volumeIdTag = '<count>' + str(newAttribute) + '</count>'
#	print('volumeIdTag: ', volumeIdTag)
	data2 = dom1.toxml()
#	data3 = re.sub("<count>(.)</count>", volumeIdTag,data2)
#	print('regex done?')
	path = basicPath + os.sep + 'info.xml'
	f = open(path, 'w')
	f.write(data2)
	f.close()


## md5 checksumme
def checkSum(imgPath):

	global md5Image
	md5FileName = nameCount('.md5', imgPath)

	imgFileList = [] 
	for file in os.listdir(imgPath): 
		if file.endswith('.img'):
			imgFileList.append(file)         

	if len(imgFileList) == 0:
		imgFileName = 'disk1.img'
	else:
		imgFileName = 'disk' + str(len(imgFileList)) + '.img'		
		
	md5LoadPath = imgPath + os.sep + imgFileName
	md5SavePath = imgPath + os.sep + md5FileName
	
	f = open(md5LoadPath, 'rb')
	daten = f.read()
	f.close()
	md5Image = hashlib.md5(daten).hexdigest()
	md5Image1 = md5Image + ' *' + md5FileName
	f = open(md5SavePath, 'w')
	f.write(md5Image1)
	f.close()
	return md5Image
	
## ein Imagetool 
def imageStandard(sourcePath, targetPath):
	checkOS = platform.platform()
	if checkOS[0:5] == 'Linux':
		logicalPath = sourcePath
	elif checkOS[0:7] == 'Windows':
		pathName = r'\\.\F:'
		logicalPath = pathName[:-2] + sourcePath[:-1]
	else:
		print('unkown os')
	
	imgFileName = nameCount('.img', targetPath)
	targetName = targetPath + os.sep + imgFileName
	
	shutil.copyfile(logicalPath, targetName)
	



