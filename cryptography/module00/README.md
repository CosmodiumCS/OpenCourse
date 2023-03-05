# Module 0.0.0 - What is Cryptography?

## 0.0.1 - Course Requirements
- because this course is designed for beginners, I will do my personal best to make everything clear as possible
---
- Security Linux [Parrot or Kali]
- Python3 Programming Language
- an understanding of computer systems
- Linux and BASH
- algebra and high school level mathematics

## 0.0.2 - Bits & Bytes
- you are already familiar with the Decimal Numeric System
	- a based 10 numeric system
	- numbers composed of 10 digits, ranging from 0-9
		-  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	-  but there are other numeric systems
---
- binary, a based-two, alpha-numeric system
- composed of two digits:
	-	1, on or true
	-	0, off or false
- a binary number is one byte, composed of 8 bits
```
Decimal : 28
Binary  : 00011100
```
---
Decimal --> Binary
- each bit in a binary number represents a value form 0-7, being squared by two
```
/----------------------------------------\
|Decimal | 28|   |   | 12| 4 | 0 |   |   |
|--------+---+---+---+---+---+---+---+---|
|Binary  | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
|--------+---+---+---+---+---+---+---+---|
|Exponet |2^7|2^6|2^5|2^4|2^3|2^2|2^1|2^0|
|--------+---+---+---+---+---+---+---+---|
|Value   |128| 64| 32| 16| 8 | 4 | 2 | 1 |
\----------------------------------------/
```
-   find the first value that can go into your decimal [from the left to your right] 
-   place a "1" in the binary section if the value can go into the decimal
-   list the decimal subtracted by the value, set this as your new decimal value 
-   rinse and repeat using your new decimal
---
Binary --> Decimal
- we are given this binary number `01011010`
- add the values under each "1" to get the decimal form
```
/----------------------------------------\
|Decimal |   | 64|   | 16| 8 |   | 2 |   |
|--------+---+---+---+---+---+---+---+---|
|Binary  | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
|--------+---+---+---+---+---+---+---+---|
|Exponet |2^7|2^6|2^5|2^4|2^3|2^2|2^1|2^0|
|--------+---+---+---+---+---+---+---+---|
|Value   |128| 64| 32| 16| 8 | 4 | 2 | 1 |
\----------------------------------------/
```
- 64 + 16 + 8 + 2 = 90
---
- bytes don't always represent numbers, they can also represent letters and symbols
- some ciphers that we will learn about will encrypt data in sets of bits

## 0.0.3 - Defining Cryptography
- cryptography [also reffered to as 'cryptology] is the study and practice of secure communications. 
- encryption is the process of turning readable information [plaintext] into unreadalbe information [ciphertext]
- decryption is the process of turning ciphertext into plaintext
- a cipher is the algorithm that encrypts plaintext or decrypts ciphertext using a key
- a key is a secretive set of characters used for the ciphering process
- block cipher, a cipher that encrypts/decrypts in blocks [or rounds] of bits
- encoding is a ciphering process that doesn't use a key

## 0.0.4 - Cryptographic Resources
- Course Home - 'https://www.cosmodiumcs.com/introduction-to-cryptography'
- Course Overview - 'https://github.com/CosmodiumCS/Introduction-to-Cryptography'
- Third Party Resources
	- Wikipedia - 'https://en.wikipedia.org/wiki/Cryptography'
- Have Questions?
	- Ask at our Discord - 'https://discord.gg/E5YBNpv8hS'
	- Ask on our Website - 'https://www.cosmodiumcs.com/contact-information'

## 0.0.5 - Homework
read this article - 'https://www.cosmodiumcs.com/post/the-story-of-rockyou'
	- it will be helpful for the next module
