
imort streamlit as st
st.title("list")
n=st.number_input("enter a how many iteam do you have&quot")
for i in range(0,n):
    
    a=st.text_input(&quot;enter a iteam&quot;)
    st.write(a)