## GitIsGood

For this challenge, we get a file *flag.txt* and a *.git* folder

***1. flag.txt***
The file contains the text **flag{REDACTED}**, so this is a hint that at some point the file used to have the original flag value. Maybe we should check the git history.

***2. .git***

I used [Git for Windows](https://git-scm.com/download/win) to view the history.

Let's inspect the logs:

![image](https://user-images.githubusercontent.com/18334788/86826045-d6d3fb00-c098-11ea-99aa-dd9370d7623b.png)

We notice 3 commits were made. Let's see what the last commit did: 

![image](https://user-images.githubusercontent.com/18334788/86827130-4a2a3c80-c09a-11ea-9f0a-754f7b99f757.png)

Looks like the last commit has overriden the original flag value:

**flag{protect_your_git}**