import sqlite3
import os

text_files_directory = 'files'
sqlite_file = 'database.sqlite'

conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS lines (content TEXT)')

def insert_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line_content = line.strip()
            cursor.execute('INSERT INTO lines (content) VALUES (?)', (line_content,))
            print(f"[ \033[1;33m+ \033[0m] {line_content}")

for file_name in os.listdir(text_files_directory):
    if file_name.endswith('.txt'):
        insert_lines_from_file(os.path.join(text_files_directory, file_name))

conn.commit()
conn.close()

print(f"[ \033[0;32m+ \033[0m] All lines of files in {text_files_directory} successfuly added to {sqlite_file}.")
