from nonebot import require,on_command
require("nonebot_plugin_orm")

from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="Chikari_economy",
    description="一个经济插件（库），可由其他插件调用，以便插件间的经济联动",
    usage="",
    type="library",
    homepage="https://github.com/mrqx0195/nonebot_plugin_chikari_economy",
    supported_adapters={}
)

__version__ = "0.0.7"

from .data_handles import def_money_type as def_money_type
from .data_handles import set_money as set_money
from .data_handles import add_money as add_money
from .data_handles import get_user_money as get_user_money

__all__ = (
    def_money_type,
    set_money,
    add_money,
    get_user_money,
)

from .handles import message_Handles

on_inquire_one_money = on_command(
    "Chikari_economy_inquire_one_money",
    priority=10,
    block=False,
    handlers=[message_Handles.inquire_one_money]
)

on_inquire_one_money = on_command(
    "Chikari_economy_inquire_all_money",
    priority=10,
    block=False,
    handlers=[message_Handles.inquire_all_money]
)