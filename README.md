# Concert Programme Builder Website

![Image](/static/images/logos/ConcertProgrammeBuilder_icon_450x450.svg)

[View the live project here.](https://ci-ms3-concert-programme-build.herokuapp.com)


### The aim of this website is to **provide an intuitive tool to enable the easier construction of concert programmes by musical directors assisted by music librarian**.
### It is designed to be responsive and accessible on a range of devices, making it easy to navigate for four distinct groups of users :
-   User Admin for maintaining user access
-   Music Librarian for maintaining music catalogue items and concert programmes
-   Musical Directors for the creation and maintenance of concert programmes
-   Members of the public and band members who want to view concert programmes (past and present)

![Image](/static/images/CI-MS3-Concert-Programme-Builder_mock_up.png)

---

## Table of Contents

> + [Overview](#overview)
> + [Description](#description)
> + [User Experience](#user-experience)
> + [Features](#features)
> + [Database Schema](#database-schema)
> + [Technologies Used](#technologies-used)
> + [References for learning](#references-for-learning)
> + [Testing](#testing)
> + [Project barriers and the solutions](#project-barriers-and-the-solutions)
> + [Code validity](#code-validity)
> + [Version Control](#version-control)
> + [Deployment](#deployment)
> + [Credits](#credits)
> + [Acknowledgments](#acknowledgements)
> + [Support](#support)

**Please note: To open any links in this document in a new browser tab, please press `CTRL + Click`.**

---

# Overview

> There is currently no purpose built tool available to bands which enable music programmes to be easily assembled from a library of music.

---

# Description

> The Concert Programme Builder project is dedicated to enabling easier construction of music programmes for a band by the musical director(s) based on music available from the music librarian.

---

# User Experience

This website project focusses on usage by band librarians and musical directors with the transparency to show the concert programmes to a wider demographic of individuals covering other band members and the public at large, hence an overall simple, yet effective website is aimed at. 
The priority focus is on ease of use by the different types of user.

- ## 0. User Stories

The following user stories remain in the scope of the final project delivered :
> - _"As a music director we wish to construct concert programmes of music based on pieces that are available in the music library, pieces that we need to buy or pieces being arranged"_
> - _"As a music director we wish to be able to create, display, update and delete music programmes for upcoming concerts"_
> - _"As a music librarian I wish to be able to maintain a current list of music available with search, create, display, update and delete capabilities"_
> - _"As a music librarian I wish to be able to maintain a current list of genres available to assign to music items with create, display, update and delete capabilities"_
> - _"As a music librarian I wish to be able to maintain a current list of venues available to assign to concert programmes with create, display, update and delete capabilities"_
> - _"As a music librarian I wish to be able to maintain a current list of music programmes with create, display, update and delete capabilities"_
> - _"As a member of the band I wish to have access to search for and display any music programmes (historic and current) via registration process"_
> - _"As a member of the general public I wish to have access to search for and display any music programmes (historic and current) without having to register to the site"_
> - _"As a user of this resource (in any capacity) I would like a responsive design that caters for mobile and non-mobile devices"_

The following user stories were descoped early on in the project due to time constraints :
> - _"As a music director we would like to be able reference pieces in other band libraries that we could borrow"_
> - _"As a music director we wish to be able to search for music programmes for upcoming concerts"_
> - _"As a music director we wish to be able to search for historic music programmes to help formulate new programmes"_
> - _"As a music librarian I wish to be able to include in the current list of music available pieces that belong to another band's library which we have permission to borrow"_
> - _"As a music librarian I wish to be able to maintain a current list of bands available to assign to concert programmes with create, display, update and delete capabilities"_
> - _"As a User Admin I wish to be able to search for, create, display, update and delete users of the site"_
> - _"As a user of this resource (in any capacity) I would like to be able to print out individual concert programmes"_

- ## 1. Strategy

> The aim of this project is to facilitate more efficient construction of concert programmes, hence keeping the UX simple and user-friendly.
>
> ### Project Goals:
>
> - Providing a simple web-based tool to construct music programmes for a band.
> - Maintain the integrity of this resource by only permitting maintenance of concert programmes by the librarian and musical director(s), restricting the options available by the type of user.
>
> ### Customer Goals:
>
> - Designed site with Mobile-first approach
> - Easy to construct concert programmes (available only to the librarian and musical director(s) ).
> - Imagery used for intuitive explanation of which template page the user is on.
> - Enable a two-way engagement with users of this site.
> - Fixed navigation bar providing user easy navigation reference.

- ## 2. Scope

> I've decided on an MVP (Minimal Viable Product) approach, which:
>
> - Provides a clean UX for users.
> - Fits in with my current skill-set.
> - Hides content and options according to the user type.

- ## 3. Structure

> The main focus of the structure is to allow Users to quickly focus in on concert programmes of interest to them. 
> Short, focused paragraphs of content information to provide enough information, yet not overwhelm.
> A selection of quality images to project the template page the user is on.

- ## 4. Skeleton

> -  Wireframes available [here](/static/docs/RLs-CI-MS3-Wireframes.pdf). It should be noted that the display layouts actually developed have evolved since the these orginal wireframes were produced to generally improve the look and feel of the site. Key differences are the use of cards rather accordion devices for displaying the concert programmes and the ability introduced to store a variable number of music items within a programme. Revised Wireframes will be provided in the future.
> -  A multi page website using Flask to route to the appropriate template page, dependent on the options selected made up of the following pages :
> -  The Home page provides a textual introduction to the site.
> -  The Music Items page (only visible to the Librarian, Musical Director(s) and registered Band Members) presents a summary list of music items available with a search facility based on the Title. Additional edit capabilities are provided only to the Librarian, Musical Director(s) for integrity purposes.
> -  The Concert Programmes page (visible to all users) presents a summary list of concert programmes available with a search facility based on the venue and/or date. Additional edit capabilities are provided only to the Librarian, Musical Director(s) for integrity purposes. 
> -  The Concert Programme Details page (available via the Concert Programmes page) provides the date, times, venue and content of the programme with an option to print. (Note : the print feature was was dropped from the initial scope of this project due to time constraints)
> -  The Login / Register page.
> -  The User Admin page (only accessible to the User Admin) for the creation, display, search, update and delete of user profiles. (Note : this feature was dropped from the initial scope of this project due to time constraints)
>
> - Fixed navigation bar - Menu headings pointing to each of the available sections (dependent on user type).
>
> - Fixed Footer with Copyright info

- ## 5. Surface

> I've decided on the same colour scheme for the body of each separate page using just the title of the page to keep a sense of where you are on the site.
>
> ### Colours
>
> Soft (neutral) amber chosen as the background colour for the generic header section (including navigation bar).
> For body text, I've used the same amber colouring for images and text, with the exception of blue for search facilities, maintaining strong, balanced contrasts.
> 
> ### Typography
>
> - "Lato" font (with fall-back font of Verdana) for main headings and the footer. This font was specifically chosen for the header page title and subtitle and the footer copyright text.
> - "Oswald" font (with fall-back font of Sans-Serif) for body content.
>
> ### Images
>
> Image usage has been avoided for the initial version of the site so as not to detract from the development of the functionality required for an MS4 project.
> Possible future usage of images could revolve around pictures of venues to be used as appropriate background to the venue entries and the individual programmes to make this a more welcoming resource.

---

# Features

- ## Current Features

> ### **Navigation menu displayed across all pages**
>
> The navigation menu will help the user move easily across all pages. 
> For the collections pages, there is a dropdown menu in which all of those pages are held. 
> This stops the navigation from becoming too cluttered. 
>
> The navigation buttons update depending on whether a user is logged in, and whether that user is the admin
> (note that Concert Programmes can only be edited by the registered user who created them) :

| Nav Link              |Not logged in  |Logged in as user|Logged in as Librarian (admin)
|:-------------         |:------------- |:------------- |:------------- |
|Logo(back to home)     |&#9989;        |&#9989;        |&#9989;
|Profile                |&#10060;       |&#9989;        |&#9989;
|New Prog               |&#10060;       |&#9989;        |&#9989;
|Concert Programmes     |&#9989;        |&#9989;        |&#9989;
|Manage Music           |&#10060;       |&#10060;       |&#9989;
|Manage Genres          |&#10060;       |&#10060;       |&#9989;
|Manage Venues          |&#10060;       |&#9989;        |&#9989;
|Log Out                |&#10060;       |&#9989;        |&#9989;
|Register               |&#9989;        |&#10060;       |&#10060;
|Log In                 |&#9989;        |&#10060;       |&#10060;

> - Designed with HTML5, CSS3, Javascript, Python and Materialise within a Flask framework deployed onto Heroku.
> - Site made up of multiple template pages routed to via app.py made up of a fixed navigation bar followed by the appropriate content as outlined above under the UX Skeleton section
> - Fixed navigation allows the user to easily navigate, regardless of which section they are currently positioned in.
> - Fixed, stacked images for mobile views.

- ## Future Features Left to Implement when time allows

> - Expand the list of available pieces to incorporate pieces that belong to another band's library which we have permission to borrow, this would required amending the database schema include an extra music item status category of 'borrowed' which would hold extra fields denoting the band it has been borrowed from and the agreed time period that it has been borrowed for.

---

# Database

> MongoDB's non-relational database structure was ideal for this site as there were very few relationships between the collections on the site.
> Below are the definitions of the collections used within my database:

## genres collection

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|genre_name             |string         |used in *music_items* to describe type of music

## bands collection

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|band_name              |string         |used in *programmes* to detail the band playing

## venues collection

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|venue_name             |string         |used in *programmes* to detail the location of concert

## statuses collection

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|status_type            |string         |used in *music_items* to detail the whereabouts of each piece of music

## music_items collection

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|genre_name             |string         |each genre chosen by user from *genres*
|title                  |string         |name of the piece
|composer               |string         |composer of the piece
|arranger               |string         |arranger of the piece
|status                 |string         |denotes source of music
|created_by             |ObjectId       |object id taken from *users*

## programmes collection

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|band_name              |array          |each band chosen by user from *bands*
|concert_venue          |string         |location of concert from *venues*
|concert_date           |date           |date of concert
|concert_times          |time           |times of concert
|prog_items             |array          |each array entry represents a chosen item on programme as a string
|                       |               |which concatenates together the genre and the title from the piece.
|created_by             |ObjectId       |object id taken from *users*

## users collection

| User                  |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |used in *music_items* and *programmes*
|username               |string         |
|password               |string         |hashed password for user security


---

# Technologies Used

## 1. Languages Used

> - [HTML5](https://en.wikipedia.org/wiki/HTML5).
>
> - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets).
>
> - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
>
> - [Python3](https://www.python.org/)

## 2. Frameworks and Libraries Used

> - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
> - [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
> - [Pip3](https://pip.pypa.io/en/stable/)
> - [dnspython](https://www.dnspython.org/)
> - [jQuery](https://jquery.com/)
> - [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
> - [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
> - [Materialize](https://materializecss.com/)
>
> - [FontAwesome](https://fontawesome.com/) - used on all pages throughout the website to add icons for aesthetic and UX purposes.

## 3. Workspace, version control and Repository storage

> - [GitPod](https://github.com/mkuti/corklagos-venture/blob/master/gitpod.io) - Main workspace IDE (Integrated Development Environment)
>
> - [Git](https://git-scm.com/) - Distributed Version Control tool to store versions of files and track changes.
>
> - [GitHub](https://github.com/) - A cloud-based hosting service to manage my **Git** repositories.

## 4. Other

> - [Heroku](https://www.heroku.com/) used to deploy live site
> - [MongoDB](https://www.mongodb.com/) used to host database information.
> - [RandomKeygen](https://randomkeygen.com/) used to create a strong password for required  `<MS3_SECRET_KEY>`.
> - [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
> - [Autoprefixer](https://autoprefixer.github.io/) Parses CSS and adds vendor prefixes.
> - [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) Mobile-friendly check on site.
> - [Website Page Test](https://www.webpagetest.org/) Runs a website speed test from multiple locations around the globe using real browsers (IE and Chrome) and at real consumer connection speeds.
> - [Responsinator](http://www.responsinator.com/) Checks rendering across a variety of device types in landscape and portrait modes.  
> - [Online-Spellcheck](https://www.online-spellcheck.com/) Online spelling and grammar checks.

## 5. IDE Extensions used in GitPod

> - Auto Close Tag
> - Auto Nametag
> - Bracket Pair Colorizer
> - Code Spellchecker
> - Prettier - Code Formatter
> - Indent-Rainbow

---

# Resources

> - [Code Institute Course Content](https://courses.codeinstitute.net/) - Main source of fundamental knowledge.
> - Code Institute **SLACK Community** - Main source of assistance, especially the **JimLynx** webinar on the "Introduction to Git Workflow" which made the process of adding, committing and pushing in gitpod so much smoother.
> - [Stack Overflow](https://stackoverflow.com/) - General resource.
> - [Youtube](https://www.youtube.com/) - General resource.
> - [CSS-Tricks](https://css-tricks.com/) - General resource.
> - [W3.CSS](https://www.w3schools.com/w3css/4/w3.css) - General resource.
> - [CommonMark](https://commonmark.org/help/) - For Markdown language reference.
> - [Coolors](https://coolors.co/) - Find matching color palette for site.
> - [TinyPNG](https://tinypng.com/) - Efficient compression of images for site.
> - [Am I Responsive](http://ami.responsivedesign.is/) - Responsive website mockup image generator.
> - [Balsamiq](https://balsamiq.com/wireframes/) - Wireframing design tool.
---

# Testing

Due to the size of the testing section, I have created a separate document for it. You can find it [here](https://github.com/tubaman48/CI-MS3-concert-programme-builder/blob/main/TESTING.md).

---

# Project barriers and solutions

> - The key technical challenge for this particular site was to provide a clean and flexible automated method to select multiple pieces from the music_items collection.
> - The limited time available for the original submission of this MS3 project meant that at the time I had to put in a rather clumsy manual process to cut and paste selected pieces into up to 6 fixed entries, which was not to my liking.
> - However, for this resubmission I worked out the basis for the automated solution with strong guidance and superb technical input from my mentor Antonio Rodrigues, which I was able to take forward and mould into a tidier solution that enabled candidate lists to be generated, where the ticked selections were automatically populated into an array of entries.
> - There are still some glitches which need further attention to fix (documented [here](https://github.com/tubaman48/CI-MS3-concert-programme-builder/blob/main/TESTING.md#known-bugs) at the bottom of the TESTING.md under Known Bugs), but I hope it can be seen that it goes a long way towards providing the user experience that I intended.

---

# Code validity

> - HTML   - [W3C](https://validator.w3.org/) - Markup Validation
>
> - CSS    - [W3C](https://jigsaw.w3.org/css-validator/) - CSS Validation
>
> - JS     - [JSHint](https://jshint.com/) - Javascript Validation
>
> - PYTHON - [PyLint](https://pylint.org/) - Python Validation
>
> - TAGS   - [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) - Validates all tags are opening and closing correctly.

---

# Version Control

> - Used Git for version control.

---
# Deployment

### **GitHub**

> The Concert Programme Builder has been deployed on GitHub Pages with the following process:
>
> - All code was written on Gitpod, an online IDE.
> - The code was then pushed to GitHub where it is stored in my [Repository](https://github.com/tubaman48/CI-MS3-concert-programme-builder).
> - Under the [settings/pages](https://github.com/tubaman48/CI-MS3-concert-programme-builder/settings/pages) section of the GitHub repository, under 'Source' drop-down, the 'Main branch' was selected.
> - Once saved, this publishes the project to GitHub Pages and displays the site url.
> - There is no difference between the deployed version and the development version.

### **Local Deployment**

> - The code can be run locally through clone or download.
> - You can do this by opening the repository on GitHub, clicking on the green 'Code' button and selecting either 'clone or download'.
> - The Clone option provides a url ( https://github.com/tubaman48/CI-MS3-concert-programme-builder ), which you can use on your desktop IDE.
> - The Download ZIP option provides a link to download a ZIP file which can be unzipped on your local machine.
> - Alternatively, you can clone the repository using the following line in your terminal: git clone https://github.com/tubaman48/CI-MS3-concert-programme-builder
> - Access the folder in your terminal window and install the application's required modules using the following command: pip3 install -r requirements.txt
> - Create the Procfile required for the Heroku App by issuing the command "echo web: python app.py > Procfile". The Procfile should now contain the following line :
web: python app.py

#### MongoDB set up
> - Sign-in or sign-up to MongoDB and create a new cluster (the information required is documented on the CI public GitHub at https://github.com/Code-Institute-Solutions/MongoDB/blob/master/01-CreateAMongoDBDatabase/01-create_a_mongodb_database/mongoSetup.md)
> - Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) called programme_builder
> - Set up the following collections: bands, genres, music_items, progs, statuses, users, and venues. Refer to earlier Database section in this README to set up the exact structure for each collection. 
> - Also, an extra second index named genre_name_text_title_text needs to be set up for collection music_items, as per following screenshot :
![Image](/static/images/MongoDB-setup-2nd-index-for-music_items.png)
> - Under the Security menu on the left, select Database Access.
> - Add a new database user, and keep the credentials secure
> - Within the Network Access option, add IP Address 0.0.0.0
> - In your IDE, create a file containing your environmental variables called env.py at the root level of the application. It will need to contain the following lines and variables: 

"""
Local environment settings
"""

import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("MS3_SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
os.environ.setdefault("MONGO_DBNAME", "programme_builder")

> - YOUR_MONGODB_URI will be the value within MongoDB found by going to clusters> connect> connect to your application and entering your passwords and dbname within the link.
> - The project was deployed to Heroku for the live site and the pushes to GitHub automatically pushed to Heroku to update the live site. 
> - Please note that this project will only run locally if : 1) an env.py file is set up containing the IP, PORT, MS3_SECRET_KEY, MONGO-URI and MONGO_DBNAME and 2) (for GitPod users) the above 5 variables are set up with the same values under Settings>Variables within your Gitpod Workspace. 
>   For security reasons these details will not be shared on this documentation. The env.py file should be added to your gitignore file.

### **Heroku**

> - **Deployment to Heroku**
>
> - **Create the application:**
>  
>      * Login in to heroku.com
>      * Click on New, and Create new app
>      * Enter your app name
>      * Select the region that is closest to you
>  
> - **Connect to you GitHub repository**
>  
>      * Click Deploy and select GitHub - Connect to GitHub
>      * Enter your repository name and search
>      * Click Connect on the correct repository
>  
> - **Set Your Environment Variables**
>  
>  Go to settings, and within Config Vars enter the following
>  
>      * IP: 0.0.0.0
>      * PORT: 5000
>      * MS3_SECRET_KEY: (This is a secret password that must be very secure - recommend selecting a "Fort Knox Password" at https://randomkeygen.com/)
>      * MONGO_DBNAME: (enter the database name that you are connecting to - in this case *programme_builder* )
>      * MONGO_URI: (enter your mongo uri. This is found by going to clusters> connect> connect to your application and entering your passwords and dbname within the link)
>  
> - **Enable Automatic Deploys**
>  
>      * Go to the deploy tab
>      * Within the automatic deploys section, choose the branch that you want to deploy from and select Enable Automatic Deploys. 

# Credits

> ## Media
>
> - The main "hero-image" used in this project is _owned and provided by myself_
> - The icons utilised in the **Technology Used** section of the README for this project were obtained from [FontAwesome](https://fontawesome.com/)
> - The "Concert Programme Builder" site icon was created via my tubaman48 account at [vectr.com](https://vectr.com/).
>
> ## Content
>
> - All text content is _self-written_
>
> ## Code Snippets
>
> - [Code Institute](https://codeinstitute.net/) - Inspiration for user profile management and 'CRUD' processing from 'Task Manager' Mini-Project in Backend Development Module.
> - [W3.org](https://www.w3.org/2005/10/howto-favicon) - How to add a Favicon to site.

---

# Acknowledgements
>
> I would like to thank:
>
> - A combination of *Amy O'Shea* and *Rachel Sherlock* for their example MS3 README.md files :
>      https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/README.md
>      https://github.com/Rachel2308/MS3-belles-task-manager/blob/master/README.md
>   These examples significantly helped me with formatting of the database schema / nav link accessibility table within features / deployment sections within this README for the original project submission.
> - *Marina Shalneva* for her example MS3 README.md file :
>      https://github.com/marina601/scooter-circle/blob/master/README.md
>   This helped me to improve my local deployment instructions for the project resubmission.
> - My mentor *Antonio Rodrigues* - especially for his technical guidance for my resubmission (so quickly imparted over 2 or 3 interactive sessions within a few days).
> - **CI staff** and **Slack Community** for always being on-hand with questions posted and assistance requests.
> - Everyone that takes part in the Slack calls, specifically from the **#In-It-Together** and **#London Community** channels.

# Support

> For any issue resolution or assistance, please email Richard Lovett on rjlovett48@gmail.com

---