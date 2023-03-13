docker run --rm --privileged alpine:latest sh -c "head -1 /etc/mtab && sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab" > output.txt

