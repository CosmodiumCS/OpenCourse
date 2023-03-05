# Module 0.2.0 - Symmetric Encryption
![Symmetric Encryption](https://github.com/CosmodiumCS/Introduction-to-Cryptography/blob/main/images/symmetric.png?raw=true)

## 0.2.1 - Defining Symmetric Encryption
- a ciphering algorithm that uses the same key to encrypt and decrypt plaintext
- faster than asymmetric encryption
	- more on 'asymmetric encryption' in module 3

## 0.2.2 - Understanding The Caesar Cipher
- a symmetric encryption ciphering process, that works by moving [shifitng] letters down the alphabet by a certain number [index]
- it was named after Julius Caesar, who used it as a way to send messages amoungst his army
- Cryptography With Java | Caesar Cipher livestream - 'https://www.youtube.com/watch?v=VLOzGG7u4x4'
---
Example [shift of 1]
```
Plaintext Indexing:
	/-----------\
	| A | B | C |
	|---+---+---|
	| 1 | 2 | 3 |
	\-----------/
	
Ciphertext Indexing:
	/-----------\
	| B | C | D |
	|---+---+---|
	| 1 | 2 | 3 |
	\-----------/
	
	plaintext = "Hello"
	ciphertext = "Ifmmp"
	
	Note: each character shifted over by one, that 'shift' is our encryption key
```
---
Algorithms
```
Encryption:
	C = (X + N) % 26
	
Decryption:
	C = (X - N) % 26
	
	C = character
	X = index
	N = number of indexes we shift down [key]
```

## 0.2.3 - Encrypting The Caesar Cipher
- if you did your homework, you should have cloned the 'python-caesar-cipher' repository to your course directory
- let's use this script to explore symmetric encryption concepts
- in your terminal, run:
```
cd python-caesar-cipher/
echo "Hello, World!" > file.txt
python3 caesar-cipher.py
```
we are now prompted to enter a file name, let's enter the 'file.txt' we created
```
Enter File Name : file.txt
Choose an Option :
1) Encrypt
2) Decrypt
3) Bruteforce
4) Exit
```
- let's choose option '1' to encrypt
- we are now prompted to choose an encryption key, we'll choose a key of 5 [remember that]
```
1
Shift of : 5
Translating...
Success! Output Written to encrypted-caesar.txt
```
let's see the contents of the encrypted text
```
cat encrypted-caesar.txt 
Mjqqt, Btwqi!
```

## 0.2.4 - Decrypting The Caesar Cipher
- let's decrypt our ciphertext
```
python3 caesar-cipher.py 
Enter File Name : encrypted-caesar.txt
Choose an Option :
1) Encrypt
2) Decrypt
3) Bruteforce
4) Exit
2

Shift of : 
```
now because this is a symmetric encryption, it can only be decrypted with the same key used to encrypt it [in this case, the number 5]
```
Shift of : 5
Translating...
Success! Output Written to decrypted-caesar.txt
```
let's view the contents of our decrypted text
```
cat decrypted-caesar.txt 
Hello, World!
```

## 0.2.5 - Bruteforcing The Caesar Cipher
- symmetric encryption methods don't tend to be the most secure, mainly because the keys for both parties are the same
- there is a special case for the Caesar Cipher that makes it especially insecure, it only has 26 possible keys
	- How is that possible? ['A' has an index of 1 & 'Z' has an index of 26] Because 'Z' is the last letter, there is no index higher than 26. So once 'Z' receives a shifted index of 1, it can have to recycle back to 26 because there are no other indexes. Therefore, if the shift key is 36 then the shift key is also equal to 10.
- we can exploit this unuiqe feature by trying to decrypt text 26 times, using 26 different keys [each key ranging from 1 to 26]
- luckily, our script will save us hours of time, and automate this process for us
- to do so, we will choose option '3'
```
python3 caesar-cipher.py 
Enter File Name : encrypted-caesar.txt
Choose an Option :
1) Encrypt
2) Decrypt
3) Bruteforce
4) Exit
3

Choose an Option :
1) Bruteforce All shift Keys
2) Choose Range
```
- we are prompted to do two options
	- the first will bruteforce using all 26 keys
	- the second will brute force keys between a range you can choose [in case if the encrypted text is really large and you know that the key is between a certain range]
- we will choose the first
```
1
Bruteforcing...
Success! Output Written to bruteforce-all-keys.txt
```
let's read those file contents
```
...
Shift Key: 4
Ifmmp, Xpsme!

Shift Key: 5
Hello, World!

Shift Key: 6
Gdkkn, Vnqkc!
...
```
- we can see that our script tried 26 different keys, and the fifth one showed us the plaintext contents
---
Fun fact, ROT13 [ROTation 13] is a cipher the exact same as the caesar cipher, but the key is always 13

## 0.2.6 - Advanced Encryption Standard [AES or Rijndael]
- a symmetric block cipher that encrypts/decrypts blocks of 128 bits using keys sized at 128, 192, or 256
	- this encryption method is [currently] the only publically available encryption method used by the U.S Government
		- it is allowed for the use of encrypting classified data
	- one of the most memory effecient ciphers [on a hardware and software level]
- the encryption rounds of the AES block cipher will vary depending on it's key bit size
```
128 bit keys --> 10 rounds
192 bit keys --> 12 rounds
256 bit keys --> 14 rounds
```
- this will be about as far as we dive into AES, but here is a link to learn more about this topic - 'https://en.wikipedia.org/wiki/Advanced_Encryption_Standard'
- we can use this website to encrypt data using AES-256
	- 'https://encode-decode.com/aes256-encrypt-online/'
	- try different passwords [keys] to makeyour ciphertext stronger

## 0.2.7 - Padding 
- because the encryption works in blocks of 128 bits, the ciphertext will often end with a '\=\=' padding
	- Why? let's say our plaintext is 150 bits. after we encrypt our first block of 128 bits, there are only 22 bits left. We need another 106 bits of data in order to meet the quota of 128 bits. Once fulfilled, the cipher can finish properly. This data added to the end is the padding.

## 0.2.8 - Homework
read this article on RSA, a type of asymmetric encryption
- 'https://hackernoon.com/how-does-rsa-work-f44918df914b'
