import logParser

def main():
    w3cParser = logParser.W3CParser()
    contents = w3cParser.loadDataSource('/Users/sarahbradley/Documents/Coding/test_log_files', 'w3c_example1.log')
    uriHitCounts = w3cParser.countInField('cs-uri-stem')
    # Sort contents of uriHitCounts dictionary in descending order by value
    sortedHitCounts = sorted(uriHitCounts.items(), key=lambda x:x[1], reverse=True)
    print("\n---------------------------------------------------------------"
          + "\nRanked list of URI stems in descending order of hits"
          + "\n---------------------------------------------------------------\n")
    for uri in sortedHitCounts:
        print(f"{uri[0]}: {uri[1]}")

if __name__=="__main__":
    main()
