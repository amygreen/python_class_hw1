def test_pal(num):
    four_dig=str(num)[2:6]
    if four_dig==four_dig[::-1]:
        num+=1
        five_dig=str(num)[1:6]
        if five_dig==five_dig[::-1]:
            num+=1
            six_dig=str(num)
            if six_dig==six_dig[::-1]:
                return num


def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
   """
   for i in range(100000,999999):
       pal=test_pal(i)
       if pal is not None:
          print(pal)
      
print(check_palindrome())
       





       
    