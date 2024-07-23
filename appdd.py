import streamlit as st
import pickle as pkl
import numpy as np 

def main():
    html_temp ="""
    <div style="background:#025246; padding:10px">
    <h2 style="color:white; text-align:center;">Sports Rating Prediction</h2>
    </div>"""

    st.markdown(html_temp, unsafe_allow_html=True)

filename = r"C:\Users\user\OneDrive\Desktop\Ai(3)\Ai (2)\Ai\model.pkl"
col1_features = ['potential', 'value_eur', 'wage_eur', 'age', 'international_reputation']
col2_features = ['release_clause_eur', 'passing', 'physic', 'attacking_short_passing', 'skill_long_passing']


def inputs():
        #Prepare input data from prediction 
        st.write('Input Data:')
        col1, col2 = st.columns(2)

        with col1:
            potential = st.number_input('Potential')
            value_eur = st.number_input('Value (EUR)')
            wage_eur = st.number_input('Wage (EUR)')
            age = st.number_input('Age')
            international_reputation = st.number_input('International Reputation')


        with col2:
            release_clause_eur = st.number_input('Release Clause (EUR)')
            passing = st.number_input('Passing')
            physic = st.number_input('Physic')
            attacking_short_passing = st.number_input('Attacking Short Passing')
            skill_long_passing = st.number_input('Skill Long Passing')

        best_model = pkl.load(open(filename, 'rb'))

        # Make prediction on button click
        if st.button('Predict'):
            input_data = np.array([[potential, value_eur, wage_eur, age, international_reputation,
                 release_clause_eur, passing, physic, attacking_short_passing, skill_long_passing]])
            prediction = best_model.predict(input_data)
            st.write(f'The predicted value is: {prediction[0]}')

main()
inputs()

