# Testing
## Contents
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [PowerMapper Compatibility](#powermapper-compatibility)
+ [Testing From User Stories](#testing-from-user-stories)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Bugs](#known-bugs)
---

 *to be done ... - incorporating below into above headings*


 

> - After initial wireframe design, I checked each navigation item link is working correctly to each section or page. I set a _temporary_ contrasting background colour to each page to mark out each section.
> - Tested responsiveness of the wireframe using Dev Tools and confirmed basic structure looks and works well on all mobile decides from 320px, up to desktop size.

## ** Navigation Menu Bar tests **
> - Tested **Logo text** in menu bar to ensure it points to the Home page.
> - Tested default **Home, Bandstand Locations, Bandstand Amendments** links in menu bar to ensure they point to each section and position correctly.
> - Tested **Receive Favourites** link in menu bar (available/visible only when 1 or more favourite bandstands are listed) to ensure that it points to the section and positions correctly.

## ** General functional and usability tests **
> - Further testing of Responsiveness of the 2 pages using [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
> - 1. [Home Page] (https://search.google.com/test/mobile-friendly?id=M9vvg5u5KfcMuqIq6_Io7w)
> - 2. [404 Page] (https://search.google.com/test/mobile-friendly?id=DIHC02OvofNRfktdJEXZhA)
> - Tested overall site colours on [a11y](https://color.a11y.com/), a Color Contrast Accessibility Validator. Tests for both of the pages (index.html and 404.html) came back with excellent results (any reported anomalies were misdiagnosed).
> - Tested [HTML Validation](https://validator.w3.org/) No errors or warnings to show.
> - Tested [CSS Validation](https://jigsaw.w3.org/css-validator/)
> - 1.  Under Fieldset definition "Property xxx doesn't exist" Error on 6 items. Researched this and found that this is a non-issue as the 6 properties are required within the fieldset element to correctly format padding and margins in the modal form.
> - 2.  Warning 'Imported style sheets are not checked in direct input and file upload modes'. Confident to ignore these after researching and a common answer is that the validator will not validate imported style sheets. See [Stack Overflow] (https://stackoverflow.com/questions/25946111/importing-css-is-ending-up-with-an-error).
> - Tested [JS Validation](https://jshint.com/) No errors or warnings of concern outstanding. 
>   Here is a capture of the summary jshint reports for the 3 js modules coded by me (favoptions, mymap and mymodals) :
>   ![Image](/assets/images/jshint_reports_for_my_js_modules.png))
> - Tested [Python Validation](https://pylint.org/) No errors or warnings of concern outstanding. 
> - Tested site URL on [Website Page Test] (https://www.webpagetest.org/) which rendered good results except for some security header issues and caching - [available here](https://www.webpagetest.org/result/210629_AiDcK9_a9f4e72a2362574c9bb5d539805b4dfc/)
> - Tested site URL on [Responsinator](http://www.responsinator.com/) which returned no significant display issues across all device types in portrait and landscape modes.
> - Checked grammar and spelling throughout document.
> - Ran CSS through [Autoprefixer](https://autoprefixer.github.io/) and copied new CSS code back into style.css doc.
> - Re-ran CSS Validation and 6 warnings appeared for 'unknown vendor extension'. Confident to ignore these as answered on [Stack Overflow](https://stackoverflow.com/questions/5271955/css-parse-errors-from-a-generated-stylesheet).
> - Ran README text through [Online-Spellcheck](https://www.online-spellcheck.com/) to double-check on grammar and spelling.) No errors or warnings to show.
