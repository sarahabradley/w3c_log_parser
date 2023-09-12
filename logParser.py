from abc import ABC, abstractmethod
import numpy as np

class LogParser(ABC):
    """Abstract class defining the methods and properties for parsing a log file
    
    Attributes
    ----------
    rawText : list[str]
        a list of strings containing each new line of text within the log file as 
        a separate element, will only be populated once loadDataSource method has been called.
    NEWLINE_CHAR : str, const
        a constant representing the newline character, defaults to '\n'
    SEPARATOR_CHAR : str, const
        a constant representing the character that separates each element, defaults to ' '

    Methods
    -------
    getRawData() : list[str]
        returns a list of strings containing each new line of text, excluding any metadata like
        field names and date the log was created
    getFields() : list[str]
        returns a list of all the fields included in the log file
    get2dDataArray() : 2DArray
        returns the log data in a 2d numpy array
    loadDataSource(path, fileName) : None
        opens the file with the given path and fileName and uses the data from the file to populate 
        the rawText attribute
    countInField(fieldName) : dict
        For the specified fieldName, counts how many occurrences there are of each unique value and 
        returns a dictionary of { unique_value: total_occurrences, ... }
    """

    NEWLINE_CHAR = '\n'
    SEPARATOR_CHAR = ' '

    @property
    def rawText(self) -> list[str]:
        return self._rawText

    """Gets and returns the raw text with any metadata, e.g. field names, removed"""
    def getRawData(self) -> list[str]:
        # Base implementation assumes that there is a single line at the top of the file containing any metadata
        # Should be overriden in any child classes where this isn't the case
        return self.rawText[1:]

    @abstractmethod
    def getFields(self) -> list[str]:
        pass

    def get2dDataArray(self):
        # Split each row of the raw data into separate elements nested within the row element
        logArray = [i.split(self.SEPARATOR_CHAR) for i in self.getRawData()]
        return np.array(logArray) # Convert the nested list into a 2d numpy array for easier manipulation

    def loadDataSource(self, path: str, fileName: str):
        with open(file=path + '/' + fileName, newline=self.NEWLINE_CHAR) as file:
            fileContents = file.readlines()
            self._rawText = fileContents

    def countInField(self, fieldName):
        uniqueValues = {}
        fieldIndex = self.getFields().index(fieldName) # The column index of the relevant field
        for value in self.get2dDataArray()[:,fieldIndex]:
            if value in uniqueValues:
                uniqueValues[value] += 1
            else:
                uniqueValues[value] = 1
        return uniqueValues

    
class W3CParser(LogParser):
    """ Implementation of parser for log files in W3C format, inherits from abstract class LogParser"""

    FIELD_MARKER = '#Fields:'

    def getRawData(self) -> list[str]:
        # Find the index of the row where the field names are defined by checking whether each row
        # starts with the relevant string, stored in FIELD_MARKER
        # If there are multiple rows starting with this string, the first is taken
        fieldRowIndex = [n for n, l in enumerate(self.rawText) if l.startswith(self.FIELD_MARKER)][0]
        return self.rawText[(fieldRowIndex + 1):] # Return all rows following the fields row
    
    def getFields(self) -> list[str]:
        try:
            fieldsLine: str = next(filter(lambda line: line.startswith(self.FIELD_MARKER), self.rawText))
        except StopIteration:
            # TODO implement more robust logging rather than printing to terminal
            print("Couldn't find a list of fields, failed to parse log file.")
        # Split the string at the FIELD_MARKER and only take what follows it, stripping away the new line
        #  character and any excess whitespace
        fields = fieldsLine.split(self.FIELD_MARKER, 1)[1].rstrip(self.NEWLINE_CHAR).strip()
        return fields.split(self.SEPARATOR_CHAR)
