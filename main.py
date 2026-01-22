import requests
from datetime import datetime
import json
import os


def get_json(save_path):
    
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        data_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"rates_{data_str}.json"
        full_path = os.path.join(save_path, filename)

        with open(full_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

if __name__=='__main__':

    #Указать свой путь сохранения!!!
    SAVE_DIR = "C:\Projects\Python\professionalsCentrabank"

    get_json(SAVE_DIR)