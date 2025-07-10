#4.PthonOperators.py

#1.Arithematic Operators
a=10
b=20
print('Addition (a+b):' ,a+b) #Addition (a+b): 30
print('Subtraction (a-b):' ,a-b) #Subtraction (a-b): -10
print('Multiplication (a*b):' ,a*b) #Multiplication (a*b): 200
print('Division (a/b):' ,a/b) #Division (a/b): 0.5
print('Floor Division (a//b):' ,a//b) #Floor Division (a//b): 0
print('Modulus (a%b):' ,a%b) #Modulus (a%b): 10
print('Exponential (a**b)' ,a**b) #Exponential (a**b) 100000000000000000000

#2.Comparision Operators
c=15
d=30
print('Equal to (c==d):' ,c==d) #Equal to (c==d): False
print('Not Equal to (c!=d):' ,c!=d) #Not Equal to (c!=d): True
print('Greater than(c>d):' ,c>d) #Greater than(c>d): False
print('Less than(c<d):' ,c<d) #Less than(c<d): True
print('Greater than or Equal to(c>=d):' ,c>=d) #Greater than or Equal to(c>=d): False
print('Less than or Equal to(c<=d):' ,c<=d) #Less than or Equal to(c<=d): True

#3. Assignment Operators
i = 10
i += 10
print('Add & Assign (i+=10):', i) #Add & Assign (i+=10): 20
i -= 10
print('Subtract & Assign (i-=10):', i) #Subtract & Assign (i-=10): 10
i *= 10
print('Multiply & Assign (i*=10):', i) #Multiply & Assign (i*=10): 100
i /= 10
print('Divide & Assign (i/=10):', i) #Divide & Assign (i/=10): 10.0
i //= 10
print('Floor Divide & Assign (i//=10):', i) #Floor Divide & Assign (i//=10): 1.0
i %= 10
print('Modulus & Assign (i%=10):', i) #Modulus & Assign (i%=10): 1.0
i **= 10
print('Exponential & Assign (i**=10):', i) #Exponential & Assign (i**=10): 1.0

#4. Logical Operators
x = 5
y = 24
print('AND (x > 10 and y < 25):' ,x>10 and y<25) #AND (x > 10 and y < 25): False
print('OR (x > 10 and y < 25):' ,x>10 or y<25) #OR (x > 10 and y < 25): True
print('NOT (x < 10):' , not x<10 ) #NOT (x < 10): False

#5.Membership Operators
Name= "Meghana" #String
print('Meg' in Name) #True
print('i' in Name) #False
print('geM' not in Name) #True
print('Meghana' not in Name) #False

List= ['python','java','ml','dsa','cloud computing'] #List
print('ml' in List) #True
print('blockchain' in List) #False
print('ai' not in List) #True
print('dsa' not in List) #False

Tuple=('cse','ece','eee','it') #Tuple
print('it' in Tuple) #True
print('civil' in Tuple) #False
print('mech' not in Tuple) #True
print('cse' not in Tuple) #False

Set={'pen','pencil','book','scale'} #Set
print('pen' in Set) #True
print('paper' in Set) #False
print('pad' not in Set) #True
print('pen' not in Set) #False

Dict={'name':'virat','age':35,'hobby':'cricket'} #Dict
print('hobby' in Dict) #True
print('place' in Dict) #False
print('job' not in Dict) #True
print('name' not in Dict) #False

#6.Identity Operators
m=[1,2,3] #List1
n=[1,2,3] #List2
print('m' is 'n') #False
print('m' is not 'n') #True
print(id(m))#Memory Allocated for m
print(id(n))#Memory Allocated for n
o=m #List 'm' is assigned to 'o'
print('o' is 'm') #True
print('o' is not 'm') #False
print(id(m))#Memory Allocated for m
print(id(o))#Memory Allocated for o
s1={3,4,5,6,7,8,9}#Set1
s2={3,4,5,6,7,8,9}#Set2
print('s1' is 's2') #False
print('s1' is not 's2') #True
print(id(s1))#Memory Allocated for m
pritn(id(s2))#Memory Allocated for n
s3=s2 #set s2 is assigned to s3
print('o' is 'm') #True
print('o' is not 'm') #False
print(id(s2))#Memory Allocated for s2
print(id(s3))#Memory Allocated for s3

#7.Bitwise Operators
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)








