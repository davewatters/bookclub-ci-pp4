# The Bookclub Meetup Project

## A one-liner subheading goes here 

<br />

You can view the live deployed app [HERE.](https://ci-pp4-dw-bookclub.herokuapp.com/)
<br />

<!-- Responsive desgin sample image from http://ami.responsivedesign.is/ -->
<h2 align="center"><img src="readme-docs/#"></h2>

## - Table of Contents -
* [Purpose](#purpose)
* [User Experience Design (UX)](#user-experience-design)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## - Purpose -
[This app was created as the fourth Portfolio Project (PP4) for the Code Institute's Full Stack Web Development course. The app is to showcase skills to design a web application using an MVC framework and related contemporary technologies, and as a requirement is deployed to Heroku.]    


Some blurb about the app goes here  



## - User Experience Design -

-   ### User stories

    -   ### Design Strategy Goals
        -    Create a simple onine Blackjack card game which will appeal to wide range of users
        -    Site must be intuitive to read & navigate on both desktop & mobile devices - using Mobile First design

    -   ### Design Scope to Deliver MVP
        -   #### First Time Visitor Goals
            As a first time user...
            -   I want to be able to intuitively navigate the site
            -   I want to easily find instructions to understand how to use the site
            -   I want to be able to easily & quickly play the game
            -   I want the site to be visually clear & appealing

        -   #### Returning Visitor Goals
            As a returning visitor...
            -   I want to be able to quickly play the game
            -   I want to be able to view and play the game on a mobile device

        -   #### Frequent User Goals
            As a frequent user...
            -   I want to to be able to increase the difficulty level of the game to make play more exciting

-   ### Design
    -   #### Layout
         
    -   #### Content
       
    -   #### User Input
         
    -   #### Process/Logic Flow
        The basic menu-driven logic flow through the program is illustrated in the following flowchart..  
        <h2 align="center"><img src="readme-docs/flowchart-pwnytrap-ci-pp3.png"></h2>  

    -   #### Typography
        The Google font..


    -   #### Imagery
           
    
    -   #### Wireframes
        I did not create wireframes with software like Balsamiq, but I have decided to include pictures of my pencil sketches of my layout design process.  These do not necessarily represent the final look of the site pages, but are presented here to show how I went about fleshing out my initial thoughts and ideas about how to structure the site before a line of code was written.
<h2 align="center"><img src="readme-docs/wf-main-mobile.jpg"></h2>


## - Features -  
To fulfil the needs of the site's users, the following features were implemented:

- 

## - Future Features -
-    
<!--  -->
<!-- End Features -->
<!--  -->


## - Technologies Used -

### Languages Used

-   [Python 3.6+](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1.  [Git](https://git-scm.com/) was used for version control and managed via the VSCode terminal to commit to Git and Push to GitHub.
1.  [GitHub](https://github.com/) was used to store the project's code after being pushed from Git
1.  [Flake8](https://flake8.pycqa.org/en/latest/) linter extension for VScode 
1.  [Heroku](https://www.heroku.com) was used to deploy the app using a Code Institute template
1.  [LucidChart](https://lucidchart.com) was used to create the logic flowchart

<!---  --->
<!---  Begin testing section --->
<!---  --->

## - Testing -
### UX Goals, User Stories

-   #### As a first time user...
    -  I want to be able to intuitively navigate the site
       
    -  I want to easily find instructions to understand how to use the site
        
    -  I want to be able to 
    -  I want the site to be visually clear & appealing  
       

-   #### As a returning visitor...
    -   I want to be able to 
    -   I want to be able to view 

-   #### As a frequent user...
    -   I want to to be able to increase the difficulty level of the game to make play more exciting  
        

 
### Code Validation
-   The [PEP8 Online](http://pep8online.com) linter was used to ensure the code adhered to the Python Style Guidelines.
<h2 align="center"><img src=readme-docs/pep8.png></h2>

-   **https://pythex.org** was used to test both regular expressions used in the program: `email_regex` and `html_regex`.  I tested that `check_email()` correctly identifies email addresses with, for example, spaces in the domain name, or a typo like a comma in place of the 'dot'. For the regex used in `strip_html()` I checked some sample descriptions from the breach info.


### Bugs  

1. No known bugs at this time
<!---  --->
<!--- end of testing section --->
<!---  --->

## - Deployment -

### Heroku  
The live deployed site can be viewed on Heroku [HERE](https://ci-pp4-dw-bookclub.herokuapp.com)

The Project repository (repo) is at [https://github.com/davewatters/pwnytrap-ci-pp3](https://github.com/davewatters/)


Deployment of the site to Heroku was done as follows:
 
1.  Login to your Heroku account
1.  Create a New App
1.  (Important!) Select the 'Settings' tab first
1.  Click on 'Reveal Config Vars'
1.  Add any relevant config vars by entering the KEY/VALUE pair data, e.g. PORT & 8000
1.  Select 'Add Buildpack'
1.  (Important!) Select Python first, then select NodeJS
1.  Select the 'Deploy' tab
1.  For the Deplyoment Method select GitHub
1.  Connect to GitHub repo by entering YOUR-REPO-NAME, then Connect
1.  A message will confirm that your app was successfuly deployed
1.  Test that the site has successfully gone live by clicking on the 'View' button
1.  Your app can now be accessed via any browser at: `https://YOUR-APP-NAME.heroku.com`


## - Credits - 

-   

### Code

-   No code was directly copied to this project but numerous resources helped me understand what I needed and how best to code it. These include: The official [Python Docs](https://docs.python.org), StackOverflow.com, W3Schools.com, RealPython.com  
-   _Automate the Boring Stuff with Python, 2nd Edition_, Al Sweigart. Very helpful as an intro to implementing regex searching in Python and also working with the `requests` and `json` modules
-   https://www.regular-expressions.info/email.html
- 


### Acknowledgements

-   My mentor [Daisy McGirr](https://github.com/Daisy-McG) for all her helpful feedback and knowledge.
-   The Code Institute community on Slack and the CI staff and students for their feedback and support.
