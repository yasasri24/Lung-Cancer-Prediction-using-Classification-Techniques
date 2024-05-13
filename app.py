import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
knn_model = joblib.load('knn_model.pkl')
# Manual mapping of encoded values to original categories
class_mapping = {0: 'Low', 1: 'Medium', 2: 'High'}


# Function to make predictions
def predict_level(new_data):
    prediction = knn_model.predict(new_data)
    return prediction

# Streamlit UI
def main():
    st.title('Lung Cancer Prediction')
    st.header('Input Details of the patient')

    # Collect user input for prediction
    age = st.number_input('Age', min_value=0, max_value=100, step=1)
    gender=st.number_input('gender', min_value=0, max_value=10, step=1)
    AirPollution=st.number_input('Air Pollution', min_value=0, max_value=10, step=1)
    Alcoholuse=st.number_input('Alcohol use', min_value=0, max_value=10, step=1)
    DustAllergy=st.number_input('Dust Allergy', min_value=0, max_value=10, step=1)
    OccuPationalHazards=st.number_input('OccuPational Hazards', min_value=0, max_value=10, step=1)
    GeneticRisk=st.number_input('Genetic Risk', min_value=0, max_value=10, step=1)
    chronicLungDisease=st.number_input('chronicLungDisease', min_value=0, max_value=10, step=1)
    BalancedDiet=st.number_input('BalancedDiet', min_value=0, max_value=10, step=1)
    Obesity=st.number_input('Obesity', min_value=0, max_value=10, step=1)
    Smoking=st.number_input('Smoking', min_value=0, max_value=10, step=1)
    PassiveSmoker=st.number_input('PassiveSmoker', min_value=0, max_value=10, step=1)
    ChestPain=st.number_input('ChestPain', min_value=0, max_value=10, step=1)
    CoughingofBlood=st.number_input('CoughingofBlood', min_value=0, max_value=10, step=1)
    Fatigue=st.number_input('Fatigue', min_value=0, max_value=10, step=1)
    WeightLoss=st.number_input('WeightLoss', min_value=0, max_value=10, step=1)
    ShortnessofBreath=st.number_input('ShortnessofBreath', min_value=0, max_value=10, step=1)
    Wheezing=st.number_input('Wheezing', min_value=0, max_value=10, step=1)
    SwallowingDifficulty=st.number_input('SwallowingDifficulty', min_value=0, max_value=10, step=1)
    ClubbingofFingerNails=st.number_input('ClubbingofFingerNails', min_value=0, max_value=10, step=1)
    FrequentCold=st.number_input('FrequentCold', min_value=0, max_value=10, step=1)
    DryCough=st.number_input('DryCough', min_value=0, max_value=10, step=1)
    Snoring=st.number_input('Snoring', min_value=0, max_value=10, step=1)
    # Collect other features similarly

    new_data = [[age,gender,AirPollution,Alcoholuse,DustAllergy,OccuPationalHazards,GeneticRisk,chronicLungDisease,BalancedDiet,Obesity,Smoking,PassiveSmoker,ChestPain,CoughingofBlood,Fatigue,WeightLoss,ShortnessofBreath,Wheezing,SwallowingDifficulty,ClubbingofFingerNails,FrequentCold,DryCough,Snoring]]  # Replace ... with other features

    if st.button('Predict'):
        prediction = predict_level(new_data)
        st.write(f"The predicted health risk level is: {prediction}")
        predicted_category = class_mapping[prediction[0]]

        st.success(f"The predicted Lung Cancer risk level is: {predicted_category}")

if __name__ == '__main__':
    main()