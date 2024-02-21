import os.path
import time

import pandas as pd
import streamlit as st
from pathlib import Path

from src.helpers import *
from src.evidently_stuff import *


st.title("Monitrong dashboard")

st.write("fdngon")

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    # with st.spinner("Loading..."):
    #     time.sleep(5)
    # st.success("Done!")

    # with st.sidebar:

    stand = st.radio(
        "Выберите этап для построения распрделения",
        ("Эталон", "Препрод")
    )

    if stand == "Препрод":
        model = st.selectbox(
            "Выберите модель",
            get_models()
        )

        data = st.selectbox(
            "Выберите дату, за которую необходимо построить распределение",
            get_last_7_days()
        )
    elif stand == "Эталон":
        etalon_name = st.selectbox(
            "Выберите дату, за которую необходимо построить распределение",
            get_etalon_names()
        )

        etalon_rows = st.slider(
            "Выберите кол-во строк эталона для аналитики",
            0, 1000, 500, 10
        )

        n_bins = st.slider("Выберите количество бинов", 1, 50, key="n_bins")

    distr_flg = st.button("Построить распрделение")

# if distr_flg:
with st.spinner("Loading..."):
    st.write(f"Вы выбрали {stand}")

    if stand == "Препрод":
        st.write(f"Вы выбрали {model}")
        st.write(f"Вы выбрали {data}")

        report_path = Path(os.path.join(os.path.dirname(__file__), "data", "report.html"))
        display_report(report_path)
    elif stand == "Эталон":
        df = pd.read_csv(f"data/{etalon_name}")
        get_data_preview(df)
