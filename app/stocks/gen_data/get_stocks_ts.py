"""
使用tushare获取成分股
需要注册获取token id并且积分达到一定要求
"""
import tushare as ts
from conf.config import TushareConfig


class GenDataByTushare:
    def __init__(self, tokenid=TushareConfig['tokenid']):
        self.pro = ts.pro_api(tokenid)

    def query_sz50_stocks(self, start_date=None, end_date=None):
        """ 获取上证50成分股 """
        sh50_df = self.pro.index_weight(index_code='000016.SH', start_date=start_date, end_date=end_date,
                                        fields=["con_code", "trade_date", "weight"])
        return sh50_df


if __name__ == "__main__":
    generator = GenDataByTushare()
    print(generator.query_sz50_stocks())

