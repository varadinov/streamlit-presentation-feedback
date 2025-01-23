import streamlit as st
from utils.feedback_service import FeedBackService


def comments(feedback_service: FeedBackService):
    st.title("Comments")
    feedbacks = [f for f in feedback_service.read() if f['q6']]

    st.write(f'Total feedbacks that provide additional comments: {len(feedbacks)}')
    for feedback in feedbacks:
        with st.container(border=1):
            if feedback['q6']:
                st.write(feedback['q6'])
