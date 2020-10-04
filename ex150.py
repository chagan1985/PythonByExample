#####
# Python By Example
# Exercise 150
# Christopher Hagan
#####

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import os, sqlite3, tkinter.messagebox, csv

soldArtworkFile='soldArtwork.csv'
soldArtworkColumnHeaders = ['PieceID', 'Artist', 'Title', 'Medium', 'Price']

def displayArtist(artistKey):
    artistListBox.delete(0, 'end')
    if (artistKey == 0):
        artistListBox.insert('end', 'No Artist Selected')
    else:
        contentsOfArtistTable = cursor.execute("""SELECT Name, Address, County, Town, Postcode FROM artists WHERE ArtistID={};""".format(artistKey))
        name, address, county, town, postcode = contentsOfArtistTable.fetchone()
        artistListBox.insert('end', 'Artist Name : {}'.format(name))
        artistListBox.insert('end', '')
        artistListBox.insert('end', 'Artist Address : {}'.format(address))
        artistListBox.insert('end', 'County : {}'.format(county))
        if (town):
            artistListBox.insert('end', 'Town : {}'.format(town))
        artistListBox.insert('end', 'Postcode : {}'.format(postcode))


def displayArtwork():
    contentsOfPiecesOfArt = cursor.execute("""SELECT PieceID, Title, Medium, Price FROM PiecesOfArt""")
    for pieceOfArt in contentsOfPiecesOfArt:
        print(pieceOfArt[0])
        newArtworkFrame.insert('', 'end', text=pieceOfArt[0], values=(pieceOfArt[1], pieceOfArt[2], pieceOfArt[3]))


def newArtworkSelected(selection):
    print(selection)
    newArtworkFrame.selection_remove(selection)
    if (selection):
        selectedArtist = cursor.execute("""SELECT ArtistID FROM PiecesOfArt WHERE PieceID={}""".format(newArtworkFrame.item(newArtworkFrame.selection())['text']))
        selectedArtistKey = selectedArtist.fetchone()[0]
    else:
        selectedArtistKey = 0
    
    displayArtist(artistKey=selectedArtistKey)


def addArtist():
    if (nameEntry.get() and addressEntry.get() and countyEntry.get() and postcodeEntry.get()):
        cursor.execute("""INSERT INTO Artists(Name, Address, Town, County, Postcode)
                    VALUES('{}', '{}', '{}', '{}', '{}')""".format(nameEntry.get(), addressEntry.get(), townEntry.get(), countyEntry.get(), postcodeEntry.get()))
        db.commit()
        nameEntry.delete(0, 'end')
        addressEntry.delete(0, 'end')
        townEntry.delete(0, 'end')
        countyEntry.delete(0, 'end')
        postcodeEntry.delete(0, 'end')
    else:
        tkinter.messagebox.showerror('Data Error', 'Incomplete entry!')

def addPieceOfArt():
    print('Add piece of art....')


def pieceOfArtSold():
    focusedItem = newArtworkFrame.item(newArtworkFrame.focus())
    artworkToBeRemoved = cursor.execute("""SELECT PieceID, ArtistID, Title, Medium, Price FROM PiecesOfArt WHERE PieceID={}""".format(focusedItem['text']))
    pieceID, artistID, title, medium, price = artworkToBeRemoved.fetchone()
    artist = cursor.execute("""SELECT Name FROM Artists WHERE ArtistID={}""".format(artistID)).fetchone()[0]

    soldFileExists = os.path.isfile(soldArtworkFile)
    with open(soldArtworkFile, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=soldArtworkColumnHeaders)
        if not soldFileExists:
            fileWriter.writeheader()
        fileWriter.writerow({'PieceID': pieceID, 'Artist': artist, 'Title': title, 'Medium': medium,'Price': price})

    cursor.execute("""DELETE FROM PiecesOfArt WHERE PieceID={}""".format(focusedItem['text']))
    db.commit()


def search():
    pass


with sqlite3.connect("ArtGallery.db") as db:
    cursor = db.cursor()

window = Tk()
window.geometry('1000x1000')
window.title('Art Gallery')

# Artist Frame and Contents
artistFrame = LabelFrame(text='Artist')
artistFrame.place(x=50, y=25, width=800, height=300)

artistListBox = Listbox()
artistListBox.place(x=150, y=75, width=300, height=150)
displayArtist(0)

newArtistFrame = LabelFrame(text='Add new Artist')
newArtistFrame.place(x=500, y=50, width=330, height=230)

nameLabel = Label(text='Name :')
nameLabel.place(x=510, y=75, width=75, height=25)
nameEntry = Entry(text='')
nameEntry.place(x=585, y=75, width=150, height=25)

addressLabel = Label(text='Address :')
addressLabel.place(x=510, y=100, width=75, height=25)
addressEntry = Entry(text='')
addressEntry.place(x=585, y=100, width=150, height=25)

townLabel = Label(text='Town :')
townLabel.place(x=510, y=125, width=75, height=25)
townEntry = Entry(text='')
townEntry.place(x=585, y=125, width=150, height=25)

countyLabel = Label(text='County :')
countyLabel.place(x=510, y=150, width=75, height=25)
countyEntry = Entry(text='')
countyEntry.place(x=585, y=150, width=150, height=25)

postcodeLabel = Label(text='Postcode :')
postcodeLabel.place(x=510, y=175, width=75, height=25)
postcodeEntry = Entry(text='')
postcodeEntry.place(x=585, y=175, width=150, height=25)

addArtistButton = Button(text='Add Artist', command=addArtist)
addArtistButton.place(x=740, y=215, width=75, height=50)

# Artwork frame and contents
artworkFrame = LabelFrame(text='Artwork')
artworkFrame.place(x=50, y=375, width=800, height=600)

newArtworkFrame = ttk.Treeview(show='headings', column=('Title', 'Medium', 'Price'), selectmode='browse')
newArtworkFrame.column('Title', width=300, anchor='w')
newArtworkFrame.heading('Title', text='Title')
newArtworkFrame.column('Medium', width=150, anchor='center')
newArtworkFrame.heading('Medium', text='Medium')
newArtworkFrame.column('Price', width=150, anchor='e')
newArtworkFrame.heading('Price', text='Price (£)')
newArtworkFrame.bind('<<TreeviewSelect>>', newArtworkSelected)
newArtworkFrame.place(x=75, y=400, width=600, height=400)
displayArtwork()

sellArtworkButton = Button(text='Mark Artwork\n   as sold', command=pieceOfArtSold)
sellArtworkButton.place(x=700, y=600, width=100, height=50)

newArtworkFrame = LabelFrame(text='Add new artwork')
newArtworkFrame.place(x=75, y=825, height=130, width=750)

titleLabel = Label(text='Title -')
titleLabel.place(x=100, y=850, width=75, height=25)
titleEntry = Entry(text='')
titleEntry.place(x=175, y=850, width=400, height=25)

mediumLabel = Label(text='Medium -')
mediumLabel.place(x=100, y=875, width=75, height=25)
mediumEntry = Entry(text='')
mediumEntry.place(x=175, y=875, width=100, height=25)

priceLabel = Label(text='Price (£) -')
priceLabel.place(x=100, y=900, width=75, height=25)
priceEntry = Entry(text='')
priceEntry.place(x=175, y=900, width=100, height=25)

artistLabel = Label(text='Artist -')
artistLabel.place(x=300, y=885, width=75, height=25)
artistCombobox = ttk.Combobox(values=cursor.execute("""SELECT ArtistID FROM Artists;""").fetchall())
artistCombobox.place(x=400, y=885, width=100, height=25)

addPieceOfArt = Button(text='Add Piece of\n    Art', command=addPieceOfArt)
addPieceOfArt.place(x=700, y=870, width=100, height=50)

window.mainloop()

db.close()
