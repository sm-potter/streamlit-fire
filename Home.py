import streamlit as st
import leafmap.foliumap as leafmap

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


st.title("A Streamlit App for Viewing Unet ++ Predictions for Burned Area in Alaska")

st.markdown(
    """
    This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and open-source mapping libraries, 
    such as [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), and [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
    This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/giswqs/streamlit-geospatial/issues) or 
    [pull requests](https://github.com/giswqs/streamlit-geospatial/pulls) to the [GitHub repository](https://github.com/giswqs/streamlit-geospatial).

    """
)

st.info("Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
