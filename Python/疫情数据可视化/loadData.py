import requests

def loadData():
    print("loading data......")

    # 获取网页数据
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    res = requests.get(url, headers=headers).json()
    response_data = res['data']

    # 世界各国
    # chinaTotal = response_data['chinaTotal']
    # chinaDayList = response_data['chinaDayList']
    # lastUpdateTime = response_data['lastUpdateTime']
    # overseaLastUpdateTime = response_data['overseaLastUpdateTime']
    areaTree = response_data['areaTree']

    # 中国
    n = len(areaTree)
    i = 0
    while i < n:
        if areaTree[i]['name'] == "中国":
            break
        i += 1

    # 省级
    china = areaTree[i]
    provinces = china['children']

    # 获取新增确诊、累计确诊人数
    province_name_list = []
    province_today_confirm_list = []
    province_total_confirm_list = []
    n = len(provinces)
    for i in range(n):
        province_name_list.append(provinces[i]['name'])
        province_today_confirm_list.append(provinces[i]['today']['confirm'])
        province_total_confirm_list.append(provinces[i]['total']['confirm'])

    print('load data successfully')
    return province_name_list, province_today_confirm_list, province_total_confirm_list

if __name__ == "__main__":
    loadData()