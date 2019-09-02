# TwitterProfiling

## Introduction

**TwitterProfiling** is a tool which provides an easy way to generate a preferences profile of a given Twitter user.

Here are all the possible categories to classify a user:
- Music and Radio
- Movies
- Videogames
- Books and Literature
- Careers
- Personal Health
- Religion and Spirituality
- Home and Garden
- Personal Finance
- Pets and Animals
- Shopping
- Travel
- Automotive
- Fine Art
- Science
- News and Politics
- Education
- Food and Drink
- Financial and Business
- Family and Relationships
- Style and Fashion
- Medical Health
- Software and Technology
- Events
- Hobbies and Pop Culture
- Sports

## Installation

To install the latest version of **TwitterProfiling**, download the repo as a [zip](https://github.com/bisite/TwitterProfiling/archive/master.zip) and run:

``pip install TwitterProfiling-master.zip``

Dependecies are listed on the setup file of the package. The use of a [virtualenv](https://virtualenv.pypa.io/en/latest/) is encouraged to prevent problems with the specific versions required, i.e.:
```
virtualenv twiprofenv
source twiprofenv/bin/activate
pip install TwitterProfiling-master.zip
```

To start the Flask server run ```twitterprofiling``` and check out [localhost:5000](http://localhost:5000) to see the API documentation.


**IMPORTANT**

To use TwitterProfiling you need to create a [Twitter application](https://developer.twitter.com/en/docs/basics/apps/overview), in order to  get the [acces tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html) and connect with the Twitter API service.

## How to use as a Python package
First of all, import the module

``from twitterprofiling import TwitterProfiling``

This next line, creates an instance of TwitterProfiling for the specified user **username**.
It also retrieves user's tweets. By default, number_of_tweets is 1200. You can decrease the value to get better execution times, but the prediction
accuracy will be penalized.
You will need to provide the credentials fot the Twitter API.

``new_user = TwitterProfiling('Tesla', consumer_key, consumer_secret, access_token, access_token_secret, number_of_tweets=1200)``

Now you can display the user's name, username, image and description.

``new_user.get_user_name()``

``new_user.get_user_username()``

``new_user.get_user_image()``

``new_user.get_user_description()``

You can also retrieve the hashtags terms count, the tweet terms count and the topics terms count:

``res = new_user.get_hashtags_terms_count()``

``res = new_user.get_tweets_terms_count()``

``res = new_user.get_topics_top_terms(nterms=30)``

To retrieve the user timeline:

``new_user.search_user_timeline(number_of_tweets)``


Now, classify the tweets with the model and get the results in a dictionary with:

``res = new_user.get_user_classification()``

## Example results

Here is the result of a simple TwitterProfiling use. **Here I only expose the top 3 categories** for each user, but all them are returned in the dictionary.

| Username  | First Category | Second Category | Third Category |
| ----- | -------------- | --------------- | -------------- |
| Tesla  | Automotive (70.92%)  | Software and Technology (10.07%) | Travel (3.86%)|
| realDonaldTrump  | News and Politics (28.02%)  | Financial and Business (11.36%) | Sports (8.02%)|
| sciencemagazine | Science (24.41%) | Medical Health (16.73%) |  Education (12.03%) |
| NintendoAmerica | Videogames (41.65%) | Hobbies and Pop Culture (12.19%) | Sports (9.74%) |

## Disclaimer

Please, bear in mind that TwitterProfiling has been developed only for research purpose. Make sure that you don't store
the results obtained with TwitterProfiling and, in any case, don't use this results with comercial purposes.

TwitterProfiling efficiency and accuracy have been tested with enterprise accounts like Nintendo or Tesla, and also with public figures accounts, like Theresa May or Pontifex.
If you want to analyse personal accounts, even if them are public, make sure you have the explicit consent.
