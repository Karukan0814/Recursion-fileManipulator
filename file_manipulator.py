import os


# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
def reverseFile(inputpath, outputpath):
    if not os.path.isfile(inputpath):
        raise ValueError("入力ファイルなし" + inputpath)
    if not os.access(inputpath, os.R_OK):
        raise PermissionError("入力ファイルが読み取り不可" + inputpath)

    if not os.path.isdir(outputpath):
        raise ValueError("出力ディレクトリなし" + outputpath)
    if not os.access(outputpath, os.W_OK):
        raise PermissionError("出力ディレクトリ書き込み不可" + outputpath)

    contents = ""

    with open(inputpath, "r", encoding="utf-8") as f:
        contents = f.read()

    # outputpathにファイルを作成
    with open(outputpath + "/reverseFile_output", "w") as f:
        f.write(contents[::-1])


# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
import shutil


def copyFile(inputpath, outputpath):
    if not os.path.isfile(inputpath):
        raise ValueError("入力ファイルなし" + inputpath)
    if not os.access(inputpath, os.R_OK):
        raise PermissionError("入力ファイルが読み取り不可" + inputpath)

    if not os.path.isdir(outputpath):
        raise ValueError("出力ディレクトリなし" + outputpath)
    if not os.access(outputpath, os.W_OK):
        raise PermissionError("出力ディレクトリ書き込み不可" + outputpath)

    destination_path = outputpath + "/copyFileOutput.txt"

    # ファイルをコピー
    shutil.copy(inputpath, destination_path)


# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
def duplicateContents(inputpath, n):
    if not os.path.isfile(inputpath):
        raise ValueError("入力ファイルなし" + inputpath)
    if not os.access(inputpath, os.R_OK):
        raise PermissionError("入力ファイルが読み取り不可" + inputpath)
    if not os.access(inputpath, os.W_OK):
        raise PermissionError("入力ファイル書き込み不可" + inputpath)

    if not isinstance(n, (int)):
        raise ValueError("繰り返しの回数はintで入力" + str(n))

    original = ""
    # outputpathにファイルを作成
    with open(inputpath) as f:
        original = f.read()
    content = ""
    for _ in range(n):
        content += original

    with open(inputpath, "w") as f:
        f.write(content)


# replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
def replaceString(inputpath, newstring):
    if not os.path.isfile(inputpath):
        raise ValueError("入力ファイルなし" + inputpath)
    if not os.access(inputpath, os.X_OK):
        raise PermissionError("入力ファイルが読み取り不可" + inputpath)
    if not os.access(inputpath, os.W_OK):
        raise PermissionError("入力ファイル書き込み不可" + inputpath)

    if not isinstance(newstring, (str)):
        raise ValueError("新たな文字列はstrで")

    search_string = "needle"
    original = ""
    # outputpathにファイルを作成
    with open(inputpath) as f:
        original = f.read()
    content = original.replace(search_string, newstring)

    with open(inputpath, "w") as f:
        f.write(content)


# 以下、テストコード
reverseFile("test.txt", "output")
copyFile("test.txt", "output")
duplicateContents("test.txt", 5)
replaceString("test.txt", "needle1needle2needle3")
