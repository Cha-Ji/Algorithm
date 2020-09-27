
class Solution:
    def calcEquation(self, equations, values, queries):
        INIT_INT = 3 * 7 * 11 * 13 * 17 * 19
        calc_dict = {}
        values = sorted(values, key= lambda x : equations[x][0])
        for idx, div in enumerate(sorted(equations)):
            if div[0] not in calc_dict:
                calc_dict[div[0]] = (INIT_INT if div[1] not in calc_dict 
                                        else calc_dict[div[1]] * values[idx])

            if div[1] not in calc_dict:
                calc_dict[div[1]] = calc_dict[div[0]] / values[idx]
        print(calc_dict)
        result = []
        for quo, div in queries:
            if quo not in calc_dict or div not in calc_dict:
                result.append(-1)
            else:
                result.append(calc_dict[quo] / calc_dict[div])
        
        return result
a = Solution()
print(a.calcEquation(
    equations=[["a","b"],["e","f"],["b","e"]], 
    values = [3.4,1.4,2.3], queries = 
    [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))
    

