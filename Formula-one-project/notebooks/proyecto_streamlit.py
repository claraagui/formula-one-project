import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
import streamlit as st

df=pd.read_csv('C:/Users/Clara/apps2/formula-one-project/Formula-one-project/data/raw/Formula1data.csv')