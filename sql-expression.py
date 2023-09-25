from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    #Queries
    # select_query = artist_table.select()
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)
    # select_query = track_table.select().where(track_table.c.Composer == "Queen")


    results = connection.execute(select_query)
    for result in results:
        print(result) 