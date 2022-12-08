import streamlit as st
import leafmap.foliumap as leafmap
import geemap.foliumap as geemap
import ee

ee.Authenticate()
ee.Initialize()

import geemap.colormaps as cm

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

st.title("Alaska CNN Predictions")

Map = geemap.Map()

#read in the predictions and lfdb ground truth
dnbr = ee.ImageCollection("projects/gee-serdp-upload/assets/mtbs_predictions").select('b7')
preds = ee.ImageCollection("projects/gee-serdp-upload/assets/mtbs_predictions").select('b10')
preds_thresh = ee.ImageCollection("projects/gee-serdp-upload/assets/mtbs_predictions").select('b11')

lfdb = ee.FeatureCollection("users/spotter/fire_cnn/raw/ak_mtbs_1985") #ak fire polygons)

palette = cm.palettes.RdBu_r


Map.addLayer(preds, {'min': 0, 'max': 1}, 'Predictions')
Map.addLayer(preds_thresh, {'min': 0, 'max': 1}, 'Predictions Threshold')
Map.addLayer(dnbr, {min:0, max: 1, 'palette' : palette}, 'dNBR')

Map.addLayer(lfdb, {}, 'Ground Truth MTBS Polygons')

width = 950
height = 600


Map.to_streamlit(width=width, height=height)
# esri = ee.ImageCollection(
#     "projects/sat-io/open-datasets/landcover/ESRI_Global-LULC_10m"
# ).mosaic()
# esri_vis = {
#     "min": 1,
#     "max": 10,
#     "palette": [
#         "#1A5BAB",
#         "#358221",
#         "#A7D282",
#         "#87D19E",
#         "#FFDB5C",
#         "#EECFA8",
#         "#ED022A",
#         "#EDE9E4",
#         "#F2FAFF",
#         "#C8C8C8",
#     ],
# }
