FROM alpine:latest

COPY process.sh /process.sh
RUN chmod +x /process.sh
ENTRYPOINT ["/process.sh"]