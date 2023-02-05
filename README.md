# Design description
- tools/packages
  - Django
  - djangorestframework
- assumption
  - "Users are part of a company" == "Users are clients of a company once they have a card"
  - a user can have more than one card in any company
- class design
  - see class_design.pdf
- api design
  - `me/<str:company>/<str:name>`: check user information given company's name and user's name
  - `card/<str:company>/<str:name>/<int:card>`: identify user and check card information given compant's name, user's name and card number
  - `modify/<str:company>/<str:name>/<int:card_number>/<int:new_limit>`: identify user & permission, then modify card limit given compant's name, user's name, card number and new limit number
  - `create/<int:number>/<str:name>/<str:company>/<str:expiration_date>/<int:masked_number>/<int:limit>/<int:balance>/<str:permission>`: create a new card, update/create the user and update company information given relevant information

# Manual and testing
- setting up
  1. Virtual environment 
     1. cd Authorization-server
     2. create a new virtual environment by `python3 -m venv venv `
     3. then type `source venv/bin/activate` to activate your virtual environment
     4. install packages Django and restframework using `python -m pip install Django` and `pip install djangorestframework`
  2. cd src
  3. Create a superuser using `python manage.py createsuperuser`
  4. Start the server using `python manage.py runserver`.
  5. Go to `http://127.0.0.1:8000/admin/`, and login as a superuser
  6. Inside the interface, `create 2 company objects`. To be consistent with following sample data, name them as "a" and "b" , and leave other attributes blank.

- testing
  ## Challenge 1
  1. Create 2 cards and users of company "a" through `/create/<int:number>/<str:name>/<str:company>/<str:expiration_date>/<int:masked_number>/<int:limit>/<int:balance>/<str:permission>`
     ```
     Sample:
     Zhaoqi(admin): /create/100100/Zhaoqi/a/2023-05-05/555/8000/1000/admin
     Lukas(normal): /create/100500/Lukas/a/2023-05-05/555/8000/1000/normal
     ```
     You should see the `card information`, `user information` and `updated company information` on the screen or in the `/admin` interface
  
  2. Check user information and permission through `/me/<str:company>/<str:name>` 
     ```
     Sample:
     Zhaoqi: /me/a/Zhaoqi
     Lukas: /me/a/Lukas
     ```
     You should see the information on the screen
  
  3. Check card information through `/card/<str:company>/<str:name>/<int:card>`
     ```
      Sample1: Zhaoqi and Lukas check their own card
      Zhaoqi: /card/a/Zhaoqi/100100
      Lukas: /card/a/Lukas/100500

      Sample2: Zhaoqi(admin) can check Lukas' card, while Lukas(normal) cannot check Zhaoqi's card
      Zhaoqi: /card/a/Zhaoqi/100500
      Lukas: /card/a/Lukas/100100
      ```
      You should see the `user and card information` / `HTTP 401 Unauthorized` on the screen

  4. Modify card limit through `/modify/<str:company>/<str:name>/<int:card_number>/<int:new_limit>`
     ```
     Sample1: Zhaoqi(admin) can modify his own limit
     /modify/a/Zhaoqi/100100/4000

     Sample2: Zhaoqi(admin) can modify Lukas' limit
     /modify/a/Zhaoqi/100500/4000

     Sample3: Lukas cannot modify either his or Zhaoqi's limit
     /modify/a/Lukas/100100/4000
     /modify/a/Lukas/100500/4000
     ```
     You should see the `user, old and updated card information` / `HTTP 401 Unauthorized` on the screen
  ## Challenge 2
  1. Create cards for Zhaoqi and Lukas as normal users in company "b" through `/create/<int:number>/<str:name>/<str:company>/<str:expiration_date>/<int:masked_number>/<int:limit>/<int:balance>/<str:permission>`
     ```
     Sample:
     Zhaoqi(normal): /create/200100/Zhaoqi/b/2023-05-05/555/8000/1000/normal
     Lukas(normal): /create/200200/Lukas/b/2023-05-05/555/8000/1000/normal
     ```
     You should see the `card information`, `user information` and `updated company information` on the screen or in the `/admin` interface
  
  2. "The admin should be able to modify the credit card limit of the user in the first company but should not be able to make any other modifications in the second company." through `/modify/<str:company>/<str:name>/<int:card_number>/<int:new_limit>`
     ```
     Sample1: As an admin in company a & normal user in company b, Zhaoqi cannot modify his and Lukas' limit
     /modify/b/Zhaoqi/200100/4000
     /modify/b/Zhaoqi/200200/4000

     Sample2: As an admin in company a & normal user in company b, Zhaoqi cannot check Lukas' card
     /card/b/Zhaoqi/200200
     ```
     You should see `HTTP 401 Unauthorized` on the screen
