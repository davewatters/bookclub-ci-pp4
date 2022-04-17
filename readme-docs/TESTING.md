# Testing - The Bookclub Meetup Project

### [ Return to the project [README document](../README.md#testing) ]

## - Table of Contents -
* [Manual Testing](#manual-testing)
* [Automated Testing](#automated-testing)
* [Code Validation](#code-validation)


## Manual Testing

### UX Goals, User Stories

- #### As a first time user...  
  -  I want to be able to intuitively navigate the site  
      - All menu options were tested to ensure that they opened the correct functionality and that all of t returned to the main menu screen.  
        
    -  I want to be able to Sign Up as a member of the site
       - I tested that I could create a new registered user from the login screen

    -  I want the site to be visually clear & appealing  
       

-   #### As a returning visitor...
    -   I want to be able to 
    -   I want to be able to view 

-   #### As a frequent user...
    -   I want to to be able to increase the difficulty level of the game to make play more exciting  

<hr>

## Automated Testing
Automated testing was not used for this project.

<hr>

## Code Validation

The [W3C Markup Validator](https://validator.w3.org/#validate_by_uri), [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) and the [JSHint JavaScript Code Quality Tool](https://jshint.com) were used to validate every page of the project for syntax errors. **NOTE: All validation was re-run after fixing any errors shown below to ensure that no further errors or warnings existed.**

### HTML
<h2 align="center"><img src="w3c-validator-html_base.html.png"></h2>
<!-- <h2 align="center"><img src="w3c-validator-html_.png"></h2> -->

### CSS
<h2 align="center"><img src="w3c-validator-css_style.css.png"></h2>

### JavaScript
In the end, JavaScript use was minimal. JSHint returned no errors.

<!-- <h2 align="center"><img src="jshint-1_script.js.png"></h2> -->

### Python PEP8
The [PEP8 Online](http://pep8online.com) linter was used to ensure the code adhered to the Python Style Guidelines. However, as this is a Django project an exception to PEP8 was made for line lengths greater than 79.  Where lines were in or around 88 characters long, and no better readability could be achieved by shortening them, they were left as is. See the following doc about coding style: [Django Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#python-style)

- **`admin.py`**
<h2 align="center"><img src="admin_py-pep8.png"></h2>

- **`forms.py`**
<h2 align="center"><img src="forms_py-pep8.png"></h2>

- **`models.py`** - showing an example of lines which exceed the PEP8 recommended 79. Django Project recommends 88.  
<h2 align="center"><img src="models_py-pep8.png"></h2>

- **`views.py`** - showing an example of lines which exceed the PEP8 recommended 79. Django Project recommends 88.  
<h2 align="center"><img src="views_py-pep8.png"></h2>


<hr>

### [ [Click here to return to the project README document](../README.md#testing) ]
