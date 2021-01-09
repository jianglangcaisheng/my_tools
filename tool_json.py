import json

'''
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串

'''


class My_Json:
    def dict2file(self, dict_json, pathFile):
        # 将字典转换成json字符串
        str_json = json.dumps(dict_json)

        # 字典转换成json 存入本地文件
        with open(pathFile, 'w') as f:
            # 设置不转换成ascii  json字符串首缩进
            f.write(json.dumps(dict_json, ensure_ascii=False, indent=2))

    def file2dict(self, pathFile):
        with open(pathFile, 'r') as f:
            # 设置不转换成ascii  json字符串首缩进
            return json.loads(f.read())

    def open_a_file_for_append(self, pathFile):
        f = open(pathFile, 'a')
        return f

    def append_row(self, f, str_row):
        """
        不能在过程中，显示结果
        :param f:
        :param str_row:
        :return:
        """
        f.write(str_row + "\n")

    def append_row_separately(self, pathFile, str_row):
        with open(pathFile, 'a') as f:
            f.write(str_row + "\n")

    def text2object(self, text):
        data = json.loads(text)
        return data


if __name__ == "__main__":

    my_json = My_Json()
    if 0:
        dict_json = {"a": "1", "b": "2"}
        print(type(dict_json))

        my_json.dict2file(dict_json, './dlt.txt')
    if 1:
        data = my_json.file2dict("../resource/stock_code.txt")
        dlt = 0
