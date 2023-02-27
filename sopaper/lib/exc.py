#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# File: exc.py
# Date: Wed Jul 08 22:52:49 2015 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

class RecoverableErr(Exception):
    pass

class FileCorrupted(RecoverableErr):
    pass
