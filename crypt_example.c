/* This example program simply takes two arguments, a password 
   and a salt, and prints the corresponding hash to screen.

   Note that this code should compile on any UNIX based OS, including
   Mac OS X, but the behavior of the program is going to differ
   accordingly.

   In linux, compile with the -lcrypt option activated, otherwise it
   will not work, e.g., 

   gcc -lcrypt crypt_example.c -o crypt_example

   Also note the behavior on LINUX systems of crypt. The actual
   algorithm to be used is part of the salt. For example, setting the salt to be

   $6$aA349808Abcd$ 

   results in the salt "aA349808Abcd" being used with (iterated)
   SHA-512. The algorithm is controlled by the first number (in this
   case 6). Also refer to the man page of crypt for more information.

   This does not work for example on Mac OS X.
*/
#define _XOPEN_SOURCE 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  char *hash;
 
  if(argc != 3) {
    printf("Usage is %s password salt\n", argv[0]);
  } else {
    hash = crypt(argv[1], argv[2]);
    printf("Password: %s\nSalt: %s\nHash: %s\n", argv[1], argv[2], hash);
  }
  return 0;
}
