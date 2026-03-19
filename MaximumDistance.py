class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        distance = 0

        for i in range(1,len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            distance = max(distance,abs(current_max-global_min),abs(global_max-current_min))

            global_min = min(current_min,global_min)
            global_max = max(current_max,global_max)

        return distance


