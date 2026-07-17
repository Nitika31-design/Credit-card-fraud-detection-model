import streamlit as st
import joblib
import numpy as np
import time

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="💳",
    layout="wide"
)


# ---------------- LOAD MODEL ----------------

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Animated Background */

.stApp{
background:linear-gradient(
-45deg,
#667eea,
#764ba2,
#43cea2,
#185a9d
);

background-size:400% 400%;
animation:bg 12s ease infinite;
}


@keyframes bg{

0%{
background-position:0% 50%;
}

50%{
background-position:100% 50%;
}

100%{
background-position:0% 50%;
}

}


/* Title */

.title{

font-size:55px;
font-weight:900;
text-align:center;
color:white;
animation:float 3s infinite;

}


@keyframes float{

50%{
transform:translateY(-15px);
}

}


.subtitle{

text-align:center;
font-size:22px;
color:white;
margin-bottom:30px;

}



/* Glass Card */

[data-testid="stVerticalBlock"]{

background:rgba(255,255,255,0.18);

border-radius:25px;

padding:25px;

backdrop-filter:blur(20px);

box-shadow:0px 10px 40px rgba(0,0,0,0.2);

}



/* Button */

.stButton button{

height:65px;

width:100%;

border-radius:20px;

font-size:25px;

font-weight:bold;

background:
linear-gradient(
45deg,
#ff512f,
#dd2476
);

color:white;

border:none;

transition:0.5s;

}


.stButton button:hover{

transform:scale(1.08);

box-shadow:
0px 0px 30px #ff416c;

}



/* Success Animation */


.success{

background:#00c853;

padding:25px;

border-radius:20px;

text-align:center;

font-size:30px;

color:white;

animation:pulse 1.5s infinite;

}


.danger{

background:#d50000;

padding:25px;

border-radius:20px;

text-align:center;

font-size:30px;

color:white;

animation:pulse 1.5s infinite;

}


@keyframes pulse{

50%{

transform:scale(1.05);

}

}


/* Footer */

.footer{

text-align:center;

color:white;

font-size:18px;

margin-top:40px;

}


</style>

""",unsafe_allow_html=True)



# ---------------- HEADER ----------------


st.markdown(
"""
<div class="title">
💳  Credit Card Fraud Detection
</div>

<div class="subtitle">
🔐 Smart Machine Learning Based Transaction Security System
</div>

""",
unsafe_allow_html=True
)



# ---------------- INPUT SECTION ----------------


col1,col2=st.columns(2)



with col1:


    st.subheader("💰 Transaction Details")

    amount=st.number_input(
        "Transaction Amount",
        0.0,
        100000.0,
        500.0
    )


    hour=st.slider(
        "Transaction Hour",
        0,
        23,
        12
    )


    merchant=st.selectbox(
        "Merchant Category",
        [
        "Food",
        "Shopping",
        "Travel",
        "Electronics",
        "Entertainment",
        "Health"
        ]
    )


    age=st.number_input(
        "Customer Age",
        18,
        100,
        30
    )


    previous=st.number_input(
        "Previous Transactions",
        0,
        1000,
        5
    )




with col2:


    st.subheader("🌐 Security Information")


    international=st.selectbox(
        "International Transaction",
        ["No","Yes"]
    )


    distance=st.number_input(
        "Distance From Home KM",
        0.0,
        500.0,
        5.0
    )


    card_present=st.selectbox(
        "Card Present",
        ["Yes","No"]
    )


    transaction_type=st.selectbox(
        "Transaction Type",
        [
        "POS",
        "Online",
        "ATM"
        ]
    )



# ---------------- ENCODING ----------------


merchant_map={
"Food":0,
"Shopping":1,
"Travel":2,
"Electronics":3,
"Entertainment":4,
"Health":5
}


international_map={
"No":0,
"Yes":1
}


card_map={
"Yes":1,
"No":0
}


transaction_map={
"POS":0,
"Online":1,
"ATM":2
}



features=np.array([[

amount,

hour,

merchant_map[merchant],

age,

previous,

international_map[international],

distance,

card_map[card_present],

transaction_map[transaction_type]

]])



# ---------------- PREDICTION ----------------


st.write("")

if st.button("🚀 CHECK TRANSACTION"):


    with st.spinner("🤖 AI is analyzing transaction..."):

        time.sleep(2)


        data=scaler.transform(features)

        prediction=model.predict(data)[0]



    st.divider()


    if hasattr(model,"predict_proba"):

        probability=model.predict_proba(data)[0]

        safe=probability[0]*100

        fraud=probability[1]*100


    else:

        safe=0
        fraud=0



    if prediction==1:


        st.markdown(

        """

        <div class="danger">

        🚨 FRAUD TRANSACTION DETECTED

        </div>

        """,

        unsafe_allow_html=True

        )


        if fraud:

            st.progress(fraud/100)

            st.metric(
                "Fraud Risk",
                f"{fraud:.2f}%"
            )


    else:


        st.markdown(

        """

        <div class="success">

        ✅ TRANSACTION IS SAFE

        </div>

        """,

        unsafe_allow_html=True

        )


        if safe:

            st.progress(safe/100)

            st.metric(
                "Safety Score",
                f"{safe:.2f}%"
            )



# ---------------- FOOTER ----------------


st.markdown(

"""

<div class="footer">

🚀 Developed by Nitika using Python | Machine Learning | Streamlit

</div>

""",

unsafe_allow_html=True

)