import librosa
import warnings
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from django.conf import settings


warnings.filterwarnings("ignore")


final = pd.read_pickle("extracted_df.pkl")
y = np.array(final["class"].tolist())
le = LabelEncoder()
le.fit_transform(y)
Model_ANN = load_model("ANN_Model.h5")



def extract_feature(audio_path):
    audio_data, sample_rate = librosa.load(audio_path, res_type="kaiser_fast")
    feature = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=128)
    feature_scaled = np.mean(feature.T, axis=0)
    return np.array([feature_scaled])





def ANN_print_prediction(audio_path):
    prediction_feature = extract_feature(audio_path)
    predicted_vector = np.argmax(Model_ANN.predict(prediction_feature), axis=-1)
    predicted_class = le.inverse_transform(predicted_vector)
    return predicted_class[0]


    
   





