# Created by : David Wang
# Created on : 23 Oct 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-08
# This program displays unicode


print('Uppercase')
print('')
for index1 in range(65, 91):
    print(str(index1) + ' corresponds to ' + unichr(index1))
print('')
print('Lowercase')
print('')
for index2 in range(97, 1235):
    print(str(index2) + ' corresponds to ' + unichr(index2))
