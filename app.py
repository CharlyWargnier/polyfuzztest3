import asyncio

import streamlit as st
import csv

from polyfuzz import PolyFuzz
from fuzzywuzzy import fuzz

import numpy as np
import base64
import pandas as pd
import io

import matplotlib as plt
import seaborn as sns


# region Layout size ####################################################################################


def _max_width_():
    max_width_str = f"max-width: 1300px;"
    # max_width_str = f"max-width: 1550px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

# endregion Layout size ####################################################################################

c30, c31, c32 = st.beta_columns(3)

with c30:
    st.image("logoNew.png", width=475)
    st.header("")

with c32:
    st.header("")
    st.header("")
    st.markdown(
        "###### Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://twitter.com/DataChaz) &nbsp [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)"
    )


with st.beta_expander("ℹ️ -  Todo - roadmap ", expanded=True):

    st.write(
        """   

-   RECHECK Deployment on S4?
-   Shorten code by doing only one text_area
-   Remove bug when click on run model button
-   RAISE ERRORS - RAISE ERRORS - RAISE ERRORS - RAISE ERRORS 
-   Prevent model to run (and final table to be displayed) if keywords are pasted instead of URLs (Currently everything runs)
-   Raise error if press run model but no uploaded file
-   FORMATTING - FORMATTING - FORMATTING - FORMATTING
-   Tweak emoji in expanders

	    """
    )


with st.beta_expander("ℹ️ -  Done", expanded=False):

    st.write(
        """   

-   Try to enable Gif when loading - Currently issue w/ polyfuzz dataframe being unbound
-   re-align Gif
-   Add new logo
-   Add tiles + 1 and 2 unicodes
-   CHECK OUTLIERS - Try with other websites (Samusung - crawl)
-   TEXT_AREA TEXT_AREA TEXT_AREA TEXT_AREA TEXT_AREA 
-   remove 100 max limit (decide which limit)
-   NOT NEEDED - Install hppx from francois so everything is displaued in app, with waiting messages? 
-   Remove crawl on disk - Keep upload
-   [TOO COMPLICATED WITH MERGING LIST WITH DATAFRAMES] Final table : Add a URL column if selection is "to title tag"
-   Remove "SF crawl" OK if no crawl uploaded
-   Change format in radio buttons section - incorrect again
-   Remove NaN as strings, replace by empty, so it doesn't count as a suggestion 
-   Final table : Tweak name logic on export, depending on options 
-   LOGIC - LOGIC - LOGIC - LOGIC - LOGIC - LOGIC - 
-   Final table : Change headers based on radio  boxes selections
-   1- "What do you want to map?"  logic for radio buttons is working
-   2- "Where to map?"  logic for radio buttons is working
-   3- "Index span"  logic for radio buttons is working
-   Remove duplicates from textarea
-   Remove empty lines in list
-   Make sure uploader is for 1 file only (currently several files)
-   Add button to launch algo
-   Try to upload on S4 Try to upload on S4 Try to upload on S4 Try to upload on S4 
-   Reformat radio buttons as it's now been messed up
-   Final table : Add red for lower values
-   Last table - Add conditionnal formatting
-   Last table - Add percentage
-   Add switch to remove non indexable URLs
-   Remove "Group" - Doesn't work! Tweak or remove
-   Add export to csv
-   Remove 'H1-2' as issue with H1-1

	    """
    )


with st.beta_expander("ℹ️ - Later ", expanded=False):

    st.write(
        """   
-   Add tagline to logo?
-   try CMAPRed but doesn't work - Do gradient red to green in table
-   LOGIC - LOGIC - LOGIC - LOGIC - LOGIC - LOGIC - 
-   Add expections messages - if keywords OR URLs are mapped
-   -   SEE COLAB! Add exceptions if uploaded file is not from Screaming Frog https://colab.research.google.com/drive/1zLYbNqiT6MMYc1ap33hrDnSSr50mc97o#scrollTo=KJV-YcMM4G7f
-   Add other crawl upload - Not just Screaming frog
-   Try synomym match with flair/Transformers models 
-   Blend with equity data (e.g. Majestic)
-   Tips from Lee Foot/ Tips from Lee Foot/ Tips from Lee Foot/ Tips from Lee Foot/  
-   Find a way to filter out URLs by equity
-   Still got more testing to do, but the plan is to do a secondary match on the anchor text vs h1 and score on both values. Got some other ideas too past that. try and send bad matches to the best matching folder, else > Homepage. But testing is going well so far!
-   https://twitter.com/cemper/status/1349852864630423559
	    """
    )


with st.beta_expander("ℹ️ -  About this app ", expanded=False):

    st.write(
        """   
-   This data app uses _________________ to ___________________________.
-   The tool is in Beta. Feedback & bug spotting are welcome. [DMs are open!](https://twitter.com/DataChaz)
-   This app is free. If it's useful to you, you can [buy me a coffee](https://www.buymeacoffee.com/cwar05) to support my work! 🙏
	    """
    )

st.markdown("## **① Upload your Screaming Frog crawl **")

c10 = st.beta_container()

with st.beta_expander("ℹ️ -  About the crawl format", expanded=False):

    st.write(
        """

-   Internal all.csv
-   Paste screenshot
        
        """
    )

st.markdown("## **② Paste KWs/Broken links & Run  Model **")

linesDeduped2 = []

c0, c1, c2, c3, c4, c5, c6, c7 = st.beta_columns(
    [0.8, 0.55, 1.1, 0.55, 1.1, 0.55, 1.1, 1.5]
)

with c1:
    st.text("")
    st.text("")
    st.text("")
with c2:
    RadioMapWhat = st.radio(
        "What do you want to map?", options=("Map Broken URLs", "Map Keywords")
    )

with c3:
    st.text("")
    st.text("")
    st.text("")

with c4:
    RadioMapTo = st.radio(
        "Where to map them?", options=("To crawled URL", "To crawled titles")
    )
    # RadioMapTo

with c5:
    st.text("")
    st.text("")
    st.text("")
with c6:
    RadioMapAgainst = st.radio(
        "Indexability span", options=("All crawled URLs", "Indexable only"), key=5
    )

c29, c30, c31 = st.beta_columns([1, 6, 1])

MAX_LINES = 200

# from re import search

substring = "http://|https://"

with c30:

    if RadioMapWhat == "Map Broken URLs":

        text = st.text_area("One per line (200 max)", height=275, key=1)
        lines = text.split("\n")  # A list of lines
        linesList = []
        for x in lines:
            linesList.append(x)
        linesList = list(dict.fromkeys(linesList))  # Remove dupes
        linesList = list(filter(None, linesList))  # Remove empty

        if len(linesList) > MAX_LINES:
            st.warning(
                f"⚠️ Only the 200 first URLs will be reviewed. Increased allowance  is coming - Stay tuned! 😊)"
            )
            linesList = linesList[:MAX_LINES]

        # Checks if element in list starts with http:// or https://
        SCHEMES = ("http://", "https://")
        list2 = all(item.startswith(SCHEMES) for item in linesList)
        if list2 == False:
            st.error(
                "Are you sure all elements are URLs? Switch to 'map KWs' if you wanted to map keywords"
            )

        c = st.beta_container()
        c30 = st.beta_container()

    elif RadioMapWhat == "Map Keywords":

        text = st.text_area("One per line (200 max)", height=275, key=2)
        lines = text.split("\n")  # A list of lines
        linesList = []
        for x in lines:
            linesList.append(x)
        linesList = list(dict.fromkeys(linesList))  # Remove dupes
        linesList = list(filter(None, linesList))  # Remove empty

        if len(linesList) > MAX_LINES:
            st.warning(
                f"⚠️ Only the 200 first keywords will be reviewed. Increased allowance  is coming - Stay tuned! 😊)"
            )
            linesList = linesList[:MAX_LINES]
        # Print list
        # linesList

        # Checks if element in list starts with http:// or https://
        SCHEMES = ("http://", "https://")
        for line in linesList:
            if line.startswith(SCHEMES):
                st.error("Are you sure all elements are KWs?")

        c = st.beta_container()
        c30 = st.beta_container()

# if text:
#    pass
# else:
#    st.success("⯅ Start by adding keywords or URLs in the box above")
#    st.stop()


start_execution = c30.button(" Run model! ✨ ")

uploaded_file = c10.file_uploader("Choose a csv for predictions", key=1)

if uploaded_file is not None:
    file_container = c10.beta_expander("See your uploaded csv")
    # Can be used wherever a "file-like" object is accepted:
    GSCDf = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    file_container.write(GSCDf)

else:
    pass
    st.stop()  # "Waiting client configuration..."

# GSCDf = pd.read_csv("Crawls_CSV\TatieLou_Internal_all.csv")

# try:
# pass
GSCDf = GSCDf.fillna(value="")

SFMinimumHeaders = ["Address", "Indexability Status", "Title 1"]

# check if headers in uploaded CSV have got the headers in SFMinimumHeaders
HeadersOK = all(i in GSCDf for i in SFMinimumHeaders)

if not uploaded_file:
    pass
elif (HeadersOK == True) and (uploaded_file):
    # elif HeadersOK == True:
    pass
    # st.success("SF crawl OK")
else:
    st.error("Not a SF crawl!")

dfIndexable = GSCDf.loc[GSCDf["Indexability"] == "Indexable"]

# st.markdown("---")

##########################################################


if RadioMapTo == "To crawled URL":
    col_one_list = GSCDf["Address"].tolist()
else:
    col_one_list = GSCDf["Title 1"].tolist()
    # col_one_listURL = GSCDf["Address"].tolist()

# col_one_list
# st.stop()

if RadioMapAgainst == "all crawled URLs":
    GSCDf = dfIndexable
else:
    pass

model = PolyFuzz("EditDistance")


gif_path = "mouse.gif"

if start_execution:

    ########## GIT NOT WORKING (UNBOUND)

    # gif_runner = st.image(gif_path)

    c1, c2, c3 = st.beta_columns([5, 5, 5])

    with c2:

        # gif_runner = st.image("mouse.gif")
        # gif_runner = st.image(gif_path)
        gif_runner = st.image("mouse.gif")

        import time

        time.sleep(2)

        model.match(linesList, col_one_list)
        # model.match(linesDeduped2, col_one_list)
        # Auto map by Similarity scores
        Polyfuzz = model.get_matches()
        # Polyfuzz
        gif_runner.empty()
    # st.stop()

    # model.match(linesList, col_one_list)
    ## Auto map by Similarity scores
    # Polyfuzz = model.get_matches()

    # Polyfuzz
    # st.stop()

    if (RadioMapTo == "To crawled titles") and (RadioMapWhat == "Map Broken URLs"):
        # Polyfuzz = pd.concat([Polyfuzz.assign(name=i) for i in col_one_listURL], ignore_index=True)
        # Polyfuzz = Polyfuzz.assign(key=1).merge(pd.DataFrame({'Name':col_one_listURL,'key':1})).drop('key',1)
        Polyfuzz.columns = ["URL to map", "Tite tag match", "Similarity"]
    elif (RadioMapTo == "To crawled titles") and (RadioMapWhat == "Map Keywords"):
        Polyfuzz.columns = ["Keywords to map", "Tite tag match", "Similarity"]
    elif (RadioMapTo == "To crawled URL") and (RadioMapWhat == "Map Keywords"):
        Polyfuzz.columns = ["Keywords to map", "Tite tag match", "Similarity"]
    elif (RadioMapTo == "To crawled URL") and (RadioMapWhat == "Map Broken URLs"):
        Polyfuzz.columns = ["URL to map", "Tite tag match", "Similarity"]

    #########################

    # from matplotlib.colors import LinearSegmentedColormap
    # cmap = LinearSegmentedColormap.from_list(
    #    name='test',
    #    colors=['red','white','green','white','red']
    # )

    #########################

    import pandas as pd

    # import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    # np.random.seed(5)
    # df = pd.DataFrame(np.random.randn(5,5))

    # Generate a custom diverging colormap
    # cmap = sns.diverging_palette(133, 10, as_cmap=True)

    # with sns.axes_style("white"):
    #    ax = sns.heatmap(
    #        Polyfuzz,
    #        annot=True,
    #        fmt=".2f",
    #        cmap=cmap,
    #        vmin=-0.99,
    #        vmax=0.99,
    #        center=0.00,
    #        square=True,
    #        linewidths=0.5,
    #        annot_kws={"size": 8},
    #        cbar_kws={"shrink": 0.5},
    #    )
    # plt.show()

    #######################

    cmapRed = sns.diverging_palette(10, 133, as_cmap=True)
    cm = sns.light_palette("red", as_cmap=True, reverse=True)
    FuzzStyled = Polyfuzz.style.background_gradient(cmap=cm)

    format_dictionary = {
        "Similarity": "{:.1%}",
    }

    FuzzStyled = FuzzStyled.format(format_dictionary)

    c2 = st.beta_container()
    c29, c30, c31 = st.beta_columns([1, 6, 1])

    with c30:
        c = st.beta_container()
        st.table(FuzzStyled)

    try:
        csv = Polyfuzz.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        # c2.markdown("---")
        c2.markdown("## **③ Check the mapping or download to CSV **")

        c.subheader("")
        if RadioMapTo == "to URL":
            href = f'<a href="data:file/csv;base64,{b64}" download="Mapping_to_URL.csv">** ⯈ Download link 🎁 **</a>'
        else:
            href = f'<a href="data:file/csv;base64,{b64}" download="Mapping_to_title.csv">** ⯈ Download link 🎁 **</a>'
        c.markdown(href, unsafe_allow_html=True)

    except NameError:
        st.write("wait")

# except NameError:
#    pass
