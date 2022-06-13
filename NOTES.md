### Hash Functions

A valid hash function must always return the same hash value for two items representing the same values. For example, the hash function mentioned in the previous paragraph always returns the same value for arrays of identical size and contents, regardless of other attributes such as memory address, etc. However, the converse is not necessarily true. Two items with the same hash values are not necessarily equal. For example, [32, 10] has the same hash value as [18, 10, 14], even though they are not equal. Such cases of two different items hashing to the same value is known as a hash collision.

A good hash function also has the following attributes:

* It is easy to calculate the hash value (the function has low time complexity).
* The chance of collision is very low.
* All possible values are utilized approximately equally.

f("Smith") = 1
    Store the value smith in index 1

f("John") = 4
    Store the value John in index 4

f^-1(4) = 68 which is John

key  value
0  :  
1  :  32
2  : 
3  : 
4  :  68
5  : 

