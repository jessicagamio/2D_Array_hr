
def makeArray(arr):

    arr = arr.split(" ")

    array=[]
    subArray=[]

    for i,char in enumerate(arr):
        subArray.append(int(char))

        if (i+1) % 6 == 0:
            array.append(subArray)
            print('subarray ===>', subArray)
            subArray = []
          

    return array







arr = "1 1 1 0 0 0 \
0 1 0 0 0 0 \
1 1 1 0 0 0 \
0 0 2 4 4 0 \
0 0 0 2 0 0 \
0 0 1 2 4 0"


