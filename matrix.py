#for Example: x=[[1,2],[3,4],[5,6]]
#this,would represent a3x2 matrix.
#Base Matrix operation.
#there are Sum and Multiply
def Sum_matrix(x,y):
    x_column=[]
    y_column=[]
    for i in range(len(x)):
        for j in x[i]:
            x_column.append(j)
    for i in range(len(y)):
        for j in y[i]:
            y_column.append(j)
    
    equal=(len(x)==len(y))
    if(equal and len(x_column)==len(y_column)):
        for i in range(len(x)):
            for j in range(len(x[0])):
                if(x[i][j]==str(x[i][j])):
                     return "it's has a string in the Matrix list."
            for k in range(len(y[0])):
                if(y[i][k]==str(y[i][k])):
                    return "it's has a string in the Matrix list."
            #sum operation.
            for a in range(len(y[0])):
                    x[i][a]+=y[i][a]
            return x
    else:
        return "on the matix list has is false lenght,\nso this is should be of a equal matrix list"


def Multiply_matrix(x,y):
    list2=[]
    x_column=[]#this is for the 'x' columns lenght
    y_row=[]#this is for the 'y' rows lenght
    
    #that is time show to False if has a string on the list
    for i in range(len(x)):
        for j in x[i]:  
            if(j==str(j)):
                return "it's has a string in the Matrix list."
    for k in range(len(y)):
        for p in y[k]:
            if(p==str(p)):
                  return "it's has a string in the Matrix list."
    #to get index number of columns on the matrix x.
    for a in range(len(x[0])):
        x_column.append(a)
    #to get index number of rows on the matrix y
    for b in range(len(y)):
        y_row.append(b)
        
    #number of rows and columns in the matrix is should be equal
    if(len(x_column)==len(y_row)):
        for i in range(len(x)):
            for j in range(len(y[0])):
               list1=0
               for k in range(len(y)):
                    list1+=x[i][k]*y[k][j]
               list2.append(list1)
        return list2
            
    # We can multiply a matirx by a 'constant'
    if(len(x_column)==1):
        constant_list=[]
        for i in range(len(y)):
            z=0
            for j in y[i]:
               z=x[0][0]*j
               constant_list.append(z)
        return constant_list
    elif(len(x_column)!=len(y)):
        return "Number of  columns in one matrix\nshould be equal to the number of rows  in second matirx"
