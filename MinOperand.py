from Function import Function
class MinOperand(Function):
    def __init__(self,args) -> None:
        self.args = args
        super().__init__()
        
    
    def getValue(self):
        result = 0
        for arg in self.args:
            val = arg.getValue()
            if arg.isType() == "RangeCell":
                for i in val:
                    if i <= result:
                        result = i
            else:
                if val <= result:
                    result = val
        return result