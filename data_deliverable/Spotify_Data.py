#imports needed modules and libraries 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# authorization.json -> responsible for storing and accessing the tokens
# playlists_like_dislike.json -> manage URL for multiple playlists
# can fetch data of up to 99 songs in a single connection session

#load credential from authorization.json
credentials = json.load(open('/Users/mohammedakel/Desktop/CS1951A-Spring2022/Final_Project/authorization.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

print(client_id)
print(client_secret)

#index and load playlists from playlists_like_dislike.json
playlists_json = json.load(open('/Users/mohammedakel/Desktop/CS1951A-Spring2022/Final_Project/playlists_like_dislike.json'))
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = playlists_json[0]["uri"]
username = uri.split(':')[0]
playlist_id = uri.split(':')[2]

playlists_row = []
for playlist_info in playlists_json:
    uri = playlist_info["uri"]
    username = uri.split(':')[0]
    playlist_id = uri.split(':')[2]
    temp = sp.playlist(playlist_id)
    playlists_row.append(temp)

tracks_details = {}
tracks_row = []       
for playlist in playlists_row:
    playlist_tracks_data = playlist['tracks']
    items = playlist_tracks_data['items']
    for track in items: 
        track_id = track['track']['id']
        track_title = track['track']['name']
        artisits = []
        for artist in track['track']['artists']:
            artisits.append(artist['name'])
        track_popularity = track['track']['popularity']
        track_expicit = track['track']['explicit']
        features = sp.audio_features(track_id)
        track_dancability = features[0]['danceability']
        track_liveness = features[0]['liveness']
        track_Loudness = features[0]['loudness']
        track_speechniess = features[0]['speechiness']
        track_instrumental = features[0]['instrumentalness']
        track_acoustic = features[0]['acousticness']
        track_energy = features[0]['energy']
        track_tempo = features[0]['tempo']
        track_valence = features[0]['valence']
        track_duration = features[0]['duration_ms']
        track_info = {
                      "tittle": track_title,
                      "artists": artisits,
                      "popularity": track_popularity,
                      "explicit": track_expicit,
                      "liveness": track_liveness,
                      "loudness": track_Loudness,
                      "speechiness": track_speechniess,
                      "instrumentalness": track_instrumental,
                      "energy": track_energy,
                      "tempo": track_tempo,
                      "valence": track_valence,
                      "duration_ms": track_duration,
                      "acousticness": track_acoustic,
                      "dancibility": track_dancability
                      }
    tracks_details[track_id] = track_info

print(len(tracks_details))
print(tracks_details)
'''
// get all playlists by spotify or a given user

username = "spotify"
playlists = sp.user_playlists(username)
count = 5 
while playlists and count>0:
    for i, playlist in enumerate(playlists['items']):
        count = count -1; 
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
'''



print("END")

