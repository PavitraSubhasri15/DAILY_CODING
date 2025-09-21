QUESTION : SECOND LARGEST

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max1=-1
        max2=-1
        for i in arr:
            if i>max1:
                max2=max1
                max1=i
            elif i!=max1 and max2<i:
                max2=i
        return max2 if max2!=-1 else -1
                


QUESTION: BUY AND SELL STOCK

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        profit=0
        for price in prices:
            buy=min(buy,price)
            profit=max(profit,price-buy)
        return profit
            


QUESTION:A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the Spreadsheet class:

Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
void resetCell(String cell) Resets the specified cell to 0.
int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

CODE:
class Spreadsheet:

    def __init__(self, rows: int):
        self.grid=[[0 for _ in range(26)]for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col=ord(cell[0])-ord('A')
        row=int(cell[1:])
        self.grid[row-1][col]=value

    def resetCell(self, cell: str) -> None:
        col=ord(cell[0])-ord('A')
        row=int(cell[1:])
        self.grid[row-1][col]=0

    def getValue(self, formula: str) -> int:
        formula=formula.lstrip('=')
        op1,op2=formula.split("+")
        
        def resolve(op):
            if op.isdigit():
                return int(op)
            else:
                col=ord(op[0])-ord('A')
                row=int(op[1:])-1
                return self.grid[row][col]
        return resolve(op1)+resolve(op2)


