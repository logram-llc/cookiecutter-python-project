# TODO: Pin alpine version
FROM python:{{ cookiecutter.python_version }}-alpine as builder

RUN set -xe \
    && apk upgrade \
    # TODO: Trim down, if not needed. Add missing dependencies.
    && apk add --no-cache gcc g++ musl-dev openssl-dev \
    && pip3 install --upgrade setuptools pip

COPY ./{{ cookiecutter.slug }}/ /install

RUN set -xe \
    && pip3 install --prefix="/install" --no-warn-script-location /install/

# TODO: Pin alpine version
FROM python:{{ cookiecutter.python_version }}-alpine

COPY --from=builder /install /usr/local
COPY --from=builder /usr/lib/ /usr/lib/

RUN set -ex \
    && addgroup -g 96 -S python-user \
    && adduser --uid 96 -D -S --ingroup python-user python-user

USER python-user:python-user

ARG BUILD_VERSION
ARG BUILD_COMMIT_SHA
ARG BUILD_CREATION_DATE
ARG BUILD_URL
ARG BUILD_CLONE_URL

ENV PYTHONUNBUFFERED=1
ENV BUILD_VERSION=${BUILD_VERSION}

LABEL org.opencontainers.image.title="{{ cookiecutter.entrypoint }}"
LABEL org.opencontainers.image.description="{{ cookiecutter.description }}"
LABEL org.opencontainers.image.version=${BUILD_VERSION}
LABEL org.opencontainers.image.created=${BUILD_CREATION_DATE}
LABEL org.opencontainers.image.revision=${BUILD_COMMIT_SHA}
LABEL org.opencontainers.image.url=${BUILD_CLONE_URL}
LABEL org.opencontainers.image.source=${BUILD_URL}

ENTRYPOINT [ "{{ cookiecutter.entrypoint }}" ]