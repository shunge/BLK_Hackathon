#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys

class sqliteTable:
	con = None


	def __init__(self, name = 'resume.db'):
		self.name = name



	def createTable(self):
		try:
		    con = lite.connect(self.name)
		    with con:
		    	cur = con.cursor()
		    	cur.execute("CREATE TABLE Users(ID INT, Name TEXT, Univ TEXT, MAJOR TEXT, GPA TEXT)")
		    	# cur.execute("SELECT * FROM Users")
		    	# rows = cur.fetchall()
		    	# for row in rows:
		    	# 	print row              
		except lite.Error, e:   
		    print "Error %s:" % e.args[0]
		    sys.exit(1)
		finally:    
		    if con:
		        con.close()



	def insertValue(self, records):
		try:
			con = lite.connect('resume.db')
			with con:
				cur = con.cursor()
				for record in records:
					param = "INSERT INTO Users VALUES(%s, %s, %s, %s, %s)" % \
							(record.getID(), '"'+record.getNAME()+'"', '"'+record.getUniv()+'"', '"'+record.getMAJOR()+'"', '"'+record.getGPA()+'"')
					print param
					cur.execute(param)
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
		finally:
			if con:
				con.close()


	def lookUp(self):
		try:
			con = lite.connect('resume.db')
			with con:
				cur = con.cursor()
				cur.execute("SELECT * FROM Users")
				rows = cur.fetchall()
				for row in rows:
					print row
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
		finally:
			if con:
				con.close()


	def queryID(self, IDList):
		result = []
		try:
			con = lite.connect('resume.db')
			with con:
				cur = con.cursor()
				IDTuple = tuple(IDList)
				instruction = "SELECT * FROM Users WHERE ID IN %s" % (IDTuple, )
				cur.execute(instruction)
				rows = cur.fetchall()
				for row in rows:
					result.append(row)
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
		finally:
			if con:
				con.close()
			return result

