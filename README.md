<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-chikari-economy

_✨ NoneBot 经济插件（库） ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-chikari-economy.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-chikari-economy">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-chikari-economy.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

一个经济插件（库），可由其他插件调用，以便插件间的经济联动

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-chikari-economy

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-chikari-economy
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-chikari-economy
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-chikari-economy
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-chikari-economy
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_chikari_economy"]

</details>


## 🎉 使用
### 开发者

你可以通过以下方法使用本插件的功能

`import nonebot_plugin_chikari_economy`

#### def_money_type
```
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
```
#### set_money
```
def set_money(uid: str,id: str,value: float):
    """设置用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id
        value (float): 货币要设置成的值

    Returns:
        float: 货币设置后的值
    """
```
#### add_money
```
def add_money(uid: str,id: str,value: float):
    """增加（或减少）用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id
        value (float): 货币要增加（负数为减少）的值

    Returns:
        float: 货币增加（或减少）后的值
    """
```
#### inquire_money
```
def inquire_money(uid: str,id: str):
    """查询用户的某种货币数量

    Args:
        uid (str): 用户id
        id (str): 货币id

    Returns:
        float: 货币当前数量
    """
```

### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| Chikari_economy_inquire_one_money | 群员 | 否 | 群聊 | 内置的单种货币查询指令，一般不建议使用 |
| Chikari_economy_inquire_all_money | 群员 | 否 | 群聊 | 内置的所有货币查询指令，一般不建议使用 |
