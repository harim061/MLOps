import requests
import logging

logging.basicConfig()

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

logger = logging.getLogger('http-app')

urllib_logger = logging.getLogger('urllib3')
urllib_logger.setLevel(logging.ERROR)

logger.info('example.com 에 요청을 전송합니다')
requests.get('http://example.com')