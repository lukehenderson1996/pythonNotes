"""Logger class with multiple output options and data handling tools"""

# Author: Luke Henderson
# Version 1.0

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt

METRIC_PREFIX_SCALE = {
"f":-15,
"p":-12,
"n":-9,
"u":-6,
"m":-3,
" ":0,
"":0,
"k":+3,
"K":+3,
"M":+6,
"G":+9,
"P":+12,
"E":+15
}

DEFAULT_HEADER = {
'csv':'Date,Time,BTCUSD,Site\n',
'xml':'<?xml version="1.0" encoding="UTF-8"?>\n<root>\n\n'
}
DEFAULT_FILENAME = 'datalog'
DEFAULT_FILENAME_CSV = 'csv log'
DEFAULT_FILENAME_XML = 'xml log'

class ResultData:
    """data class for return of data in standard format
    marks time of creation in multiple formats"""
    resultData : list
    unit : str
    site : str #website
    capTime : float

    def __init__(self, resultData=None, unit="", site="", capTime=None):
        """Short description\n
        Args:
            capTime [int, optional]: can save exact time of
                data capture here"""
        if not isinstance(resultData, list):
            self.resultData = [resultData]
        else:
            self.resultData = resultData
        self.unit = unit
        self.site = site
        if capTime is None:
            capTime = time.time()
        self.capTime = capTime
        self.dateObj = datetime.fromtimestamp(capTime)
        self.humReadTime = self.dateObj.strftime("%H:%M:%S.%f")[:-3]
        self.humReadDate = self.dateObj.strftime("20%y-%m-%d")

class LOGGER:
    """This logs data to disk with optional formatting
    Current methods in use:
        __init__() creates list of actives files
        simpLog() will create simple csv and xml logs, 
            depending on what's active
        xmlCheckTag() will verify correct xml tag format
        close() will close all files and finalize xml formatting
        """

    def __init__(self, logCols=None, filename=None, prefix='', quiet=True, \
        csv=False, xml=False, absPath=None):
        """Logger with various output options\n
        Args:
            logCols [list of str]: populates the headers if not None\n
            filename [str, optional]: custom name of file to override default\n
            prefix [str, optional]: prefix to file names, default ''\n
            quiet [bool, optional]: False for log location information\n
            csv [bool, default/optional]: whether to create csv log under this instance\n
            xml [bool, optional]: whether to create xml log under this instance\n
            absPath [str, optional]: include file extension
                filename parameter will be ignored\n
                changes mode of logger to csv only, not tested for xml
        Notes:
            Number of logCols must exacly equal length of list when\n
            calling simpLog()"""
        self.logCols = logCols
        self.csv = csv
        self.xml = xml
        self.filesClosed = False

        #manage and open file(s)
        if not (csv or xml):
            csv = True #default to csv
        #for time at suffix:
        if not prefix=='':
            prefix += ' '
        fileSuffix = ' ' + str(time.time()).split('.')[0] #just the end for now
        # #for time at prefix:
        # if prefix == '':
        #     prefix = str(time.time()).split('.')[0] + ' ' + prefix
        # else:
        #     prefix = str(time.time()).split('.')[0] + ' ' + prefix + ' '
        # fileSuffix = ''

        #generate file path list
        if absPath is None:
            #relative path
            filePath = os.path.dirname(os.getcwd())
            filePathList = []
            filenameList = [filename, filename] #can change to accept list or str for filenames later
            if csv:
                if filenameList[0] is None:
                    filenameList[0] = DEFAULT_FILENAME_CSV
                filePathList.append(filePath + f'\\datalogs\\{prefix + filenameList[0] + fileSuffix}.csv')
            if xml:
                if filenameList[1] is None:
                    filenameList[1] = DEFAULT_FILENAME_XML
                filePathList.append(filePath + f'\\datalogs\\{prefix + filenameList[2] + fileSuffix}.xml')
        else:
            #absolute path
            filePathList = []
            filePathList.append(absPath)
        #generate file list, guaranteeing no modification of old files
        self.fileList = []
        for el in filePathList:
            fileExt = el.split('.')[-1]
            if not (fileExt=='csv' or fileExt=='xml'):
                cl.red('Error: Unsupported file extension: ' + fileExt)
                raise Exception
            thisFilePath = el
            while os.path.exists(thisFilePath):
                thisFilePath = thisFilePath[:-4]
                thisFilePath += '-1.' + fileExt
            if not quiet:
                print('Saving ' + fileExt + ' datalog as:')
                print('\t' + thisFilePath)
            self.fileList.append(open(thisFilePath, "a"))
            self.fileList[-1].ext = fileExt
        
        #write headers
        for el in self.fileList:
            if (logCols is None) or el.ext == 'xml':
                el.write(DEFAULT_HEADER[el.ext])
                el.flush()
            else:
                if el.ext == 'csv':
                    headerStr = logCols[0]
                    for elem in logCols[1:]:
                        headerStr += ',' + elem
                    el.write(headerStr + '\n')
                    el.flush()

    def __del__(self):
        if not self.filesClosed:
            self.close()

    def simpLog(self, dataInput):
        '''Simple logging to disk with only one type of formatting\n
        Args:
            data [list of str/int/float]: Any data input to be logged under
                previously defined columns (self.logCols)'''
        #data copy/conditioning/validating
        data = dataInput.copy()
        for i in range(len(data)):
            if isinstance(data[i], str):
                pass
            elif isinstance(data[i], int) or isinstance(data[i], float):
                data[i] = str(data[i])
            else:
                cl.red(f'Error: unexpected data type in simpLog(): {data[i]} {type(data[i])}')
                raise Exception
        #write to logs
        for el in self.fileList:
            if el.ext == 'csv':
                #error checking
                if len(data) != len(self.logCols):
                    cl.red('Error: logger data length mismatch with logCols length')
                    dt.info('self.logCols', self.logCols)
                    dt.info('data', data)
                    raise Exception
                #write content
                el.write(data[0])
                for elem in data[1:]:
                    el.write(',' + elem) #' , '
                el.write('\n')
                el.flush()
            if el.ext == 'xml':
                currTime = 'time_' + str(time.time())
                xmlEntryCont = ''
                for tagName, cont in zip(self.logCols, data):
                    self.xmlCheckTag(tagName)
                    xmlEntryCont += f'\t<{tagName}>{cont}</{tagName}>\n'
                self.xmlCheckTag(currTime)
                el.write(f'<{currTime}>\n{xmlEntryCont}</{currTime}>\n\n')
                el.flush()

    def log(self, resultData):
        '''to be used with ResultData class
        finish later'''
        if not isinstance(resultData, ResultData):
            print('incorrect args')
        else:
            print('correct args')

    def chrisLog(self, testNum, resultData, testDesc='', notes='', scaleUnit=None) -> None:
        """NOT CONVERTED TO LUKE'S CODE FORMAT
        logs the test data to the screen and the log file"""
        if notes == '': 
            addComma = ''
        else:
            addComma = ','
        if True:
            if scaleUnit is not None:
                self.scaleUnits(resultData, scaleUnit)
            print(f'TN{testNum}-{testDesc}', resultData.resultData, f'{resultData.unit} {resultData.instr}{addComma} {notes}')
            testDesc = f'"{testDesc}"' #add "" around string to deal with commas in the string
            notes = f'"{notes}"' #add "" around string to deal with commas in the string
            self.file.write(f'{testNum},{testDesc},{",".join([str(data) for data in resultData.resultData])},{resultData.unit},{resultData.instr},{notes},,{self.logValues.TEMP},{self.logValues.VCC},{self.logValues.PROG}\n')
            for site in self.sites.onActiveSite():
                if isinstance(resultData.resultData[site], bool): resultData.resultData[site] = int(resultData.resultData[site] == True) #convert True/False to 1/0 for spotfire
                if resultData.resultData[site] is None: resultData.resultData[site] = "" #remove none from the starfish log and leave empty instead
                self.file2.write(f'{testNum},{time.strftime("%x")},{time.strftime("%X")},{time.time()},{self.logValues.DeviceVersion},{self.logValues.UID+site},DeviceID,StarfishID,{site},{testDesc},{resultData.resultData[site]},{resultData.unit},{resultData.instr},{notes},,,{self.logValues.TEMP},{self.logValues.VCC},{self.logValues.PROG}\n')

    def xmlCheckTag(self, tagName) -> bool:
        '''Description\n
        Args:
            tagName [str]: tag name
        Return:
            [bool] True for pass, False for fail
        '''
        #check content of tag
        ret = True
        if tagName[0:3].lower()=='xml' or tagName[0].isnumeric():
            ret = False
        if tagName[0]=='-' or tagName[0]=='.' or tagName=='root':
            ret = False
        if " " in tagName:
            ret = False
        #final ruling
        if not ret:
            cl.yellow(f'Warning: Incorrect XML tag: {tagName}')
        return ret

    def scaleUnits(self, resultData, scaleUnit) -> None:
        """scales data from the current unit to the scaleUnit"""
        #find the scale factor for the scaling unit
        if len(scaleUnit) == 1 or \
          (len(scaleUnit) == 2 and scaleUnit.lower() == "hz") or \
          (len(scaleUnit) == 3 and scaleUnit.lower() == "ohm") or \
          (len(scaleUnit) == 4 and scaleUnit.lower() == "ohms"):
            scaleTo = 0
        else:
            prefix = scaleUnit[:1] #get prefix
            scaleTo = METRIC_PREFIX_SCALE[prefix]
        #find the scale factor for the current unit
        if len(resultData.unit) == 1 or \
          (len(resultData.unit) == 2 and resultData.unit.lower() == "hz") or \
          (len(resultData.unit) == 3 and resultData.unit.lower() == "ohm") or \
          (len(resultData.unit) == 4 and resultData.unit.lower() == "ohms"):
            scaleFrom = 0
        else:
            prefix = resultData.unit[:1] #get prefix
            scaleFrom = METRIC_PREFIX_SCALE[prefix]
        scaleFactor = scaleFrom - scaleTo
        for idx in range(len(resultData.resultData)):
            if resultData.resultData[idx] is not None:
                resultData.resultData[idx] *= 10**scaleFactor
        resultData.unit = scaleUnit

    def close(self) -> None:
        '''closes files'''
        for el in self.fileList:
            if el.ext == 'xml':
                el.write('</root>')
                el.close()
            else:
                el.close()
        self.filesClosed = True
