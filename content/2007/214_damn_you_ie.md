Title: damn you ie
Date: 2007-04-16 13:59:39
Tags: imported
Category: 
Slug: damn_you_ie

Obviously do one who reads this uses Internet Explorer or they would have mentioned (hopefully) that my little drop case trick doesn't work in IE.  This is the CSS I'm currently using:

<code>p.dc:first-letter {
float: left;
font-size: 2.5em;
text-transform: uppercase;
font-weight:bold;
font-family: Georgia, Times, Verdana;
line-height: 0em;
color:#707070;
}</code>

It looks as though IE7 does support the <code>:first-letter</code> pseudo class, but the box model is failing with the <code>float: left</code>.  Any suggestions?
