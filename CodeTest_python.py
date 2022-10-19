import traceback
import time
import re
import math

M_264910_printcopy,M_264910_inputcopy = print,input
M_264910_testcase_count = 0

class M_264910_exit_Exception(Exception):
    pass

def M_264910_countspace(Str,beforecount):
    """
    行の先頭にインデントがいくつあるか数える
    """
    count = 0
    for s in Str:
        if s == " ":
            count += 1
        else:
            break
    return count

def M_264910_defchange(String):
    """
    def a()をdef a(TM)のように置き替えることで、
    TMを変数内で扱えるようにする
    """
    x = re.match("(def .*\(.*)(\):)",String)
    if x:
        return True
    else:
        return False

def M_264910_CheckNull(Str):
    """
    何も書かれていない行はエラー原因なので、判定して取り除く
    """
    x = re.match("(?: |　|\r|\n|\t)*",Str)
    if x.group() == Str:
        return True

def M_264910_remakecode(Str):
    """
    可能な限り行の後ろにcodecheckを挿入し、コードのテストを行う
    """
    StrList = Str.split("\r\n")
    newStr = ""
    nowcount = 0
    for i,S in enumerate(StrList):
        #何も書かれていない行は処理しない
        if M_264910_CheckNull(S):
            continue
        newStr += S + "\r\n"
        nowcount = M_264910_countspace(S,nowcount)
        if i+1 >= len(StrList) or (not nowcount < M_264910_countspace(StrList[i+1],nowcount)):
            newStr += " " * nowcount + "M_264910_codecheck(M_264910_TM," + str(i) + ")" + "\r\n"
    return newStr

def M_264910_codecheck(TM,count):
    #コードのチェックを行う、現在は時間と呼び出し回数
    TM.checktime(count)
    

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

class M_264910_ReturnCode:
    def __init__(self,Str,Str2):
        self.OringinalCode = Str
        self.RemakeCode = Str2

M_264910_testcase_count
def M_264910_test(M_264910_inputcode,M_264910_input_testcase):
    M_264910_printcopy("a",time.time())

    # テストケースをテキストで入力
    # inputした回数を記録しておき、コード内で適切な入力を取り出すための変数
    global M_264910_testcase_count
    M_264910_testcase_count = 0

    #pythonに出力されてしまうのでHTMLで使えるよう関数の上書き
    def print(*printtext):
        M_264910_returnList.append(printtext)

    # 同様に上書き
    def input():
        global M_264910_testcase_count
        r = M_264910_testcase[M_264910_testcase_count]
        M_264910_testcase_count += 1
        return r

    #実行したくない関数を定義したい場合に使う
    def M_264910_not_method(*arg):
        pass    

    def exit():
        raise M_264910_exit_Exception("error!")

    M_264910_inputcode_remake = M_264910_remakecode(M_264910_inputcode)
    M_264910_testcase = M_264910_input_testcase.split("\r\n")

    # 入力の行数を保存
    M_264910_inputrow = len(M_264910_inputcode.split("\r\n"))

    # printを返却するためのリスト
    M_264910_returnList = []

    global M_264910_TM
    M_264910_TM = M_264910_timemanage(M_264910_inputrow)

    M_264910_result = ""

    try:
        M_264910_Before = time.time() 
        DICT = globals()
        for k,v in locals().items():
            DICT[k] = v
        exec(M_264910_inputcode_remake,DICT,DICT)

        M_264910_TM.FinishTM()
        M_264910_result += "実行完了: " + str(((time.time()-M_264910_Before)*100//1)/100) + " (s)/r/n"
    except M_264910_exit_Exception as e:
        M_264910_TM.FinishTM()
        M_264910_result += "実行完了: " + str(((time.time()-M_264910_Before)*100//1)/100) + " (s)/r/n"
    except Exception as e:
        M_264910_returnList = []
        M_264910_returnList.append(traceback.format_exc())
        M_264910_result = "実行失敗"

    try:
        #コードの追加を無視して実行し、正規の実行時間を確認する
        DICT = globals()
        for k,v in locals().items():
            DICT[k] = v
        DICT['print'] = M_264910_not_method
        M_264910_testcase_count = 0
        M_264910_Before = time.time() 
        exec(M_264910_inputcode,DICT,DICT)
        M_264910_result += "実行完了: " + str(((time.time()-M_264910_Before)*100//1)/100) + " (s)/r/n"
    except M_264910_exit_Exception as e:
        M_264910_result += "実行完了: " + str(((time.time()-M_264910_Before)*100//1)/100) + " (s)/r/n"
    except Exception as e:
        M_264910_returnList = []
        M_264910_returnList.append(traceback.format_exc())
        M_264910_result = "実行失敗"

    RC = M_264910_ReturnCode(M_264910_inputcode.replace(" ","　").split("\r\n"),M_264910_inputcode_remake.replace(" ","　").split("\r\n"))

    M_264910_TM.changecolor()

    M_264910_printcopy("b",time.time())
    return M_264910_result,M_264910_returnList[0:10],RC,M_264910_TM
