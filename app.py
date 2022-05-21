# save this as app.py
#import torch
from flask import Flask, request, jsonify
import pickle
import numpy as np
import movierec
#from torch.nn import MatrixFactorization
#model = torch.load('model/pytorch_resnet50.pth',map_location ='cpu')
from movierec import kmeans, train_set, ratings_df, movie_names


#model = pickle.load(open('model_pkl', 'rb'))
with open('model_pkl', 'rb') as files:
  lr = pickle.load(files)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/recommend', methods=['POST'])

  #str1 = ''

def recommend():
  import re
  #kw = input("Enter the keywords: ")
  movie_name = request.form.get('movie_name')
  str1 = ''
  for cluster in range(100):
    movs = []
    recs = []
    for movidx in np.where(kmeans.labels_ == cluster)[0]:
      movid = train_set.idx2movieid[movidx]
      rat_count = ratings_df.loc[ratings_df['movieId']==movid].count()[0]
      movs.append((movie_names[movid], rat_count))
    for mov in sorted(movs, key=lambda tup: tup[1], reverse=True)[:10]:
      recs.append(mov[0])
    for r in recs:
      flag=0
      if (re.search( movie_name, r , re.IGNORECASE)) :
        flag=1
        print("The selected movie is "+ r )
        str1+= "The selected movie is "+ r +'\n'
        recs.remove(r)
        print("You might also want to watch: ")
        str1+= "You might also want to watch: " + '\n'
        for m in recs:
          print(m)
          str1+= m + '\n'
        recs.append(r)
      if(flag==1):
        break

  return jsonify(str1)


if __name__ == '__main__':
    #movierec.main();
    app.run()
