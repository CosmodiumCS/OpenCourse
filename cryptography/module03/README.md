# Module 0.3.0 - Asymmetric Encryption
![Asymmetric Encryption](https://github.com/CosmodiumCS/Introduction-to-Cryptography/blob/main/images/asymmetric.png?raw=true)

## 0.3.1 - Defining Asymmetric Encryption
- a ciphering algorithm that uses a key for encryption [public key] and a key for decryption [private key]
	- asymmetric encryption is often reffered to as public key encryption
	- it is more secure than symmetric encryption
		- more on 'symmetric encryption' in module 2
- private keys are only available to the owner, while public keys are "publicly available"
	- as in available to whoever the owner shares them to

## 0.3.2 - Authentication & Encryption
- similar to symmetric encryption, asymmetric encryption allows for end to end encryption 
- however, it also allows for authentication
- the cipher's public key can assure that a user with the private key sent the encrypted message or file

## 0.3.3 - Diffie-Hellman Key Exchange
- created by Dr. Whitfield Diffie and Dr. Martin Hellman
- allows for the generation and exhange of asymmetric keys
---
How It Works
1. John and Jane both pick two whole numbers
	- both must be larger than one, Jane's must be larger than John's
	- the larger the number, the more secure [but more processing memory]
```
1 < JohnsInteger < JanesInteger
```
2. John and Jane run both pick two random numbers and run it through the following equation 
	- '\*\*' = to the power of
	- '%' = the remainder of
```
JohnsResult = JohnsInteger ** JohnsRandomInt % JanesInteger
JanesResult = JohnsInteger ** JanesRadnomInt % JanesInteger
```
3. John and Jane send their respective results to each other. with these results, they will generate their keys
```
JohnsKey = JanesResult ** JohnsRandomInt % JanesInteger
JanesKey = JohnsResult ** JanesRandomInt % JanesInteger
```
