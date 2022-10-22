import time
import math

class M_264910_timemanage:
    """
    各行の実行時間、出現回数、一回当たりの実行時間を保持するクラス
    """
    def __init__(self,count):
        self.time_start = time.time()
        self.beforetime = time.time()
        self.time_sum = [0 for i in range(count)]
        self.count_sum = [0 for i in range(count)]
        self.time_per_count = [0 for i in range(count)]
    def checktime(self,count):
        x = time.time() - self.beforetime
        self.time_sum[count] += x
        self.count_sum[count] += 1
        
        self.beforetime = time.time()
    def FinishTM(self):
        #一回当たりの実行時間を求める
        #小数第四位以下を四捨五入
        for i in range(len(self.time_per_count)):
            if self.count_sum[i] != 0:
                self.time_per_count[i] = self.time_sum[i]/self.count_sum[i]
            for x in [self.time_sum,self.time_per_count]:
                x[i] = math.floor(x[i]*1000)/1000
    def changecolor(self):
        #値をもとにコードカラーを作成する
        SUM,LEN = sum(self.time_sum)+0.000001,len(self.time_sum)
        self.time_sum_color = ["background-color:rgb(255," + M_264910_createcolor(x,SUM) + "," + M_264910_createcolor(x,SUM)  + ")" for x in self.time_sum]
        SUM,LEN = sum(self.count_sum)+0.000001,len(self.count_sum)
        self.count_sum_color = ["background-color:rgb(255," + M_264910_createcolor(x,SUM) + "," + M_264910_createcolor(x,SUM)  + ")" if x != 0 else "background-color:rgb(226,226,226)" for x in self.count_sum]
        SUM,LEN = sum(self.time_per_count)+0.000001,len(self.time_per_count)
        self.time_per_count_color = ["background-color:rgb(255," + M_264910_createcolor(x,SUM) + "," + M_264910_createcolor(x,SUM)  + ")" for x in self.time_per_count]

def M_264910_createcolor(x,SUM):
    #実行時間の長い箇所が濃い色になるように調整する。
    return str(max(0, 255 - (((x * 255) /SUM ) // 1)))