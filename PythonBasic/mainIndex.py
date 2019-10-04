import sys
from os import path
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

from overrideModules.jsonModules import getJsonObject as getJO
from requests_module import deviceInsights_requests



def resource_path(relative_path):
    try: base_path = sys._MEIPASS    # PyInstaller creates a temp folder and stores path in _MEIPASS
    except Exception: base_path = path.dirname(path.abspath(__file__))
    return path.join(base_path, relative_path)


def main():
    try:
        print("Execution Starts Here.")
        deviceName = 'deviceInsights_requests'

        labInfoPath = resource_path('config\\labInfo.json')
        deviceInsightsPath = resource_path('config\\deviceInsights_info.json')
        
        sys.path.insert(0, resource_path('requests_module\\'))
        driver = __import__(('{}'.format(deviceName)), globals(), locals(), ['startsFunction'], 0)
        driver.startsFunction(getJO(labInfoPath), getJO(deviceInsightsPath))

        print("Execution Ends Here.")
    except Exception as ERR:
        MessageBox(None, f"{ERR.__class__.__name__} in logBufferWriter :: {ERR}", 'Warning', 0)
    

# main()
if __name__ == "__main__":
    main()
