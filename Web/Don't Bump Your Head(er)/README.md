## Don't Bump Your Head(er)

We get only an URL for this challenge: http://165.227.106.113/header.php

Let's check it with Postman:

![image](https://user-images.githubusercontent.com/18334788/86829390-0553d500-c09d-11ea-9b52-6db4819f48dd.png)

We already get a hint that we are not using the correct User-Agent header. So let's modify it to **Sup3rS3cr3tAg3nt**

![image](https://user-images.githubusercontent.com/18334788/86829721-6a0f2f80-c09d-11ea-8dec-d72f3956e8d5.png)

Great, now we got another hint. We should change the [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header.

![image](https://user-images.githubusercontent.com/18334788/86830033-d12ce400-c09d-11ea-9ca6-d151b55725f8.png)

And the final request will give us the flag:

**flag{did_this_m3ss_with_y0ur_h34d}**