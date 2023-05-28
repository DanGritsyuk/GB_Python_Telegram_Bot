import json


class SaveloadFile:

    @staticmethod
    def SaveToFile(filePath: str, data: str, rewrite = False) -> bool:
        mode='a'
        if rewrite:
            mode='w'
        with open(filePath, mode, encoding='utf8') as txtFile:
            txtFile.write(data)
        return True

    @staticmethod
    def LoadFromFile(filePath: str) -> str:
        with open(filePath, 'r', encoding='utf8') as txtFile:
            data = txtFile.read()
        return data
    
    def JsonSaveToFile(filePath: str, data: str, rewrite = False) -> bool:
        mode='a'
        if rewrite:
            mode='w'
        with open(filePath, mode, encoding='utf8') as jsonFile:
            json.dump(data, jsonFile, ensure_ascii=False)

    def JsonLoadFromFile(filePath: str) -> dict:
        splitMark = '\033[A\033[6n'
        with open(filePath, 'r', encoding='utf8') as jsonFile:
            dataList = jsonFile.read().replace('"}{"', '"}' + splitMark + '{"').split(splitMark)
            for item in dataList:
                data = json.loads(item)
                yield data
