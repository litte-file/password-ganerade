# passworld ganerade

# how do i start the application
  
### **to make it run**

(MacOs/linux)
```
$source myenv/bin/activate

$python src/main.py
```
#### or
```
$./run.sh
```

(Windows) 
```
$myenv\Scripts\activate

$python src/main.py
```
  >write terminal `jupyter notebook mainjnb.ipynb` for jupyter notebook version.


### how do i passwordganerade.desktop setup

#### 1. open the passwordganerade.desktop file in a text editor

#### 2. type the path in the file Exec= section you opened.
#### SAMPLE: Exec=/home/ai/app/password-ganerade/run.sh

#### 3. type the path in the file Icon= section you opened.

#### SAMPLE: Icon=/home/ai/app/password-ganerade/password.png

#### 4. the file you opened will look like this

##### SAMPLE:

```
[Desktop Entry]
Name=Password Ganerade \
Comment=Terminalde çalışan şifre oluşturma uygulamanızı başlatır.\
Exec=/home/ai/app/password-ganerade/run.sh \
Icon=/home/ai/app/password-ganerade/password.png \
Terminal=true \
Type=Application \
Categories=Utility; 
```
#### 5. if it is like the file i give for sample save your file
#### 6. /usr/share/applications/ copy the file

##### SAMPLE:
```
$cp project/password-ganerade/passwordganeradedesktop /usr/share/applications/
```

#### 7. type this command sudo update-desktop-database if it doesnt work find a command like this or reboot

#### 8. open the run.sh file in a text editor

#### 9. set the path to the password-ganerate file in the cd section you thhe file you opened

#### SAMPLE: cd /path/to/password-ganerade/

#### 10. the file you opened will look like this

##### SAMPLE:

```
#!/bin/sh
cd /home/ai/project/password-ganerade/
python main.py
```

#### 11. if it is like the file i give for sample save your file

### $done$
