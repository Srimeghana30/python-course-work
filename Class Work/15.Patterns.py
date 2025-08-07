#1.
for row in range(5):
    for col in range(5):
        print('*',end=' ')
    print()
'''
  0 1 2 3 4
0 * * * * * 
1 * * * * * 
2 * * * * * 
3 * * * * * 
4 * * * * *
'''

#2.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()
'''
Enter the size:5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''

#3.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(row,end=' ')
    print()

'''
Enter the size:4
0 0 0 0 
1 1 1 1 
2 2 2 2 
3 3 3 3
'''

#4.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(col,end=' ')
    print()
'''
Enter the size:3
0 1 2 
0 1 2
'''

#5.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()
'''
Enter the size:6
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *
'''

#6.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()
'''
Enter the size:6
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''

#7.
n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()
'''
Enter the size:5
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''

#8.
n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
'''
Enter the size:4
* * * * 
  * * * 
    * * 
      *
'''

#9.
n=int(input("Enter the size:"))
for row in range(n):
    if row<=n//2:
        for col1 in range(row+1):
            print('*',end=' ')
    else:
        for col2 in range(n-row):
            print("*",end=' ')
    print()
'''
Enter the size:8
* 
* * 
* * * 
* * * * 
* * * * * 
* * * 
* * 
*
'''

#10.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
Enter the size:7
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * * 
'''

#11.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n/2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
Enter the size:7
* * * * * * * 
*           * 
*           * 
* * * * * * * 
*           * 
*           * 
* * * * * * *
Enter the size:8
* * * * * * * * 
*       *     * 
*       *     * 
*       *     * 
* * * * * * * * 
*       *     * 
*       *     * 
* * * * * * * *
'''

#12.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(row+1):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
Enter the size:6
* 
*   
*     
*       
*         
* * * * * *
'''

#13.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
Enter the size:8
* * * * * * * * 
            *   
          *     
        *       
      *         
    *           
  *             
* * * * * * * *
'''

#14.
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if col==row or col+row==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
Enter the size:5
*       * 
  *   *   
    *     
  *   *   
*       *
'''



