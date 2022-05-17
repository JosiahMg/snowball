"""
使用baostock获取成分股
需要注册获取token id并且积分达到一定要求
"""
import baostock as bs
import pandas as pd
from common.log_utils import get_logger
from conf.path_config import data_dir
from common.file_operator import make_dir_if_not_exists

logger = get_logger(__name__)


class GenDataByBaostock:
    def __init__(self):
        self.lg = bs.login()
        if self.lg.error_code != '0':
            logger.error('login respond error_code:' + self.lg.error_code)
            logger.error('login respond  error_msg:' + self.lg.error_msg)
            raise Exception(self.lg.error_msg)

    def query_sz50_stocks(self, traderdate=''):
        """ # 获取上证50成分股
            traderdate: 为空表示默认最新的数据
        """
        rs = bs.query_sz50_stocks(traderdate)

        if rs.error_code != '0':
            logger.error('query_sz50 error_code:' + rs.error_code)
            logger.error('query_sz50  error_msg:' + rs.error_msg)
            return

        # 打印结果集
        sz50_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            sz50_stocks.append(rs.get_row_data())

        if len(sz50_stocks) != 50:
            logger.error(f'query_sz50 length[{len(sz50_stocks)}] below 50')
            return

        result = pd.DataFrame(sz50_stocks, columns=rs.fields)
        updateDate = sz50_stocks[0][0]
        # 结果集输出到csv文件
        make_dir_if_not_exists(data_dir)
        result.to_csv(f"{data_dir}/sz50_stocks_{updateDate}.csv", encoding="utf-8", index=False)
        logger.debug(result)

    def query_zz500_stocks(self, traderdate=''):
        """ # 中证500成分股信息
            traderdate: 为空表示默认最新的数据s
        """
        rs = bs.query_zz500_stocks(traderdate)

        if rs.error_code != '0':
            logger.error('query_zz500 error_code:' + rs.error_code)
            logger.error('query_zz500 error_msg:' + rs.error_msg)
            return

        # 打印结果集
        zz500_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            zz500_stocks.append(rs.get_row_data())

        if len(zz500_stocks) != 500:
            logger.error(f'query_zz500 length[{len(zz500_stocks)}] below 500')
            return

        result = pd.DataFrame(zz500_stocks, columns=rs.fields)
        updateDate = zz500_stocks[0][0]
        # 结果集输出到csv文件
        make_dir_if_not_exists(data_dir)
        result.to_csv(f"{data_dir}/zz500_stocks_{updateDate}.csv", encoding="utf-8", index=False)
        logger.debug(result)

    def query_hs300_stocks(self, traderdate=''):
        """ # 沪深300成分股信息
            traderdate: 为空表示默认最新的数据s
        """
        rs = bs.query_hs300_stocks(traderdate)

        if rs.error_code != '0':
            logger.error('query_hs300 error_code:' + rs.error_code)
            logger.error('query_hs300 error_msg:' + rs.error_msg)
            return

        # 打印结果集
        hs300_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            hs300_stocks.append(rs.get_row_data())

        if len(hs300_stocks) != 300:
            logger.error(f'query_hs300 length[{len(hs300_stocks)}] below 300')
            return

        result = pd.DataFrame(hs300_stocks, columns=rs.fields)
        updateDate = hs300_stocks[0][0]
        # 结果集输出到csv文件
        make_dir_if_not_exists(data_dir)
        result.to_csv(f"{data_dir}/hs300_stocks_{updateDate}.csv", encoding="utf-8", index=False)
        logger.debug(result)

    def query_history_k_data(self, code, fields=None, start_date='2000-01-01', end_date='', frequency='d', adjustflag='2'):
        """ 给定股票代码获取股票历史数据
            code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
            fields：指示简称，支持多指标输入，以半角逗号分隔，填写内容作为返回类型的列。详细指标列表见历史行情指标参数章节，日线与分钟线参数不同。此参数不可为空；
            start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
            end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
            frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据
            adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。
        """
        if fields is None:
            fields = "date, code, open, high, low, close, preclose, " \
                     "volume, amount, adjustflag, turn, tradestatus, pctChg, isST"
        else:
            if isinstance(fields, list):
                fields = ','.join(fields)

        rs = bs.query_history_k_data_plus(code,
                                          fields,
                                          start_date=start_date, end_date=end_date,
                                          frequency=frequency, adjustflag=adjustflag)

        if rs.error_code != '0':
            logger.error('query_history_k_data error_code:' + rs.error_code)
            logger.error('query_history_k_data error_msg:' + rs.error_msg)
            return

        # 打印结果集
        stock_histroy = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            stock_histroy.append(rs.get_row_data())

        result = pd.DataFrame(stock_histroy, columns=rs.fields)
        # 结果集输出到csv文件
        make_dir_if_not_exists(data_dir)
        result.to_csv(f"{data_dir}/{code}.csv", encoding="utf-8", index=False)
        logger.debug(result)

    def close(self):
        bs.logout()


if __name__ == "__main__":
    generator = GenDataByBaostock()

    fields = ['date', 'code', 'open', 'high', 'low', 'close', 'volume']
    generator.query_history_k_data('sh.600000', fields)
    generator.close()
