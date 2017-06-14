import sqlite3
from User import User
from Table import Table
from Character import Character

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
cursor.execute('DROP TABLE IF EXISTS char_inv')
cursor.execute('DROP TABLE IF EXISTS inventory')
cursor.execute('DROP TABLE IF EXISTS char_clas')

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
        level INTEGER,
        inventory INTEGER NOT NULL,
        experience INTEGER,
        class INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (creator) REFERENCES users(id),
        FOREIGN KEY (inventory) REFERENCES char_inv(id)
        FOREIGN KEY (class) REFERENCES char_clas(clas_id)
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
 	CREATE TABLE inventory (
		item VARCHAR(20),
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

cursor.execute("""
 	CREATE TABLE char_inv (
		char_id INTEGER NOT NULL,
		inv_id INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (char_id) REFERENCES characteres(id),
		FOREIGN KEY (inv_id) REFERENCES inventory(id)
	); """)

cursor.execute("""
 	CREATE TABLE char_clas (
		char_id INTEGER NOT NULL,
		clas_id INTEGER NOT NULL,
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		FOREIGN KEY (char_id) REFERENCES characteres(id),
		FOREIGN KEY (clas_id) REFERENCES inventory(id)
	); """)

def saveClass(classToAdd):
    numId = 0
    name = classToAdd.getName()
    cursor.execute("""SELECT id FROM users WHERE name = ?;""", (name,))
    for row in cursor.fetchall():
        numId = row[0]
    cursor.execute("""INSERT OR REPLACE INTO classes (name, creator, edition, id) VALUES (?,?,?,?);""", (name, int(numId), 0, None))

def getClass(name):
	result = cursor.execute("""SELECT * FROM classes WHERE name = ?;""", (name,))
	return result

def delClass(ID):
	cursor.execute("""DELETE FROM classes WHERE id = ?;""", (ID))

def saveUser(userToAdd):
	cursor.execute("""INSERT OR REPLACE INTO users (name, password, id) VALUES (?,?,?); """, (userToAdd.getName(), userToAdd.getPassword(), None))

def getUser(name):
    password = ''
    cursor.execute("""SELECT * FROM users WHERE name = ?;""", (name,))
    for row in cursor.fetchall():
        password = row[1]
    player = User(name, password)
    return player

def delUser(ID):
	cursor.execute("""DELETE FROM users WHERE id = ?;""", (ID))

def addOpenTable(table):
    numId = 0
    name = table.getName()
    cursor.execute("""SELECT id FROM tables WHERE name = ?;""", (name,))
    for row in cursor.fetchall():
        numId = row[0]
    cursor.execute("""
        INSERT OR IGNORE INTO openTables (table_id, id) VALUES (?,?)
    ;""", (int(numId), None))


def delOpenTable(ID):
	cursor.execute("""DELETE FROM openTables WHERE id = ?;""", (ID,))

def getTable(name):
    name = ""
    master = 0
    edition = 0
    tableid = 0
    cursor.execute("""SELECT * FROM tables WHERE name = ?;""", (name,))
    for row in cursor.fetchall():
        name = row[0]
        master = row[1]
    table = Table(name, master)
    return table

def getTableID(name, master):
    cursos.execute("""SELECT id FROM tables WHERE name = ? AND master = ?;""", (name, master))
    return cursor.fetchall()

def saveTable(table):
    master = table.getMaster()
    name = table.getName()
    numId = 0
    cursor.execute("""SELECT id FROM users WHERE name = ?;""", (name,))
    for row in cursor.fetchall():
        numId = row[0]
    cursor.execute("""INSERT OR REPLACE INTO tables (name, master, edition, id) VALUES (?,?,?,?);""", (name, int(numId), 0, None))

def delTable(ID):
	cursor.execute("""DELETE FROM tables WHERE id = ?;""", (ID))

def getCharacter(name):
    cursor.execute("""SELECT * FROM characters WHERE name = ?;""", (name,))
    for row in cursor.fetchall():
        name = row[0]
        creator = row [1]
        clas = row[7]
    cursor.execute("""SELECT name FROM users WHERE id = ?""", (creator,))
    for row in cursor.fetchall():
        creatorName = row[0]
    user = getUser(creatorName)
    char = Character(name, clas, user)
    return char

def saveCharacter(character):
    numId = 0
    inv_id = 0
    clas_id = 0
    name = character.getName()
    level = character.getLevel()
    xp = character.getExperience()
    description = character.getDescription()
    player = character.getCreator()
    playerName = player.getName()
    cursor.execute("""SELECT id FROM users WHERE name = ?;""", (playerName,))
    for row in cursor.fetchall():
        numId = row[0]
    cursor.execute("""SELECT inventory FROM characters WHERE creator = ? AND name = ?;""", (numId, name))
    for row in cursor.fetchall():
        inv_id = row[0]
    cursor.execute("""SELECT class FROM characters WHERE creator = ? AND name = ?;""", (numId, name))
    for row in cursor.fetchall():
        clas_id = row[0]
    cursor.execute("""
		INSERT OR REPLACE INTO characters (name, creator, edition, description, level, inventory, experience, class, id) VALUES (?,?,?,?,?,?,?,?,?)
	; """, (name, int(numId), 0, description, level, int(inv_id), xp, id(clas_id), None))

def delCharacter(ID):
	cursor.execute("""DELETE FROM characters WHERE id = ?;""", (ID))

def addCharToTable(charName, tableName):
    charId = 0
    cursor.execute("""SELECT id FROM characters WHERE name = ?;""", (charName))
    for row in cursor.fetchall():
        charId = row[0]
    tableId = 0
    cursor.execute("""SELECT id FROM tables WHERE name = ?;""", (tableName,))
    for row in cursor.fetchall():
        tableId = row[0]
    cursor.execute("""
    	INSERT OR IGNORE INTO char_table (char_id, table_id, id) VALUES (?,?,?)
    ; """, (int(charId), int(tableId), None,))

def delCharFromTable(charName, tableName):
    charId = 0
    cursor.execute("""SELECT id FROM characters WHERE name = ?;""", (charName))
    for row in cursor.fetchall():
        charId = row[0]
    tableId = 0
    cursor.execute("""SELECT id FROM tables WHERE name = ?;""", (tableName,))
    for row in cursor.fetchall():
        tableId = row[0]
    cursor.execute("""DELETE FROM char_table WHERE table_id = ? AND char_id = ?;""", (int(tableId), int(charId)))

def addPlayerToTable(playerName, tableName):
    playerId = 0
    cursor.execute("""SELECT id FROM users WHERE name = ?;""", (playerName))
    for row in cursor.fetchall():
        playerId = row[0]
    tableId = 0
    cursor.execute("""SELECT id FROM tables WHERE name = ?;""", (tableName,))
    for row in cursor.fetchall():
        tableId = row[0]
    cursor.execute("""
    	INSERT OR IGNORE INTO table_user (player_id, table_id, id) VALUES (?,?,?)
    ;""", (int(playerId), int(tableId), None))

def delPlayerFromTable(playerName, tableName):
    playerId = 0
    cursor.execute("""SELECT id FROM users WHERE name = ?;""", (playerName))
    for row in cursor.fetchall():
        playerId = row[0]
    tableId = 0
    cursor.execute("""SELECT id FROM tables WHERE name = ?;""", (tableName,))
    for row in cursor.fetchall():
        tableId = row[0]
    cursor.execute("""DELETE FROM table_user WHERE table_id = ? AND player_id = ?;""", (int(playerId), int(tableId)))
