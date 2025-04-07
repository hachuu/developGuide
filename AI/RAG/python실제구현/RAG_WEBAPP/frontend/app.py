# frontend/app.py
import streamlit as st
import requests

st.title("👶 은수의 하루 루틴 Q&A")

question = st.text_input("📌 궁금한 점을 입력하세요:")

if st.button("질문하기") and question:
    with st.spinner("답변 생성 중..."):
        try:
            response = requests.post(
                "http://localhost:8000/api/ask",
                json={"question": question},
                timeout=15
            )
            if response.status_code == 200:
                answer = response.json().get("answer", "❌ 응답 없음")
                st.success(f"✅ 답변:\n\n{answer}")
            else:
                st.error(f"서버 오류: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"요청 실패: {e}")
