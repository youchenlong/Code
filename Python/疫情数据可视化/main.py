from loadData import loadData

from visualization import plot_country


if __name__ == "__main__":

    provinces, today_confirm, total_confirm = loadData()
    plot_country(provinces, today_confirm, '新增确诊人数')
    plot_country(provinces, total_confirm, '累计确诊人数')