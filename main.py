import logParser

def main():
    w3cParser = logParser.W3CParser()
    contents = w3cParser.loadDataSource('/Users/sarahbradley/Documents/Coding/test_log_files', 'w3c_example1.log')
    print(w3cParser.countInField('cs-uri-stem'))

if __name__=="__main__":
    main()