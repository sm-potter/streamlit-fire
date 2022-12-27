import streamlit as st
import leafmap.foliumap as leafmap
import geemap.foliumap as geemap
import ee
import warnings


# ee.Authenticate()
# ee.Initialize()
# geemap.ee_authenticate()
# geemap.ee_initialize(auth_mode='gcloud')

import geemap.colormaps as cm

st.set_page_config(layout="wide")

warnings.filterwarnings("ignore")


@st.cache(persist=True)
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)

ee_authenticate(token_name="EARTHENGINE_TOKEN")


# year = st.selectbox(
#                     "Select Fire Year:",
#                     [
#                         "1985",
#                         "1986",
#                         "1987",
#                         "1988",
#                         "1999",
#                         "2000",
#                         "2001",
#                         "2002",
#                         "2003",
#                         "2004",
#                         "2005",
#                         "2006",
#                         "2007",
#                         "2008",
#                         "2009",
#                         "2010",
#                         "2011",
#                         "2012",
#                         "2013",
#                         "2014",
#                         "2015",
#                         "2016",
#                         "2017",
#                         "2018",
#                         "2019",
#                         "2020"
#                     ],
#                     index=9,
#                 )


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
in_collection = ee.ImageCollection("projects/gee-serdp-upload/assets/mtbs_predictions")

red = in_collection = in_collection.select('b1')
green = in_collection = in_collection.select('b2')
blue = in_collection = in_collection.select('b3')
nir = in_collection = in_collection.select('b4')
swir1 = in_collection = in_collection.select('b5')
swir2 = in_collection = in_collection.select('b6')
dnbr = in_collection = in_collection.select('b7')
ndii  = in_collection = in_collection.select('b8')
ndvi = in_collection = in_collection.select('b9')
preds = ee.ImageCollection("projects/gee-serdp-upload/assets/mtbs_predictions").select('b10')
preds_thresh = ee.ImageCollection("projects/gee-serdp-upload/assets/mtbs_predictions").select('b11')

lfdb = ee.FeatureCollection("users/spotter/fire_cnn/raw/ak_mtbs_1985")

dnbr_palette = cm.palettes.RdBu_r


Map.setCenter(-151.29, 65.11, 4)
Map.addLayer(preds, {'min': 0, 'max': 1}, 'Predictions')
Map.addLayer(preds_thresh, {'min': 0, 'max': 1}, 'Predictions Threshold')
Map.addLayer(dnbr, {min:0, max: 1, 'palette' : dnbr_palette}, 'dNBR')
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
