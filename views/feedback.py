import streamlit as st

from utils.feedback_service import FeedBackService

def on_click_submit():
    st.session_state['disable_submit_button'] = True

def feedback(email: str, name: str, feedback_service: FeedBackService):
    st.title("Presentation Feedback Form")
    user = next(iter(feedback_service.read({'email': email})), None)
    if user:
        st.info('You already provided feedback!')
    else:
        with st.form(key="feedback_form"):
            st.subheader("Please fill out the form below to provide your feedback.")
                        
            # Feedback position
            positions = ["Software Developer", "Quality Assurance Engineer", "Data science", "Data engineer", 
                         "Database Administrator", "Systems Administrator", "Network Administrator", "Cloud Engineer", 
                         "Cybersecurity Specialist", "Support Specialist", "Manager", "Director", "Student"]
            
            position = st.selectbox("Your Position/Occupation", options=positions)
            
            # Feedback questions
            st.subheader("Rate the following aspects from 1 (low) to 10 (high):")
            q1 = st.slider("Will you consider using Streamlit in the future?", 1, 10, 5)
            q2 = st.slider("How would you rate the presentation content?", 1, 10, 5)
            q3 = st.slider("Were the demos sufficient?", 1, 10, 5)
            q4 = st.slider("How would you rate the trainer?", 1, 10, 5)
            q5 = st.slider("Would you like more similar presentations in the future?", 1, 10, 5)
            q6 = st.text_area("Please provide any additional comments or notes")
            
            # Submit button
            with st.spinner('Processing:'):
                submit_button = st.form_submit_button(label="Submit Feedback", 
                                                      on_click=on_click_submit, 
                                                      disabled=st.session_state.get('disable_submit_button', False))
                
                if submit_button:
                    feedback_service.create({
                        'email': email,
                        'name': name,
                        'position': position,
                        'q1': q1,
                        'q2': q2,
                        'q3': q3,
                        'q4': q4,
                        'q5': q5,
                        'q6': q6
                    })
                    st.session_state['feedback_required'] = False
                    st.success('Thank you for your feedback!')
                        
                    
                
            
        