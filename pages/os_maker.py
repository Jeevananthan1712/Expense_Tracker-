
from pathlib import Path
import os
import streamlit as st
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
st.write(path_to_download_folder)