#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
version: 0.1
Author: Yayia
Date: 2021-09-27
"""
import os
import time
import random


def SayHello():
    """输出Hello world

    Returns:
    'Hello world!'
    """
    return 'Hello world!'


def NineNineTable():
    """打印九九乘法表

    Returns:
        None
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i} * {j} = {i * j}', end='\t')
        print()
    return None


def MarqueeBri():
    """创建跑马灯文字

    Returns:
        None
    """
    content = 'hello world...........'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
    return None


def generate_code(code_len=6):
    """生成指定类型、长度的验证码

    Args:
        code_len (int, optional): 选择验证码的长度. Defaults to 6.

    Returns:
        Staring/int: 生成验证码
    """
    # 包含数字和字母大小写
    # all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 包含数字和大写字母
    # all_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 仅包含数字
    all_chars = '0123456789'
    last_ops = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_ops)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    code = generate_code()
    print(code)

