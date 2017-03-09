#Implementation
##Server Side

https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe

The most unique part of this project was undoubtedly its multi-player aspect. From an architecture level, this was implemented most noticibly in the inclusion of two scripts, a server and a client. A copy of the client would run on each machine, but only one server instance should exist. The server script creates a server object from the server class, utilizing it to listen for new connections. Once the socket has been initialized and a client has connected the server creates a new model instance, and the model creates a new user which stores that player's color, as well as whether or not it is their turn. The server then echoes the state of the board back to all connected clients. Once both clients have connected they can begin to play. Upon further attempted connections the server rejects them, giving an appropriate error message. 

The model handles all of the logic of the game, with the clients sending click positions to the server, and the server forwarding them on to the model. Once there, the model checks whether the user that sent the click has the turn or not, and if the square that they clicked is (a) unoccupied and (b) within the box currently in focus. If all of these conditions are met, the clicked square is given the color of the user who clicked on it, and the state matrix** of the board is updated and broadcast to all clients. The clients then take the matrix, decompose it, and draw the correctly positioned (and colored) squares onto their board. Upon a click, the cycle begins again. 

In terms of design decisions, the most critical one was that of having all game-level logic happen on the server side, with the clients essentially being shells that blindly draw data and output click points. We eventually went with the option that we did in order to create as lightweight a program as possible. Before the game concept was fully finalized we were going to make an Asteroids clone, where low latency between computers would have been paramount, so this was prioritized. Although the game we eventually went with was less speed-dependent, the structure stayed. This does make the clients extremely lightweight, a good thing in general. 

**the state matrix is composed of data describing the position of each played box, as well as which box is the "focus"
