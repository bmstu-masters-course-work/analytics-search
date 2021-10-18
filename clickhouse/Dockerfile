FROM alpine:3.14

RUN apk add curl
RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64
RUN chmod +x /usr/local/bin/dbmate

WORKDIR /migration/
COPY . ./
CMD ["sh", "/migration/entrypoint.sh"]
