from polyfuzz import PolyFuzz

import streamlit as st
#from polyfuzz import PolyFuzz

#import polyfuzz

st.text('Test')

from_list = ["https://www.tatielou.co.uk/apples/sadasda", "https://www.tatielou.co.uk/oranges/sadasda"]
to_list = ["https://www.tatielou.co.uk/apples/", "https://www.tatielou.co.uk/oranges/", "https://www.tatielou.co.uk/pears/"]
from_list = ["apple", "apples", "appl", "recal", "house", "similarity"]
to_list = ["apple", "apples", "mouse"]

to_list

model = PolyFuzz("EditDistance")
model.match(from_list, to_list)
# Auto map by Similarity scores
Polyfuzz = model.get_matches()
Polyfuzz
st.write(Polyfuzz)


#model.match(linesDeduped2, col_one_list)
## Auto map by Similarity scores
#Polyfuzz = model.get_matches()
#Polyfuzz

