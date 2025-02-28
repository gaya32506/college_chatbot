import streamlit as st
import pandas as pd
import google.generativeai as genai
from sklearn.metrices.pairwise import cousine_similarity
from sklearn .feature_extraction.text import TfidfVectorizer
st.set_page_config(page_title="College Chatbot",layout
