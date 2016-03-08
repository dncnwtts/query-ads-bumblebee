# query-ads-bumblebee
Short python script that creates URL querying Bumblebee database

The output of this script is a link to ADS Bumblebee:

[Publication list (broken)]
(https://ui.adsabs.harvard.edu/#search/fq={!type%3Daqp
v%3D%24fq_property}&fq_property=(property%3Arefereed)&q=((pos(aff%3A"Hopkins",1)
AND (author%3A"^Aguilar, J" OR author%3A"^Alexandroff, R" OR author%3A"^Ali, A"
OR author%3A"^Anand, N" OR author%3A"^Arpino, K" OR author%3A"^Atakhodjaev, I"
OR author%3A"^Bankert, J" OR author%3A"^Berghaus, K" OR author%3A"^Bobrow, E" OR
author%3A"^Bose, P" OR author%3A"^Brehm, D" OR author%3A"^Breysse, P" OR
author%3A"^Cantrell, S" OR author%3A"^Cao, L" OR author%3A"^Carey, N" OR
author%3A"^Caviglia, C" OR author%3A"^Chan, C" OR author%3A"^Chaudhuri, D" OR
author%3A"^Chen, H" OR author%3A"^Chen, K" OR author%3A"^Chen, Y" OR
author%3A"^Chen, Y" OR author%3A"^Chen, Y" OR author%3A"^Cheng, B" OR
author%3A"^Clemmer, J" OR author%3A"^Cordisco, A" OR author%3A"^Crichton, D" OR
author%3A"^Crosley, M" OR author%3A"^Dahal, S" OR author%3A"^Dasgupta, S" OR
author%3A"^Dugan, Z" OR author%3A"^Ely, D" OR author%3A"^Eminizer, N" OR
author%3A"^Engelke, P" OR author%3A"^Faroughy, C" OR author%3A"^Fehling, D" OR
author%3A"^Feng, L" OR author%3A"^Fogarty, K" OR author%3A"^Fuhrman, W" OR
author%3A"^Galvani Cunha, M" OR author%3A"^Ghosh, A" OR author%3A"^Greenbaum, A"
OR author%3A"^Hall, K" OR author%3A"^Harrington, K" OR author%3A"^Hart, M" OR
author%3A"^Hassan, N" OR author%3A"^Huang, C" OR author%3A"^Huang, Y" OR
author%3A"^Hussong, C" OR author%3A"^Iuliano, J" OR author%3A"^Jafari Alanjagh,
A" OR author%3A"^Jones, D" OR author%3A"^Karwal, T" OR author%3A"^Kinch, B" OR
author%3A"^Knizhnik, K" OR author%3A"^Lambrides, E" OR author%3A"^Lan, T" OR
author%3A"^Laurita, N" OR author%3A"^Lee, M" OR author%3A"^Lowry, I" OR
author%3A"^Maingi, L" OR author%3A"^Marcus, G" OR author%3A"^Meibody, R" OR
author%3A"^Mokris, J" OR author%3A"^Monti, J" OR author%3A"^Morris, M" OR
author%3A"^Mortazavi, A" OR author%3A"^Munoz, J" OR author%3A"^Nayak, O" OR
author%3A"^O'Connor, T" OR author%3A"^Osherson, M" OR author%3A"^Osumi, K" OR
author%3A"^Paul, B" OR author%3A"^Peth, M" OR author%3A"^Pfeffer, D" OR
author%3A"^Plunkett, E" OR author%3A"^Qu, D" OR author%3A"^Redwine, K" OR
author%3A"^Ren, B" OR author%3A"^Rivas, D" OR author%3A"^Rosenthal, S" OR
author%3A"^Roskes, H" OR author%3A"^Sady, A" OR author%3A"^Safarzadeh, M" OR
author%3A"^Sarica, U" OR author%3A"^Scheie, A" OR author%3A"^Sharp, T" OR
author%3A"^Shi, Y" OR author%3A"^Simons, R" OR author%3A"^Su, T" OR
author%3A"^Tchernyshyov, K" OR author%3A"^Tutmaher, J" OR author%3A"^Valentine,
M" OR author%3A"^Wang, H" OR author%3A"^Wang, Y" OR author%3A"^Watts, D" OR
author%3A"^Wolff, S" OR author%3A"^Wu, S" OR author%3A"^Xu, B" OR author%3A"^Xu,
Z" OR author%3A"^Yang, L" OR author%3A"^You, C" OR author%3A"^Zhang, S" OR
author%3A"^Zhang, X" OR author%3A"^Zhou, Y")) AND year%3A2005-2099)&sort=date
desc)


[Publication list (working, abridged)]
(https://ui.adsabs.harvard.edu/#search/fq={!type%3Daqp
v%3D%24fq_property}&fq_property=(property%3Arefereed)&q=((pos(aff%3A"Hopkins",1)
AND aff%3A"Astronomy" AND (author%3A"^Aguilar, J" OR author%3A"^Alexandroff, R"
OR author%3A"^Ali, A" OR author%3A"^Anand, N" OR author%3A"^Arpino, K" OR
author%3A"^Atakhodjaev, I" OR author%3A"^Bankert, J" OR author%3A"^Berghaus, K"
OR author%3A"^Bobrow, E" OR author%3A"^Bose, P" OR author%3A"^Brehm, D" OR
author%3A"^Breysse, P" OR author%3A"^Cantrell, S" OR author%3A"^Cao, L" OR
author%3A"^Carey, N" OR author%3A"^Caviglia, C" OR author%3A"^Chan, C" OR
author%3A"^Chaudhuri, D" OR author%3A"^Chen, H" OR author%3A"^Chen, K" OR
author%3A"^Chen, Y" OR author%3A"^Chen, Y" OR author%3A"^Chen, Y" OR
author%3A"^Cheng, B" OR author%3A"^Clemmer, J" OR author%3A"^Cordisco, A" OR
author%3A"^Crichton, D" OR author%3A"^Crosley, M" OR author%3A"^Dahal, S" OR
author%3A"^Dasgupta, S" OR author%3A"^Dugan, Z" OR author%3A"^Ely, D" OR
author%3A"^Eminizer, N" OR author%3A"^Engelke, P" OR author%3A"^Faroughy, C" OR
author%3A"^Fehling, D" OR author%3A"^Feng, L" OR author%3A"^Fogarty, K" OR
author%3A"^Fuhrman, W" OR author%3A"^Galvani Cunha, M")) AND
year%3A2005-2099)&sort=date desc
)
