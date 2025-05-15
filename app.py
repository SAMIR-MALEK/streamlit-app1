
import streamlit as st

st.title("نموذج تفاعلي حسب الإجابة")

answer = st.text_input("هل ترغب في المتابعة؟ (أدخل 'نعم' أو 'لا')")

if answer.strip().lower() == "نعم":
    st.success("أهلاً بك في القسم الثاني ✅")
    st.write("هذا محتوى القسم الثاني الخاص بالمتابعة.")
elif answer.strip().lower() == "لا":
    st.warning("تم تحويلك إلى قسم التوقف ⛔")
    st.write("هذا محتوى القسم الثالث.")
elif answer:
    st.error("الرجاء إدخال 'نعم' أو 'لا' فقط.")
