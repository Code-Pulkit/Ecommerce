# Ecommerce Website - 

Motivation --> 
  1. Wanted to Learn more about Web Development
  2. Apply all the Learning from the courses undertaken.

Ideation --> 
  1. First and Foremost , I looked up at famous e commerce websites for inspiration. I saw that they had Landing Pages , Specific Category Page , 
  Login , Registration and Cart Pages.One Feature that intersted me was that a single id can have multiple Users with different address ,  
  so I also tried to implement.
  
  So I decided my UX that A person would start at landing page, if login could directly add things to the cart and proceed for checkout else to login page.
  On checkout he would be asked for address and payment method. Boom Once Payment is done , Order should be placed.
  
UI Design --> 
  1. I created wireframes using Bootstrap but roughly drew the design on Whimisical.

Model Ideation --> 
  1. Based on my exploration , I found 2-3 features really good and tried to implement on my project. 
     Single User - Multiple Address
     Filtering Based on Category(Didn't implemented Search Bar)
     Forget Password Mailing 

  2. User (Login One ) , Customer (Address of User) , Product () , Order() , Cart() and added them to admin.py

Then I coded all the views (static with Dummy Data).
  1. I added some dummy data in the Products from Django Admin also installed Pillow. 
  2. I had firstly implement the feature of dynamic content rendering on my website. 
  3. Then for Specific Rendering Like Mobiles differntiated by category , different filters were used(SideBar Filter).
     basiccally differnt URL calls and distinguish on that
 
Then I implemented Registration - 
  UserCreationForm - Inbuild (More Secure and Validations)
For informing the user that account had been successfully created, I used messages library.
There could be 2 kinds of errors while submitting the form - label_tag and non_field_error.

Then I implemented Login - 
  AuthenticationForm (Username Field Standard) - 
  PasswordChange , 
  PasswordReset from auth_views
  
Created Some dummy data for Customers. 
Implemented the feature that when a user is logged in , he could move to checkout. 
In the checkout , given a feature to add more addresses(Customer DataBase Updation). 
