#!/usr/bin/env python
# Filename: pywow.py

#imports
import requests
import json
from config import realm_relation

class Realm(object):
	'''
	Class description
	'''

	# Class Variables
	__base_url = "https://us.battle.net/api/wow/realm/status"
	__realms = realm_relation

	def __init__(self, name):
		self.name = name

	def __get_realm(self):
		return self.__realms[self.name]

	def __get_realm_data(self, url):
		r = requests.get(url)
		r = r.json()
		return r


	def get_realm_status(self):
		'''
		Function definition
		@return: True if the realm is up or False if the realm is down
		'''

		# Lookup the realm in realm_relation to get the index of the realm
		# For the query that we are going to perform on the api
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Status of the realm
		return results['realms'][realm_lookup]['status']


	def get_realm_population(self):
		'''
		Function definition
		@return: A string representing the realm get_realm_population
		'''

		# lookup the realm in the realm_relation to get the index of the realm
		# for the query that we are going to perform on the api.
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Population of the realm
		return results['realms'][realm_lookup]['population']


	def get_connected_realms(self):
		'''
		Function definition
		@return: an array of connected realms
		'''

		# lookup the realm in the realm_relation to get the index of the realm
		# for the query that we are going to perform on the api.
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Array of connected realms
		connected_realms = results['realms'][realm_lookup]['connected_realms']
		
		# Delete the first element of the list because it is itself
		del connected_realms[0]

		return connected_realms














	