import hashlib
import random
import time

import requests

def generate_random_number():
    return random.randint(1000000000, 9999999999)

# REVIEW: 11 kinds of languages, write error that language code seven kinds, then less three kinds
to_languages = ['ara', 'de', 'el', 'en', 'spa', 'fra', 'jp', 'kor', 'pt', 'ru']

from_language = 'zh'

def generate_sign(appid, q, salt):
    return hashlib.md5((appid + q + str(salt) + 'g_BC4p2FRTReU93K3HqT').encode('utf-8')).hexdigest()
    

url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q=%s&from=%s&to=%s&appid=20240605002070663&salt=%s&sign=%s"

def send_get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()  # 如果响应是JSON格式的，返回解析后的数据
    else:
        return None
    

if __name__ == '__main__':
    for to in to_languages:
        # Notice: 
        #   1. Baidu translate api has call limit, so you can't call it too frequently. And ready translate text get together, then call the api.
        #   2. Using the " 119 " to split the countries, because the Baidu translate api will translated is correct. Sure, you can replace 119 with any string, the important thing is that the string before and after blank space. 
        q = '中国 119 美国 119 泰国 119 越南 119 印度尼西亚 119 马来西亚 119 阿富汗 119 阿尔巴尼亚 119 阿尔及利亚 119 美属萨摩亚 119 安道尔 119 安哥拉 119 安圭拉 119 南极洲 119 安提瓜和巴布达 119 阿根廷 119 亚美尼亚 119 阿鲁巴 119 澳大利亚 119 奥地利 119 阿塞拜疆 119 巴哈马 119 巴林 119 孟加拉国 119 巴巴多斯 119 白俄罗 119 比利时 119 伯利兹 119 贝宁 119 百慕大 119 不丹 119 玻利维亚 119 波斯尼亚和黑塞哥维那的 119 博茨瓦纳 119 布维岛 119 巴西 119 英属印度洋领土 119 文莱 119 保加利亚 119 布基纳法索 119 布隆迪 119 柬埔寨 119 喀麦隆 119 加拿大 119 开曼群岛 119 中非共和国 119 乍得 119 智利 119 圣诞岛 119 科科斯(基灵)群岛岛哥伦比亚 119 科摩罗 119 刚果民主共和国 119 刚果 119 库克群岛 119 哥斯达黎加 119 象牙海岸 119 克罗地亚 119 古巴 119 塞浦路斯 119 捷克共和国 119 丹麦 119 吉布提 119 多米尼克 119 多米尼加共和国 119 厄瓜多尔 119 埃及 119 萨尔瓦多 119 赤道几内亚 119 厄立特里亚 119 爱沙尼亚 119 斯威士兰 119 埃塞俄比亚 119 福克兰群岛 119 法罗群岛 119 斐济群岛 119 芬兰 119 法国 119 法属圭亚那 119 法属波利尼西亚 119 法国南部的领土 119 加蓬 119 冈比亚 119 格鲁吉亚 119 德国 119 加纳 119 直布罗陀 119 希腊 119 格陵兰 119 格林纳达 119 瓜德罗普岛 119 关岛 119 危地马拉 119 根西岛 119 几内亚 119 几内亚比绍 119 圭亚那 119 海地 119 赫德岛和麦克唐纳群岛 119 罗马教廷(梵蒂冈城市国家) 119 洪都拉斯 119 匈牙利 119 冰岛 119 印度 119 伊朗 119 伊拉克 119 爱尔兰 119 马恩岛 119 以色列 119 意大利 119 牙买加 119 日本 119 泽西 119 约旦 119 哈萨克斯坦 119 肯尼亚 119 基里巴斯 119 北朝鲜 119 韩国 119 科威特 119 吉尔吉斯斯坦 119 老挝 119 拉脱维亚 119 黎巴嫩 119 莱索托 119 利比里亚 119 阿拉伯利比亚众国 119 列支敦士登 119 立陶宛 119 卢森堡 119 澳 119 马达加斯加 119 马拉维 119 马尔代夫 119 马里 119 马耳他 119 马绍尔群岛 119 马提尼克岛 119 毛里塔尼亚 119 毛里求斯 119 马约特岛 119 墨西哥 119 密克罗尼西亚联邦 119 摩尔多瓦 119 摩纳哥 119 蒙古 119 黑山 119 蒙特塞拉特 119 摩洛哥 119 莫桑比克 119 缅甸 119 纳米比亚 119 瑙鲁 119 尼泊尔 119 荷兰 119 新喀里多尼亚 119 新西兰 119 尼加拉瓜 119 尼日尔 119 尼日利亚 119 纽埃 119 诺福克岛 119 北的马其顿 119 北马里亚纳群岛 119 挪威 119 阿曼 119 巴基斯坦 119 帕劳 119 巴勒斯坦 119 巴拿马 119 巴布亚新几内亚 119 巴拉圭 119 秘鲁 119 菲律宾 119 皮特凯恩 119 波兰 119 葡萄牙 119 波多黎各 119 卡塔尔 119 留尼汪 119 罗马尼亚 119 俄罗斯联邦 119 卢旺达问题 119 圣赫勒拿的 119 圣基茨和尼维斯 119 圣卢西亚 119 圣皮埃尔和密克隆群岛 119 圣文森特和格林纳丁斯 119 萨摩亚 119 圣马力诺 119 圣多美和普林西比 119 沙特阿拉伯 119 塞内加尔 119 塞尔维亚 119 塞舌尔 119 塞拉利昂 119 新加坡 119 斯洛伐克 119 斯洛文尼亚 119 所罗门岛 119 索马里的 119 南非 119 南乔治亚岛和南桑威奇群岛 119 苏丹南部 119 西班牙 119 斯里兰卡 119 苏丹 119 苏里南 119 斯瓦尔巴特群岛和扬马延岛 119 瑞典 119 瑞士 119 叙利亚 119 塔吉克斯坦 119 坦桑尼亚 119 东帝汶 119 多哥 119 托克劳 119 汤加 119 特立尼达和多巴哥 119 突尼斯 119 土耳其 119 土库曼斯坦 119 特克斯和凯凯斯群岛 119 图瓦卢 119 乌干达 119 乌克兰 119 阿拉伯联合酋长国 119 联合王国 119 乌拉圭 119 乌兹别克斯坦 119 瓦努阿图 119 委内瑞拉 119 属维尔京群岛、英国 119 属维尔京群岛、美国 119 瓦利斯群岛和富图纳群岛 119 西撒哈拉 119 也门 119 赞比亚 119 津巴布韦'
        salt = generate_random_number()
        sign = generate_sign('20240605002070663', q, salt)
        request_url = url % (q, from_language, to, str(salt), sign)
        send_get_request(request_url)
        # REVIEW: Baidu translate api has call limit, 1QPS for standard, others that supported 28 kinds languages. Current, standard supported 8 kinds languages, not supported may('马来语')、gle('爱尔兰语')、id('印尼语').
        time.sleep(1)