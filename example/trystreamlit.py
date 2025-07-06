#!/usr/bin/env python

import streamlit as st
import jwt
import time


def main():
    st.title("Demo Streamlit")
    debug_mode: bool = True

    # example from doc
    st.subheader("Slider Example")
    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)

    # example from online
    st.subheader("Columns")
    col1, col2, col3 = st.columns(3)
    with col2:
        instagram = st.checkbox("Instagram")
    with col1:
        linkedin = st.checkbox("Linkedin")
    with col3:
        twitter = st.checkbox("Twitter")
        st.text_input("Test string", placeholder="Write something here")
        st.caption("explain the above text")

    # test on jwt using slider
    st.subheader("Add a secret message sample")
    mymsg = st.text_area("Add jwt message:", value="123", placeholder="{'message': 'this is a quick message to encode'}")
    try:
        encoded_string = jwt.encode({'message': mymsg}, f"secret{x}",  algorithm="HS256")

        with st.spinner("Please wait ..."):
            time.sleep(1)

        my_bar = st.progress(0, text="Encrypting")
        for i in range(1,101,21):
            my_bar.progress(i)
            time.sleep(0.5)
        my_bar.progress(100)

        st.divider()
        st.badge("Encoded",color="red")
        st.code(encoded_string)
        decoded_string: dict[str,str] = jwt.decode(encoded_string, "secret" + str(x), algorithms=["HS256"])

        st.divider()
        st.badge("Decoded", color="green")
        st.code(str(decoded_string))

        st.divider()
        st.badge("Return string", color="orange")
        st.codeb(decoded_string.get("message", "empty message"))

    except Exception as e:
        st.divider()
        st.subheader("🔥 Error occurred")
        st.write("Sorry for inconvenience but we are experiencing some technical difficulties. Please try again later")
        if debug_mode:
            st.exception(e)


if __name__ == "__main__":
    main()
