#### Create & Read
![kuva](https://user-images.githubusercontent.com/58463139/119876801-f2eebe00-bf30-11eb-8d49-9bbe7136d42e.png)
#### Update
![kuva](https://user-images.githubusercontent.com/58463139/119876970-23cef300-bf31-11eb-94c9-c8862c9842a4.png)
#### Delete
![kuva](https://user-images.githubusercontent.com/58463139/119877015-32b5a580-bf31-11eb-9b1f-a1f5fe56803c.png)



Epähuomiossa olin viemässä kotitehtäviä versiohallintaan samaan aikaan, kun kotitehtävän ohjelma oli käynnissä.

Sain seuraavan virheilmoituksen:
```
sami@flask:~/FlaskCourse-ICT8TN034-3001$ git add . && git commit; git pull && git push
error: object file .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f is empty
error: object file .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f is empty
fatal: loose object 3d68715f59888dfcc009b9e0edbc4f00f04a0e7f (stored in .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f) is corrupt
error: object file .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f is empty
fatal: loose object 3d68715f59888dfcc009b9e0edbc4f00f04a0e7f (stored in .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f) is corrupt
```
```
sami@flask:~/FlaskCourse-ICT8TN034-3001$ git status
error: object file .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f is empty
error: object file .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f is empty
fatal: loose object 3d68715f59888dfcc009b9e0edbc4f00f04a0e7f (stored in .git/objects/3d/68715f59888dfcc009b9e0edbc4f00f04a0e7f) is corrupt
```
Löysin mahdollisen ratkaisun ongelmaan [täältä](https://stackoverflow.com/questions/11706215/how-to-fix-git-error-object-file-is-empty). Kiersin ongelman kloonaamalla versionhallintaan viedyn viimeisimmän version ja lisäämällä tekemäni
ohjelman kloonattuun varastoon.
