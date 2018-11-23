#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    装饰器模式 (基于注解)
"""

from functools import wraps
from datetime import datetime
import time


def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print("function [%s] executes for %d seconds" % (func.__name__, (end - begin).seconds))
        return result

    return wrapper


@decorate
def func(*args, **kwargs):
    print("Do something ...")
    sec = 3
    print("Sleeping for %d seconds" % sec)
    time.sleep(sec)


if __name__ == '__main__':
    func()
