import streamlit as st
from db import restio_client

def comments():
    st.title("Comments")
    feedbacks = [f for f in restio_client.read_all() if f['q6']]

    st.write(f'Total feedbacks that provide additional comments: {len(feedbacks)}')
    for feedback in feedbacks:
        with st.container(border=1):
            if feedback['q6']:
                st.write(feedback['q6'])
