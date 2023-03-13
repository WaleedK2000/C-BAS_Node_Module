docker build -t vulimage - <<EOF && docker run --rm -it vulimage sh
FROM nginx
RUN useradd guest
RUN echo "root:root" | chpasswd
USER guest
EOF
