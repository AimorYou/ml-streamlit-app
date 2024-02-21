import os
from pathlib import Path
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from typing import Iterable
from typing import List
from typing import Text


@st.cache_data
def display_report(report_path: Path) -> List[Text]:
    """Display report.

    Args:
        report (Path): Report path.

    Returns:
        List[Text]: Report parts content - list report part contents.
    """

    # If a report is file then read and display the report
    if report_path.is_file():
        with open(report_path, encoding="utf8") as report_f:
            report: Text = report_f.read()
            components.html(report, width=1000, height=1200, scrolling=True)
        return [report]