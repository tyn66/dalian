from dlpc.utils import post,get
from dlpc.utils import CarTypedata
import re,json
# b = {"requestType": "wei502_checkcarinfo", "para": {"CarType": "02", "CarNum": "辽B72XF2", "CarCode": "9397"}}
def dalianpachong(CarType,CarNum,CarCode):
    try:
        CarType1 = CarTypedata[CarType]
        CarNum1 = CarNum[1:]
        # print(CarType1)
        # CarNum = "B72XF2"
        # CarCode = "9397"
        url = 'http://weixin.dlutc.gov.cn/weixin_trunk/WeiXin/wei501.php?openid=oA2-lv6lIvhvzEn2YIISY_K14_cs&cartype=' + CarType1 + '&carnum=%E8%BE%BD' + CarNum1 + '&carcode=' + CarCode
        print(url)
        a = get(url)
        if a["code"] == 0:
            a = get(url)
        # print(a["data"].decode())
        b = a["data"].decode().replace('\n', '').replace('\t', '').replace('\r', '')
        c = re.findall('<font color="#FF9900">(.*?)</font>  笔',b)
        L = []
        if int(c[0]) != 0 :
            d = re.findall('class="weui_cell_bd weui_cell_primary.*?<p>(.*?)</p>.*?扣(.*?)</p>.*?罚款金额.*?<p>¥(.*?)</p>.*?违法地点：(.*?)</p>.*?违法行为(.*?)</p>',b)
            print(d)
            for i in d:
                dict = {}
                dict["cph"] = CarNum  # 车牌号
                dict["youwuwz"] = "有违章记录"
                dict["jffakuan"] = "罚款%s元扣%s" % (i[2], i[1])  # 扣几分罚多少钱
                dict["time1"] = i[0]  # 违章时间
                dict["site"] = i[3]  # 违章地址
                dict["miaoshu"] = i[4]  # 违章描述
                L.append(dict)
            jsonL = {
                "code": 1,
                "msg": "查询成功",
                "data": L,
            }
            return json.dumps(jsonL, ensure_ascii=False)
        else:
            dict = {}
            dict["cph"] = CarNum
            dict["youwuwz"] = "暂无违章记录"
            L.append(dict)
            jsonL = {
                "code": 1,
                "msg": "查询成功",
                "data": L,
            }
            return json.dumps(jsonL, ensure_ascii=False)
    except Exception as e:
        jsonL = {
            "code": 0,
            "msg": "服务器错误",
        }
        return json.dumps(jsonL, ensure_ascii=False)
# if __name__ == '__main__':
#
#     print(dalianpachong(CarType,CarNum,CarCode))