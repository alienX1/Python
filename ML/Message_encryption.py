# In a certain encrypted message which has information about the
# location(area, city), the characters are jumbled such that the
# first character of the first word is followed by the first
# character of the second word, then it is followed by the second
# character of the first word and so on.

# In other words, let’s say the location is bandra,mumbai

# The encrypted message says ‘bmaunmdbraai’.

import ast,sys
input_str = sys.stdin.read()
# Type your code here
message1 = input_str[0::2]
message2 = input_str[1::2]
print(message1+","+message2)
