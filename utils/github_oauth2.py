import requests
import streamlit as st
from streamlit_oauth import OAuth2Component


def github_oauth2(client_id: str, client_secret: str,  redirect_uri: str):
    authorize_endpoint = "https://github.com/login/oauth/authorize"
    token_endpoint = "https://github.com/login/oauth/access_token"
    api_endpoint =  "https://api.github.com"
    
    st.title("Feedback Application")
    st.write("This is a demo feedback application for the Sofia Python MeetUp")
    # Create an OAuth2Component instance
    oauth2 = OAuth2Component(client_id, client_secret, authorize_endpoint, token_endpoint)
    result = oauth2.authorize_button(
        name="Login with GitHub",
        icon="https://github.githubassets.com/favicons/favicon.png",
        redirect_uri=redirect_uri,
        scope="user:email",  # Scope to access user's email
        key="github_login",
        extras_params={"allow_signup": "true"},
        use_container_width=True,
    )
    
    if result:
        # Use the access token to fetch the user's GitHub profile
        access_token = result["token"]["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        user_response = requests.get(f"{api_endpoint}/user", headers=headers)
        if user_response.status_code == 200:
            user_data = user_response.json()
            st.session_state["user_data"] = user_data

        # Fetch emails
        email_response = requests.get(f"{api_endpoint}/user/emails", headers=headers)
        if email_response.status_code == 200:
            emails = email_response.json()
            primary_email = next((email['email'] for email in emails if email['primary']), "No primary email found")
            st.session_state["email"] = primary_email
            st.rerun()

        else:
            st.error("Failed to fetch email information. Please try again.")