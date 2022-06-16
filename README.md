# flask-webapp

해당 부분은 Python과 spotify api를 활용한 가벼운 ML이 포함된 웹 앱 구축 프로젝트입니다.\
ML은 음악 스타일의 이진 분류를 위한 RandomForestClassifier를 채택했습니다.\
웹 앱 구축을 위하여 Flask, SQLite 등을 사용했습니다.

spotify api를 통하여 이진 분류를 위한 Upbeat, Chillout 플레이리스트 내 음악 리스트와,\
나의 최근 들은 음악의 데이터를 가져왔습니다.

Python Files\
__init__ : Flask를 run하는 python 파일입니다. db를 쿼리를 통해 호출하고, html과 함께 시각화합니다. \
__RFClassifier__ : 랜덤포레스트 이진분류로 pickle 모델을 생성하는 부분입니다. 미리 선별하여 만들어진 플레이리스트 내 음악들이 있는 sample.json을 활용합니다.\
__recent_music__ : 최근 들었던 음악을 가져와 db에 저장하는 함수입니다. 해당 과정에서 RFClassifier를 통하여 만들어진 pickle모델을 통해 분류 예측값이 함께 저장됩니다.\
__practice__ : 연습장입니다.

현재 db 재구성과 개선점 추가를 진행 중에 있습니다.
