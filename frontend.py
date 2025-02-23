import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="GitHub Profile Stats", page_icon="🐙", layout="centered")

st.title("🐙 GitHub Profile Stats")

username = st.text_input("Enter GitHub Username")

if st.button("Get Stats"):
    if username:
        api_url = f"http://127.0.0.1:5000/github-stats?username={username}"  # Backend URL
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            st.image(data["avatar_url"], width=150)
            st.subheader(data["name"] if data["name"] else "No Name Available")
            st.write(f"📍 **Location:** {data['location'] if data['location'] else 'Unknown'}")
            st.write(f"📖 **Bio:** {data['bio'] if data['bio'] else 'No bio available'}")
            st.write(f"📂 **Public Repos:** {data['public_repos']}")
            st.write(f"👥 **Followers:** {data['followers']}  |  🏃 **Following:** {data['following']}")
        else:
            st.error("User not found! Please enter a valid username.")
    else:
        st.warning("Please enter a username.")

