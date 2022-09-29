import os
import json
from xlsx2csv import Xlsx2csv
import configparser
import tkinter as tk

def ignoreFilesWithLeftExtension(fileNames, leftExtension, verbose = False):
    '''from a fileList remove all files starting from leftExtension 
        it returns the list without the ignored files'''
    l = len(leftExtension)
    if verbose: 
        print('\nfileslist before ignoring files starting by %s' % leftExtension)
        print(fileNames)
    # ignore ghost file
    files2ignore = []
    for file in fileNames:
        if file[0:l] == leftExtension:
            files2ignore.append(file)
    for file in files2ignore:
        fileNames.remove(file)
    if verbose:
        print('\nfileslist after ignoring files starting by %s' % leftExtension)
        print(fileNames)
    return fileNames

def addPath2fileNames(fileNames, path):
    '''add the same path to a list of file names,
    it retunrs the list of filePaths'''
    filePaths = []
    for fileName in fileNames:
        filePaths.append(os.path.join(path, fileName))
    return filePaths

def importJsonFile(filepath):
    f = open(filepath) 
    data = json.load(f) 
    f.close() 
    return data

def writeJsonFile(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()

def updateJsonFile(filepath, new_key, new_value):
    data = importJsonFile(filepath)
    data[new_key] = new_value
    writeJsonFile(filepath, data)

def writeBinFileFromBinData(filepath, data):
    file = open(filepath, "wb")
    file.write(data)
    file.close()

def readBinFile(filepath):
    f = open(filepath,"rb")
    data = list(f.read())
    f.close()
    return data

def convertXlsx2Csv(path):
    list_of_file = os.listdir(path)
    for filename in list_of_file:
        if filename.split('.')[-1] == 'XLSX':
            filename_wo_extension = filename.split('.')[0]
            newfilename = filename_wo_extension + '.csv'
            dest_filepath = os.path.join(path, newfilename)
            filepath = os.path.join(path, filename)
            Xlsx2csv(filepath, outputencoding="utf-8").convert(dest_filepath)

def getAllDirContainingFiles(path):
    '''returns a list of touples containing the filename 
    and the path containinng the file. If the dir contains no file
    it is not returned'''
    return [(x[2], x[0]) for x in os.walk(path) if len(x[2]) is not 0]

def getAllFileNamesInDir(path):
    return [x[2] for x in os.walk(path) ][0]

def getUrlFromUrlIniFile(path):
    parser = configparser.RawConfigParser()
    parser.read(path)
    return parser['InternetShortcut']['url']

def writeFileFromString(filePath, string):
    outputFile = open(filePath,"w+") # the file we want to write
    print('\nWriting file %s', filePath)
    w = outputFile.write(string)
    outputFile.close()
    return w

def getFolderPathGui():
    root = tk.Tk()
    root.withdraw()
    folderSelected = tk.filedialog.askdirectory()
    print('user selects folder: %s', folderSelected)
    return folderSelected

def createDirIfNotExist(path):
    if not os.path.exists(path):
        os.makedirs(path)