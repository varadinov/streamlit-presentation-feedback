import streamlit as st
import pandas as pd
from utils.feedback_service import FeedBackService

def statistics(feedback_service: FeedBackService):
    st.title("Statistics")
    feedbacks = feedback_service.read()
    
    st.subheader('Rating per position')
    feedbacks_df = pd.DataFrame(feedbacks)[['position', 'q1', 'q2', 'q3', 'q4', 'q5']]
    st.bar_chart(feedbacks_df.groupby("position").mean(numeric_only=True).T, stack=False)  
    st.markdown("""
                * **q1** - "Will you consider using Streamlit in the future?"
                * **q2** - "How would you rate the presentation content?"
                * **q3** - "Were the demos sufficient?"
                * **q4** - "How would you rate the trainer?"
                * **q5** - "Would you like more similar presentations in the future?"
                """)
    
    st.subheader('Participants count per position')
    participants = feedbacks_df.groupby("position").size()
    # Convert to a DataFrame (optional, for a tabular format)
    participants_df = participants.reset_index(name="participants").set_index('position').T
    st.bar_chart(participants_df, stack=False)  
