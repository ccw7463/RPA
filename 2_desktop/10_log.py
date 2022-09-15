# 자동화를 실행하고있을떄는 print 문을 볼수없을 수도 있음
# 따라서 자동화진행동안 파일이나 로그를 남겨서 확인가능

import logging

from isort import stream

'''
◆ 터미널에 로깅 남기기

<방법1>
logging.basicConfig(레벨,포맷) 설정 
    - logging 에 남길 레벨과 형식을 설정해준다.
logging.debug("문장1") --> debug 레벨 시 로깅 내용
    - 나머지 이하 동일
    - log level 순서 : debug < info < warning < error < critical 
'''
# DEBUG 레벨이상 모든 log를 찍어줌
# logging.ERROR 으로 설정시 ERROR 이상만 로그 남김 
logging.basicConfig(level=logging.ERROR,format="%(asctime)s [%(levelname)s] %(message)s") 

# debug < info < warning < error < critical : log level 순서
logging.debug("아 이거 누가 짠거야?")
logging.info("자동화 수행 준비")
logging.warning("경고 : 실행상에 문제가 있을 수 있습니다.")
logging.error("에러가 발생하였습니다. 에러코드는 ...")
logging.critical("복구가 불가능한 문제가 발생했습니다.")


'''
◆ 터미널에 로깅 남기기

<방법2>
(1) 포맷객체정의
    - logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
(2) logging 객체 정의 
    - logger  = logging.getLogger()
(3) log 레벨 정의 
    - logger.setLevel(logging.DEBUG)
(4) streamhandler 객체 정의
    - StreamHandler = logging.StreamHandler()
    - StreamHandler.setFormatter(logFormatter)
    - logger.addHandler(StreamHandler)
'''
import logging
from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger  = logging.getLogger()

# 로그레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림(=터미널)
StreamHandler = logging.StreamHandler()
StreamHandler.setFormatter(logFormatter)
logger.addHandler(StreamHandler)

'''
◆ 파일로 로깅 남기기
1. filename 지정
2. filehandler 객체 지정 (이름,인코딩,포맷 전달)
3. logger.addHandler
'''
# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
filehandler = logging.FileHandler(filename,encoding="utf-8")
filehandler.setFormatter(logFormatter)
logger.addHandler(filehandler)

# 수행 => 터미널 & 파일 동시 진행
logger.debug("로그를 남겨보는 테스트를 진행합니다.")
logger.info("자동화 수행 준비")
logger.warning("경고 : 실행상에 문제가 있을 수 있습니다.")
logger.error("에러가 발생하였습니다. 에러코드는 ...")
logger.critical("복구가 불가능한 문제가 발생했습니다.")

