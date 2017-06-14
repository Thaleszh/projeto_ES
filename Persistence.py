import sqlite3

conn = sqlite3.connect('base.db')
cursor  = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS classes')
cursor.execute('DROP TABLE IF EXISTS characters')
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('DROP TABLE IF EXISTS tables')
cursor.execute('DROP TABLE IF EXISTS openTables')
cursor.execute('DROP TABLE IF EXISTS char_user')
cursor.execute('DROP TABLE IF EXISTS table_user')
cursor.execute('DROP TABLE IF EXISTS char_table')

cursor.execute("""
 	CREATE TABLE classes (
		name VARCHAR(20),
		creator INTEGER NOT NULL,
		edition INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (creator) REFERENCES users(id)
	); """)

cursor.execute("""
 	CREATE TABLE characters (
		name VARCHAR(20),
		creator INTEGER NOT NULL,
		edition INTEGER NOT NULL,
		description VARCHAR(300),
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (creator) REFERENCES users(id)
	); """)

cursor.execute("""
 	CREATE TABLE tables (
		name VARCHAR(20),
		master INTEGER NOT NULL,
		edition INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (master) REFERENCES users(id)
	); """)

cursor.execute("""
 	CREATE TABLE openTables (
		table_id INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (table_id) REFERENCES tables(id)
	); """)

cursor.execute("""
 	CREATE TABLE users (
		name VARCHAR(20),
		password VARCHAR(20),
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
	); """)

cursor.execute("""
 	CREATE TABLE table_user (
		player_id INTEGER NOT NULL,
		table_id INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (table_id) REFERENCES tables(id),
		FOREIGN KEY (player_id) REFERENCES users(id)
	); """)

cursor.execute("""
 	CREATE TABLE char_table (
		char_id INTEGER NOT NULL,
		table_id INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (table_id) REFERENCES tables(id),
		FOREIGN KEY (char_id) REFERENCES characters(id)
	); """)

cursor.execute("""
 	CREATE TABLE char_user (
		char_id INTEGER NOT NULL,
		user_id INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (char_id) REFERENCES characteres(id),
		FOREIGN KEY (user_id) REFERENCES users(id)
	); """)

def saveClass(classToAdd):
	numId = cursor.execute("""(SELECT id FROM users WHERE name = ?);""", (classToAdd.getName))
	cursor.execute("""(
		INSERT OR IGNORE INTO classes (name, creator, edition, id) VALUES (?,?,?,?,?)
	); """, (classToAdd.getName(), numId, 0, None))

def getClass(name):
	result = cursor.execute("""(SELECT * FROM classes WHERE name = ?);""", (name))
	return result

def delClass(ID):
	cursor.execute("""(DELETE * FROM classes WHERE id = ?);""", (ID))

def saveUser(userToAdd):
	cursor.execute("""(
		INSERT OR IGNORE INTO users (name, password, id) VALUES (?,?,?)
	); """, (userToAdd.getName(), userToAdd.getPassword(), None))

def getUser(name):
	result = cursor.execute("""(SELECT * FROM users WHERE name = ?);""", (name))
	return result

def delUser(ID):
	cursor.execute("""(DELETE * FROM users WHERE id = ?);""", (ID))

def addOpenTable(table):
	numId = cursor.execute("""(SELECT id FROM tables WHERE name = ?);""", (table.getName))
	cursor.execute("""(
		INSERT OR IGNORE INTO openTables (table_id, id) VALUES (?,?)
	); """, (numId, None))


def delOpenTable(ID):
	cursor.execute("""(DELETE * FROM openTables WHERE id = ?);""", (ID))

def getTable(name):
	result = cursor.execute("""(SELECT * FROM tables WHERE name = ?);""", (name))
	return result

def getTableID(name, master):
    cursos.execute("""(SELECT id FROM tables WHERE name = ? AND master = ?));""", (name, master))

def saveTable(table):
	name = table.getMaster()
	numId = cursor.execute("""(SELECT id FROM users WHERE name = ?);""", (name))
	cursor.execute("""(
		INSERT OR IGNORE INTO users (name, creator, edition, id) VALUES (?,?,?,?)
	); """, (table.getName(), numId, 0, None))

def delTable(ID):
	cursor.execute("""(DELETE * FROM tables WHERE id = ?);""", (ID))

def getCharacter(name):
	result = cursor.execute("""(SELECT * FROM characters WHERE name = ?);""", (name))
	return result

def saveCharacter(character):
		numId = cursor.execute("""(SELECT id FROM users WHERE name = ?);""", (character.getCreator()))
		cursor.execute("""(
			INSERT OR IGNORE INTO users (name, creator, edition, description, id) VALUES (?,?,?,?)
		); """, (character.getName(), numId, character.getDescription(), None))

def delCharacter(ID):
	cursor.execute("""(DELETE * FROM characters WHERE id = ?);""", (ID))

def addCharToTable(playerName, charName, tableName):
    charId = cursor.execute("""(SELECT id FROM characters WHERE name = ? AND creator = ?);""", (charName, playerName))
    tableId = cursor.execute("""(SELECT id FROM tables WHERE name = ?);""", (tableName))
    cursor.execute("""(
    	INSERT OR IGNORE INTO char_table (table_id, id) VALUES (?,?)
    ); """, (tableId, charId, None))

def delCharFromTable(charName, tableName):
    charId = cursor.execute("""(SELECT id FROM characters WHERE name = ? AND creator = ?);""", (tableName, playerName))
    tableId = cursor.execute("""(SELECT id FROM tables WHERE name = ?);""", (tableName))
    cursor.execute("""(DELETE * FROM char_table WHERE table_id = ? AND char_id = ?);""", (tableId, charId))


def addPlayertoTable(playerName, tableName):
    playerId = cursor.execute("""(SELECT id FROM players WHERE name = ?);""", (playerName))
    tableId = cursor.execute("""(SELECT id FROM tables WHERE name = ?);""", (tableNmae))
    cursor.execute("""(
    	INSERT OR IGNORE INTO user_table (table_id, id) VALUES (?,?)
    ); """, (playerId, tableId, None))

def delPlayerFromTable(playerName, tableName):
    playerId = cursor.execute("""(SELECT id FROM players WHERE name = ? AND creator = ?);""", (playerName))
    tableId = cursor.execute("""(SELECT id FROM tables WHERE name = ?);""", (tableName))
    cursor.execute("""(DELETE * FROM char_table WHERE table_id = ? AND player_id = ?);""", (tableId, playerId))
