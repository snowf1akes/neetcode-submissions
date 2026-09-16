class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for items in operations:
            if items not in ["+", "C", "D"]:
                arr.append(int(items))
            elif items == "+":
                arr.append(arr[-1] + arr[-2])
            elif items == "C":
                arr.pop()
            elif items == "D":
                arr.append(arr[-1] * 2)
        
        return sum(arr)

        
        