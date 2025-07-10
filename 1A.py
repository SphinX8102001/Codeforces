import sys
import math
user_input = sys.stdin.readline().strip().split()
user_input = [int(x) for x in user_input]

height ,width = user_input[0] , user_input[1]
flagstone_length = user_input[2] 

heightwise_required_flagstones = math.ceil(height/flagstone_length)
widthwise_required_flagstones = math.ceil(width/flagstone_length)

total_flagstone_required = heightwise_required_flagstones * widthwise_required_flagstones

print(total_flagstone_required)