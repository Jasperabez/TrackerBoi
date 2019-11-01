---
layout: post
title: Using Jekyll pages
---

"Jekyll is a simple, blog-aware, static site generator for personal, project, or organization sites. Written in Ruby by Tom Preston-Werner, GitHub's co-founder" But what you need to know that is just that it can help you set up a bloglike site really really fast.

I used [Jekyll-now](https://github.com/barryclark/jekyll-now) for this specific site. Follow the detail steps as according to the link, and remember to tick the github pages option for your fork. After editing the config and set up everything you can add new post by putting the markdown files in the "_posts" folder.

## Sample post template

```
---
layout: post
title: Using Jekyll pages
---
```
the text above is the heading for all post you make, so put it at the top.

To be able to get the written date be sure to format the name of the file as "YYYY-MM-DD-POSTNAME.md" for example like this "2019-10-16-Using-Jekyll-pages"

## Some useful info

To refer to content in the site use this (remove the quotes):

```
{"{site.baseurl}"}
```

which points to the root directory of the site

## Final words
You are all set to whip up new posts using markdown, and [here's]({{ site.baseurl }}\Hans) a quick markdown cheatsheet that my friend Hans wrote to refer to :)
