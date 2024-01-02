##POSTFIXEVALUATOR
from Content.usecases.Functions.usecases.RangeCells import RangeCells
from Content.usecases.Functions.usecases.Number import Number
from Content.usecases.Functions.entities.SumOperand import SumOperand
from Content.usecases.Functions.entities.MaxOperand import MaxOperand
from Content.usecases.Functions.entities.MinOperand import MinOperand
from Content.usecases.Functions.entities.PromedioOperand import PromedioOperand

class ContentManager():
    
    def __init__(self, operations, formulaComputing, spreadsheet) -> None:
        self.operators = ["+","-","*","/"]
        self.functions = ["MAX", "MIN", "SUMA", "PROMEDIO"]
        self.postfix = formulaComputing.computeFormula(operations)
        self.spreadsheet = spreadsheet
        self.iDependOn = []
    def calculateFormulaValue(self):
        print("Content Postfix")
        stack = []
        args = []
        
        i = 0
        for token in self.postfix:
            for s in stack:
                print("STACK: ", s.getValue(), token)
            print("ARGUMENTS", args)
            # for x in stack:
            #     print(x.getValue())
            if token in self.operators:
                operand = [stack[len(stack)-2], stack[len(stack)-1]]
                res = self.calculate(operand, token)
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                if token == ":":
                    
                    rangecells = RangeCells(self.postfix[i-2], self.postfix[i-1], self.spreadsheet)
                    stack.pop()
                    stack.pop()
                    stack.append(rangecells)
                    args.append(rangecells)
                    self.iDependOn.extend(rangecells.getCells())
                
                
                elif token == ";":
                    if len(args) == 0:
                        
                        args.append(stack[len(stack)-1])
                        args.append(stack[len(stack)-2])
                        stack.pop()
                        stack.pop()
                    else:
                        args.append(stack[len(stack)-1])
                        stack.pop()


                    print(args)                    
                elif token in self.functions:
                    print("STACK IN FUNCTION" , stack)
                    if self.postfix[i-1] == ":":
                        stack.pop()
                  
                    
                    if token == "MIN":
                        min = MinOperand(args)
                        stack.append(Number(min.getValue()))

                    elif token == "MAX":
                        max = MaxOperand(args)
                        stack.append(Number(max.getValue()))

                    elif token == "PROMEDIO":
                        promedio = PromedioOperand(args)
                        stack.append(Number(promedio.getValue()))

                    elif token == "SUMA":
                        suma = SumOperand(args)
                        stack.append(Number(suma.getValue()))
                                                
                    args = []
                    print("STACK AFTER FUNCTION: ", stack)
                elif token.isdigit():
                    num = Number(token)
                    stack.append(num)
                    
                else:
                    #CAS ESPECIAL CELLREFERENCE
                    cell_value = RangeCells(token, token, self.spreadsheet)
                    self.iDependOn.append(cell_value.getCells())
                    stack.append(cell_value)
       
            i+=1
        
        return stack[0].getValue()         
                    
    def calculate(self, operands, operator):
        
            if operator == "+":
                o = operands[0].getValue() + operands[1].getValue()
                return Number(o)
                
            elif operator == "-":
                o = operands[0].getValue() - operands[1].getValue()
                return Number(o)

            elif operator == "*":
                o = operands[0].getValue() * operands[1].getValue()
                return Number(o)

            elif operator == "/":
                o = operands[0].getValue() / operands[1].getValue()
                return Number(o)

    def dependingCells(self):
        return self.iDependOn