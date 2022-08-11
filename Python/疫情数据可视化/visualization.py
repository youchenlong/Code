from pyecharts import options as opts
from pyecharts.charts import Map

def plot_world(attrs, values, title):
    map = Map()
    map.add(title, list(zip(attrs, values)), "world", is_map_symbol_show=False)
    map.set_series_opts(label_opts=opts.LabelOpts())
    map.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=min(values), max_=max(values), range_color=['white', 'red']))
    map.render(title + '.html')
    print("visualization finished")

def plot_country(attrs, values, title):
    map = Map()
    map.add(title, list(zip(attrs, values)), "china", is_map_symbol_show=False)
    map.set_series_opts(label_opts=opts.LabelOpts())
    map.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=min(values), max_=max(values), range_color=['white', 'red']))
    map.render(title + '.html')
    print("visualization finished")

def plot_province(attrs, values, title):
    map = Map()
    map.add(title, list(zip(attrs, values)), "四川", is_map_symbol_show=False)
    map.set_series_opts(label_opts=opts.LabelOpts())
    map.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=min(values), max_=max(values), range_color=['white', 'red']))
    map.render(title + '.html')
    print("visualization finished")

if __name__ == "__main__":
    province_distribution = {'China':100, 'United States': 50}
    attrs = list(province_distribution.keys())
    values = list(province_distribution.values())
    plot_world(attrs, values, 'world')

    # province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9,'浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3,'云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '天津': 1,'其他': 1}
    # attrs = list(province_distribution.keys())
    # values = list(province_distribution.values())
    # plot_country(attrs, values, 'china.html')

    # province_distribution = {'成都市':100, '达州市':80}
    # attrs = list(province_distribution.keys())
    # values = list(province_distribution.values())
    # plot_province(attrs, values, 'country')