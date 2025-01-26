#!/usr/bin/bash
aaa=$1
/usr/bin/objdump -D -b binary -M intel -m i386 -Maddr16,data16 ./uploads/$aaa.bin >./tmp/$aaa.S
  