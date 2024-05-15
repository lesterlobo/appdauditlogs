import json
import requests
from time import strftime, localtime
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
    audit_resp = requests.get(mc.url + audit_str,
                                auth=(mc.user_at_account_name, mc.pw))
    audit_json = json.loads(audit_resp.content.decode('utf-8'))
    counter = 0

    for item in audit_json:
        print(item)
        logger.info(item)


mc = Controller()
#bus_app_dict = load_all_apps()

local_time = strftime("%Y-%m-%dT%H:%M:%S", localtime())
current_local_hour = int(strftime("%H", localtime()))
current_local_day_date = int(strftime("%d", localtime()))

x_hours_before_current_local_time = str(current_local_hour - time_interval_to_run_in_hours)
one_day_before_current_local_time = str(current_local_day_date - 1)

if x_hours_before_current_local_time == "-1":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "23"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-2":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "22"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-3":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "21"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-4":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "20"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-5":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "19"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-6":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "18"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-7":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "17"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-8":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "16"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-9":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "15"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-10":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "14"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-11":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "13"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-12":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "12"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-13":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "11"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-14":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "10"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-15":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "09"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-16":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "08"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-17":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "07"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-18":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "06"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-19":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "05"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-20":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "04"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-21":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "03"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-22":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "02"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-23":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "01"),
                                                           localtime()))
elif x_hours_before_current_local_time == "-24":
    one_hour_before_current_local_time_full = str(strftime("%Y-%m-{}T{}:%M:%S".format(one_day_before_current_local_time, "00"),
                                                           localtime()))

start = "{}.000-0700".format(one_hour_before_current_local_time_full)
end = "{}.000-0700".format(local_time)

get_audit_history(start, end)
