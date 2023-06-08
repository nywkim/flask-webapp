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

<table style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; border-collapse: collapse; width:100%; border-collapse:collapse ;">
<tbody><tr>
<td rowspan="2" style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">
<strong>Subject #</strong><br>
</td>
<td rowspan="2" style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">
<strong>Age</strong><br>
</td>
<td rowspan="2" style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">
<strong>Prior Therapy /</strong><br><strong># of Prior Lines</strong><br>
</td>
<td colspan="2" style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; "><strong>SES-CD</strong></td>
<td colspan="2" style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; "><strong>LIGHT pg/mL</strong></td>
<td rowspan="2" style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">
<strong>Response</strong><br>
</td>
</tr>
<tr>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; "><strong>Baseline</strong></td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; "><strong>8 Weeks</strong></td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; "><strong>Baseline</strong></td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; "><strong>8 Weeks</strong></td>
</tr>
<tr>
<td style="max-width:10%; width:10%; min-width:10%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: justify ;  vertical-align: middle; vertical-align: middle ; ">Subject #1</td>
<td style="max-width:5%; width:5%; min-width:5%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">42</td>
<td style="max-width:20%; width:20%; min-width:20%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">Remicade, Entyvio, <br>Stelara</td>
<td style="max-width:8%; width:8%; min-width:8%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">11</td>
<td style="max-width:8%; width:8%; min-width:8%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">4</td>
<td style="max-width:8%; width:8%; min-width:8%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">455</td>
<td style="max-width:8%; width:8%; min-width:8%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">24</td>
<td style="max-width:33%; width:33%; min-width:33%;;border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; vertical-align: middle ; ">Significant mucosal healing: <ul>
<li>64% reduction in SES-CD score (moderate to mild)</li>
<li>Patient relapsed post treatment and needed surgery<br>
</li>
</ul> </td>
</tr>
<tr>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: justify ;  vertical-align: middle; vertical-align: middle ; ">Subject #2</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">63</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">Remicade, Humira, Entyvio, <br>Stelara<br>
</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">18</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">19</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">193</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">29</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; vertical-align: middle ; ">No evidence of improvement<br>
</td>
</tr>
<tr>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: justify ;  vertical-align: middle; vertical-align: middle ; ">Subject #3</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">28</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">Remicade, Humira, <br>Stelara, Methotrexate</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">21</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">15</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">75</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">27</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; vertical-align: middle ; ">Significant mucosal healing: <ul type="disc">
<li>29% reduction in SES-CD score (severe to moderate)</li>
<li>Exploring single-patient IND<br>
</li>
</ul> </td>
</tr>
<tr>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: justify ;  vertical-align: middle; vertical-align: middle ; ">Subject #4</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">49</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">Remicade, Stelara, <br>Humira, Entyvio, Methotrexate, Mercaptopurine<br>
</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">12</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">3</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">162</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; text-align: center ;  vertical-align: middle; vertical-align: middle ; ">45</td>
<td style="border-top: solid black 1pt ; border-right: solid black 1pt ; border-bottom: solid black 1pt ; border-left: solid black 1pt ; vertical-align: middle ; ">Significant mucosal healing: <ul type="disc">
<li>75% reduction in SES-CD score (moderate to mild)</li>
<li>Exploring single-patient IND</li>
</ul> </td>
</tr>
</tbody></table>

<table border="1" cellpadding="0" cellspacing="0" style="BORDER-COLLAPSE: COLLAPSE; BORDER-TOP:1pt black; BORDER-RIGHT:1pt black; BORDER-BOTTOM:1pt black; BORDER-LEFT:1pt black ;"><tr><td colspan="1" rowspan="1" style>
<p style><span style>Outcome measure</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>AYVAKIT</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>Placebo</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>p-value</span></p>
</td>
</tr><tr><td colspan="1" rowspan="1" style>
<p style><span style>Proportion with ≥50% reduction in serum tryptase</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>53.9 %</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>0 %</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>p&lt;0.0001</span></p>
</td>
</tr><tr><td colspan="1" rowspan="1" style>
<p style><span style>Proportion with ≥50% reduction in KIT D816V variant allele fraction</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>67.8 %</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>6.3 %</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>p&lt;0.0001</span></p>
</td>
</tr><tr><td colspan="1" rowspan="1" style>
<p style><span style>Proportion with ≥50% reduction in bone marrow mast cell aggregates</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>52.8 %</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>22.8 %</span></p>
</td>
<td colspan="1" rowspan="1" style>
<p style><span style>p&lt;0.0001</span></p>
</td>
</tr></table>
