import unittest


def makeArray(arr):

    arr = arr.split(" ")

    array=[]
    subArray=[]

    for i,char in enumerate(arr):
        subArray.append(int(char))

        if (i+1) % 6 == 0:
            array.append(subArray)
            subArray = []
          

    return array


def hourglassSum(arr):
    """returns the maximum sum of hourglass array"""

    array=makeArray(arr)

    maxNum=0

    for i in range(0,4):
        for j in range(0,4):

            top=array[i][j:j+3]
            middle=array[i+1][j+1]
            bottom=array[i+2][j:j+3]

            hourglassSum = sum(array[i][j:j+3]) + array[i+1][j+1] + sum(array[i+2][j:j+3])

            if maxNum == 0:
                maxNum = hourglassSum
            elif hourglassSum > maxNum:
                maxNum = hourglassSum
    return maxNum





arr = "1 1 1 0 0 0 \
0 1 0 0 0 0 \
1 1 1 0 0 0 \
0 0 2 4 4 0 \
0 0 0 2 0 0 \
0 0 1 2 4 0"

#answer is 28
arr1= "-9 -9 -9 1 1 1 \
0 -9 0 4 3 2 \
-9 -9 -9 1 2 3 \
0 0 8 6 6 0 \
0 0 0 -2 0 0 \
0 0 1 2 4 0"

#answer is 13
arr2="1 1 1 0 0 0 \
0 1 0 0 0 0 \
1 1 1 0 0 0 \
0 9 2 -4 -4 0 \
0 0 0 -2 0 0 \
0 0 -1 -2 -4 0"


class testFunction(unittest.TestCase):

    def testMethod(self):
        self.assertEqual(hourglassSum(arr),19)
        self.assertEqual(hourglassSum(arr1),28)
        self.assertEqual(hourglassSum(arr2),13)
if __name__=="__main__":
    unittest.main()
