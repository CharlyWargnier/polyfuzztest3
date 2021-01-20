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

# st.write(
#    "<style>div.row-widget.stRadio > div{flex-direction:row;}</style>",
#    unsafe_allow_html=True,
# )
#
# st.write(
#    "<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>",
#    unsafe_allow_html=True,
# )


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

# with c4:
#  st.markdown('###')
#  c = st.beta_container()
#  if uploaded_file:
#      st.success('✅ Nice! Your credentials are uploaded!')


# c29, c30, c31 = st.beta_columns([1, 6, 1])
#
# with c30:
#
#    # st.write("Multi-file uploader from ashikMultifile.py")
#    multiple_files = st.file_uploader("", accept_multiple_files=True)
#    for file in multiple_files:
#        file_container = st.beta_expander(f"File name: {file.name} ({file.size})")
#        data = io.BytesIO(file.getbuffer())
#        file_container.write(pd.read_csv(data, error_bad_lines=False))
#        file.seek(0)
#
#    dfs = [pd.read_csv(file) for file in multiple_files]
#
#    # st.write("Print 1st dataframe")
#    # st.write(dfs[0])
#
# uploaded_file = st.file_uploader("Choose a file NEW NEW NEW ")
# if uploaded_file is not None:
#    ## To read file as bytes:
#    # bytes_data = uploaded_file.read()
#    # st.write(bytes_data)
#    #
#    ## To convert to a string based IO:
#    # stringio = StringIO(uploaded_file.decode("utf-8"))
#    # st.write(stringio)
#    #
#    ## To read file as string:
#    # string_data = stringio.read()
#    # st.write(string_data)
#
#    # Can be used wherever a "file-like" object is accepted:
#    # with st.beta_expander("SADASDASD"):
#    dataframe = pd.read_csv(uploaded_file)
#    # file_container = st.beta_expander(f"File name: {file.name} ({file.size})")
#    st.write(dataframe)


# GSCDf = pd.read_csv("internal_all.csv")
GSCDf = pd.read_csv("Crawls_CSV\TatieLou_Internal_all.csv")
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
#start_execution = c30.button(" 🚀✨Run model! ")
if start_execution:

    ########## gIF NOT WORKING (UNBOUND)
    #
    #    # gif_runner = st.image(gif_path)
    #    c1, c2, c3 = st.beta_columns([5, 5, 5])
    #    with c2:
    #
    #        gif_runner = st.image("mouse.gif")
    #        model.match(linesDeduped2, col_one_list)
    #        # Auto map by Similarity scores
    #        Polyfuzz = model.get_matches()
    #        gif_runner.empty()

    model.match(linesDeduped2, col_one_list)
    # Auto map by Similarity scores
    Polyfuzz = model.get_matches()

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


st.stop()

COL_BOX1 = "Box #01"
COL_BOX2 = "Box #02"
COL_PARTIAL = "Partial"
COL_TOKEN_SET = "Token set"
COL_TOKEN_SORT = "Token sort"
MAX_LINES = 1000


if (len(linesDeduped1) > MAX_LINES) or (len(linesDeduped2) > MAX_LINES):
    linesDeduped1 = linesDeduped1[:MAX_LINES]
    linesDeduped2 = linesDeduped2[:MAX_LINES]
    st.success(
        f"⚠️ Only the first 1,000 keywords/URLs will be processed. More coming, stay tuned! 😊"
    )


# endregion text2_area_02  ############################################################


def ratio(row):
    name = row[COL_BOX1]
    name1 = row[COL_BOX2]
    return fuzz.ratio(name, name1)


def partial_ratio(row):
    name = row[COL_BOX1]
    name1 = row[COL_BOX2]
    return fuzz.partial_ratio(name, name1)


def token_sort_ratio(row):
    name = row[COL_BOX1]
    name1 = row[COL_BOX2]
    return fuzz.token_sort_ratio(name, name1)


def token_set_ratio(row):
    name = row[COL_BOX1]
    name1 = row[COL_BOX2]
    return fuzz.token_set_ratio(name, name1)


# d = dict( A = np.array([1,2]), B = np.array([1,2,3,4]) )
# pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))

st.stop()


@st.cache(allow_output_mutation=True)
def prepareDF(linesDeduped1, linesDeduped2):

    s1 = pd.Series(linesDeduped1, name=COL_BOX1)
    s2 = pd.Series(linesDeduped2, name=COL_BOX2)
    dfRatio = pd.concat([s1, s2], axis=1)
    dfRatio = dfRatio.replace(np.nan, "NaN", regex=True)

    # Ratio
    dfRatio[COL_PARTIAL] = dfRatio.apply(partial_ratio, axis=1)
    dfRatio[COL_TOKEN_SET] = dfRatio.apply(token_sort_ratio, axis=1)
    dfRatio[COL_TOKEN_SORT] = dfRatio.apply(token_set_ratio, axis=1)

    # Cast columns to float64
    dfRatio.astype(
        {
            COL_PARTIAL: np.float64,
            COL_TOKEN_SET: np.float64,
            COL_TOKEN_SORT: np.float64,
        },
        copy=False,
    )

    PartialRatio = pd.DataFrame({"ratio": dfRatio[COL_PARTIAL]})
    PartialRatio["algoType"] = COL_PARTIAL
    PartialRatio["ratioClass"] = np.where(
        dfRatio[COL_BOX1] == dfRatio[COL_BOX2],
        "Duplicate",
        np.where(
            dfRatio[COL_BOX2] == "/",
            "Redirects to Home P.",
            np.where(
                PartialRatio.ratio >= 70,
                "HighScore",
                np.where(PartialRatio.ratio >= 40, "MediumScore", "Low score"),
            ),
        ),
    )

    dfToken = pd.DataFrame({"ratio": dfRatio[COL_TOKEN_SORT]})
    dfToken["algoType"] = COL_TOKEN_SORT
    dfToken["ratioClass"] = np.where(
        dfRatio[COL_BOX1] == dfRatio[COL_BOX2],
        "Duplicate",
        np.where(
            dfRatio[COL_BOX2] == "/",
            "Redirects to Home P.",
            np.where(
                dfToken.ratio >= 70,
                "HighScore",
                np.where(dfToken.ratio >= 40, "MediumScore", "Low score"),
            ),
        ),
    )

    dfTokenSet = pd.DataFrame({"ratio": dfRatio[COL_TOKEN_SET]})
    dfTokenSet["algoType"] = COL_TOKEN_SET
    dfTokenSet["ratioClass"] = np.where(
        dfRatio[COL_BOX1] == dfRatio[COL_BOX2],
        "Duplicate",
        np.where(
            dfRatio[COL_BOX2] == "/",
            "Redirects to Home P.",
            np.where(
                dfTokenSet.ratio >= 70,
                "HighScore",
                np.where(dfTokenSet.ratio >= 40, "MediumScore", "Low score"),
            ),
        ),
    )

    dfNew = PartialRatio.append([dfToken, dfTokenSet])

    dfPivot1 = pd.pivot_table(
        dfNew, values="ratio", index=["ratioClass", "algoType"], aggfunc=len
    ).reset_index("algoType")
    dfPivot1["ratioName"] = dfPivot1.index
    dfPivot1["algoType"] = dfPivot1.replace(
        {
            "algoType": {
                COL_TOKEN_SET: "Token Set ratio count",
                COL_TOKEN_SORT: "Token Sort ratio count",
                COL_PARTIAL: "Partial count",
            }
        }
    )

    dfTemplate = pd.DataFrame(
        {
            "algoType": [
                "Partial count",
                "Token Set ratio count",
                "Token Sort ratio count",
                "Partial count",
                "Token Set ratio count",
                "Token Sort ratio count",
                "Partial count",
                "Token Set ratio count",
                "Token Sort ratio count",
                "Partial count",
                "Token Set ratio count",
                "Token Sort ratio count",
            ],
            "ratio": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "ratioName": [
                "Duplicate",
                "Duplicate",
                "Duplicate",
                "HighScore",
                "HighScore",
                "HighScore",
                "MediumScore",
                "MediumScore",
                "MediumScore",
                "Low score",
                "Low score",
                "Low score",
            ],
        }
    )

    dfMerged3 = pd.concat([dfTemplate, dfPivot1])
    dfMerged3.drop_duplicates(
        subset=["algoType", "ratioName"], inplace=True, keep="last"
    )
    dfMerged3 = dfMerged3.sort_values(["ratioName", "algoType"], ascending=[True, True])

    dfPivotFiltered1 = dfMerged3.loc[dfMerged3["ratioName"] == "HighScore"]
    dfPivotFiltered2 = dfMerged3.loc[dfMerged3["ratioName"] == "MediumScore"]
    dfPivotFiltered3 = dfMerged3.loc[dfMerged3["ratioName"] == "Duplicate"]
    dfPivotFiltered4 = dfMerged3.loc[dfMerged3["ratioName"] == "Low score"]

    listHighScore = dfPivotFiltered1["ratio"].tolist()
    listMediumScore = dfPivotFiltered2["ratio"].tolist()
    listLow = dfPivotFiltered4["ratio"].tolist()
    listDuplicate = dfPivotFiltered3["ratio"].tolist()

    # Compute duplicates
    dfRatio["Duplicate"] = np.where(
        dfRatio[COL_BOX1] == dfRatio[COL_BOX2],
        "Duplicate",
        np.where(dfRatio[COL_BOX2] == "/", "Redirects to Home P.", "No duplicate"),
    )

    # Cast columns to int64
    dfRatio.astype(
        {
            COL_PARTIAL: np.int64,
            COL_TOKEN_SET: np.int64,
            COL_TOKEN_SORT: np.int64,
        },
        copy=False,
    )

    return {
        "df": dfRatio,
        "duplicate": listDuplicate,
        "unique_duplicate": dfRatio["Duplicate"].unique(),  # Not used
        "scores": {
            "low": listLow,
            "medium": listMediumScore,
            "high": listHighScore,
        },
        "range": {
            COL_PARTIAL: {
                "min": dfRatio[COL_PARTIAL].min(),
                "max": dfRatio[COL_PARTIAL].max(),
            },
            COL_TOKEN_SET: {
                "min": dfRatio[COL_TOKEN_SET].min(),
                "max": dfRatio[COL_TOKEN_SET].max(),
            },
            COL_TOKEN_SORT: {
                "min": dfRatio[COL_TOKEN_SORT].min(),
                "max": dfRatio[COL_TOKEN_SORT].max(),
            },
        },
    }


data = prepareDF(linesDeduped1, linesDeduped2)


st.markdown("## ** ▼ Check results or download CSV **")

c1, c2 = st.beta_columns(2)

with c1:
    with st.beta_expander("ℹ️ - More info about scores", expanded=False):

        st.write(
            """        
            -   high score means anything above
            -   medium score means anything above
            -   low score means anything above
                    """
        )

with c2:

    with st.beta_expander("ℹ️ - More info about algos", expanded=False):

        st.write(
            """        
            -   Algo 1
            -   Algo 2
                    """
        )

st.markdown("")

Algolist = []

c1000 = st.beta_container()

c0, c0a, c1, c1a, c2, c2a, c3 = st.beta_columns([6, 0.2, 6, 1, 6, 1, 6])

with c1:
    two = st.checkbox("Partial Ratio", value=True)
    c1 = st.beta_container()
    if two:
        Algolist.append("Partial Ratio")

with c3:
    three = st.checkbox("Token Sort Ratio", value=True)
    c3 = st.beta_container()
    if three:
        Algolist.append("Token Sort Ratio")

with c2:
    one = st.checkbox("Token Set Ratio", value=True)
    c2 = st.beta_container()
    if one:
        Algolist.append("Token Set Ratio")

scores = [
    "High score (70-100)",
    "Medium score (40-70)",
    "Low score (0-40)",
    "Duplicate",
]

opts = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "color": ["#808080", "#6AB155", "#fb8649", "#FF0000"],
    "legend": {"data": scores},
    "textStyle": {
        "fontSize": "13",
    },
    "grid": {"left": "13%", "right": "14%", "bottom": "13%", "containLabel": False},
    "xAxis": {"type": "value"},
    "yAxis": {"type": "category", "data": Algolist},
    "series": [
        {
            "name": "Duplicate",
            "type": "bar",
            "stack": "01",
            "label": {"show": True, "position": "insideLeft"},
            "data": data["duplicate"],
        },
        {
            "name": "High score (70-100)",
            "type": "bar",
            "stack": "01",
            "label": {"show": True, "position": "insideLeft"},
            "data": data["scores"]["high"],
        },
        {
            "name": "Medium score (40-70)",
            "type": "bar",
            "stack": "01",
            "label": {"show": True, "position": "insideLeft"},
            "data": data["scores"]["medium"],
        },
        {
            "name": "Low score (0-40)",
            "type": "bar",
            "stack": "01",
            "label": {"show": True, "position": "insideLeft"},
            "data": data["scores"]["low"],
        },
    ],
}

with c1000.beta_container():
    st_echarts(opts, width=1600, height=375, key="chart")

# region multiselect ############################################################

# Note from Synode
# No need to copy
# The following filtering operations won't alter the dataframe (no column drop), they just define a "view"
dfFiltered = data["df"]


def filter_if(condition, df, column, error_msg, step=1, key=None):
    if not condition:
        # Filter out the column, does not drop it
        return df[df.columns.difference([column])]

    else:
        value_min = int(data["range"][column]["min"])
        value_max = int(data["range"][column]["max"])

        if value_min < value_max:
            slider_value = st.slider(
                "", value_min, value_max, value=value_max, step=step, key=key
            )
            df = df[(df[column] <= slider_value)]
        else:
            pass

        return df


with c2:
    error_msg = "No T-Set slider as `minValue` == `maxValue`"
    dfFiltered = filter_if(one, dfFiltered, COL_TOKEN_SET, error_msg, key=10)

with c1:
    error_msg = "No Partial slider as `minValue` == `maxValue`"
    dfFiltered = filter_if(two, dfFiltered, COL_PARTIAL, error_msg)

with c3:
    error_msg = "No T-Sort slider as `minValue` == `maxValue`"
    dfFiltered = filter_if(three, dfFiltered, COL_TOKEN_SORT, error_msg, key=1)

loopBox = c0.checkbox("Only show duplicates", key=100)

c0.write("")
c0.write("")

if loopBox:
    dfFiltered = dfFiltered[dfFiltered["Duplicate"] == "Duplicate"]


def where(x):
    bg = ["red", "peachpuff"]
    fg = ["white", "black"]
    ls = ["Duplicate", "Redirects to Home P."]
    for i, y in enumerate(ls):
        if y in x:
            return f"background-color: {bg[i]}; color: {fg[i]}"
    return ""


try:
    # tips from Arran - remove index from st.table tables
    dfFiltered.index = dfFiltered.index + 1

    # st.markdown("---")
    # st.table(dfFiltered.style.background_gradient(axis=None, cmap='Reds_r')\
    st.table(
        dfFiltered.style.background_gradient(axis=None, cmap="RdYlGn").applymap(
            where, subset=["Duplicate"]
        )
    )
except ValueError:
    pass

try:
    csv = dfFiltered.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_table.csv">**   ⯈ Download filtered table 🎁**</a>'
    c0.markdown(href, unsafe_allow_html=True)

except NameError:
    print("wait")

except NameError:
    st.markdown("NameError")

with st.beta_expander("ℹ️ - To-do's ", expanded=True):

    st.write(
        """  

-   Change color codes in table to do a shade from green to red
-   Change rules to 70
-   Remove commented out code
-   Remove boxes
-   Do overall debug
-   Add Info about algos
-   Add Use cases about fuzz matching
-   Tweak logo

	    """
    )


with st.beta_expander("ℹ️ - Fixed ", expanded=False):
    # st.markdown(" text to add - https://docs.google.com/document/d/1z9X16ZF0d-T2hc2JEp3EPpbaJfUlpfRDRO0tNsK1ZHs/edit")

    st.write(
        """  
    
-   fix index in table
-   Add a stop so charts can't be seen if no data (at start)
-   try with 20K URLs (too slow!)
-   try with 10K URLs (too slow!)
-   Add exception 01: add content in both boxes otherwise error
-   Fix ValueError when one box is emptu: arrays must all be same length
-   Remove dupe in 'Only the first 1000 elements'
-   Cached NOT WORKING! (too long to get data in table when sliders are changed)
-   Add many URLs - from logs
-   Add cache to score classifiers 
-   Add cache to sliders -if one == True etc...
-   remove error: Only the 5 first URLs will be reviewed
-   Increase allowance to 1000
-   Change yellow to orange?
-   Review scores bracket
-   Add Info about scores
-   Change colour charts
-   increase legend size
-   ratios - remove underscores in names
-   re-order columns with partial 1st
-   remove decimals in sliders
-   Amend index in last table!!!!!!!!
-   create a list for low scores - otherwise won't appear in charts
-   remove index in last table
-   biggest issue: created lists don't add up properly and incorrect reading in charts - paste URLs to find out    
-   check -> https://colab.research.google.com/drive/1GZKKPtOCjjic5tbnr9mPzFKGMHnzrEvp#scrollTo=enTISRhUvSK1 
-   issue with labels - invert toekn sort and set!
-   put medium scores on the left of the chart, to be visible
-   Add duplicate in Add search box forain token columns, otherwise biased!

	    """
    )

with st.beta_expander("ℹ️ - Maybe? ", expanded=False):
    # st.markdown(" text to add - https://docs.google.com/document/d/1z9X16ZF0d-T2hc2JEp3EPpbaJfUlpfRDRO0tNsK1ZHs/edit")

    st.write(
        """  
    
-   Add a toggle button for text areas

	    """
    )


with st.beta_expander("ℹ️ - Still To-Do! ", expanded=False):
    # st.markdown(" text to add - https://docs.google.com/document/d/1z9X16ZF0d-T2hc2JEp3EPpbaJfUlpfRDRO0tNsK1ZHs/edit")

    st.write(
        """  
    
-   Optimise speed and cached functions
-   Display indicators (# of elements imported,filtered etc..)
-   Add percentages in chart
-   Add more than 1000 URLs
-   sort by partial or token score
-   sort high scores only
-   add one more ratio
-   add bi dirwctional sliders
-   add histogram/distribution per ratio
-   box 1 and 2 - Add search box - Needs to do 'or' not 'and'
-   Add score class in dupe columns

	    """
    )
