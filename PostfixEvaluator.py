##POSTFIXEVALUATOR
import re
from Argument import Argument
from RangeCells import RangeCells
from Number import Number
from CellReference import CellReference
from SumOperand import SumOperand
from MaxOperand import MaxOperand
from MinOperand import MinOperand
from PromedioOperand import PromedioOperand
class ContentManager():
    
    def __init__(self, operations, formulaComputing) -> None:
        self.operators = ["+","-","*","/"]
        self.functions = ["MAX", "MIN", "SUMA", "PROMEDIO"]
        self.postfix = formulaComputing.computeFormula(operations)
        
    def calculateFormulaValue(self, depending_cells):
        stack = []
        args = []
        i = 0
        for token in self.postfix:
            
            if token in self.operators:
                operand = [stack[i-1], stack[i]]
                res = self.calculate(operand, token)
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                if token == ":":
                    
                    rangecells =  RangeCells(stack[i-1], stack[i])
                    stack.pop()
                    stack.pop()
                    stack.append(rangecells)
                
                elif token == ";":
                    args.append[stack[i]]
                    if len(args) == 0:
                        args.append(stack[i-1])
                        stack.pop()
                    stack.pop()
                    
                elif token in self.functions:
                    if self.postfix[i-1] != ";":
                        args.append[stack[i]]
                        args.append[stack[i-1]]
                        stack.pop()
                        stack.pop()
                    
                    if token == "MIN":
                        MinOperand(args)
                    elif token == "MAX":
                        MaxOperand(args)
                    elif token == "PROMEDIO":
                        PromedioOperand(args)
                    elif token == "SUMA":
                        SumOperand(args)
                        
                    args = []
                    
                elif token.isdigit():
                    num = Number(token)
                    stack.append()
                    
                else:
                    cell_value = CellReference(token, depending_cells[token].content)
                    stack.append(cell_value)
       
            i+=1         
                    
    def calculate(self, operands, operator):
        
            if operator == "+":
                return operands[0] + operands[1]
                
            elif operator == "-":
                return operands[0] - operands[1]

            elif operator == "*":
                return operands[0] * operands[1]

            elif operator == "/":
                return operands[0] / operands[1]

    def dependingCells(self):
        dependincells = []
        for pos in self.postfix:
            if self.is_valid_cell(pos):
                dependincells.append[pos]
        return dependincells
    
    def is_valid_cell(self, cell):
        # Verifica si la celda es válida
        if isinstance(cell, str) and re.match(r'^[A-Z]+[1-9]\d*$', cell):    # Modificar si las celdas pueden ser más largas
            return True
        return False