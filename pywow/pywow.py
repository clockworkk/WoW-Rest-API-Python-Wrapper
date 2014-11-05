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

		# Convert next start to a time

		# Convert the numerical value to the faction they correspond to
		if (controlling_faction == 0):
			controlling_faction = "Alliance"
		else:
			controlling_faction = "Horde"

		# Change the status to the coressponding value they represent
		if(status == 0):
			status = "Idle"
		elif (status == 1):
			status = "Populating"
		elif (status == 2):
			status = "Active"
		elif (status == 3):
			status = "Concluded"
		else:
			status = "Unknown"

		# Populate the dictionary with its data
		tb_data = {
			'next_start' : next_start,
			'controlling' : controlling_faction,
			'status' : status,
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
		elif (status == 1):
			status = "Populating"
		elif (status == 2):
			status = "Active"
		elif (status == 3):
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
		pass

	def get_data(self):
		'''
		Function definition
		@return the number of members for a given guild
		'''

		#Function Variables
		url = self.__base_url + self.realm + self.guild
		
		# Query the api for guild information
		guild_lookup = self.__get_guild_data(url)
		pass


	def get_news(self):
		'''
		Function definition
		@return the number of members for a given guild
		'''

		#Function Variables
		url = self.__base_url + self.realm + self.guild + "?fields=news"
		
		# Query the api for guild information
		guild_lookup = self.__get_guild_data(url)
		pass


	def get_achievements(self):
		'''
		Function definition
		@return the number of members for a given guild
		'''

		#Function Variables
		url = self.__base_url + self.realm + self.guild + "?fields=achievements"
		
		# Query the api for guild information
		guild_lookup = self.__get_guild_data(url)
		pass


	def get_challenge(self):
		'''
		Function definition
		@return the number of members for a given guild
		'''

		#Function Variables
		url = self.__base_url + self.realm + self.guild + "?fields=challenge"
		
		# Query the api for guild information
		guild_lookup = self.__get_guild_data(url)
		pass

	


class Character(object):
	'''
	Class description
	'''

	# Class Variables
	__base_url = "https://us.battle.net/api/wow/character"

	# Finsih
	def __init__(self, realm, character):
		realm = self.realm
		character = self.character

	def __get_character_data(self, url):
		r = requests.get(url)
		r = r.json()
		return r

	def get_achievements(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=achievements"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only achivement information
		return results



	def get_appearance(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=appearance"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only appearance information
		return results


	def get_activity_feed(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=feed"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only feed information
		return results


	def get_guild(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=guild"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only guild information
		return results


	def get_hunter_pets(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=hunterPets"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only hunterPets information
		return results


	def get_items(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=items"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only item information
		return results


	def get_mounts(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=mounts"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only mount information
		return results


	def get_pets(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=pets"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only pets information
		return results


	def get_pet_slots(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=petSlots"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only pet slots information
		return results


	def get_professions(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=professions"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only profession information
		return results	


	def get_progression(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=progression"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only progression information
		return results


	def get_pvp(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=pvp"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only pvp information
		return results


	def get_quests(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=quests"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only quest information
		return results


	def get_reputation(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=reputation"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only reputation information
		return results


	def get_stats(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=stats"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only stat information
		return results


	def get_talents(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=talents"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only talents information
		return results


	def get_titles(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=titles"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only titles information
		return results


	def get_audit_data(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=audit"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only audit information
		return results

	def get_all_data(self):
		''' 
		Function definition
		'''
		
		# Function variables
		url = self.__base_url + self.realm + self.character + "?fields=achievements,appearance,feed,guild,hunterPets,items,mounts,pets,petSlots,professions,pvp,quests,reputation,stats,talents,titles,audit"

		# Query the api for character information
		results = __get_character_data(url)

		# Potentially modify this to return only all information
		return results






















	