#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, datetime

path1 = os.path.abspath('.')  # 表示当前所处的文件夹的绝对路径
GitPath = ''
OnlinePath = ''


# 即https://github.com/你的用户名/你的项目名/raw/分支名/存放图片的文件夹/
# 或者写作https://raw.githubusercontent.com/Dawn-K/PictureBed/master/

def file_extension(path):
    return os.path.splitext(path)[1]


def makeLocal(GitPath, path, fileExten):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
    nowTimeTomin = datetime.datetime.now().strftime('%H:%M:%S')
    print('现在时间' + nowTime + ' ' + nowTimeTomin)
    newPath = GitPath + '/' + nowTime
    if os.path.isdir(newPath):
        print('今日文件夹已存在，直接保存')
    else:
        print('今日文件夹尚未存在，正在创建...')
        os.system('mkdir ' + GitPath + '/' + nowTime)
        print('创建成功')
    print('正在复制文件')
    os.system('cp ' + path + ' ' + newPath + '/' + nowTimeTomin + fileExten)
    print('复制成功')
    return nowTimeTomin + fileExten, nowTime, nowTimeTomin


def makeUpload(GitPath, nowTimeTomin):
    comment = 'add in ' + nowTimeTomin
    os.chdir(GitPath)
    os.system('git add *')
    os.system('git commit -m' + "'" + comment + "'")
    os.system('git pull && git push')


def writeLog(FinalPath, filename):
    f1 = open(GitPath + '/log.md', 'a')
    f1.write("![" + filename + "](" + FinalPath + ")\n")
    f1.close()


def main():
    # 检测是否输入路径
    if len(sys.argv) != 2:
        print('You must pass only one path')
        return
    path = sys.argv[1]
    print("输入地址为： ", path)
    # 检查文件是否存在
    if not os.path.isfile(path):
        print('该地址不存在！')
        return
    print('已检测到文件，正在上传')
    fileExten = file_extension(path)
    filename = makeLocal(GitPath, path, fileExten)
    FinalPath = OnlinePath + filename[1] + '/' + filename[2] + fileExten
    writeLog(FinalPath, filename[1] + '/' + filename[2] + fileExten)
    makeUpload(GitPath, filename[0])
    print('<============最终地址============>')
    print(FinalPath)
    print('<============================>')


if __name__ == "__main__":
    f = open('init.txt', 'r')
    GitPath = f.readline()
    GitPath = GitPath[:-1]
    OnlinePath = f.readline()
    f.close()
    main()
