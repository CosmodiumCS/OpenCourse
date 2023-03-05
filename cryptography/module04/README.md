# Module 0.4.0 - Other Ciphers

## 0.4.1 - Understanding The Vigenere Cipher
- invented by Giovan Battista Bellaso in 1553
	- a more advance version was published by Blaise de Vigenere
	- also called the 'Polyalphabetic cipher'
- let's learn how it works
---
we start with our indexing chart, a little different than the one for the caesar cipher
```
Indexing:
/---------------------------------------------------\
| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---+---+---+---+---+---+---+---+---+---+---+---+---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12|
|---+---+---+---+---+---+---+---+---+---+---+---+---|
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---+---+---+---+---+---+---+---+---+---+---+---+---|
| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25|
\---------------------------------------------------/
```
for this example, we will be using "KEY" as our key
	- our key has the following indexes [these will be important]
```
/-----------\
| K | E | Y |
|---+---+---|
| 10| 4 | 24|
\-----------/
```

## 0.4.2 - Encrypting The Vigenere Cipher
- now we can start to encrypt some plaintext, we will choose the text "ENCRYPT"
- we must first find the indexes of the plaintext's characters
```
/---------------------------\
| E | N | C | R | Y | P | T |
|---+---+---+---+---+---+---|
| 4 | 13| 2 | 17| 24| 15| 19|
\---------------------------/
```
we can now comibne them to the respective index's of our key
```
/---------------------------\
| E | N | C | R | Y | P | T | <-- PLAINTEXT
|---+---+---+---+---+---+---| 
| 4 | 13| 2 | 17| 24| 15| 19| <-- PLAINTEXT INDEXES
|---+---+---+---+---+---+---|
|+10| +4|+24|+10| +4|+24|+10| <-- KEY
|---+---+---+---+---+---+---|
| 14| 17| 0 | 1 | 2 | 13| 3 | <-- CIPHERTEXT INDEXES
|---+---+---+---+---+---+---|
| O | R | A | B | C | N | D | <-- CIPHERTEXT
\---------------------------/
```

## 0.4.3 - Decrypting The Vigenere Cipher
now we can just reverse the process by subtracting the key values from the plaintext
```
/---------------------------\
| O | R | A | B | C | N | D | <-- CIPHERTEXT
|---+---+---+---+---+---+---| 
| 14| 17| 0 | 1 | 2 | 13| 3 | <-- CIPHERTEXT INDEXES
|---+---+---+---+---+---+---|
|-10| -4|-24|-10| -4|-24|-10| <-- KEY
|---+---+---+---+---+---+---|
| 4 | 13| 2 | 17| 24| 15| 19| <-- PLAINTEXT INDEXES
|---+---+---+---+---+---+---|
| E | N | C | R | Y | P | T | <-- PLAINTEXT
\---------------------------/
```

## 0.4.4 - Base64
- a ciphering process that uses binary data to encode text
- each digit is composed of 6 bits [rather than the 8 bit binary digits]
	- this means that four Base64 digits is equal to three binary numbers
	- because of this, we may need a padding at the end of our Base64 string
---
![Base64 Table](https://github.com/CosmodiumCS/Introduction-to-Cryptography/blob/main/images/base64.png?raw=true)
- full credit to Wikipedia - 'https://en.wikipedia.org/wiki/Base64' for the table
---
- you can see how each respective number [binary or decimal] represents the index of an uppercase letter, then a lowercase letter, then a number, and finally a symbol
- this order of characters is part of ASCII [American Standard Code for Information Interchange]
	- it is the national standard that all encoding process's follow in America
