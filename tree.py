import os
import mimetypes

# files = os.listdir("./")

# file一覧出力 再帰関数
def output_files(file_path):
    # TODO /のチェックと調整

    # ファイル一覧を取得
    files = os.listdir(file_path)
    
    # ファイル一覧でループ
    for file_name in files:
        # pathを取得
        child_file_path = file_path + '/' + file_name

        # ファイル・タイプを取得
        # file_type = mimetypes.guess_type(file_path)
        # print(file_type)

        # ディレクトリかどうか
        if is_dir(child_file_path):
            # ディレクトリの場合は再帰
            output_files(child_file_path)
        else:
            # 通常ファイルの場合
            print('node: ' + file_path)
            print(file_name)
            print(child_file_path)
            print('-')

def is_dir(file_path):
    return os.path.isdir(file_path)

output_files(".")
