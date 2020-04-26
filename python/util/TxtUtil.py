class TxtUtil:
    @staticmethod
    def readTxt(txt_path):
        file = open(txt_path, 'r', encoding='utf-8')
        return file.readlines()

    @staticmethod
    def writeTxt(txt_path, content):
        file = open(txt_path, 'w', encoding='utf-8')
        for var in content:
            file.writelines(var)
            file.write("\n")
