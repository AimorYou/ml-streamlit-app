import datetime
import os

import pandas as pd
import streamlit as st
import plotly.figure_factory as ff

from src.vizualization import *


def get_last_7_days():
    dates = []

    for i in range(7):
        dates.append((datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y-%m-%d'))

    return dates


def get_models():
    return (
        10511001,
        10511005,
        10511006,
        10511012,
        10511013,
        10511014,
        10511015,
    )


def get_etalon_names():
    return tuple(os.listdir("data"))


def get_data_preview(df):
    """Data Preview main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("DATA PREVIEW")
    col1, col2 = st.columns(2)

    st.subheader("Original dataframe")
    st.dataframe(df)
    st.write(df.shape)

    with col1:
        st.subheader("Data types")
        st.dataframe(df.dtypes.astype(str), use_container_width=True)

    with col2:
        st.subheader("Dataframe description")
        st.dataframe(df.describe(), use_container_width=True)

    # Correlation matrix
    st.header("Distribution")

    tab1, tab2 = st.tabs(["pyplot", "plotly_chart"])

    with tab1:
        zxc = sns.displot(data=df, x="Age", kde=True, bins=st.session_state.n_bins)
        st.pyplot(zxc.fig, use_container_width=True)

    with tab2:
        zxc = sns.displot(data=df, x="Age", kde=True, bins=st.session_state.n_bins)
        st.plotly_chart(zxc.fig, theme="streamlit", use_container_width=True)

    with col1:
        zxc = sns.displot(data=df, x="Age", kde=True, bins=st.session_state.n_bins)
        st.pyplot(zxc.fig, use_container_width=True)

    with col2:
        zxc = sns.displot(data=df, x="Age", kde=True, bins=st.session_state.n_bins)
        st.plotly_chart(zxc.fig, theme="streamlit", use_container_width=True)



    # for col in df.columns:
    #     Histogram(df, col)
