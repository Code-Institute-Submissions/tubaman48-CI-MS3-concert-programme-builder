# Testing
## Contents
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [Testing From User Stories](#testing-from-user-stories)
+ [Manual User Testing](#manual-user-testing)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Bugs](#known-bugs)
---

# Validator Testing

## Site Colours

 Tested overall site colours on [a11y](https://color.a11y.com/), a Color Contrast Accessibility Validator. Tested progs.html as an example and came back with acceptable results.
## HTML

I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/).

Because the code is made up of Jinja templates, I had to check from the live site by right clicking each page, selecting View Page Source and running that generated code through the validator.

All pages passed all checks.

As an example I passed https://github.com/tubaman48/CI-MS3-concert-programme-builder/blob/main/templates/progs.html through the validator and no errors or warnings showed up that were directly attributable to my code.
The warning and errors largely related to js elements under https://github.githubassets.com/assets/ outside my control.

## CSS
Tested [CSS Validation](https://jigsaw.w3.org/css-validator/).
I passed https://github.com/tubaman48/CI-MS3-concert-programme-builder/blob/main/static/css/style.css through the validator and no errors or warnings showed up that were directly attributable to my code. 
The warning and errors largely related to css elements under https://github.githubassets.com/assets/ outside my control.

## JavaScript

Skipped [JS Validation](https://jshint.com/) as my js file https://github.com/tubaman48/CI-MS3-concert-programme-builder/blob/main/static/js/script.js just contained standard jQuery functions (identical to those used in the Task Manager Mini Project within the CI LMS) plus one custom jQuery function developed to build the music_items_selector (utilised within the prog_add and prog_edit templates).

## Python
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks. 

> - Tested site URL on [Website Page Test] (https://www.webpagetest.org/) which rendered good results except for some security header issues - [available here](https://www.webpagetest.org/result/211218_AiDcYQ_211d7efc2852521e92d58ed5a750a260/)
> - Tested site URL on [Responsinator](http://www.responsinator.com/) which returned no significant display issues across all device types in portrait and landscape modes.
> - Checked grammar and spelling throughout document.
> - Ran CSS through [Autoprefixer](https://autoprefixer.github.io/) and copied new CSS code back into style.css doc.
> - Re-ran CSS Validation and 6 warnings appeared for 'unknown vendor extension'. Confident to ignore these as answered on [Stack Overflow](https://stackoverflow.com/questions/5271955/css-parse-errors-from-a-generated-stylesheet).
> - Ran README text through [Online-Spellcheck](https://www.online-spellcheck.com/) to double-check on grammar and spelling.) No errors or warnings to show.


# Lighthouse Testing

> - Rating as at 18:00 on 20th Sep 2021 - original submission (generated via Chrome referencing live Heroku app URL) :
![lighthouse-01](/static/images/MS3-lighthouse-rating-2021-09-20-1800.png)
> - Rating as at 02:50 on 12th Dec 2021 - resubmission (generated via Chrome referencing live Heroku app URL) :
![lighthouse-02](/static/images/MS3-lighthouse-rating-2021-12-18-0250.png)

# Testing From User Stories

## User Stories implemented thus far
> - _"As a music director we wish to construct concert programmes of music based on pieces that are available in the music library, pieces that we need to buy or pieces being arranged"_
> - - Catered for via the editable Programmes menu option available only to registered users. Note that for integrity purposes the editing and removal of programmes can only be carried by the creator of the programme.
> - _"As a music director we wish to be able to create, display, update and delete music programmes for upcoming concerts"_
> - - Catered for via the editable Programmes menu option available only to registered users. Note that for integrity purposes the editing and removal of programmes can only be carried by the creator of the programme.
> - _"As a music librarian I wish to be able to maintain a current list of music available with search, create, display, update and delete capabilities"_
> - - Catered for via the Music menu option available only to the librarian.
> - _"As a music librarian I wish to be able to maintain a current list of genres available to assign to music items with create, display, update and delete capabilities"_
> - - Catered for via the Genres menu option available only to the librarian.
> - _"As a music librarian I wish to be able to maintain a current list of venues available to assign to concert programmes with create, display, update and delete capabilities"_
> - - Catered for via the Venues menu option available only to registered users.
> - _"As a music librarian I wish to be able to maintain a current list of music programmes with create, display, update and delete capabilities"_
> - - Catered for via the editable Programmes menu option available only to registered users. Note that for integrity purposes the editing and removal of programmes can only be carried by the creator of the programme.
> - _"As a member of the band I wish to have access to search for and display any music programmes (historic and current) via registration process"_
> - _"As a member of the general public I wish to have access to search for and display any music programmes (historic and current) without having to register to the site"_
> - - Non-registered read-only access to programmes provided as per test screen capture scenario 1.1 below (Logged out (Programmes Page))
> - _"As a user of this resource (in any capacity) I would like a responsive design that caters for mobile and non-mobile devices"_
> - - Catered for using materialise css grid classes with some custom media queries to improve formatting for smaller mobile devices.

# Manual User Testing

> - After initial wireframe design, I checked each navigation item link is working correctly to each section or page. I set a _temporary_ contrasting background colour to each page to mark out each section.
> - Tested responsiveness of the wireframe using Dev Tools and confirmed basic structure looks and works well on all mobile decides from 320px, up to desktop size.

## Navigation Menu Bar tests
> - Tested **Logo text** in menu bar to ensure it points to the Programmes page.
> - Tested default **Programmes, Login, Register** links in menu bar to ensure they point to each section and position correctly.
> - Tested **Profile, Venues** links in menu bar (available/visible only to all logged on users) to ensure that it points to the section and positions correctly.
> - Tested **Music, Genres** links in menu bar (available/visible only to Librarian user) to ensure that it points to the section and positions correctly.
> - **Note** that the screenshots relate to Menu Bar tests carried out before original project submission in September 2021. No amendments have been made to the Menu Bar options since then - so original screenshots are still valid as at resubmission in December 2021.
## 1. User menu options (whilst logged out)

### 1.1 Logged out (Programmes Page)
> - Only **Programmes, Login, Register** links available in menu bar
![tsc-01-01](/static/images/test-screen-captures/tsc-01-01-loggedout-progs.png)

### 1.2 Logged out (Log In Page)
> - Only **Programmes, Login, Register** links available in menu bar
![tsc-01-02](/static/images/test-screen-captures/tsc-01-02-loggedout-login.png)

### 1.3 Logged out (Register Page)
> - Only **Programmes, Login, Register** links available in menu bar
![tsc-01-03](/static/images/test-screen-captures/tsc-01-03-loggedout-register.png)

## 2. User menu options (whilst logged in as general user)

### 2.1 Logged in - General User (Profile Page)
> - Only **Profile, Programmes, Venues, Log Out** links available in menu bar
![tsc-02-01](/static/images/test-screen-captures/tsc-02-01-loggedin-gen-profile.png)
> - Above screenshot is from immediately after successful registration - complete with "Registration Successful!" flash message

### 2.2 Logged in - General User (Programmes Page)
> - Only **Profile, Programmes, Venues, Log Out** links available in menu bar
![tsc-02-02](/static/images/test-screen-captures/tsc-02-02-loggedin-gen-progs.png)

### 2.3 Logged in - General User (Venues Page)
> - Only **Profile, Programmes, Venues, Log Out** links available in menu bar
![tsc-02-03](/static/images/test-screen-captures/tsc-02-03-loggedin-gen-venues.png)

## 3. User menu options (whilst logged in as Librarian user)

### 3.1 Logged in - Librarian User (Profile Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-01](/static/images/test-screen-captures/tsc-03-01-loggedin-lib-profile.png)
> - Above screenshot is from immediately after successful login - complete with "Welcome, Librarian" flash message

### 3.2 Logged in - Librarian User (Programmes Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-02](/static/images/test-screen-captures/tsc-03-02-loggedin-lib-progs.png)

### 3.3 Logged in - Librarian User (Music Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-03](/static/images/test-screen-captures/tsc-03-03-loggedin-lib-music.png)

### 3.4 Logged in - Librarian User (Genres Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-04](/static/images/test-screen-captures/tsc-03-04-loggedin-lib-genres.png)

### 3.5 Logged in - Librarian User (Venues Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-05](/static/images/test-screen-captures/tsc-03-05-loggedin-lib-venues.png)

# Responsive Testing

## General functional and usability tests
> - Further testing of Responsiveness of all the pages (excluding the nnn.html pages covering common http error codes) using [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
> - &#9989;01.- [Programmes Page] (https://search.google.com/test/mobile-friendly/result?id=l7qe3CJsh6XqOPzGlkAYiQ)
> - - &#9989;01-01. [Add Programme Page] (https://search.google.com/test/mobile-friendly/result?id=t_sK2VGJ-5jhFEqvZcgEyg)
> - - &#10060;01-02. [Edit Programme Page] (https://search.google.com/test/mobile-friendly/result?id=LrxKOFiXMfOMPeZsuwsmZA) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - &#9989;02.- [Log In Page] (https://search.google.com/test/mobile-friendly/result?id=WyFlXkgtB_PGMxvMewkfAA)
> - &#9989;03.- [Register Page] (https://search.google.com/test/mobile-friendly/result?id=iRmgwcaK1ayRUcQPO6RmtA)
> - &#10060;04.- [Profile Page] (https://search.google.com/test/mobile-friendly/result?id=tidGXj7-hI9iuTe5-5ZF2g) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - &#10060;05.- [Music Page] (https://search.google.com/test/mobile-friendly/result?id=3pR75-K446eN_lkzDbrAJQ) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - - &#9989;05-01. [Add Music Page] (https://search.google.com/test/mobile-friendly/result?id=Wlonui79eCpPMq5XcRaOSQ)
> - - &#10060;05-02. [Edit Music Page] (https://search.google.com/test/mobile-friendly/result?id=wGGSyOvmEjroJJvzDgM1ug) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - &#10060;06.- [Genres Page] (https://search.google.com/test/mobile-friendly/result?id=prBroa6HpTLE0HatACVWZg) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - - &#9989;06-01. [Add Genres Page] (https://search.google.com/test/mobile-friendly/result?id=LDBDaSkZ6iC1y6c4vYO4wQ) 
> - - &#10060;06-02. [Edit Genres Page] (https://search.google.com/test/mobile-friendly/result?id=3YlOFEHEGQp6928tsHe6ow) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - &#10060;07.- [Venues Page] (https://search.google.com/test/mobile-friendly/result?id=FfW_-l-QamfLPhKaPrm3jA) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - - &#9989;07.01 [Add Venues Page] (https://search.google.com/test/mobile-friendly/result?id=p7VZL-rNMUC3zUdLVT18OQ)
> - - &#10060;07.02 [Edit Venues Page] (https://search.google.com/test/mobile-friendly/result?id=ufYf4XkvgZYDVYIMVoK-Rg) "URL is not available to Google" - however this page was accessed successfully when used on an iPhone 11.
> - &#10060;08.- [HTTP 400 Error Page] (https://search.google.com/test/mobile-friendly/result?id=vqXW-JdrD8Gj7vDuB0aPrQ) "URL is not available to Google"
> - &#10060;09.- [HTTP 401 Error Page] (https://search.google.com/test/mobile-friendly/result?id=ZoWQ0XLp4lCbcCxdX-ClPA) "URL is not available to Google"
> - &#10060;10.- [HTTP 403 Error Page] (https://search.google.com/test/mobile-friendly/result?id=AMGhbZJLrbjtkWbqAcj5uA) "URL is not available to Google"
> - &#10060;11.- [HTTP 404 Error Page] (https://search.google.com/test/mobile-friendly/result?id=bfBNBQZ6uWo3uOklFGhDFg) "URL is not available to Google"
> - &#10060;12.- [HTTP 405 Error Page] (https://search.google.com/test/mobile-friendly/result?id=nldV3el5SGV-Ogt9kZFpcw) "URL is not available to Google"
> - &#10060;13.- [HTTP 500 Error Page] (https://search.google.com/test/mobile-friendly/result?id=vx3Ejf0XUy5dtOTJ4CaPWQ) "URL is not available to Google"


# Bugs and Fixes
## Title text overflow issue
> - Default font-size settings for materialise brand-logo class within nav elements was causing the title text to overflow outside of the nav bar area.
> - Resolution was to introduce some media query overrides within the style.css file.
## Auto-population of music items within a concert programme to be coded
> - Clunky manual copy and paste tool tip was in place on original project submission as a tactical solution to populate a selected music item within the programme based on the music item selected via the inline query just above the 6 music item entries. Extra code built to auto-populate into revised prog_items array within prog structure (replacing the 6 fixed items in prog_item_n strings - where n = 1 to 6). There are a couple of scenarios though where the new code does not work as expected - these exceptions are documented below in Known Bugs.

# Known Bugs
## Add Concert Programme "All Genres" selection discrepancy depending on when it is selected
> - If the "All Genres" drop down selection is the first Genre drop down selection it correctly returns a full candidate list of pieces sorted on Title within Genre, but if it follows the addition of a piece via a specifc genre subselection prior to saving the new programme entry, the full candidate list is returned unordered. Ran out of time to carry out a detailed debug to ascertain why this is happening.
## Edit Concert Programme "All Genres" selection discrepancy if some pieces already selected
> - If on entering the Edit Concert Programme page some pieces are already selected, then the "All Genres" drop down selection only returns those pieces already selected rather than a full list of all pieces available. Ran out of time to carry out a detailed debug to ascertain why this is happening.
