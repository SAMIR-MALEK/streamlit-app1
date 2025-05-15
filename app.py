import streamlit as st
import os
from datetime import datetime

# قائمة الرموز الصالحة (كلمة السر) المرتبطة بالمذكرات
valid_codes = {
    "CODE123": "مذكرة الطالب أحمد",
    "XYZ789": "مذكرة الطالبة سارة"
}

st.title("إيداع مذكرة التخرج")

code = st.text_input("أدخل كلمة السر الخاصة بالمذكرة:")

if code:
    if code in valid_codes:
        st.success(f"الكود صحيح: {valid_codes[code]}. يمكنك رفع ملف المذكرة الآن.")
        
        uploaded_file = st.file_uploader("اختر ملف المذكرة (PDF)", type=["pdf"])
        
        if uploaded_file is not None:
            save_dir = "uploaded_theses"
            os.makedirs(save_dir, exist_ok=True)
            
            filename = f"{code}_{uploaded_file.name}"
            save_path = os.path.join(save_dir, filename)
            
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            deposit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success(f"تم رفع المذكرة بنجاح بتاريخ {deposit_date}. شكراً لك.")
            
    else:
        st.error("كلمة السر غير صحيحة، يرجى المحاولة مرة أخرى.")
