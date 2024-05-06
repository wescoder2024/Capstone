Table of Contents:
- 1. Name of project
  2. Description of project
  3. Installation guide
  4. Usage guide
  5. Credits

  1.Name of project: Capstone
  
  2. Description of the project: This project is a website of a rockband.
     The website allows you to vote on the on questions about favourite songs or albums.
     You can also read a blog about some of the band participants.
     
  4. Installation guide:
     Make sure the files are organised the same way they are in the github repository
      Install django commands:
     - mkvirtualenv my_django
     - workon my_django
     - pip install django
     This will allow you to work on a vrtual environment and use django
     Run the server with this command:
      python manage.py runserver(Make sure you are in the directory as manage.py)
     Online port:
      http://127.0.0.1:8000 to access website home page
 
      Docker installation and run:
     
      Install docker desktop to run containers on the desktop.
     
      Once installed, go to the directory where your docker file is located(Usually .docker file) and run a command prompt from that directory.
     
      run command: docker build -t rockband ./ to build the docker image.
     
      run command: docker run -dp 8000:8000 rockband to run the docker image.
     
      type http://localhost(numeric):8000 in browser and the website should run in the browser.
      
     docker links:
     
     Docker repsository image link: https://hub.docker.com/repository/docker/wescoder2024/rockband/general
     
      Docker playground link: https://labs.play-with-docker.com/

  6. Usage guide:
     home page:
     ![Screenshot (41)](https://github.com/wescoder2024/Capstone/assets/167479161/2feb1bd2-4d4e-4b7f-aa2b-178f2c7b4ef3)

     login:
     ![Screenshot (42)](https://github.com/wescoder2024/Capstone/assets/167479161/72784a60-d87b-44ff-ae09-eecaeb531acf)

     welcome page:
     ![Screenshot (43)](https://github.com/wescoder2024/Capstone/assets/167479161/566b84ef-1bb0-48ad-8fc1-b6d45c2a3fd2)

     Register page:
     ![Screenshot (44)](https://github.com/wescoder2024/Capstone/assets/167479161/0d2e98ca-561b-4043-ac12-5ec4aa273a6f)
 
     You will be redirected to welcome page upon successful registration

     Blog pages:
     ![Screenshot (45)](https://github.com/wescoder2024/Capstone/assets/167479161/ea57523a-a525-48c8-b78a-de68677360aa)

     Individual blog page:
     ![Screenshot (46)](https://github.com/wescoder2024/Capstone/assets/167479161/607b9fd2-a33d-4d05-9390-be362485e7d4)

     Poll Questions(Need to login first):
     ![Screenshot (47)](https://github.com/wescoder2024/Capstone/assets/167479161/a69dc215-5bc7-4ffc-909f-ee002d6437bb)

     Poll answer choices:
     ![Screenshot (48)](https://github.com/wescoder2024/Capstone/assets/167479161/256ff1f9-d240-4299-b2bb-197c0f5715a7)

     Vote tally:
     ![Screenshot (49)](https://github.com/wescoder2024/Capstone/assets/167479161/a1410506-a603-40ec-8dd5-ec37c4b2e4db)

     Credits:
     Vincent.WN.2024.Django Login, Logout, Signup, Password Change, and Password Reset[online]Available from: https://learndjango.com/tutorials/django-login-and-logout-tutorial
[Accessed 19 march 2024]
     My mom and sister for using there tasks for references.






     



     
   
