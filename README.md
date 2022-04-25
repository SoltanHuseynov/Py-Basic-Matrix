# Basic Matrix
<div><a>Matrix is an arrangement of numbers into <i>rows</i> and <i>columns</i>.</a></div>

## Matrix rule
<p>Number of columns in the first matrix(x) should be equal to the number of rows in the second matrix(y)</p>

## Process
<p> For test,we're creating a matrix list,just the python specail is a matrix list.<p>

  For example,the dimension of the matrix below is ` 3 x 2 `,because there are three rows and two columns.
  
  **Python**
  
  ``` 
  x=[     [1,2],
          [4,5],
          [6,3]
        ]
  ```
  **Note**: The Python hasn't prepared a built for matrices.
  Maybe there is prepared a built but your're import to this library into code.
  
  - this is ` numpy ` and these are like matrix lists,so like a arrey
  ```
    import numpy as np
    x = np.array([[1, 2, 3], [3, 4, 5]])
  ```
  
  
![matrix of image](https://upload.wikimedia.org/wikipedia/commons/b/bf/Matris.png)
  
- A matrix sum. The tow matrix must be same size or index length.

on the formula,this is `x[i][a]+=y[i][a]` and there is nested for loop 
  
![matrix of image](https://www.mathsisfun.com/algebra/images/matrix-addition.gif)
  
- A matrix multiply by a constant.
<p> 
  
  if there is a index into the list,it will be `z=x[0][0]*j`
</p>

![matrix of image](https://www.mathsisfun.com/algebra/images/matrix-multiply-constant.gif)

- Multiplying a matrix by another matrix
<p>
  
  on this process,it's important `list1+=x[i][k]*y[k][j]` these are rows and columns must be equal on every two list.
<p>
  
 we need to do [dot product](https://www.mathsisfun.com/algebra/vectors-dot-product.html) of rows and columns
  
 ![matrix of image](https://www.mathsisfun.com/algebra/images/matrix-multiply-a.svg)
