# Ad_System_Project
-------Working of the project---------
#Every ad have specific locations where it will show and we have set the number of users for each location who can visit the ad according to their location. If this limit reached then ad will block in that location but it will open for other locations.Every midnight mean 12 pm 2 cron jobs will run. One cron job will reset the total number of users to 0 who visited the ad per day. this will done file ( "update_location_users_per_day.py"). Second job will create a text file in this file following content will show file name ("generate_text_file.py")

Ad-name: Ad1
Location: Lahore
Total no of users allowed for Ad1 per day: 100
Total users from Lahore viewed Ad1 per day: 30
Viewed Details of each User
test viewed the Ad1 for 5 times 

#Example:
# We have a ad named Ad1 and its locations Lahore(total user who can view the ad = 10),Karachi(total user who can view the ad = 15), if 10 users who belong from Lahore view the Ad1 then Ad1 will block for 11th user belong from Lahore. But Ad1 is still open for users of Karachi untill their limit == 15. users of other locations like Multan,Faisalabad can not view the Ad1 and it will show message that you are unable to view the ad. becuse Ad1 have locations Lahore and Karachi. 

#Now user1 belongs from Lahore view the Ad1 50 times per day, it will count one user not 50, like Youtube videos, one user can view the video 100 times or more but it count as 1 view same here, Ad1 will close when number of users become 10 because its limit sets to 10 per day. And same for other locations according to thier set limts.

#At mid-night or 12pm it will create a file for each ad seprately and stored these files in model "FileStored" and set ad will open again for the users if its limit reached.

# To add locations use this url "http://127.0.0.1:8000/api/v1/locations/"
#To add ads use this url "http://127.0.0.1:8000/api/v1/ads/"      
#Payload for adding the ads 
{
    "locations": [],
    "ad_name": "",
    "start_date": null,
    "end_date": null
}
#To add user-locations mean which user belongs from which location use this url "http://127.0.0.1:8000/api/v1/user-locations/"
#To view the ad use this url "http://127.0.0.1:8000/api/v1/view-ad-by-name/?ad_name=Ad"
#Provide the ad_name as a query parameter, if you will not provide the ad_name it will raise error and also if provided the wrong ad name again error. Only authenticated users can access the api. I have created some user, you can also create the users. Username and passwords are given below
1- username:admin1    Password:admin1
2- username:admin2    Password:adminadmin22
3- username:admin3    Password:adminadmin33
4- username:test    Password:test
5- username:test1    Password:testtest11


 


