import streamlit as st
import streamlit.ReportThread as ReportThread
from streamlit.server.Server import Server

radioButton = st.sidebar.radio("Go to",['Home', 'Page One'])

def get_session():
    ctx = ReportThread.get_report_ctx().session_id
    this_session = None
    current_session = Server.get_current()._get_session_info(ctx)
    this_session = current_session.session
    st.write("ch",current_session.session)

    if current_session is None:
        raise RuntimeError(
            "Oh noes. Couldn't get your Streamlit Session object"
            'Are you doing something fancy with threads?')

    return this_session

def get_state(hash_funcs=None):
    session = get_session()
    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = SessionState(session, hash_funcs)

    return session._custom_session_state

class SessionState:
    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

def main():
    state = get_state()
    if radioButton == "Home":
        st.write("Home")
        state.slider = st.slider('How old are you?', 0, 130, state.slider)
    else:
        st.write("Page One")

main()