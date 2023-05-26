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