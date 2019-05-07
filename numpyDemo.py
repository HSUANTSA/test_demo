#11. Numpy array takes less memory compare to python list
# import numpy as np
# import sys
#
# lst = range(1000)
# arr1 = np.arange(1000)
#
# print("The list occupied space is",sys.getsizeof(1) * len(lst),"bytes")
# print("The array occupied space is",arr1.itemsize * arr1.size,"bytes")


#2. Numpy arrays runs very faster than python list

# import numpy as np
# import time
#
# lst1 = range(10000000)
# lst2 = range(10000000)
#
# arr1 = np.arange(10000000)
# arr2 = np.arange(10000000)
#
# start_time = time.time()
# lst = [(i,j) for i,j in zip(lst1,lst2)]
# end_time = time.time()
# print("The time taken by list objects is",end_time - start_time)
# start_time = time.time()
# arr1 + arr2
# end_time = time.time()
# print("The time taken by array objects is",end_time - start_time)

# 3. Numpy arrays provides more flexibility to the developer the python list

import numpy as np
arr1 = np.arange(1,11)
arr2 = np.arange(1,11)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)
