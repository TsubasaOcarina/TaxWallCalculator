import pandas as pd
import altair as alt
import streamlit as st

st.title('103万の壁')

# 103万のボーダー
border = 1030000

#１日勤務時間
day_worktime = 5

#何月
month = 4

# 合計額
income_sum = 0

salary_per_hour = st.number_input('時給', min_value=0.0, max_value=10000000.0, value=1000.0, step=100.0)
day_worktime = st.number_input('1日の勤務時間', min_value=0.0, max_value=24.0, value=4.0)
month = st.number_input('何月', value=9)
income = st.number_input('今月の収入を教えてください', min_value=0, max_value=10000000)


# 残り働ける時間を計算
can_work = (border - income) / salary_per_hour
border -= income

st.write(f'残り {can_work} 時間働くことが出来ます')