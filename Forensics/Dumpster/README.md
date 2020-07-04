## Dumpster

For this challenge, there are two files: *Decryptor.java* and *heapdump.hprof*.

***1. Decryptor.java***:

There is a FLAG variable holding the encrypted flag:

![image](https://user-images.githubusercontent.com/18334788/86511376-2d270c80-be01-11ea-9bac-e97b31ff7480.png)

The password string was read from the console:

![image](https://user-images.githubusercontent.com/18334788/86511472-49777900-be02-11ea-9b42-b27e66ed584b.png)

The **passHash** field holds the SHA-256 digest of the password string:

![image](https://user-images.githubusercontent.com/18334788/86511482-6b70fb80-be02-11ea-8a27-8e1f0b7c3875.png)

This was used to decrypt the encrypted flag:

![image](https://user-images.githubusercontent.com/18334788/86511602-62345e80-be03-11ea-806f-fc79a63aaf32.png)

Now we know we need to find the value of either **pass** or **passHash** variables. For this, let's analyze the heap dump file.

***2. heapdump.hprof***

I used *Eclipse Memory Analyzer* tool for loading the heap dump.

In the *Histogram* view we have all the classes loaded, so we can filter for *Decryptor* class:

![image](https://user-images.githubusercontent.com/18334788/86512454-1ab1d080-be0b-11ea-9417-25f29f556517.png)

By *right click on Decryptor$Password -> List objects with outgoing references*, we obtain the **passHash** byte array variable:

![image](https://user-images.githubusercontent.com/18334788/86512502-8431df00-be0b-11ea-8734-a2f29be94074.png)

And its values in the left pannel:

![image](https://user-images.githubusercontent.com/18334788/86512516-a0358080-be0b-11ea-98dc-06f5a2a2693d.png)


Now all we need to do is intialize the **passHash** variable with these values:

![image](https://user-images.githubusercontent.com/18334788/86511960-59915780-be06-11ea-8d5a-910eb54878e0.png)

Also make sure to delete the arguments of the Password constructor in the call so that the code compiles.

![image](https://user-images.githubusercontent.com/18334788/86512046-24393980-be07-11ea-9b61-9cf0c9565187.png)

If we run the program now, it prints the flag to the console:

**stCTF{h34p_6ump5_r_c00l!11!!}**

