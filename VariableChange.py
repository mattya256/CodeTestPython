Alreadyglobal = ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'E', 'traceback', 'time', 're', 'math', 'M_264910_TimeManage_module', 'M_264910_VaribleChange', 'M_264910_printcopy', 'M_264910_inputcopy', 'M_264910_testcase_count', 'M_264910_exit_Exception', 'M_264910_countspace', 'M_264910_defchange', 'M_264910_CheckNull', 'M_264910_remakecode', 'M_264910_codecheck', 'M_264910_ReturnCode', 'M_264910_test', 'M_264910_inputcode', 'M_264910_input_testcase', 'print', 'input', 'M_264910_not_method', 'exit', 'M_264910_inputcode_remake', 'M_264910_inputrow', 'M_264910_TM', 'M_264910_VM', 'M_264910_result', 'M_264910_Before', 'M_264910_DICT', 'M_264910_returnList', 'M_264910_testcase','M_264910_k','M_264910_v']
AlreadyGlobalDict = {}
for i in Alreadyglobal:
    AlreadyGlobalDict[i] = True

def CheckDict(Dict1,Dict2):
    SubDict = {}
    for k,v in Dict1.items():
        if k not in Dict2:
            SubDict[k] = "削除"
        elif v != Dict2[k]:
            SubDict[k] = (v," -> ",Dict2[k])
    for k,v in Dict2.items():
        if k not in Dict1:
            SubDict[k] = "追加"
    return SubDict

def OnlyUse(Dict):
    Dict2 = {}
    for k,v in Dict.items():
        if k not in AlreadyGlobalDict:
            Dict2[k] = v
    return Dict2

class Variable_in_Code:
    def __init__(self,Num,Global_VariableDict,Global_changeDict,Local_VariableDict,Local_changeDict):
        self.CodeNum = Num
        self.Global_VariableDict = Global_VariableDict
        self.Global_changeDict = Global_changeDict
        self.Local_VariableDict = Local_VariableDict
        self.Local_changeDict = Local_changeDict

class Variable_in_Code_List:
    def __init__(self):
        self.List = []
        self.BeforeGlobalDict = {}
        self.BeforeLocalDict = {}
    def Append(self,Num,GlobalDict,LocalDict):
        GlobalDict = OnlyUse(GlobalDict)
        LocalDict = OnlyUse(LocalDict)
        Global_changeDict = CheckDict(self.BeforeGlobalDict,GlobalDict)
        Local_changeDict = CheckDict(self.BeforeLocalDict,LocalDict)
        self.List.append(Variable_in_Code(Num,GlobalDict,Global_changeDict,LocalDict,Local_changeDict))
        self.BeforeGlobalDict = GlobalDict
        self.BeforeLocalDict = LocalDict
