import pandas as pd
import random
import streamlit as st


def check():
    inp = st.session_state.inp
    i = st.session_state.i
    if st.session_state.q_list[i][2]==inp:
      st.session_state.point += 10
      st.header("正解")
    else :
      st.header("不正解")
    st.session_state.i += 1
    if st.session_state.i ==10:
     st.subheader(f"{st.session_state.point}点")
     st.session_state.i = 0
     st.session_state.point = 0
     st.button("もう一度",on_click=ask)
    else:
      st.button("次の問題",on_click=ask)

def ask():
  lis=st.session_state.lis
  if st.session_state.i == 0:
    st.session_state.q_list = q_list =  random.sample(lis,k=10)
  else:
    q_list = st.session_state.q_list
  i = st.session_state.i
  st.subheader(q_list[i][1],"("+q_list[i][0]+")")
  st.image(q_list[i][3],width=200)

  I = [4,5,6,7]
  rud = random.sample(I,k=4)

  with st.form(key="my_form"):
        st.radio("選択してください",[q_list[i][rud[0]],q_list[i][rud[1]],q_list[i][rud[2]],q_list[i][rud[3]]],key="inp")
        submit_button = st.form_submit_button(label="決定",on_click=check)

if not "idx" in st.session_state:
  df=pd.read_excel('アニメリサーチ.xlsx',sheet_name='シート1')
  st.session_state.lis=df.values.tolist()
  st.session_state.idx = 0
  st.session_state.point = 0
  st.session_state.i = 0
  st.title('アニメクイズ')
  ask() 

