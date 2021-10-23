
# importing things

import matplotlib.pyplot as plt
import json


#DRAKE SONGS JSON FILE WORK


#how many songs does drake have?

files = ['drake_data.json']
text = ''
songs = []

with open('drake_data.json', encoding='ascii') as f:
    text = f.read()
    songs += json.loads(text)

print('len(songs) =', len(songs))


# how many times does drake say these things in his songs?

num_baby = 0
num_shawty = 0
num_girl = 0
num_drake = 0
num_man = 0
num_yeah = 0
num_money = 0
num_what = 0
for s in songs:
    if s['lyrics']:  #checking to see if the lyrics exist period
        if 'baby' in s["lyrics"].lower():
            num_baby += 1
        if 'shawty' in s["lyrics"].lower() or 'shorty' in s["lyrics"].lower():
            num_shawty += 1
        if 'girl' in s["lyrics"].lower():
            num_girl += 1
        if 'drake' in s["lyrics"].lower():
            num_drake += 1
        if 'man' in s["lyrics"].lower():
            num_man += 1
        if 'yeah' in s["lyrics"].lower() or 'ya' in s["lyrics"].lower() or 'yea' in s["lyrics"].lower():
            num_yeah += 1
        if 'money' in s["lyrics"].lower():
            num_money += 1
        if 'what' in s["lyrics"].lower():
            num_what += 1
print('num_baby=', num_baby)
print('num_shawty=', num_shawty)
print('num_girl=', num_girl)
print('num_drake=', num_drake)
print('num_man=', num_man)
print('num_yeah=', num_yeah)
print('num_what=', num_what)


# making a dictionary with these numbers

counts = {
    'baby': num_baby,
    'shawty': num_shawty,
    'girl': num_girl,
    'drake': num_drake,
    'man': num_man,
    'yeah': num_yeah,
    'money': num_money,
    'what': num_what
}
print('counts =', counts)


#getting the data for the plot

xs = sorted(counts.keys())
ys = [ counts[key] for key in xs ]


#axes work

print('xs=',xs)
print('ys=',ys)


#plotting??

fig, ax = plt.subplots()
ax.bar(xs, ys)
ax.set_xlabel('Words')
ax.set_ylabel('Frequency')
ax.set_title('How often does Drake use these words in his songs?')
plt.show()




#TSWIFT LYRIC WORK

# how many taylor songs in this data set?

files = ['swift_lyrics.json']
text = ''
songs = []

with open('swift_lyrics.json', encoding='ascii') as f:
    text = f.read()
    songs += json.loads(text)

print('len(songs) =', len(songs))

# how many songs each year?

num_2006 = 0
num_2007 = 0
num_2008 = 0
num_2009 = 0
num_2010 = 0
num_2011 = 0
num_2012 = 0
num_2013 = 0
num_2014 = 0

for s in songs:
    if s["year"]:  #checking to see if the lyrics exist period
        if "2006" in s["year"]:
            num_2006 += 1
        if "2007" in s["year"]:
            num_2007 += 1
        if "2008" in s["year"]:
            num_2008 += 1
        if "2009" in s["year"]:
            num_2009 += 1
        if "2010" in s["year"]:
            num_2010 += 1
        if "2011" in s["year"]:
            num_2011 += 1
        if "2012" in s["year"]:
            num_2012 += 1
        if "2013" in s["year"]:
            num_2013 += 1
        if "2014" in s["year"]:
            num_2014 += 1

print("num_2006=",num_2006)
print("num_2007=",num_2007)
print("num_2008=",num_2008)
print("num_2009", num_2009)
print("num_2010=",num_2010)
print("num_2011=",num_2011)
print("num_2012=",num_2012)
print("num_2013=",num_2013)
print("num_2014=",num_2014)

# making a dictionary with these numbers

counts = {
    '2006': num_2006,
    '2007': num_2007,
    '2008': num_2008,
    '2009': num_2009,
    '2010': num_2010,
    '2011': num_2011,
    '2012': num_2012,
    '2013': num_2013,
    '2014': num_2014
}
print('counts =', counts)

# songs per year with love in them

num_love2006 = 0
num_love2007 = 0
num_love2008 = 0
num_love2009 = 0
num_love2010 = 0
num_love2011 = 0
num_love2012 = 0
num_love2013 = 0
num_love2014 = 0
for s in songs:
    if s["year"]:  #checking to see if the years exist period
        if "2006" in s["year"] and "love" in s["lyrics"]:
            num_love2006 += 1
        if "2007" in s["year"] and "love" in s["lyrics"]:
            num_love2007 += 1
        if "2008" in s["year"] and "love" in s["lyrics"]:
            num_love2008 += 1
        if "2009" in s["year"] and "love" in s["lyrics"]:
            num_love2009 += 1
        if "2010" in s["year"] and "love" in s["lyrics"]:
            num_love2010 += 1
        if "2011" in s["year"] and "love" in s["lyrics"]:
            num_love2011 += 1
        if "2012" in s["year"] and "love" in s["lyrics"]:
            num_love2012 += 1
        if "2013" in s["year"] and "love" in s["lyrics"]:
            num_love2013 += 1
        if "2014" in s["year"] and "love" in s["lyrics"]:
            num_love2014 += 1

print('num_love2006', num_love2006)
print('num_love2007', num_love2007)
print('num_love2008', num_love2008)
print('num_love2009', num_love2009)
print('num_love2010', num_love2010)
print('num_love2011', num_love2011)
print('num_love2012', num_love2012)
print('num_love2013', num_love2013)
print('num_love2014', num_love2014)

# making a dictionary with these numbers

lovecounts = {
    '2006': num_love2006,
    '2007': num_love2007,
    '2008': num_love2008,
    '2009': num_love2009,
    '2010': num_love2010,
    '2011': num_love2011,
    '2012': num_love2012,
    '2013': num_love2013,
    '2014': num_love2014
}
print('lovecounts =', lovecounts)

# getting data for plot

xs = sorted(counts.keys())
ys1 = [ counts[key] for key in xs ]
ys2 = [ lovecounts[key] for key in xs ]

# making sure my axes have the right data

print('xs=',xs)
print('ys1=',ys1)
print('ys2=', ys2)


#plotting??

fig, ax = plt.subplots()
ax.plot(xs, ys1, ys2)
plt.legend(["all songs", "songs with 'love'"], loc ="upper left")
ax.set_xlabel('Year')
ax.set_ylabel('Songs')
ax.set_title('Songs per year: All songs vs. songs with the word "love"')
plt.show()
