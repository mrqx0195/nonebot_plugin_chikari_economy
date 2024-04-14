from ast import literal_eval

from nonebot_plugin_orm import Model,async_scoped_session,get_session
from sqlalchemy.orm import Mapped, mapped_column

class Data(Model):
    uid: Mapped[str] = mapped_column(primary_key=True)
    money: Mapped[str] = "{}"
    
class ConfigData(Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = "Unnamed money"
    description: Mapped[str] = "Unnamed money"

async def get_money_dict(uid: str) -> dict:
    """获取用户的货币字典

    Args:
        uid (str): 用户id

    Returns:
        dict: 用户的货币字典
    """
    
    session = get_session()
    async with session.begin():
        dat = await session.get(Data, uid)
        if not dat:
            dat = Data(uid = uid,money = str({"defaultmoney": 0.0}))
            session.add(dat)
        return literal_eval(dat.money)
    
async def get_money_config(id: str) -> tuple:
    """获取货币的信息

    Args:
        id (str): 货币的id

    Returns:
        tuple: 货币的信息，应当为(name, description)
    """
    
    session = get_session()
    async with session.begin():
        con = await session.get(ConfigData, id)
        if not con:
            raise NameError(f"Undefined money type:{id}")
        return (con.name, con.description)
    
async def get_user_money(uid: str,id: str) -> float:
    """获取用户的单种货币

    Args:
        uid (str): 用户id

    Returns:
        float: 这种货币的量
    """
    
    d = get_money_dict(uid)
    if id not in d.keys and get_money_config(id):
        return 0.0
    return d[id]

async def def_money_type(id: str,name: str = "Unnamed money",description: str = "Unnamed money") -> tuple:
    """定义一种新的货币种类
    
    不使用此方法定义货币直接使用可能会出现错误
    
    id相同时，新的定义会覆盖旧的定义，但已有的货币量不变

    Args:
        id (str): 货币的id，不同的id会视为不同的货币
        name (str): 货币的名字
        description (str): 货币的描述

    Returns:
        tuple: 一个二元组，应当为(name, description)
    """
    
    session = get_session()
    async with session.begin():
        con = await session.get(ConfigData, id)
        con = ConfigData(id = id,name = name,description = description)
        session.add(con)
        return (con.name, con.description)

async def set_money(uid: str,id: str,value: float) -> None:
    """设置用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id
        value (float): 货币要设置成的值
    """
    
    session = get_session()
    async with session.begin():
        dat = await session.get(Data, uid)
        if not dat and get_money_config(id):
            dat = Data(uid = uid,money = str({"defaultmoney": 0.0,id: value}))
        else:
            dat = Data(uid = uid,money = str(get_money_dict(uid).update({id: value})))
        session.add(dat)
    return 

def add_money(uid: str,id: str,value: float) -> float:
    """增加（或减少）用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id
        value (float): 货币要增加（负数为减少）的值

    Returns:
        float: 货币增加（或减少）后的值
    """
    
    set_money(uid,id,get_user_money(uid,id) + value)
    return get_user_money(uid,id)
