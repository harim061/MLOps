FROM centos:7

# 필요한 패키지 설치
RUN yum groupinstall -y "Development Tools" && \
    yum install -y openssl-devel bzip2-devel libffi-devel

# Python 3.8 소스 다운로드 및 설치
RUN curl -O https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz && \
    tar xzf Python-3.8.10.tgz && \
    cd Python-3.8.10 && \
    ./configure --enable-optimizations && \
    make altinstall

# 심볼릭 링크 생성 (선택 사항: python3 명령어로 Python 3.8 사용)
RUN ln -s /usr/local/bin/python3.8 /usr/bin/python3

# 설치 파일 정리
RUN rm -f Python-3.8.10.tgz && \
    rm -rf Python-3.8.10

# yum 캐시 정리
RUN yum clean all

ENTRYPOINT ["/bin/bash"]