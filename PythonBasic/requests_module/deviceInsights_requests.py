import requests
from os import path
import os
import json
import logging
from pathlib import Path
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'cache-control': 'no-cache'}
labINFO, diINFO, logsWriter = {}, {}, None

def returnLogBufferObject(logFilePath):
    logger = None
    try:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(logFilePath)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter("%(asctime)s:%(msecs)3d %(levelname)7s -> %(message)s", "%H:%M:%S"))
        logger.addHandler(file_handler)
    except Exception as ERR:
        MessageBox(None, f"{ERR.__class__.__name__} in returnLogBufferObject :: {ERR}", 'Warning', 0)
    return logger

def getCompoundIDs():
    qcCompoundIDs = {}
    try:
        # url = f"{diINFO['protocol']}://{diINFO['url']}{diINFO['getCompoundsListPath']}{labINFO['labId']}/{labINFO['instrumentId']}"
        url = f"https://{diINFO['url']}{diINFO['getCompoundsListPath']}{labINFO['labId']}/{labINFO['instrumentId']}"
        responseData = requests.get(url)
        # responseData = requests.request("GET", url, headers=headers, verify=False)
        # print(url)
        responseData = responseData.text
        print(responseData)
        qcCompoundIDs = json.loads(responseData) if type(responseData) == str and len(responseData) > 0 else {}
        if "isSuccess" in qcCompoundIDs and qcCompoundIDs["isSuccess"] and "data" in qcCompoundIDs and len(qcCompoundIDs["data"]) > 0:
            tempData, qcCompoundIDs = qcCompoundIDs["data"], {}
            for item in tempData:
                qcCompoundIDs[item['COMP_NAME']] = int(item["COMP_ID"])
        else:
            print(f"Reply From Server :: {responseData}")
            logsWriter.error(f"Reply From Server :: {responseData}")
        # print(qcCompoundIDs)
        logsWriter.info(json.dumps(qcCompoundIDs))
    except Exception as ERR:
        print(f"Exception in getCompoundIDs :: {ERR}")
        logsWriter.exception(f"Exception in getCompoundIDs :: {ERR}")


def startsFunction(labInfo, deviceIsnightsInfo):
    global labINFO, diINFO, logsWriter
    try:
        labINFO, diINFO = labInfo, deviceIsnightsInfo

        # Creating logs Folder in request foles
        logRootFolder = os.path.dirname(os.path.abspath(__file__))
        Path(path.join(logRootFolder, "logs")).mkdir(exist_ok=True, parents=True)
        logsWriter = returnLogBufferObject(path.join(logRootFolder, "logs", "log_TimeStamp.txt"))


        getCompoundIDs()
        # getMethodIDs()
    except Exception as ERR:
        MessageBox(None, f"{ERR.__class__.__name__} in logBufferWriter :: {ERR}", 'Warning', 0)
    

def main():
    startsFunction(labINFO, diINFO)


# if __name__ == "__main__":
#     main()