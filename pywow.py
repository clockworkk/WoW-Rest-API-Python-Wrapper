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
		Depends on if the realm is up, should put a try catch for if the realm is up
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


	def get_battlegroup(self):
		'''
		Function definition
		@return a string of what battlegroup the realm belongs to.
		'''

		# lookup the realm in the realm_relation to get the index of the realm
		# for the query that we are going to perform on the api.
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Battlegroup that the given realm belongs to
		return results['realms'][realm_lookup]['battlegroup']


	def get_timezone(self):
		'''
		Function definition
		@return a string that represents the timezone
		'''

		# lookup the realm in the realm_relation to get the index of the realm
		# for the query that we are going to perform on the api.
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Timezone that the given realm belongs to
		return results['realms'][realm_lookup]['timezone']


	def get_tb_data(self):
		'''
		Function definition
		@return a dictionary with useful data
		'''
		#Function Variables
		tb_data = {}

		# lookup the realm in the realm_relation to get the index of the realm
		# for the query that we are going to perform on the api.
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Timezone that the given realm belongs to
		results = results['realms'][realm_lookup]['tol-barad']

		next_start = results['next']
		controlling_faction = results['controlling-faction']
		status = results['status']
		num_players = results['area']

		# Convert next start to a time

		# Convert the numerical value to the faction they correspond to
		if (controlling_faction == 0):
			controlling_faction = "Alliance"
		else:
			controlling_faction = "Horde"

		# Change the status to the coressponding value they represent
		if(status == 0):
			status = "Idle"
		else if (status = 1):
			status = "Populating"
		else if (status = 2):
			status = "Active"
		else if (status = 3):
			status = "Concluded"
		else:
			status = "Unknown"

		# Populate the dictionary with its data
		tb_data = {
			'next_start' : next_start,
			'controlling' : controlling_faction,
			'status' : status,
			'zone_population' : num_players
		}

		return tb_data


	def get_wg_data(self):
		'''
		Function definition
		@return a dictionary with useful data
		'''
		#Function Variables
		wg_data = {}

		# lookup the realm in the realm_relation to get the index of the realm
		# for the query that we are going to perform on the api.
		realm_lookup = self.__get_realm()

		# Get the current stats of all realms
		results = self.__get_realm_data(self.__base_url)

		# Timezone that the given realm belongs to
		results = results['realms'][realm_lookup]['wintergrasp']

		next_start = results['next']
		controlling_faction = results['controlling-faction']
		status = results['status']
		num_players = results['area']

		# Convert next start to a time

		# Convert the numerical value to the faction they correspond to
		if (controlling_faction == 0):
			controlling_faction = "Alliance"
		else:
			controlling_faction = "Horde"

		# Change the status to the coressponding value they represent
		if(status == 0):
			status = "Idle"
		else if (status = 1):
			status = "Populating"
		else if (status = 2):
			status = "Active"
		else if (status = 3):
			status = "Concluded"
		else:
			status = "Unknown"

		# Populate the dictionary with its data
		wg_data = {
			'next_start' : next_start,
			'controlling' : controlling_faction,
			'status' : status,
			'zone_population' : num_players
		}

		return wg_data


class Guild(object):
	'''
	Class description
	'''

	# Class variables
	__base_url = "https://us.battle.net/api/wow/guild"

	def __init__(self, realm, guild):
		realm = realm.replace(" ", "%20")
		self.realm = realm
		self.guild = "/" + guild

	def __get_guild_data(self, url):
		r = requests.get(url)
		r = r.json()
		return r

	def get_members(self):
		'''
		Function definition
		@return the number of members for a given guild
		'''

		#Function Variables
		url = self.__base_url + self.realm + self.guild + "?fields=members"
		
		# Query the api for guild information
		guild_lookup = self.__get_guild_data(url)

		# Return the number of members the guild has
		


























	