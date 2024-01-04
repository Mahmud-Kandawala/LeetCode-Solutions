class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]] #Initialized with a list, represents the first row
        for i in range(numRows -1): #Iterate, as the first row is already initialized
            temp = [0] + result[-1] + [0] #Starts and ends with 0, and in between, it contains the elements of the last row
            row = []
            for j in range(len(result[-1]) + 1): #Iterates over the range of the length of the last row plus one
                row.append(temp[j] + temp[j + 1]) #Calculates the sum of adjacent elements in the temp list and appends it to the row list
            result.append(row) #Newly created row is appended to the result list
        return result   
