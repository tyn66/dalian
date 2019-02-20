import requests

#todo  封装后的requests的get与post方法
#http是无状态的，封装的方法仅用于一次请求，无法保存cookie
def get(url, params=None, headers=None, cookies=None, proxies=None, verfiy=None, timeout=20):
    '''
    此方法用于get请求
    :param url: url地址
    :param params: ？&符号后面的参数，说白，url路由参数
    :param headers: 请求头信息
    :param cookies: 请求的cookie
    :param proxies: 请求的代理ip
    :param verfiy: 请求时是否认证https
    :param timeout: 请求网络超时
    :return:
    '''
    s = requests.session()
    ret = {}
    ret["code"] = 0
    try:
        if params != None:
            s.params = params
        if headers != None:
            s.headers = headers
        if cookies != None:
            s.cookies = cookies
        if verfiy != None:
            s.verfiy = verfiy
        if proxies != None:
            s.proxies = proxies
        r = s.get(url=url, timeout=timeout)
        if r != None:
            ret["code"] = 1
            ret["data"] = r.content
            return ret
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()
    return ret


def post(url, data, params=None, headers=None, cookies=None, proxies=None, verfiy=None, timeout=20):
    s = requests.session()
    ret = {}
    ret["code"] = 0
    try:
        if params != None:
            s.params = params
        if headers != None:
            s.headers = headers
        if cookies != None:
            s.cookies = cookies
        if verfiy != None:
            s.verfiy = verfiy
        if proxies != None:
            s.proxies = proxies

        r = s.post(url=url, data=data, timeout=timeout)
        if r != None:
            ret["code"] = 1
            ret["data"] = r.content
            return ret
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()
    return ret

CarTypedata = {
    '大型汽车':'01',
    '小型汽车':'02',
    '使馆汽车':'03',
    '领馆汽车':'04',
    '境外汽车':'05',
    '外籍汽车':'06',
    '两、三轮摩托车':'07',
    '境外摩托车':'11',
    '外籍摩托车':'12',
    '农用运输车':'13',
    '拖拉机':'14',
    '挂车':'15',
    '教练汽车':'16',
    '教练摩托车':'17',
    '试验汽车':'18',
    '试验摩托车':'19',
    '临时入境汽车':'20',
    '临时入境摩托车':'21',
    '临时行驶车':'22',
    '警用汽车':'23',
    '警用摩托':'24',
}