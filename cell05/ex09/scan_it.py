import re
import sys
pattern_for_scan, input_string = sys.argv[1], sys.argv[2]
print(len(re.findall(pattern_for_scan, input_string)))
