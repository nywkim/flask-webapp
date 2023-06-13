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

your study.\nFeel free to contact

<table>
<tbody><tr>
<td colspan="13" rowspan="1">
<p>
Schedule 1

</p>
</td>
</tr>
<tr>
<td colspan="13" rowspan="1">
<p>
ALTRIA GROUP, INC.

</p>
<p>
and Subsidiaries

</p>
<p>
Reconciliation of GAAP and non-GAAP Measures

</p>
<p>
(dollars in millions, except per share data)

</p>
<p>
(Unaudited)

</p>
</td>
</tr>
<tr>
<td colspan="13" rowspan="1"></td>
</tr>
<tr>
<td colspan="13" rowspan="1">
<p>
<b>Reconciliation of Altria’s Full-Year 2022 Adjusted Results</b>
</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="3" rowspan="1">
<p>
<b>Earnings before Income Taxes</b>
</p>
</td>
<td colspan="3" rowspan="1">
<p>
<b>Provision for Income Taxes</b>
</p>
</td>
<td colspan="3" rowspan="1">
<p>
<b>Net Earnings</b>
</p>
</td>
<td colspan="3" rowspan="1">
<p>
<b>Diluted EPS</b>
</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
<b>2022 Reported</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>7,389</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>1,625</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>5,764</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>3.19</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
NPM Adjustment Items

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
(68

</p>
</td>
<td colspan="1" rowspan="1">
<p>
)

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
(17

</p>
</td>
<td colspan="1" rowspan="1">
<p>
)

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
(51

</p>
</td>
<td colspan="1" rowspan="1">
<p>
)

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
(0.03

</p>
</td>
<td colspan="1" rowspan="1">
<p>
)

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
Acquisition and disposition-related items

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
11

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
2

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
9

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
—

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
Tobacco and health and certain other litigation items

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
131

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
33

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
98

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
0.05

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
JUUL changes in fair value

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
1,455

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
—

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
1,455

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
0.81

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
ABI-related special items

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
2,544

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
534

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
2,010

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
1.12

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
Cronos-related special items

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
186

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
—

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
186

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
0.10

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
Income tax items

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
—

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
729

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
(729

</p>
</td>
<td colspan="1" rowspan="1">
<p>
)

</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
(0.40

</p>
</td>
<td colspan="1" rowspan="1">
<p>
)

</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>
<b>2022 Adjusted for Special Items</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>11,648</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>2,906</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>8,742</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>$</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
<b>4.84</b>
</p>
</td>
<td colspan="1" rowspan="1">
<p>
 

</p>
</td>
</tr>
</tbody></table>
