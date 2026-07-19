import streamlit as st

def prediction_page():

    st.title("🤖 Data Quality Prediction")

    if st.session_state.df is None:
        st.warning("Please upload a dataset first.")
        return

    quality_score = st.session_state.get("quality_score", 0)

    if quality_score >= 90:
        prediction = "🟢 Excellent"
    elif quality_score >= 75:
        prediction = "🟡 Good"
    elif quality_score >= 50:
        prediction = "🟠 Average"


    else:
        prediction = "🔴 Poor"



    st.metric("Quality Score", f"{quality_score}%")

    st.success(f"Predicted Data Quality: {prediction}")

    st.progress(quality_score / 100)