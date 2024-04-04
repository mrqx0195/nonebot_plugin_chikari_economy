from nonebot.adapters.onebot.v11 import GroupMessageEvent,Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg

from . import data_handles

class message_Handles():
    """消息处理
    """
    async def inquire_one_money(
            matcher: Matcher,event: GroupMessageEvent,args: Message = CommandArg()
    ):
        """内置的单种货币查询指令，一般不建议使用
        """
        command: str = args.extract_plain_text()
        uid: str = event.get_user_id()
        s = f"{uid}的{command}量："
        try:
            s += data_handles.inquire_money(command)
        except NameError:
            s = "未注册的货币类型！"
        await matcher.finish(s)
        
    async def inquire_all_money(
            matcher: Matcher,event: GroupMessageEvent,args: Message = CommandArg()
    ):
        """内置的所有货币查询指令，一般不建议使用
        """
        uid: str = event.get_user_id()
        s = f"{uid}的所有货币量："
        for i in data_handles.configdata["money_types"].keys:
            s += "\n" + data_handles.inquire_money(i)
        await matcher.finish(s)
        