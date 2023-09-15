#  Required Libraries
import pandas as pd
import streamlit as st
import psycopg2 as pg2
import sqlalchemy as sql
from streamlit_option_menu import *
from streamlit_extras import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import pymongo as pm
import time
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


st.set_page_config(page_title='Diabetes Prediction By Praveen', layout="wide")

# POSTGRESQL CONNECTIVITY
praveen = pg2.connect(host='localhost', user='postgres', password='root', database='sugarsenseai')
cursor = praveen.cursor()

praveen_1 = pm.MongoClient(
    'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
db = praveen_1['Feedback_SugarSenseAI']
collection = db['comment']

class Diabetes_prediction:

    def process(self):
        predict_data = []
        with st.sidebar:
            selected = option_menu(
                menu_title="SugarSense AI Project",
                options=['Intro', "ML Process", 'Feedback'],
                icons=['mic-fill', 'person-square', 'chat-heart-fill'],
                menu_icon='alexa',
                default_index=0,
            )
        if selected == 'Intro':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            # Start Intro
            col1, col2 = st.columns([7, 3])
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color: cyan;'>Howdy ,</span> <span style='color: white;'> I am Praveen</span> </h1>",
                    unsafe_allow_html=True)

                title_text = "<h1 style='color:cyan; font-size: 60px;'>A Data Science Aspirant From India</h1>"
                st.markdown(title_text, unsafe_allow_html=True)

                title_text = "<h6 style='color:white; font-size: 15px;'><span style='color: white;'>I am Detective who finding hidden pattern and insights from complex data to help for business decisions, hit </span><span style='color: cyan;'> 'P' </span><span style='color: white;'>on keyboard to know about me</span></h6>"
                st.markdown(title_text, unsafe_allow_html=True)
                # st.markdown(
                #     "<h1 style='font-size: 80px;'><span style='color: cyan;'>Lets</span> <span style='color: white;'>    Explore</span> </h1>",
                #     unsafe_allow_html=True)

                keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")

            with col2:
                file = lottie("cyan_boy_lap2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=500,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            # ______________________________________________________________ABOUT PROJECT______________________________________________________________________________________


            st.markdown("<h1 style='font-size: 60px;'><span style='color: white;'>About</span> <span style='color: cyan;'> SugarSense AI</span> </h1>",unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('hospital_symbok.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=570,
                    width=800,
                    key=None
                )
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([3, 8, 3])
            # with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>What Has Praveen Done in this project?</h1>"
            st.markdown(title_text, unsafe_allow_html=True)


            col1, col2, col3 = st.columns([3, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('boydoubtface.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=550,
                    width=700,
                    key=None
                )
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([5, 8, 3])
            # with col2:
            col2.markdown("<h1 style='font-size: 80px;'><span style='color: cyan;'>Lets</span> <span style='color: white;'>    Explore</span> </h1>",unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([3, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('down_arrow.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=700,
                    key=None
                )
            #___________________________________________________________________________PROBLEM Statement____________________________________________
            st.write("")
            st.write("")
            st.write("")

            st.markdown("<h1 style='font-size: 60px;'><span style='color: white;'>Problem</span> <span style='color: cyan;'> Statement</span> </h1>",unsafe_allow_html=True)

            col1, col2, col3 = st.columns([4, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.markdown("<h1 style='font-size: 50px;'></span> <span style='color: cyan;'>Patient</span><span style='color: white;'> Diabetes</span><span style='color:cyan;'> Prediction</span> </h1>",unsafe_allow_html=True)
            col1, col2, col3 = st.columns([3, 8, 3])
            with col2:
                file = lottie('problem_statement.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=570,
                    width=800,
                    key=None
                )
            # st.write("")
            # st.write("")
            # st.write("")
            #_______________________________________________________________________________________STEPS________________________________________________#
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([6, 8, 3])
            # with col2:
            col2.markdown(
                "<h1 style='font-size: 80px;'><span style='color: cyan;'>View </span> <span style='color: white;'>  Steps</span> </h1>",
                unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([3, 8, 3])
            with col2:
                file = lottie('down_arrow.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=700,
                    key=None
                )

            # _________________________________________________________Steps 1 __________________________________________________________

            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([3, 23, 3])

            col2.markdown( "<h1 style='font-size: 55px;'><span style='color:white;'>Get Data From </span> <span style='color:cyan;'> Praveen's </span><span style='color:white;'> Github Repository</span> </h1>",unsafe_allow_html=True)
            keyboard_to_url(key="d", url="https://github.com/praveendecode/Datasets/blob/main/Ml_dataset/SugarSense_AI.csv")
            col1, col2, col3 = st.columns([3, 8, 3])
            with col2:
                file = lottie('github.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=700,
                    key=None
                )
            # _________________________________________________________________________________Step 2_____________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([5.7, 23, 3])

            col2.markdown( "<h1 style='font-size: 55px;'><span style='color:white;'>Data</span> <span style='color:cyan;'> Exploration </span><span style='color:white;'>  and </span><span style='color:cyan;'>  Preprocessing</span> </h1>",unsafe_allow_html=True)


            col1,  col3 = st.columns([15, 15])
            # col2.write("")
            # col2.write("")
            with col1:
                file = lottie('dashboard_1.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=680,
                    width=600,
                    key=None
                )
            with col3:
                file = lottie('step2_1.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=680,
                    width=800,
                    key=None
                )
            col3.write("")
            col3.write("")

            # _______________________________________________________________________________step 3_____________________________________________________


            col1, col2, col3 = st.columns([7, 25, 3])

            col2.markdown( "<h1 style='font-size: 60px;'><span style='color:white;'>Model</span> <span style='color:cyan;'>Selection</span><span style='color:white;'>  and </span><span style='color:cyan;'> Training</span> </h1>",unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 10, 3])
            # col2.write("")
            # col2.write("")
            with col2:
                file = lottie('model_training.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=780,
                    key=None
                )
                # _______________________________________________________________________________step 4_____________________________________________________

            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([5, 25, 3])

            col2.markdown(
                "<h1 style='font-size: 65px;'><span style='color:white;'>Collect</span> <span style='color:cyan;'> Diabetes</span><span style='color:white;'> Data From User</span> </h1>",
                unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 10, 3])
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('diabetes_data_2.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            #___________________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([8, 25, 3])

            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color:white;'>Patient's </span> <span style='color:cyan;'> Diabetes</span><span style='color:white;'> Status</span> </h1>",
                unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 10, 3])
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('plus_medical.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=880,
                    key=None
                )

            # ____________________________________________________________step 5_____________________________________________________________

            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([3, 25, 3])

            col2.markdown(
                "<h1 style='font-size: 50px;'><span style='color:white;'>Finally Here </span> <span style='color:cyan;'> Praveen </span><span style='color:white;'> To Share His Work To You</span> </h1>",
                unsafe_allow_html=True)


            col1, col2, col3 = st.columns([3, 10, 2])

            with col2:
                file = lottie('code_explnation.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=1000,
                    key=None
                )
            colored_header(
                label="",
                description="",
                color_name="blue-green-70"
            )
        elif selected == 'ML Process':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)
            # Data Collection
            df = pd.read_csv('SugarSense_AI.csv')

            # Preprocessing
            enc = OrdinalEncoder()
            df["smoking_history"] = enc.fit_transform(df[["smoking_history"]])
            df["gender"] = enc.fit_transform(df[["gender"]])

            # Data Split
            x = df.drop("diabetes", axis=1)
            y = df["diabetes"]
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
            model = DecisionTreeClassifier().fit(x_train, y_train)

            # Patient Input
            col1,col2 ,col3 = st.columns([2,15,2])

            with col2:
               st.markdown( "<h1 style='font-size: 70px;'><span style='color: cyan;'>SugarSense AI </span> <span style='color: white;'>Data </span> <span style='color: cyan;'>Submission</span> </h1>",unsafe_allow_html=True)


               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")

               # ___________________________________________________________________________PROBLEM Statement____________________________________________

               # Gender

            col1 , col2, col3 = st.columns([4,15, 5])

           #
           # Gender
            with col2:
               colored_header(
                   label="Select Gender",
                   description="",
                   color_name="blue-green-70")
               gender = st.selectbox('', ['Choose 👇','Female', 'Male'])
               if gender == 'Female':
                   if st.button('Proceed'):
                     cursor.execute("update predict_data set gender = 0 where id = 100")
                     praveen.commit()
                     st.success('Your Gender Data Saved ✅')
               elif gender == 'Male':
                   if st.button('Proceed'):
                      cursor.execute("update predict_data set gender = 1 where id = 100")
                      praveen.commit()
                      st.success('Your Gender Data Saved ✅')
            col2.write("")
            col2.write("")

           # Age
            with col2 :
               colored_header(
                   label="Provide Age",
                   description="",
                   color_name="blue-green-70")
               age = st.number_input(" ", min_value=0, max_value=100, value=21, step=1)
               if st.button('PROCESS'):
                   cursor.execute(f"update predict_data set age = {age} where id = 100")
                   praveen.commit()
                   st.success('Your Age Data Saved ✅')
            col2.write("")
            col2.write("")

           # Hyper Tension
            with col2:
               colored_header(
                   label="Do You Have HyperTension",
                   description="",
                   color_name="blue-green-70")
               gender = st.selectbox('                      ', ['Choose 👇','Yes', 'No'])
               if gender == 'No':
                   if st.button('proceed'):
                       cursor.execute(f"update predict_data set hypertension = 0 where id = 100")
                       praveen.commit()
                       st.success('Your HyperTension Data Saved ✅')
               elif gender == 'Yes':
                   if st.button('proceed'):
                       cursor.execute(f"update predict_data set hypertension = 1 where id = 100")
                       praveen.commit()
                       st.success('Your HyperTension Data Saved ✅')
            col2.write("")
            col2.write("")
           # Heart Disease
            with col2:
               colored_header(
                   label="Do You Have Heart Disease ",
                   description="",
                   color_name="blue-green-70")
               gender = st.selectbox('  ', ['Choose 👇','Yes', 'No'])
               if gender == 'No':
                   if st.button('Save'):
                       cursor.execute(f"update predict_data set heart_disease = 0 where id = 100")
                       praveen.commit()
                       st.success('Your Heart Disease Data Saved ✅')
               elif gender == 'Yes':
                   if st.button('Save'):
                       cursor.execute(f"update predict_data set heart_disease = 1 where id = 100")
                       praveen.commit()
                       st.success('Your Heart Disease Data Saved ✅')

            col2.write("")
            col2.write("")


            # Smoking History
            with col2:
                colored_header(
                    label="Tell About You Smoking Habit",
                    description="",
                    color_name="blue-green-70")
                gender = st.selectbox('  ', ['Choose 👇', 'Never!!! My Wife Will Kill Me ', 'I Wont Provide Detail', 'At Present Iam Smoking', 'I had used to Smoke But not now', 'Daily I will Smoke', 'At Present Iam Not Smoking'])
                if gender == 'Never!!! My Wife Will Kill Me ':
                    if st.button('STORE'):
                        cursor.execute(f"update predict_data set smoking_history = 4 where id = 100")
                        praveen.commit()
                        st.success('Your Smoking History Data Saved ✅')
                elif gender == 'I Wont Provide Detail':
                    if st.button('store'):
                        cursor.execute(f" update predict_data set smoking_history = 0 where id = 100")
                        praveen.commit()
                        st.success('Your Smoking History Data Saved ✅')
                elif gender == 'At Present Iam Smoking':
                    if st.button('Entry'):
                        cursor.execute(f"update predict_data set smoking_history = 1 where id = 100")
                        praveen.commit()
                        st.success('Your Smoking History Data Saved ✅')
                elif gender == 'I had used to Smoke But not now':
                    if st.button('ENTRY'):
                        cursor.execute(f"update predict_data set smoking_history = 3 where id = 100")
                        praveen.commit()
                        st.success('Your Smoking History Data Saved ✅')

                elif gender == 'Daily I will Smoke':
                    if st.button('ENTRY'):
                        cursor.execute(f"update predict_data set smoking_history = 2 where id = 100")
                        praveen.commit()
                        st.success('Your Smoking History Data Saved ✅')
                elif gender == 'At Present Iam Not Smoking':
                    if st.button('SAVE IT'):
                        cursor.execute(f"update predict_data set smoking_history = 5 where id = 100")
                        praveen.commit()
                        st.success('Your Smoking History Data Saved ✅')
            # BMI

            with col2 :

                colored_header(
                        label="Provide Body Mass Index",
                        description="",
                        color_name="blue-green-70")
                bmi = st.number_input("               ", min_value=0, max_value=100, value=27, step=1)
                if st.button('Process'):
                        cursor.execute(f"update predict_data set bmi = {bmi} where id = 100")
                        praveen.commit()
                        st.success('Your Body Mass Index Data Saved ✅')
            col2.write("")
            col2.write("")

            # Hba1c Level

            with col2:

                colored_header(
                    label="Provide Hba1c Level",
                    description="",
                    color_name="blue-green-70")
                hba1c_level = st.number_input("                               ", min_value=3, max_value=9, value=5, step=1)
                if st.button('PROCEED'):
                    cursor.execute(f"update predict_data set hba1c_level = {hba1c_level} where id = 100")
                    praveen.commit()
                    st.success('Your Hemoglobin A1c Data Saved ✅')
            col2.write("")
            col2.write("")

            col2.write("")
            col2.write("")

            # Blood Glucose Level

            with col2:

                colored_header(
                    label="Provide Blood Glucose Level",
                    description="",
                    color_name="blue-green-70")
                blood_glucose_level = st.number_input("                               ", min_value=70, max_value=300,
                                              value=85, step=1)
                if st.button('SAVE'):
                    cursor.execute(f"update predict_data set blood_glucose_level = {blood_glucose_level} where id = 100")
                    praveen.commit()
                    st.success('Your Blood Glucose Level Data Saved ✅')
            col2.write("")
            col2.write("")

            # Fetch predict data
            cursor.execute("select gender, age, hypertension, heart_disease, smoking_history,bmi, Hba1c_level, blood_glucose_level from predict_data")
            test = [i for i in cursor.fetchall()]



            col1, col2, col3 = st.columns([8, 8, 3])
            if col2.button("Get Status"):
                col2.write("")
                col2.write("")
                col2.write("")
                col1, col2, col3 = st.columns([3.5,8 , 3])
                with col2:
                    file = lottie('heart_rate_2.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=470,
                        width=600,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                with col2:
                    with st.spinner('WAIT FOR YOUR RESULT !!!'):
                        time.sleep(5)

                # Prediction process
                result = model.predict([test[0]])

                result = model.predict([test[0]])
                col1, col2, col3 = st.columns([10,9 ,10])
                if result == 0:

                    with col1:
                        file = lottie('star2.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=300,
                            width=400,
                            key=None
                        )

                    with col3:
                        file = lottie('star2.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=400,
                            width=500,
                            key=None
                        )

                    with col2:
                        file = lottie('stareyeblick.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=300,
                            width=400,
                            key=None
                        )
                    col1, col2, col3 = st.columns([5, 9, 2])
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:cyan;'>SugarSense AI Reported : </span> <span style='color:white;'>No Diabetes</span> </h1>",
                        unsafe_allow_html=True)

                elif result == 1:
                    col1, col2, col3 = st.columns([2, 9, 2])
                    with col2:
                        file = lottie('doctor_sugar.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=600,
                            width=900,
                            key=None
                        )
                    col1, col2, col3 = st.columns([4, 9,2])
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:cyan;'>SugarSense AI Reported : </span> <span style='color:white;'> Diabetes (Consult Doctor)</span> </h1>",
                        unsafe_allow_html=True)
        elif selected == 'Feedback':
            # Mongo Python connectivity
            praveen_1 = pm.MongoClient(
                'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')


            st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                selected_1 = option_menu(
                    menu_title="OPINION BOX",
                    options=['CHOOSE OPTION', 'Your Feedback', "Explore User Thoughts"],
                    icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                    default_index=0)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            if selected_1 == 'CHOOSE OPTION':
                      pass

            elif selected_1 == 'Your Feedback':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])
                col2.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                # animation

                st.write("")

                st.write("")

                st.write("")
                col1, col2, col3 = st.columns([15, 30, 5])
                with col2:
                    file = lottie("star_before_fb.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=600,
                        key=None
                    )

                col1, col2, col3, = st.columns([3, 8, 3])

                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                        unsafe_allow_html=True)
                    Comment = st.text_input('   ')
                    st.write(Comment)
                    if st.button('Save Comment'):
                        collection.insert_one({'comment of user': Comment})
                        st.write("")
                        st.write("")
                        col1, col2, col3, = st.columns([5, 8, 5])
                        st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                        col1, col2, col3 = st.columns([10, 30, 10])
                        with col2:
                            file = lottie("star.json")
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                # renderer='svg',
                                height=100,
                                width=400,
                                key=None
                            )

                col1, col2, col3, = st.columns([3, 8, 3])
                with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )


            elif selected_1 == 'Explore User Thoughts':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])

                with col2:

                    file = lottie("down_arrow.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=800,
                        key=None
                    )
                col2.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                col2.write("")
                col2.write("")

                with col2:

                    file = lottie("thoughts.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=800,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                col1, col2, col3, = st.columns([3.6, 10, 3])
                with col2:
                    # if st.button("Click Me!"):
                    res = [i['comment of user'] for i in collection.find()]
                    st.write("")
                    with st.spinner('Wait for it...'):
                        time.sleep(5)

                    colored_header(
                        label="Comments By Users ⬇",
                        description="",
                        color_name="blue-green-70", )
                    for i in res:
                        print(st.code(i))

                    col1, col2, col3 = st.columns([1, 10, 1])
                    col2.write("")
                    col2.write('')
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                        unsafe_allow_html=True)
                    with col2:
                        keyboard_to_url(key="G", url="https://github.com/praveendecode")

                    def lottie(filepath):
                        with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                            return js.load(file)

                    col1, col2, col3 = st.columns([2, 4, 1])
                    with col2:
                        file = lottie("click2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=100,
                            width=300,
                            key=None
                        )

                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )





object = Diabetes_prediction()
object.process()