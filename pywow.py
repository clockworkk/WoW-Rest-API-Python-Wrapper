#!/usr/bin/env python
# Filename: pywow.pywow

#imports
import requests
import json
from config import realm_relation

class Pywow(object):
	'''
	Class description
	'''

	# Class Variables
	__base_url = "https://us.battle.net/api/wow/"
	__realms = realm_relation

	def __get_realm_status(self, url, data, headers):
		r = requests.get(url, headers=headers)
		return r

	def get_realm_status(self, name):
		'''
		Function definition
		@return: True if the realm is up or False if the realm is down
		'''
		realm_lookup = self.__realms[name]
		url = self.__base_url + 'realm/status'
		headers = None
		data = None

		# Get the current status of all realms
		results = self.__get_realm_status(url, data, headers)
		results = results.json()

		# Status of the realm
		return results['realms'][realm_lookup]['status']





	