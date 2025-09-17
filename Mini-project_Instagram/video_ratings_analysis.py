import pandas as pd
from sklearn.metrics import cohen_kappa_score
import matplotlib.pyplot as plt

# Loading dataset
ratings = pd.read_csv("Mini-project_Instagram/Ratings.csv")

# Cohen's kappa for appeal, clarity and creativity
kappa_1 = cohen_kappa_score(ratings[ratings["person"]=="A"]["appeal"], ratings[ratings["person"]=="B"]["appeal"])
kappa_2 = cohen_kappa_score(ratings[ratings["person"]=="A"]["clarity"], ratings[ratings["person"]=="B"]["clarity"])
kappa_3 =  cohen_kappa_score(ratings[ratings["person"]=="A"]["creativity"], ratings[ratings["person"]=="B"]["creativity"])


print("Appeal Cohen's Kappa:", kappa_1)
print("Clarity Cohen's Kappa:", kappa_2)
print("Creativity Cohen's Kappa:", kappa_3)
print("< 0 → worse than random, " \
"0.0-0.20 -- slight agreement, " \
"0.21-0.40 -- fair agreement, " \
"0.41-0.60 -- moderate agreement, " \
"0.61-0.80 -- substantial agreement, " \
"0.81-1.0 -- almost perfect agreement")

# Average rubric scores calculation
avg_ratings = ratings.groupby("id")[["appeal", "clarity", "creativity"]].mean()

# Normalizing engagement metrics by 1K of views: likes/views,  comments/views, saved/views, shared/views
engagement = ratings.groupby("id")[["views", "likes", "comments", "saved", "shared"]].mean()
engagement["likes_rate"] = round(engagement["likes"]/engagement["views"] * 1000, 2)
engagement["comments_rate"] = round(engagement["comments"]/engagement["views"] * 1000, 2)
engagement["saved_rate"] = round(engagement["saved"]/engagement["views"] * 1000, 2)
engagement["shared_rate"] = round(engagement["shared"]/engagement["views"] * 1000, 2)

# Merging average ratings and engamenet metrics
ratings_engagement = avg_ratings.merge(engagement, on = "id")
print(ratings_engagement)

# Calculation of correlation coefficients
corr = ratings_engagement.corr()
print(corr)

# Vizualizing rubic scores per video
ratings_engagement[["appeal", "clarity", "creativity"]].plot(kind = "bar")
plt.title("Average Rubic Scores for Videos")
plt.ylim(0,5)
plt.ylabel("Score")
plt.xlabel("Video id")
plt.xticks(rotation=0)
plt.show()