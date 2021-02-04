# Day 8 of 100 Days of Code
## Caesar Cipher

Today's lesson built on previous knowledge of functions by adding in arguments. The concept itself is something I am familiar with working with, but I found the challenge quite difficult today. 

The most challenging exercise before the end project was definitely the prime number checker. This takes in any number and outputs whether it is prime or not. Dr Angela did it a much simpler way than I did, but I got there in the end and was proud for figuring it out.

Dr Angela's method:
```python
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime")
    else: 
        print("Not prime")
```
My method:
```python
def prime_checker(number):
    if number == 0 or number == 1:
        print("Not a prime")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("Not prime")
                break
        if number % i != 0:
        print("Prime")    
```
A Caesar Cipher is an ancient encryption technique that I didn't know existed until today! A message is written and a predetermined "shift" is used to encrypt the message. For example if the shift is 3, then "a" becomes "d", "b" becomes "e", and so on. The same shift is then used in reverse to decode the message.

![Caesar Cipher](https://lh3.googleusercontent.com/proxy/btfQ_Qcbh7Romq3Kz2kDTQhEz8HHgfUDTL3avvXW3N_iYHt-bgCQ03T6jXS6r_o98r5W36Ea4LdCmNnfD1Dp-RNmVwYCjlJMh8tPL9pLFYZbaq4aY-q89aS5Ug_pfaJq_vm5hBcT_rVi0mrlI9xPtiLH0WrTapebPcaXR-2njStyLyd6gGK0BB8)

The hardest part about the Caesar Cipher project was figuring out how to shift the letters and loop it around so that "z" can still be shifted too. Once I figured it out, the rest all fell into place.

```python
message = ""
current_index = alphabet.index(letter)
                new_index = current_index + shift
                if new_index > 25:
                    new_index -= 26
                letter_coded = alphabet[new_index]
                message += letter_coded
        print(message)
```