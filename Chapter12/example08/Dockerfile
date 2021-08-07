FROM docker.io/fedora:34
 
RUN dnf install -y cowsay nginx 
RUN echo "daemon off;" >> /etc/nginx/nginx.conf 
RUN cowsay boop > /usr/share/nginx/html/index.html 
 
EXPOSE 80 
 
CMD /usr/sbin/nginx 
