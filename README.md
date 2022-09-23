# Attendance Management system using Face👦🏻👧 Recognition 

![image](https://user-images.githubusercontent.com/89336758/192049249-7381e7ee-68b0-4525-88d6-caddbcedfd3d.png)

# Code Requirements

 1. Opencv(pip install opencv-python),
 2. Tkinter(Available in python)
 3. PIL (pip install Pillow)
 4. Pandas(pip install pandas)
 
# What steps you have to follow??
  1. Download my Repository
  2. Create a TrainingImage folder in a project.
  3. Open a AMS_Run.py and change the all paths with your system path
  4. Run AMS_Run.py.

# What steps you have to follow??

 1.  Download or clone my Repository to your device
 2.  type pip install -r requirements.txt in command prompt(this will install required package for project)
 3.  Create a TrainingImage folder in a project folder.
 4.  open attendance.py and automaticAttendance.py, change all the path accoriding to your system
 5.  Run attandance.py file


# Project Structure

 1. After run you need to give your face data to system so enter your ID and name in box than click on Take Images button.
 2. It will collect 200 images of your faces, it save a images in TrainingImage folder
 3. After that we need to train a model(for train a model click on Train Image button.
 4. It will take 5-10 minutes for training(for 10 person data).
 5. After training click on Automatic Attendance ,it can fill attendace by your face using our trained model (model will save in TrainingImageLabel )
 6. it will create .csv file of attendance according to time & subject.
 7. You can store data in database (install wampserver),change the DB name according to your in AMS_Run.py.
 8. Manually Fill Attendace Button in UI is for fill a manually attendance (without facce recognition),it's also create a .csv and store in a database.


# Attendance in tabular format

![image](https://user-images.githubusercontent.com/89336758/192049759-b05641d6-339d-4be1-89fe-8d74c1fe306d.png)




# Notes

 1. It will require high processing power(I have 8 GB RAM & 2 GB GC)
 2. If you think it will recognise person just like humans,than leave it ,its not possible.
 3. Noisy image can reduce your accuracy so quality of images matter.
