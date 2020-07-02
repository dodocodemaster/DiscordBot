#!/usr/bin/env python3

from googleapiclient.discovery import build
import random

DEVELOPER_KEY = 'AIzaSyAMxv2lEGzHIM8Y2L8EJNr8LrUBZQWBja8'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(word):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=word,
    part='snippet',
    maxResults=100
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))

  if len(videos) == 0:
    result = "По запросу " + "{" + word + "} - нихуя не найдено!"
  else:
    result = 'https://www.youtube.com/watch?v=' + videos[random.randint(0, len(videos)-1)]

  return result
