class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):            
            if operations[i] == "+":
                sum_2 = record[-1]+record[-2]
                record.append(sum_2)
            elif operations[i] == "D":
                multi2 = record[-1]*2
                record.append(multi2)
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))
       
        total=0
        for i in range(len(record)):
            total += record[i]
        return total
        