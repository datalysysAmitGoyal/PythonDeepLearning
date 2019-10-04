import json

def getJsonObject(filePath):
    returnObject = {}
    with open(filePath, 'r') as readJson:
        returnObject = json.load(readJson)
    return returnObject

def main():
    # Callling function for testing
    print(getJsonObject(r'config\TestJsonFile.json'))

# if __name__ == "__main__":
#     main()