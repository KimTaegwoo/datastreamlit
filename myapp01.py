import streamlit as st
import pandas as pd
from datetime import datetime

# print('hello')  -> 이건 터미널에 나온다.

# ---- 글자 크기

st.title('이것은 타이틀입니다.')
st.header('이것은 헤더 입니다.')
st.subheader('이것은 서브헤더 입니다.')


# ----- 데이터프레임 -----
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)


st.markdown('### ----- df.describe() -----')
st.write(df.describe())



var1 = '저장'
var2 = '조회'

# st.button(var1)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

if st.button(var1):
    var1 = var2
    st.text(var1)

# ----- st.download_button
    # -- @st.cache 데코레이터
    #  Streamlit은 해당 함수가 이전과 같은 입력과 함께 
    #  호출된 적이 있는지 확인합니다. 
    #  이전에 호출되었다면, Streamlit은 함수의 출력을 캐시에서 읽어옵니다. 
    #  그렇지 않다면 함수를 실행하고 결과를 캐시에 저장하고 결과를 반환함

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
    )

# ----- checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write('Not selected!')

# ----- radio

genre = st.radio (
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
    )

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")


# ----- selectbox

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# ----- multiselect()

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)\


# ----- slide

age = st.slider('나이는', 0, 130, 25)
st.write("내 나이는 ", age, '살 이어요.')

  # -----here's an example of a range slider:
values = st.slider(
    '사이의 값을 고르세요',
    0.0, 100.0, (25.0, 75.0))
st.write('선택한 값은:', values)

  # ----- This is a range time slider:

from datetime import time
appointment = st.slider(
    "약속시간:",
    value=(time(11, 30), time(12, 45)))
st.write("당신의 스케쥴은:", appointment)

  # ----- Finally, a datetime slider:

from datetime import datetime
start_time = st.slider(
    "언제 떠날래?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("출발시간:", start_time)


# --- text_input: 텍스트 데이터를 입력하고 싶은 경우

title = st.text_input('영화제목', 'Life of Brian')
st.write('The current movie title is: ', title)

# --- text_input: 텍스트 데이터를 암호로 사용하고 싶은 경우엔 type=”password” 인자를 추가

st_text = st.text_input('비번', '1234', type="password")
st.write('st.text_input is: ', st_text)

# ----- 숫자 데이터를 입력하고 싶은 경우

st_number = st.number_input('숫자만 입력하세요', 1234)
st.write('st.number_input is: ', st_number)


# ----- 여러 줄의 텍스트 데이터를 입력하고 싶은 경우

st.text_area('여러 줄의 텍스트 데이터를 입력: ', '무궁화 꽃이\n 피었습니다.')


# ----- 날짜를 입력하고 싶은 경우

# st.date_input ('날짜를 입력: ', datetime.date(2019, 7, 6))

my_date = datetime.date(2021, 3, 2)
print( '---> ', my_date)

d = st.date_input('날짜를 입력하세요', my_date)
st.write('날짜: ', d)


# ----- 시간을 입력하고 싶은 경우

t = st.time_input('시간 입력: ')
st.write('시간: ', t)
print(type(t))


# ----- 색깔 입력

c = st.color_picker('색깔:')
st.write('색깔: ', c)
print('색깔: ', type(c))

