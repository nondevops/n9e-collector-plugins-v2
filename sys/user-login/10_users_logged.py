#!/usr/bin/env python
# -*- coding: utf-8 -*-

#V1.0 Description：用户登录数监控

import os
import time
import json
import commands
import platform
import sys
import logging
import socket

data = []
step = int(os.path.basename(sys.argv[0]).split("_", 1)[0])
plugins_log_dirs = '/opt/n9e-collector/logs/plugin/'
if not os.path.exists(plugins_log_dirs):
    os.makedirs(plugins_log_dirs)

logging.basicConfig(level=logging.ERROR,  
                    filename='/opt/n9e-collector/logs/plugin/error.log',  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def get_ip_address(key):
    if key=='ip':
        return socket.gethostbyname(socket.gethostname())
    elif key=='hostname':
        return socket.gethostname()
    elif key=='endpoint':
        endpoint = commands.getoutput('''ifconfig `route|grep '^default'|awk '{print $NF}'`|grep inet|awk '{print $2}'|awk -F ':' '{print $NF}'|head -n 1 ''')
        return endpoint

try:
    value = int(commands.getoutput("/usr/bin/last | grep 'logged' | grep -v 'grep' | wc -l").strip())
except Exception,err:
    logging.error("Run command failed:%s" %str(err))
    sys.exit(2)
def create_record():
    record = {}
    record['metric'] = 'sys.users.logged'
    record['endpoint'] = get_ip_address('endpoint')
    record['timestamp'] = int(time.time())
    record['step'] = step
    record['value'] = value
    record['counterType'] = 'GAUGE'
    record['tags'] = ''
    data.append(record)
create_record()
if data:
   print json.dumps(data)
