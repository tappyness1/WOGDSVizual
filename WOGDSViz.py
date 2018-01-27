import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import cycle, islice
import numpy as np
from matplotlib import cm as cmap
import matplotlib.cm as cm

memberdf = pd.read_csv("member.csv")
feeddf = pd.read_csv("feed.csv", encoding = "ISO-8859-1")
latlondf = pd.read_csv("latlon.csv")

# clean the agency column preliminarily
memberdf['Agency'] = memberdf['Agency'].str.replace('.gov.sg', '')
memberdf['Agency'] = memberdf['Agency'].str.replace('.edu.sg', '')
memberdf['Agency'] = memberdf['Agency'].str.upper()

# Join left for the user name and associated agency
feeddf = pd.merge(feeddf, memberdf, how = "left", left_on = "User ID", 
                  right_on= 'User ID')
feeddf = feeddf.dropna(axis = 0, subset = ['Agency', 'Name'])
# number of members by agency
numberinagency = memberdf['Agency'].value_counts()
# bar plot for the above
plt.figure(1)
numberinagency[:30].plot(kind = 'bar')
plt.title("Number of Members in each agency (Top 30)")
plt.xticks(rotation=90)
plt.grid(False)
plt.show()

# number of posts by agency
plt.figure(2)
postsperagency = feeddf['Agency'].value_counts()
postsperagency.plot(kind = 'bar')
plt.title("Number of Posts Per Agency")
plt.grid(False)
plt.xticks(rotation=90)
plt.show()

# make new df by number of posts per agency and number of member
agencydf = numberinagency.reset_index()
joindf = postsperagency.reset_index()
agencydf = pd.merge(agencydf, joindf, how = 'left', left_on = 'index', 
                    right_on = 'index')
agencydf.fillna(0, inplace = True)

# make post-to-member ratio by agency
agencydf['Agencies'] = agencydf['index']
agencydf['Post Ratio'] = agencydf['Agency_y'] / agencydf['Agency_x'] 
agencydf = agencydf.fillna(0)
agencydf.sort_values(by = ['Post Ratio'], ascending = False, inplace = True)
length = agencydf[agencydf['Post Ratio'] > 0].shape[0]
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(agencydf)))
plt.figure(3)
agencydf[:length].plot.bar(x ='Agencies', y = 'Post Ratio', color = my_colors)
plt.xticks(rotation=45)
plt.title("Avg Posts Per Member Per Agency")
plt.grid(False)
plt.show()
