# Module 0.1.0 - Password Hashing

## 0.1.1 - Understanding Hashes
- when you make an account for a service, they store your passwords in one of three main ways:
	1. plaintext
	2. ciphertext
	3. hashing

## 0.1.2 - Storing Plaintext
- if you did your homework, you would understand why storing passwords in plaintext can be so dangerous. 
- if you didn't do the homework, the rockyou.txt file is a file holding the most common passwords on the internet, all in plaintext
- in our security linux operating system, we actually have acces to the 'rockyou.txt' file
	- let's explore it
---
run the following in your terminal:
```
cd /usr/share/wordlists/
ls
```
if you see a `rockyou.txt.gz` instead of `rockyou.txt`, run:
```
sudo gzip -d rockyou.txt.gz
```
- we can now iterate through the rockyou.txt
- let's look for all the passwords containing 'tree'
```
cat rockyou.txt | grep tree
```
- you can replace 'tree' to look for any password you wish, you can even try some of your passwords to see if they are in there

## 0.1.3 - Storing Ciphertext
- some services may store passwords, but encrypt/encode them before storing them
	- there are many methods of encryption, a lot of which we will cover next module
- now encrypting passwords may seem smart, but may not be as smart as you think
- this is because, if we can encrypt a password, we can decrypt a password
---
- let's say we are a hacker, and we uncovered this password from a database
```
c3Vic2NyaWJl==
```
- because of the padding at the end '\=\=' we know it's [probably] a base64 encoding
	- we will dive into paddings and block ciphers later in the course
- let's use our terminal to decrypt it
```
echo "c3Vic2NyaWJl" | base64 -d
```

## 0.1.4 - Storing Hashes
- so if plaintext is to dangerous and ciphertext can be to dangerous, how do we stroe passwords?
- actually, most [secure] services don't store the passwords at all, they store hashes
- hashing, the process of generating ciphertext from plaintext, using some sort of mathematical function
	- hashes can not be decrypted
- so if services store your passwords in hashes, but you can't decrypt them, how do services know if your password is correct?
	- simple, when an user enters their password, it is hashed.
	- the hashed version of the password they entered is compared to the password stored in the database
- but if we can't decrypt a hash, how do hackers figure out your password?
---
- let's say we are a hacker, and we found the following hash in a database
```
f40fd562f63078722310bf105375576916ef81609331c36aa36015b4f56f9082
```
- we can obtain the plaintext password by bruteforcing using some sort of rainbow table
	- bruteforcing [dictionary attacks] is a password attack where an attacker iterates through a list of possible passwords, trying each one until one works
		- this process would obviously be automated by some sort of script or program
	- a rainbow table, is a bruteforce attack but each password is hashed and compared to the hashed password we obtained
- now we could create our own rainbow tables or we can use rainbow tables where somebody took a every word in the english dictionary and every password in rockyou, hashed them, and stored them in a database
- websites like 'https://crackstation.net/' will search it's database to see if it has a hash that matches your hash, if it finds one, it will display the plaintext it has stored with the hash
	- go ahead and try to see if you can figure out the plaintext version of the hash
	
## 0.1.5 - Salts
- so if hackers found a way to break through hashes, how do websites stay protected against bruteforce attacks
- introducing salts, a random string of text added to the end of a hash
- it will protect against bruteforce attacks but hackers can still easily identify salts
- this is the reason why it is so important to use complex passwords
	- the more complex the password is, the less likely it will be in a database of 'likely' passwords

## 0.1.6 - Homework
- in your terminal, clone this repository to your course directory
```
git clone https://github.com/CosmodiumCS/python-caesar-cipher.git
```
- if you want to see the GitHub page for this repository, i'll have it linked here - 'https://github.com/CosmodiumCS/python-caesar-cipher.git'
- we will need this code for our next module