import streamlit as st

from polyfuzz import PolyFuzz

import numpy as np
#import base64
import pandas as pd
import io


#import matplotlib as plt
#import seaborn as sns


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
    st.image("logo.png", width=425)
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

-   Try to upload on S4 Try to upload on S4 Try to upload on S4 Try to upload on S4 
-   Try to enable Gif when loading - Currently issue w/ polyfuzz dataframe being unbound
-   Make sure uploader is for 1 file only (currently several files)
-   Try with other websites (Samusung - crawl)
-   Add tiles + 1 and 2 unicodes
-   remove 100 max limit (decide which limit)
-   Remove crawl on disk - Keep upload
-   Add expections messages - if keywords OR URLs are mapped
-   Tweak emoji in expanders
-   Add a column if selection is "to title tag"
-   Add button to launch algo
-   Add exceptions if uploaded file is not from Screaming Frog
-   Remove empty lines in list
-   TABLE - TABLE - TABLE - TABLE - TABLE - TABLE
-   1- "What do you want to map?"  logic for radio buttons is working
-   2- "Where to map?"  logic for radio buttons is working
-   3- "Index span"  logic for radio buttons is working
-   Add new logo 
-   Add tagline to logo?
-   Install hppx from francois so everything is displaued in app, with waiting messages? 
-   Add gif when loading?
-   TABLE - TABLE - TABLE - TABLE - TABLE - TABLE
-   Final table : Change headers based on radio  boxes selections
-   Final table : Tweak name logic on export, depending on options 

	    """
    )


with st.beta_expander("ℹ️ -  Done", expanded=False):

    st.write(
        """   

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


# c29, c30, c31 = st.beta_columns([8, 1, 8])

# st.markdown("---")
# st.markdown("## **③ Check mapping or download CSV **")
st.markdown("## **① Upload your Screaming Frog crawl **")

# st.markdown("## **① Upload your JSON credentials **")  #########

c3, c4 = st.beta_columns(2)


uploaded_filePredict = st.file_uploader("Choose a csv for predictions", key=1)

if uploaded_filePredict is not None:
    file_container = st.beta_expander("See your uploaded csv")
    # Can be used wherever a "file-like" object is accepted:
    dfPredictions = pd.read_csv(uploaded_filePredict)
    uploaded_filePredict.seek(0)
    file_container.write(dfPredictions)

else:
    pass

# GSCDf = pd.read_csv("internal_all.csv")
#GSCDf = pd.read_csv("Crawls_CSV\TatieLou_Internal_all.csv")
GSCDf = pd.read_csv("Crawls_CSV/TatieLou_Internal_all.csv")


# st.header("SF Crawl -  Tatie Lou")
# st.write(GSCDf, width=1300)

GSCDf = GSCDf.fillna(value="NAN")

dfIndexable = GSCDf.loc[GSCDf["Indexability"] == "Indexable"]

with st.beta_expander("ℹ️ -  About the crawl format", expanded=False):

    st.write(
        """

-   Internal all.csv
-   Paste screenshot
	    
        """
    )


# st.markdown("---")
st.markdown("## **② Paste KWs/Broken links & Run  Model **")

linesDeduped2 = []

c0, c1, c2, c3, c4, c5, c6, c7 = st.beta_columns([0.8, 0.55, 1, 0.55, 1, 0.55, 1, 1.5])

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

with c5:
    st.text("")
    st.text("")
    st.text("")
with c6:
    RadioMapAgainst = st.radio(
        "Indexability span", options=("All crawled URLs", "Indexable only"), key=5
    )


c29, c30, c31 = st.beta_columns([1, 6, 1])

with c30:

    if RadioMapWhat == "Map Broken URLs":

        text2 = st.text_area("One per line (200 max)", height=275, key=2)
        lines2 = text2.split("\n")  # A list of lines2

        linesDeduped2 = []

        for x in lines2:
            linesDeduped2.append(x)

        c = st.beta_container()

    elif RadioMapWhat == "Map Keywords":

        # st.header("Paste Keywords")
        text2 = st.text_area("One per line (200 max)", height=275, key=3)
        lines2 = text2.split("\n")  # A list of lines2

        linesDeduped2 = []

        for x in lines2:
            linesDeduped2.append(x)

        c = st.beta_container()

        c30 = st.beta_container()


if text2:
    pass
else:
    st.success("⯅ Start by adding keywords or URLs in the box above")
    st.stop()


if RadioMapTo == "to URL":
    col_one_list = GSCDf["Address"].tolist()
elif RadioMapTo == "to H1":
    col_one_list = GSCDf["H1-2"].tolist()
else:
    col_one_list = GSCDf["Title 1"].tolist()


if RadioMapAgainst == "all crawled URLs":
    GSCDf = dfIndexable
else:
    pass


##########################################################

model = PolyFuzz("EditDistance")

start_execution = c30.button(" Run model! ✨ ")


model.match(linesDeduped2, col_one_list)
# Auto map by Similarity scores
Polyfuzz = model.get_matches()

Polyfuzz

st.stop()

#start_execution = c30.button(" 🚀✨Run model! ")
if start_execution:
 
    


    cm = sns.light_palette("red", as_cmap=True, reverse=True)
    FuzzStyled = Polyfuzz.style.background_gradient(cmap=cm)

    format_dictionary = {
        # "Probability (in %)": "{:.1%}",
        "Similarity": "{:.1%}",
    }

    FuzzStyled = FuzzStyled.format(format_dictionary)
    # st.table(dfFinal2)

    c2 = st.beta_container()

    c29, c30, c31 = st.beta_columns([1, 6, 1])

    with c30:

        # if RadioMapWhat == "Map Broken URLs":
        #
        #    text2 = st.text_area("One per line (100 max)", height=275, key=2)
        c = st.beta_container()

        st.table(FuzzStyled)

    try:
        csv = Polyfuzz.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        # c2.markdown("---")
        c2.markdown("## **③ Check mapping or download CSV **")

        c.subheader("")
        if RadioMapTo == "to URL":
            href = f'<a href="data:file/csv;base64,{b64}" download="Mapping_to_URL.csv">** ⯈ Download link 🎁 **</a>'
        elif RadioMapTo == "to H1":
            href = f'<a href="data:file/csv;base64,{b64}" download="Mapping_to_h1.csv">** ⯈ Download link 🎁 **</a>'
        else:
            href = f'<a href="data:file/csv;base64,{b64}" download="Mapping_to_title.csv">** ⯈ Download link 🎁 **</a>'
        c.markdown(href, unsafe_allow_html=True)

    except NameError:
        print("wait")

