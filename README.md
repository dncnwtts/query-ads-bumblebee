# query-ads-bumblebee
Short python script that creates URL querying Bumblebee database

The output of this script is a set of four links to ADS. Run this script every
time the grad student list is updated...

[Publication list 1]
(https://ui.adsabs.harvard.edu/#search/q=((pos(aff:"Hopkins",1) AND (author:"^Aguilar, J" OR author:"^Alexandroff, R" OR author:"^Ali, A" OR author:"^Amram, O" OR author:"^Anand, N" OR author:"^Arpino, K" OR author:"^Atakhodjaev, I" OR author:"^Balaji, B" OR author:"^Bankert, J" OR author:"^Berghaus, K" OR author:"^Bobrow, E" OR author:"^Bose, P" OR author:"^Brehm, D" OR author:"^Breysse, P" OR author:"^Busch, M" OR author:"^Carey, N" OR author:"^Caviglia, C" OR author:"^Chaudhuri, D" OR author:"^Chauhan, P" OR author:"^Chen, H" OR author:"^Chen, K" OR author:"^Chen, Y" OR author:"^Chen, Y" OR author:"^Chen, Y" OR author:"^Cheng, B" OR author:"^Cleary, J" OR author:"^Clemmer, J" OR author:"^Corcodilos, L" OR author:"^Cordisco, A" OR author:"^Crichton, D" OR author:"^Crosley, M" OR author:"^Dahal, S" OR author:"^Dasgupta, S" OR author:"^Dasgupta, S" OR author:"^de la Vega, A" OR author:"^Diamond, M" OR author:"^Dugan, Z" OR author:"^Durgad, R" OR author:"^Ely, D" OR author:"^Eminizer, N" OR author:"^Engelke, P" OR author:"^Faroughy, C" OR author:"^Fehling, D" OR author:"^Feng, L" OR author:"^Fogarty, K")) AND year:2007-2099)&sort=date desc)

[Publication list 2]
(https://ui.adsabs.harvard.edu/#search/q=((pos(aff:"Hopkins",1) AND (author:"^Fuhrman, W" OR author:"^Galvani Cunha, M" OR author:"^Ghasemi, A" OR author:"^Ghosh, A" OR author:"^Hall, K" OR author:"^Halloran, T" OR author:"^Harrington, K" OR author:"^Hart, M" OR author:"^Hassan, N" OR author:"^Huang, C" OR author:"^Huang, Y" OR author:"^Hung, W" OR author:"^Hussong, C" OR author:"^Hwang, H" OR author:"^Iuliano, J" OR author:"^Jafari Alanjagh, A" OR author:"^Jones, D" OR author:"^Kable, J" OR author:"^Karwal, T" OR author:"^Kinch, B" OR author:"^Knizhnik, K" OR author:"^Lambrides, E" OR author:"^Laurita, N" OR author:"^Lee, M" OR author:"^Lowry, I" OR author:"^Luo, Y" OR author:"^Maingi, L" OR author:"^Mantilla Suarez, C" OR author:"^Marcus, G" OR author:"^Meibody, R" OR author:"^Mokris, J" OR author:"^Monti, J" OR author:"^Morris, M" OR author:"^Munoz, J" OR author:"^Nayak, O" OR author:"^Nishikawa, H" OR author:"^O'Connor, T" OR author:"^Osumi, K" OR author:"^Paul, B" OR author:"^Peth, M" OR author:"^Petroff, M" OR author:"^Pfeffer, D" OR author:"^Plunkett, E" OR author:"^Qu, D" OR author:"^Redwine, K")) AND year:2007-2099)&sort=date desc)

[Publication list 3]
(https://ui.adsabs.harvard.edu/#search/q=((pos(aff:"Hopkins",1) AND (author:"^Ren, B" OR author:"^Rivas, D" OR author:"^Roskes, H" OR author:"^Sady-Cocoros, A" OR author:"^Safarzadeh, M" OR author:"^Sarica, U" OR author:"^Scheie, A" OR author:"^Shi, Y" OR author:"^Simons, R" OR author:"^Su, T" OR author:"^Sun, C" OR author:"^Tchernyshyov, K" OR author:"^Trump, B" OR author:"^Tutmaher, J" OR author:"^Valentine, M" OR author:"^Wang, B" OR author:"^Wang, H" OR author:"^Wang, W" OR author:"^Wang, Y" OR author:"^Watts, D" OR author:"^Weck, P" OR author:"^Wolff, S" OR author:"^Wu, S" OR author:"^Xu, B" OR author:"^Xu, Z" OR author:"^Yang, L" OR author:"^You, C" OR author:"^Yue, D" OR author:"^Zhang, S" OR author:"^Zhang, X" OR author:"^Zhou, Y")) AND year:2007-2099)&sort=date desc)


For the future, a better way to do this would be using the ADS API directly.

http://adsabs.github.io/help/api/

https://github.com/adsabs/adsabs-dev-api

This is split up into four lists because a query with 120 names directly is too many. The API should be able to handle it though.
