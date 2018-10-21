# -*- coding: utf-8 -*-
import time
from datetime import datetime


def timestamp_to_strtime(timestamp, format_str="%Y-%m-%d %H:%M:%S.%f"):
    """将 13 位整数的毫秒时间戳转化成本地普通时间 (字符串格式)

    :param format_str:
    :param timestamp: 13 位整数的毫秒时间戳 (1456402864242)
    :return: 返回字符串格式 {str}'2016-02-25 20:21:04.242000'
    """
    local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime(format_str)
    return local_str_time


def timestamp_to_datetime(timestamp):
    """将 13 位整数的毫秒时间戳转化成本地普通时间 (datetime 格式)

    :param timestamp: 13 位整数的毫秒时间戳 (1456402864242)
    :return: 返回 datetime 格式 {datetime}2016-02-25 20:21:04.242000
    """
    local_dt_time = datetime.fromtimestamp(timestamp / 1000.0)
    return local_dt_time


def datetime_to_strtime(datetime_obj, format_str="%Y-%m-%d %H:%M:%S.%f"):
    """将 datetime 格式的时间 (含毫秒) 转为字符串格式

    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: {str}'2016-02-25 20:21:04.242'
    """
    local_str_time = datetime_obj.strftime(format_str)
    return local_str_time


def datetime_to_timestamp(datetime_obj):
    """将本地(local) datetime 格式的时间 (含毫秒) 转为毫秒时间戳

    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: 13 位的毫秒时间戳  1456402864242
    """
    local_timestamp = time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0
    return local_timestamp


def strtime_to_datetime(timestr, format_str="%Y-%m-%d %H:%M:%S.%f"):
    """将字符串格式的时间 (含毫秒) 转为 datetiem 格式

    # datetime. strftime (format)
    # %a 星期的简写。如 星期三为Web
    # %A 星期的全写。如 星期三为Wednesday
    # %b 月份的简写。如4月份为Apr
    # %B月份的全写。如4月份为April
    # %c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
    # %d:  日在这个月中的天数（是这个月的第几天）
    # %f:  微秒（范围[0,999999]）
    # %H:  小时（24小时制，[0, 23]）
    # %I:  小时（12小时制，[0, 11]）
    # %j:  日在年中的天数 [001,366]（是当年的第几天）
    # %m:  月份（[01,12]）
    # %M:  分钟（[00,59]）
    # %p:  AM或者PM
    # %S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
    # %U:  周在当年的周数当年的第几周），星期天作为周的第一天
    # %w:  今天在这周的天数，范围为[0, 6]，6表示星期天
    # %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
    # %x:  日期字符串（如：04/07/10）
    # %X:  时间字符串（如：10:43:39）
    # %y:  2个数字表示的年份
    # %Y:  4个数字表示的年份
    # %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
    # %Z:  时区名称（如果是本地时间，返回空字符串）
    # %%:  %% => %

    :param timestr: {str}'2016-02-25 20:21:04.242'
    :return: {datetime}2016-02-25 20:21:04.242000
    """
    local_datetime = datetime.strptime(timestr, format_str)
    return local_datetime


def strtime_to_timestamp(local_timestr):
    """将本地时间 (字符串格式，含毫秒) 转为 13 位整数的毫秒时间戳

    :param local_timestr: {str}'2016-02-25 20:21:04.242'
    :return: 1456402864242
    """
    local_datetime = strtime_to_datetime(local_timestr)
    timestamp = datetime_to_timestamp(local_datetime)
    return timestamp
