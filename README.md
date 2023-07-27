# NBS-Hierarchical
This work is my implementation of a Nash bargaining solution framework, applied to 
network interaction between a hierarchical multi-tier content delivery network.
It uses an exhaustive search routine to solve different scenarios of server interactions.
The Hierarchy model is defined as interaction between a Content Provider, A trasmit network and
an Access network at the lowest tier which provides the content to end user. This image represents the model:

![alt text](https://github.com/Danii-Sh/NBS-Hierarchical/blob/a8756bee75d4edf1e4f08801b4c176cc93a523b5/1.jpg)

A benchmark of selfish operation is done using extensive form game.
The next codes entail different cooperation and bargaining situations, each resembling 
real server user interactions.

### Some Sample results: 

Proof of Nash equilibrium for bargaining solution, set analysis:

![alt text](https://github.com/Danii-Sh/NBS-Hierarchical/blob/060ee4d41c2746476987b346c5885c8a311c5c4e/set%20three%20server.png)

A sample output for Price strategy setting in two server cooperation scenario:

![alt text](https://github.com/Danii-Sh/NBS-Hierarchical/blob/060ee4d41c2746476987b346c5885c8a311c5c4e/Result-cooporat%20strategy-price.png)

A comparison between different scenario utilities, which illuminates the incentive to cooperate, 
The utility is translated to server finanical gain in our literature:
![alt text](https://github.com/Danii-Sh/NBS-Hierarchical/blob/060ee4d41c2746476987b346c5885c8a311c5c4e/usum_new.png)
