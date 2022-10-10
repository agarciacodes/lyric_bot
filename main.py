import lyricsgenius
import random
import tweepy

# set up twitter access keys
keys = {
	'CONSUMER_API_KEY': 'TWjkgrfmTMnjDQiT5HIyw405X',
	'CONSUMER_API_SECRET_KEY': 'Cn9nFqySicXl86fG88wA93GyiRrzLyB7q8qgV3Ge3nA1tJiclh',
	'ACCESS_TOKEN': '1312520754542632964-0NqA1PamRm4IhAImoL4QVtAClfZwCx',
	'ACCESS_TOKEN_SECRET': 'qwYqxKNueu9enXEpXbgRxwUbapQoxGVTyjwCbDxce6jgE'}

all_songs = ['Wat’s Wrong', '4r da Squaw', 'Heavenly Father', 'Shot You Down (Remix)', "Free Lunch", "Park", "Silkk da Shocka", "West Savannah", "Tity and Dolla", "Shot U Down", "R.I.P. Kevin Miller", "Ronnie Drake", "Smile", "Modest", "Stuck in the Mud", "Menthol", "AA", "Headshots (4r Da Locals)", "Rope // rosegold", "Soliloquy", "Webbie Flow (U Like)", "Cilvia Demo", "Banana", "Tranquility", "Dressed Like Rappers", "RIP Young", "Brad Jordan", "Bday", "Lay Wit Ya", "Find a Topic (homies begged)", "From the Garden", "Hereditary", "HB2U", "Nelly", "Brenda", "Hii (Fuck Love)", "Wat U Sed", "Claymore", "Part III", "A lot", "Darkseid", "where u at?", "Score", "THIB", "Chad", "Hurt Cobaine", "by george (outro)", "Hey Mista", "True Story", "2x Pills", "Don’t Matter", "GIL / Sounds from Friday Morning", "Mani Lux", "Sydney Jones", "Why Worry", "Weak Shit", "Food for Thought", "Fake Trill", "All Herb", "Don’t Shoot", "Grace", "200/Warning", "Like That", "Gusto", "9-3 Freestyle", "i mean", "Part II", "Khaki", "95", "RUNNIN’ 4RM DA LAW", "The Spill (Grammy Family Freestyle)", "The Race Freestyle", "Donuts", "RIP Young (Remix)", "XXL Freshman Freestyle", "Deep Blue", "Geordan Favors", "Part IV", "Runnin’", "Genius Freestyle 002", "Sounds from Friday Morning", "Slow Motion (Freestyle)", "Worm", "Calculator", "Fingernails*", "How I Started", "Elevators", "Fears", "Whales", "Punch Drunk (Love Love)", "Ain’t Trippin’", "Heavenly Father x TDE", "See", "Sway in the Morning Freestyle", "Seasons (Demo)", "Bat Cave*", "Monkey Bites BACK", "On My Mind*", "Gatorade", "Loose Change", "Vibers (Prayers)", "Demo Outro", "PEANUT", "Ashley", "Unknown", "Toca Tuesdays Freestyle", "GIL", "Junkies Interlude", "Mista Ride Tha Whip*", "Ask About Me", "S.B.B.B. (Goblin)", "Weak Shit 2*", "Wings Spread*", "PSA", "Group Freestyles", "Voyage to Atlanta", "Music (Where is He)", "Blaze*", "Voltron", "C.R.E.A.M.", "Dirty Sanchez", "Hoarder", "Villain", "Kabook*", "Chattanooga", "Mista", "Pulse", "Saturday*", "Up In Smoke”, 'Geek*', '2 Pills (Hands Out)', 'B32', 'Quicksand', 'RapFix Freestyle', 'From The Garden (Demo)', 'GAS', 'The Basement", 'From the Garden (OG)", "Vomit',
"Frozens", "Strange Love", "Ery’day Situations", "From The Garden (Original)", "Snippet", "Donuts (OG)", "Wat U Sed (OG)", "Break A Habit", "Score (OG)"]

# get a random song's lyrics

def get_raw_lyrics():
	genius_client_access_token = "_k7abKQsKkPRRxQi2JAdt3tGThZg7TeB9skk3F1DK1rE1bh436cBtBdWvyORS0EF"
	genius = lyricsgenius.Genius('_k7abKQsKkPRRxQi2JAdt3tGThZg7TeB9skk3F1DK1rE1bh436cBtBdWvyORS0EF')
	random_song_title = random.choice(all_songs)
	lyrics = genius.search_song(random_song_title, "Isaiah Rashad").lyrics
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

