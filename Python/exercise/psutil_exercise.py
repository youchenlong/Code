import psutil

def show_info():
    print('逻辑CPU数量：\t', psutil.cpu_count())
    print('CPU利用率：\t', psutil.cpu_percent())
    print('CPU使用情况：\t', psutil.cpu_times())
    print('内存使用情况：\t', psutil.virtual_memory())
    print('磁盘使用情况：\t', psutil.disk_usage('/'))
    print('网络使用情况：\t', psutil.net_io_counters())
    print('电池使用情况：\t', psutil.sensors_battery())

show_info()
