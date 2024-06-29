FROM centos:8

# EPEL 리포지토리 설치 및 패키지 설치
RUN dnf install -y epel-release && \
    dnf install -y \
    python38 \
    && dnf clean all

# Python 패키지 설치
RUN pip install \
    pytest==6.2.5 \
    --no-cache-dir

# 컨테이너가 실행될 기본 명령 설정
ENTRYPOINT ["/bin/bash"]