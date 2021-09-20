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

Skipped [JS Validation](https://jshint.com/) as my js file https://github.com/tubaman48/CI-MS3-concert-programme-builder/blob/main/static/js/script.js just contained standard jQuery functions (identical to those used in the Task Manager Mini Project within the CI LMS).

## Python
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks.

> - Tested site URL on [Website Page Test] (https://www.webpagetest.org/) which rendered good results except for some security header issues - [available here](https://www.webpagetest.org/result/210911_BiDc74_312dfb8766f43fdacee85cee11939146/)
> - Tested site URL on [Responsinator](http://www.responsinator.com/) which returned no significant display issues across all device types in portrait and landscape modes.
> - Checked grammar and spelling throughout document.
> - Ran CSS through [Autoprefixer](https://autoprefixer.github.io/) and copied new CSS code back into style.css doc.
> - Re-ran CSS Validation and 6 warnings appeared for 'unknown vendor extension'. Confident to ignore these as answered on [Stack Overflow](https://stackoverflow.com/questions/5271955/css-parse-errors-from-a-generated-stylesheet).
> - Ran README text through [Online-Spellcheck](https://www.online-spellcheck.com/) to double-check on grammar and spelling.) No errors or warnings to show.


# Lighthouse Testing

> - Rating as at 18:00 on 20th Sep 2021 (generated via Chrome referencing live Heroku app URL) :
![lighthouse-01](/static/images/MS3-lighthouse-rating-2021-09-20-1800.png)

# Testing From User Stories

## User Stories
> - _"As a music director we wish to construct concert programmes of music based on pieces that are available in the music library, pieces that we need to buy or pieces being arranged"_
> - _"As a music director we wish to be able to search for, create, display, update and delete music programmes for upcoming concerts"_
> - _"As a music director we wish to be able to search for historic music programmes to help formulate new programmes"_
> - _"As a music librarian I wish to be able to maintain a current list of music available with search, create, display, update and delete capabilities"_
> - _"As a music librarian I wish to be able to maintain a current list of music programmes with search, create, display, update and delete capabilities"_
> - _"As a User Admin I wish to be able to search for, create, display, update and delete users of the site"_
> - _"As a member of the band I wish to have access to search for and display any music programmes (historic and current) via registration process"_
> - _"As a member of the general public I wish to have access to search for and display any music programmes (historic and current) without having to register to the site"_
> - _"As a user of this resource (in any capacity) I would like a responsive design that caters for mobile and non-mobile devices"_

# Manual User Testing

> - After initial wireframe design, I checked each navigation item link is working correctly to each section or page. I set a _temporary_ contrasting background colour to each page to mark out each section.
> - Tested responsiveness of the wireframe using Dev Tools and confirmed basic structure looks and works well on all mobile decides from 320px, up to desktop size.

## ** Navigation Menu Bar tests **
> - Tested **Logo text** in menu bar to ensure it points to the Programmes page.
> - Tested default **Programmes, Login, Register** links in menu bar to ensure they point to each section and position correctly.
> - Tested **Profile, Venues** links in menu bar (available/visible only to all logged on users) to ensure that it points to the section and positions correctly.
> - Tested **Music, Genres** links in menu bar (available/visible only to Librarian user) to ensure that it points to the section and positions correctly.

## ** 1. User menu options (whilst logged out) **

### ** 1.1 Logged out (Programmes Page)
> - Only **Programmes, Login, Register** links available in menu bar
![tsc-01-01](/static/images/test-screen-captures/tsc-01-01-loggedout-progs.png)

### ** 1.2 Logged out (Log In Page)
> - Only **Programmes, Login, Register** links available in menu bar
![tsc-01-02](/static/images/test-screen-captures/tsc-01-02-loggedout-login.png)

### ** 1.3 Logged out (Register Page)
> - Only **Programmes, Login, Register** links available in menu bar
![tsc-01-03](/static/images/test-screen-captures/tsc-01-03-loggedout-register.png)

## ** 2. User menu options (whilst logged in as general user) **

### ** 2.1 Logged in - General User (Profile Page)
> - Only **Profile, Programmes, Venues, Log Out** links available in menu bar
![tsc-02-01](/static/images/test-screen-captures/tsc-02-01-loggedin-gen-profile.png)
> - Above screenshot is from immediately after successful registration - complete with "Registration Successful!" flash message

### ** 2.2 Logged in - General User (Programmes Page)
> - Only **Profile, Programmes, Venues, Log Out** links available in menu bar
![tsc-02-02](/static/images/test-screen-captures/tsc-02-02-loggedin-gen-progs.png)

### ** 2.3 Logged in - General User (Venues Page)
> - Only **Profile, Programmes, Venues, Log Out** links available in menu bar
![tsc-02-03](/static/images/test-screen-captures/tsc-02-03-loggedin-gen-venues.png)

## ** 3. User menu options (whilst logged in as Librarian user) **

### ** 3.1 Logged in - Librarian User (Profile Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-01](/static/images/test-screen-captures/tsc-03-01-loggedin-lib-profile.png)
> - Above screenshot is from immediately after successful login - complete with "Welcome, Librarian" flash message

### ** 3.2 Logged in - Librarian User (Programmes Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-02](/static/images/test-screen-captures/tsc-03-02-loggedin-lib-progs.png)

### ** 3.3 Logged in - Librarian User (Music Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-03](/static/images/test-screen-captures/tsc-03-03-loggedin-lib-music.png)

### ** 3.4 Logged in - Librarian User (Genres Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-04](/static/images/test-screen-captures/tsc-03-04-loggedin-lib-genres.png)

### ** 3.5 Logged in - Librarian User (Venues Page)
> - Only **Profile, Programmes, Music, Genres, Venues, Log Out** links available in menu bar
![tsc-03-05](/static/images/test-screen-captures/tsc-03-05-loggedin-lib-venues.png)

# Responsive Testing

## ** General functional and usability tests **
> - Further testing of Responsiveness of all the pages (excluding the nnn.html pages covering common http error codes) using [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
> - &#9989;01.- [Programmes Page] (https://search.google.com/test/mobile-friendly?id=zkKOTxnvCJGYXjJV9EIYdA)
> - - &#9989;01-01. [Add Programme Page] (https://search.google.com/test/mobile-friendly?id=1q8UeWbBw43hWaiE8IJ9xQ)
> - - &#10060;01-02. [Edit Programme Page] (https://search.google.com/test/mobile-friendly?id=fzYmIfGMJ4GdBoz59gbcng) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt" - however this page was accessed successfully when used on an iPhone 11.
> - &#9989;02.- [Log In Page] (https://search.google.com/test/mobile-friendly?id=nYynSGepKX09_OGRKYna3A)
> - &#9989;03.- [Register Page] (https://search.google.com/test/mobile-friendly?id=IKq5rh65d7QHlEZCrkjnYA)
> - &#10060;04.- [Profile Page] (https://search.google.com/test/mobile-friendly?id=QCn6N3b3QiVe38xYo1O_uQ) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt" - however this page was accessed successfully when used on an iPhone 11.
> - &#9989;05.- [Music Page] (https://search.google.com/test/mobile-friendly?id=R0kNPnKbOQBe7YRvMmLCWQ)
> - - &#9989;05-01. [Add Music Page] (https://search.google.com/test/mobile-friendly?id=kwmhhcJ8yrcyXQ5seSn4MA)
> - - &#10060;05-02. [Edit Music Page] (https://search.google.com/test/mobile-friendly?id=avLeR8Tolm5Cwo1SU0FNLg) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt" - however this page was accessed successfully when used on an iPhone 11.
> - &#9989;06.- [Genres Page] (https://search.google.com/test/mobile-friendly?id=Ewy1psd1VfrvE9iN9dgU9w)
> - - &#9989;06-01. [Add Genres Page] (https://search.google.com/test/mobile-friendly?id=Qn4PSHspFZmBpt_E5Z1AcQ) 
> - - &#10060;06-02. [Edit Genres Page] (https://search.google.com/test/mobile-friendly?id=eny8DYGzsMb1D2eXYGl2rA) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt" - however this page was accessed successfully when used on an iPhone 11.
> - &#9989;07.- [Venues Page] (https://search.google.com/test/mobile-friendly?id=fKRQNRUZlX-xBb7eCizsNw)
> - - &#9989;07.01 [Add Venues Page] (https://search.google.com/test/mobile-friendly?id=1PywRqrXaJDNLiTpFNiNwg)
> - - &#10060;07.02 [Edit Venues Page] (https://search.google.com/test/mobile-friendly?id=ASJe4ALw2spCk0IKh5GKRQ) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"
> - &#10060;08.- [HTTP 400 Error Page] (https://search.google.com/test/mobile-friendly?id=xlalJKuvLke1qTscGXWY3Q) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"
> - &#10060;09.- [HTTP 401 Error Page] (https://search.google.com/test/mobile-friendly?id=fkdW3Pd5Osf1_jywG5ugPA) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"
> - &#10060;10.- [HTTP 403 Error Page] (https://search.google.com/test/mobile-friendly?id=ysfsERxVgZwWD_I0PU_LFw) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"
> - &#10060;11.- [HTTP 404 Error Page] (https://search.google.com/test/mobile-friendly?id=pmbWe40NeONUiAImmR5gYw) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"
> - &#10060;12.- [HTTP 405 Error Page] (https://search.google.com/test/mobile-friendly?id=9ETDaD6wj1qmaFNvPiX47Q) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"
> - &#10060;13.- [HTTP 500 Error Page] (https://search.google.com/test/mobile-friendly?id=gy919xtILkOyq53eVoZNaQ) "Page cannot be reached
This could be because the page is unavailable or blocked by robots.txt"


# Bugs and Fixes

# Known Bugs
 

