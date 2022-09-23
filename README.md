##Attendance Management system using Face👦🏻👧 Recognition 

![image](https://user-images.githubusercontent.com/89336758/192049249-7381e7ee-68b0-4525-88d6-caddbcedfd3d.png)

Code Requirements

Opencv(pip install opencv-python)
Tkinter(Available in python)
PIL (pip install Pillow)
Pandas(pip install pandas)
What steps you have to follow??
Download my Repository
Create a TrainingImage folder in a project.
Open a AMS_Run.py and change the all paths with your system path
Run AMS_Run.py.

What steps you have to follow??

Download or clone my Repository to your device
type pip install -r requirements.txt in command prompt(this will install required package for project)
Create a TrainingImage folder in a project folder.
open attendance.py and automaticAttendance.py, change all the path accoriding to your system
Run attandance.py file


Project Structure
After run you need to give your face data to system so enter your ID and name in box than click on Take Images button.
It will collect 200 images of your faces, it save a images in TrainingImage folder
After that we need to train a model(for train a model click on Train Image button.
It will take 5-10 minutes for training(for 10 person data).
After training click on Automatic Attendance ,it can fill attendace by your face using our trained model (model will save in TrainingImageLabel )
it will create .csv file of attendance according to time & subject.
You can store data in database (install wampserver),change the DB name according to your in AMS_Run.py.
Manually Fill Attendace Button in UI is for fill a manually attendance (without facce recognition),it's also create a .csv and store in a database.


Attendance in tabular format

![image](https://user-images.githubusercontent.com/89336758/192049759-b05641d6-339d-4be1-89fe-8d74c1fe306d.png)




Notes

It will require high processing power(I have 8 GB RAM & 2 GB GC)
If you think it will recognise person just like humans,than leave it ,its not possible.
Noisy image can reduce your accuracy so quality of images matter.
