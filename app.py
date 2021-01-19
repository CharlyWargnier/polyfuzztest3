from polyfuzz import PolyFuzz
from_list = ["https://www.tatielou.co.uk/apples/sadasda", "https://www.tatielou.co.uk/oranges/sadasda"]
to_list = ["https://www.tatielou.co.uk/apples/", "https://www.tatielou.co.uk/oranges/", "https://www.tatielou.co.uk/pears/"]
from_list = ["apple", "apples", "appl", "recal", "house", "similarity"]
to_list = ["apple", "apples", "mouse"]
model = PolyFuzz("EditDistance")
model.match(from_list, to_list)
# Auto map by Similarity scores
model.get_matches()