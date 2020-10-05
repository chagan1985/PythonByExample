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

def clearNewArtistFields():
    nameEntry.delete(0, 'end')
    addressEntry.delete(0, 'end')
    townEntry.delete(0, 'end')
    countyEntry.delete(0, 'end')
    postcodeEntry.delete(0, 'end')


def clearNewArtworkFields():
    titleEntry.delete(0, 'end')
    mediumEntry.delete(0, 'end')
    priceEntry.delete(0, 'end')
    artistCombobox.set('')


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
    for i in artworkFrame.get_children():
        artworkFrame.delete(i)
    contentsOfPiecesOfArt = cursor.execute("""SELECT PieceID, Title, Medium, Price FROM PiecesOfArt""")
    for pieceOfArt in contentsOfPiecesOfArt:
        print(pieceOfArt[0])
        artworkFrame.insert('', 'end', text=pieceOfArt[0], values=(pieceOfArt[1], pieceOfArt[2], pieceOfArt[3]))


def newArtworkSelected(selection):
    print(selection)
    artworkFrame.selection_remove(selection)
    if (selection):
        selectedArtist = cursor.execute("""SELECT ArtistID FROM PiecesOfArt WHERE PieceID={}""".format(artworkFrame.item(artworkFrame.selection())['text']))
        selectedArtistKey = selectedArtist.fetchone()[0]
    else:
        selectedArtistKey = 0
    
    displayArtist(artistKey=selectedArtistKey)


def addArtist():
    if (nameEntry.get() and addressEntry.get() and countyEntry.get() and postcodeEntry.get()):
        cursor.execute("""INSERT INTO Artists(Name, Address, Town, County, Postcode)
                    VALUES('{}', '{}', '{}', '{}', '{}')""".format(nameEntry.get(), addressEntry.get(), townEntry.get(), countyEntry.get(), postcodeEntry.get()))
        db.commit()
        artistCombobox.config(values=cursor.execute("""SELECT ArtistID FROM Artists;""").fetchall())
        clearNewArtistFields()
    else:
        tkinter.messagebox.showerror('Data Error', 'Incomplete Artist entry!')

def addPieceOfArt():
    if (titleEntry.get() and mediumEntry.get() and priceEntry.get() and artistCombobox.get()):
        cursor.execute("""INSERT INTO PiecesOfArt(ArtistID, Title, Medium, Price)
                    VALUES('{}', '{}', '{}', '{}')""".format(int(artistCombobox.get()), titleEntry.get(), mediumEntry.get(), int(priceEntry.get())))
        db.commit()
        displayArtwork()
        clearNewArtworkFields()
    else:
        tkinter.messagebox.showerror('Data Error', 'Incomplete Artwork entry!')
        

def pieceOfArtSold():
    focusedItem = artworkFrame.item(artworkFrame.focus())
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

artworkFrame = ttk.Treeview(show='headings', column=('Title', 'Medium', 'Price'), selectmode='browse')
artworkFrame.column('Title', width=300, anchor='w')
artworkFrame.heading('Title', text='Title')
artworkFrame.column('Medium', width=150, anchor='center')
artworkFrame.heading('Medium', text='Medium')
artworkFrame.column('Price', width=150, anchor='e')
artworkFrame.heading('Price', text='Price (£)')
artworkFrame.bind('<<TreeviewSelect>>', newArtworkSelected)
artworkFrame.place(x=75, y=400, width=600, height=400)
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
