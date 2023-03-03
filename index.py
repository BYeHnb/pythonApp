// 指定cpu使用率，与内存占用率
# -*- coding: utf-8 -*-
import psutil
import time
import os
import sys
import json
import requests
import datetime
import logging
import logging.handlers
import configparser
import threading
import socket
import re
import subprocess
import platform
import random
import string
import base64
import hashlib
import urllib
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import gzip
import io
import ssl

# 读取配置文件
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

if __name__ == '__main__':
    # 读取配置文件

