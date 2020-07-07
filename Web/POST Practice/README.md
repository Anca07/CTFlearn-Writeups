## POST practice

We get one URL for this challenge: http://165.227.106.113/post.php

Let's ignore POST for now and do a simple GET in Postman:

![image](https://user-images.githubusercontent.com/18334788/86831001-084fc500-c09f-11ea-8bcc-7a8da1f28563.png)

Luckily we get the username and password in response.

Let's try a POST with authentication. The credentials should go under *Body tab -> form-data option*.

![image](https://user-images.githubusercontent.com/18334788/86831195-477e1600-c09f-11ea-834f-00a8902b9c4e.png)

And we get the flag in the response:

***flag{p0st_d4t4_4ll_d4y}***