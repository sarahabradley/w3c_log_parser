from abc import ABC, abstractmethod
import numpy as np

class LogParser(ABC):
    """Abstract class defining the methods and properties for parsing a log file"""

    NEWLINE_CHAR = '\n'
    SEPARATOR_CHAR = ' '

    @property
    def rawText(self) -> list[str]:
        return self._rawText

    def getRawData(self) -> list[str]:
        return self.rawText[1:]

    @abstractmethod
    def getFields(self) -> list[str]:
        pass

    def get2dDataArray(self):
        logArray = [i.split(self.SEPARATOR_CHAR) for i in self.getRawData()]
        return np.array(logArray)

    def loadDataSource(self, path: str, fileName: str):
        with open(file=path + '/' + fileName, newline=self.NEWLINE_CHAR) as file:
            fileContents = file.readlines()
            self._rawText = fileContents

    def countInField(self, fieldName):
        uniqueValues = {}
        fieldIndex = self.getFields().index(fieldName)
        for value in self.get2dDataArray()[:,fieldIndex]:
            if value in uniqueValues:
                uniqueValues[value] += 1
            else:
                uniqueValues[value] = 1
        return uniqueValues

    
class W3CParser(LogParser):

    FIELD_MARKER = '#Fields:'

    def getRawData(self) -> list[str]:
        fieldRowIndex = [n for n, l in enumerate(self.rawText) if l.startswith(self.FIELD_MARKER)][0]
        return self.rawText[(fieldRowIndex + 1):]
    
    def getFields(self) -> list[str]:
        try:
            fieldsLine: str = next(filter(lambda line: line.startswith(self.FIELD_MARKER), self.rawText))
        except StopIteration:
            print("Couldn't find a list of fields, failed to parse log file.")
        fields = fieldsLine.split(self.FIELD_MARKER, 1)[1].rstrip(self.NEWLINE_CHAR).strip()
        return fields.split(self.SEPARATOR_CHAR)
