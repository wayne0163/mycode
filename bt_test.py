import backtrader as bt
import tushare as ts

class MyStrategy(bt.Strategy):
    def __init__(self):
        # 初始化策略是可以定义参数和设置指标等
        pass

    def buy(self): # 定义交易信号
        if self.data.close[0] > self.data.simple_move_avg[0]:
            self.buy()

    def sell(self):
        if self.data.close[0] < self.data.simple_move_avg[0]:
            self.sell()

    def next(self): #定义买入卖出的逻辑
        #检查是否持有头寸
        if not self.position:
            self.buy()
        elif self.position.size > 0:
            self.sell()

    def __init__(self):
        self.data = bt.feeds.PandasData(data_name=self.data)
        self.simple_move_avg = \
        bt.indicators.SimpleMovingAverage(self.data.close,period=10)

def main():
    #创建引擎
    cerebro = bt.Cerebro() 
    #导入数据
    data = bt.feeds.PandasData(data_name=df) # df假设是导入的股票数据
    cerebro.adddata(data)

    # 添加策略
    cerebro.addstrategy(MyStrategy)

    # 运行策略
    cerebro.run()

    #显示结果
    cerebro.plot()

if __name__ == '__main__':
    main()
