import streamlit as st
import pandas as pd
from statistics import NormalDist
from statsmodels.stats.weightstats import ztest
from scipy.stats import shapiro

st.title('Z Test')

with st.expander('View Data'):
    df= pd.read_csv('https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv')
    st.dataframe(df.transpose())

with st.expander('View Statistics'):
    st.dataframe(df.describe().transpose())

st.write('## Constructing Hypothesis')
st.latex('H_{0} : \mu = \mu_{0}')
st.latex('H_{1} : \mu \neq \mu_{1}')

clicked = st.button('Do The Z Test')

alpha = st.number_input('Masukan Nilai Alpha',step=0.00001, min_value=0., max_value=1.)
null_mean = st.number_input('Masukkan Nilai mu_0', step=0.00001)


if clicked:
    print(alpha)
    alpha_z = NormalDist().inv_cdf(p=1-alpha/2)
    z_score, p_value = ztest(df['grades'], value=null_mean, alternative='two-sided')

    if abs(z_score) > alpha_z:
        st.latex('Reject H_{0}')
    else:
        st.latex('Can Not Reject H_{0}')
    st.write('Titik Kritis = {alpha_z}, hitung z = {z_score}, p_value = {p_value}')

st.write('## CHECK NORMALITY')

Clicked_2 = st.button('Do The Shapiro Test')

if Clicked_2:
    result = shapiro(df['grades'])
    st.write(result)
    st.bar_chart(df['grades'])


