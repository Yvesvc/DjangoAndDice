import os

base = open("spells_migration.txt", "rt", encoding = 'utf-8')
out_2 = open("spells_migration2.txt", "wt",  encoding = 'utf-8')

for line in base:
	out_2.write(line.replace('{', ' {"model": "spells.spells5e","pk": 1, "fields": {'))
	
base.close()
out_2.close()

##########
out_2 = open("spells_migration2.txt", "rt",  encoding = 'utf-8')
out_3 = open("spells_migration3.txt", "wt",  encoding = 'utf-8')

for line in out_2:
	out_3.write(line.replace('}', '}}'))
	
out_2.close()
out_3.close()

#########
out_3 = open("spells_migration3.txt", "rt",  encoding = 'utf-8')
out_4 = open("spells_migration4.txt", "wt",  encoding = 'utf-8')

num = 1
for line in out_3:
	if '"pk": 1' in line:
		out_4.write(line.replace('"pk": 1','"pk": '+ str(num)))
		num += 1
	else:
		out_4.write(line)

	
out_3.close()
out_4.close()

####
out_4 = open("spells_migration4.txt", "rt",  encoding = 'utf-8')
out_5 = open("spells_migration5.txt", "wt",  encoding = 'utf-8')

num = 1
for line in out_4:
	out_5.write(line.replace('"class"', '"char_class"'))
	
out_4.close()
out_5.close()

#####
pre, ext = os.path.splitext("spells_migration5.txt")
os.rename("spells_migration5.txt", pre + '.json')
