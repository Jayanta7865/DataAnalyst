##In NumPy, missing values are usually represented as: np.nan
## we can handel using 
##np.isnon():-This function check any non value present in array.if present return true.
##syntex=np.sinan(array)

import numpy as np
arr=np.array([1,2,3,np.nan,5,6,np.nan,8,np.nan,np.nan])
print(np.isnan(arr))

##np.nan_to_num():This function used to replace nan values in an array
##syntex=np.nan_to_num(array,nan=value) by defalut it take 0

new_arr=np.nan_to_num(arr,nan=10) ## replace all nan into 10
print(new_arr)
new_arr=np.nan_to_num(arr) ## replace all nan value by default 0
print(new_arr)

##np.isinf():It is used to detect infinite values in an array.
#🔥 What are Infinite Values?
# +inf → positive infinity
# -inf → negative infinity
# syntex=np.isinf(array)
inf_arr=np.array([1,2,3,np.inf,5,6,-np.inf,8,np.inf,-np.inf])
print(inf_arr)

#How replace inf value
##np.nan_to_num(array,posinf=value,neginf=value)
new_inf=np.nan_to_num(inf_arr,posinf=10,neginf=-20)
print(new_inf)

