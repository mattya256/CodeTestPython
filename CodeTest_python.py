from tkinter import E
import traceback
import time
import re
import math
import TimeManage as M_264910_TimeManage_module
import VariableChange as M_264910_VaribleChange

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

def M_264910_remakecode(Str,VDB):
    """
    可能な限り行の後ろにcodecheckを挿入し、コードのテストを行う
    VariableDictBoolean(VDB)は辞書の管理を行うかを決定する
    """
    if VDB:
        StrVDB = ",M_264910_VM,globals(),locals()"
    else:
        StrVDB = ""
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
            newStr += " " * nowcount + "M_264910_codecheck(M_264910_TM," + str(i) + StrVDB  + ")" + "\r\n"
    return newStr

def M_264910_codecheck(TM,count,VM = None,globalDict = None,localDict=None):
    """
    コードのチェックを行う、現在は時間と呼び出し回数
    """
    TM.checktime(count)

    if VM != None:
        VM.Append(count,globalDict,localDict)

class M_264910_ReturnCode:
    """
    修正前のコードと修正後のコードを保持するクラス
    """
    def __init__(self,Str,Str2):
        self.OringinalCode = Str
        self.RemakeCode = Str2

M_264910_testcase_count
def M_264910_test(M_264910_inputcode,M_264910_input_testcase):
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

    M_264910_inputcode_remake = M_264910_remakecode(M_264910_inputcode,VDB = True)
    M_264910_testcase = M_264910_input_testcase.split("\r\n")

    # 入力の行数を保存
    M_264910_inputrow = len(M_264910_inputcode.split("\r\n"))

    # printを返却するためのリスト
    M_264910_returnList = []

    M_264910_TM = M_264910_TimeManage_module.M_264910_timemanage(M_264910_inputrow)
    M_264910_VM = M_264910_VaribleChange.Variable_in_Code_List()

    M_264910_result = ""

    try:
        M_264910_Before = time.time() 
        M_264910_DICT = {}
        for M_264910_k,M_264910_v in globals().items():
            M_264910_DICT[M_264910_k] = M_264910_v
        for M_264910_k,M_264910_v in locals().items():
            M_264910_DICT[M_264910_k] = M_264910_v

        #もう一度使うのでコピー
        M_264910_DICT_copy = {}
        for M_264910_k,M_264910_v in M_264910_DICT.items():
            M_264910_DICT_copy[M_264910_k] = M_264910_v

        exec(M_264910_inputcode_remake,M_264910_DICT_copy,M_264910_DICT_copy)

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
        M_264910_testcase_count = 0
        M_264910_DICT_copy = {}
        for M_264910_k,M_264910_v in M_264910_DICT.items():
            M_264910_DICT_copy[M_264910_k] = M_264910_v
        M_264910_DICT_copy['print'] = M_264910_not_method
        M_264910_Before = time.time() 
        exec(M_264910_inputcode,M_264910_DICT_copy,M_264910_DICT_copy)
        M_264910_result += "実行完了: " + str(((time.time()-M_264910_Before)*100//1)/100) + " (s)/r/n"
    except M_264910_exit_Exception as e:
        M_264910_result += "実行完了: " + str(((time.time()-M_264910_Before)*100//1)/100) + " (s)/r/n"
    except Exception as e:
        M_264910_returnList = []
        M_264910_returnList.append(traceback.format_exc())
        M_264910_result = "実行失敗"

    RC = M_264910_ReturnCode(M_264910_inputcode.replace(" ","　").split("\r\n"),M_264910_inputcode_remake.replace(" ","　").split("\r\n"))

    M_264910_TM.changecolor()

    M_264910_variable_timechange = M_264910_VM.List
    
    #順に、実行の有無(str:実行完了or実行失敗)、printされた実行の結果(List:),修正前の修正後のコード、実行回数などを示したTM
    return M_264910_result,M_264910_returnList[0:10],RC,M_264910_TM,M_264910_variable_timechange
