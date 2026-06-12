import streamlit as st

from src.components.footer import footer_dashboard
from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout
)
from src.components.header import header_dashboard


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    # Initialize session state
    if "teacher_login_type" not in st.session_state:
        st.session_state.teacher_login_type = "login"

    # Show page based on state
    if st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_screen_login():
    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge"
    )

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go Back to Home",
            type="secondary",
            key="teacher_back_home_login"
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login with Password")

    st.write("")

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="Enter your username",
        key="teacher_login_username"
    )

    teacher_pass = st.text_input(
        "Enter Password",
        placeholder="Enter your password",
        type="password",
        key="teacher_login_password"
    )

    st.divider()

    btn1, btn2 = st.columns(2)

    with btn1:
        if st.button(
            "Login",
            icon=":material/passkey:",
            type="primary",
            key="teacher_login_btn"
        ):
            # Login logic here
            st.success(f"Welcome {teacher_username}")

    with btn2:
        if st.button(
            "Register Instead",
            icon=":material/app_registration:",
            type="secondary",
            key="teacher_register_switch_btn"
        ):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()


def teacher_screen_register():
    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge"
    )

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go Back to Home",
            type="secondary",
            key="teacher_back_home_register"
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Register Your Teacher Profile")

    st.write("")

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="Enter your username",
        key="register_username"
    )

    teacher_name = st.text_input(
        "Enter Full Name",
        placeholder="Enter your full name",
        key="register_name"
    )

    teacher_pass = st.text_input(
        "Enter Password",
        placeholder="Enter your password",
        type="password",
        key="register_password"
    )

    teacher_pass_confirm = st.text_input(
        "Confirm Password",
        placeholder="Confirm your password",
        type="password",
        key="register_confirm_password"
    )

    st.divider()

    btn1, btn2 = st.columns(2)

    with btn1:
        if st.button(
            "Login Instead",
            icon=":material/passkey:",
            type="primary",
            key="register_to_login_btn"
        ):
            st.session_state.teacher_login_type = "login"
            st.rerun()

    with btn2:
        if st.button(
            "Register Now",
            icon=":material/app_registration:",
            type="secondary",
            key="register_now_btn"
        ):

            if not teacher_username:
                st.error("Username is required.")

            elif not teacher_name:
                st.error("Full name is required.")

            elif not teacher_pass:
                st.error("Password is required.")

            elif teacher_pass != teacher_pass_confirm:
                st.error("Passwords do not match.")

            else:
                # Registration logic here
                st.success("Teacher registered successfully!")

    footer_dashboard()