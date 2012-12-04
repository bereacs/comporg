---
title: Home
date: 2012 11 05
layout: minimal
---

# December 3, 2012

I need to know when all of the Tuesdays and Thursdays are next term. So, I searched for the phrase **python script generate dates**, and the [first hit](http://love-python.blogspot.com/2010/09/python-code-to-generate-dates-in-range.html) was most everything I needed.

I added a list to the function <code>generate_dates</code>, and appended the results to that list instead of printing them. I returned this list at the end of the function, so that I could capture the list in a variable (which I called "tuesdays"). Finally, I looped through the list, starting with the first entry (which was a Tuesday), added two (to get a Thursday), and then added five (to get to the next Tuesday). The loop terminates when I walk off the end of the list. The result? A printout of the dates of the Tuesdays and Thursdays next term.

2013-01-07
2013-01-09
2013-01-14
2013-01-16
2013-01-21
2013-01-23
2013-01-28
2013-01-30
2013-02-04
2013-02-06
2013-02-11
2013-02-13
2013-02-18
2013-02-20
2013-02-25
2013-02-27
2013-03-04
2013-03-06
2013-03-11
2013-03-13
2013-03-18
2013-03-20
2013-03-25
2013-03-27
2013-04-01
2013-04-03
2013-04-08
2013-04-10
2013-04-15
2013-04-17
2013-04-22
2013-04-24

That, however, was not good enough. I then wanted to have a Markdown page generated for every single Tuesday and Thursday; this way, I wouldn't have to create any new pages all term---I could just fill them in. And, then, I realized that each week should really have a page, and it should just include the pages. Again, I didn't want to write those pages myself... I wanted the script to generate them for me. 

So, I modified it. Now, it spits out a directory of pages for each day, and a directory of pages for each week. I put everything in the <code>_includes</code> folder in my Jekyll site, and I can include them one week at a time, with one line of code, on the main page.

The code lives in a Gist, which is a mini, disconnected Github repository. It's good enough for now, although I'll probably end up storing it somewhere in the repository for this site anyway.

<script src="https://gist.github.com/4199940.js?file=create-pages.py"></script>