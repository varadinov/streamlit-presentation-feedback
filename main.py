import streamlit as st
from utils.github_oauth2 import github_oauth2
from views.feedback import feedback
from views.statistics import statistics
from views.comments import comments
from dotenv import load_dotenv
from functools import partial
from config import config
from services import feedback_service
load_dotenv()

if "email" not in st.session_state:
    with st.spinner():
        github_oauth2(config['OAUTH2_CLIENT_ID'], config['OAUTH2_CLIENT_SECRET'], config['OAUTH2_REDIRECT_URI'])
else:
    pages = [
        st.Page(partial(feedback, st.session_state['email'], st.session_state['user_data']['name'], feedback_service),  url_path= "feedback", title="Feedback"),
        st.Page(partial(statistics, feedback_service), url_path= "statistics", title="Statistics"),
        st.Page(partial(comments, feedback_service), url_path= "comments", title="Comments"),
    ]
    pg = st.navigation(pages)
    st.logo('images/logo.png', size='large')
    st.sidebar.write(f"Welcome: {st.session_state['user_data']['name']}")

    with st.spinner():
        pg.run()

