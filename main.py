#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2016 - yangxiang <yangxiang92@163.com>

import regex
import getopt
import sys

# ===============================================================
# 获取命令行输入的参数
# ===============================================================
def getOpt():
    opts,args = getopt.getopt(sys.argv[1:], "i:o:h");

    in_file = '';
    out_file = '';

    for op,value in opts:
        if op == '-i':
            in_file = value;
        elif op == '-o':
            out_file = value;
        else:
            print("Plese input the right parameters:");
            print("    -i  Set the input file.");
            print("    -o  Set the output file to store the results.(not necessary)");
            print("    -h  Show the help menu.")
            sys.exit();

    if len(in_file) == 0:
        print("Please set the input file with parameter -i.");
        sys.exit();

    return in_file, out_file;

# ===============================================================
# 利用正则表达式获取要求的字符串
# ===============================================================
def findFloat(text_content):
    ret_list = [];
    re_result = regex.findall(r'(?<![-+\d\.]+)([-+]?\d+)(\.\d+)(?![\.\d])', text_content);
    for c in re_result:
        ret_list.append(c[0]+c[1]);
    return ret_list;

# ===============================================================
# 主程序
# ===============================================================
if __name__ == "__main__":
    in_file, out_file = getOpt();

    # 打开输入文件
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as f:
        text_content = f.read();

    # 解析文件内容中符合要求的浮点数字符串
    float_str_list = findFloat(text_content);

    # 输出匹配结果
    for float_str in float_str_list:
        print(float_str);

    # 保存匹配结果到输出文件中去
    if len(out_file) != 0:
        with open(out_file, 'w') as f:
            for float_str in float_str_list:
                f.write(float_str+'\n\r');

