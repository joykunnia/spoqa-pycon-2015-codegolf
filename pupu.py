from __future__ import print_function

import sys

draw_struct = [[['\n', 1], [' ', 51], ['*', 7], ['\n', 1], [' ', 50], ['*', 10], ['\n', 1], [' ', 49], ['*', 11], ['\n', 1], [' ', 48], ['*', 13], ['\n', 1], [' ', 48], ['*', 13], [' ', 4], ['*', 3], ['\n', 1], [' ', 48], ['*', 12], [' ', 1], ['*', 11], ['\n', 1], [' ', 48], ['*', 25], ['\n', 1], [' ', 49], ['*', 25], ['\n', 1], [' ', 34], ['*', 8], [' ', 8], ['*', 25], ['\n', 1], [' ', 32], ['*', 10], [' ', 10], ['*', 22], ['\n', 1], [' ', 29], ['*', 13], [' ', 11], ['*', 21], ['\n', 1], [' ', 29], ['*', 13], [' ', 10], ['*', 20], ['\n', 1], [' ', 23], ['*', 24], [' ', 4], ['*', 7], [' ', 2], ['*', 10], ['\n', 1], [' ', 19], ['*', 38], ['\n', 1], [' ', 16], ['*', 40], ['\n', 1], [' ', 14], ['*', 44], ['\n', 1], [' ', 13], ['*', 46], ['\n', 1], [' ', 12], ['*', 48], ['\n', 1], [' ', 11], ['*', 49], ['\n', 1], [' ', 10], ['*', 51], ['\n', 1], [' ', 10], ['*', 52], ['\n', 1], [' ', 9], ['*', 13], [' ', 3], ['*', 15], [' ', 3], ['*', 19], ['\n', 1], [' ', 9], ['*', 10], [' ', 3], ['*', 4], [' ', 2], ['*', 9], [' ', 2], ['*', 4], [' ', 2], ['*', 17], ['\n', 1], [' ', 9], ['*', 10], [' ', 1], ['*', 8], [' ', 1], ['*', 6], [' ', 2], ['*', 8], [' ', 1], ['*', 16], ['\n', 1], [' ', 10], ['*', 8], [' ', 1], ['*', 9], [' ', 1], ['*', 6], [' ', 1], ['*', 9], [' ', 2], ['*', 15], ['\n', 1], [' ', 10], ['*', 8], [' ', 1], ['*', 10], [' ', 1], ['*', 5], [' ', 1], ['*', 10], [' ', 1], ['*', 15], ['\n', 1], [' ', 10], ['*', 8], [' ', 1], ['*', 10], [' ', 1], ['*', 5], [' ', 1], ['*', 10], [' ', 1], ['*', 15], ['\n', 1], [' ', 8], ['*', 10], [' ', 1], ['*', 10], [' ', 1], ['*', 5], [' ', 1], ['*', 10], [' ', 1], ['*', 17], ['\n', 1], [' ', 7], ['*', 11], [' ', 1], ['*', 9], [' ', 1], ['*', 6], [' ', 1], ['*', 10], [' ', 1], ['*', 19], ['\n', 1], [' ', 6], ['*', 13], [' ', 1], ['*', 8], [' ', 1], ['*', 7], [' ', 2], ['*', 7], [' ', 2], ['*', 20], ['\n', 1], [' ', 5], ['*', 16], [' ', 6], ['*', 11], [' ', 7], ['*', 22], ['\n', 1], [' ', 4], ['*', 63], ['\n', 1], [' ', 4], ['*', 63], ['\n', 1], [' ', 4], ['*', 63], ['\n', 1], [' ', 4], ['*', 63], ['\n', 1], [' ', 5], ['*', 61], ['\n', 1], [' ', 6], ['*', 59], ['\n', 1], [' ', 7], ['*', 58], ['\n', 1], [' ', 8], ['*', 56], ['\n', 1], [' ', 9], ['*', 53], ['\n', 1], [' ', 12], ['*', 48], ['\n', 1], [' ', 16], ['*', 39], ['\n', 1]]]

def pupu():

    for line in draw_struct:
        for temp in line:
            text = temp[0]
            loop_cnt = temp[1]
            cnt = 0
            str_list=[]
            while loop_cnt > cnt :
                str_list.append(text)
                cnt += 1

            sys.stdout.write("""""".join(str_list))
        print('')
if __name__ == '__main__':
    pupu()
