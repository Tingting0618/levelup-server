# levelup-server

## ERD 
https://dbdiagram.io/d/61b73ff78c901501c0edceee

- There will be 4 main tables, Gamer, Game, GameType. and Event.
- Each of those tables have some fields that would be useful to keep track of in the database.
- The Game table will have a one to many relationship with GameType since a game will be associated with 1 game type and a game type can be associated with many games.
- The Game will also have a one to many relationship with Gamer because gamers can create more than one game.
- The Event table will have a 1 to many relationship with Gamer, called the organizer, because gamers can host many events but an event will only have 1 host.
- To keep track of who is attending events, there is a many to many relationship between gamers and events. There will need to be a join table to connect that many to many relationship. 
