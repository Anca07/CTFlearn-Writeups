## GandalfTheWise

For this challenge, there is one file *Gandalf.jpg*.

When we inspect the file with hex editor, we can see 3 comments (or we extract them using **strings** command):

![image](https://user-images.githubusercontent.com/18334788/86513400-96634b80-be12-11ea-8cda-296e074e585f.png)


Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=
xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p
h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU

The first comment is the Base64 representation of a clear text, so let's decode it:

Base64: Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=

Decoded: **CTFlearn{xor_is_your_friend}**

This is a hint that we should XOR the next 2 comments.

Those comments are also in Base64, so we need to decode them and then apply XOR. This short Python script does just that: 

![image](https://user-images.githubusercontent.com/18334788/86513901-9402f080-be16-11ea-8cfe-52d90be29848.png)


We get the flag in clear text:

**CTFlearn{Gandalf.BilboBaggins}**