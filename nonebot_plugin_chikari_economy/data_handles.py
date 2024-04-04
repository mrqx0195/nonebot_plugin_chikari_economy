import json
import os

from pathlib import Path
import nonebot_plugin_localstore as store

plugin_data_file: Path = store.get_data_file("chikari_economy", "data.json")
plugin_config_file: Path = store.get_config_file("chikari_economy", "config.json")

#用户数据文件初始化及载入

if not os.path.exists(plugin_data_file):
    f = open(plugin_data_file,'w')
    f.close
with open(plugin_data_file,encoding='utf-8')as datafile:
    datastr = datafile.read()
    if not os.path.exists(plugin_data_file) or not datastr:
        f = open(plugin_data_file,'w')
        init_data = {
            
        }
        json.dump(init_data,f,indent=4)
        f.close
        data = init_data
    else:
        data = json.loads(datastr,strict=False)
        
#配置数据文件初始化及载入

if not os.path.exists(plugin_config_file):
    f = open(plugin_config_file,'w')
    f.close
with open(plugin_config_file,encoding='utf-8')as configfile:
    configstr = configfile.read()
    if not os.path.exists(plugin_config_file) or not configstr:
        f = open(plugin_config_file,'w')
        init_data = {
            "money_types":{"defaultmoney":("Chikari币","Chikari_economy提供的默认钱币")}
        }
        json.dump(init_data,f,indent=4)
        f.close
        configdata = init_data
    else:
        configdata = json.loads(configstr,strict=False)

def file_save():
    """将内存中的数据保存至文件
    """
    
    global data
    global configdata
    f = open(plugin_data_file,'w')
    json.dump(data,f,indent=4)
    f.close
    f = open(plugin_config_file,'w')
    json.dump(configdata,f,indent=4)
    f.close

def data_set(uid: str,key: str,value):
    """设置特定用户的特定数值

    Args:
        uid (str): 用户id
        key (str): 数据键值
        value (_type_): 数据
    """
    
    global data
    if uid not in data.keys:
        data[uid] = {key: value}
    else:
        data[uid][key] = value
    file_save()
    return

def configdata_set(key: str,value):
    """设置配置文件

    Args:
        key (str): 配置键值
        value (_type_): 数据
    """
    
    global configdata
    configdata[key] = value
    file_save()
    return

def def_money_type(id: str,name: str,description: str):
    """定义一种新的货币种类
    
    不使用此方法定义货币直接使用可能会出现意料之外的错误
    
    id相同时，新的定义会覆盖旧的定义，但已有的货币量不变

    Args:
        id (str): 货币的id，不同的id会视为不同的货币
        name (str): 货币的名字
        description (str): 货币的描述

    Returns:
        tuple: 一个二元组，应当为(name, description)
    """
    global configdata
    configdata_set(id,(name, description))
    return configdata["money_types"][id]

def set_money(uid: str,id: str,value: float):
    """设置用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id
        value (float): 货币要设置成的值

    Returns:
        float: 货币设置后的值
    """
    global data,configdata
    if id not in configdata["money_types"].keys:
        raise NameError(f"Undefined money type:{id}")
    data_set(uid,id,float(value))
    return data[uid][id]

def add_money(uid: str,id: str,value: float):
    """增加（或减少）用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id
        value (float): 货币要增加（负数为减少）的值

    Returns:
        float: 货币增加（或减少）后的值
    """
    global data
    if id not in configdata["money_types"].keys:
        raise NameError(f"Undefined money type:{id}")
    set_money(uid,id,data[uid][id] + value)
    return data[uid][id]

def inquire_money(uid: str,id: str):
    """查询用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id

    Returns:
        float: 货币当前数量
    """
    global data
    if id not in configdata["money_types"].keys:
        raise NameError(f"Undefined money type:{id}")
    if id not in data[uid]:
        return 0
    return data[uid][id]