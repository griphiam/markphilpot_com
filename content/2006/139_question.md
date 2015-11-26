Title: Question
Date: 2006-06-30 20:10:52
Tags: imported
Category: 
Slug: question

<p>Anyone who isn't a full fledged computer nut (or someone who does this for a living... I at least fit both categories) can move on to some of my other posts below (<a title="Knockout Round Review" href="http://blog.mcstudios.net/2006/06/28/world-cup-part-3/">World Cup Part 3</a> for example).&nbsp; However, if you aren't phased, please continue.</p>
<p>Why has no one done a one to one port of the extensive <a title="Java 1.4.2 API" href="http://java.sun.com/j2se/1.4.2/docs/api/index.html">Java libraries</a> to C++?&nbsp; I know there is <a title="Standard Library on Steriods" href="http://boost.org">Boost</a> which is basically an advanced extension to the C++ standard library, but wouldn't you think it would be worth while to have a 1 to 1 port where you didn't need to think about different syntax, the function and behavior was the same (or as close as you can get in C++ while still concerning yourself with memory management).&nbsp; Is there a technical reason?&nbsp; The productivity boost you get from Java comes from not having to worry about memory and by having an extensive library what works well together.&nbsp; You don't need to reinvent the wheel every time.&nbsp; They wouldn't be the most efficient libraries in the world, I understand that.&nbsp; And maybe the memory management aspect kills the idea, but I'm suprised I can't find anyone's attempt at it.</p>
<p>You see, I think the kicker would be since you can overload operators in C++, the distinction between Objects and primatives wouldn't be as drastic.&nbsp; For example you would be able to write:</p>
<pre>Integer i;</pre>
<pre>i++;</pre>
<pre>vector&lt;Integer&gt; i_vector;</pre>
<p>You would also get control over the stack and references, etc.&nbsp; Pointers would still had a complexity... (This is me thinking out loud).</p>
<pre>Integer * i = new Integer(0);</pre>
<pre>*i++;</pre>
<pre>vector&lt;Integer*&gt; ip_vector;</pre>
<p>Well, not nearly as clean.&nbsp; It would give you more control, and maybe that's the reason it wouldn't quite work.&nbsp; You would still have an abstract Object class that everything would inherit from.</p>
<p>So, could it work?&nbsp; Is it worth trying?&nbsp; Would anyone use it?</p>
<p><em>Update</em></p>
<p>Well, to partially answer my own question, there are least two attempts at an implementation that I've found -- <a href="http://sourceforge.net/projects/dol/" title="DOL">DObjectLibrary</a> and <a href="http://sourceforge.net/projects/fccl" title="FCCL">Free C++ Class Library</a>.&nbsp; The latter appears no longer maintained, with DObjectLibrary appearing the more advanced of the two and even provides a <a href="http://programics.com/dfc.php" title="DOL Homepage">Java to C++</a> translator!&nbsp; Pretty cool.&nbsp; So that partially answers my question.&nbsp; However, DOL is <a href="http://www.gnu.org/licenses/licenses.html#GPL" title="GNU General Public License">GPL</a> license... not a great move, considering this is exactly what the <a href="http://www.gnu.org/licenses/licenses.html#LGPL" title="GNU Lesser Public License">LGPL</a> was made for.<br /></p>
