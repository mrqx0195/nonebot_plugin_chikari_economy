from nonebot import require,on_command
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER
require("nonebot_plugin_localstore")

from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="Chikari_economy",
    description="一个经济插件（库），可由其他插件调用，以便插件间的经济联动",
    usage="",
    type="library",
    homepage="https://github.com/mrqx0195/nonebot_plugin_chikari_economy",
    supported_adapters={"~onebot.v11"}
)

__version__ = "0.0.3"

from .data_handles import def_money_type as def_money_type
from .data_handles import set_money as set_money
from .data_handles import add_money as add_money
from .data_handles import inquire_money as inquire_money

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