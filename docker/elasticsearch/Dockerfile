ARG ELASTIC_VERSION=8.5.0

# https://www.docker.elastic.co/
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}
#VOLUME ["/usr/share/elasticsearch/data"]
#EXPOSE 9200
#EXPOSE 9300
HEALTHCHECK --interval=5s --timeout=1s --retries=10 \
    CMD curl -f http://localhost:9200/_cat/health >/dev/null || exit 1
# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu"