# University projects  

A lot of need to be finished (see comments in projects themselves).  

From time to time improving and adding code.  

## Sparse Matrix

The example of memory efficient implementation of Data Structure to store and traverse matrices with a lot of zero-values.  

### Needs to be done  

* Input validating  
* Errors handling  
* Increase scalability (for matrix representation)  
* Additional functionality:  
    1. Insertion checking  
    2. Cycle-traversing for each row and column  
* Tests  

### Interface  

* __from_elements(elements, rows_count, columns_count)__  
create matrix of size `rows_count*columns_count` from non-zero-values elements list  

* __from_matrix(matrix)__  
create from existing matrix  

* __change_element(position, value)__  
change value of element at `position` to `value`  

* __get_non_zeros()__  
get list of non-zero elements  

* __get_first(row_idx, col_idx)__  
get first node with non-zero value in row or column by `idx` 
