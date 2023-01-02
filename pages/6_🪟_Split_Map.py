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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
