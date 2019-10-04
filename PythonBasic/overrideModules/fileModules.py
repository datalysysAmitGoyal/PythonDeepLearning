import json

def getJsonObject(filePath):
    returnObject = {}
    with open(filePath, 'r') as readJson:
        returnObject = json.load(readJson)
    return returnObject

def main():
    # Callling function for testing
    # print(getJsonObject(r'D:\Development\My_Practise_Work\PythonDeepLearning\PythonBasic\TestJsonFile.json'))

if __name__ == "__main__":
    main()