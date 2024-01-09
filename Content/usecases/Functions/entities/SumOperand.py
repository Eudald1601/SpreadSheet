
class SumOperand():
    def __init__(self, args) -> None:
        self.args = args
        
    def getValue(self):
        result = 0
        for arg in self.args:
            val = arg.getValue()
            if arg.isType() == "RangeCell":
                for i in val:
                    result += i
            else:
                result += val
        return result