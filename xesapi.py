
#
#
#
# 版本:v1.1.7.3_221112.Full





import requests
import time

def save(name :str, xml, cookies: str, headers={}, type_='webpy',projectid=3) -> object:
    """
    保存作品
    name: 作品名
    xml: 作品内容（代码）
    cookie: COOKIE（用户凭证）
    headers: 自定义请求头
    type_: 作品类型 scratch python cpp
    projectid: 写代码的时候编辑器的id（没什么用）

    name就是新作品名 比如叫做hellopython
    xml就是代码 比如print('helloworld!')
    cookies就是用户凭证，可以去百度什么意思
    其他的没什么用

    :return: 返回请求变量
    """
    if headers == {}:
        headers = {'Cookie': cookies,
                   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"
                   }

    base = "https://code.xueersi.com/api/compilers/save"
    data = {"name": name, "xml": xml, "type": type_, "lang": type_, "id": '',
            "original_id": 3, "version": "webpy", "args": [], "planid": 'null', "problemid": '', "projectid": projectid,
            "code_complete": 1, "removed": 0, "user_id": 8510061,
            "assets": {"assets": [], "cdns": ["https://livefile.xesimg.com"], "hide_filelist": False}}
    res = requests.post(base, data=data, headers=headers)
    return res


def publish(res:str, cookies: str, headers: dict = {},description='',thumbnail="https://static0.xesimg.com/talcode/assets/py/default-python-thumbnail.png", name='NONE',tags='') -> object:
    """
    发布作品
    res: 请求变量
    name: 作品名
    description 作品描述
    thumbnail 封面链接
    不推荐使用（可能出现严重错误）：tags 作品标签

    res就是save的请求变量（如果你直接填入的话会报错）
    正确示例：
    res=save(...)
    publish(res.save,...)

    cookies就是用户凭据，不作说明
    description就是作品简介
    thumbnail就是封面图片（没有限制文件格式，但如果上传了一些奇怪的格式就显示不出来）
    name就是作品名字
    tags就是标签 以空格分界（没有限制内容，可以自定义）

    :return: 请求变量
    """
    if headers == {}:
        headers = {'Cookie': cookies,
                   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"
                   }

    res = eval(res.replace('true', "True").replace('false', "False"))
    ID = res['data']['id']
    # print(ID)
    base = "https://code.xueersi.com/api/python/%s/publish"  # 作品id
    data = {"projectId": str(ID), "name": name, "description": description, "created_source": "original",
            "hidden_code": 2, "thumbnail": thumbnail,
            "tags": tags}
    res = requests.post(base % ID, headers=headers, data=data)
    return res

def raw_publish(ID, cookies: str, headers: dict = {},thumbnail="https://static0.xesimg.com/talcode/assets/py/default-python-thumbnail.png",description='', name='NONE',tags='') -> object:
    """
    发布作品（推荐使用）
    ID:作品ID 该ID必须属于自己
    name: 作品名
    description 作品描述
    thumbnail 封面图片
    tags 作品标签

    ID就是作品id 如果你的作品列表中已经有这个作品了就能提交 即使他已经发布了
    cookies就是用户凭据，不作说明
    description就是作品简介
    thumbnail就是封面图片（没有限制文件格式，但如果上传了一些奇怪的格式就显示不出来）
    name就是作品名字
    tags就是标签 以空格分界（没有限制内容，可以自定义）

    :return: 请求变量
    """
    if headers == {}:
        headers = {'Cookie': cookies,
                   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"
                   }


    # print(ID)
    base = "https://code.xueersi.com/api/python/%s/publish"  # 作品id
    data = {"projectId": str(ID), "name": name, "description": description, "created_source": "original",
            "hidden_code": 2, "thumbnail": thumbnail,
            "tags": tags}
    res = requests.post(base % ID, headers=headers, data=data)
    return res


def cancel_publish(ID, cookies):
    """
    取消发布
    ID：要取消发布的作品ID
    cookies就是用户凭据，不作说明
    """

    data = {'params': {'id': ID}}
    headers = {'Cookie': cookies,
               'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",'cookie':cookies
               }
    res = requests.post("https://code.xueersi.com/api/python/34747602/cancel_publish", data=data, headers=headers)
    return res


def report(cookies: str, reason: str, reason_detail: int, complaint_reason_url: str, ID: int) -> object:
    """
    举报作品
    cookie:COOKIE
    reason: 理由
    reason_detail: 理由类型 1 2 3等
    complaint_reason_url: （被抄袭）源地址
    ID: 作品ID
    :return: 请求变量

    cookies就是用户凭据，不作说明
    reason就是理由 应该不用我多说了
    reason_detail举报原因
    1骗赞刷赞
    2未成年人不宜
    3人身攻击
    4抄袭他作
    5违法违规
    6垃圾广告
    7危险病毒
    8其他

    ID就是作品ID

    """
    base = "https://code.xueersi.com/api/projects/submit_complaint"
    data = {"reason": reason, "reason_detail": reason_detail, "complaint_reason_images": [],
            "complaint_reason_url": complaint_reason_url, "id": ID}

    res = requests.post(base, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
        'Cookie': cookies},
                        data=data)
    return res


def send_comment(Content: str, Cookie: str, Id_: int, UserAgent='', headers={}) -> object:
    """
    发送评论

    type_:
    1:Python（包含webpy等）
    2:Cpp
    3:Scratch
    # 严重警告： 如果不填写会导致发送失败！

    Content: 内容
    Cookie: COOKIE
    Id_: 作品id
    UserAgent: 用户代理（可不填，有默认UA）
    headers: 请求头（可不填，会默认设置）
    :return: 访问变量


    Content就是评论内容
    Cookies就是用户凭证，不多说
    Id_就是你要发评论的的目标作品id
    UserAgent就是用户代理，不多说，可以不填
    headers请求头，不多说，可以不填

    """

    if UserAgent == '':
        UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30"

    if headers == {}:
        headers = {'Cookie': Cookie,
                   'User-Agent': UserAgent
                   }

    Type=get_works_info(Id_)

    if Type == 'webpy' or Type=='python':
        Type = 'CP_'
    elif Type == 'cpp':
        Type = 'CC_'
    elif Type == 'scratch':
        Type = 'CS_'
    else:
        raise ValueError('变量Type 包含意外的值:%s 应为1、2或3' % Type)

    res = requests.post("https://code.xueersi.com/api/comments/submit",
                        headers=headers,
                        data={"appid": 1001108, 'topic_id': Type + str(Id_), 'target_id': '0', 'content': Content})
    return res


def get_works_info(ID: int) -> dict:
    """
    获取作品信息
    ID: 作品ID

    这里不需要解释了吧

    :return: dict
    """
    base = "https://code.xueersi.com/api/compilers/v2/%s" % ID
    res = requests.get(base, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'})
    f = eval(res.text.replace('null', '\'null\'').replace('true', '\'true\'').replace('false', '\'false\''))
    return f


def check_work_exists(ID) -> bool:
    """
    检查作品是否存在
    ID:作品ID

    这里不需要解释了吧

    :return: 作品是否存在（bool）是（True）否（False）
    """
    f = get_works_info(ID)
    if 'status_code' in f:
        return False
    else:
        if f['data']['published_at'] != '0000-00-00 00:00:00':
            return True
        else:
            return False


def process_works_info(Dict: dict) -> dict:
    """
    解析作品常用信息

    name: 作品名
    type: 类型（homework或normal等）
    description: 通常为简介，也有可能显示在xml项
    xml: 可能为简介
    user_id: 作者ID
    thumbnail: 封面链接
    modified_at: 最后一次修改日期
    likes: 点赞
    views: 浏览、观看数
    comments: 评论数
    deleted_at: 删除时间（通常为空）
    created_at: 创建时间
    updated_at: 提交时间
    topic_id: 待研究
    manual_weight: 是否适合继续推荐（存疑，变量名显示可能是管理员手动设置）
    popular_score: 受喜爱指数 0-1之间 越高代表越受欢迎

    Dict: get_info的返回值（或其他可分析的字典）
    :return:返回以上内容

    这个不需要解释了吧


    """
    if 'status_code' in Dict:  # 失败
        return {'stat': '0', 'msg': Dict['msg']}

    _output = {
        "name": Dict['data']['name'],
        'type': Dict['data']['type'],
        'description': Dict['data']['description'],
        'xml': Dict['data']['xml'],
        'user_id': Dict['data']['user_id'],
        'thumbnail': Dict['data']['thumbnail'],
        'modified_at': Dict['data']['modified_at'],
        'likes': Dict['data']['likes'],
        'views': Dict['data']['views'],
        'comments': Dict['data']['comments'],
        'deleted_at': Dict['data']['deleted_at'],
        'created_at': Dict['data']['created_at'],
        'updated_at': Dict['data']['updated_at'],
        'topic_id': Dict['data']['topic_id'],
        'manual_weight': Dict['data']['manual_weight'],
        'popular_score': Dict['data']['popular_score']
    }
    return _output


def get_user_info(user_id, cookie='') -> dict:
    """
    获取用户信息

    user_id 用户id

    已知信息：
    fans 粉丝数量
    follows 关注数量
    is_my 是我自己（bool）
    realname 真名
    signature 个性签名
    disabled 封禁
    avatar_path 头像链接
    is_follows 我已关注

    已经很明白了，不解释

    :return:
    """
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33','cookie':cookie
    }
    if cookie != '':
        _output = requests.get('https://code.xueersi.com/api/space/profile?user_id=%s' % user_id, headers=headers)
    else:
        _output = requests.get('https://code.xueersi.com/api/space/profile?user_id=%s' % user_id, headers=headers)
    _output = eval(_output.text.replace('true', 'True').replace('false', 'False'))
    return _output


def get_user_page_info(user_id) -> dict:
    """
    首页信息
    https://code.xueersi.com/api/space/index?user_id=?

    已知信息：（data下）
    overview 我的成就
    fans 粉丝列表
    favorites 收藏列表
    follows 关注列表
    representative_work 代表作信息
    works 作品列表

    这个没什么用，不做说明

    协议 GET
    :param user_id: 用户id
    :return: 输出以上
    """
    _output = requests.get('https://code.xueersi.com/api/space/index?user_id=%s' % user_id)
    _output = eval(_output.text.replace('true', 'True').replace('false', 'False'))
    return _output


def get_msg_overview(cookie: str, headers={}) -> dict:
    """
    获取用户消息提示（必须登录）
    :param cookie: COOKIE
    :return: 返回值

    示例返回值：
    {"stat":1,"status":1,"msg":"\u64cd\u4f5c\u6210\u529f","data":[{"category":1,"text":"\u8bc4\u8bba\u548c\u56de\u590d","count":0},{"category":2,"text":"\u70b9\u8d5e\u4e0e\u6536\u85cf","count":0},{"category":5,"text":"\u5173\u6ce8","count":0},{"category":3,"text":"\u53cd\u9988\u548c\u5ba1\u6838","count":0},{"category":4,"text":"\u7cfb\u7edf\u6d88\u606f","count":0}]}
    category 1 评论与回复
    category 2 点赞与收藏
    category 5 关注
    category 3 反馈和审核
    category 4系统消息

    count为消息数量

    """
    base = "https://code.xueersi.com/api/messages/overview"
    if headers == {}:
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
            'cookie':cookie
        }
    res = requests.get(base, headers=headers)
    res = eval(res.text)
    return res


def get_comments(ID,page=1) -> dict:
    """
    获取评论信息
    ID 作品ID
    page 页数

    这个要讲的话有点麻烦，有时间写一下

    :return:
    """
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'
    }
    base = "https://code.xueersi.com/api/comments?appid=1001108&topic_id=%s&parent_id=0&order_type=&page=%s&per_page=15"
    topic_id = process_works_info(get_works_info(ID))['topic_id']
    res = requests.get(base % (topic_id,page), headers=headers)
    res = res.text.replace('null', '\'null\'').replace('false', 'False').replace('true', 'True')
    return eval(res)


def process_comments(Dict: dict, mode=1):
    """
    获取评论信息
    :param res:get_comments的返回值或其他可处理内容
    :param mode:模式
    :return:

    page:页数
    per_page: 每页多少评论
    total: 评论总数
    ------------------------
    mode
    1 不对任何信息进行处理，仅获取常用信息
    2 仅输出所有评论的信息（包含评论内容）
    3 仅输出所有评论文本
    ------------------------


    can_delete: 是否可以删除 bool
    can_top: 是否为置顶 bool
    comment_from: 评论来源（待分析） str
    content: 评论文本 str
    created_at: 发送时间 str
    emojis: 使用的emoji列表 list
    id: 可能是评论的ID，待分析 int
    is_like: 已登录用户是否点赞 bool
    is_topic_author_like: 作者是否点赞 bool
    is_topic_author_reply: 作者是否回复过 bool
    is_unlike: 已登录用户是否踩过 bool
    likes: 点赞数 int
    links: 评论发布者发送的链接 list
    parent_id: 未知，待分析 int
    removed: 未知，待分析 int
    replies: 回复数量 int
    reply_list: 回复列表 list
    data: 未知，待分析 list
    hasMore: 未知，待分析 bool
    total: 未知，待分析 int
    reply_user_id: 回复作品作者id str
    reply_username: 回复作品作者名
    target_id: 待分析 int
    top: 是否为置顶（是为1 否为0） int
    topic_id: 作品的topicid str
    unlikes: 踩过人数
    user_avatar_path: 评论发布者头像地址 str
    user_id: 发布者uid str

    """

    if mode not in [1, 2, 3]:
        raise ValueError('意外的值:%s' % mode)

    def mode_1(Dict):
        _output = {
            'page': Dict['data']['page'],  # 页数
            'per_page': Dict['data']['per_page'],  # 未知
            'total': Dict['data']['total'],  # 评论总数
            'comments': Dict['data']['data']

        }
        return _output

    def mode_2(Dict):
        return Dict['data']['data']

    def mode_3(Dict):
        _output = []
        for i in Dict['data']['data']:
            _output.append(i['content'])
        return _output

    return eval('mode_%s(Dict)' % mode)


def delete_comment(comment_id: int, ID: int, cookie: str) -> dict:
    """
    删除评论
    :param comment_id: 评论id（在get_comments中获得）
    :param ID: 作品id
    :param cookie: cookie
    :return:
    """
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
        'Cookie':cookie
    }
    data = {
        'appid': 1001108,
        'topic_id': process(get_info(ID)),
        'id': comment_id
    }
    res = requests.post("https://code.xueersi.com/api/comments/delete", headers=headers, data=data)
    return eval(res.text)


def follow(follow_user_id: int, cookies: str) -> dict:
    """
    关注用户
    :param follow_user_id:用户ID
    :param cookies:用户凭证
    这个不多说
    :return:
    """
    data = {'followed_user_id': str(follow_user_id), 'state': 1}
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
        'Cookie':cookies
    }
    res = requests.post('https://code.xueersi.com/api/space/follow', data=data, headers=headers)
    return eval(res.text)


def like(cookies: str, ID: int):
    """
    点赞某作品
    :param cookies: 用户凭证
    :param ID: 作品id
    :return: 访问变量 没什么用
    """
    "https://code.xueersi.com/api/python/34748790/like"
    data = {'params': {'id': ID, 'lang': 'code', 'form': get_works_info(ID)['data']['lang']}}
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
        'Cookie':cookies
    }
    res = requests.post("https://code.xueersi.com/api/python/%s/like" % ID, headers=headers, data=data)
    return res


def unlike(cookies: str, ID: int):
    """
    踩某作品
    :param cookies: 用户凭证
    :param ID: 作品ID
    :return:
    """
    "https://code.xueersi.com/api/python/34748790/unlike"
    data = {'params': {'id': ID, 'lang': 'code', 'form': get_works_info(ID)['data']['lang']}}
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
        'Cookie':cookies
    }
    res = requests.post("https://code.xueersi.com/api/python/%s/unlike" % ID, headers=headers,
                        data=data)
    return res


def edit_signature(cookies: str, word: str):
    """
    更改个性签名（不限长度）
    cookies:用户登录凭证
    word:目标内容

    return 请求变量
    """
    path = "https://code.xueersi.com/api/space/edit_signature"
    data = {"signature": word}
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
        'Cookie':cookies
    }
    res = requests.post(path, data=data, headers=headers)
    return res


def get_cookies(sleep_time=20):
    """
    获取cookies
    #需在目录下放置edgedriver.exe
    #否则会报错

    :return: str cookies
    """

    driver = webdriver.Edge('%s\\msedgedriver.exe' % os.path.dirname(os.path.realpath(sys.argv[0])))
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""
    })
    url = "http://login.xueersi.com"
    driver.get(url)
    time.sleep(sleep_time)
    # 获取cookie列表
    cookie_list = driver.get_cookies()
    # 格式化打印cookie
    cookie_list = [item["name"] + "=" + item["value"] for item in cookie_list]

    cookiestr = ';'.join(item for item in cookie_list)

    self.cookies = cookiestr
    return cookiestr


def get_danger_info(ID):
    """
    获得作品警告信息

    https://code.xueersi.com/api/compilers/danger_level?id=38568188


    返回示例：
    {stat: 1, status: 1, msg: "操作成功", data: {result: null}}
    {stat: 1, status: 1, msg: "操作成功", data: {result: {level: "warning", tips: "该作品可能会获取您的cookie信息，请谨慎运行"}}}
    :param ID:
    :return:
    """
    res=requests.get("https://code.xueersi.com/api/compilers/danger_level?id=%s"%ID)
    res = res.text.replace('null', '\'null\'').replace('false', 'False').replace('true', 'True')
    return res

