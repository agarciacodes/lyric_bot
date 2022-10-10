import lyricsgenius
import random
import tweepy

# set up twitter access keys
keys = {
	'CONSUMER_API_KEY': 'COSUMER_API_KEY_HERE',
	'CONSUMER_API_SECRET_KEY': 'CONSUMER_API_SECRET_KEY_HERE',
	'ACCESS_TOKEN': 'ACCESS_TOKEN_HERE',
	'ACCESS_TOKEN_SECRET': 'ACCESS_TOKEN_SECRET_HERE'}

all_songs = [list_of_your_artist_song_here]

# get a random song's lyrics

def get_raw_lyrics():
	genius_client_access_token = "genius_client_access_token_here"
	genius = lyricsgenius.Genius('genius_client_access_token_here')
	random_song_title = random.choice(all_songs)
	lyrics = genius.search_song(random_song_title, "Artist_name").lyrics
	song = random_song_title.upper()
	return lyrics, song

# cleaning up lyrics

def get_tweets_from(lyrics):
	lines = lyrics.split('\n')
	for index in range(len(lines)):
		if lines[index] == "" or "[" in lines[index]:
			lines[index] = "XXX"
	lines = [i for i in lines if i != "XXX"]
	random_num = random.randrange(0, len(lines)-1)
	tweet = lines[random_num] + "\n" + lines[random_num+1]
	tweet = tweet.replace("\\", "")
	return tweet

def handler(event, context):
	auth = tweepy.OAuthHandler(
		keys['CONSUMER_API_KEY'],
		keys['CONSUMER_API_SECRET_KEY']
	)
	auth.set_access_token(
		keys['ACCESS_TOKEN'],
		keys['ACCESS_TOKEN_SECRET']
	)
	api = tweepy.API(auth)
	lyrics, song = get_raw_lyrics()
	tweet = get_tweets_from(lyrics)
	status = api.update_status(tweet)
	# if someone @s asking what song, insert functionality
	return tweet



# above function is handler for lambda
# tutorial by Mahib Hosain medium.com

