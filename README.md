# Team_Julia_Recommender_System

A recommendation engine filters consumer data using different algorithms and recommends the most relevant items to users based on the users behaviour and what other users that have similar characteristics have purchased.

The task we have been presented with is to create a recommendation engine/system for lucid.blog a blog for created by ex-interns of HNG. We were presented with a database dump of the blog and our task was to recommend articles to users of the blog and suggestions of who to follow. 

From the database dump we were able to pull relevant features from tables.

There are two ways we can test this model. Reasons being we used the turicreate library to create the recommender system and we had diffculties installing it on windows.

**First and most recommended step to try out the model is**
1. Go to the colab https://colab.research.google.com/drive/1yaUUM9aWt2fdwy0EH6C5va01yCxUTit1#scrollTo=exaELg8KZdHV
2.Download the data from https://drive.google.com/drive/folders/1BOKo2EeCRQ-Z85t5hzEtGz1svEYB6GmK?usp=sharing
3. Upload the data to your google drive 
4. Run the colab and set the path to the data on your google drive. There are instructions on the colab notebooks that you can also follow.

You can also find the colab notebook in the colab_notebook folder.

**For the second method, you can**
1. Clone the repo to your local repo using git clone repo_url
2. cd into the cloned directory and locate the jupyter_model folder.
3. If you are using linux. Install turicreate using pip install turicreate
4. Run and test the model.
5. For instruction on how to test the model. A simpler guide is written on the notebook.

**Lastly, the model was deployed using flask.**
Note. You have to have turicreate installed locally on your system.
1. You have to clone the repo. Same way as described above.
2. cd into the deploy model folder.
3. Run the deploy.py file. Make sure the files are kept in that folder. Do Not take any file out.
To check if the model is working
1. go to this url on your browser

**For the follower rec_sys http://127.0.0.1:5000/recomend/user_id**
**For the article rec_sys http://127.0.0.1:5000/articles/user_id**

Take note user_id is a number 1-infinity
	For example, Imagine we want to recommend users and articles for a user with user_id= 1.  		The main url for recommending followers will be http://127.0.0.1:5000/recomend/1
	The main url for recommending articles will be http://127.0.0.1:5000/articles/1 




**You are likely to run into issues with the turicreate package, it installs natively on the MacOs and Linux , it also does install on Windows 10 using WSL 
checkout https://pypi.org/project/turicreate/ for directions as to how to go about doing that #




 
