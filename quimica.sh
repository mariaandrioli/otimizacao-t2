#!/bin/sh
make
FILES="testes/*.in"
if [ $? -eq 0 ] ; then
  for f in $FILES
  do
    echo "Processing $f file..."
    ./quimica < $f
    echo "\n"
  done
else 
  echo "failed to compile"
fi
make clean