import json
import requests
from time import strftime, localtime
from datetime import datetime, timedelta
import logging
import logging.handlers as handlers


# how much data to pull back on each API call; max the API supports is 24 hours, if more than 24, no data is returned
time_interval_to_run_in_hours = 20

# Logging Config
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logHandler = handlers.RotatingFileHandler('app.log', maxBytes=5000000, backupCount=2)
logger.addHandler(logHandler)



class Controller:
    def __init__(self, host='', un='', pw='',
                 account_name='',
                 https_enabled='t', bus_app_dict=''):
        self.update(host, un, pw, account_name, https_enabled, bus_app_dict)

    def update(self, host, un, pw, account_name, https_enabled, bus_app_dict):
        self.host = host
        self.un = un
        self.pw = pw
        self.account_name = account_name
        self.user_at_account_name = self.un + "@" + self.account_name
        self.https_enabled = https_enabled
        self.bus_app_dict = bus_app_dict
        if self.https_enabled == 't':
            self.url = 'https://' + host
        elif self.https_enabled == 'f':
            self.url = 'http://' + host
        else:
            print('t or f not entered so default chosen, default - SSL=True')

    def reset(self):
        self.update('', '', '', '', '', '')


# GET
# /controller/
# ControllerAuditHistory?startTime=<start-time>&endTime=<end-time>&include=<field>:<value>&exclude=<field>:<value>
def get_audit_history(start_time, end_time, time_zone_id='', include='', exclude=''):
    audit_str = '/controller/ControllerAuditHistory?startTime={}&endTime={}'.format(start_time, end_time)
    try:
        audit_resp = requests.get(mc.url + audit_str,
                                    auth=(mc.user_at_account_name, mc.pw))
        
        if (audit_resp.ok):
            audit_json = json.loads(audit_resp.content.decode('utf-8'))
            for item in audit_json:
                logger.info(item)
            print("name=Custom Metrics|AuditLogs|Running,aggregator=OBSERVATION,value=1")
        else:
            print(audit_resp.content)
            logger.error("Error getting Audit logs from controller")
            print("name=Custom Metrics|AuditLogs|Running,aggregator=OBSERVATION,value=0")
    except:
        print("An error occurred connecting to the controller")
        logger.error("Error getting Audit logs from controller")
        print("name=Custom Metrics|AuditLogs|Running,aggregator=OBSERVATION,value=0")


mc = Controller()
last_hour_date_time = datetime.now() - timedelta(hours = time_interval_to_run_in_hours)
 
start = "{}.000-0700".format(last_hour_date_time.strftime('%Y-%m-%dT%H:%M:%S'))
end = "{}.000-0700".format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))


start = "{}.000-0700".format(start)
end = "{}.000-0700".format(end)

get_audit_history(start, end)

