'''Logger class with multiple output options and data handling tools'''

# Author: Luke Henderson
__version__ = '1.32'
_PY_VERSION = (3, 7)

import os
import platform
import time
from datetime import datetime

import colors as cl
import debugTools as dt
import utils as ut

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

    def __init__(self, logCols=None, prefix='', filename=None, quiet=True, \
        csv=False, xml=False, absPath=None, persistent=False):
        """Logger with various output options\n
        Args:
            logCols [list of str]: populates the headers if not None\n
            filename [str, optional]: custom name of file to override default\n
            prefix [str, optional]: prefix to file names, default ''
                format: 'prefix Text' or 'subfolder/' 
            quiet [bool, optional]: False for log location information\n
            csv [bool, default/optional]: whether to create csv log under this instance\n
            xml [bool, optional]: whether to create xml log under this instance\n
            absPath [str, optional]: include file extension
                filename parameter will be ignored\n
                changes mode of logger to csv only, not tested for xml
            persistent [bool, optional]: use same file if already exists (true)
                or create unique files per run (False)
        Notes:
            Number of logCols must exacly equal length of list when\n
            calling simpLog()"""
        self.logCols = logCols
        self.csv = csv
        self.xml = xml
        self.filesClosed = False
        plat = platform.system()

        #validate input parameters
        if not logCols == None:
            assert isinstance(logCols, list)
            for col in logCols:
                assert isinstance(col, str)
                assert not ',' in col
        assert isinstance(prefix, str)
        assert isinstance(filename, str) or filename==None
        assert isinstance(quiet, bool)
        assert isinstance(csv, bool)
        assert isinstance(xml, bool)
        assert isinstance(absPath, str) or absPath==None
        assert isinstance(persistent, bool)
        #platform-dependent validation
        if plat == 'Windows':
            sep = '\\'
            incorrectSep = '/'
        else:
            sep = '/'
            incorrectSep = '\\'
        if prefix and incorrectSep in prefix:
            # cl.red('Error (logger.py): Incorrect separator in prefix')
            prefix = ut.pth(prefix)
        if filename and incorrectSep in filename:
            # cl.red('Error (logger.py): Incorrect separator in filename')
            filename = ut.pth(filename)
        if absPath and incorrectSep in absPath:
            # cl.red('Error (logger.py): Incorrect separator in absPath')
            absPath = ut.pth(absPath)

        #manage and open file(s)
        if not (csv or xml):
            csv = True #default to csv
        #for time at suffix:
        if filename is None:
            if not prefix=='':
                prefix += ' '
            fileSuffix = ' ' + str(time.time()).split('.')[0] #just the end for now
        else:
            fileSuffix = ''
        # #for time at prefix:
        # if prefix == '':
        #     prefix = str(time.time()).split('.')[0] + ' ' + prefix
        # else:
        #     prefix = str(time.time()).split('.')[0] + ' ' + prefix + ' '
        # fileSuffix = ''

        #generate file path list
        if absPath is None:
            #relative path
            filePathList = []
            filenameList = [filename, filename] #can change to accept list or str for filenames later
            if csv:
                if filenameList[0] is None:
                    filenameList[0] = DEFAULT_FILENAME_CSV
                thisFilePath = ut.pth(f'/datalogs/{prefix + filenameList[0] + fileSuffix}.csv', 'rel1')
                if not os.path.exists(os.path.dirname(thisFilePath)):
                    cl.yellow(f"Warning (logger.py): Directory doesn't exist. Creating subfolder(s) for directory {os.path.dirname(thisFilePath)}")
                    os.makedirs(os.path.dirname(thisFilePath))
                filePathList.append(thisFilePath)
            if xml:
                if filenameList[1] is None:
                    filenameList[1] = DEFAULT_FILENAME_XML
                thisFilePath = ut.pth(f'/datalogs/{prefix + filenameList[1] + fileSuffix}.xml', 'rel1')
                if not os.path.exists(os.path.dirname(thisFilePath)):
                    cl.yellow(f"Warning (logger.py): Directory doesn't exist. Creating subfolder(s) for directory {os.path.dirname(thisFilePath)}")
                    os.makedirs(os.path.dirname(thisFilePath))
                filePathList.append(thisFilePath)
        else:
            #absolute path
            ut.pth(absPath)
            if not os.path.exists(os.path.dirname(absPath)):
                cl.yellow(f"Warning (logger.py): Directory doesn't exist. Creating subfolder(s) for directory {os.path.dirname(absPath)}")
                os.makedirs(os.path.dirname(absPath))
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
            appending = False
            if not persistent:
                while os.path.exists(thisFilePath):
                    thisFilePath = thisFilePath[:-4]
                    thisFilePath += '-1.' + fileExt
            else:
                if os.path.exists(thisFilePath):
                    appending = True
            if not quiet:
                print('Saving ' + fileExt + ' datalog as:')
                print('\t' + thisFilePath)
            self.fileList.append(open(thisFilePath, "a"))
            self.fileList[-1].ext = fileExt
        
        #write headers
        if not appending:
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
        if hasattr(dataInput, 'copy'):
            data = dataInput.copy()
        else:
            data = dataInput
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

    def logBlankRow(self):
        '''Logs a blank csv row'''
        self.simpLog(['']*len(self.logCols))

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
        if hasattr(self, 'fileList'):
            for el in self.fileList:
                if el.ext == 'xml':
                    el.write('</root>')
                    el.close()
                else:
                    el.close()
        self.filesClosed = True

class ManagedLog:
    '''Managed Log'''

    def __init__(self, logCols, prefix=''):
        '''Manages a single log per day regardless of program interruptions\n
        Args:
            logCols [list of str]: populates the headers if not None\n
            prefix [str, optional]: prefix to file names, default ''\n
        Notes:
            filename will be in the following format: 
                [prefix]YYYY-MM-DD.csv
            Only works for csv files for now'''
        self.logCols = logCols
        self.prefix = prefix

        self.log = None
        self.prevLoggedDate = '1970-01-01' #date the last datapoint was logged for, human readable time from utils.py
        

    def manLog(self, dataInput):
        '''Managed log: \n
        Args:
            data [list of str/int/float]: Any data input to be logged under
                previously defined columns (self.logCols)'''
        humReadDate, humReadTime = ut.humTime()
        if humReadDate != self.prevLoggedDate:
            cl.purple(f'Managed log: logging for new day, filename: {self.prefix}{humReadDate}.csv')
            self.log = LOGGER(logCols=self.logCols, filename=f'{self.prefix}{humReadDate}', persistent=True)
        self.log.simpLog(dataInput)
        self.prevLoggedDate = humReadDate

    def logBlankRow(self):
        '''Logs a blank csv row'''
        self.manLog(['']*len(self.logCols))
