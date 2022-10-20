import streamlit as st
import requests


st.set_page_config(page_title="اخبار ورزشی",page_icon="https://myket.ir/app-icon/ir.gharivand.breakingnews_6266d09a-0c19-46c3-ae5b-edf65278623e.png")
st.title("اخبار ورزشی")
st.image("https://myket.ir/app-icon/ir.gharivand.breakingnews_6266d09a-0c19-46c3-ae5b-edf65278623e.png")

text = st.text_input(" اخبار کدام تیم رو دنبال میکنید ؟")

hide= """
<style>

.block-container {direction : rtl}

#MainMenu {visibility : hidden;}
footer {visibility : hidden;}

</styles>
"""

st.markdown(hide ,unsafe_allow_html=True)

r = requests.get(f'https://search-api.varzesh3.com/v1.0/query?q={text}')

x= r.json()


for i in x['news'] :
    st.subheader(i['title'])
    st.success(i['persianPublishedOn'])
    st.image(i['picture'])
    st.write(i['shortDescription'])
    st.write('--------')


st.warning("طراح و برنامه نویس : عبدالله چلاسی")
