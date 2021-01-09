import tool_json


class DB_file:
    def __init__(self, pathFile):
        self.data = {}
        self.__my_json = tool_json.My_Json()
        self.pathFile = pathFile

    def save_data_to_file(self):
        self.__my_json.dict2file(self.data, self.pathFile)

    def load_data_from_file(self):
        import os
        if not os.path.exists(self.pathFile):
            self.data = {}
        else:
            self.data = self.__my_json.file2dict(self.pathFile)

if __name__ == "__main__":
    db_file = DB_file('./dlt_db_file.txt')
    db_file.data = {"a": "A"}
    db_file.save_data_to_file()
    db_file.data = {}
    db_file.load_data_from_file()
    dlt = 0
