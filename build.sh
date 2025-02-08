#!/usr/bin/bash
aaa=$1
/usr/bin/i686-linux-gnu-gcc -c  -nostdlib ./uploads/$aaa.c -o /tmp/$aaa.o
