# python3.7.3
# Author: Erick Enriquez - eenriquez@stanford.edu
# load_conversation_files.py - Pulls data from a spreadhsheet, maps the data to the appropriate fields, and
# writes each row of data to a single text file, where each file is saved in a common folder. 
import openpyxl, pprint, os #useful import packages
from paths import *
from dataFields import *

# Takes a row corresponding to a single conversation and returns a dictionary of its
# attributes to the values written on the spreadsheet.
def pull_conversation_data(currRow, fields):
    currConv = {}
    for i in range(len(fields)):
        currConv[fields[i]] = str(currRow[i].value)
    return currConv

# Takes in a sheet containing information about all the conversations
# and uses that data to create a list of conversation data.
def organize_data(sheet):
    sheetData = []
    for i in range(numConversations): # This value should be modified in 'dataFields.py' when conversations are added.
        currFile = pull_conversation_data(list(sheet.rows)[i], convDataFields)
        sheetData.append(currFile)
    return sheetData

# Writes a given attribute to a given file and adds delimeters to ensure clean reading by other tools.
def write_fields(data, index, file):
	for i in range(len(cleanData)):
		if data[index]['status'] == 'publish':
			file.write(data[index][cleanData[i]])
			file.write('. ')

# Writes relevant data from the xmlData we extracted such that each conversation contains its own file in the folder 'conversationResults'.
def write_conversation_files(conversations):
	print('Writing conversation files...')
	for i in range(len(conversations)):
		resultFile = open(conversationResultPath + str(i), 'w')
		write_fields(conversations, i, resultFile)
		resultFile.close()
	print('Done.')

landTalkWorkBook = openpyxl.load_workbook(scrapedDataPath)
conversationData = organize_data(landTalkWorkBook[collectionSheet])
write_conversation_files(conversationData)