#!/bin/bash

UTIL=$(df / --output=pcent | tail --lines=1 | tr -d ' %')


if [ $UTIL -gt 90 ];
then
   echo Warning!! Disk space at / utilized at $UTIL
else
   echo OK, Disk space at / utilized at $UTIL
fi
