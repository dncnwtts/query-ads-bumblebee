# query-ads-bumblebee
Short python script that creates URL querying Bumblebee database

The output of this script is a set of four links to ADS. Run this script every
time the grad student list is updated...

[Publication list 1]
(https://ui.adsabs.harvard.edu/#search/q=((pos(aff:"Hopkins",1)%20AND%20(author:"^Aguilar,%20J"%20OR%20author:"^Alexandroff,%20R"%20OR%20author:"^Ali,%20A"%20OR%20author:"^Amram,%20O"%20OR%20author:"^Anand,%20N"%20OR%20author:"^Arpino,%20K"%20OR%20author:"^Atakhodjaev,%20I"%20OR%20author:"^Balaji,%20B"%20OR%20author:"^Bankert,%20J"%20OR%20author:"^Berghaus,%20K"%20OR%20author:"^Bobrow,%20E"%20OR%20author:"^Bose,%20P"%20OR%20author:"^Brehm,%20D"%20OR%20author:"^Breysse,%20P"%20OR%20author:"^Busch,%20M"%20OR%20author:"^Carey,%20N"%20OR%20author:"^Caviglia,%20C"%20OR%20author:"^Chaudhuri,%20D"%20OR%20author:"^Chauhan,%20P"%20OR%20author:"^Chen,%20H"%20OR%20author:"^Chen,%20K"%20OR%20author:"^Chen,%20Y"%20OR%20author:"^Chen,%20Y"%20OR%20author:"^Chen,%20Y"%20OR%20author:"^Cheng,%20B"%20OR%20author:"^Cleary,%20J"%20OR%20author:"^Clemmer,%20J"%20OR%20author:"^Corcodilos,%20L"%20OR%20author:"^Cordisco,%20A"%20OR%20author:"^Crichton,%20D"%20OR%20author:"^Crosley,%20M"%20OR%20author:"^Dahal,%20S"%20OR%20author:"^Dasgupta,%20S"%20OR%20author:"^Dasgupta,%20S"%20OR%20author:"^de%20la%20Vega,%20A"%20OR%20author:"^Diamond,%20M"%20OR%20author:"^Dugan,%20Z"%20OR%20author:"^Durgad,%20R"%20OR%20author:"^Ely,%20D"%20OR%20author:"^Eminizer,%20N"%20OR%20author:"^Engelke,%20P"%20OR%20author:"^Faroughy,%20C"%20OR%20author:"^Fehling,%20D"%20OR%20author:"^Feng,%20L"%20OR%20author:"^Fogarty,%20K"))%20AND%20year:2007-2099)&sort=date%20desc)


[Publication list 2]
(https://ui.adsabs.harvard.edu/#search/q=((pos(aff:"Hopkins",1)%20AND%20(author:"^Fuhrman,%20W"%20OR%20author:"^Galvani%20Cunha,%20M"%20OR%20author:"^Ghasemi,%20A"%20OR%20author:"^Ghosh,%20A"%20OR%20author:"^Hall,%20K"%20OR%20author:"^Halloran,%20T"%20OR%20author:"^Harrington,%20K"%20OR%20author:"^Hart,%20M"%20OR%20author:"^Hassan,%20N"%20OR%20author:"^Huang,%20C"%20OR%20author:"^Huang,%20Y"%20OR%20author:"^Hung,%20W"%20OR%20author:"^Hussong,%20C"%20OR%20author:"^Hwang,%20H"%20OR%20author:"^Iuliano,%20J"%20OR%20author:"^Jafari%20Alanjagh,%20A"%20OR%20author:"^Jones,%20D"%20OR%20author:"^Kable,%20J"%20OR%20author:"^Karwal,%20T"%20OR%20author:"^Kinch,%20B"%20OR%20author:"^Knizhnik,%20K"%20OR%20author:"^Lambrides,%20E"%20OR%20author:"^Laurita,%20N"%20OR%20author:"^Lee,%20M"%20OR%20author:"^Lowry,%20I"%20OR%20author:"^Luo,%20Y"%20OR%20author:"^Maingi,%20L"%20OR%20author:"^Mantilla%20Suarez,%20C"%20OR%20author:"^Marcus,%20G"%20OR%20author:"^Meibody,%20R"%20OR%20author:"^Mokris,%20J"%20OR%20author:"^Monti,%20J"%20OR%20author:"^Morris,%20M"%20OR%20author:"^Munoz,%20J"%20OR%20author:"^Nayak,%20O"%20OR%20author:"^Nishikawa,%20H"%20OR%20author:"^O'Connor,%20T"%20OR%20author:"^Osumi,%20K"%20OR%20author:"^Paul,%20B"%20OR%20author:"^Peth,%20M"%20OR%20author:"^Petroff,%20M"%20OR%20author:"^Pfeffer,%20D"%20OR%20author:"^Plunkett,%20E"%20OR%20author:"^Qu,%20D"%20OR%20author:"^Redwine,%20K"))%20AND%20year:2007-2099)&sort=date%20desc)

[Publication list 3]
(https://ui.adsabs.harvard.edu/#search/q=((pos(aff:"Hopkins",1)%20AND%20(author:"^Ren,%20B"%20OR%20author:"^Rivas,%20D"%20OR%20author:"^Roskes,%20H"%20OR%20author:"^Sady-Cocoros,%20A"%20OR%20author:"^Safarzadeh,%20M"%20OR%20author:"^Sarica,%20U"%20OR%20author:"^Scheie,%20A"%20OR%20author:"^Shi,%20Y"%20OR%20author:"^Simons,%20R"%20OR%20author:"^Su,%20T"%20OR%20author:"^Sun,%20C"%20OR%20author:"^Tchernyshyov,%20K"%20OR%20author:"^Trump,%20B"%20OR%20author:"^Tutmaher,%20J"%20OR%20author:"^Valentine,%20M"%20OR%20author:"^Wang,%20B"%20OR%20author:"^Wang,%20H"%20OR%20author:"^Wang,%20W"%20OR%20author:"^Wang,%20Y"%20OR%20author:"^Watts,%20D"%20OR%20author:"^Weck,%20P"%20OR%20author:"^Wolff,%20S"%20OR%20author:"^Wu,%20S"%20OR%20author:"^Xu,%20B"%20OR%20author:"^Xu,%20Z"%20OR%20author:"^Yang,%20L"%20OR%20author:"^You,%20C"%20OR%20author:"^Yue,%20D"%20OR%20author:"^Zhang,%20S"%20OR%20author:"^Zhang,%20X"%20OR%20author:"^Zhou,%20Y"))%20AND%20year:2007-2099)&sort=date%20desc)

For the future, a better way to do this would be using the ADS API directly.

http://adsabs.github.io/help/api/

https://github.com/adsabs/adsabs-dev-api

This is split up into four lists because a query with 120 names directly is too many. The API should be able to handle it though.
