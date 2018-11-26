EXPLOIT1
run this script with the length of the compiler-allocated space for the buffer
in order to overwrite the return address.  This will make the address return to 0x08048685,
which is the print statement before the system call for a new shell with escalated privileges.
This shell can run the h4ck command and add blake_johnson to the group Mr177.
21 for the buffer size + 4 for the stack pointer gives us the location of the return address that I overwrote.
padding = "b" * length (length is 21+4)creates the necessary padding to cause the correct overflow and allow for a specific return address.
TA Christian did a really good job explaining this conceptually in section



EXPLOIT2
Exploit 2 was different than exploit one because there was no system call already in place that would open up a shell with escalated privileges, meaining I could not 
only redirect program flow, I also had to inject the necessary machine code to open up a shell through execv.
To do this, I overflowed the buffer to get a return address of my choice, similar to number one.  Instead of using 'b' as my padding like in number one, I used machine
code that opens a shell, which was padded with nop (\x90) to create a nop sled.  This made my target return address range bigger.  From there, I was able to get the return address through trial and error and educated guessing.  I started off with calculating the distance of the buffer from the ebp, since I knew the address of ebp from gdb.  from there I incremented upwards until eventually I hit the nop sled and opened up an escalated shell.  However, I think there is some difference or randomization between trials with this exploit. I hardcoded my exploit to return to a certain address, and I think that address has since changed, because I tried to run this exploit a few days later and it was no longer working.  I still recorded my progress through h4ck, so I hope I can still get full credit.


EXPLOIT3
Exploit 3 built upon exploits 1 and 2.  This time I was without inherent shell code and I was without a buffer big enough to store my nop-padded machine code.  To work around this, I used environment variables to store the nop-padded machine code from number 2, and used the 8 byte buffer to overflow my return address to that of my specified environment variable. Since the offset from the ebp to the environment variables is 0x10, finding the address was easy and I was able to open up a shell that could execute h4ck.


EXPLOIT4
Exploit 4 was difficult for me due to the de-escalation aspect of shell.  I noticed the setgid bit was set, and I tried copying my_programs to my home directory and executing it, but my base privileges kept me from executing h4ck even though I did not receive the de-escalation warning from shell.  After this i looked into integer overflow exploits, thinking the factorial executable that is given could perform some sort of overflow.  However that would be a heap overflow i belive, which we have not covered in depth, so I went back to trying to escalate privileges in my_programs, but I noticed in gdb that the buffer was copied using strncpy, which is not succeptible to overflow attacks.  The only other idea I had was trying to expose fscanf somehow, because I know that it is vulnerable.  I have spent like 9 hours on this last part today alone and it's getting close to the due date, so I am not going to be able to execute h4ck but hopefully I can get some partial credit for my thought processes.  Thanks for reading.


