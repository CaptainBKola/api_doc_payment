from flask import *
import tweepy

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"success":True,"message":"Hello World!"})

@app.route("/get-tweet/")
def get_tweet():

    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        username=request.args.get("username")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        tweets = api.user_timeline(screen_name=username)
        data=[]
        for t in tweets:
            data.append([{'tweet': t.text,
                      'created_at': t.created_at,
                      'username': username,
                      'headshot_url': t.user.profile_image_url}])
        return jsonify({"success":True,"data":data})
    except:
        return jsonify({"success": False})

@app.route("/post-tweet/")
def post_tweet():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        tweet=request.args.get("tweet")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        api.update_status(status=tweet)
        return jsonify({"success": True,"Name":user.name,"Location":user.location,"friends":user.friends_count})
    except:
        return jsonify({"success": False})

@app.route("/get-status/")
def get_status():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        count=request.args.get("count")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        statuses = api.home_timeline(count=count)

# printing the screen names of each status
        data=[]
        for status in statuses:
            data.append({"status":status.user.screen_name})
        return jsonify({"success":True,"data":data})
    except:
        return jsonify({"success": False})

@app.route("/post-status/")
def post_status():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        status=request.args.get("status")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


# posting the tweet
        api.update_status(status)
        return jsonify({"success": True})
    except:
        return jsonify({"success": False})

@app.route("/get-friends/")
def get_friends():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        screen_name = request.args.get("screen_name")

# printing the latest 20 friends of the user
        data=[]
        for friend in api.friends(screen_name):
            data.append({"friend":friend.screen_name})
        return jsonify({"success":True,"data":data})
    except:
        return jsonify({"success": False})
@app.route("/get-follower/")
def get_followers():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        screen_name = request.args.get("screen_name")

# printing the latest 20 friends of the user
        data=[]
        for follower in api.followers(screen_name):
            data.append({"follower":follower.screen_name})
        return jsonify({"success":True,"data":data})
    except:
        return jsonify({"success": False})

@app.route("/get-retweets/")
def get_retweets():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        username=request.args.get("username")
        count=request.args.get("count")
        ID=request.args.get("ID")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        retweets_list = api.retweets(ID)

# printing the latest 20 friends of the user
        data=[]
        for retweet in retweets_list:
            data.append({"retweet":retweet.user.screen_name})
        return jsonify({"sucess":True,"data":data})
    except:
        return jsonify({"success": False})
@app.route("/post-retweet/")
def post_retweet():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        username=request.args.get("username")
        count=request.args.get("count")
        ID=request.args.get("ID")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        api.retweet(ID)
        return jsonify({"success":True})
    except:
        return jsonify({"success": False})

@app.route("/post-media-tweet/")
def post_media_tweet():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        status=request.args.get("status")
        file=request.args.get("file")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        user = api.me()



        api.update_with_media(file, status)
        return jsonify({"success":True})
    except:
        return jsonify({"success": False})

@app.route("/get-user/")
def get_user():
    try:
        consumer_key = request.args.get("consumer_key")
        consumer_secret = request.args.get("consumer_secret")
        access_token = request.args.get("access_token")
        access_token_secret=request.args.get("access_token_secret")
        query=request.args.get("query")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)


        users = api.search_users(query)

# print the users retrieved
        data=[]
        for user in users:
            data.append({"user":user.screen_name})
        return jsonify({"success":True,"data":data})
    except:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run(debug=True)
