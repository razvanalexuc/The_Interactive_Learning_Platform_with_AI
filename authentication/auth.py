from streamlit_login_auth_ui.widgets import __login__
import streamlit as st
from constants import COURIER_AUTH_TOKEN

def check_login():
    if 'login' not in st.session_state:
        st.session_state.login = False

    __login__obj = __login__(
        auth_token=COURIER_AUTH_TOKEN,
        company_name="Razvan Alexuc",
        width=200,
        height=250,
        logout_button_name="Logout",
        hide_menu_bool=False,
        hide_footer_bool=False,
        lottie_url="https://lottie.host/ed21a0be-6971-4e95-a65c-895010ddf209/uCReZBSbWe.json",
    )

    st.session_state.login = __login__obj.build_login_ui()  

    if st.session_state.login:
        st.markdown("Bun venit pe pagina principala, ")
        fetched_cookies = __login__obj.cookies
        if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
            username = fetched_cookies['__streamlit_login_signup_ui_username__']
            st.write(username)

    return st.session_state.login 