# Write to a file called John Doe.txt 
# It should contain data about John Doe

f = open("C:\\Users\\YC COMPUTER\\Documents\\GitHub\\Python\\18_files\\John Doe3.txt", "w")

string = '''
John Doe is a nice guy. He lives in Nyc and he works with Python
His favorite package is Pandas
'''
f.write(string)

f.close()