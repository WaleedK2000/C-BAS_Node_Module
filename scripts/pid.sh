docker run --rm -it --pid=host ubuntu bash -c '
for e in `ls /proc/*/environ`; do 
  echo
  echo $e
  xargs -0 -L1 -a $e
done
'
