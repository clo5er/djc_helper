from sys import exit

from util import message_box, uin2qq


class BlackListInfo:
    def __init__(self, ban_at, qq, nickname, reason):
        self.ban_at = ban_at
        self.qq = qq
        self.nickname = nickname
        self.reason = reason

    def __str__(self):
        return f"{self.qq}({self.nickname})在{self.ban_at}因[{self.reason}]被本工具拉入黑名单"


black_list = {
    "823985815": BlackListInfo("2021-01-05", "823985815", "章鱼宝宝。", "伸手党，不看提示直接开问"),
    "1531659746": BlackListInfo("2021-01-20", "1531659746", "北望", "别人图氛围说继续发红包时，骂别人网络乞丐，然后被踢后，加我说我是傻逼罢了"),
    "262163207": BlackListInfo("2021-01-31", "262163207", "孤独患者", "说了不要问我疲劳药怎么设置，也看到注释的内容了，还要问，还说我优越感很强。既然合不来，就再见吧。"),
    "69512151": BlackListInfo("2021-02-22", "69512151", "不知道是谁", "做坏事，永久拉黑"),
    "642364310": BlackListInfo("2021-02-22", "642364310", "不知道是谁", "做坏事，永久拉黑"),
    "39752616": BlackListInfo("2021-02-22", "39752616", "不知道是谁", "做坏事，永久拉黑"),
    "4838116": BlackListInfo("2021-04-03", "4838116", "玉簪子", "不可理喻"),
    "1832447846": BlackListInfo("2021-04-17", "1832447846", "欧皇", "在半夜修完bug通知群友修好了的时候，跑出来一句：大晚上的@nm的全体啊"),
    "410639497": BlackListInfo("2021-06-11", "410639497", "一人一世界", "看不懂中文，提示写的明明白白了，让他绑定道聚城，还要问个不停"),
    "931394485": BlackListInfo("2021-08-02", "931394485", "将夜", "说卡丢了，回复应该没有这种问题，如果真怀疑是小助手的问题，可以退款停止使用，最后骂我是 麻痹脑残"),
}


def check_in_black_list(uin):
    qq = uin2qq(uin)
    if qq in black_list:
        message = (
            "发现你的QQ在本工具的黑名单里，本工具禁止你使用，将在本窗口消失后退出运行。\n"
            "黑名单相关信息如下：\n"
            f"{black_list[qq]}"
        )
        message_box(message, "禁止使用")
        exit(0)


if __name__ == '__main__':
    check_in_black_list("o823985815")
