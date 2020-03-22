# use an existing docker image as a base
FROM alpine


# download and install a dependency
RUN apk add --update  openjdk8-jre
WORKDIR /usr/app
COPY ./ ./

# Tell the image what to do when it starts as a continer
#CMD ["java", "HelloWorld"]
#ENTRYPOINT ["java", "HelloWorld"]
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "HelloWorld"]

# docker build -t <<your_name>>:latest .
# docker run -it hbjava
# docker run -it alpine sh
# /# apk add --update redis