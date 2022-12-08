import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image

st.set_page_config(layout="wide")

st.sidebar.title("About")

st.sidebar.info(
    """
    Web App URL: <https://sm-potter-streamlit-fire-streamlit-app-7sy8c9.streamlit.app/>

    GitHub repository: <https://github.com/sm-potter/streamlit-fire>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Stefano Potter: <spotter@woodwellclimate.org>
    [GitHub](https://github.com/sm-potter) 
    """
)

# # Customize page title
st.title("An Appplication which Vizualizes the Output of Unet++ CNN Model to Predict Burned Area in Alaska, along with Individual Predictors Used to Train the Model")


# st.markdown(
#     """
#     This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
#     """
# )

st.header("Instructions")

markdown = """
1. Zoom into a fire of interest.
2. Within the map layer lick the layers icon in the top right corner to turn individual layers on and off.
"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
