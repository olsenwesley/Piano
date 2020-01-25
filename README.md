# Piano sheet music

## __Intro__

**_Piano_**

I am a self-taught classical pianist. Playing piano is what I love to do when I have time to myself. It is relaxing, fulfilling,
challenging and motivating.

A few years ago, I decided to push myself further and compete. I won first place at the American Protégé International Piano and Strings
Competition (adult amateur category), and got invited to play a recital at Carnegie Hall in NYC.

Since then, I continue playing classical music (my coup de coeur right now is Frederic Chopin), but I also decided to compose covers
of pop songs. I started a YouTube channel ([Wesley Olsen](https://www.youtube.com/user/dwholsen)) and plan on growing it. Some people have
even asked if I could give them the sheet music for my compositions!

**_Tech_**

I am also an engineer by training (Nanotechnology Engineering at University of Waterloo). I learned to code throughout my undergrad
program (**_MATLAB_**), but only associated coding with calculus, linear algebra, and quantum mechanics problems.

Today, I work as a process engineer and quality manager for a Fortune 500 manufacturing company. I do a lot of data manipulation using
**_SQL_** for work (self-taught), but for some reason, only a few months ago I caught the _data science bug_. So I took some bootcamp
courses in _Data Science and Machine Learning_ in **_R_** and **_Python_** on my own time (again, self-taught).
([Udemy](https://www.udemy.com/))

It really seems like the things I enjoy doing the most are things that I learn and figure out on my own...

**Then it clicked!**

With a few new programming languages under my belt, why not try to code my own sheet music!!! :astonished: :sunglasses:

So I read up on Abjad (Python API for formalized score control) and Lilypond (file format for music engraving), rolled up my
sleeves, and got to work!

One week later, I produced my own sheet music, coded in an object-oriented way. I never thought I would be able to mix my two seemingly
separate worlds in this way, but now I can! New hobby, here we come!

## __First coded piece (Chopin prelude Op. 28 No. 20)__

Since I have a limited repertoire of my own compositions, I decided to try to reproduce a short Chopin prelude using Python. After a lot of iterations in the code, the final product is here, located in this repository.

**_Analysis of the piece and coding logic_**

It is pretty evident in the piece that the first 4 measures are strong and regal, composed of firm chords with a second voice protruding
out on the third beat. Measures 5 to 8 repeat themselves for measures 9 to 12, which made my life easier; I could create the tuple containing the notes and chords for measures 5 to 8, and just concatenate it on itself, thus cutting down the code by a factor of two.

I decided to create each measure before adding on another empty measure to fill; this is a very logical approach. Because of this, I was able to create and fill measures through a while loop calling the appropriate index of the tuples containing notes and chords, for both the upper and lower measures. This cut down the length of the code considerably, making the actual sheet music code nice and compact.

Then all the bells and whistles were added to the sheet music (dynamics, fermatas, accents, title, composer, tempo, footer, etc.)

**_Drawbacks and room for improvement_**

As mentioned earlier, the third beat of each measure contains two voices. To ensure these two voices are captured in each measure, I decided to create a new container that holds only the two voices of the third beat, and then insert this container into the appropriate index position of the measure in question.

But because of this, I am unable to add ties, hairpins or slurs to the score. This is because the containers containing the two voices and the regular measures are not contiguous. If anyone knows how I can side-step this issue without drastically changing the code, please contact me!
