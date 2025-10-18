# Chapter 1

- I remember the reaction

where he had drawn these characters

and he was slowly moving around

and like people had no experience with 3D navigation,

it was all still keyboard.

We didn't even have mice set up at that time.

But slowly moving, going up, picked up a key, go to a wall,

the wall disappears in a little animation

and there's a monster like right there.

And he practically fell out of his chair.

It was just like, ah.

And games just didn't do that.

The games were the god's eye view.

You were a little invested in your little guy.

You can be like happy or sad when things happen,

but you just did not get that kind of startle reaction.

- You weren't inside your game.

- Something in the back of your brain,

some reptile brain thing is just going,

"Oh, shit something just happened."

And that was one of those early points where it's like,

yeah, this is gonna make a difference.

This is going to be powerful and it's gonna matter.

- The following is a conversation with John Carmack,

widely considered

to be one of the greatest programmers ever.

He was the co-founder of id Software

and the lead programmer on several games

that revolutionized the technology,

the experience and the role of gaming in our society,

including Commander Keen, Wolfenstein 3D, Doom and Quake.

He spent many years as the CTO of Oculus VR,

helping to create portals into virtual worlds

and to define the technological path to the Metaverse

at Meta.

And now he has been shifting some of his attention

to the problem of artificial general intelligence.

This was the longest conversation on this podcast

at over five hours,

and still I could talk to John many, many more times

and we hope to do just that.

This is the "Lex Fridman Podcast."

To support it,

please check out our sponsors in the description.

And now, dear friends, here's John Carmack.

What was the first program you've ever written?

Do you remember?

- Yeah, I do.

So, I remember being in a radio shack going up

to the TRS 80 computers

and learning just enough to be able to do 10 print,

John Carmack.

And it's kind of interesting how, of course I,

Carnegie and Richie kind of standardized hello world

as the first thing

that you do in every computer programming language

and every computer.

But not having any interaction with the cultures of Unix

or any other standardized things,

it was just like, "Well, what am I gonna say?"

"I'm gonna say my name and then you learn how to do,

"Go to 10 and have it scroll all off the screen."

And that was definitely the first thing

that I wound up doing on a computer.

- Can I ask you programming advice?

I was always told in the beginning that you're not allowed

to use Go-to statements.

That's really bad programming.

Is this correct or not?

Jumping around code?

Can we look at the philosophy

and the technical aspects of the Go-to statement

that seems so convenient,

but it's supposedly bad programming?

- Well, so certainly back in the day

in basic programming languages,

you didn't have proper loops.

You didn't have four while and repeats,

that was the land of Pascal for people that kind

of generally had access to it back then.

So, you had no choice but to use Go-tos.

And as you made, what were big programs back then,

which were a thousand line basic programs,

is a really big program,

they did tend to sort of degenerate into madness.

You didn't have good editors or code exploration tools,

so you would wind up fixing things in one place,

add a little patch.

And there's reasons why structured programming,

generally helps understanding, but go-tos aren't poisonous.

Sometimes they're the right thing to do.

Usually it's because

there's a language feature missing, like nested breaks

or something where,

it can sometimes be better to do a go-to cleanup

or go-to error rather than having multiple flags,

multiple if statements littered throughout things.

But it is rare.

I mean, if you grip through all of my code right now,

I don't think any of my current code bases,

would actually have a go-to,

but deep within sort of the technical underpinnings

of a major game engine,

you're gonna have some go-tos

in a couple places probably.

- Yeah, the infrastructure on top of,

like the closer you get to the machine code,

the more go-tos you're gonna see,

the more of these like hacks you're going to see,

because the set of features available to you

in low level programming languages is not, is limited.

So, print John Carmack,

when is the first time, if we could talk about love

that you fell in love with programming.

You said like this is really something special.

- It really was something

that was one of those love at first sight things

where just really from the time that I understood

what a computer was even, I mean,

I remember looking through old encyclopedias

at the black and white photos of the IBM mainframes

at the real tore tape decks.

And for people nowadays,

it can be a little hard to understand what the world

was like then from information gathering

where I would go to the libraries

and there would be a couple books on the shelf,

about computers and they would be very out of date,

even at that point, just not a lot of information,

but I would grab everything that I could find

and devour everything.

Whenever "Time" or "Newsweek"

had some article about computers,

I would like cut it out with scissors and put it somewhere.

It felt like this magical thing to me,

this idea that the computer would just do exactly

what you told it to.

I mean, and there's a little bit

of the Genie monkey's paw sort of issues there

where you'd better be really, really careful

with what you're telling it to do.

But it wasn't gonna backtalk you,

it wasn't gonna have a different point of view.

It was gonna carry out what you told it to do.

And if you had the right commands

you could make it do these pretty magical things.

- And so what kind of programs did you write at first?

So, beyond the print John Carmack.

- So, I can remember as going through the learning process

where you find at the start you're just learning how to do

the most basic possible things.

And I can remember stuff like a Superman Comic

that Radio Shack commissioned to have,

it's like Superman had lost some of his super brain

and kids had to use Radio Shack TRS 80 computers

to do calculations to help him kind of complete his heroics.

And I'd find little things like that

and then get a few basic books

to be able to kind of work my way up.

And again, it was so precious back then.

I had a couple books

that would teach me important things about it.

I had one book that I could start to learn

a little bit of assembly language from

and I'd have a few books on basic

and some things that I could get from the libraries.

But my goals in the early days

was almost always making games of various kinds.

I loved the arcade games and the early Atari 2,600 games

and being able to do some of those things myself

on the computers was very much what I aspired to.

And it was a whole journey where if you learn normal, basic,

you can't do any kind of an action game.

You can write an adventure game,

you can write things where you say, "What do you do here?"

"I get sort, attack, troll," that type of thing.

And that can be done in the context of basic,

but to do things that had moving graphics

that were only the most limited things

you could possibly do.

You could maybe do breakout or pong or that sort of thing

in low resolution graphics.

And in fact, one of my first sort of major technical hacks

that I was kind of fond of was on the Apple II computers.

They had a mode called low resolution graphics

where of course all graphics were low resolution back then,

but regular low resolution graphics.

It was a grid of 40 by 40 pixels normally,

but they could have 16 different colors.

And I wanted to make a game,

kind of like the arcade game Vanguard,

just a scrolling game.

And I wanted to just kind of have it scroll vertically up

and I could move a little ship around you.

You could manage to do that in basic,

but there's no way you could redraw the whole screen.

And I remember at the time,

just coming up with what felt like a brainstorm to me

where I knew enough about the way

the hardware was controlled,

where the text screen and the low resolution graphic screen

were basically the same thing.

And all those computers,

could scroll their text screen reasonably.

You could do a listing and it would scroll things up

and I figured out that I could kind of tweak,

just a couple things that I barely understood

to put it into a graphics mode and I could draw graphics

and then I could just do a line feed at the very bottom

of the screen and then the system would scroll it all up,

using an assembly language routine

that I didn't know how to write back then.

So, that was like this first great hack

that sort of had analogs later on in my career

for a lot of different things.

So, I found out that I could draw a screen,

I could do a line feed at the bottom,

we would scroll it up once,

I could draw a couple more lines of stuff at the bottom.

And that was my first way to kind of scroll the screen,

which was interesting

in that that played a big part later on

in the id Software days as well.

- So, do efficient drawing

where you don't have to draw the whole screen,

but you draw from the bottom using the thing

that was designed in the hardware for text output.

- Yeah.

Where so much of,

until recently game design was limited

by what you could actually get the computer to do,

where it's easy to say like,

"Okay, I wanna scroll the screen."

You just redraw the entire screen at a slight offset.

And nowadays that works just fine.

Computers are ludicrously fast.

But up until a decade ago or so,

there were all these things everybody wanted to do,

but if they knew enough programming

to be able to make it happen,

it would happen too slow to be a good experience,

either just ridiculously slow or just slow enough

that it wasn't fun to experience it like that.

So, so much of kinda the first couple decades

of the programming work that I did

was largely figuring out how to do something

that everybody knows how they want it to to happen.

It just has to happen two to 10 times faster

than sort of the straightforward way

of doing things would make it happen.

And it's different now because at this point,

lots of things you can just do

in the most naive possible way and it still works out.

You don't have nearly the creative limitations

or the incentives for optimizing on that level.

And there's a lot of pros and cons to that.

But I do generally,

I'm not gonna do the angry old man,

shaking my fist at the clouds bit

where back in my day programmers had to do real programming.

It's amazing that you can just kind of pick an idea

and go do it right now.

And you don't have to be some assembly language wizard

or deep GPU arcane

to be able to figure out how to make your wishes happen.

- Well there's still,

see that's true,

but let me put on my old man with a fist hat

and say that probably the thing

that will define the future,

still requires you to operate

at the limits of the current system.

So, we'll probably talk about this,

but if you talk about building the metaverse

and building a VR experience that's compelling,

it probably requires you to not to go to assembly

or maybe not literally,

but sort of spiritually to go to the limits

of what the system is capable of.

- And that really was why virtual reality

was specifically interesting to me

where it had all the ties to,

you could say that even back in the early days,

I have some old magazine articles

that's talking about doom as a virtual reality experience,

back when just seeing anything in 3D.

So, you could say that we've been trying

to build those virtual experiences from the very beginning.

And in the modern era, virtual reality,

especially on the mobile side of things,

when it's standalone

and you're basically using a cell phone chip

to be able to produce these very immersive experiences,

it does require work.

It's not at the level

of what an old school console game programmer,

would have operated at

where you're looking at hardware registers

and you're scheduling all the DMA accesses,

but it is still definitely a different level

than what a web developer

or even a PC steam game developer usually has to work at.

And again, it's great.

There's opportunities for people

that wanna operate at either end of that spectrum there

and still provide a lot of value to the world.

- Let me ask you sort of a big question about preference.

What would you say is the best programming language,

your favorite,

but also the best,

you've seen throughout your career?

You're considered by many

to be the greatest programmer ever.

I mean, it's so difficult to place that label on anyone,

but if you put it on anyone, it's you.

So, let me ask you these kind of ridiculous questions

of what's the best band of all time,

but in your case, what's the best programming language?

- Everything has all the caveats about it,

but so what I use,

so nowadays I do program a reasonable amount of Python

for AI ML sorts of work.

I'm not a native Python programmer.

It's something I came to very late in my career.

I understand what it's good for.

- But you don't dream in Python.

- I do not.

And it has some of those things

where there's some amazing stats

when you say if you just start,

if you make a loop, a triply nested loop

and start doing operations in Python,

you can be thousands to potentially a million times slower

than a proper GPU tensor operation.

And these are staggering numbers,

you can be as much slower

as we've almost gotten faster in our pace of progress

and all this other miraculous stuff.

- So, your intuition's about inefficiencies

within the Python sort of-

- It keeps hitting me upside the face.

Where it's gotten to the point now I understand.

It's like, okay, you just can't do a loop

if you care about performance in Python.

You have to figure out how you can reformat this

into some big vector operation

or something that's going to be done completely,

within a C plus plus library.

But the other hand is it's amazingly convenient

and you just see stuff

that people are able to cobble together

by you just import a few different things

and you can do stuff that nobody on earth,

could do 10 years ago

and you can do it in a little cookbook thing

that you copy paste it out of a website.

So, that is really great.

When I'm sitting down to do

what I consider kind of serious programming.

It's still in C plus plus

and it's really kind of a C flavored C plus plus at that

where I'm not big

into the modern template meta programming sorts of things.

I see a lot of train wrecks coming from,

some of that over abstraction.

I spent a few years really going kind of deep

into the kinda the historical lisp work

and the Haskell

and some of the functional programming sides of things.

And there is a lot of value there

in the way you think about things.

And I changed a lot of the way I write

my C and C plus plus code based on what I learned about

the value that comes out of not having

this random mutable state that you kind of lose track of.

Because something that many people don't really appreciate,

till they've been at it for a long time

is that it's not the writing of the program initially,

it's the whole lifespan of the program and that's when,

# Chapter 2

It's still in C plus plus

and it's really kind of a C flavored C plus plus at that

where I'm not big

into the modern template meta programming sorts of things.

I see a lot of train wrecks coming from,

some of that over abstraction.

I spent a few years really going kind of deep

into the kinda the historical lisp work

and the Haskell

and some of the functional programming sides of things.

And there is a lot of value there

in the way you think about things.

And I changed a lot of the way I write

my C and C plus plus code based on what I learned about

the value that comes out of not having

this random mutable state that you kind of lose track of.

Because something that many people don't really appreciate,

till they've been at it for a long time

is that it's not the writing of the program initially,

it's the whole lifespan of the program and that's when,

it's not necessarily just how fast you wrote it

or how fast it operates,

but it's how can it bend and adapt as situations change.

And then the thing that I've really been learning

in my time at Meta with the Oculus and VR work is

it's also how well it hands off,

between a continuous kind of revolving door

of programmers taking over maintenance and different things

and how you get people up to speed in different areas

and there's all these other different aspects of it.

- Is C plus plus a good language

for handover between engineers?

- Probably not the best.

And there's some really interesting aspects to this

where in some cases languages

that are not generally thought well of for many reasons.

Like C is derided pretty broadly that yes,

obviously all of these security flaws

that happen with the memory and unsafeness

and buffer overruns and the things that you've got there.

But there is this underappreciated aspect to the language

is so simple.

Anyone can go and if you know C,

you can generally jump in someplace

and not have to learn what paradigms

they're using because there just aren't that many available.

I think there's,

and there's some really, really well-written C code,

like I find it great that if I'm messing around

with something in open BSD say,

I mean I can be walking around in the kernel and I'm like,

I understand everything that's going on here.

It's not hard for me to figure out what I need to do

to make whatever change that I need to,

while you can have more significant languages.

Like, it's a downside of lisp

where I don't regret the time that I spent with Lisp.

I think that it did help my thinking about programming

in some ways.

- Yes.

- But the people that are the biggest defenders

of Lisp are saying how malleable of a language it is

that if you write a huge Lisp program,

you've basically invented your own kind of language

and structure because it's not the primitives

of the language you're using very much.

It's all of the things you've built on top of that.

And then a language like Racket,

kind of one of the more modern Lisp versions,

it's essentially touted as a language

for building other languages.

And I understand the value of that

for a tiny little project,

but the idea of that for one of these long-term supported

by lots of people kind of horrifies me,

where all of those abstractions that you're like,

"Okay, you can't touch this code,

"till you educate yourself on all of these things

"that we've built on top of that."

And it was interesting to see how when Google made Go,

a lot of the criticisms of that are,

it's like, "Wow, this is not a state-of-the-art language.

"This language is just so simple and almost crude."

And you could see the programming language people,

just looking down at it,

but it does seem to be quite popular

as basically saying this is the good things about C.

Everybody can just jump right in and use it.

You don't need to restructure your brain

to write good code in it.

So, I wish that I had more opportunity

for doing some work in Go.

Rust is the other modern language that everybody talks about

that I'm not fit past judgment on.

I've done, a little bit beyond Hello World,

I wrote some like video decompression work in Rust,

just as an exercise, but that was a few years ago

and I haven't really used it since.

The best programming language is the one that works,

generally that you're currently using,

because that's another trap is

in almost every case I've seen

when people mixed languages on a project, that's a mistake.

I would rather stay just in one language,

so that everybody can work across the entire thing.

And we have, like at Meta, we have a lot of projects

that use kind of React framework.

So, you've got JavaScript here

and then you have C plus plus for real work,

and then you may have Java interfacing

with some other part of the Android system

and those are all kind of horrible things.

And that was one thing that,

I remember talking with with Boz at Facebook about it

where like, man, I wish we could have just said

we're only hiring C plus plus programmers.

And he just thought from the Facebook Meta perspective,

well we just wouldn't be able to find enough,

with the thousands of programmers they've got there.

It is not necessarily a dying breed,

but you can sure find a lot more JavaScript programmers

and I kind of mentioned that to Elon one time

and he was kind of flabbergasted about that.

It's like, well you just,

you go out and you find those programmers

and you don't hire the other programmers

that don't do the languages that you want to use.

But right now, I guess, yeah,

they're using JavaScript on a bunch of the,

the SpaceX work for the UI side of things.

When you go find UI programmers,

they're JavaScript programmers.

- I wonder if that's because

there's a lot of JavaScript programmers

because I do think that great programmers are rare,

that if you just look at statistics of how many people

are using different programming languages,

that doesn't tell you the story

of what the great programmers are using.

And so you have to really look at what you were speaking to,

which is the fundamentals of a language.

What does it encourage you?

How does it encourage you to think,

what kind of systems does it encourage you to build?

There is something about C plus plus

that has elements of creativity

but forces you to be an adult about your programming.

- [John] Is that it expects you to be an adult.

It does not forced you to.

- And so it brings out people

that are willing to be creative

in terms of building large systems

and coming up with interesting solutions,

but at the same time,

have the sort of the good software engineering practices

that amend themselves to real world systems.

Let me ask you about this other language, JavaScript.

So, if aliens visit in thousands of years

and humans are long gone,

something tells me that most of the systems

they find will be running JavaScript.

I kind of think that if we're living this simulation,

it's written in JavaScript.

For the longest time,

even still JavaScript didn't get any respect

and yet it runs so much of the world

and an increasing number of the world.

Is it possible that all everything will be written

in JavaScript one day?

- So, the engineering under JavaScript

is really pretty phenomenal.

The systems that make JavaScript run as fast

as it does right now

are kind of miracles of modern engineering in many ways.

It does feel like it is not an optimal language

for all the things that it's being used for

or an optimal distribution system to build huge apps

in something like this without type systems and so on.

But I think for a lot of people

it does reasonably the necessary things.

It's still a C flavored language,

it's still a braces and semicolon language.

It's not hard for people to be trained in JavaScript

and then understand the roots of where it came from.

I think garbage collection is unequivocally a good thing

for most programs to be written in.

It's funny that I still just this morning I was on,

I was seeing a Twitter thread of a bunch

of really senior game dev people arguing about

the virtues and costs of garbage collection.

And you will run into some people

that are top-notch programmers that just say,

"No, this is literally not a good thing."

- Oh, because it makes you lazy?

- Yes, that it makes you not think about things.

And I do disagree.

I think that there is so much objective data

on the vulnerabilities that have happened

in C and C plus plus programs,

sometimes written by the best programmers in the world.

It's like nobody is good enough

to avoid ever shooting themselves in the foot with that.

You write enough C code,

you're going to shoot yourself in the foot

and garbage collection is a very great thing

for the vast majority of programs.

It's only when you get into the tightest of real time things

that you start saying, it's like,

"No, the garbage collection has more costs

"than it has benefits for me there."

But that's not 99 plus percent of all the software

in the world.

So, JavaScript is not terrible in those ways

and so much of programming is not the language itself,

it's the infrastructure around,

that surrounds it.

All the libraries that you can get

and the different stuff that you can,

ways you can deploy it,

the portability that it gives you.

And JavaScript is really strong on a lot of those things

where for a long time and it still does if I look at it,

but the web stack about everything that has to go

when you do something really trivial in JavaScript

and it shows up on a web browser

to kind of X-ray through that and see everything

that has to happen for your one little JavaScript statement

to turn into something visible in your web browser.

It's very, very disquieting,

just the depth of that stack

and the fact that so few people can even comprehend,

all of the levels that are going on there.

But it's, again, I have to caution myself to not be the,

in the good old days old man about it,

because clearly there's enormous value here.

The world does run on JavaScript

to a pretty good approximation there

and it's not falling apart.

There's a bunch of scary stuff

where you look at console logs

and you just see all of these bad things that are happening,

but it's still kind of limping along

and nobody really notices.

But so much of my systems design

and systems analysis goes around,

you should understand what the speed of light is,

like what would be the best you could possibly do here?

And it sounds horrible,

but in a lot of cases you can be a thousand times off

your speed of light velocity for something

and it still be okay.

And in fact it can even sometimes still be

the optimal thing in a larger system standpoint

where there's a lot of things

that you don't wanna have to parachute in someone like me

to go in and say,

make this webpage run a thousand times faster.

Make this web app into a hardcore native application

that starts up in 37 milliseconds

and everything responds in less than one frame latency.

That's just not necessary.

And if somebody wants to go pay me millions of dollars

to do software like that,

when they can take somebody right out of a bootcamp and say,

"Spin up an application for this,"

often being efficient is not really the best metric.

And that applies in a lot of areas

where it's kind of interesting how a lot of our appliances

and everything are all built around energy efficiency,

sometimes at the expense of robustness

in some other ways or higher costs in other ways

where there's interesting things where energy

or electricity could become much cheaper in a future world

and that could change our engineering trade-offs

for the way we build certain things

where you could throw away efficiency

and actually get more benefits that actually matter.

I mean that's one of the directions

I was considering swerving into was nuclear energy

when I was kind of like, what do I want to do next?

It was either gonna be cost effective nuclear fission

or artificial general intelligence.

And one of my pet ideas there is like,

people don't understand how cheap nuclear fuel is

and there would be ways that you could be a quarter

the efficiency or less,

but if it wound up making your plant 10 times cheaper,

that could be a radical innovation in something like that.

So, there's like some of these thoughts around,

like direct fission energy conversion,

fission fragment conversion that maybe you build something

that doesn't require all the steam turbines and everything,

even if it winds up being less efficient.

So, that applies a lot in programming where there's always,

it's always good to know what you could do

if you really sat down and took it far,

because sometimes there's discontinuities,

like around user reaction times,

there are some points where the difference between operating

in one second and 750 milliseconds, not that huge.

You'll see it in webpage statistics,

but most of the usability stuff not that great.

But if you get down to 50 milliseconds,

then all of a sudden this just feels amazing.

It's just like doing your bidding instantly,

rather than you're giving it a command,

twiddling your thumbs, waiting for it to respond.

So, sometimes it's important to really crunch hard

to get over some threshold,

but there are broad basins in the value metric

for lots of work

where it just doesn't pay to even go that extra mile.

And there are craftsmen that,

they just don't wanna buy that

and more power to them,

if somebody just wants to say, no, I'm going to be,

my pride is in my work,

I'm never going to do something

that's not as good as I could possibly make it.

I respect that and sometimes I am that person,

but I try to focus more on the larger value picture

and you do pick your battles

and you deploy your resources in the play

that's going to give you sort of the best user value

in the end.

- Well if you look at the evolution of life on earth

as a kind of programming effort,

it seems like efficiency

isn't the thing that's being optimized for,

like natural selection is very inefficient,

but it kind of adapts

and through the process of adaptations,

building more and more complex systems

that are more and more intelligent,

the final result is kind of pretty interesting.

And so I think of JavaScript the same way.

It's like this giant mess that,

things naturally die off if they don't work

and if they're become useful to people,

they kind of naturally live.

And then you build this community,

large community of people that are jittering code

and some code is sticky, some is not,

and nobody knows the inefficiencies

or the efficiencies or the breaking points,

like how reliable this code is

and you kind of just run it, assume it works,

and then get unpleasantly surprised

and then that's very kind of the evolutionary process.

- So, that's a really good analogy

and we can go a lot of places with that

where in the earliest days of programming,

when you had finite,

you could count the bites that you had to work on this.

You had all the kind of hackers playing code golf

to be one less instruction

than the other person's multiply routine

to kind of get through.

And it was so perfectly crafted,

it was a crystal piece of artwork when you had a program,

because there just were not that many.

You couldn't afford to be lazy in different ways.

And in many ways I see that as akin to the symbolic AI work

where again, if you did not have the resources to just say,

"Well we're gonna do billions and billions

"of programmable weights here,"

you have to turn it down into something that is symbolic

and crafted like that.

But that's definitely not the way DNA and life

and biological evolution and things work.

On the one hand it's almost humbling

how little programming code is in our bodies.

We've got a couple billion base pairs

# Chapter 3

you could count the bites that you had to work on this.

You had all the kind of hackers playing code golf

to be one less instruction

than the other person's multiply routine

to kind of get through.

And it was so perfectly crafted,

it was a crystal piece of artwork when you had a program,

because there just were not that many.

You couldn't afford to be lazy in different ways.

And in many ways I see that as akin to the symbolic AI work

where again, if you did not have the resources to just say,

"Well we're gonna do billions and billions

"of programmable weights here,"

you have to turn it down into something that is symbolic

and crafted like that.

But that's definitely not the way DNA and life

and biological evolution and things work.

On the one hand it's almost humbling

how little programming code is in our bodies.

We've got a couple billion base pairs

and it's like this all fits on a thumb drive for years now.

And then our brains are even a smaller section of that.

You've got maybe 50 megabytes

and this is not like Shannon limit,

perfectly information dense conveyances here.

It's like these are messy codes,

they're broken up into amino acids.

A lot of them don't do important things

or they do things in very awkward ways.

But it is this process of just accumulation

on top of things.

And you need scale,

both you need scale for sort of the population

for that to work out.

And in the early days in the 50s and 60s,

the kind of ancient era of computers

where you could count when they say like,

when the internet started,

even in the seventies there were like 18 hosts

or something on it.

It was this small finite number

and you were still optimizing everything

to be as good as you possibly could be.

But now it's billions and billions of devices

and everything going on

and you can have this very much natural evolution going on

where lots of things are tried,

lots of things are blowing up.

Venture capitalists lose their money

when a startup invested in the wrong tech stack

and things completely failed or failed to scale.

But good things do come out of it.

And it's interesting to see the mimetic evolution

of the way different things happen.

Like mentioning Hello World at the beginning,

it's funny how some little thing like that where everybody,

every programmer knows Hello World now.

And that was a completely arbitrary sort of decision

that just came out of the dominance of Unix and C

and early examples of things like that.

So, millions of experiments are going on all the time,

but some things do kind of rise to the top

and win the fitness war for whether it's mind space

or programming techniques or anything.

- Like, there's a site on stack exchange called Code Golf

where people compete to write the shortest possible program

for a particular task

in all the different kinds of languages.

And it's really interesting to see folks kind of,

that are masters of their craft really play

with the limits of programming languages.

It's really beautiful to see

and across all the different programming languages,

you get to see some of these weird programming languages

and mainstream ones,

difference between Python two and three.

You get to see the difference between C and C plus plus

and Java and you get to see JavaScript, all of that.

And it's kind of inspiring to see how much depth

of possibility there is within programming languages

that code golfed kind of tasks reveal.

Most of us, if you do any kind of programming,

you kind of do boring kind of very vanilla type of code.

That's the way to build large systems.

But it's nice to see that the possibility of creative genius

is still within those languages,

it's laden with in those languages.

So, given that you are once again

one of the greatest programmers ever,

what do you think makes a good programmer,

maybe a good modern programmer?

- So, I just gave a long rant/lecture at Meta

to the TPM organization

and my biggest point was,

everything that we're doing really should flow

from user value.

You know, all the good things that we're doing.

It's like we're not technical people.

It's like you shouldn't be taking pride,

just in the specific thing.

Like code golf is the sort of thing,

it's a fun puzzle game,

but that really should not be a major motivator for you.

It's like we're solving problems for people

or we're providing entertainment to people.

We're doing something of value to people

that's displacing something else in their life.

So, we want to be providing a net value over

what they could be doing,

but instead they're choosing to use our products.

And that's where,

I mean, it sounds trite or corny,

but I fundamentally do think

that's how you make the world a better place.

If you have given more value to people than it took you

and your team to create,

then the world's a better place.

People have,

they've gone from something of lesser value,

chosen to use your product

and their life feels better for that.

And if you've produced that economically,

that's a really good thing.

On the other hand,

if you spent ridiculous amounts of money,

you've just kind of shoveled a lot of cash

into a wood chipper there

and you should maybe not feel so good,

about what you're doing.

So, being proud about like a specific architecture

or a specific technology

or a specific code sequence that you've done,

it's great to get a little smile,

like a tiny little dopamine hit for that.

But the top level metrics should be

that you're building things of value.

Now you can get into the argument about what is user value,

how do you actually quantify that?

And there can be big arguments about that,

but it's easy to be able to say,

"Okay, this off user there is not getting value

"from what you're doing.

"This user over there with a big smile on their face.

"I am the moment of delight when something happened.

"There's a value that's happened there."

I mean if you have to at least accept

that there is a concept of user value.

Even if you have trouble exactly quantifying it,

you can usually make relative arguments about it,

well this was better than this, we've improved things.

So, being a servant to the user is your job

when you're a developer.

You want to be producing something that

you know other people are gonna find valuable.

And if you are technically inclined,

then finding the right levers to be able to pull

to be able to make a design

that's going to produce the most value

for the least amount of effort.

And it always has to be kind of divide.

There's a ratio there where you,

it's a problem at the big tech companies,

whether it's Meta, Google, Apple, Microsoft, Amazon,

companies that have almost infinite money.

I mean, I know their CFO will complain

that it's not infinite money,

but from most developer standpoints

it really does feel like it.

And it's almost counterintuitive

that if you're working hard as a developer on something,

there's always this thought,

if only I had more resources,

more people, more RAM, more megahertz,

then my product will be better.

And that sense that at certain points,

it's certainly true that

if you are really hamstrung by this,

removing an obstacle will make a better product,

make more value.

But if you're not making your core design decisions

in this fiercely competitive way

where you're saying feature A or feature B,

you can't just say let's do both.

Because then you're not making a value judgment about them.

You're just saying,

"Well they both seem good.

"I don't wanna necessarily have

"to pick out which one is better or how much better

"and tell team B that, sorry, we're not gonna do this,

"because A is more important."

But that notion of always having to really critically value

what you're doing,

the resources you expend,

even the opportunity cost of doing something else,

that's super important.

- Well let me ask you about this,

the debates that you're mentioning of how to measure value.

Is it possible to measure it kind of numerically

or can you do the sort of Johnny,

the design route of imagining sort of somebody using a thing

and imagining a smile on their face,

imagining the experience of love and joy

that you have when you use the thing,

that's from a design perspective

or if you're building more like a lower level thing

for like Linux,

you imagine a developer that might come across this

and use it and become happy and better off because of it.

So, where do you land on those things?

Is it measurable?

So, I imagine like Meta and Google,

will probably try to measure the thing,

they'll try to,

it's like you try to optimize engagement or something,

let's measure engagement.

And then I think there is a kind of,

I mean, I admire the designer ethic of like,

think of a future that's immeasurable

and you try to make somebody in that future

that's different from today happy.

- So, I do usually favor

if you can get any kind of a metric that's good,

by all means listen to the data.

But you can go too far there

where we've had problems where it's like,

"Hey, we had a performance regression,

"because our fancy new telemetry system

"is doing a bazillion file rights

"to kind of archive this stuff,

"because we needed to collect information

"to determine if our plans were good."

So, when information is available,

you should never ignore it.

- From actual users using the thing,

human beings using the thing,

large number of human beings

and you get to see sort of at all large.

- So, there's zero to one problem

of when you're doing something really new,

you do kind of have to make a guess.

But one of the points that I've been making at Meta is

we have more than enough users now

that anything somebody wants to try in VR,

we have users that will be interested in that.

You do not get to make

a completely greenfield blue sky pitch and say,

I'm going to do this,

because I think it might be interesting.

I challenge everyone.

There are going to be people,

whether it's working in VR on your,

like on your desktop replacement

or communicating with people in different ways

or playing the games.

There are going to be probably millions of people

or at least if you pick some tiny niche

that we're not in right now,

there's still gonna be thousands of people out there

that have the headsets that would be your target market.

And I tell people, pay attention to them.

Don't invent fictional users,

don't make an Alice, Bob, Charlie

that fits whatever matrix of tendencies

that you want to break the market down to,

because it's a mistake to think about imaginary users

when you've got real users that you could be working with.

But on the other hand there is,

there is value to having a kind of wholeness of vision

for a product.

And companies like Meta have,

they understand the trade-offs

where you can have a company like SpaceX

or Apple in the Steve Jobs era

where you have a very powerful leading personality

that can micromanage at a very low level

and can say it's like, no, that handle needs to be different

or that icon needs to change the tint there.

And they clearly get a lot of value out of it.

They also burn through a lot of employees

that have horror stories

to tell about working there afterwards.

My position is that you are at your best

when you've got a leader that is at their limit

of what they can kind of comprehend

of everything below them

and they can have an informed opinion,

about everything that's going on.

And you take somebody,

you've gotta believe that somebody that has 30, 40 years

of experience,

you would hope that they've got wisdom

that the the just out of bootcamp person,

contributing doesn't have.

And that if they're like, well that's wrong there,

you probably shouldn't do it that way

or even just don't do it that way, do it another way.

So, there's value there,

but it can't go beyond a certain level.

I mean I have Steve Jobs stories of him saying,

things that are just wrong right in front of me,

about technical things,

because he was not operating at that level.

But when it does work

and you do get that kind of passionate leader

that's thinking about the entire product

and just really deeply cares,

about not letting anything slip through the cracks,

I think that's got a lot of value.

But the other side of that is the people saying that,

"Well, we wanna have these independent teams

"that are bubbling up the ideas because"

and like it's almost, it's anti-capitalist

or anti-free market to say it's like I want my grand,

my great leader to go ahead

and dictate all these points there

where clearly free markets bring up things that,

you don't expect.

Like in VR we saw a bunch of things,

like it didn't turn out at all

the way the early people thought

were gonna be the key applications

and things that would not have been approved by

the dark cabal making the decisions about

what gets into the store turn out to,

in some cases be extremely successful.

So yeah, I definitely kind of wanted

to be there as a point where I did make a pitch.

It's like, "Hey, make me VR dictator

"and I'll go and get shit done."

And it's not in the culture at Meta,

they understand the trade offs.

And that's just not the way,

that's not the company that they want,

the team that they want to do.

- Yeah, it's fascinating 'cause VR

and we'll talk about it more.

It's still unclear to me

in what way VR will change the world,

because it does seem clear

that VR will somehow fundamentally transform this world.

And it's unclear to me how.

- [John] Yeah, let me know when you wanna get into that.

- We will, well hold on a second.

So, stick to the, you being the best programmer ever,

okay, in the early days

when you didn't have adult responsibilities of leading teams

and all that kind of stuff

and you can focus on just being a programmer,

what did the productive day

in the life of John Carmack look like?

How many hours of the keyboard, how much sleep?

What was the source of calories that fueled the brain?

What was it like, what time did you wake up?

- So, I was able to be remarkably consistent about

what was good working conditions for me

for a very long time.

I was never one of the programmers that I,

that would do all-nighters,

going through work for 20 hours straight.

It's like my brain generally starts turning

to mush after 12 hours or so,

but the hard work is really important

and I would work for decades.

I would work 60 hours a week.

I would work a 10 hour day,

six days a week and try to be productive at that.

Now, my schedule shifted around a fair amount

when I was young without any kids,

I am any other responsibilities,

I was on one of those cycling schedules

where I'd kind of get in an hour later each day

and roll around through the entire time

and I'd wind up kind of pulling in at two or three

in the afternoon sometimes

and then working again past midnight or two in the morning.

And that was

when it was just me trying to make things happen

and I was usually isolated off in my office.

People generally didn't bother me much at it

and I could get a lot of programming work done that way.

I did settle into a more normal schedule

when I was taking kids to school and things like that.

- So, kids were the forcing function that got you to wake up

and at the same time these-

- And it's not clear to me that

there was a much of a difference in the productivity

with that where I kind of feel if I just get up

when I feel like it,

it's usually a little later each day.

But I just recently made the focusing decision

to try to push my schedule back a little bit earlier

to getting up at eight in the morning

# Chapter 4

and I'd wind up kind of pulling in at two or three

in the afternoon sometimes

and then working again past midnight or two in the morning.

And that was

when it was just me trying to make things happen

and I was usually isolated off in my office.

People generally didn't bother me much at it

and I could get a lot of programming work done that way.

I did settle into a more normal schedule

when I was taking kids to school and things like that.

- So, kids were the forcing function that got you to wake up

and at the same time these-

- And it's not clear to me that

there was a much of a difference in the productivity

with that where I kind of feel if I just get up

when I feel like it,

it's usually a little later each day.

But I just recently made the focusing decision

to try to push my schedule back a little bit earlier

to getting up at eight in the morning

and trying to shift things around.

Like I'm often doing experiments with myself about

what should I be doing to be more productive.

And one of the things that I did realize

was happening in recent months

where I would go for a walk or a run.

I cover like four miles a day and I would usually do that,

just as the sun's going down at here in Texas now

and it's still really damn hot.

But I'd go out at 8:30 or something

and cover the time there and then the showering

and it was putting a hole in my day

where I would have still a couple hours after that

and sometimes my best hours were at night

when nobody else is around, nobody's bothering me.

But that hole in the day was a problem.

So, just a couple weeks ago I made the change

to go ahead and say,

"All right, I'm gonna get up a little earlier,

"I'm gonna do a walk or get out there first

"so I can have more uninterrupted time."

So, I'm still playing with factors like this

as I kind of optimize my work efforts.

But it's always been,

it was 60 hours a week for a very long time.

To some degree I had a little thing in the back of my head

where I was almost jealous of some of the programmers

that would do these marathon sessions

and I had like Dave Taylor, one of the guys that he had,

he would be one of those people

that would fall asleep under his desk sometimes

and all the kind of classic hacker tropes about things.

And a part of me was like always a little bothered

that that wasn't me.

That I wouldn't go program 20 hours straight,

because I'm falling apart

and not being very effective after 12 hours.

I mean, yeah, a 12 hour programming,

that's fine when you're doing that,

but you're not doing smart work much after,

at least I'm not, but there's a range of people.

I mean that's something that a lot of people,

don't really get in their gut

where there are people that work on four hours of sleep

and are smart and can continue to do good work,

but then there's a lot of people that just fall apart.

So, I do tell people

that I always try to get eight hours of sleep.

It's not this,

push yourself harder, get up earlier.

I just do worse work,

you can work a hundred hours a week

and still get eight hours of sleep

if you just kind of prioritize things correctly.

But I do believe in working hard, working a lot.

There was a comment that a game dev made that,

that I know there's a backlash against really hard work

in a lot of cases,

and I get into online arguments about this all the time.

But it was basically saying,

yeah, 40 hours a week, that's kind of a part-time job

and if are really in it,

you're doing what you think is important,

what you're passionate about,

working more gets more done.

And it's just really not possible

to argue with that if you've been around the people

that work with that level of intensity

and just say it's like, no, they should just stop.

And we had,

I kind of came back around to that a couple years ago

where I was using the fictional example of,

alright, some people say, they'll say with a straight face,

they think no, you are less productive

if you work more than 40 hours a week.

And they're generally misinterpreting things

where you're marginal productivity for an hour,

after eight hours is less than in one of your peak hours,

but you're not literally getting less done.

There is a point where you start breaking things

and getting worse behavior and everything out of it

where you're literally going backwards,

but it's not at eight or 10 or 12 hours.

And the fictional example I would use was,

imagine there's an asteroid coming to impact,

to crash into earth destroy all of human life.

Do you want Elon Musk or the people working at SpaceX

that are building the interceptor

that's going to deflect the asteroid?

Do you want them to clock out at five,

because damn it they're just gonna go do worse work

if they work another couple hours.

And it seems absurd

and that's a hypothetical though

and everyone can dismiss that.

But then when Coronavirus was hitting

and you have all of these medical personnel

that are clearly pushing themselves really, really hard.

And I'd say it's like,

okay, do you want all of these scientists,

working on treatments and vaccines

and caring for all of these people?

Are they really screwing everything up

by working more than eight hours a day?

And of course people say,

"I'm just an to say something like that,"

but it's the truth.

Working longer gets more done.

- So, that's kind of the layer one.

But I'd like to also say that

at least I believe depending on the person,

depending on the task,

working more and harder will make you better

for the next week in those peak hours.

So, there's something about a deep dedication to a thing

that kind of gets deep in you.

So, it's the hard work

isn't just about the raw hours of productivity.

It's the thing it does to you

in the weeks and months after too.

- You're tempering yourself in some ways.

- And I think, it's like the "Jiro Dreams of Sushi."

If you really dedicate yourself completely

to making the sushi like to really putting in

the long hours day after day after day,

you become a true craftsman of the thing you're doing.

Now there's of course discussions about

are you sacrificing a lot of personal relationships?

Are you sacrificing a lot

of other possible things you could do with that time?

But if you're talking about purely being a master

or a craftsman of your art,

that more hours isn't just about doing more,

it's about becoming better at the thing you're doing.

- Yeah and I don't gain say anybody that

wants to work the minimum amount,

they've got other priorities in their life.

My only argument that I'm making,

it's not that everybody should work hard,

it's that if you want to accomplish something,

working longer and harder

is the path to getting it accomplished.

- Well, let me ask you about this then.

The mythical work-life balance,

for an engineer,

it seems like that's one of the professions for programmer

where working hard does lead to greater productivity

and but it also raises the question of,

sort of personal relationships and all that kind of stuff,

family and how are you able to find work-life balance?

Is there advice you can give, maybe even outside yourself?

Have you been able to arrive at any wisdom

on this part in your years of life now?

- So, I do think that there's a wide range of people

where different people have different needs.

It's not a one size fits all.

I am certainly what works for me.

I can tell enough

that I'm different than a typical average person

in the way things impact me.

The things that I want to do,

my goals are different and sort of the levers

to impact things are different

where I have literally never felt burnout.

And I know there's lots of brilliant,

smart people that do world leading work that get burned out

and it's never hit me.

I've never been at a point where I'm like,

I just don't care about this.

I don't wanna do this anymore.

But I've always had the flexibility

to work on lots of interesting things.

I can always just turn my gaze to something else

and have a great time working on that.

And so much of that,

so much of the ability to actually work hard

is the ability to have multiple things to choose from

and to use your time on the most appropriate thing.

Like there are time periods where I am,

it's the best time for me to read a new research paper

that I need to really be thinking hard about it.

Then there's a time that maybe I should just scan

and organize my old notes

because I'm just not on top of things.

Then there's the time that,

alright, let's go,

bang out a few hundred lines of code for something.

So, switching between them has been,

real valuable.

- So, you always have kind of joy in your heart

for all the things you're doing

and that is a kind of work life balance

as a first sort of step.

So you're always happy?

- I do.

I mean it's like I,

a lot of people would say that,

often I look like kind of a grim person

with just sitting there with a neutral expression

or even like knitted brows

and a frown on my face as I'm staring at something.

- That's what happiness looks like for you.

- Yeah, it's kind of true where that it's like,

okay, I'm pushing this, I'm making progress here.

I know that doesn't work for everyone.

I know it doesn't work for most people.

But what I am always trying to do in those cases is,

I don't wanna let somebody that might be a person like that,

be told by someone else that,

"No, don't even try that out as an option,"

where work life-balance versus kind of your life's work

where there's a small subset of the people

that can be very happy being obsessive about things

and obsession can often get things done

that just practical, prudent pedestrian work won't

or at least won't for a very long time.

- There's legends of your nutritional intake

in the early days.

What can you say about sort of as a being a programmer,

as a kind of athlete?

So, what was the nutrition that fueled?

- So, I have never been that great

on really paying attention to it

where I'm good enough that I don't eat a lot,

I've never been like a big heavy guy.

But it was interesting where one of the things

that I can remember being an unhappy teenager,

not having enough money

and like, one of the things

that bothered me about not having enough money

is I couldn't buy pizza whenever I wanted to.

So I got rich and then I bought a whole lot of pizza.

- So, that was defining,

like that's what being rich felt like.

You could buy Pizza.

- There was a lot pizza of the little things.

Like I could buy all the pizza and comic books

and video games that I wanted to,

and it really didn't take that much.

But the pizza was one of those things

and it's absolutely true

that for a long time it did software.

I had a pizza delivered every single day.

The delivery guy knew my name,

and I didn't find out until years later

that apparently I was such a good customer

that they just never raised the price on me.

And I was using this 6-year-old price for the pizzas

that they were still kind of sending my way every day.

- So, you were doing eating once a day or were you-

- It would be spread out.

You have a few pieces of pizza, you have some more later on,

and I'd maybe have something at home.

It was one of the nice things that Facebook Meta is they do,

they feed you quite well.

You get a different,

I guess now it's DoorDash sorts of things delivered,

but they take care of making sure

that everybody does get well fed.

And I probably had better food those six years

that I was working in the Meta office there

than I used to before.

But it's worked out okay for me.

My health has always been good.

I get a pretty good amount of exercise

and I don't eat to excess and I avoid a lot of other,

kind of not so good for you things.

So, I'm still doing quite well at my age.

- Did you have a kind of,

I don't know, spiritual experience with food or coffee

or any of that kind of stuff?

I mean, the programming experience with music,

or like I listen to brown noise in a program

or like creating an environment

and the things you take into your body.

Just everything you construct can become a kind of ritual

that empowers the whole process of the program.

Did you have that relationship with pizza?

- It would really be with Diet Coke.

I mean, there still is that sense of drop the can down,

crack open the can of Diet Coke.

All right now, I mean business, we're getting to work here.

- But still to this day,

diet Coke is still part.

- Yeah, probably eight, eight or nine a day.

- Nice, okay.

What about your setup?

How many screens,

what kind of keyboard is there something interesting,

what kind of IDE, Emacs, Vim

or something modern.

Linux, what operating system laptop

or any interesting thing that brings you joy?

- So, I kind of migrated cultures

where early on through all of game dev

there was sort of one culture there,

which was really quite distinct

from the Silicon Valley venture culture for things.

They're different groups

and they have pretty different mos in the way they think

about things where,

and I still do think a lot of the big companies

can learn things

from the hardcore game development side of things

where it still boggles my mind

how hostile to debuggers and IDEs that so much of them,

the kind of big money get billions

of dollars Silicon Valley venture backed funds are.

- Oh, that's interesting.

Sorry, so you're saying like big companies

at Google and Meta are hostile to-

- They are not big on debuggers and IDEs.

Like so much of it is like Emacs, Vim for things

and we just assume that debuggers,

don't work most of the time for the systems.

And a lot of this comes from a sort of Linux bias

on a lot of things where I did come up,

through the personal computers and then the DOS,

and then Windows

and it was Borland tools and then Visual Studio.

- [Lex] Do you appreciate debuggers?

- Very much so.

I mean, a debugger is how you get a view into a system

that's too complicated to understand.

I mean, anybody that thinks just read the code

and think about it, that's an insane statement,

you can't even read all the code on a big system.

You have to do experiments on the system.

And doing that by adding log statements,

recompiling and rerunning it,

is an incredibly inefficient way of doing it.

I mean, yes, you can always get things done,

even if you're working with stone knives and bare skins.

That is the mark of a good programmer is that,

given any tools, you will figure out a way to get it done.

But it's amazing what you can do

with sometimes much, much better tools

where instead of just going through this iterative,

compile, run debug cycle,

you have the old Lips direction of like you've got a riple

and you're working interactively

and doing amazing things there,

but in many cases a debugger

as a very powerful user interface that can stop,

examine all the different things in your program,

set all of these different break points.

And of course you can do that with GDB or whatever there,

but this is one of the user interface fundamental principles

where when something is complicated to do,

you won't use it very often.

There's people that will break out GDB

when they're at their wits end

and they just have beat their head against a problem

for so long.

But for somebody that kind of grew up in game dev,

it's like they were running into the debugger anyways,

before they even knew there was a problem.

And you would just stop and see what was happening.

And sometimes you could fix things,

even before you know, even before you did one compile cycle,

you could be in the debugger and you could say,

well, I'm just going to change this right here and yep,

that did the job and fix it and go on.

- And for people don't know,

GDB is a sort of popular,

I guess Linux debugger primarily for C plus plus.

# Chapter 5

And of course you can do that with GDB or whatever there,

but this is one of the user interface fundamental principles

where when something is complicated to do,

you won't use it very often.

There's people that will break out GDB

when they're at their wits end

and they just have beat their head against a problem

for so long.

But for somebody that kind of grew up in game dev,

it's like they were running into the debugger anyways,

before they even knew there was a problem.

And you would just stop and see what was happening.

And sometimes you could fix things,

even before you know, even before you did one compile cycle,

you could be in the debugger and you could say,

well, I'm just going to change this right here and yep,

that did the job and fix it and go on.

- And for people don't know,

GDB is a sort of popular,

I guess Linux debugger primarily for C plus plus.

- They handle most of the languages.

Okay, but it's based on C

as the original kind of Unix heritage.

- And it's kind of like command line,

it's not user friendly.

It doesn't allow for clean visualizations

and you're exactly right.

So, you're using this kind of debugger,

usually when you're at what's end

and there's a problem that you can't figure out why

by just looking at the codes they have to find it.

That's how, I guess normal programmers use it.

But you're saying there should be tools

that kind of visualize

and help you as part of the programming process,

just a normal programming process

to understand the code deeper?

- Yeah, when I'm working on like my C, C plus plus code,

I'm always running it from the debugger,

just I type in the code, I run it many times.

The first thing I do after writing code

is set a break point and step through the function.

Now other people will say,

it's like, "Oh, I do that in my head."

Well, your head is a faulty interpreter

of all those things there

and I've written brand new code,

I wanna step in there

and I'm gonna single step through that,

examine lots of things and see if it's actually doing

what I expected it to.

- It it is a kind of companion, the debugger,

like you're now coding in an interactive way

with another being,

the debugger is a kind of dumb being,

but it's a reliable being.

That is an interesting question of what role does AI play

in that kind of with Codex

and these kind of ability to generate code might be,

you might start having tools that understand the code

in interesting deep ways that can work with you.

- Because there's a whole spectrum there

from static code analyzers

and various kind of dynamic tools there up to AI

that can conceivably grok these programs

that literally no human can understand.

There are two big too intertwined and too interconnected,

but it's not beyond the possibility of understanding.

It's just beyond what we can hold in our heads

as kind of mutable state while we're working on things.

And I'm a big proponent again

of things like static analyzers and some of that stuff

where you'll find some people

that don't like being scolded by a program

for how they've written something

where it's like, "Oh, I know better."

And sometimes you do.

But that was something that I was,

it was very, very valuable for me when

and not too many people get an opportunity like this

to have, this is almost one of those spiritual experiences

as a programmer and awakening to,

be it in software code bases

were a couple million lines of code.

And at one point I had used a few

of the different analysis tools,

but I made a point to really go through

and scrub the code base using every tool that I could find.

And it was eye-opening where we had a reputation

for having some of the, the most robust, strongest code,

where there were some great things

that I remember hearing

from like Microsoft telling us about crashes on Xbox

and we had this tiny number that they said

were probably literally hardware errors.

And then you have other significant titles

that just have millions of faults

that are getting recorded all the time.

So, I was proud of our code on a lot of levels,

but when I took this code analysis squeegee,

through everything,

it was shocking how many errors there were in there.

Things that you can say,

"Okay, this was a copy paste,

"not changing something right here."

Lots of things that were,

the most common problem was something

in a print F format string that was the wrong data type

that could cause crashes there

and you really want the warnings for things like that.

Then the next most common was missing a check for null

that could actually happen that could blow things up.

And those are obviously like top C, C plus plus things.

Everybody has those problems,

but the long tail of all of the different little things

that could go wrong there.

And we had good programmers and my own code,

it's not that I'd be looking at,

it's like, "Oh, I wrote that code, that's definitely wrong."

We've been using this for a year

and it's this submarine,

this mind sitting there waiting for us to step on.

And it was humbling.

And I reached the conclusion that anything

that can be syntactically allowed in your language,

if it's gonna show up eventually

in a large enough code base,

you're not gonna,

good intentions aren't going to keep it from happening.

You need automated tools and guardrails for things.

And those start with things like static types

and or even type hints in the more dynamic languages.

But the people that rebel against that basically say,

that slows me down doing that.

There's something to that I get that I've written,

I've cobbled things together in a notebook.

I'm like, "Wow, this is great that it just happened,"

but yeah, that's kind of sketchy, but it's working fine.

I don't care.

It does come back to that value analysis

where sometimes it's right to not care,

but when you do care,

if it's going to be something that's going to live for years

and it's gonna have other people working on it

and it's gonna be deployed to millions of people,

then you want to use all of these tools you want to be told.

It's like, no, you've screwed up here, here and here.

And that does require kind of an ego check about things

where you have to be open to the fact that everything

that you're doing is just littered with flaws.

It's not that, "Oh, you occasionally have a bad day,"

it's just whatever stream of code you output

there is going to be a statistical regularity of things

that you just make mistakes on.

And I do think there's the whole argument about,

test driven design and unit testing versus,

kind of analysis and different things.

I am more in favor of the analysis and the stuff

that just like,

you can't run your program until you fix this,

rather than you can run it

and hopefully a unit test will catch it in some way.

- Yeah, in my private code I have asserts everywhere.

- [John] Yeah.

- It just, there's something pleasant to me,

pleasurable to me,

about sort of the dictatorial rule of like,

this should be true at this point.

And too many times,

I've made mistakes that shouldn't have been made

and I would assume I wouldn't be the kind of person

that would make that mistake,

but I keep making that mistake.

Therefore, an assert really catches me,

really helps all the time.

So, I would say like 10 to 20% of my private code,

just for personal use is probably a service.

- And they're active comments.

It's one of those things that in theory

they don't make any difference to the program.

And if it was all operating

the way you expected it would be,

then they will never fire.

But even if you have it right

and you wrote the code right initially,

then circumstances change.

The world outside your program changes.

And in fact that's one of the things

where I'm kind of fond in a lot of cases

of static erase size declarations

where I went through this period where it's like,

okay, now we have general collection classes,

we should just make everything variable,

because I had this history of,

in the early days you get Doom,

which had some fixed limits on it,

then everybody started making crazier and crazier things

and they kept bumping up the different limits,

this many lines, this many sectors.

And it seemed like a good idea.

Well, we should just make this completely generic.

It can go kind of go up to whatever

and there's cases where that's the right thing to do.

But it also,

the other aspect of the world changing around you is

it's good to be informed when the world

has changed more than you thought it would.

And if you've got a continuously growing collection,

you're never gonna find out.

You might have this quadratic slowdown on something

where you thought,

"Oh, I'm only ever gonna have a handful of these,

"but something changes and there's a new design style

"and all of a sudden you've got 10,000 of them."

So, I kind like in many cases picking a number,

some nice round power of two number

and sending it up in there

and having an assert saying it's like,

"Hey, you hit this limit."

You should probably think about the choices

that you've made around all of this still relevant

if somebody's using 10 times more than

you thought they would?

- Yeah, this code was originally written

with this kind of worldview,

with this kind of set of constraints.

You were thinking of the world in this way.

If something breaks,

that means you gotta rethink the initial stuff.

And it's nice for it to for it to do that.

Is there any stuff like keyboard or monitors?

- I'm fairly pedestrian on a lot of that

where I did move to triple monitors,

like in the last several years ago.

I had been dual monitor for a very long time

and it was one of those things

where probably years later than I should have,

I'm just like,

well the video cards now generally have three output ports.

I should just put the third monitor up there.

That's been a pure win.

I've been very happy with that.

But no,

I don't have fancy keyboard or mouse

or anything really going on.

- The key things is an ID

that has helpful debuggers has helpful tools,

so it's not the Emacs, Vim route and then Diet Coke.

- Yeah, so I did spend,

I spent one of my week-long retreats where I'm like,

okay, I'm gonna make myself use,

it was actually classic VI,

which I know people will say

you should never have done that.

You should have just used Vim directly.

But I gave it the good try.

It's like, okay, I'm being in kind of,

classic Unix developer mode here

and I worked for a week on it.

I used end key to like teach myself

the different little key combinations for things like that.

And in the end it was just like,

alright,

this was kind of like my civil war reenactment phase,

it's like I'm going out there,

doing it like they used to in the old days.

And it was kind of fun in that regard.

- You're offending so many people right now,

they're screaming as they're listening to this.

- So again, the out is that this was not modern Vim,

but still yes, I was very happy to get back

to my visual studio at the end.

- Yeah, I'm actually, I struggle with this a lot,

because, so I use a Kinesis keyboard

and I use Emacs primarily,

and I feel like I can exactly as you said,

I can understand the code, I can navigate the code.

There's a lot of stuff you could build within Emacs

with using Lisp.

You can customize a lot of things for yourself

to help you introspect the code,

like to help you understand the code

and visualize different aspects of the code.

You can even run debuggers,

but it's work and the world moves past you

and the better and better ideas are constantly being built.

And that puts a kind of,

I need to take the same kind of retreat

as you're talking about,

but now I'm still fighting the Civil War.

I need to kind of move into the 21st century.

- And it does seem like the world is

or a large chunk of the world

is moving towards Visual Studio Code,

which is kind of interesting to me,

against the JavaScript ecosystem on the one hand

and IDEs are one of those things

that you want to be infinitely fast.

You want them to just kind of immediately respond.

And like, I mean, heck, I've got, there's someone I know,

I am an old school game dev guy

that still uses Visual Studio Six

and on a modern computer,

everything is just absolutely instant on something like that

because it was made to work on a computer

that's 10,000 or a hundred thousand times slower.

So, just everything happens immediately

and all the modern systems just feel,

they feel so crufty when it's like,

"Oh, why is this refreshing the screen and moving around

"and updating over here and something blinks down there

"and you should update this."

And there are things that we've lost

with that incredible flexibility,

but lots of people get tons of value from it.

And I am super happy that that seems

to be winning over even a lot of the old Vim

and Emacs people that they're kind of like,

"Hey, Visual Studio code is may be not so bad."

I am that may be the final peacekeeping solution

where everybody is reasonably happy

with something like that.

- So, can you explain what a dot plan file is

and what role that played in your life?

Does it still continue to play a role?

- Back in the early, early days of id Software,

one of our big things that was unique with what we did

is I had adopted next stations

or kind of next steps systems

from Steve Jobs's out in the woods way from Apple Company.

And they were basically, it was kind of interesting,

because I did not really have a background

with the Unix system.

So, many of the people,

they get immersed in that in college

and that sets a lot of cultural expectations for them.

And I didn't have any of that,

but I knew that my background was,

I was a huge Apple II fan, boy,

I was always a little suspicious of the Mac.

I was not really

what kind of I wanted to to go with.

But when Steve Jobs left Apple and started NeXT,

this computer did just seem like one

of those amazing things from the future

where it had all of this cool stuff in it.

And we were still back in those days,

working on DOS, everything blew up.

You had reset buttons,

because your computer would just freeze

if you're doing development work,

literally dozens of times a day.

Your computer was just rebooting constantly.

And so this idea of,

yes, any of the Unix workstations,

would've given a stable development platform

where you don't crash and reboot all the time.

But NeXT also had this really amazing graphical interface

and it was great for building tools

and it used objective C as the kind of an interesting.

- [Lex] Oh wow.

So, NeXT was Unix based, instead objective C.

So, it has a lot of the elements.

- That became Mac,

I mean the kind of reverse acquisition of Apple by NeXT,

where that took over

and became what the modern Mac system is.

- And defined some of the developer like the tools

and the whole community.

- Yeah, you've still got,

if you're programming on Apple stuff now,

there's still all these Ns somethings

which was originally next step objects

of different kinds of things.

But one of the aspects of those Unix systems

was they had this notion of a dot plan file where,

a dot file is an invisible file,

usually in your home directory or something.

And there was a trivial server,

running on most Unix systems at the time that,

that when somebody ran a trivial little command,

called finger,

you could a finger and then somebody's address,

it could be anywhere on the internet

if you were connected correctly,

then all that server would do was read the dot plan file

in that user's home directory

and then just spit it out to you.

And originally the idea was that could be,

whether you're on vacation, what your current project was,

it's supposed to be like the plan of what you're doing

and people would use it for, various purposes.

But all it did was dump that file,

over to the terminal of whoever issued the finger command.

And at one point I started just keeping a list of

what I was doing in there,

which would be what I was working on in the day.

And I would have this little syntax,

I kind of got to myself about,

here's something that I'm working on,

I put a star when I finish it,

I could have a few other little bits of punctuation.

And at the time it was,

it started off as being just like my to-do list

# Chapter 6

if you were connected correctly,

then all that server would do was read the dot plan file

in that user's home directory

and then just spit it out to you.

And originally the idea was that could be,

whether you're on vacation, what your current project was,

it's supposed to be like the plan of what you're doing

and people would use it for, various purposes.

But all it did was dump that file,

over to the terminal of whoever issued the finger command.

And at one point I started just keeping a list of

what I was doing in there,

which would be what I was working on in the day.

And I would have this little syntax,

I kind of got to myself about,

here's something that I'm working on,

I put a star when I finish it,

I could have a few other little bits of punctuation.

And at the time it was,

it started off as being just like my to-do list

and it would be these trivial obscure little things,

like I fixed something with collision detection code,

made Fireball do something different

and just little one-liners that people

that were following the games could kind of decipher.

But I did wind up starting

to write much more in depth things.

I would have little notes of thoughts and insights

and then I would eventually start having little essays.

I would sometimes dump into the dot plan files,

interspersed with the work logs of things that I was doing.

So, in some ways it was like a super early proto blog

where I was just kind of dumping out what I was working on.

But it was interesting enough

that there were a lot of people

that were interested in this.

So, most of the people didn't have Unix workstations.

So, there were the websites back in the day

that would follow the Doom and Quake development

that would basically make a little service

that would go grab all the changes

and then people could just get it with a web browser.

And there was a period

where like all of the little kind of Dallas gaming diaspora

of people that were at all in that orbit,

there were a couple dozen plan files going on,

which was, and this was some years,

before blogging really became kind of a thing.

And it was kind of a premonition

of sort of the way things would go.

And there was,

it's all been collected,

it's available online in different places

and it's kind of fun to go back

and look through what I was thinking,

what I was doing in the different areas.

- Have you had a chance to look back?

Is there some interesting,

very low level specific to-do items,

maybe things you've never completed,

all that kind of stuff

and high level philosophical essay type of stuff

that stands out.

- Yeah, there's some good stuff on both,

where a lot of it was low level nitpicky details,

about game dev and I've learned enough things

where there's no project that I worked on

that I couldn't go back and do a better job on now.

I mean you learn things hopefully if you're doing it right,

you learn things as you get older

and you should be able to do a better job

at all of the early things.

And there's stuff in Wolfenstein, Doom, Quake that like,

"Oh, clearly I could go back and do a better job at this."

Whether it's something in the rendering engine side

or how I implemented the monster behaviors

or managed resources.

- Do you see flaws in your thinking now looking back?

- Yeah, I do.

I mean sometimes I'll get the,

I'll look at it and say,

"Yeah, I had a pretty clear view of,

"I was doing good work there"

and I haven't really hit the point

where there was another programmer, Graham Devine,

he had worked at id and 7th Guest

and he made some comment one time where he said,

he looked back at some of his old notes

and he was like, "Wow, I was really smart back then."

And I don't hit that so much where,

I mean, I look at it and I always know that,

yeah, there's all the,

with aging you get certain changes

in how you're able to work problems.

But all of the problems that I've worked,

I'm sure that I could do a better job on all of them.

- Oh wow.

- So, you can still step right in.

If you could travel back in time and talk to that guy,

you would teach him a few things.

- [John] Yeah, absolutely.

- That's awesome.

What about the high level philosophical stuff?

Is there some insights that stand out that you remember?

- There's things that I was understanding about development

and the industry

and so on that we're in a more primitive stage,

where I definitely learned a lot more

in the later years about business

and organization and team structure.

There were, I mean,

there were definitely things that I was not the best person

or even a very good person about managing,

like how a a team should operate internally,

how people should work together.

I was just,

the just get outta my way and let me work on the code

and do this.

And more and more I've learned how

in the larger scheme of things,

how sometimes relatively unimportant,

some of those things are

where it is this user value generation.

That's the overarching importance for all of that.

And I didn't necessarily have my eye on that ball correctly

through a lot of my earlier years.

And there's things that,

I could have gotten more out of people handling things

in different ways.

I could have made in some ways more successful products

by following things in different ways.

There's mistakes that we made

that we couldn't really have known

how things would've worked out.

But it was interesting to see in later years,

companies like Activision showing that,

hey, you really can just do the same game,

make it better every year.

And you can look at that from a negative standpoint

and say it's like,

"Oh, that's just being derivative and all that."

But if you step back again and say it's like,

no, are the people buying it still enjoying it?

Are they enjoying it more than

what they might have bought otherwise?

And you can say,

"No, that's actually a great value creation engine

"to do that if you're in a position where you can."

Don't be forced into reinventing everything,

just because you think that you need to,

lots of things about business

and team stuff that could be done better.

But the technical work

that the kind of technical visionary type stuff

that I laid out, I still feel pretty good about.

There are some classical ones about my defending of OpenGL,

versus D3D, which turned out to be one of the more,

probably important momentous things there where it never,

it was always a rear guard action on Windows

where Microsoft was just not gonna let that win.

But when I look back on it now,

that fight to keep OpenGL relevant

for a number of years there meant that OpenGL

was there when mobile started happening.

And OpenGL ES was the thing that drove,

all of the acceleration of the mobile industry.

And it's really only in the last few years

as Apple has moved to Metal

and some of the other companies have moved to Vulcan,

that that's moved away.

But really stepping back and looking at it,

it's like, yeah, I sold tens of millions of games

for different things,

but billions and billions of devices wound up

with an appropriate capable graphics API

in no small part to me,

thinking that that was really important

that we not just give up and use Microsoft's,

at that time really terrible, API.

The thing about Microsoft is the APIs don't stay terrible.

They were terrible at the start,

but a few versions on they were actually quite good.

And there was a completely fair argument to be made

that by the time DX9 was out,

it was probably a better programming environment

than OpenGL.

But it was still a wonderful good thing

that we had an open standard that could show up on Linux

and Android and iOS and eventually WebGL still to this day.

So, that was one that would be on my greatest hits list

of things that I kind of pushed-

- Impact it had on billions of devices, yes.

So, let's talk about it.

Can you tell the origin story of id Software,

again, one of the greatest game developer companies ever.

It created Wolfenstein 3D,

games that define my life also in many ways

as a thing that made me realize what computers

are capable of in terms of graphics,

in terms of performance.

It just unlocks something deep in me

and understanding what these machines are all about,

as games can do that.

So, Wolfenstein 3D, Doom, Quake

and just all the incredible engineering innovation

that went into that.

So, how did it all start?

- So, I'll caveat upfront

that I usually don't consider myself the historian

of the software side of things.

I usually do.

I kind of point people at John Romero

for stories about the early days where I've never been,

like I've commented

that I'm a remarkably unsentimental person in some ways

where I don't really spend a lot of time

unless I'm explicitly prodded to go back

and think about the early days of things.

And I didn't necessarily make the effort

to archive everything exactly in my brain.

And the more that I work on machine learning and AI

and the aspects of memory

and how when you go back and polish certain things,

it's not necessarily exactly the way it happened.

But having said all of that from my view,

the way everything happened

that led up to that was after I was an adult

and kind of taking a few college classes,

deciding to drop out,

I was doing, I was hard scrabble contract programming work,

really struggling to kind of keep groceries

and pay my rent and things.

And the company that I was doing the most work for

was a company called Soft Disc Publishing,

which had the sounds bizarre now business model

of monthly subscription software.

Before there was an internet that people could connect to

and get software you would pay a certain amount

and every month they would send you a disc

that had some random software on it.

And people that were into computers

thought this was kind of cool.

And they had different ones for the Apple II,

the 2GS, the PC, the Mac, the Omega,

lots of different things here.

So, quirky little business.

But I was doing a lot of contract programming for them

where I'd write tiny little games

and sell them for 300, $500.

And one of the things that I was doing, again,

to keep my head above water here

was I decided that I could make one program

and I could port it to multiple systems.

So, I would write a game like Dark Designs or Catacombs

and I would develop it on the Apple II, the 2GS

and the IBM PC,

which apparently was the thing

that really kind of peaked the attention

of the people working down there.

Like Jay Wilber was my primary editor

and Tom Hall was a secondary editor and they kept asking me,

it's like, "Hey, you should come down and work for us here."

And I pushed it off a couple times,

because I was really enjoying my freedom

of kind of being off on my own,

even if I was barely getting by.

I loved it.

I was doing nothing but programming all day.

But I did have enough close scrapes with like,

I'm just really outta money

that maybe I should get an actual job,

rather than contracting these kind of one at a time things.

And Jay Wilbur was great.

He was like FedExing me the checks when I would need them

to kind of get over whatever hump I was at.

So, I took the,

I finally took 'em up on their offer

to come down to Shreveport, Louisiana.

I was in Kansas City at the time,

drove down to through the Ozarks

and everything down to Louisiana

and saw the Soft Disc Offices.

Went through, talked to a bunch of people,

met the people I had been working with remotely

at that time.

But the most important thing for me was,

I met two programmers there, John Romero and Lane Roth,

that for the first time ever I had met programmers

that knew more cool stuff than I did,

where the world was just different back then.

I was in Kansas City,

it was one of those smartest kid in the school,

does all the computer stuff,

the teachers don't have anything to teach him.

But all I had to learn from

was these few books at the library.

It was not much at all.

And there were some aspects of programming

that were kind of black magic to me.

Like it's like,

"Oh, he knows how to format a track

"on a low level drive programming interface."

And this was,

I was still not at all sure I was gonna take the job,

but I met these awesome programmers

that were doing cool stuff.

And like Romero had worked at Origin Systems

and he had done like so many different games ahead of time

that I did kind of quickly decide.

It's like, yeah, I'll go take the job down there.

And I settled down there, moved in

and started working on more little projects.

And the first kind of big change that happened down there

was the company wanted to make

a PC gaming focused subscription,

just like all their others.

The same formula that they used for everything,

pay a monthly fee and you'll get a disc

with one or two games just every month

and no choice in what you get,

but we think it'll be fun.

And that was the model they were comfortable with and said,

"All right, we're gonna start this Gamers' Edge Department."

And all of us that were interested in that,

like me and Romero,

Tom Hall was kind of helping us from his side of things.

Jay would peek in

and we had a few other programmers working

with us at the time

and we were going to just start making games.

Just the same model.

And we dived in and it was fantastic.

- So, you have to make new games.

- [John] Every month.

- Every month.

- Yeah.

And this, in retrospect,

looking back at it,

that sense that I had done all this contract programming

and John Romero had done like far more of this

where he had done one of his teaching himself efforts

was he made a game for every letter of the alphabet.

It's that sense of like,

I'm just gonna go make 26 different games,

give him a different theme.

And you learn so much when you go through

and you crank these things out like on a biweekly,

monthly basis, something like that.

- From start to finish.

So, it's not like an I just an idea.

It's not just,

from the very beginning to the very end.

It's done, it has to be done,

there's no delaying, it's done.

- Yep and you've got deadlines.

And that kind of rapid iteration pressure cooker environment

was super important for all of us developing the skills

that brought us to where we eventually went to,

I mean people would say like in the history of the Beatles,

like it wasn't them being the Beatles,

it was them playing all of these other early works

that that opportunity to craft all of their skills,

before they were famous

that was very critical to their later successes.

And I think there's a lot of that here

where we did these games that nobody remembers.

Lots of little things that contributed

to building up the skillset for the things

that eventually did make us famous.

- Fyodor Dostoevsky wrote "The Gambler,"

he had to write it in a month, just make money.

And nobody remembers that probably,

'cause he had to figure out,

'cause it's literally he didn't have enough time

to write it fast enough.

So, to come up with hacks,

to actually literally write it faster.

- It gain comes down that point

where pressure and limitation of resources

is surprisingly important.

- [Lex] Yeah.

- And it's counterintuitive in a lot of ways

where you just think that if you've got all the time

in the world and you've got all the resources in the world,

of course you're gonna get something better.

But sometimes it really does work out that

the innovations mother necessity

and you know where you can or resource constraints

and you have to do things when you don't have a choice.

It's surprising what you can do.

- Is there any good games written in that time,

would you say?

- Some of them are still fun to go back

and play where you get the,

they were all about kind of the more modern term

is game feel about how just the exact feel that things,

it's not the grand strategy of the design,

# Chapter 7

- It gain comes down that point

where pressure and limitation of resources

is surprisingly important.

- [Lex] Yeah.

- And it's counterintuitive in a lot of ways

where you just think that if you've got all the time

in the world and you've got all the resources in the world,

of course you're gonna get something better.

But sometimes it really does work out that

the innovations mother necessity

and you know where you can or resource constraints

and you have to do things when you don't have a choice.

It's surprising what you can do.

- Is there any good games written in that time,

would you say?

- Some of them are still fun to go back

and play where you get the,

they were all about kind of the more modern term

is game feel about how just the exact feel that things,

it's not the grand strategy of the design,

but how running and jumping and shooting

and those things feel in the moment.

And some of those are still you sat down at 'em,

you kind of go, it's a little bit different.

It doesn't have the same movement feel,

but you move over and you're like bang, jump bang.

It's like, "Hey, that's kind of cool still."

- So, you can get lost in the rhythm of the game.

Like is that what you mean by feel?

Just like there's something about it that pulls you in.

- Nowadays, again, people talk about compulsion loops

and things where it's that that sense of exactly

what you're doing,

what your fingers are doing on the keyboard,

what your eyes are seeing.

And there are gonna be these sequences of things.

Grab the loot, shoot the monster, jump over the obstacle,

get to the end of the level.

These are eternal aspects of game design in a lot of ways.

But there are better and worse ways to do all of them.

And we did so many of these games that it was,

we got a lot of practice with it.

So, one of the kind of weird things

that was happening at this time is John Romero

was getting some strange fan mail.

And back in the days, this is before email,

so we literally got letters sometimes

and telling him, it's like,

"Oh, I wanna talk to you about your games.

"I wanna reach out different things."

And eventually it turned out

that these were all coming from Scott Miller

at Apogee Software and he was reaching out through,

he didn't think he could contact John directly

that he would get intercepted.

So, he was trying to get him to contact him through,

like back channel fan mail because he basically was saying,

"Hey, I'm making all this money on shareware games.

"I want you to make Shareware games."

Because he had seen some of the games that Romero had done

and we looked at Scott Miller's games

and we didn't think they were very good.

We're like, that can't be making the kind of money

that he's saying he's making 10 grand or something.

I am off of this game.

We really thought that he was full of shit.

That it was a lie trying to get to get him into this.

So that was kind of going on at one level,

and it was funny the moment when Romero realized

that he had some of these letters pinned up on his wall

of like all of his fans.

And then we noticed

that they all had the same return address

with different names on them,

which was a little bit of a two-edged sword there.

- But trying to figure out the puzzle laid out before him.

- Yeah, what happened after I kind of coincident

with that was I was working on a lot of the new technologies

where I was now full on the IBM PC for the first time

where I was really a long hold out on Apple II forever.

And I loved my Apple II,

it was the computer I always wished I had

when I was growing up.

And when I finally did have one,

I was kind of clinging onto that well past it,

sort of good use by day.

- Was it the best computer I ever made you, would you say?

- I wouldn't make judgments like that about it.

But it was positioned in such a way,

especially in the school systems,

that it impacted a whole lot of American programmers

at least where there was programs

that the Apple IIs got into the schools

and they had enough capability

that lots of interesting things happened with them.

In Europe it was different.

You had your Omegas and Ataris

and Acorns in the UK

and things that that had different things.

But in the United States it was probably the Apple II,

made the most impact for a lot of programmers

of my generation.

But, so I was really digging into the IBM

and this was even more so with the total focus,

because I had moved to another city

where I didn't know anybody that I wasn't working with.

I had a little apartment and then at Soft Disk,

again, the things that that drew me to it,

I had a couple programmers that knew more than I did

and they had a library,

they had a set of books and a set of magazines.

They had a couple years of magazines,

the old "Dr. Dobbs Journal" and all of these magazines

that had information about things.

And so I was just in total immersion mode.

It was eat, breathe, sleep, computer programming,

particularly the IBM for everything that I was doing.

And I was digging into

a lot of these low level hardware details

that people weren't usually paying attention to.

The way the IBM EGA cards worked,

which was fun for me.

I hadn't had experience with things at that level.

And back then you could get hardware documentation,

just down at the register levels.

This is where the CRTC register is,

this is how the color registers work

and how the different things are applied.

And they were designed for a certain reason.

They were designed for an application.

They had an intended use in mind,

but I was starting to look at other ways

that they could perhaps be exploited

that they weren't initially intended for.

- Could you comment on like,

first of all, what operating system was there?

What instruction set was it?

Like what are we talking about?

- So, this was Dawson X86.

So 16 bit 8086, the 286s were there and 386s existed.

They were rare.

We a couple for our development systems,

but we were still targeting the more broad,

it was all DOS 16 bit.

None of this was kind of DOS extenders and things.

- How different is it from the systems of today,

is it kind of the a precursor that's similar?

- Very little if you open up command.com on Windows,

you see some of the remnants of all of that.

But it was a different world.

It was the 640K is enough world and nothing was protected.

It crashed all the time.

You had TSRs or terminate

and stay resident hacks on top of things

that would cause configuration problems.

All the hardware was manually configured in your auto exec.

So, it was a very different world.

- The code is still the same.

- You could still write it.

My earliest code there was written in Pascal.

That was what I had learned kind of at an earlier point.

- So, between Basic and C plus plus there was Pascal.

- So, when basic assembly language and some of my-

- [Lex] Take a step back.

- Yeah, my intermediate stuff was,

well you had to for performance,

basic was just too slow.

So, most of the work that I was doing

as a contract programmer in my teenage years

was assembly language.

- You wrote games in assembly?

- Yeah, complete games in assembly language.

And it's thousands and thousands of lines

of three letter acronyms for the instructions.

- You don't earn

the once again greatest programmer ever label

without being able to write a game in assembly, okay.

- But that's again, everybody wrote their,

everybody serious wrote their games in assembly language.

- Pretty serious, you see what he said?

Everybody's serious.

- It was an outlier to use Pascal a little bit

where there was one famous program called Wizardry.

It was one, like one of the great early role playing games.

That was written in Pascal,

but it was almost nothing used Pascal there.

But I did learn Pascal

and I remember doing all of my,

like to this day,

I sketch in data structures

when I'm thinking about something,

I'll open up a file

and I'll start writing struct definitions

for how data is gonna be laid out.

And Pascal was kind of formative to that,

because I remember designing my RPGs

in Pascal records structures and things like that.

And so I had gotten a Pascal compiler

for the Apple IIGS that I could work on.

And the first IBM game that I developed, I did in Pascal.

And, and that's actually kind of an interesting story,

again, talking about the constraints and resources

where I had an Apple IIGS,

I didn't have an IBM PC.

I wanted to port my applications to IBM,

because I thought I could make more money on it.

So, what I wound up doing is I rented a PC for a week

and bought a copy of Turbo Pascal.

And so I had a hard one week

and this was cutting into what minimal profit margin

I had there.

But I had this computer for a week.

I had to get my program ported,

before I had to return the PC.

- Yeah.

- And that was kind of what the first thing

that I had done on the IBM PC

and what led me to the taking the job at Soft Disk.

- And Turbo Pascal.

How's that different from regular Pascal?

Is it different compiler or something like that?

- So, it was a product of Borland,

which before Microsoft kind of killed them,

they were the hot stuff developer tools company.

You had Borland Turbo Pascal and Turbo C and Turbo Prologue,

I mean all the different things.

But what they did was

they took a supremely pragmatic approach

of making something useful.

It was one of these great examples

where Pascal was an academic language

and you had things like the UCSDP system

that Wizardry was actually written in

that they did manage to make a game with that.

But it was not a super practical system.

While Turbo Pascal was,

it was called Turbo because it was blazingly fast

to compile,

I mean really ridiculously 10 to 20 times faster

than most other compilers at the time.

But it also had very pragmatic access to look,

you can just poke at the hardware in these different ways.

And we have libraries that let you do things.

And it was a perfectly good way to write games.

And this is one of those things

where people have talked about different paths

that computer development could have taken

where C took over the world for reasons

that came out of Unix and eventually Linux.

And that was not a foregone conclusion at all.

And people can make real reasoned, rational arguments

that the world might've been better

if it had gone a Pascal route.

I'm somewhat agnostic on that,

where I do know from experience

it was perfectly good enough to do that.

And it had some fundamental improvements.

Like it had range checked arrays as an option there,

which could avoid many of C's real hazards

that happened in a security space.

But C one,

they were basically operating

at about the same level of abstraction.

It was a systems programming language.

- But you said Pascal had a more emphasis

on data structures.

I actually,

in the tree of languages the Pascal come before C,

did it inspire a lot-

- They were pretty contemporaneous.

So, Pascal's Lineage went to modular two

and eventually Oberon which was another Niklaus Wirth

kind of experimental language.

But they were all good enough at that level.

Now some of the classic academic oriented Pascals

were just missing fundamental things.

Like, oh, you can't access this core system thing,

because we're just using it to teach students.

But Turbo Pascal showed that only modest changes

to it really did make it a completely capable language

and it had some reasons why you could implement it

as a single pass compiler.

So, it could be way, way faster,

although less scope for optimizations if you do it that way.

And it did have some range checking options.

It had a little bit better typing capability.

You'd have properly typed enums sorts of things

and other stuff that C lacked.

But C was also clearly good enough

and it wound up with a huge inertia

from the Unix ecosystem and everything that came with that.

- Garbage collection.

- [John] No, it was not garbage collected.

- It's the same kind of thing as C.

- Same manual.

So, you could still have your use after freeze

and all those other problems,

but just getting rid of array overruns,

at least if you were compiled with that debugging option,

certainly would've avoided a lot of problems

and could have a lot of benefits.

But, so anyways, that was the next thing,

I had to learn C,

because C was where it seemed like,

most of the things were going.

So, I abandoned Pascal and I started working in C.

I started hacking on these hardware things,

dealing with the graphics controllers

and the EGA systems and what we most wanted to do.

So, at that time we had,

we were sitting in our darkened office playing,

all the different console video games

and we're figuring out what do we want to kind of,

what games do we want to make

for our Gamers Edge product there?

And so we had one of the first super Nintendos sitting there

and we had an older Nintendo

and we were looking at all those games.

And the core thing that those consoles did

that you just didn't get on the PC games

was this ability to have a massive scrolling world

where most of the games that you would make on the PC

and earlier personal computers would be a static screen.

You move little things around on it

and you interact like that,

maybe you go to additional screens as you move.

But arcade games and consoles

had this wonderful ability to just have a big world

that you're slowly moving your window through.

And that was for those types of games,

the kind of action exploration, adventure games,

that was a super, super important thing.

And PC games just didn't do that.

And what I had had come across

was a couple different techniques

for implementing that on the PC.

And they're not hard complicated things.

When I explained 'em now,

they're pretty straightforward,

but just nobody was doing it.

- You sound like Einstein describing his five papers

as pretty straightforward.

I understand.

But they're nevertheless revolutionary.

So, side scrolling is a game changer.

- [John] Yeah, it's scrolling-

- It's a genius invention.

- There's tighter vertical.

And some of the consoles had different limitations,

about you could do one but not the other.

And there were similar things going on as advancements,

even in the console space

where you'd have like the original Mario game

was like just horizontal scrolling.

And then later Mario Games added vertical aspects to it

and different things that you were doing to explore,

kind of expand the capabilities there.

And so much of the early game design for decades

was removing limitations,

letting you do things that you envisioned as a designer,

you wanted the player to experience,

but the hardware just couldn't really

or you didn't know how to make it happen.

It felt impossible.

- You can imagine that you want to create,

like this big world through which you can side scroll,

like through which you can walk

and then you ask yourself a question,

how do I actually build that in a way that's,

like the latency is low enough,

the hard work can actually deliver that

in such a way that's a compelling experience.

- Yeah and we knew what we wanted to do,

because we were playing all of these console games,

playing all these Nintendo games and arcade games.

Clearly there was a whole world of awesome things there

that we just couldn't do on the PC,

at least initially because every programmer can tell,

it's like if you wanna scroll,

you can just redraw the whole screen.

But then it turns out,

well, you're going five frames per second.

That's not an interactive fun experience.

You wanna be going 30 or 60 frames per second or something.

And it just didn't feel like that was possible.

It felt like the PCs had to get five times faster

for you to make a playable game there.

And interestingly,

I wound up with two completely different solutions

for the scrolling problem.

And this is a theme that runs through everything

where all of these big technical advancements,

it turns out there's always a couple different ways

of doing them.

And it's not like you found the one true way of doing it.

And we'll see this as we go into 3D games and things later.

But, so the scrolling,

the first set of scrolling tricks that I got

was the hardware had this ability to,

you could shift like inside the window of memory.

So, the EGA cards at the time had 256 kilobytes of memory.

And it was awkwardly set up in this planer format

where instead of having 256 or 24 million colors,

you had 16 colors, which is four bits.

So you had four bit planes, 64K a piece.

# Chapter 8

It felt like the PCs had to get five times faster

for you to make a playable game there.

And interestingly,

I wound up with two completely different solutions

for the scrolling problem.

And this is a theme that runs through everything

where all of these big technical advancements,

it turns out there's always a couple different ways

of doing them.

And it's not like you found the one true way of doing it.

And we'll see this as we go into 3D games and things later.

But, so the scrolling,

the first set of scrolling tricks that I got

was the hardware had this ability to,

you could shift like inside the window of memory.

So, the EGA cards at the time had 256 kilobytes of memory.

And it was awkwardly set up in this planer format

where instead of having 256 or 24 million colors,

you had 16 colors, which is four bits.

So you had four bit planes, 64K a piece.

Of course 60 4K is a nice round number

for 16 bit of dressing.

So, your graphics card had a 16 bit window

that you could look at

and you could tell it

to start the video scan out anywhere inside there.

So, there were a couple games that had taken this approach.

If you could make a two by two screen

or a one by four screen

and you could do scrolling really easily like that,

you could just lay it all out and just pan around there,

but you just couldn't make it any bigger,

because that's all the memory that was there.

The first insight to the scrolling that I had was,

well, if we make a screen that's just one tile larger,

and we usually had tiles that were 16 pixels by 16 pixels,

the little classic Mario block that you run into,

lots of art gets drawn that way

and your screen is a certain number of tiles.

But if you had one little buffer region outside of that,

you could easily pan around inside that 16 pixel region

that could be perfectly smooth.

But then what happens if you get to the edge

and you want to keep going?

The first way we did scrolling was

what I call the adaptive tile refresh,

which was really just a matter of you get to the edge

and then you go back to the original point

and then only change the tiles that have actually,

that are different between where it was.

In most of the games at the time

if you think about sort of your classic,

Super Mario Brothers game,

you've got big fields of blue sky,

long rows of the same brick texture

and there's a lot of commonality.

It's kind of like a data compression thing.

If you take the screen

and you set it down on top of each other,

in general, only about 10% of the tiles

were actually different there.

So, this was a way to go ahead and say,

well, I'm gonna move it back

and then I'm only going to change those 10, 20,

whatever percent tiles there.

And that meant that it was essentially five times faster

than if you were redrawing all of the tiles.

And that worked well enough for us to do a bunch

of these games for Gamers Edge,

we had a lot of these scrolling games,

like slurred acts and shadow nights and things like that,

that we were cranking out at this high rate

that had this scrolling effect on it.

And it worked well enough.

There were design challenges there

where if you made the worst case,

if you made a checkerboard over the entire screen,

you scroll over one and every single tile changes

and your frame rates now five frames per second,

because it had to redraw everything.

So, the designers had a little bit

that they had to worry about,

they had to make these relatively plain looking levels,

but it was still pretty magical.

It was something that we hadn't seen before.

And the first thing that we wound up doing with that was,

I had just gotten this working

and Tom Hall was sitting there with me

and we were looking over at our Super Nintendo

on the side there with Super Mario three running,

and we had the technology, we had the tools set up there

and we stayed up all night

and we basically cloned the first level

of Super Mario Brothers.

- Performance wise as well?

- Yeah and so and we had our little character running

and jumping in there.

It was close to pixel accurate

as far as all of the backgrounds and everything,

but the gaming was just stuff that we cobbled together

from previous games that I had written.

I just kind of like really kitbashed

the whole thing together to make this demo.

And that was one of the rare cases when I said I,

I don't usually do these all night programming things.

There's probably only two memorable ones

that I can think about.

One was the all-nighter to go ahead

and to get our Dangerous Dave in copyright infringement

is how we titled it,

because we had a game called Dangerous Dave,

which was running around with the shotgun shooting things.

And we were just taking our most beloved game

at the time there, the Super Mario Three,

and sort of sticking Dave inside that

with this new scrolling technology

that was going perfectly smooth for him as it ran.

And Tom and I just kind of literally the next morning,

kind of left and we left a disc on the desk

for John Romero and Jay Wilbur to see and just said,

run this.

And we eventually made it back in later in the day.

And it was,

like they grabbed us and pulled us in pulled us

into the room.

And that was the point where they were like,

we gotta do something with this.

We're gonna make a company,

we're gonna go make our own games.

Where this was something that

we were able to just kind of hit them

with a hammer of an experience like,

"Wow, this is just like so much cooler than

"what we thought was possible there."

And initially we tried to get Nintendo

to let us make Super Mario three on the PC.

That's really what we wanted to do.

We were like, "Hey, we can finish this.

"It's line of sight for this'll be great."

And we sent something to Nintendo

and we heard that it did get looked at in Japan

and they just weren't interested in that.

But that's another one of those life could have gone

a very different way

where we could have been like Nintendo's House PC team

at that point.

- And to find the direction of Wolfenstein

and Doom and Quake could have been a Nintendo creation.

- Yeah, so at the same time

that we were just doing our first scrolling demos,

we reached out to Scott Miller at Apogee and said,

it's like, "Hey, we do wanna make some games."

These things that you think you want,

those are nothing,

what do you see what we can actually do now?

This is gonna be amazing.

And he just like popped right up

and sent a check to us where we at that point

we still thought he might be a fraud,

that he was just lying about all of this.

But he was totally correct on how much money he was making

with his shareware titles.

And this was his kind of real brainstorm about this,

where Shareware was this idea

that software doesn't have a fixed price.

If you use it,

you send outta the goodness of your heart some money

to the creator.

And there were a couple utilities

that did make some significant success like that,

but for the most part it didn't really work.

Now, there wasn't much software

in a pure shareware model that was successful.

The Apogee innovation was to take something,

call it shareware, split it into three pieces.

You always made a trilogy

and you would put the first piece out,

but then you buy the whole trilogy

for some shareware amount, which in reality,

it meant that the first part was a demo

where you kind of like the demo went everywhere for free

and you paid money to get the whole set,

but it was still played as shareware.

And we were happy to have the first one go everywhere.

And it wasn't a crippled demo

where the first episode of all of these trilogies,

it was a real complete game

and probably 20 times as many people played

that part of it thought they had a great game,

had found fond memories of it but never paid us a dime.

But enough people were happy with that,

where it was really quite successful.

And these early games that we didn't think very much of,

compared to commercial quality games,

but they were doing really good business,

some fairly crude things and people,

it was good business people enjoyed it.

And it wasn't like you were taking a crapshoot

on what you were getting.

You just played a third of the experience

and you loved it enough to hand write out a check

and put it in an envelope and address it

and send it out to Apogee to get the rest of them.

So, it was a really pretty feel good business prospect there

because everybody was happy,

they knew what they were getting when they send it in.

And they would send in fan mail

if you're going into the trouble of addressing a letter

and filling out an envelope,

you write something in it.

And there were just the literal bags of fan mail

for the shareware games.

So, people loved them.

- I should mention that for you,

the definition of wealth

is being able to have pizza whenever you want.

For me, there was a dream,

because I would play shareware games over and over,

the part that's free over and over.

And it was very deeply fulfilling experience.

But, I dreamed of a time

when I could actually afford the full experience.

And this is kind of this dream land beyond the horizon

where you could find out what else is there.

In some sense, even just playing the shareware was,

it's the limitation of that,

life is limited, eventually all die.

In that way, shareware was like somehow really fulfilling

to have this kind of mysterious thing beyond

what's free always there.

It's kind of, I don't know,

maybe it's because a part of my childhood

is playing shareware games.

That was a really fulfilling experience.

It's so interesting how that model still brought joy

to so many people.

20x people that played it.

- Yeah, I felt very good about that.

And I would run into people,

it's like that would say, oh, I loved that game,

that you had early on Commander Keen whatever.

And they meant just the first episode

that they got to see everywhere.

- That's me, I played the crap outta Commander Keen.

- And that was all good.

- Yeah, yeah.

- But so we were in this position where Scott Miller

was just fronting us cash saying,

yeah, make a game.

But we did not properly pull the trigger and say,

"All right, we're quitting our jobs."

We were like, we're gonna do both.

We're gonna keep working at Soft Disc working on this

and then we're going to go ahead

and make a new game for Apogee at the same time.

And this eventually did lead to some legal problems

and we had trouble.

It all got worked out in the end,

but it was not a good call at the time there.

- And your legal mind at the time was not stellar.

You were not thinking in terms in legal terms.

- No, I definitely wasn't.

None of us were.

And in hindsight, yeah,

it's like how did we think we were gonna get away

with like even using our work computers

to write software for our breakaway new company.

It was not a good plan.

- How did Commander Keen come to be?

- So, the design process,

we would start from,

we had some idea of what we wanted to do.

We wanted to do a Mario-like game.

It was gonna be a side scroller,

it was gonna use the technology.

We had some sense of what it would have to look like,

because of the limitations

of this adaptive tile refresh technology.

It had to have fields of relatively constant tiles.

You couldn't just paint up a background

and then move that around.

The early design

or all the design for Commander Keen really came

from Tom Hall where he was kind of the main creative mind

for the early id Software stuff

where we had an interesting division of things

where Tom was all creative in design.

I was all programming, John Romero was an interesting bridge

where he was both a very good programmer

and also a very good designer and artist

and kind of straddled between the areas.

But Commander Keen was very much Tom Hall's baby

and he came up with all the design

and backstory for the different things of kind of,

a mad scientist little kid with I am,

building a rocket ship and a zap gun

and visiting alien worlds

and doing all of this that the background

that we lay the game inside of.

And there's not a whole lot to any of these things.

Design for us was always just what we needed to do

to make the game that was gonna be so much fun to play.

And we made our, we laid out our first trilogy of games,

the shareware formula.

It was gonna be three pieces.

We would make Commander Keen one, two, and three.

And we just really started busting on all that work.

And it went together really quickly.

It was like three months or something

that while we were still making games every month

for Gamers' Edge, we were sharing technology between that.

I'd write a bunch of code for this

and we'd just kind of use it for both.

Again, not a particularly good idea there

that had consequences for us.

But in three months we got our first game out

and all of a sudden it was three times as successful

as the most successful thing Apogee had had before.

And we were making like $30,000 a month,

immediately from the Commander Keen stuff.

And that was again, a surprise to us.

It was more than we thought that was gonna make.

And we said, well,

we're gonna certainly roll into another set of titles

from this.

And in that three months,

I had come up with a much better way

of doing the scrolling technology

that was not the adaptive tile refresh,

which in some ways was even simpler.

And these things,

so many of the great ideas of technology are things

that are back of the envelope designs.

I make this comment about modern machine learning

where all the things that are really important practically

in the last decade are,

each of them fits on the back of an envelope.

There are these simple little things,

they're not super dense, hard to understand technologies.

And so the second scrolling trick was just a matter of like,

okay, we know we've got this 64K window

and the question was always like,

well you could make a two by two

but you can't go off the edge.

But I finally asked,

well what actually happens if you just go off the edge?

If you take your start and you say it's like, okay,

I can move over.

I'm scrolling, I can move over, I can move down.

I'm scrolling.

I get to what should be the bottom of the memory window?

It's like, well what if I just keep going

and I say I'm gonna start at,

what happens if I start at FFFE at the very end

of the 64K block and it turns out it just wraps back around

to the top of the block.

And I'm like, "Oh well this makes everything easy."

You can just scroll the screen everywhere

and all you have to draw is just one new line of tiles,

which everything you expose,

it might be unaligned off various parts

of the screen memory, but it just works.

That no longer had the problem of,

you had to have fields of the similar colors,

because it doesn't matter what you're doing,

you could be having a completely unique world

and you're just drawing the new strip as it comes on.

- But it might be like you said unaligned,

so it can be all over the place.

- Yeah and it turns out it doesn't matter.

I would have two page flipped screens.

As long as they didn't overlap,

they moved in series through this two dimensional window

of graphics.

And that was one of those like,

well this is so simple, this just works.

It's faster there.

It seemed like there was no downside.

Funny thing was,

it turned out after we shipped titles with this,

there were what they called super VGA cards,

the cards that would allow higher resolutions

and different features that the standard ones didn't.

And on some of those cards,

this was a weird compatibility quirk again,

because nobody thought

this was not what it was designed to do.

And some of those cards had more memory,

they had more than just 256K in four planes.

They had five 12K or a megabyte.

And on some of those cards,

I scroll my window down

and then it goes into initialized memory

that actually exists there,

rather than wrapping back around to the top.

And then I was in the tough position of,

do I have to track every single one of these?

And it was a madhouse back then with,

# Chapter 9

Funny thing was,

it turned out after we shipped titles with this,

there were what they called super VGA cards,

the cards that would allow higher resolutions

and different features that the standard ones didn't.

And on some of those cards,

this was a weird compatibility quirk again,

because nobody thought

this was not what it was designed to do.

And some of those cards had more memory,

they had more than just 256K in four planes.

They had five 12K or a megabyte.

And on some of those cards,

I scroll my window down

and then it goes into initialized memory

that actually exists there,

rather than wrapping back around to the top.

And then I was in the tough position of,

do I have to track every single one of these?

And it was a madhouse back then with,

there were 20 different video card vendors

with all slightly different implementations

of their non-standard functionality.

So, either I needed to natively program all of the VGA cards

there to map in that memory

and keep scrolling down through all of that.

Or I kind of punted and took the easy solution

of when you finally did run to the edge of the screen,

I accepted a hitch

and just copied the whole screen up there.

So, on some of those cards, it was a compatibility mode.

In the normal ones, when it all worked fine,

everything was just beautifully smooth.

But if you had one of those cards

where it did not wrap the way I wanted it to,

you'd be scrolling around, scrolling around

and then eventually you'd have a little hitch

where 200 milliseconds or something

that was not super smooth.

- Yeah, it froze a little bit.

And it's a binary thing.

Is it one of the standard screens

or is it one of the weird ones?

The super VGA ones.

- Yeah. - Okay.

- And so we would default to,

and I think that was one of those that changed,

over the kind of course of deployment

where early on we would have a normal mode

and then you would enable the compatibility flag

if your screen did this crazy flickery thing

when you got to a certain point in the game.

And then later I think it probably got enabled by default

as just more and more of the cards.

It kind of did not do exactly the right thing.

And that's the two-edged sword

of doing unconventional things with technology

where you can find something that nobody thought about doing

that kind of scrolling trick when they set up those cards.

But the fact that nobody thought

that was the primary reason when I was relying on that,

then I wound up being broken on some of the later cards.

- Let me take a bit of a tangent,

but ask you about the hacker ethic,

'cause you mentioned shareware,

it's an interesting world,

the world of people that make money,

the business and the people that build systems,

the engineers.

And what is the hacker ethic?

You've been a man of the people

and you've embodied at least the part of that ethic.

What does it mean?

What did it mean to you at the time?

What does it mean to you today?

- So, Stephen Levy's book "Hackers"

was a really formative book for me as a teenager.

I mean I read it several times

and there was all of the great lore

of the early MIT era of hackers

and ending up at the end with,

it kind of went through the early MIT hackers

and then the Silicon Valley hardware hackers

and then the game hackers in part three.

And at that time as a teenager,

I really was kind of bitter in some ways.

Like I thought I was born too late,

I thought I missed the window there

and I really thought I belonged in that third section

of that book with the game hackers.

And they were talking about the Williams at Sierra

and Origin Systems with Richard Garriott,

and it's like, I really wanted to be there.

And I knew that was now a few years in the past it,

it was not to be,

but the early days, especially the early MIT hacker days,

talking a lot about this sense of the hacker ethic,

that there was this sense that

it was about sharing information, being good,

not keeping it to yourself

and that it's not a zero sum game

that you can share something with another programmer

and it doesn't take it away from you.

You then have somebody else doing something.

And I also think that there's an aspect of it

where it's this ability to take joy

in other people's accomplishments

where it's not the cutthroat bit of like I have to be first,

I have to be recognized

as the one that did this in some way.

But being able to see somebody do something and say,

"Holy shit, that's amazing."

And just taking joy in the ability of something amazing

that somebody else does.

And the big thing that I was able to do

through id Software

was this ability to eventually release the source code

for most of our,

like all of our really seminal game titles.

And that was a,

it was a stepping stone process

where we were kind of surprised early on

where people were able to hack the existing games.

And of course I had experience with that.

I remember hacking my copies of Ultima,

so I'd give myself, 9999 gold and raise my levels

and break out the sector editor.

And so I was familiar with all of that.

So, it was just, it was with a smile

when I started to see people doing that to our games.

Making level editors for Commander Keen

or hacking up Wolfenstein 3D

but I made the pitch internally

that we should actually release our own tools

for like what we did,

what we used to create the games.

And that was a little bit debatable about well,

we'll give people a leg up.

It's always like,

what's that gonna mean for the competition?

- [Lex] Yeah.

- But the really hard pitch

was to actually release the full source code for the games

and it was a balancing act

with the other people inside the company

where, it's interesting how the programmers,

generally did get,

certainly the people that I worked closely with,

they did kind of get that hacker ethic bit

where you wanted to share your code,

you were proud of it,

you wanted other people to take it

and do cool things with it.

But interestingly, the broader game industry

is a little more hesitant to embrace that

than like the group of people that we happen to have

at id Software.

Where it was always a little interesting to me,

seeing how a lot

of people in the game modding community

were very possessive of their code.

They did not want to share their code,

they wanted it to be theirs,

it was their claim to fame.

And that was much more like what we tended to see

with artists

where the artists understand something about credit

and wanting it to be known as their work.

And a lot of the game programmers,

felt a little bit more like artists

than like hacker programmers

in that it was about building something

that maybe felt more like art to them

than the more tool-based and exploration-based,

kind of hacking culture side of things.

- Yeah.

So, it's so interesting that this kind of fear

that credit will not be sufficiently attributed to you.

- And that's one of the things that I do bump into a lot,

because I try not to go clean.

I mean, it's easy for me to say,

because so much credit is heaped on me

for the the id Software side of things.

But when people come up and they want to pick a fight

and say no, it's like that wasn't

where first person gaming came from.

And you can point to some of like things on obscure titles

that I was never aware of or like the old Plato systems

or each personal computer had something

that was 3D-ish and moving around

and I'm happy to say it's like no,

I mean I saw Battle Zone and Star Wars in the arcades.

I had seen 3D graphics,

I had seen all these things

that I'm standing on the shoulders of lots of other people,

but sometimes these examples they pull out,

it's like, "Nah, I didn't know that existed."

I mean there,

I had never heard of that before then

that didn't contribute to what I made.

But there's plenty of stuff that did.

And I think there's good cases to be made

that obviously Doom and Quake and Wolfenstein

were were formative examples

for what everything that came after that.

But I don't feel the need to go fight

and say claim primacy or initial invention

of anything like that.

But a lot of people do want to.

- I think when you fight for the credit in that way

and it does go against the hacker ethic,

you destroy something fundamental about the culture,

about the community that builds cool stuff.

I think credit ultimately,

I had this sort of,

there's a famous wrestler and freestyle wrestling,

called Tatsuhiro Saito,

and he always preached that you should just focus

on the art of the wrestling

and let people write your story however they want.

Te highest form of the art is just focusing on the art.

And that's something that is something,

about the hacker ethic

is just focused on building cool stuff,

sharing it with other cool people

and credit will get assigned correctly

in the long arc of history.

- Yeah.

And I generally think that's true and you've got,

like there's some things there's,

there's the graphics technique

that got labeled CarMax Reverse,

literally named and it turned out

that I wasn't the first person to figure that out.

Like most scientific things or mathematical things,

you wind up, it's like,

"Oh this other person had actually done that,

"somewhat before."

And then there's things that get attributed to me,

like the inverse square root hack that I actually didn't do.

I flat out that wasn't me.

And it's like, it's weird

how the mimetic power of the internet.

I cannot convince people of that, yes.

- It's just everything just gets attributed to you now,

even though you've never sought the credit of things.

I mean, but part of the fact that humility behind that

is what attracts the attributions.

Let's talk about a game,

to me one of the greatest games ever made.

I know you could talk about Doom and Quake and so on,

but to me Wolfenstein 3D was like, whoa,

it blew my mind that that world like this could exist.

So, how did Wolfenstein 3D come to be

in terms of the programming,

in terms of the design,

in terms of some of the memorable technical challenges

And also actually just something you haven't mentioned

is how do these ideas come to be inside your mind,

the adaptive side scrolling.

So, the solutions to these technical challenges.

- So, I usually can introspectively pull back,

pretty detailed accounts of how technology solutions

and design choices on my part came to be.

Where technically we had done two games,

3D games like that before

where Hover Tank was the first one

which had flat shaded walls

but did have the scaled enemies inside it.

And then Catacombs 3D which had textured walls,

scaled enemies and some more functionality,

like the disappearing walls and some other stuff.

But what's really interesting

from a game development standpoint is

those games Catacombs 3D, Hover Tank and Wolfenstein,

they literally used the same code

for a lot of the character behavior that a 2D game

that I had made earlier called Catacombs did,

where it was an overhead view game,

kind of like gauntlet,

you're running around and you can open up doors,

pick up items, basic game stuff.

And the thought was that

this exact same game experience just presented

in a different perspective.

It could be literally the same game,

just with a different view into it,

would have a dramatically different impact on the players.

- So, it wasn't a true 3D,

you're saying that you could kind of fake it.

You can like scale enemies,

meaning things that are farther away,

you can make 'em smaller.

- So, from the game was a 2D map,

like all of our games used the same tool for creation.

We used the same map editor for creating Keen,

as Wolfenstein and Hover Tank and Catacombs

and all this stuff.

So the game was a 2D grid made outta blocks

and you could say, well these are walls,

these are where the enemies start.

Then they start moving around.

And these early games like Catacombs,

you played it strictly in a 2D view.

It was a scrolling 2D view

and that was kind of using an adaptive tile refresh

at the time to be able to do something like that.

And then the thought that these early games,

all it did was take the same basic enemy logic,

but instead of seeing it from the god's eye view on top,

you are inside it

and turning from side to side yawing your view

and moving forwards and backwards and side to side.

And it's a striking thing

where you always talk about wanting to isolate

and factor changes in values.

And this was one of those most pure cases there

where the rest of the game changed very little.

It was our normal kind of change the colors on something

and draw a different picture for it,

but it's kind of the same thing.

But the perspective changed in a really fundamental way

and it was dramatically different.

I can remember the reactions where the artist Adrian

that had been drawing the pictures for it,

we had a cool big troll thing in Catacombs 3D

and we had these walls that you could get a key

and you could make the blocks disappear

and really simple stuff,

blocks could either be there or not there.

So, our idea of a door

was being able to make a set of blocks just disappear.

And I remember the reaction

where he had drawn these characters

and he was slowly moving around

and like people had no experience with 3D navigation,

it was all still keyboard.

We didn't even have mice set up at that time.

But slowly moving, going up, picked up a key, go to a wall,

the wall disappears in a little animation

and there's a monster like right there.

And he practically fell out of his chair.

It was just like, ah.

And games just didn't do that.

The games were the god's eye view.

You were a little invested in your little guy,

you can be like happy or sad when things happen,

but you just did not get that of startle reaction.

- You weren't inside your game.

- Something in the back of your brain.

Some reptile brain thing is just going,

"Oh, shit something just happened."

And that was one of those early points where it's like,

yeah, this is gonna make a difference.

This is going to be powerful and it's gonna matter.

- Were you able to imagine that in the idea stage or no?

- So not that exact thing.

So again, we had cases like the arcade games,

Battle Zone and Star Wars

that you could kind of see a 3D world

and things coming at you and you get some sense of it.

But nothing had done the kind of worlds

that we were doing and the sort of action based things.

3D at the time was really largely about

the simulation thoughts.

And this is something that,

really might have trended differently

if not for the id Software approach in the games

where there were flight simulators,

there were driving simulators,

you had like hard drive in and Microsoft Flight Simulator

and these were doing 3D and general purpose 3D

and ways that were more flexible

than what we were doing with our games.

But they were looked at as simulations.

They weren't trying to necessarily be fast or responsive

or letting you do kind of exciting maneuvers,

because they were trying to simulate reality

and they were taking their cues from the big systems,

the Evans and Sutherlands

and the Silicon Graphics that were doing things.

But we were taking our cues

from the console and arcade games,

we wanted things that were sort of quarter eaters

that were doing fast paced things

that you could smack you around,

rather than just smoothly gliding you from place to place.

- So, quarter years.

- And a funny thing is,

# Chapter 10

there were driving simulators,

you had like hard drive in and Microsoft Flight Simulator

and these were doing 3D and general purpose 3D

and ways that were more flexible

than what we were doing with our games.

But they were looked at as simulations.

They weren't trying to necessarily be fast or responsive

or letting you do kind of exciting maneuvers,

because they were trying to simulate reality

and they were taking their cues from the big systems,

the Evans and Sutherlands

and the Silicon Graphics that were doing things.

But we were taking our cues

from the console and arcade games,

we wanted things that were sort of quarter eaters

that were doing fast paced things

that you could smack you around,

rather than just smoothly gliding you from place to place.

- So, quarter years.

- And a funny thing is,

so much that that built into us that Wolfenstein,

still had lives

and you had like one of the biggest power ups

in all these games, like was an extra life,

because you started off with three lives

and you lose your lives and then it's game over

and there weren't save games in most of this stuff.

It sounds almost crazy to say this,

but it was an innovation in Doom to not have lives.

You could just play doom as long as you wanted.

You just restart at the the start of the level and why not?

This is like we aren't trying to take people's quarters,

they've already paid for the entire game.

We want them to have a good time

and you would have some,

some old timer purists that might think

that there's something to the epic journey

of making it to the end,

having to restart all the way from the beginning

after a certain number of tries.

But now more fun is had

when you just let people kind of keep trying

when they're stuck rather than having to go all the way back

and learn different things.

- So, you've recommended the book,

"Game Engine Black Book Wolfenstein 3D"

for technical exploration of the game.

So looking back 30 years,

what are some memorable technical innovations

that made this perspective shift into this world

that's so immersive that scares you when a monster appears?

What were some things you had to solve?

- So, one of the interesting things

that come back to the theme of deadlines

and resource constraints,

the game Catacombs 3D we shipped,

we were supposed to be shipping this for Gamers' Edge

on a monthly cadence and I had slipped,

I was actually late,

it slipped like six weeks,

because this was texture mapped walls doing stuff

that I hadn't done before.

And at the six week point,

it was still kind of glitchy and buggy.

There were things that I knew that

if you had a wall that was like almost edge on,

you could slide over to it

and you could see some things freak out

or vanish or not work.

And I hated that, but I was up against the wall.

We had to ship the game.

It was still a lot of fun to play.

It was novel, nobody had seen it.

It gave you that startle reflex reaction.

So, it was worth shipping,

but it had these things that I knew were kind of flaky

and janky and not what I was really proud of.

So, one of the things that I did very differently

in Wolfenstein, I was went,

Catacombs used almost a conventional thing

where you had segments

that were one dimensional polygons basically,

that were clipped and back faced

and done kind of like a very crude 3D engine

from the professionals.

But I wasn't getting it done right.

I was not doing a good enough job.

I didn't really have line of sight to fix it, right?

There's stuff that of course I look back,

it's like, oh it's obvious how to do this

and do the math right?

Do your clipping right,

check all of this, how you handle the precision.

But I did not know how to do that at that time.

- Was that the first 3D engine you wrote Catacombs 3D?

- And Hover Tank had been a little bit before that,

but that had the flat shaded walls.

So the texture mapping on the walls was

what was bringing in some of these challenges.

That was hard for me

and I couldn't solve it right at the time.

- Can you describe what flat shading is and texture mapping?

- So, the walls were solid color,

one of 16 colors in Hover Tank.

So, that's easy, it's fast.

You just draw the solid color for everything.

Texture mapping is what we all see today

where you have an image that is stretched

and distorted onto the walls

or the surfaces that you're working with.

And it was a long time for me to just figure out how to do

that without it distorting in the wrong ways

and I did not get it all exactly right in Catacombs

and I had these flaws.

So, that was important enough to me

that rather than continuing to bang my head on that

when I wasn't positive I was gonna get it,

I went with a completely different approach for drawing,

for figuring out where the walls were,

which was a ray casting approach,

which I had done in Catacombs 3D,

I had a bunch of C code trying to make this work right

and it wasn't working right.

In Wolfenstein,

I wound up going to a very small amount of assembly code.

So, in some ways this should be a slower way of doing it,

but by making it a smaller amount of work

that I could more tightly optimize, it worked out.

And Wolfenstein 3D was just absolutely rock solid.

It was nothing glitched in there.

The game just was pretty much through all of that

and I was super proud of that.

But eventually, like in the later games,

I went back to the more span based things

where I could get more total efficiency,

once I really did figure out how to do it.

So, there were two sort of key technical things

to Wolfenstein.

One will this ray casting approach,

which you still to this day,

you see people go and say let's write a ray casting engine

because it's an understandable way of doing things

that lets you make games very much like that.

So, you see ray casters in JavaScript,

ray casters in Python,

people that are basically going

and reimplementing that approach

to taking a tiled world and casting out into it.

It works pretty well,

but it's not the fastest way of doing it.

- Can you describe what ray casting is?

- So you start off and you've got your screen,

which is 320 pixels across at the time

if you haven't sized down in the window for greater speed.

And at every pixel there's gonna be an angle from,

you've got your position in the world

and you're gonna just run along that angle

and keep going until you hit a block.

So, up to 320 times across there,

it's gonna throw a cast array out into the world

from wherever your origin is until it runs into a wall

and then it can figure out exactly

where on the wall it hits.

The performance challenge of that is

as it's going out every block it's crossing it checks,

is this a solid wall?

So, that means that in like the early Wolfenstein levels,

you're in a small jail cell going out into a small hallway,

it's super efficient for that,

because you're only stepping across three or four blocks.

But then if somebody makes a room that covers,

our maps we're limited to 64 by 64 blocks.

If you made one room that was nothing

but walls at the far space,

it would go pretty slow,

because it would be stepping across 80 tile tests

or something along the way.

- By the way

the physics of our universe seems to be competing

in this very thing.

So, this maps nicely to the actual physics of our world.

- Yeah, you get like-

- Intuitively

- I follow a little bit of something,

like Stephen Wolfram's work on,

interconnected network information states of that

and it's beyond what I can have an informed opinion on.

But it's interesting that people

are considering things like that

and have and have things that can back it up.

Yeah, there's whole different sets

of interesting stuff there.

- So, Wolfenstein 3D had ray casting.

- So, ray casting

and then the other kind of key aspect was

what I called compiled scalers,

where the idea of,

you saw this in the earlier classic arcade games,

like Space Harrier and stuff where,

you would take a picture

which is normally drawn directly on the screen

and then if you have the ability

to make it bigger or smaller,

big chunky pixels or fizzly, small drop sample pixels.

That's the fundamental aspect

of what our characters were doing in these 3D games.

You would have,

it's just like you might've drawn a tiny little character,

but now we can make 'em really big

and make 'em really small and move it around.

That was the limited kind of 3D that we had for characters

to make 'em turn,

there were literally eight different views of them.

You didn't actually have a 3D model that would rotate,

you just had these cardboard cutouts,

but that was good enough for that startle fight reaction

and it was kind of what we had to do deal with there.

So, a straightforward approach to do that,

you could just write out your doubly nested loop

of you've got your stretch factor

and it's like you've got a point,

you stretch by a little bit.

It might be on the same pixel,

it might be on the next pixel,

it might have skipped a pixel.

You can write that out,

but it's not gonna be fast enough

where especially you get a character

for that right in your face,

monster covering almost the entire screen.

Doing that with a general purpose scaling routine,

would've just been much too slow.

It would've worked when they're small characters,

but then it would get slower and slower as they got closer

to you until right at the time

when you most care about having a fast reaction time,

the game would be chunking down.

So, the fastest possible way to draw pixels at that time

was to, instead of saying,

I've got a general purpose version

that can handle any scale I made,

I used a program to make essentially a hundred

or more separate little programs that was optimized for,

I will take an image and I will draw it 12 pixels tall,

I'll take an image, I'll draw it 14 pixels tall,

up by every two pixels, even for that.

So, you would have the most optimized code,

so that in the normal case where most of the world

is fairly large, like the pixels are big,

we did not have a lot of memory.

So, in most cases that meant

that you would load a pixel color

and then you would store it multiple times.

So, that was faster than even copying an image

in a normal conventional case

because most of the time the image is expanded.

So, instead of doing one read,

one write for a simple copy,

you might be doing one read and three or four writes

as it got really big.

And that had the beneficial aspect

of just when you needed the performance most

when things are covering the screen,

it was giving you the most acceleration for that.

- By the way,

were you able to understand this through thinking about it

or were you testing like the right speed?

- So this again comes back to,

I can find the antecedents for things like this.

So, in back in the Apple II days,

the graphics were essentially single bits at a time.

And if you wanted to make your little spaceship,

if you wanted to make it smoothly go across the world,

if you just took the image

and you drew it out at the next location,

you would move by seven pixels at a time.

So it would go chunk, chunk, chunk.

If you wanted to make it move smoothly,

you actually had to make seven versions of the ship

that were pre-shift.

You could write a program that would shift it dynamically,

but on a one megahertz processor

that's not going anywhere fast.

So, if you wanted to do a smooth moving fast action game,

you made separate versions of each of these sprites.

Now, there were a few more tricks you could pull

that if it still fast enough,

you could make a compiled shape where,

instead of this program that normally copies an image

and it says like, get this bite from here stored here,

get this bite stored this bite.

If you've got the memory space,

you could say,

I'm going to write the program that does nothing

but draw this shape.

It's going to be like,

I'm going to load the immediate value 25,

which is some bit pattern.

And then I'm going to store that at this location,

rather than loading something from memory

that involved indexing registers and this other slow stuff.

You could go ahead and say,

no, I'm gonna hard code the exact values

of all of the image right into the program.

And this was always a horrible trade off there,

but you didn't have much memory

and you didn't have much speed.

But if you had something that you wanted to go really fast,

you could turn it into a program.

And that was knowing about that technique

is what made me think about some of these,

unwinding it for the PC

where people that didn't come from that background

were less likely to think about that.

- I mean there's some deep parallels,

probably to human cognition as well.

There's something about optimizing

and compressing the processing of a new information

that requires you to predict the possible ways

in which the game or the world might unroll.

And you have something like compiled scaler is always there.

So, you have like you have a prediction

of how the world will unroll

and you have some kind of optimized data structure

for that prediction.

And then you can modify

if the world turns out to be different,

you can modify a slight way.

- And as far as building out techniques,

so much of the brain is about the associative context.

When you learn something,

it's in the context of something else

and you can have faint, tiny little hints of things.

And I do think there are some deep things around,

like sparse distributed memories and boosting that.

It's like if you can just be slightly above the noise floor

of having some hint of something,

you can have things refined into pulling the memory back up.

So, being a programmer and having a toolbox

of like all of these things that,

things that I did in all of these previous lives

of programming tasks that still matters to me,

about how I'm able to pull up some of these things.

Like in that case it was something I did on the Apple II

then being relevant for the PC.

And I have still cases

when I would work on mobile development then be like,

"Okay, I did something like this back in the the Doom days,

"but now it's a different environment,"

but I has still had that tie.

I can bring it in and I can transform it

into what the world needs right now.

And I do think that's actually one of the very core things

with human cognition and brain-like functioning

is finding these ways about,

your brain is kind of everything everywhere, all at once.

It is just a set of all of this stuff

that is just fetched back by these queries that go into it

and they can just be slightly above the noise floor

with random noise in your neurons and synapses

that are affecting exactly what gets pulled up.

- So, you're saying some of these very specific solutions

for different games,

you find that there's a kernel of an a deep idea

that's generalizable to other to other things.

- Yeah, you can't predict what it's going to be,

but that idea of like,

I called out that compiled shaders in the forward

that I wrote for that the Game engine black book

as it's kind of an end point of unrolling code.

But that's one of those things that,

thinking about that and having that in your mind,

and I'm sure there are some programmers

that you know hear about that,

think about it a little bit,

it's kind of the mind blown moment.

It's like, "Oh you can just turn all of that data into code"

and nowadays you have instruction cache issues

and that's not necessarily the best idea.

But there are different,

it's an idea that has power

and has probably relevance in some other areas.

Maybe it's in a hardware point of view

that there's a way you approach building hardware

that has that same,

you don't even have to think about iterating,

you just bake everything all the way into it in one place.

- What is the story of how you came to Program Doom?

What are some memorable technical challenges

or innovations within that game?

- So, the path that we went after Wolfenstein got out

and we were on this crazy arc

where Keen one through three more success than we thought,

keen four through six, even more success,

Wolfenstein even more success.

So, we were on this crazy trajectory for things.

So actually our first box commercial project

was a Commander Keen game,

but then Wolfenstein was going to have a game,

called Spear of Destiny,

which was a commercial version, 60 new levels.

So, the rest of the team took the game engine,

pretty much as it was and started working on that.

We got new monsters,

but it's basically reskins of the things there.

And there's a really interesting aspect about that

that I didn't appreciate until much, much later,

# Chapter 11

- What is the story of how you came to Program Doom?

What are some memorable technical challenges

or innovations within that game?

- So, the path that we went after Wolfenstein got out

and we were on this crazy arc

where Keen one through three more success than we thought,

keen four through six, even more success,

Wolfenstein even more success.

So, we were on this crazy trajectory for things.

So actually our first box commercial project

was a Commander Keen game,

but then Wolfenstein was going to have a game,

called Spear of Destiny,

which was a commercial version, 60 new levels.

So, the rest of the team took the game engine,

pretty much as it was and started working on that.

We got new monsters,

but it's basically reskins of the things there.

And there's a really interesting aspect about that

that I didn't appreciate until much, much later,

about how Wolfenstein clearly did tap out

its limit about what you wanna play all the levels

and a couple of our license things.

There was a hard creative wall

that you did not really benefit much

by continuing to beat on it.

But a game like Doom

and other more modern games like Minecraft or something,

there's kind of a touring completeness level

of design freedom that you get in games

that Wolfenstein clearly sat on one side of,

all the creative people in the world,

could not go and do a masterpiece,

just with the technology that Wolfenstein had.

Wolfenstein could do Wolfenstein,

but you really couldn't do something crazy and different.

But it didn't take that much more capability

to get to Wolfenstein with the freeform lines

and a little bit more artistic freedom to get to the point

where people still announced new Doom levels today,

all these years after

without having completely tapped out the creativity.

- How did you put it touring complete-

- Like tour complete design space.

- Design space.

- Where it's like

we have the kind of computational universality

on a lot of things and how different substrates work.

But yeah, there's things where,

a box can be too small

but above a certain point

you kind of are at the point,

you really have almost unbounded creative ability there.

- And Doom was the first time you crossed that line.

- Yeah, where there were thousands of Doom levels created

and some of 'em still have something new

and interesting to say to the world about it.

- Is that line, can you introspect what that line was?

Is it in the design space?

Is it something about the programming capabilities

that you were able to add to the game?

- So, the graphics fidelity was a necessary part,

because the block limitations in Wolfenstein,

what we had right there was not enough.

The full scale blocks, although Minecraft,

I really did show that perhaps blocks stacked in 3D

and at one quarter the scale of that

or one eighth in volume

is then sufficient to have all of that.

But the wall sized blocks that we had in Wolfenstein

was too much of a creative limitation.

We licensed the technology to a few other teams.

None of them made too much of a dent with that.

It just wasn't enough creative ability,

but a little bit more,

whether it was the variable floors and ceilings

and arbitrary angles in Doom

or the smaller foxhole blocks in Minecraft

is then enough to open it up to just worlds and worlds

of new capabilities.

- What is binary space partitioning?

Which is one of the technologies, is it?

- Yeah, so jump around a little bit on the story path there.

- Yes.

- So, while the team was working on Spirit Destiny

for Wolfenstein.

We had met another development team, Raven Software,

while we were in Wisconsin

and they were doing,

they had RPG background and I still kind of loved that.

And I offered to do a game engine for them

to let them do a 3D rendered RPG instead of the,

like most RBG games were kind of hand drawn.

They made it look kind of 3D

but it was done just all with artist work,

rather than a real engine.

And after Wolfenstein, this was still a tile based world,

but I added floors and ceilings

and some lighting and the ability

to have some sloped floors in different areas.

And that was my intermediate step

for a game called Shadow Caster.

And it had slowed down enough,

it was not fast enough to do our type of action things.

So, they had the screen crop down a little bit,

so you couldn't go the full screen width,

like we would try to do in Wolfenstein,

but I learned a lot.

I got the floors and ceilings

and lightings and it looked great.

They were great artists up there.

And it was an inspiration

for us to look at some of that stuff.

But I had learned enough from that, that I had the plan for,

I knew faster ways to do the lighting and shadowing

and I wanted to do this freeform geometry.

I wanted to break out of this tile-based,

90 degree world limitations.

So, that was when we got our next stations

and we were working with these higher powered systems

and we built an editor

that let us draw kind of arbitrary line segments.

And I was working hard to try

to make something that could render this fast enough.

I was pushing myself pretty hard.

And we were at a point

where we could see some things that looked amazingly cool,

but it wasn't really fast enough for the way I was doing it,

for this flexibility, it was no longer,

I couldn't just ray cast into it.

And I had these very complex sets of lines

and simple little worlds were okay,

but the cool things that we wanted to do,

just weren't quite fast enough.

And I wound up taking a break at that point,

and I did the port,

I did two ports of our games Wolfenstein

to the Super Nintendo.

It was a crazy difficult thing to do

which was an even slower processor.

It was like a couple megahertz processor.

And it had been this whole thing

where we had farmed out the work and it wasn't going well.

And I took it back over

and trying to make it go fast on there,

where it really did not have much processing power.

The pixels were stretched up hugely

and it was pretty ugly when you looked at it,

but in the end it did come out fast enough to play

and still be kind of fun from that.

But that was where I started using BSP trees

or binary space partitioning trees.

It was one of those things I had to make it faster there.

It was a stepping stone

where it was reasonably easy to understand

in the grid world of Wolfenstein,

where it was all still 90 degree angles.

BSP trees were, I eased myself into it with that

and it was a big success.

Then when I came back to working on Doom,

I had this new tool in my toolbox.

It was gonna be a lot harder

with the arbitrary angles of Doom.

This was where I really started grappling

with Epsilon problems and just,

up until that point,

I hadn't really had to deal with the fact

that I am so many numeric things.

This almost felt like a betrayal to me

where people had told me

that I had mathematicians up on a bit of a pedestal

where I was, people think I'm a math wizard and I'm not.

I really, everything that I did was really done

with a solid high school math understanding,

algebra two, trigonometry.

And that was what got me all the way through Doom and Quake

and all of that, of just understanding basics of matrices

and knowing it well enough to do something with it.

- What's the Epsilon problems you ran into?

- So, when you wind up taking a,

like a sloped line and you say,

I'm going to intersect it with another sloped line,

then you wind up with something

that's not going to be on these nice grid boundaries.

With the Wolfenstein tile maps,

all you've got is horizontal and vertical lines,

looking at it from above.

And if you cut one of them,

it's just obvious the other one gets cut

exactly at that point.

But when you have angled lines,

you're doing a kind of a slope intercept problem

and you wind up with rational numbers there

where things that are not going to evenly land on an integer

or on any fixed point value that you've got.

So, everything winds up having to snap

to some fixed point value.

So, the lines slightly change their angle.

You wind up, if you cut something here,

this one's gonna bend a little this way

and it's not gonna be completely straight.

And then you come down to all these questions of,

well this one is a point on an angled line.

You can't answer that in finite precision,

unless you're doing something with actual rational numbers.

And later on I did waste far too much time,

chasing things like that.

How do you do precise arithmetic with rational numbers?

And it always blows up eventually,

exponentially as you do enough.

- So, these kind of things are impossible with computers?

- So they're possible.

Again, there are paths to doing it,

but you can't fit them conveniently in any of the numbers.

You need to start using big nums

and different factor trackings of different things.

- Right, so if you have any elements of OCD

and you wanna do something perfectly,

you're screwed if you're working with floating point.

- Yeah.

- So, you had to deal with this for the first time.

- And there were lots of challenges there about like,

okay, they build this cool thing

and the way the BSP trees work is it basically takes

the walls and it carves other walls

by those walls in this clever way that you can then

take all of these fragments and then you can for sure

from any given point get an ordering

of everything in the world.

And you can say, this goes in front of this,

goes in front of this,

all the way back to the last thing.

And that's super valuable for graphics

where kind of a classic graphics algorithm would be,

painter's algorithm.

You paint the furthest thing first and then the next thing

and then the next thing,

and then it comes up and it's all perfect for you.

That's slow because you don't wanna have

to have drawn everything like that.

But you can also flip it around

and draw the closest thing to you

and then if you're clever about it,

you can figure out what you need to draw

that's visible beyond that.

- And that's what BSP trees allow you to do.

- Yeah, so it's combined with a bunch of other things,

but it gives you that ordering.

It's a clever way of doing things.

And I remember I had learned this from,

one of my graphics bible at the time,

a book called "Foley and van Dam."

And again, it was a different world back there.

There was a small integer number of books

and this book that,

this book that was,

it was big fat college textbook

that I had read through many times.

I didn't understand everything in it.

Some of it wasn't useful to me,

but they had the little thing about finite orderings

of you draw little t-shaped thing

and you can say you can make a fixed ahead of time order

from this and you can generalize this with the BSP trees.

And I got a little bit more information about that

and it was kind of fun.

Later while I was working on Quake,

I got to meet Bruce Naer,

who was one of the original researchers

that developed those technologies for academic literature.

And that was kind of fun.

But I was very much just finding a tool

that can help me solve what I was doing.

And I was using it in this very crude way

in a two dimensional fashion, rather than the general 3D.

The Epsilon problems got much worse in Quake

and dimensional when things angle in every way.

But eventually I did sort out how to do it reliably on Doom.

There were still a few edge cases in Doom

that were not absolutely perfect,

where they even got terminologies in the communities.

Like when you got to something where it was messed up,

it was a hall of mirrors effect because you'd sweep by

and it wouldn't draw something there

and you would just wind up with the leftover remnants

as you flipped between the two pages.

But BSP trees were important for it,

but it's again worth noting that after we did Doom,

our major competition came

from Ken Silverman's build Engine,

which was used for Duke Newcomb 3D

and some of the other games for 3D realms.

And he used a completely different technology,

nothing to do with BSP trees.

So, there's not just a one true way of doing things.

There were critical things about

to make any of those games fast,

you had to separate your drawing into,

you drew vertical lines

and you drew horizontal lines,

just kind of changing exactly what you would draw with them.

That was critical for the technologies at that time.

And like all the games that were kind of like that,

wound up doing something similar,

but there were still a bunch of other decisions

that could be made.

And we made good enough decisions on everything on Doom.

We brought in multiplayer significantly

and it was our first game that was designed to be modified

by the user community

where we had this whole setup of our WAD files and PWADs

and things that people could build with tools

that we released to them.

And they eventually rewrote to be better than

what we released.

But they could build things

and you could add it to your game

without destructively modifying it,

which is what you had to do in all the early games.

You literally hacked the data files

or the executable before,

while Doom was set up in this flexible way

so that you could just say, run the normal game

with this added on on top

and it would overlay just the things

that you wanted to there.

- Would you say that Doom

was kind of the first true 3D game that you created?

- So, no, it's still,

Doom would usually be called a two and a half D game

where it had three dimensional points on it.

And this is another one of these kind of pedantic things

that people love to argue about,

about what was the first 3D game I still like

and like every month probably I hear from somebody about,

well, was Doom really a 3D game or something?

And I give the the point

where characters had three coordinates.

So, you had like an X, Y, and Z,

the Kakademon could be coming in very high

and come down towards you.

The walls had three coordinates on them.

So, on some sense it's a 3D game engine,

but it was not a fully general 3D game engine.

You could not build a pyramid in Doom

because you couldn't make a sloped wall,

which was slightly different

where in that previous shadow caster game,

I couldn't have Vertexes and have a sloped floor there.

But the changes that I made for Doom to get higher speed

and a different set of flexibility traded away that ability.

But you literally couldn't make that,

you could make different heights of passages,

but you could not make a bridge over another area.

You could not go over and above it.

So, that's more, it still had some 2D limitations to it.

- That's more about the building,

versus the actual experience,

'cause the experience is.

- It felt like things would come at you,

but again, you couldn't look up either.

- [Lex] Right.

- You could only pitch,

it was four degrees of freedom,

rather than six degrees of freedom.

You did not have the ability to tilt your head this way

or pitch up and down.

- So, that takes us to Quake.

What was the leap there?

What was some fascinating technical challenges

and there were a lot or not challenges,

but innovations that you've come up with.

- So, Quake was kind of the first thing

where I did have to kind of come face to face

with my limitations.

Where it was the first thing

where I really did kind of give it my all

and still come up a little bit short

in terms of what and when I wanted to get it done.

And the company ran had some serious stresses,

through the whole project.

And we bid off a lot.

So, the things that we set out to do was,

it was going to be really a truth 3D engine

where it could do six degree of freedom.

You could have all the viewpoints,

you could model anything.

It had a really remarkable new lighting model

with the surface caching and things.

That was one of those

where it was starting to do some things

that they weren't doing even on the very high end systems.

And it was going to be completely programmable

in the modding standpoint,

where the thing that you couldn't do in Doom,

you could replace almost all of the media,

but you couldn't really change the game.

There were still some people that

were doing the hack setting of the executable,

they hacked things

where you could change a few things about rules

and people made some early capture the flag type things

by hacking the executable,

but it wasn't really set out to do that.

Quake was going to have its own programming language

that the game was gonna be implemented in it,

# Chapter 12

you could model anything.

It had a really remarkable new lighting model

with the surface caching and things.

That was one of those

where it was starting to do some things

that they weren't doing even on the very high end systems.

And it was going to be completely programmable

in the modding standpoint,

where the thing that you couldn't do in Doom,

you could replace almost all of the media,

but you couldn't really change the game.

There were still some people that

were doing the hack setting of the executable,

they hacked things

where you could change a few things about rules

and people made some early capture the flag type things

by hacking the executable,

but it wasn't really set out to do that.

Quake was going to have its own programming language

that the game was gonna be implemented in it,

and that would be able to be overwritten,

just like any of the media.

Code was going to be data for that.

And you would be able to have expansion pacs

that changed fundamental things and mods and so on.

And the multiplayer was gonna be playable over the internet.

It was going to support a client server,

rather than peer to peer.

So, we had the possibility of supporting larger numbers

of players in disparate locations

with this full flexibility of the programming overrides

with full six degree of freedom modeling and viewing

and with this fancy new light mapped,

kind of surface caching side.

It was a lot.

And this was one of those things that if I could go back

and tell younger me to do something differently,

it would've been to split those innovations up

into two phases in two separate games.

- What would be phase one and phase two?

- So, it probably would've been,

taking the Doom rendering engine

and bringing in the TCP IP client server.

- [Lex] Focusing on the multiplayer.

- And the Quake C,

or would've been Doom C programming language there.

So, I would've split that into programming language

and networking with the same Doom engine,

rather than forcing everybody to go towards

the Quake Engine,

which really meant getting a pentium,

while it ran on a 486.

It was not a great experience there.

We could have made more people happier

and gotten two games done in 50% more time.

- So, speaking of people happier,

our mutual friend Joe Rogan,

it seems like the most important moment of his life

is centered around Quake.

So, it was a definitive part of his life.

So, would he agree with your thinking

that they should split?

So, he as a person who loves Quake

and played Quake a lot,

would he agree that you should have done the Doom engine

and focus on the multiplayer for phase one

or in your looking back

is the 3D world that Quake created

was also fundamental to the enriching experience?

- So, I would say that what would've happened is,

you would've had a Doom-looking but Quake feeling game,

eight months earlier

and then maybe six months after Quake actually shipped,

then there would've been the full running

on a Pentium,

six degree of freedom graphics engine type things there.

So, it wouldn't have been there,

it would've been something amazingly cool earlier

and then something even cooler somewhat later

where I would much rather in have gone

and done two one year development efforts,

cycle them through,

be a little more pragmatic about that,

rather than killing us ourselves

on the whole quake development.

But I would say it's obviously things worked out well

in the end, but looking back and saying,

how would I optimize and do things differently?

That did seem to be a clear case

where going ahead and we had enormous momentum on Doom,

we did Doom Two as the kind of commercial boxed version,

after our shareware success with the original,

but we could have just made another Doom game.

Adding those new features in it would've been huge.

We would've learned all the same lessons, but faster

and it would've given six degree of freedom

and Pentium class systems a little bit more time

to get mainstream,

because we did cut out a lot of people

with the hardware requirements for Quake.

- Was there any dark moments for you personally,

psychologically in having such harsh deadlines

and having to also meet difficult technical challenges?

- So, I've never really had really dark black places.

I mean, I can't necessarily put myself

in anyone else's shoes,

but I understand a lot of people have significant challenges

with kind of their mental health and wellbeing.

And I've been super stressed.

I've been unhappy as a teenager in various ways,

but I've never really gone to a very dark place.

I just seem to be largely immune

to what really wrecks people.

I mean, I've had plenty of time

when I'm very unhappy and miserable about something,

but it's never hit me.

Like, I believe it winds up hitting some other people.

I've born up well under whatever stresses,

have kind of fallen on me.

And I've always coped best on that when all I need to do

is usually just kind of bear down on my work.

I pull myself out of whatever hole I might be slipping into

by actually making progress.

I mean, maybe if I was in a position

where I was never able to make that progress,

I could have slid down further.

But I've always been in a place where,

okay, a little bit more work.

Maybe I'm in a tough spot here,

but I always know if I just keep pushing,

eventually I break through and I make progress.

I feel good about what I'm doing.

I am and that's been enough for me so far in my life.

- Have you seen it in the distance,

like ideas of depression or contemplating suicide?

Have you seen those things far?

- So, what was interesting when I was a teenager,

I was probably on some level a troubled youth.

I was unhappy most of my teenage years.

I really, I wanted to be on my own,

doing programming all the time.

As soon as I was 18, 19, even though I was poor,

I was doing exactly what I wanted and I was very happy.

But high school was not a great time for me.

And I had a conversation with like the school counselor

and they're kind of running their script.

It's like, okay, is kind of a weird kid here,

let's carefully probe around.

It's like do you ever think about ending it all?

I'm like, no, of course not.

Never, not at all.

I this is temporary, things are going to be better.

- [Lex] Wow.

- And that's always been kind of the case for me.

And obviously that's not that way for everyone

and other people do react differently.

- What was your escape from the troubled youth?

Like music, video games, books?

How did you escape from a world

that's full of cruelty and suffering and that's absurd.

- Yeah, I mean, I was not a victim of cruelty and suffering.

It's like I was an unhappy,

somewhat petulant youth in my point

where I'm not putting myself up

with anybody else's suffering,

but I was unhappy objectively.

And I am, the things that I did

that very much characterized my childhood were,

I had books, comic books,

Dungeons and Dragons, arcade games, video games.

Like some of my fondest childhood memories

are the convenience stores,

the 7-Elevens and QuikTrips,

because they had a spinner rack of comic books

and they had a little side room with two

or three video games, arcade games in it.

And that was very much my happy place,

if I could,

I get my comic books and if I could go to a library

and go through those,

the little 000 section where computer books

were supposed to be.

And there were a few sad little books there,

but still just being able to sit down and go through that.

And I read a ridiculous number of books,

both fiction and nonfiction as a teenager.

And my rebel my rebelling in high school

was just sitting there with my nose in a book,

ignoring the class.

And through lots of it.

And teachers had a range of reactions to that.

Some more accepting of it than others.

- I'm with you on that.

So, let us return to Quake for bit

with the technical challenges.

What everything together

from the networking to the graphics.

What are some things you remember

that were innovations you had to come up

with in order to make it all happen?

- Yeah, so there were a bunch of things on Quake

where on the one hand,

the idea that I built my own programming language

to implement the game in,

looking back and I try to tell people,

it's like every high level programmer sometime

in their career goes through

and they invent their own language.

It just seems to be a thing that's pretty broadly done.

People will be like,

I'm gonna go write a computer programming language.

And I don't regret having done it.

But after that, I switched from Quake C,

my quirky little,

pseudo object entity-oriented language there.

Quake Two went back to using DLLs with C

and then Quake Three I implemented my own C interpreter

or compiler, which was a much smarter thing to do

that I should have done originally for Quake.

But building my own language was an experience,

I learned a lot from that.

And then there was a generation of game programmers

that learned programming with Quake C,

which I feel kind of bad about,

because I mean we give JavaScript a lot of crap,

but Quake C was nothing to write home about there,

but it allowed people to do magical things.

You get into programming,

not because you love the the BNF syntax of a language,

it's because the language lets you do something

that you cared about.

- And here is very much you could do something

in a whole beautiful three-dimensional world.

- Yeah and the idea and the fact that the code

for the game was out there, you could say,

I like the shotgun,

but I want it to be more badass.

You go in there and say,

okay, now it does 200 points damage.

And if you go around with a big grin on your face,

blowing up monsters all over the game.

So yeah, it is not what I would do today going back

with that language, but that was a big part of it,

learning about the networking stuff,

because it's interesting

where I learn these things by reading books.

So, I would get a book on networking,

find something I read all about it and learn,

okay, packets they can be,

out of order lost or duplicated.

These are all the things that can theoretically happen

to packets.

So, I wind up spending all this time thinking about

how do we deal about all of that?

And it turns out, of course in the real world,

those are things that yes,

theoretically can happen with multiple routes,

but they really aren't things

that you're 99.999% of your packets have to deal with.

So, there was learning experiences about lots of that

and like why when TCP is appropriate versus UDP

and how if you do things in UDP,

you wind up reinventing TCP badly in almost all cases.

So, there's good arguments for using both

for different parts of the game process transitioning

from level to level and all.

But the graphics were the showcase

of what Quake was all about.

It was this graphics technology that nobody had seen there.

And it was a while before,

there were competitive things out there

and it went a long time internally really not working

where we were even building levels

where the game just was not at all shippable

with large fractions of the world,

like disappearing,

not being there or being really slow in various parts of it.

And it was this act of faith.

It's like, I think I'm gonna be able to fix this.

I think I'm gonna be able to make this work.

And lots of stuff changed

where the level designers would build something

and then have to throw it away

as something fundamental the kind of graphics

or level technology change.

And so there were two big things

that contributed to making it possible at that timeframe.

Two new things.

There was certainly hardcore optimized,

low level assembly language.

And this was where I had hired Michael Abrash,

away from Microsoft,

and he had been one of my early inspirations

where that back in the soft softest days,

the library of magazines that they had,

some of my most treasured ones

were Michael Abrash's articles in "Dr. Dobbs journal."

And it was amazing,

after all of our success in Doom,

we were able to kind of hit him up and say,

"Hey, we'd like you to come work at id Software."

And he was in the senior technical role at Microsoft

and he was on track for,

and this was right when Microsoft was starting to take off

and I did eventually convince him that

what we were doing was gonna be really amazing with Quake.

It was going to,

it was gonna be something nobody had seen before.

It had these aspects of what we were talking about.

And we had Metaverse talk back then.

We had read "Snow Crash"

and we knew about this

and Michael was big into the science fiction

and we would talk about all that and kind of spin this tail.

And it was some of the same conversations

that we have today about the Metaverse,

about how you could have different areas linked together

by portals and you could have user generated content

and changing out all of these things.

- So, you really were created in the Metaverse with Quake?

- And we talked about things like,

used to be advertised as a virtual reality experience.

That was the first wave of virtual reality was

in the late '80s and early '90s.

You had like the "Lawnmower Man" movie

and you had Time and Newsweek,

talking about the early VPL headsets.

And of course that cratered so hard

that people didn't wanna look at virtual reality

for decades afterwards where it was just,

it was smoke and mirrors.

It was not real

in the sense that you could actually do something real

and valuable with it.

But still we had that kind of common set of talking points

and we were talking about what these games could become

and how you'd like to see people,

building all of these creative things,

because we were seeing an explosion

of work with Doom at that time

where people were doing amazingly cool things.

Like we saw cooler levels

than we had built coming out of the user community.

And then people finding ways to change

the characters in different ways.

And it was great.

And we knew what we were doing in Quake

was removing those last things.

There was some quirky things with a couple of the data types

that didn't work right for overriding.

And then the core thing about the programming model,

and I was definitely going to hit all of those in Quake,

but the graphics side of it was,

it was still,

I knew what I wanted to do

and it was one of these hubris things where it's like,

well, so far I've been able to kind of kick everything

that I set out to go do.

But Quake was definitely a little bit more

than could be comfortably chewed at that point.

But Michael was one of the strongest programmers

and graphics programmers that I knew,

and he was one of the people that I trusted

to write assembly code better than I could.

And there's a few people that I can point to,

about things like this where I'm a world class optimizer.

I mean, I make things go fast,

but I recognize there's a number of people

that can write tighter assembly code,

tighter SIMD code or tighter CUDA code than I can write.

My best strengths are a little bit more at the system level.

I mean, I'm good at all of that,

but the most leverage comes

from making the decisions that are a little bit higher up

where you figure out how to change your large scale problems

# Chapter 13

and it was one of these hubris things where it's like,

well, so far I've been able to kind of kick everything

that I set out to go do.

But Quake was definitely a little bit more

than could be comfortably chewed at that point.

But Michael was one of the strongest programmers

and graphics programmers that I knew,

and he was one of the people that I trusted

to write assembly code better than I could.

And there's a few people that I can point to,

about things like this where I'm a world class optimizer.

I mean, I make things go fast,

but I recognize there's a number of people

that can write tighter assembly code,

tighter SIMD code or tighter CUDA code than I can write.

My best strengths are a little bit more at the system level.

I mean, I'm good at all of that,

but the most leverage comes

from making the decisions that are a little bit higher up

where you figure out how to change your large scale problems

so that these lower level problems

are easier to do or it makes it possible to do them

in a uniquely fast way.

So, most of my big wins in a lot of ways from,

all the way from the early games through VR

and the aerospace work that I'm doing

and or did and hopefully the AI work

that I'm working on now,

is finding an angle on something

that means you trade off something

that you maybe think you need,

but it turns out you don't need.

And by making a sacrifice in one place,

you can get big advantages in another place.

- Is it clear at which level of the system

those big advantages can be gained?

- It's not always clear.

And that's why the thing that,

that I try to make one of my core values

and I proselytize to a lot of people is,

trying to know the entire stack,

trying to see through everything that happens.

And it's almost impossible on,

like the web browser level of things

where there's so many levels to it,

but you should at least understand what they all are,

even if you can't understand,

all the performance characteristics at each level.

But it goes all the way down to literally the hardware.

So, what is this chip capable of

and what is this software that you're writing capable of?

And then when this architecture you put on top of that,

then the ecosystem around it,

all the people that are working on it.

So, there are all these decisions

and they're never made in a globally optimal way,

but sometimes you can drive a thread

of global optimality through it.

You can't look at everything.

It's too complicated.

But sometimes you can step back up

and make a different decision.

And we kind of went through this on the graphics side

on Quake where in some ways

it was kind of bad

where Michael would spend his time writing,

like I'd rough out the basic routines,

like, okay, here's our span rusterizer

and he would spend a month writing this,

beautiful cycle optimized piece of assembly language

that does what I asked it to do.

And he did it faster than like my original code would do

or probably what I would be able to do even

if I had spent that month on it.

But then we'd have some cases when I'd be like, okay,

well I figured out at this higher level,

instead of drawing these in a painter's order here,

I do a span buffer and it cuts out 30% or 40%

of all of these pixels,

but it means you need to rewrite,

kind of this interface of all of that.

And I could tell that wore on him a little bit,

but in the end it was the right thing to do

where we wound up changing that rasterization approach

and we wound up with a super optimized assembly language,

core loop and then a good system around,

which minimized how much that had to be called.

- And so in order to be able to do this,

kind of system level thinking,

whether we're talking about game development,

aerospace, nuclear energy, AI, VR,

you have to be able to understand the hardware,

the low level software, the high level software,

the design decisions,

the whole thing, the full stack of it.

- Yeah and that's where a lot of these things,

become possible when you're really,

when you're bringing the future forward.

I mean there's a pace that everything,

just kind of glides towards where we have a lot of progress

that's happening at such a,

so many different ways.

You kind of slide towards progress,

just left to your own programs just get faster

for a while it wasn't clear

if they were gonna get fatter,

more than they get quicker than they get faster

and it cancels out.

But it is clear now in retrospect now,

programs just get faster

and have gotten faster for a long time.

But if you wanna do something,

like back at that original talking about scrolling games,

say what this needs to be five times faster,

well we can wait six years and just,

it'll naturally get that much faster at that time.

Or you come up with some really clever way of doing it.

So, there are those opportunities like that

in a whole bunch of different areas.

Now, most programmers don't need to be thinking about that.

There's not that many,

there's a lot of opportunities for this,

but it's not everyone's workaday type stuff.

So, everyone doesn't have to know how all these things work.

They don't have to know how their compiler works,

how the processor chip manages cash eviction

and all these low level things.

But sometimes there are powerful opportunities

that you can look at and say,

we can bring the future five years faster.

We can do something that,

wouldn't it be great if we could do this?

Well, we can do it today

if we make a certain set of decisions.

And it is in some ways smoke and mirrors

where you say it's like,

Doom was a lot of smoke and mirrors

where people thought it was more capable

than it actually was,

but we picked the right smoke and mirrors to deploy

in the game where by doing this,

people will think that it's more general,

if we are gonna amaze them with what they've got here

and they won't notice that it doesn't do these other things.

So, smart decision making at that point,

that's where that kind of global holistic top-down view

can work.

And I'm really a strong believer

that technology should be sitting at that table,

having those discussions,

because you do have cases where you say,

well you wanna be the Jonathan Ivy or whatever,

where it's a pure design solution.

And in some cases now

where you truly have almost infinite resources.

Like if you're trying to do a scrolling game on the PC now,

you don't even have to talk to a technology person.

You can just have,

any intern can make that go run as fast as it needs to there

and it can be completely design-based.

But if you're trying to do something that's hard,

either that can't be done for resources like VR

on a mobile chip set

or that we don't even know how to do yet,

like artificial general intelligence,

it's probably going to be a matter of coming at it

from an angle.

Like, I mean for AGI we have some of like,

some of the harder principles about how you can SI

or there are theoretical ways

that you can say this is the optimal learning algorithm

that can solve everything, but it's completely impractical.

You just can't do that.

So, clearly you have to make some concessions

for general intelligence

and nobody knows what the right ones are yet.

So, people are taking different angles of attack.

I hope I've got something clever to come up with

in that space.

- It's been surprising to me

and I think it perhaps it is a principle of progress

that smoke and mirrors somehow

is the way you build the future.

You kind of fake it till you make it

and you almost always make it.

And I think that's going to be the way we achieve AGI,

that's going to be the way we build consciousness

into our machines

is there's philosophers debate about the touring test

is essentially about faking it till you make it.

You start by faking it.

And I think that always leads to making it.

Because if we look at history-

- Arguments when as soon as people start talking about

and consciousness and Chinese rooms and things,

it's like I just check out,

I just don't think there's any value in those conversations.

It's just like, go ahead, tell me it's not gonna work.

I'm gonna do my best to try to make it work anyways.

- I don't know if you work with legged robots,

there's a bunch of these,

they sure as heck make me feel like they're cautious

in a certain way that's not here today,

but is you could see the kernel.

It's like the flame, the beginnings of a flame.

- We don't have line of sight,

but there's glimmerings of light in the distance

for all of these things.

- Yeah, I'm hearing murmuring in a distant room.

Well, let me ask you a human question here.

In the game design space,

you've done a lot of incredible work throughout,

but in terms of game design,

you have changed the world

and there's a few people around you that did the same.

So, famously there's some animosity,

there's much love,

but there's some animosity between you and John Romero,

what is at the core of that animosity and human tension.

- So there really hasn't been,

for a long time and even at the beginning it's like,

yes I did push Romero out of the company

and this is one of the things that I look back,

if I could go back telling my younger self,

some advice about things,

the original founding kind of corporate structure

of id Software really led to a bunch of problems.

We started off with us as equal partners

and we had a buy sell agreement,

because we didn't want outsiders to be telling us

what to do inside the company.

And that did lead to a bunch of the problems

where I was sitting here going,

it's like, alright, I'm working harder than anyone.

I'm doing these technologies,

nobody's done before, but we're all equal partners

and then I see somebody that's not working as hard.

And I mean, I can't say I was the most mature about that.

I was 20 something years old

and it did bother me when I'm like,

everybody, okay, we need all pull together

and we've done it before.

Everybody we know we can do this if we get together

and we grind it all out.

But not everybody wanted to do that for all time

and I was the youngest, one of the crowd there.

I had different sets of kind of backgrounds and motivations

and left at that point where it was all right,

either everybody has to be contributing,

like up to this level or they need to get pushed out,

that was not a situation.

And I look back on it

and now we pushed people outta the company

that could have contributed

if there was a different framework for them

and the modern kind of Silicon Valley,

like let your stock vest over a time period

and maybe it's non-voting stock

and all those different things.

We knew nothing about any of that.

I mean, we didn't know what we were doing in terms

of corporate structure or anything.

- So, if you think the framework was different,

some of the human tension could have been a little bit of-

- It almost certainly would have.

I mean I look back at that

and it's like even trying to summon up in my mind it's like,

I know I was really, really angry about,

like Romero not working as hard as I wanted him to work

or not carrying his load on the design for Quake

and coming up with things there.

But he was definitely doing things.

He made some of the best levels there.

He was working with some of our external teams,

like Raven on the licensing side of things.

But there were differences of opinion about it.

But he landed right on his feet.

He went and he got $20 million from IDOs

to go do Ion Storm and he got to do things his way

and spun up three teams simultaneously,

because that was always one of the challenging things

in at id,

where we were doing these single string,

one project after another.

And I think some of them, wanted to grow the company more.

And I didn't because I knew people that were saying that,

"Oh, companies turned to shit when you got 50 employees."

It's just a different world there.

And I loved our little dozen people working on the projects,

but you can look at it and say,

"Well, business realities matter."

It's like, you're super successful here

and we could take a swing and a miss on something,

but you do it a couple times and you're outta luck.

There's a reason companies try to have,

multiple teams running at one time.

And so that was again,

something I didn't really appreciate back then.

- So, if you look past all that,

you did create some amazing things together.

What did you love about John Romero?

What did you respect and appreciate about him?

What did you admire about him?

What did you learn from him?

- When I met him,

he was the coolest programmer I had ever met.

He had done all of this stuff.

He had made all of these games.

He had worked at,

one of the companies that I thought was the coolest

at Origin Systems and he knew all this stuff.

He made things happen fast and he could,

he was also kind of a polymath about this

where he could do,

he made his own, he drew his own art,

he made his own levels as well as,

he worked on sound design systems on top

of actually being a really good programmer.

And we had we went through a little,

it was kind of fun where one of the early things that we did

where there was kind of the young buck bit going in

where I was the new guy and he was the,

he was the top man programmer at the Soft Disc Area.

And eventually we had sort of a challenge over the weekend

that we were gonna like race to implement this game

to port one of our PC games down to the Apple II.

And that was where we finally kind of became clear,

it's like, okay, CarMax stands a little bit apart

on the programming side of things,

but Romero then very gracefully moved into,

well he'll work on the tools,

he'll work on the systems,

do some of the game design stuff

as well as contributing on starting

to lead the design aspects of a lot of things.

So, he was enormously valuable in the early stuff

and so much of Doom

and even Quake have his stamp on it in a lot of ways.

But he wasn't at the same level of focus

that I brought to the work that we were doing there.

And he really did,

we hit such a degree of success

that it was all in the press about

that the Rockstar game programmers.

- I mean it's the Beatles problem.

- Yeah, I mean, he ate it up and he did personify,

there was the whole game developers

with Ferraris that we had there.

And I thought that led to some challenges there.

But so much of the stuff that was great

in the games did come from him.

And I would certainly not take that away from him.

And even after we parted ways and he took his swing

with IDOs in some ways he was like,

he was ahead of the curve with mobile gaming as well,

where one of his companies after IDOs

was working on feature phone game development

and I wound up doing some of that just,

before the iPhone crossing over into the iPhone phase there.

And that was something that clearly did turn out

to be a huge thing,

although he was too early

for what he was working on at that time.

We've had pretty cordial relationships

where I was happy to talk with him anytime I'd run into him

at a conference.

I haven't actually had some other people just say it's like,

oh, you shouldn't go over there

and give him the time of day

or felt that Masters of Doom was,

like portray played things up in a way

that I shouldn't be too happy with.

But I'm okay with all of that and I know.

- So you still got love in your heart?

- Yeah, I mean, I just talked with him like last year,

I guess it was even this year about mentioning

that I'm going off doing this AI stuff.

I'm going big into artificial intelligence

and he had bunch of ideas

for how AI is gonna play into gaming

and asked if I was interested in collaborating

and it's not in line with what I'm doing,

# Chapter 14

for what he was working on at that time.

We've had pretty cordial relationships

where I was happy to talk with him anytime I'd run into him

at a conference.

I haven't actually had some other people just say it's like,

oh, you shouldn't go over there

and give him the time of day

or felt that Masters of Doom was,

like portray played things up in a way

that I shouldn't be too happy with.

But I'm okay with all of that and I know.

- So you still got love in your heart?

- Yeah, I mean, I just talked with him like last year,

I guess it was even this year about mentioning

that I'm going off doing this AI stuff.

I'm going big into artificial intelligence

and he had bunch of ideas

for how AI is gonna play into gaming

and asked if I was interested in collaborating

and it's not in line with what I'm doing,

but I wish almost everyone the best.

I mean, I know I may not have parted on the best of terms

with some people,

but I was thrilled to see Tom Hall writing VR games now.

He wrote working on a game called "Demio,"

which is really an awesome VR game.

It's like "Dungeons and Dragons"

we all used to play "Dungeons and Dragons" together.

That was one of the things that was what we did on Sundays

in the early days,

I would Dungeon Master and they'd all play

and so it really made me smile seeing Tom involved

with an RPG game in virtual reality.

- You were the CTO of Oculus VR since 2013

and maybe lessen your involvement a bit in 2019.

Oculus was acquired by Facebook now Meta in 2014.

You've spoken brilliantly about both the low level details,

the experimental design

and the big picture vision of virtual reality.

Let me ask you about the Metaverse,

the big question here,

both philosophically and technically,

how hard is it to build the Metaverse?

What is the metaverse in your view,

you started with discussing

and thinking about quake as a kind of a metaverse

as you think about it today.

What is the metaverse the thing

that could create this compelling user value,

this experience that will change the world

and how hard is it to build it?

- So, the term comes from Neil Stevenson's book,

"Snow Crash," which many of us had read,

back in the '90s.

It was one of those kind of formative books.

And there was this sense that the possibilities

and kind of the freedom

and unlimited capabilities to build a virtual world,

that does whatever you want,

whatever you ask of it

has been a powerful draw for generations of developers,

game developers specifically

and people that are thinking,

about more general purpose applications.

So, we were talking about that back

in the Doom and Quake days about how do you wind up

with an interconnected set of worlds

that you kind of visit from one to another

and as webpage were becoming a thing,

you start thinking about

what is the interactive kind of 3D-based equivalent of this?

And there were a lot of really bad takes.

You had like VRML then, virtual reality markup languages.

And there's aspects like that came from people saying,

well what kind of capabilities should we develop

to enable this?

And that kind of capability-first work

has usually not panned out very well.

On the other hand,

we have successful games that started

with things like Doom and Quake

and communities that formed around those

and whether it was server lists in the early days

or literal portal link between different games

and then modern things

that are on completely different order

of magnitude like Minecraft and Fortnite

that have a hundred million plus users.

I still think that that's the right way to go

to build the Metaverse is you build something

that's amazing that people love

and people wind up spending all their time in,

because it's awesome

and you expand the capabilities of that.

- So, even if it's a very basic experience?

- As long as it's,

Minecraft is an amazing case study in so many things.

What's been able to be done with that

is really enlightening.

And there are other cases where,

like right now Roblox

is basically a game construction kit aimed at kids

and that was a capability first play

and it's achieving scale

that's on the same order of those things.

So, it's not impossible,

but my preferred bet would be,

you make something amazing that people love

and you make it better and better.

And that's where I could say we could have gone back

and followed a path kind of like that

in the early days if you just kind of take the same game.

Whether it's when Activision demonstrated

that you could make Call of Duty every year

and not only is it not bad, people kind of love it

and it's very profitable.

The idea that you could have taken something like that,

take a great game, release a new version every year

that lets the capabilities grow

and expand to start saying it's like,

okay, it's a game about running around and shooting things,

but now you can have, bring your media into it.

You can add persistence of social sense, signs of life

or whatever you want to add to it.

I still think that's quite a good position to take.

And I think that while Meta

is doing a bottoms up capability approach

with Horizon Worlds,

where it's a fairly general purpose,

creators can build whatever they want

in their sort of thing,

it's hard to compare and compete

with something like Fortnite,

which also has enormous amounts of creativity,

even though it was not designed originally

as a general purpose sort of thing.

So, we have examples on both sides.

Me personally,

I would've bet on trying to do entertainment,

valuable destination first and expanding from there.

- So, can you imagine the thing that will be kind of,

if we look back a couple of centuries from now

and you think about the experiences

that marked the singularity,

the transition in where most of our world moved

into virtual reality.

What do you think those experiences will look like?

- So, I do think it's gonna be kind of like

the way the web slowly took over

where you're the frog in the pot of water

that's slowly heating up

where having lived through all of that,

I remember when it was shocking to start

seeing the first website address on a billboard

when you're like,

"Hey, my computer world is infecting the real world."

This is spreading out in some way.

But there's still when you look back and say,

"Well, what made the web take off?"

And it wasn't a big bang sort of moment there,

it was a bunch of little things

that turned out not to even be the things

that are relevant now that brought them into it.

- Well I wonder if from,

I mean like you said, you're not a historian,

so maybe there's a historian out there

that could really identify that moment data-driven way.

It could be like MySpace or something like that.

Maybe the first major social network

that really reached into non-Geek World

or something like that.

- I think that's kind of the fallacy of historians though,

looking for some of those kind of primary dominant,

causes where so many of these things are like,

we see an exponential curve,

but it's not because like one thing is going exponential,

it's because we have hundreds of little sigmoid curves,

overlapped on top of each other

and they just happen to keep adding up

so that you've got something kind of going exponential

at any given point.

But no single one of them was the critical thing.

There were dozens and dozens of things.

I mean, seeing the transitions of stuff like

as obviously MySpace giving way to other things,

but even like blogging, giving way to social media

and getting resurrected in other guises

and things that happened there.

- And the memes with dancing baby GIF

or whatever all your base not belonged to us.

Whatever those early memes that led to the modern memes

and the humor on the different evolution

of humor on the internet

that I'm sure the historians will also write books about

from the different website that support,

that create the infrastructure for that humor,

like Reddit and all that kind of stuff.

- So, people will go back

and they will name firsts in critical moments.

But it's probably going to be a poor approximation

of what actually happens.

And we've already seen,

like in the VR space where it didn't play out

the way we thought it would

in terms of what was gonna be like when the modern era

of VR basically started with my E3 demo of Doom Three

on the Rift prototype.

So, we're like first person shooters in VR,

match made in heaven, right?

And that didn't work out that way at all.

They have the most comfort problems with it.

And then the most popular virtual reality app is Beat Saber,

which nobody predicted back then.

- What's that make you like from First Principles?

If you were to like reverse engineer that,

why are these like silly fun games the most?

- It actually makes very clear sense

when you analyze it from hindsight

and look at the engineering reasons

where it's not just that it was a magical, quirky idea.

It was something that played almost perfectly

to what turned out to be the real strengths of VR.

Where the one thing

that I really underestimated importance in VR

was the importance of the controllers.

I was still thinking we could do a lot more

with the Game Pad

and just the amazingness of taking any existing game.

Being able to move your head around

and look around that, that was really amazing.

But the controllers were super important.

But the problem is,

so many things that you do with the controllers just suck.

It feels like it breaks the illusion,

like trying to pick up glasses

with the controllers where you're like,

"Oh, use the grip button when you're kind of close

"and it'll snap into your hand."

All of those things are unnatural actions that you do them,

and it's still part of the VR experience.

But Beat Saber winds up playing only to the strengths.

It completely hides all the weaknesses of it,

because you are holding something in your hand,

you keep a solid grip on it the whole time.

It slices through things without ever bumping into things.

You never get into the point

where I'm knocking on this table, but in VR,

my hand just goes right through it.

So, you've got something that slices through.

So, it's never your brain telling you,

"Oh, I should have hit something."

You've got a lightsaber here.

It's just, you expect it to slice through everything.

Audio and music turned out to be a really powerful aspect

of virtual reality

where you're blocking the world off

and constructing the world around you

and being something that can run efficiently on,

even this relatively low powered hardware

and can have a valuable loop in a small amount of time.

Where a lot of modern games,

you're supposed to sit down and play it for an hour,

just to get anywhere.

Sometimes a new game takes an hour

to get through the tutorial level

and that's not good for VR for a couple reasons.

You do still have the comfort issues

if you're moving around at all,

but you've also got just discomfort from the headset,

battery lifespan on the mobile versions.

So, having things that do break down

into three and four minute windows of play,

that turns out to be very valuable

from a gameplay standpoint.

So, it winds up being kind of a perfect storm

of all of these things that are really good.

It doesn't have any of the comfort problems.

You're not navigating around, you're standing still.

All the stuff flies at you.

It has placed audio strengths.

It adds the whole,

the whole fitness in VR.

Nobody was thinking about that back at the beginning.

And it turns out that

that is an excellent daily fitness thing to be doing.

If you go play an hour of "Beat Saber"

or "Supernatural" or something that is legit solid exercise

and it's more fun than doing it,

just about any other way there.

- So, that's kind of the arcade stage of things.

If I were to say with my experience with VR,

the thing that I think is powerful is the,

maybe it's not here yet,

but the degree to which it is immersive

in the way that Quake is immersive,

it takes you to another world for me,

because I'm a fan of role playing games,

the elder scroll series like Sky Room

or even Daggerfall, it just takes you to another world.

And when you're not in that world, you miss not being there.

And then you just, you kind of wanna stay there forever.

'Cause life is shitty and you just wanna go to this place.

- Is that there was a time

when we were kind of asked to come up with like,

what's your view about VR?

And my pitch was that

it should be better inside the headset than outside.

It's the world as you want it.

- Yeah.

- And everybody thought that was dystopian

and like that's like,

"Oh, you're just gonna forget about the world outside."

And I don't get that mindset

where the idea that if you can make the world better

inside the headset than outside,

you've just improved the person's life

that's has a headset that can wear it.

And there are plenty of things

that we just can't do for everyone in the real world.

Everybody can't have Richard Branson's private island,

but everyone can have a private VR island

and it can have the things that they want on it.

And there's a lot of these kind

of rivalry goods in the real world

that VR can just be better at.

We can do a lot of things like that

that can be very, very rich.

So yeah, I want the, I think it's gonna be a positive thing,

this world where people want to go back into their headset

where it can be better than somebody

that's living in a tiny apartment

can have a palatial estate in virtual reality.

They can have all their friends

from all over the world come over and visit them

without everybody getting on a plane

and meeting in someplace and dealing

with all the other logistics hassles.

There is real value

in the presence that you can get for remote meetings.

It's all the little things that we need to sort out,

but those are things that we have line of sight on.

People that have been in like a good VR meeting,

using workrooms where you can say,

"Oh, that was better than a Zoom meeting."

But of course it's more of a hassle to get into it.

Not everyone has the headset.

Interoperability is worse.

You can't have you cap out at a certain number.

There's all these things that need to be fixed,

but that's one of those things you can look at

and say we know there's value there.

We just need to really grind hard,

file off all the rough edges and make that possible.

- So, you do think we have line of sight,

because there's a reason like,

I do this podcast in person for example.

It's doing it remotely, it it's not the same.

And if somebody were to ask me why it's not the same,

I wouldn't be able to write down exactly why.

But you're saying that it's possible,

whatever the magic is for in-person interaction,

that immersiveness of the experience,

we are almost there.

- Yes, so the idea like,

I am doing a VR interview with someone,

I'm not saying it's here right now,

but you can see glimmers of what it should be.

And we largely know what would need to be fixed

and improved to like you say,

there's a difference between at remote interview,

doing a podcast over Zoom or something and face-to-face.

There's that sense of presence, that immediacy,

the super low latency, responsiveness,

being able to see all the subtle things there,

just occupying the same field of view.

And all of those are things that we absolutely can do in VR.

And that simple case of a small meeting

with a couple people,

that's the much easier case than everybody thinks.

The ready player one multiverse

with a thousand people going across

# Chapter 15

that immersiveness of the experience,

we are almost there.

- Yes, so the idea like,

I am doing a VR interview with someone,

I'm not saying it's here right now,

but you can see glimmers of what it should be.

And we largely know what would need to be fixed

and improved to like you say,

there's a difference between at remote interview,

doing a podcast over Zoom or something and face-to-face.

There's that sense of presence, that immediacy,

the super low latency, responsiveness,

being able to see all the subtle things there,

just occupying the same field of view.

And all of those are things that we absolutely can do in VR.

And that simple case of a small meeting

with a couple people,

that's the much easier case than everybody thinks.

The ready player one multiverse

with a thousand people going across

a huge bridge to amazing places.

That's harder in a lot of other technical ways.

Not to say we can't also do that,

but that's further away and has more challenges.

But this small thing about being able to have a meeting

with one or a few people

and have it feel real, feel like you're there,

like you have the same interactions

and talking with them,

you get subtle cues

as we start getting eye and face tracking

and some of the other things on high-end headsets,

a lot of that is going to come over

and it doesn't have to be as good.

This is an important thing that people miss,

where there was a lot of people that,

especially rich people that would look at VR

and say it's like, oh, this just isn't that good.

And I'd say it's like,

well you've already been courtside backstage

and on pit row and you've done all of these experiences,

because you get to do them in real life.

But most people don't get to

and even if the experience is only half as good,

if it's something that they never would've gotten

to do before, it's still a very good thing.

And as we can push that number up over time.

It has a minimum viable value level

when it does something that is valuable enough to people,

as long as it's better inside the headset on any metric

than it is outside and people choose to go there,

we're on the right path and we have a value gradient

that I'm just always hammering on.

We can just follow this value gradient.

Just keep making things better,

rather than going for that one.

Close your eyes swing for the fences,

kind of silver bullet approach.

- Well, I wonder if there's a value gradient

for in-person meetings.

Because if you get that right,

I mean that would change the world.

- [John] Yeah.

- That it doesn't need to,

I mean you don't need ready player one.

but I wonder if there's that value gradient

you can follow along because if there is

and you follow it then there'll be a certain,

like phase shift at a certain point

where people will shift from Zoom to this.

I wonder what are the bottlenecks?

Is it software?

Is it hardware?

Is it all about latency?

So, I have big arguments internally,

about strategic things like that

where like the next headset that's coming out

that we've made various announcements about

is gonna be a higher end headset,

more expensive, more features.

Lots of people wanna make those trade-offs.

We'll see what the market has to say about

the exact trade-offs we've made here.

But if you wanna replace Zoom,

you need to have something that everybody has.

- [Lex] So, you want something you like cheaper.

- I like cheaper because also lighter and cheaper,

wind up being a virtuous cycle there where expensive

and more features tends to also lead towards heavier.

And it just kind of goes,

it's like, let's add more features.

The features are not,

they have physical presence and weight

and draw from batteries and all of those things.

So, I've always favored a lower end, cheaper,

faster approach.

That's why I was always behind the mobile side of VR,

rather than the higher end PC headsets.

And I think that's proven out well.

But there's, you always,

ideally we have a whole range of things,

but if you've only got one or two things,

it's important that those two things cover

the scope that you think is most important.

When we're in a world when it's like cell phones

and there's 50 of 'em on the market,

covering every conceivable ecological niche you want,

that's gonna be great,

but we're not gonna be there for a while.

- Where are the bottlenecks?

Is it the hardware or the software?

- Yeah, so right now you can play,

you can get workrooms on Quest

and you can set up these things

and it's a pretty good experience.

It's surprisingly good.

- I haven't tried it.

Is it surprisingly good.

- Yeah, the voice latency

is better on that than a lot better than a Zoom meeting.

So, you've got a better sense of immediacy there.

The expressions that you get

from the current hardware with just kind of your controllers

and your head is pretty realistic feeling

and you've got a pretty good sense of being there

with someone with that.

- Are these like avatars of people?

Like do you get to see their body

and they're sitting around a table?

- [John] Yeah.

- And it feels is better than Zoom?

- Better than, yeah, better than you'd expect for that.

It is definitely,

yeah, I'd say it's quite a bit better than Zoom

when everything's working right.

But there's still all the rough edges of,

the reason Zoom became so successful

is because they just nailed the usability of everything.

It's high quality with a absolutely first rate experience

and we are not there yet with any of the VR stuff.

I'm trying to push hard to get,

I keep talking about,

it's like it needs to just be one click

to make everything happen.

And we're getting there in our home environment,

not the whole work room's application,

but the main home where you can now kind of go over

and click an invite

and it still winds up taking five times longer

than it should.

But we're getting close to that

where you click there, they click on their button

and then they're sitting there

in this good presence with you.

But latencies need to get a lot better.

User interface needs to get a lot better.

Ubiquity of the headsets needs to get better.

We need to have a hundred million of 'em out there,

just so that everybody knows somebody

that uses this all the time.

- Well I think it's a virtuous cycle,

because I do think the interface is the thing that makes

or breaks this kind of revolution.

It's so interesting how, like you said, one click,

but it's also like how you achieve that one click.

I don't know what is, can I ask a dark question?

Maybe let's keep it outside of Meta,

but this is about Meta but also Google and big companies.

Are they able to do this kind of thing?

It seems like, let me put on my cranky old man hat,

they seem to not do a good job

of creating these user-friendly interfaces

as they get bigger and bigger as a company.

Like Google has created,

some of the greatest interfaces ever early on

and it's, I mean, creating Gmail,

just so many brilliant interfaces

and she seems to getting crappier and crappier at that.

Same with Meta, same with Microsoft.

It's just, it seems to get worse and worse at that.

I don't know what is it,

because you've become more conservative,

careful, risk averse.

Is that why?

Can you speak to that?

- So, it's been really eye-opening to me,

working inside a tech titan where I am.

I had my small companies

and then we are acquired by a mid-size game publisher

and then Oculus getting acquired by Meta.

And Meta has grown by a factor of many,

just in the eight years since the acquisition.

So, I did not have experience with this.

And it was interesting

because I remember like previously my benchmark

for kind of use of resources

was some of the government programs I interacted with

on the aerospace side.

And I remember thinking there was,

okay, there's an Air Force program

and they spent $50 million

and they didn't launch anything.

They didn't even build anything.

It was just kind of like they made a bunch of papers

and had some parts in a warehouse and nothing came of it.

It's like $50 million

and I've had to radically recalibrate

my sense of like how much money can be spent with-

- [Lex] Without a product at the end.

- Resources on the plus side VR has turned out,

we've built pretty much exactly what,

we just passed the 10-year mark then from my,

I like my first demo of the Rift

and if I could have said what I wanted to have,

it would've been a standalone,

inside out tracked 4K resolution headset

that could still plug into a PC for High-end rendering.

And that's exactly what we've got on Quest Two right now.

- Yes, first of all, let's pause on that

with me being cranky and everything.

What Meta achieved with Oculus and so on is incredible.

I mean this is this

when I thought about the future of VR,

this is what I imagined in terms of hardware I would say.

And maybe in terms of the experience as well,

but it's still not there somehow

- On the one hand we did kind of achieve it and win

and we've sold,

we're a success right now.

But the amount of resources that have gone into it,

it winds up getting floated up in accounting

where Mark did announce that they spent $10 billion a year,

like on Reality Labs.

Now Reality Labs covers a lot.

It was, VR was not the large part of it,

also had portal and Spark and the big AR research efforts

and it's been expanding out to include AI

and other things there where there's a lot going on there.

But $10 billion was just a number

that I had trouble processing.

I feel sick to my stomach,

thinking about that much money being spent.

But that's how they demonstrate commitment to this

where it's not more so than like yeah,

Google goes and cancels all of these projects,

different things like that while Meta

is really sticking with the funding of VR and AR

is still further out with it.

So, there's something to be said for that.

It's not just gonna vanish the work's going in.

I just wish it could be all those resources,

could be applied more effectively.

Yeah, because I see all these cases,

I point out these examples of how a third party

that we're kind of competing with in various ways,

there's a number of these examples

and they do work with a 10th of the people

that we do internally.

And a lot of it comes from,

yes, there's the small company

can just go do it while in a big company

you do have to worry about,

is there some SDK internally that you should be using,

'cause another team's making it.

You have to have your cross-functional group meetups

for different things.

You do have more concerns about privacy

or diversity and equity

and safety of different things,

parental issues and things that a small startup company

can just kind of cowboy off and do something interesting.

And there's a lot more that is a problem

that you have to pay attention to in the big companies.

But I'm not willing to believe

that we are within even a factor of two or four

of what the efficiency could be.

I am constantly kind of crying out for it's like,

we can do better than this.

- Yeah and you wonder what the mechanisms

to unlock that efficiency are.

There is some sense in a large company that,

like an individual engineer might not believe

that they can change the world.

Maybe you delegate a little bit of the responsibility

to be the one who changes the world in a big company,

I think.

But the reality is like the world will get changed

by a single engineer anyway.

So, whether inside Google or inside a startup,

it doesn't matter.

It's just like Google

and Meta needs to help those engineers believe.

They're the ones that are gonna decrease that latency,

it'll take one John Carmack like the 20-year-old Carmack

that's inside Meta right now to change everything.

- And I try to point that out and push people.

It's like, try to go ahead and when you see some,

because you get the silo mentality where you're like,

"Okay, I know something's not right over there,

"but I'm staying in my lane here."

And there's a couple people that I can think about

that are willing to just like hop all over the place

and man, I treasure them.

The people that are just willing to,

they're fearless, they will go over

and they will go rebuild the kernel

and change this distribution and go in

and hack the firmware over here to get something done right.

And that is relatively rare,

there's thousands of developers

and you've got a small handful that are willing to operate

at that level and it's potentially risky for them.

The the politics are real in a lot of that.

And I'm in the very much the privileged position of I am,

I'm more or less untouchable

where I've been dinged like twice for,

it's like you said something insensitive in that post.

And you should probably not say that,

but for the most part,

yes, I get away with I every week I'm posting something,

pretty loud and opinionated internally.

And I think that's useful for the company.

But yeah, it's rare to have a position like that

and I can't necessarily offer advice

for how someone can do that.

- Well, you could offer advice to a company in general

to give a little bit of freedom for the young, wild,

like the wildest ideas come from the young minds.

And so you need to give the young minds freedom to think big

and wild and crazy.

And for that they have to be opinionated.

They have to think crazy ideas and thoughts

and pursue them with a full passion,

without being slowed down by bureaucracy or managers

and all that kind of stuff.

Obviously startups really empower that.

But big companies could too.

And that's a design challenge for company,

for big companies to see how can you enable that?

How can you empower that?

- 'Cause the big company,

there are so many resources there.

And they do amazing things do get accomplished,

but there's so much more that could come out of that.

And I'm hope, I'm always hopeful.

I'm an optimist in almost everything.

I think things can get better.

I think that they can improve things

that you go through a path

and you're learning kind of what does and doesn't work.

And I'm not ready to be fatalistic about

the kind of the outcome of any of that.

- Me neither.

I know too many good people inside of those large companies

that are incredible.

You have a friendship with Elon Musk,

often when I talk to him,

he'll bring up how incredible of an engineer

and just a big picture thinker you are,

he has a huge amount of respect for you.

I have never been a fly on the wall,

between the discussion between the two of you.

I just wonder, is there something you guys debate,

argue about, discuss?

Is there some interesting problems

that the two of you think about?

You come from different worlds.

Maybe there's some intersection in aerospace,

maybe there's some intersection in your new efforts

in artificial intelligence in terms of thinking.

Is there something interesting

you could say about sort of the debates

that two of you have?

- So, I think in some ways

we do have a kind of similar background

where we're almost exactly the same age

and we had kind of similar programming backgrounds

on the personal computers

and even some of the books that we would read

and things that would kind of turn us into the people

that we are today.

And I think there is a degree of sensibility similarities

# Chapter 16

I just wonder, is there something you guys debate,

argue about, discuss?

Is there some interesting problems

that the two of you think about?

You come from different worlds.

Maybe there's some intersection in aerospace,

maybe there's some intersection in your new efforts

in artificial intelligence in terms of thinking.

Is there something interesting

you could say about sort of the debates

that two of you have?

- So, I think in some ways

we do have a kind of similar background

where we're almost exactly the same age

and we had kind of similar programming backgrounds

on the personal computers

and even some of the books that we would read

and things that would kind of turn us into the people

that we are today.

And I think there is a degree of sensibility similarities

where we kind of call bullshit on the same things

and kind of see the same opportunities

in different technology.

And there's that sense of,

I always talk about the speed of light solutions for things.

And he's thinking about kind of minimum manufacturing

and engineering and operational standpoints for things.

And so, I mean,

I first met Elon right at the start of the aerospace era

where I wasn't familiar with,

I was still in my game dev bubble.

I really wasn't familiar with all the startups

that were going and being successful

and what went on with PayPal

and all of his different companies.

But I met him as I was starting to do Armadillo Aerospace

and he came down with kind of his right hand propulsion guy.

And we talked about rockets what can we do with this?

And it was kind of specific things about like

how are our flight computers set up?

What are different propellant options?

What can happen with different ways

of putting things together?

And then in some ways,

he was certainly the biggest player

in the sort of alt space community

that was going on in the early 2000s.

He was the most well-funded, although,

his funding in the larger scheme of things compared to a,

like a NASA or something like that was really tiny.

It was a lot more than I had at the time.

But it was interesting.

I had a point years later when I realized,

okay, like my financial resources at this point

are basically what Elon's was

when he went all in on SpaceX and Tesla.

And I think in many corners he does not get the respect

that he should about being a wealthy person

that could just retire.

And he went all in where he was really going to,

he could have gone bust.

And there's plenty of people you look at the sad athletes

or entertainers that had all the money in the world

and blew it.

And he could have been the business case example of that.

But the things that he was doing,

space exploration, electrification of transportation,

solar city type things, these are big world level things.

And I have a great deal of admiration

that he was willing to throw himself

so completely into that because in contrast with myself,

I was doing Armadillo Aerospace with this tightly bounded,

it was John's crazy money at the time

that had a finite limit on it.

It was never going to impact me or my family

if it completely failed.

And I was still hedging my bets working

in software at the time

when he had been really all in there.

And I have a huge amount of respect for that.

And people do not,

the other thing I get irritated with is people that say

it's like, "Oh, Elon's just a business guy."

"He just got like,

"he was gifted the money

"and he's just kind of investing in all of this."

When he was really deeply involved

in a lot of the decisions, not all of 'em were perfect,

but he cared very much about engine material selection,

propellant selection.

And for years he'd be kind of telling me it's like,

get off that hydrogen peroxide stuff.

It's like liquid oxygen is the only proper oxidizer

for this.

And unlike the times that I've gone through the factories

with him,

we're talking very detailed things about like

how this weld is made,

how this subassembly goes together,

what are like startup shutdown behaviors

of the different things.

So, he is really in there at a very detailed level.

And I think that he is the best modern example now

of someone that tries to,

that can effectively micromanage some decisions on things,

on both Tesla and SpaceX to some degree

where he cares enough about it.

I worry a lot that he stretched too thin,

that you get Boring Company and Neuralink and Twitter

and all the other possible things there

where I know I've got,

I've got limits on how much I can pay attention to

that I have to kind of box off different amounts of time.

And I look back at like,

at my aerospace side of things,

it's like I did not go all in on that.

I did not commit myself at a level

that it would've taken to be successful there.

And yeah and it's kind of a weird thing,

just like having a discussion with him.

He's the richest man in the world right now.

But he operates on a level that is still very much

in my wheelhouse on a technical side of things.

- Doing that systems level type of thinking

where you can go to the low level details

and go up high to the big picture.

Do you think in aerospace arena in the next five, 10 years,

do you think we're gonna put a human on Mars?

Like what do you think is the interesting point.

- No, in fact, I made a bet with someone,

with a group of people kind of this about,

whether boots on Mars by 2030.

And this was kind of a fun story

because I was at an Intel sponsored event

and we had a bunch of just world class brilliant people

and we were talking about computing stuff,

but the after dinner conversation was like,

what are some other things?

How are they gonna go in the future?

And one of the ones tossed up on the whiteboard was like,

boots on Mars by 2030.

And most of the people in the room thought, yes.

They thought that like, SpaceX is kicking ass,

we've got all this possible stuff,

seems likely that it's gonna go that way.

And I said, no, I think less than 50% chance

that it's going to make it there.

And people were kind of like,

"Oh, why the pessimism or whatever."

And of course I'm an optimist at almost everything,

but for me to be the one kind of outlier saying,

no, I don't think so.

Then I started saying some of the things I said,

well, let's be concrete about it.

Let's bet $10,000 that it's not gonna happen.

And this was really a startling thing to see that I,

again, room full of brilliant people,

but as soon as like money came on the line

and they were like, do I wanna put $10,000 in?

I was not the richest person in the room.

There are people much better off than I was.

There's a spectrum.

But as soon as they started thinking it's like,

oh, I could lose money by keeping my position right now.

And all these engineers, they engaged their brain,

they started thinking it's like,

okay, launch windows, launch delays.

Like how many times would it take to get this right?

What historical precedents do we have?

And then it mostly came down to it's like,

well what about in transit by 2030?

And then what about I,

different things or would you hand would you go for 2032?

But one of the people did go ahead

and was optimistic enough to make a bet with me.

So, I have a $10,000 bet that by 2030,

I think it's gonna happen shortly thereafter.

I think there will probably be infrastructure

on Mars by 2030,

but I don't think that we'll have humans on Mars in 2030.

I think it's possible,

but I think it's less than a 50% chance.

So, I felt safe making that bet.

- Well I think you had an interesting point.

Correct me if I'm wrong, that's a dark one,

that should perhaps help people appreciate Elon Musk,

which is in this particular effort,

Elon is critical to the success.

SpaceX seems to be critical to 20th humans on Mars

by 2030 or thereabouts.

So, if something happens to Elon,

then all of this collapses.

- And this is in contrast to the the other $10,000 bet

I made kind of recently

and that was self-driving cars

at like a level five running around cities.

And people have kind of nitpicked that,

that we probably don't mean exactly level five,

but the guy I'm having the bet with is we're gonna be,

we know what we mean about this.

- [Lex] Jeff Atwood.

- Yeah, Coding horror and stack flow and all.

- [Lex] Yeah.

- But yeah, I mean it's just,

he doesn't think that people are gonna be riding

around in Robotaxis in 2030 in major cities.

Just like you take an Uber now

and think I think it will.

- [Lex] And you think you think it will.

- And the difference is everybody looks at this,

it's like, "Oh, but Tesla's been wrong for years."

They've been promising it for years and it's not here yet.

And the reason this is different than the bet

with Mars is Mars really is more than

is comfortable a bet on Elon Musk.

That is his thing and he is really going to move heaven

and earth to try to make that happen.

- And perhaps not even SpaceX.

- [John] Yeah. - Perhaps just Elon Musk.

- Yeah, because if Elon went away and SpaceX went public

and got a board of directors,

there are more profitable things they could be doing

than focusing on human presence on Mars.

So, this really is a sort of personal thing there.

And in contrast with that,

self-driving cars have a dozen credible companies,

working really hard.

And while yes,

it's going slower than most people thought it would,

betting against that is a bet against almost

the entire world

in terms of all of these companies

that have all of these incentives.

It's not just one guy's passion project.

And I do think that it is solvable.

Although I recognize

it's not a hundred percent chance because it's possible.

The long tail of self-driving problems winds up being

an AGI complete problem.

I think there's plenty of value to mine out of it

with narrow AI

and I think that it's going

to happen probably more so than people expect,

but it's that whole sigmoid curve where you over,

you overestimate the near term progress

and you underestimate the long-term progress.

And I think self-driving is gonna be like that.

And I think 2030 is still a pretty good bet.

- Yeah, unfortunately self-driving

is a problem that is safety critical.

Meaning that if you don't do it well, people get hurt.

- But the other side of that is people are terrible drivers.

So, it is not going to be,

that's probably gonna be the argument

that gets it through is like,

we can save 10,000 lives a year

by taking imperfect self-driving cars

and letting them take over

a lot of driving responsibilities.

It's like, was it 30,000 people a year die

in auto accidents right now in America?

And a lot of those are preventable.

And the problem is you'll have people

that every time a Tesla crashes into something,

you've got a bunch of people

that literally have vested interests shorting Tesla

to come out and make it the worst thing in the world.

And people will be fighting against that.

But optimist in me again, I think that we will have systems

that are statistically safer than human drivers

and we will be saving thousands

and thousands of lives every year

when we can hand over more of those responsibilities to it.

- I do still think as a person

who studied this problem very deeply

from a human side as well,

it's still an open problem how good/bad humans are driving.

It's a kind of funny thing we say about each other.

All humans suck at driving,

everybody except you, of course.

Like we think we're good at driving.

But after really studying it,

I think you start to notice,

'cause I've watched hundreds of hours

of humans driving with the projects of this kind of thing.

You've noticed that even with the distraction,

even with everything else,

humans are able to do some incredible things

with the attention.

Even when you're just looking at a smartphone,

just to get cues from the environment

to make less seconds decisions,

to use instinctual type of decisions

that actually save your ass time and time and time again

and are able to do that

with so much uncertainty around you

in such tricky dynamic environments.

I don't know,

I don't know exactly how hard is it

to beat that kind of skill of common sense reasoning.

- So, this is one of those interesting things

that there have been a lot of studies about how experts

in their field usually underestimate the progress

that's going to happen,

because an expert thinks about all the problems

they deal with and they're like,

damn, I'm gonna have a hard time solving all of this.

And they filter out the fact that they are one expert

in a field of thousands.

And you think about, yeah, I can't do all of that.

And you sometimes forget about the scope of the ecosystem

that you're embedded in.

And if you think back eight years,

very specifically the state of AI and machine learning,

where was that?

We had just gotten res nets probably at that point.

And you look at all the amazing magical things

that have happened in eight years

and they do kind of seem to be happening a little faster

in recent years also.

And you project that eight more years into the future

where again I think there's a 50% chance

we're gonna have signs of life of AGI,

which we can put through driver's ed if we need to,

to actually build self-driving cars.

And I think that the narrow systems are going

to have real value demonstrated well before then.

- So, signs of life in AGI,

you've mentioned that, okay, first of all,

you're one of the most brilliant people on this earth.

You could be solving a number of different problems,

as you've mentioned,

you mind was attracted to nuclear energy.

Obviously virtual reality with the metaverse

is something you could have a tremendous impact on.

- So, I do wanna say a quick thing about nuclear energy

where this is something that,

this so precisely feels like aerospace before SpaceX,

where from everything that I know about all of these,

the physics of this stuff hasn't changed.

And the reasons why things are expensive now

are not fundamental.

I somebody should be going

into a really hard Elon Musk style visions,

economical vision, not fusion,

where the fusion is the kind of the darling of people

that want to go and do nuclear,

because it doesn't have the taint that fission has

in a lot of people's minds.

But it's an almost absurdly complex thing

where nuclear fusion is,

you look at the tocomax

or any of the things that people are building

and it's doing all of this infrastructure,

just at the end of the day to make something hot,

so that you can then turn into energy,

through a conventional power plant

and all of that work,

which we think we've got line of sight on.

# Chapter 17

the physics of this stuff hasn't changed.

And the reasons why things are expensive now

are not fundamental.

I somebody should be going

into a really hard Elon Musk style visions,

economical vision, not fusion,

where the fusion is the kind of the darling of people

that want to go and do nuclear,

because it doesn't have the taint that fission has

in a lot of people's minds.

But it's an almost absurdly complex thing

where nuclear fusion is,

you look at the tocomax

or any of the things that people are building

and it's doing all of this infrastructure,

just at the end of the day to make something hot,

so that you can then turn into energy,

through a conventional power plant

and all of that work,

which we think we've got line of sight on.

But even if it comes out,

then you have to do all of that immensely complex,

expensive stuff just to make something hot.

Where nuclear fission is basically,

you put these two rocks together

and they get hot all by themselves.

That is just that much simpler.

It's just orders of magnitude simpler and the actual rocks,

the refined uranium is not very expensive.

It's a couple percent of the cost of electricity.

That's why I made that point where you could have something

which was five times less efficient than current systems.

And if the rest of the plant was a whole bunch cheaper,

you could still be super, super valuable.

- So, how much of the pie do you think could be solved

by nuclear energy by fission?

So, how much could it become the primary source

of energy on earth?

- It could be most of it,

like the reserves of uranium as it stands now,

could not power the whole earth.

But you get into breeder reactors and thorium

and things like that that you do for conventional fission.

There is enough for everything.

Now, I mean, solar photovoltaic has been amazing.

One of my current projects is working on an off-grid system

and it's been fun just kind of, again,

putting my hands on all the stripping the wires

and wiring things together and doing all of that

and just having followed that a little bit

from the outside over the last couple decades,

there's been semiconductor like magical progress

in what's going on there.

So, I'm all for all of that,

but it doesn't solve everything

and nuclear really still does seem like the smart money bet

for what you should be getting for baseband

on a lot of things.

And solar may be cheaper

for peaking over air conditioning loads during the summer

and things that you can push around in different ways.

But it's one of those things that's,

it's just strange

how we've had the technology sitting there,

but these non-technical reasons on the social optics of it

has been this major forcing function for something that,

really should be at the cornerstone

of all of the world's concerns with energy.

It's interesting how the non-technical factors,

have really dominated something

that is so fundamental to kind of the existence

of the human race as we know it today.

- And much of the troubles of the world,

including wars in different parts of the world,

like Ukraine is energy based

and yeah, it's just sitting right there to be solved.

That said, I mean to me personally,

I think it's clear that if AGI were to be achieved,

that would change the course of human history.

- So, AGI wise,

I was making this decision about

what do I want to focus on after VR

and I'm still working on VR regularly.

I spend a day a week kind of consulting with Meta

and Boz styles me, the consulting CTO

is kind of like the Sherlock Holmes that comes in

and consults on some of the specific tough issues.

And I'm still pretty passionate about all of that,

but I have been figuring out how to compartmentalize

and force that into a smaller box

to work on some other things.

And I did come down to this decision,

between working on economical nuclear fission

or artificial general intelligence

and the fission side of things.

I've got a bunch of interesting things going that way.

But it would take,

that would be a fairly big project thing to do.

I don't think it's needs to be as big as people expect.

I do think something original SpaceX sized,

you build it, power your building off of it,

and then the government I think will come around

to what you need to, everybody loves an existence proof.

I think it's possible somebody should be doing this,

but it's gonna involve some politics.

It's going to involve decent sized teams

and a bunch of this cross-functional stuff

that I don't love.

While the artificial general intelligence side of things,

it seems to me like this is the highest leverage moment

for potentially a single individual,

potentially in the history of the world

where the things that we know about the brain,

about what we can do with artificial intelligence.

Nobody can say absolutely on any of these things,

but I am not a madman for saying that it is likely

that the code for artificial general intelligence

is going to be tens of thousands of lines of code,

not millions of lines of code.

This is code that conceivably one individual could write,

unlike writing a new web browser or operating system.

And based on the progress that AI machine learning has made

in the recent decade,

it's likely that the important things

that we don't know are relatively simple.

There's probably a handful of things

and my bet is that I think

there's less than six key insights that need to be made.

Each one of them can probably be written

on the back of an envelope.

We don't know what they are,

but when they're put together in concert with GPUs at scale

and the data that we all have access to,

that we can make something that behaves like a human being

or like a living creature

and that can then be educated in whatever ways

that we need to get to the point

where we can have universal remote workers

where anything that somebody does mediated by a computer

and doesn't require physical interaction

that an AGI will be able to do.

We can already simulate the equivalent of the Zoom meetings

with avatars and synthetic deepfakes and whatnot.

We can definitely do that.

We have superhuman capabilities on any narrow thing

that we can formalize and make a loss function for.

But there's things we don't know how to do now,

but I don't think they are unapproachable hard.

Now, that's incredibly hubristic to say that it's like,

but I think that what I said a couple years ago

is a 50% chance that somewhere

there will be signs of life of AGI in 2030

and I've probably increased that slightly.

I may be at 55, 60% now,

because I do think there's a little sense

of acceleration there.

- So, I wonder what the

and by the way you also written that,

I bet with hindsight we'll find that clear antecedents

of all the critical remaining steps for AGI

are already buried somewhere

in the vast literature of today.

So, the ideas are already there.

- I think that's likely the case.

One of the things that appeals to so many people,

including me about the promise of AGI

is we know that we're only drinking from a straw

from the fire hose of all the information out there.

I mean, you look at just in a very narrowly bounded field,

like machine learning,

like you can't read all the papers

that come out all the time.

You can't go back and read all the clever things

that people did in the '90s or earlier

that people have forgotten about,

because they didn't pan out at the time

when they were trying to do them with 12 neurons.

So that this idea that,

yeah, I think there are gems buried

in some of the older literature

that was not the path taken by everything.

And you can see a kind of herd mentality

on the things that happen right now.

It's almost funny to see,

it's like, oh, Google does something

and OpenAI does something and Meta does something

and they're the same people that all talk to each other

and they're all one-upping each other

and they're all capable of implementing each other's work,

given a month or two after somebody

has an announcement of that.

But there's a whole world of possible approaches

to machine learning

and I think that we probably will in hindsight go back

and see it's like, yeah, that was kind of clearly predicted

by this early paper here

and this turns out that if you do this and this

and take this result from animal training

and this thing from neuroscience over here

and put it together

and set up this curriculum for them to learn in,

that that's kind of what it took.

You don't have too many people now that are still saying

it's not possible

or it's gonna take hundreds of years

and 10 years ago you would get,

you would get a collection of experts

and you would have a decent chunk on the margin

that either say not possible

or couple hundred years, might be centuries.

And the median estimate would be like 50, 70 years.

And it's been coming down

and I know with me saying eight years for something

that still puts me on the optimistic side,

but it's not crazy out in the fringes.

And just being able to look at that a Meta level,

about the trend of the trend of the predictions,

going down there,

the idea that something could be happening relatively soon.

Now, I do not believe in fast takeoffs.

That's one of the safety issues that people say.

It's like, oh, it's gonna go foom

and the AI's gonna take over the world.

There's a lot of reasons

I don't think that's a credible position.

And I think that we will go from a point

where we start seeing things that credibly look like,

look like animals behaviors

and have a human voice box wired into them.

It's like, I tried to get Elon to say,

it's like, you're your pig at neuralink.

Give it a human voice box

and let it start learning human words.

I think that,

I think animal intelligence is closer

to human intelligence than a lot of people like to think.

And I think that culture

and modalities of IO

are make the Gulf seem a lot bigger than it actually is.

There's just that smooth spectrum of how the brain developed

and cortexes and scaling of different things going on there.

- Cultural modalities of IO, yes languages,

the sort of loss in translation,

conceals a lot of intelligence.

And so when you're thinking about signs of life or AGI,

you're thinking about human interpretable signs.

- So, the example I give,

if we get to the point

where you've got a learning disabled toddler,

some kind of real special needs child

that can still interact with their favorite TV show

and video game and can be trained

and learn in some appreciably human-like way,

at that point you can deploy an army of engineers,

cognitive scientists, developmental education people

and you've got so many advantages there.

Unlike real education where you can do rollbacks

and AB testing

and you can find a golden path through a curriculum

of different things.

If you get to that point learning disabled toddler,

I think that it's gonna be a done deal.

- But do you think we'll know it when we see it?

So, there's been a lot

of really interesting general learning progress

from DeepMind, OpenAI a little bit too.

I tend to believe that Tesla autopilot,

deserves a lot more credit than is getting

for making progress on the general,

on sort of on doing the multitask learning thing

and increasing the number of tasks

and automating that process of sort of learning

from discovering the edge cases

and learning from the edge cases.

It's really approaching from a different angle,

the general learning problem of AGI,

but the more clear approach comes from DeepMind

where you have these kind of game situations

and you build systems there,

but I don't know, people seem to be quite.

- Yes, there will always be people

that just won't believe it and I fundamentally don't care.

I mean, I don't care if they don't believe it.

When it starts doing people's jobs and I mean,

I don't care about the philosophical zombie argument at all.

- Yes, absolutely, absolutely.

But do you think you will notice

that something special has happened here

and or because to me,

I've been noticing a lot of special things.

I think, you know, a lot of credit should go to DeepMind

for Alpha Zero that was truly special

through self play mechanisms achieve sort of solve problems

that used be thought unsolvable, like the game of go also,

I mean, protein folding starting to get into that space

where learning is doing.

At first, there's not, it wasn't end-to-end learning.

And so now it's end-to-end learning

of a very difficult previously thought unsolvable problem

of protein folding.

And so yeah,

where do you think would be a really magical moment for you?

- There have been incredible things happening

in recent years.

Like you say, all of the things

from DeepMind, OpenAI that have been

huge showpiece things, but when you really get down to it

and you read the papers

and you look at the way the models are going,

it's still like a feed forward.

You push something in, something comes out on the end,

I mean maybe there's diffusion models

or Monte Carlo tree rollouts and different things going on,

but it's not a being, it's not close to a being

that's going through a lifelong learning process.

- So you want something that kind of gives signs of a being,

like what's the difference between a neural network,

a feedforward neural network and a being?

- So fundamentally, the brain is a recurrent neural network

generating an action policy.

I mean, it's implemented on a biological substrate.

And it's interesting thinking about things like that

where we know fundamentally the brain

is not a convolutional neural network or a transformer.

Those are specialized things that are very valuable

for what we're doing,

but it's not the way the brain's doing.

Now, I do think consciousness

and AI in general is a substrate independent mechanism

where it doesn't have

to be implemented the way the brain is.

But if you've only got one existence proof,

there's certainly some value

in caring about what it says and does.

And so the idea that anything that can be done

with a narrow AI that you can quantify up a loss function

for or reward mechanism, you're almost certainly going

to be able to produce something

that's more resource effective to train and deploy

and use in an inference mode,

train a whole lot using an inference.

But a living being is gonna be something

that's a continuous, lifelong learned, task agnostic thing.

And while lot.

- So the lifelong learning is really important too,

and the long-term memory.

So memory is a big weird part of that puzzle.

- We've got and again,

I have all the respect in the world for the amazing things

that are being done now,

but sometimes they can be taken a little bit out of context

with things like there's some smoke and mirrors going on,

like the gato, the recent work,

the multitask learning stuff, it's amazing

that it's one model

that plays all the Atari games I am as well

as doing all of these other things.

But of course it didn't learn to do all of those.

It was instructed in doing that

by other reinforcement learners

# Chapter 18

train a whole lot using an inference.

But a living being is gonna be something

that's a continuous, lifelong learned, task agnostic thing.

And while lot.

- So the lifelong learning is really important too,

and the long-term memory.

So memory is a big weird part of that puzzle.

- We've got and again,

I have all the respect in the world for the amazing things

that are being done now,

but sometimes they can be taken a little bit out of context

with things like there's some smoke and mirrors going on,

like the gato, the recent work,

the multitask learning stuff, it's amazing

that it's one model

that plays all the Atari games I am as well

as doing all of these other things.

But of course it didn't learn to do all of those.

It was instructed in doing that

by other reinforcement learners

going through and doing that.

And even in the case of all the games, it's still going

with a specific hand-coded reward function in each

of those Atari games where it's not that, how does it?

It just wants to spend its summer afternoon playing Atari

because that's the most interesting thing for it.

So it's, again, not a general,

it's not learning the way humans learn.

And there's, I believe a lot of things that are challenging

to make a loss function for that you can train

through these existing conventional things.

We are gonna chip away at all the things that people do

that we can turn into narrow AI problems.

And billions, probably trillions of dollars

of value are gonna be created by that.

But there's still gonna be a set of things.

And we've got questionable cases like the self-driving car

where it's possible, it's not my bet,

but it's plausible

that the long tail could be problematic enough

that that really does require

a full on artificial general intelligence.

The counter argument is that data solves almost every,

everything's an interpolation problem

if you have enough data.

And Tesla may be able to get enough data

from all of their deployed stuff to be able

to work like that, but maybe not.

And there are all the other problems about,

like say you want to have a strategy meeting

and you want to go ahead

and bring in all of your remote workers and your consultants

and you want a world where some of those could be AIs

that are talking and interacting with you

in an area that is too murky

to have a crisp loss function.

But they still have things that on some level,

they're rewarded on some internal level

for building a valuable to humans kind of life

and ability to interact with things.

- See, I still think that self-driving cars solving

that problem will take us very far towards AGI.

You might not need AGI,

but I am really inspired by what Autopilot is doing.

Waymo, so some of the other companies,

I think Waymo leads the way there

is also really interesting,

but they don't have quite as ambitious of an effort in terms

of learning based sort of data hungry approach

to driving, which I think is very close to the kind of thing

that would take us far towards AGI.

- Yeah, and it's a funny thing

because as far as I can tell,

Elon is completely serious about all

of his concerns about AGI being an existential threat.

And I tried to draw him out to talk about AI

and he just didn't want to.

And I think that,

I get that little fatalistic sense from him and it's weird

because his company could very well be the leading company.

Leading towards a lot of that,

where Tesla being a super pragmatic company

that's doing things

because they really wanna solve this actual problem.

It's different vibe than the research oriented companies

where it's a great time to be an AI researcher.

You've got your pick of trillion dollar companies

that will pay you to kind

of work on the problems you're interested in.

But that's not necessarily driving hard towards

the core problem of AGI as something

that's going to produce a lot of value by doing things

that people currently do or would like to do.

- I mean, I have a million questions to you

about your ideas about AGI,

but do you think it needs to be embodied?

Do you think it needs to have a body to start

to notice the signs of life

and to develop the kind of system that's able to reason,

perceive the world in the way that an AGI should

and act in the world?

So should we be thinking about robots

or can this be achieved in a purely digital system?

- So I have a clear opinion on that

and that's that, no, it does not need

to be embodied in the physical world

where you could say most of my career

is about making simulated virtual worlds.

You know, in games or virtual reality.

And so on a fundamental level, I believe

that you can make a simulated environment that provides much

of the value of what the real environment does.

And restricting yourself

to operating at real time in the physical world

with physical objects, I think is an enormous handicap.

I mean, that's one of the real lessons driven home

by all my aerospace work is that reality

is a bitch in so many ways there,

where dealing with all the mechanical components,

like everything fails Murphy's Law,

even if you've done it right before on your fifth one,

it might come out differently.

So yeah, I think that anybody

that is all in on the embodied aspect of it,

they are tying a huge weight to their ankles.

And I think that I would almost count them out, anybody

that's making that a cornerstone of their belief about it,

I would almost write them off

as being worried about them getting to AGI first,

I was very surprised that Elon's big on the humanoid robots.

I mean like the NASA robot stuff was always

almost a gag line.

Like, what are you doing people?

- Well that's very interesting

'cause he has a very pragmatic view of that.

That's just a way

to solve a particular problem in a factory.

- Now I do think that once you have an AGI, robotic bodies,

humanoid bodies are going to be enormously valuable.

I just don't think they're helpful getting to AGI.

- Well he has a very sort of practical view,

which I disagree with and argue with him,

but it's a practical view that there's,

you could transfer the problem of driving

to the problem of robotic manipulation

because so much of it is perception.

It's perception and action,

and it's just a different context.

And so you can apply all the same kind

of data engine learning processes

to a different environment.

And so why not you apply it

to the humanoid robot environment?

But I think I do think that there's a certain magic

to the embodied robot.

- That may be the thing that finally convinces people.

- Yes.

- But again, I don't really care

that much about convincing people.

You know, the world that I'm looking towards

is you go to the website

and say, I want five frank one A's to work on my team today.

And they all spin up

and they start showing up in your Zoom meetings.

- To push back, but also to agree with you.

But first to push back.

I do think you need to convince people for them to welcome

that thing into their life.

- I think there's enough businesses

that operate on an objective,

kind of profit loss sort of basis that,

I mean, if you look at how many things,

again, talking about the world

as an evolutionary space there,

when you do have free markets

and you have entrepreneurs, you are gonna have people

that are gonna be willing to go out

and try whatever crazy things.

And when it proves to be beneficial,

there's fast followers in all sorts of places.

- Yeah and you're saying that, I mean,

Quake and VR is a kind of embodiment,

but just in a digital world

and if you're able to demonstrate,

if you're able to do something productive

in that kind of digital reality,

then AGI doesn't need to have a body.

- Yeah, it's like one

of the really practical technical questions

that I kind of keep arguing with myself over.

If you're doing a training and learning

and you've got, like, you can watch Sesame Street

and you can play master system games or something,

is it enough to have just a video feed that,

is that video coming in

or should it literally be on a virtual TV set

in a virtual room, even if it's a simple room just to have

that sense of you're looking at a 2D projection on a screen

versus having the screen beamed directly into your retinas.

And I think it's possible

to maybe get past some of these signs of life of things

with the just kind

of projected directly into the receptor fields,

but eventually for more kind

of human emotional connection for things.

Probably having some VR room with a lot of screens in it

for the AI to be learning in is likely helpful.

- It may be a world of different AIs,

interacting with each other.

- That self play I do think is one of the critical things

where socialization wise, one of the other limitations I set

for myself thinking about thing these is I need something

that is at least potentially real time

because I want, it's nice, you can always slow down time.

You can run on a subscale system

and test an algorithm at some lower level.

And if you've got extra horsepower,

running it faster than real time is a great thing.

But I want to be able to have the AIs

either socially interact with each other

or critically with actual people.

Your sort of child development psychiatrist

that comes in and interacts

and does the good boy bad boy sort of thing

as they're going through and exploring different things.

And it's nice to, I come back to the value

of constraints in a lot of ways.

And if I say,

well one of my constraints is real time operation,

I mean, it might still be a huge data center full

of computers, but it should be able

to interact on a Zoom meeting with people.

And that's how you also do start convincing people,

even if it's not a robot body moving around,

which eventually gets to irrefutable levels.

But if you can go ahead and not just type back

and forth to a GPT bot on something,

but you're literally talking to them

in an embodied over Zoom form

and working through problems with them

or exploring situations, having conversations

that are fully stateful and learned,

I think that that's a valuable thing.

So I do keep all of my eyes on things

that can be implemented

within sort of that 30 frames per second kind of work.

And I think that's feasible.

- Do you think the most compelling experiences

that are first will be for pleasure

or for business as they ask in airports?

So meaning is if it's interacting with AI agents,

will it be sort of like friends entertainment,

almost like a therapist

or whatever, that kind of interaction?

Or is it in the business setting something like you said,

brainstorming different ideas, sort of,

this is all a different formulation of kind

of a touring test or the spirit

of the original touring test.

Where do you think the biggest benefit will first come?

- So it's gonna start off hugely expensive.

I mean, you're gonna, if we're still all guessing about

what compute is gonna be necessary, I fall on the side of,

I don't think you run the numbers

and you're like 86 billion neurons,

a hundred trillion synapses.

I don't think those all need to be weights.

I don't think we need models that are quite

that big evaluated quite that often.

I base that on,

we've got reasonable estimates

of what some parts of the brain do.

We don't have the neocortex formula,

but we kind of get some of the other sensory processing

and it doesn't feel like we need to, we can simulate

that in computers for less weights,

but still it's probably going to be thousands of GPUs

to be running a human level AGI,

depending on how it's implemented,

that might give you sort of a clan of 128

and kind of run in batch people,

depending on whether there's sparsity

in the way the weights and things are set up,

if it is a reasonably dense thing,

then just the memory bandwidth trade offs means

you get 128 of 'em at the same time.

And either it's all feeding together, learning in parallel

or kind of all running together kind

of talking to a bunch of people.

But still, if you've got thousands of GPUs necessary

to run these things, it's gonna be kind of expensive.

Where it might start off a thousand dollars an hour

for your even post development

or something for that, which would be something

that you would only use for a business.

You know, something where you think

they're gonna help you make a strategic decision

or point out something super important.

But I also am completely confident

that we will have another factor

of a thousand in cost performance increase

in AGI type calculations.

Not in general computing necessarily,

but there's so much more that we can do with packaging,

making those right trade-offs, all those same types

of things that in the couple next couple decades,

thousand X easy and then you're down to a dollar an hour

and then you're kind of like,

well I should have an entourage of AIs

that are following me around helping me out on anything

that I want them to do.

- That's one interesting trajectory,

but I'll push back 'cause I have, so for, in that case,

if you wanna pay thousands of dollars,

it should actually provide some value.

I think it's easier for cheaper

to provide value via a dumb AI

that will take a store's AGI to just have a friend.

I think there's an ocean of loneliness in the world

and I think an effective friend that doesn't have

to be perfect, that doesn't have to be intelligent,

that has to be empathic.

Having emotional intelligence, having ability

to remember things, having ability to listen.

Most of us don't listen to each other.

One of the things that love

and when you care about somebody,

when you love somebody is when you listen.

And that is something we treasure about each other.

And if an AI can do that kind of thing,

I think that provides a huge amount of value

and very importantly provides value in its ability

to listen and understand versus provide really good advice.

I think providing really good advice is very difficult,

is another next level step that would,

I think it's just easier to do companionship.

- Yeah, I wouldn't disagree.

I mean, I think that there's very few things

that I would argue can't be reduced

to some kind of a narrow AI.

I think we can do trillion dollars of value easily

and all the things that can be done there.

And a lot of it can be done with smoke and mirrors

without having to go the whole thing.

I mean, there's going to be the equivalent of the doom,

the doom version for the AGI, that's not really AGI,

it's all smoke and mirrors.

But it happens to do enough valuable things

that it's enormously useful and valuable to people.

But at some point you do wanna get to the point

where you have the fully general thing

and you stop making bespoke specialized systems

for each thing and you wind up,

start using the higher level language instead

of writing everything in assembly language.

- What about consciousness, the C word?

Do you think that's fundamental to solving AGI

or is it a quirk of human cognition?

- So I think most

of the arguments about consciousness

don't have a whole lot of merit.

I think that consciousness

is kind of the way the brain feels when it's operating.

- Yes.

- And this idea that I do generally subscribe

to sort of the pandemonium theories

of consciousness where there's all these things bubbling

# Chapter 19

But it happens to do enough valuable things

that it's enormously useful and valuable to people.

But at some point you do wanna get to the point

where you have the fully general thing

and you stop making bespoke specialized systems

for each thing and you wind up,

start using the higher level language instead

of writing everything in assembly language.

- What about consciousness, the C word?

Do you think that's fundamental to solving AGI

or is it a quirk of human cognition?

- So I think most

of the arguments about consciousness

don't have a whole lot of merit.

I think that consciousness

is kind of the way the brain feels when it's operating.

- Yes.

- And this idea that I do generally subscribe

to sort of the pandemonium theories

of consciousness where there's all these things bubbling

around and I think of them

as kind of slightly randomized,

sparse, distributed memory bit strings of things

that are kind of happening,

recalling different associative memories.

And eventually you get some level of consensus

and it bubbles up to the point

of being a conscious thought there.

And the little bits of stochasticity that are sitting on

in this as it cycles between different things

and recalls different memory,

that's largely our imagination and creativity.

So I don't think there's anything deeply magical about it.

Certainly not symbolic.

I think it is generally

the flow of these associations drawn up

with stochastic noise overlaid on top of them.

And I think so much of that is like,

it depends on what you happen to have in your field of view

as some other thought was occurring to you that overlay

and blend into the next key

that queries your memory for things.

And that kind of determines

how your chain of consciousness goes.

- So that's kind of the quality of the subjective experience

of it is not essential for intelligence.

- I don't think so,

I don't think there's anything really important there.

- What about some other human qualities,

like fear of mortality and stuff like that?

Like the fact that this ride ends, is that important?

Like we talked

so much about this conversation about the value

of deadlines and constraints.

Do you think that's important for intelligence?

- That's actually a super interesting angle

that I don't usually take on that,

about has death being a deadline that forces you

to make better decisions.

- [Lex] Yes.

- Because I have heard people talk about

how if you have immortality, people are gonna stop trying

and working on things

because they've got all the time in the world.

- [Lex] Yeah.

- But I would say that I don't expect it

to be a super critical thing that a sense of mortality

and death, impending death is necessary there

because those are things that they do wind up providing

reward signals to us,

and we will be in control of the reward signals.

And there will have to be something fundamental

that causes that engenders curiosity and goal setting

and all of that.

Something is gonna play in there at the reward level,

whether it's positive or negative or both.

I don't have any strong opinions

on exactly what it's going to be,

but that's that type of thing where I doubt

that might be one of those half dozen key things

that has to be sorted out on exactly what the master reward,

that's the meta reward overall

of the local task, specific rewards have to be.

- That could be that big negative reward of death,

maybe not death,

but ability to walk away from an interaction.

So it bothers me when people treat AI systems like servants.

So it doesn't bother me,

but I mean it really is drawing the line

between what an AI system could be.

It's limiting the possibility,

what an system could be is treating them as justice tools.

Now that's of course, from a narrow AI perspective,

there's so many problems that narrow AI could solve,

just like you said, as in its form of a tool.

But it could also be a being

which is much more than a tool.

And to become a being, you have to respect

that thing for being a being.

And for that it has to be able to have,

to make its own decisions to walk away to say,

I had enough of you, I would like to break up with you now,

you've not treated me well and I would like to move on.

So I think that actually, that choice to end things.

- So a couple things on that.

So on the one hand,

it is kind of disturbing when you see people,

being like people that are mean to robots

and mean to Alexa whatever.

And that seems to speak badly about humanity,

but there's also the exact opposite side of that

where you have so many people

that imbue humanity in inanimate objects

or things that are toys or that are relatively limited.

So I think there may even be more danger

about people putting more emotional investment

into a lot of these proto AIs in different ways.

- Yeah and then the AI would manipulate that.

- But as far as like the AI ethnic sides of things,

I really stay away from any of those discussions

or even really thinking about it.

It's similar with the safety things

where I think it's just premature.

And there's a certain class of people

that enjoy thinking about impractical things,

things that are not in the world

and of pragmatic effect around you.

And I think that, again,

because I don't think there's gonna be a fast takeoff,

I think we actually will have time

to have these debates

when we know the shape of what we're debating.

And some people do take a principled approach

that they think it's gonna go too fast,

that you really do need to get ahead of it.

That you need to be thinking about this

because we have slow processes of coming to any kind

of consensuses or even coming up with ideas about this.

And maybe that's true.

I wouldn't put any of my money

or funding into something like that

because I don't think it's a problem yet.

And I think that we will have these signs of life

when we've got our learning disabled toddler,

we should really start talking about some of the safety

and ethics issues, but probably not before then.

- Can you elaborate briefly about why you don't think

there'll be a fast takeoff?

Is there some deep intuition you have about it?

Does it because it's grounded in the physical world or why?

- Yeah, so it is my belief that we're gonna start off

with something that requires thousands of GPUs.

And I don't know if you've tried

to go get a thousand GPU instance

on a cloud anytime recently, but these are not things

that you can just go spin up hundreds of.

There are real challenges to, I mean,

these things are gonna take data centers

and data centers take years to build,

and the last few years we've seen a few of them kind

of coming up, going in different places.

They're big engineering efforts.

You can hear people bemoan about the fact

that I, oh the network was wired all wrong

and it took 'em a month to go unwire it

and rewire it the right way.

These aren't things that you can just magic into existence.

And the ideas of like the old tropes

about it's gonna escape onto the internet

and take over other systems.

There's the fast takeoff ones are clearly nonsense

because you just can't open TCP connections

above a certain rate no matter how smart you are,

even if you have perfect hacking ability

that take over the world in an instant sort of thing,

just isn't plausible at all.

And even if you had access to all of the resources,

these are going to be specialized systems

where you're going to wind up with something

that is architected around exactly this chip

with this interconnect and it's not just gonna be able

to be plopped somewhere else.

Now interestingly, it is going to be something

that the entire code for all

of it will easily fit on a thumb drive

that's total spy movie thriller sorts of things

where you could have, hey, we cracked the secret to AGI

and it fits on this thumb drive and anyone could steal it.

Now they're still gonna have to build the right data center

to deploy it and have the right kind

of life experience curriculum to take it up

to the point where it's valuable.

But the real core of it, the magic

that's gonna happen there is going to be very small.

You know, it's again, tens of thousands of lines of code,

not millions of lines of code.

- It is possible to imagine a world,

as you mentioned this in this spy thriller view.

If it's just a few lines of code,

we can imagine a world where the surface

of computation is growing, maybe growing exponentially,

meaning there's the refrigerators start getting a GPU

and just every first of all the smartphones,

the billions of smartphones.

But maybe if there come highways

through which code can spread across the entirety

of the computation surface, then you don't any longer have

to book AWS GPUs.

- There were real fundamental issues there

when you start getting down to taking an actual problem

and putting it on an abstract machine like that,

that has not worked out well in practice.

And the idea that there was always,

like, it's always been easy to come up with ways

to get compute faster to say more flops

or more more giga ops or whatever there,

that's usually the easy part,

but you then have interconnect

and then memory for what goes into it.

And when you talk about saying, well, cell phones,

well you're limited to like a 5G connection

or something on that.

And if you say how, if you take your calculation

and you factor it across a million cell phones

instead of a thousand GPUs in a warehouse, you might be able

to have some kind of a substrate like that.

But it could be operating then at one 1000th the speed.

And so yes, you could get,

you could have an AGI working there,

but it wouldn't be a real time AGI, it would be something

that is operating at really a snails pace,

much slower than kind of human level thought for things.

So I'm not worried about that problem.

- You're transferring the problem into the interconnect,

the communication, the shared memory,

the collective intelligence aspect of it,

which is extremely difficult as well.

- Yeah, I mean it's back to the very earliest days

of supercomputers, you still have the balance

between bandwidth storage and computation,

and sometimes they're easier to get one or the other,

but it's been remarkably constant across all those years

that you still need all three.

- What do your efforts now, you mentioned to me

that you're really committing to AI at this stage.

What do you see your life in the next few months,

years look like?

What do you hope to achieve achieve here?

- So I literally just this week signed a term sheet

to take some investment money for my company

where the last two years I had backed off from Meta

and I was still doing my consulting CTO role there,

but I had styled it as I was going to take

the Victorian gentleman scientist route

where I was gonna be the the wealthy person

that was going to go pursue science and learn about this

and do experiments.

And honestly, I'm surprised there aren't more people like

that are like me, technical people that made a bunch

of money and are interested in some

of these possibly the biggest leverage point

in human history.

I mean, I know of, I've heard of a couple organizations

that are basically led by one rich techie guy

that gets a few people around him to try to work on this,

but I'm surprised that there's not more,

that there aren't like a dozen of them.

I mean, maybe people still think

that it's an unapproachable problem,

that it's kind of beyond their ability to get a wrench on

and have some effect on like whatever startups

they've run before.

But that was my kind of like,

with all the stuff I've learned, whether it's gaming,

aerospace, whatever I go through a larval phase

where I'm like, okay, I'm sucking up all

of this information trying to see is this something

that I can actually do?

Is this something that's practical

to devote a large chunk of my life to?

And I've gone through that

with the AI machine learning space of things.

And I think I've got my arms around it,

I've got the measure of it where some

of the most brilliant people in the world

are working on this problem,

but nobody knows exactly the path that it's going on.

We're throwing a lot of things at the wall

and seeing what sticks.

But I have a, another interesting thing,

just learning about all of this,

the contingency of your path to knowledge

and talking about the associations

and the context that you have with them

where people that learn in the same path will have similar

thought processes.

And I think it's useful that I come at this

from a different background,

different history than the people

that have had the largely academic backgrounds for this,

where I have huge blind spots

that they could easily point out.

But I have a different set of experiences in history

and approaches to problems

and systems engineering that might turn out to be useful.

And I can afford to take that bet

where I'm not gonna be destitute.

I have enough money to fund myself working on this

for the rest of my life.

But what I was finding is that I was still not committing

where I had a foot firmly in the VR

and Meta side of things where

in theory I've got a very nice position there.

I only have to work one day a week for my consulting role.

But I was engaging every day.

I'd still be like, my computer's there,

I'd be going and checking the workplace and notes

and testing different things and communicating with people.

But I did make the decision recently that no,

I'm gonna get serious.

I'm still gonna keep my ties with Meta,

but I am seriously going for the AGI side of things.

- And it's actually a really interesting point

because a lot of it, the machine learning,

the AI community is quite large.

But really basically almost everybody has taken

the same trajectory through life in that community.

And it's so interesting to have somebody like you,

which with a fundamentally different trajectory

and that's where the big solutions can come

because there is a kind of silo

and it is a bunch of people,

kind of following the same kind of set of ideas.

- And I was really worried that I didn't wanna come off

as like an arrogant outsider for things

where I have all the respect in the world for the work

that's it's been a miracle decade.

We're in the midst

of a scientific revolution happening now

and everybody doing this is,

these are the Einsteins and Bohr

and whatever is of our modern era.

And I was really happy to see that the people

that I've sat down and talked with everybody does seem

to really be quite great about just happy

to talk about things, willing to acknowledge

that we don't know what we're doing,

we're figuring it out as we go along.

And I mean, I've got a huge debt on this

where this all really started for me

because Sam Altman basically tried to recruit me to OpenAI

and it was at a point when I didn't know anything about

what was really going on in machine learning.

And in fact,

it's funny how the first time you reached out to me,

it was like four years ago for your AI podcast.

- Yeah, for people who listening to this should know

that first of all, obviously I've been a huge fan

of yours for the longest time,

but we've agreed to talk like, yeah,

like four years ago back when this was called

the "Artificial Intelligence Podcast,"

we wanted to do a thing and we said, you said yes.

- And I said, it's like I don't know anything

about modern AI.

- That's right. - I said,

I could kind of take an angle on machine perception

'cause I'm doing a lot of that with the sensors

and the virtual reality,

but we could probably find something to talk about.

# Chapter 20

because Sam Altman basically tried to recruit me to OpenAI

and it was at a point when I didn't know anything about

what was really going on in machine learning.

And in fact,

it's funny how the first time you reached out to me,

it was like four years ago for your AI podcast.

- Yeah, for people who listening to this should know

that first of all, obviously I've been a huge fan

of yours for the longest time,

but we've agreed to talk like, yeah,

like four years ago back when this was called

the "Artificial Intelligence Podcast,"

we wanted to do a thing and we said, you said yes.

- And I said, it's like I don't know anything

about modern AI.

- That's right. - I said,

I could kind of take an angle on machine perception

'cause I'm doing a lot of that with the sensors

and the virtual reality,

but we could probably find something to talk about.

- And then, so I mean,

when did Sam talk to you about OpenAI around the same time?

- No, it was a little bit after that.

So I had done the most basic work.

I had kind of done the neural networks from scratch

where I had gone and written it all in C

just to make sure I understood back propagation

at the lowest level and my nuts and bolts approach.

But after Sam approached me,

it was flattering to think that he thought

that I could be useful at OpenAI largely for kind

of like systems optimization sorts of things.

I am without being an expert.

But I asked Ilya Sutskever to give me a reading list

and he gave me a binder full of all the papers

that like, okay, these are the important things.

If you really read and understand all of these,

you'll know like 80% of what most

of the machine language researchers work on.

And I went through

and I read all those papers multiple times

and highlighted 'em and went through

and kind of figured the things out there

and then started branching out into my own sets

of research on things

and eventually started writing my own experiments

and doing, kind of figuring out,

finding out what I don't know,

what the limits of my knowledge are

and starting to get some of my angles

of attack on the things

that I think are a little bit different

from what people are doing.

And I've had a couple years now, like two years

since I kind of left the full-time position at Meta

and now I've kind of pulled the trigger

and said I'm gonna get serious about it.

But some of my lessons all the way back

to Armadillo Aerospace about how I know I need

to be more committed to this,

where there is that it's both a freedom

and a cost in some ways when you know

that you're wealthy enough to say it's like,

this doesn't really mean anything.

I can spend a million dollars a year for the rest of my life

and it doesn't mean anything, it's fine.

But that is an opportunity to just kind of meander.

And I could see that in myself when I'm doing some things.

It's like, oh, this is a kind of interesting, curious thing.

Let's look at this for a little while, let's look at that.

It's not really bearing down on the problem.

So there's a few things that I've done that are kind

of tactics for myself to make me more effective.

Like one thing I noticed I was not doing well

is I had a Google Cloud account with,

to get GPUs there and I was finding,

I was very rarely doing that

for no good psychological reasons where I'm like, oh,

I can always think of something to do other than

to spin up instances and run an experiment.

I can keep working on my local titans or something.

But it was really stupid.

I mean, it was not a lot of money.

I should have been running more experiments there.

So I thought to myself, well,

I'm gonna go buy a quarter million dollar DGX station,

I'm gonna just like sit it right there

and it's gonna mock me if I'm not using it.

If the fans aren't running on that thing,

I'm not properly utilizing it.

And that's been helpful.

You know, I've done a lot more experiments since then.

It's been interesting

where I thought I'd be doing all this

low level envy link optimized stuff,

but 90% of what I do is just spin up four instances

of an experiment with different hyper parameters on it.

- Oh, interesting.

So you're doing like really sort of building up intuition

by doing ML experiments of different kinds.

- But so the next big thing though is I am,

I decided that I was gonna take some investor money

because I have an overactive sense

of responsibility about other people's money.

And it's like, I don't want, I mean a lot

of my push and my passionate in treaties for things at Meta,

it's like I don't want Zuck

to have wasted his money investing in Oculus.

I want it to work out.

I want it to change the world.

I want it to be worth all of this time, money,

and effort going into it.

And I expect that it's going to be that like that

with my company where.

- [Lex] It's a huge forcing function, this investment.

- I have investors that are going

to expect something of me.

Now, we've all had the conversation

that this is a low probability long-term bet.

It's not something that there's a million things I could do

that I would have line of sight on the value proposition

for this isn't that, I think there are,

there are unknown unknowns in the way,

but it's one of these things

that it's hyper bull but it's potentially one

of the most important things humans ever do.

And it's something that I think is within our lifetimes,

if not within a decade to happen.

So yeah, this is just now happening like term sheet,

like the ink is barely virtual in's barely dry off.

- It's drying.

I mean, as I mentioned to you offline,

like somebody I admire

and somebody you know, Andre Pathy,

I think the two of you, different trajectories in life,

but approach problems similarly

in that he codes stuff from scratch up all the time.

And he's created a bunch of little things outside of,

even outside the course at Stanford

that have been tremendously useful

to build up intuition about stuff, but also to help people.

And they're all in the realm of AI.

Do you see yourself potentially doing things like this

or not necessarily solving a gigantic problem,

but on the journey,

on the path to that building up intuitions

and sharing code or ideas

or systems that give inklings of AGI

but also kind of are useful to people in some way?

- So yeah.

First of all, Andre is awesome.

I learned a lot when I was going

through my larval phase from his blog posts

and his Stanford course and super valuable.

I got to meet him first a couple years ago

when I was first kind of starting off

on my gentleman scientist bit.

And just a couple months ago

when he went out on his sabbatical, he stopped by in Dallas

and we talked for a while

and I had a great time with him.

And then when I heard he actually left Tesla,

I did of course along with a hundred other people say,

"Hey, if you ever wanna work with me, it would be an honor."

- Yeah. - So he thinks

that he's gonna be doing this educational work,

but I think someone's gonna make him an offer he can't

refuse before he gets too far along on it.

- Oh, his current interest is the educational side.

He's a special mind.

Is there something you could speak

to what makes him so special?

So from your understanding.

- Like he did,

he was very much a programmer's programmer

that was doing machine learning

work rather than- - That's right.

- It's a different feel than an academic

where you can see it in paper sometimes where somebody

that's really a mathematician or a statistician at heart

and they're doing something with machine learning,

but you know, Andre's about getting something done

and you could see it in like all of his earliest approaches

to, it's like, okay,

here's how reinforcement learning works.

Here's how recurrent neural networks work.

Here's how transformers work,

here's how I crypto works and I am,

and yeah, it's just, he's a hacker's,

one of his old posts

was like a hacker's guide to machine learning.

- [Lex] Yeah.

- And you know, he deprecated that and said,

don't really pay attention to what's in here.

But it's that thought that carries through in a lot of it

where it is that back again to that hacker mentality

and the hacker ethic with what he's doing

and sharing all of it.

- Yeah and a lot of his approach to new thing,

like you said, larva stage is,

let me code up the simplest possible thing

to build up intuition about it.

- Yeah, like I say, I sketch with structs

and things when I'm just thinking about a problem.

I'm thinking in some degree of code.

- You are also among many things a martial artist,

both judo and jujitsu.

How has this helped make you the person you are?

- So, I mean, I was a competent club player

in judo and grappling.

I mean, I was by no means any kind of a superstar,

but it was, I went through a few phases

with it where I did some, when I was quite young,

a little bit more when I was 17,

and then I got into it kind of seriously in my mid '30s

and I went pretty far with it

and I was pretty good at some

of the things that I was doing.

And I did appreciate it quite a bit where,

and on the one hand it's always,

if you're gonna do exercise or something,

it's a more motivating form of exercise.

If someone is crushing you are like,

you are motivated to do something about that.

To up your attributes

and be better about getting outta that.

- Attributes, yes.

- But there's also that sense

that like I was not a sports guy.

I did do wrestling in junior high

and I often wish that, I think I would've,

I would've been good for me if I'd carried

that on into high school and had a little bit more of that.

I mean, it's like I, a little bit

of wrestling vibe with always going on about embracing

the grind and like that push

that I associate with the wrestling team

that yes, that in hindsight,

I wish I had gone through that and pushed myself that way.

But even getting back into judo and jiujitsu

in my mid-30s as usually the old man on the mat with that,

there was still the sense that working out with the group

and having the guys

that you're beating each other up with it,

but you just feel good coming out of it.

And I can remember those driving home aching in various ways

and just thinking it's like, oh, that was really great.

And it's mixing with a bunch of people

that had nothing to do with any of the things

that I worked with.

You know, every once in a while someone would be like,

oh, you're the Doom guy.

But for the most part it was just different slice of life,

you know, a good thing.

And I made the call when I was 40

that's like, maybe I'm getting a little old for this.

I had separated a rib and tweaked a few things

and as one does without any really bad injuries.

And it was like, have I dodged enough bullets?

Should I hang it up?

I went back, I've gone a couple times

in the last decade trying to get my kids

into it a little bit.

I didn't really stick with any of them,

but it was fun to get back on the mats.

I really hurts for a while when you haven't gone,

I gone for a while,

but I still debate this pretty constantly.

My brother's only a year younger than me

and he's going kind of hard in jujitsu right now.

And he was just, he won a few medals

at the last tournament he was at.

- [Lex] So he's competing too? - Yeah.

And I was thinking, yeah,

I guess we're in the executive division if you're over 50,

we're over 45 or something.

And it's not outta the question

that I go back at some point and do some of this,

but again, I'm just reorganizing my life around more focus.

Probably not gonna happen.

I'm pushing my exercise around

to give me longer uninterrupted intellectual focus time,

pushing it to the beginning or the end of the day.

- Like running and stuff like that, or walking, yeah.

- [John] Yeah, I running in calisthenics

and some things like that, but-

- It allows you to still think about a problem and yeah.

- But if you're going to a judo club or something,

you've got a fixed, it's gonna be seven o'clock

or whatever, 10 o'clock on Saturday.

Although I talked about this a little bit

when I was on Rogan and shortly after that,

Carlos Machado did reach out

and I had trained with him for years back in the day

and he was like, hey, we've got kind of a small private club

with a bunch of kind of executive type people

and it does tempt me.

- Yeah, I don't know if you know him,

but John Danaher moved here to Austin

with Gordon Ryan and a few other folks.

And he has a very interesting way, very deep, systematic way

of thinking about jiujitsu that reveals the chest of it,

like the science of it.

- And I do think about that more as kind

of an older person considering the martial arts

where I can remember

the very earliest days getting back into judo

and I'm like, teach me submissions right now, right?

You know, it's like learn the arm bar, learn the choke.

But yeah, as you get older you start thinking more about,

it's like, okay,

I really do wanna like learn the entire cannon of judo.

It's like, or all the different things there

and like all the different approaches for it.

Not just the, if you want to compete,

there's just a handful

of things you learn really, really well,

but sometimes there's interest

in learning a little bit more of the scope there

and figuring some things out from,

at one point I had wasn't exactly a spreadsheet,

but I did have a big long text file

with like, here's the things that I learned

and here are like ways you chain this together.

And while when I went back a few years ago,

it was good to see

that I whipped myself back into reasonable shape

about doing the basic grappling.

But I know there was a ton of the subtleties that were just,

that were gone but could probably

be brought back reasonably quickly.

- And there's also the benefit, I mean,

you're exceptionally successful now.

You're brilliant and the old problem of the ego.

- Yeah, I still pushed kind of harder than I should.

I mean that was,

I was one of those people that I'm on the smaller side

for a lot of the people competing.

And I'd go with all the big guys and I'd go hard.

And I'd push myself a lot

and that would be one of those where I'd be dangerous

to anyone for the first five minutes.

But then sometimes after that I'm already dead.

And I knew it was terrible for me

'cause it meant I got less training time

with all of that when you go

and you just gas out relatively quickly there.

And I like to think that I would be better about that

where after I gave up judo,

I started doing the half marathons

and tough butters and things like that.

And so when I did go back to the local Judo kai club,

I thought it's like,

oh, I should have better cardio for this.

'Cause I'm a runner now and I do all of this

and didn't work out that way.

It was the same old thing where just push really hard,

strain really hard.

And of course when I worked with good guys like Carlos,

it's like he just, the whole flow,

like water thing is real and he's just like-

- That's true with judo too.

Some of the best people like I've trained

with Olympic gold medalists

and for some reason with them everything's easier.

Everything is, you actually start to feel the science of it,

the music of it, the dance of it.

Everything is effortless.

You understand that there's an art to it.

It's not just an exercise.

- Yeah, it was interesting where I did go

to the Kode Con in Japan, kind of the birthplace

of judo and everything.

And I remember I rolled with one old guy,

I didn't start standing, just started on ground work

and it was striking how different it was from Carlos.

He was still, he was better than me and he got my arm

and I had to tap there,

but it was a completely different style

where I just felt like I could do nothing.

He was just enveloping me

and just like slowly ground it down

and took my arm and bent it while with Carlos,

he's just loose and free

and you always thought like, oh,

you're just gonna go grab something.

But never had any chance to do it.

That's, but it was a very different feeling.

- That's a good summary of the difference

between jiujitsu and judo.

In jiujitsu,

it is a dance and you feel like there's a freedom.

# Chapter 21

of judo and everything.

And I remember I rolled with one old guy,

I didn't start standing, just started on ground work

and it was striking how different it was from Carlos.

He was still, he was better than me and he got my arm

and I had to tap there,

but it was a completely different style

where I just felt like I could do nothing.

He was just enveloping me

and just like slowly ground it down

and took my arm and bent it while with Carlos,

he's just loose and free

and you always thought like, oh,

you're just gonna go grab something.

But never had any chance to do it.

That's, but it was a very different feeling.

- That's a good summary of the difference

between jiujitsu and judo.

In jiujitsu,

it is a dance and you feel like there's a freedom.

And actually it anybody, I try like the Gordon Ryan,

one of the best grappler in the world,

Nogi grappler in the world.

There's a feeling like you can do anything,

but when you actually try to do something, you can't.

- Just magically doesn't work.

- But with the best judo players in the world, yeah,

it does feel like there's a blanket

that weighs a thousand pounds on top of you.

And there's not a feeling like you can do anything.

You just, you're trapped.

And that's a style,

that's a difference in the style of martial arts.

But it's also once you start to study,

you understand it all has to do with human movement

and the physics of it and the leverage

and all that kind of stuff.

And that's like. - [John] Yeah.

- That's super fascinating.

At the end of the day, for me, the biggest benefit is,

and the humbling aspect when another human being,

kind of tells you that there's a hierarchy

or you're not that special.

- Yeah and in the most extreme case,

when you tap to a choke, you are basically living

because somebody lets you live.

And that is one of those, if you think about it,

that is a closer brush with mortality

than most people consider.

- And that kind of humbling act is good to take

to your work then where it's harder

to get humbled, you know?

- Yeah, 'cause nobody that does any martial art

is coming out thinking I'm the best in the world at anything

because everybody loses.

- Let me ask you for advice.

What advice would you give to young people today about life,

about career?

How they can have a job, how they can have an impact,

how they can have a life they could be proud of.

- So it was kind of fun.

I got invited to give the commencement speech back

I went to a college for two semesters and dropped out

and went on to do my tech stuff,

but they still wanted me to come back

and give a commencement speech.

And I've got that pinned on my Twitter account

and I still feel good about everything that I said there.

And, you know, my biggest point was that the path

for me might not be the path for everyone.

And in fact, the advice, the path that I took

and even the advice that I would give based on my experience

and learnings probably isn't the best advice for everyone.

Because what I did was all about this knowledge and depth.

It was about not just having this surface level ability

to make things do what I want,

but to really understand them through and through,

to let me do the systems engineering work.

And to sometimes find these inefficiencies

that can be bypassed

and that the whole world doesn't need that.

You know, most programmers don't need,

or engineers of any kind don't necessarily need to do that.

They need to do a little job

that's been parceled out to them, be reliable.

Let people depend on you.

Do quality work with all of that.

But people that do have an inclination for wanting

to know things deeper and learn things deeper.

You know, there are just layers

and layers of things out there.

And it's amazing.

If you're the right person that is excited about that,

the world's never been like this before.

It's better than ever.

I mean, everything that was wonderful

for me is still there.

And there's whole new worlds

to explore on the different things that you can do

and that it's hard work.

Embrace the grind with it and understand as much as you can.

And then be prepared for opportunities

to present themselves where you can't just say,

this is my goal in life.

And just push at that.

I mean, you might be able to do that,

but you're going to make more total progress if you say,

I'm preparing myself with this broad set of tools

and then I'm being aware of all the way things are changing

as I move through the world

and as the whole world changes around me.

And then looking for opportunities

to deploy the tools that you've built.

And there's going to be more and more

of those types of things there where an awareness

of what's happening, where the inefficiencies are,

what things can be done,

what's possible versus what's current practice.

And then finding those areas where you can go

and make an adjustment

and make something that may affect millions

or billions of people in the world make it better.

- When maybe from your own example,

how were you able to recognize this about yourself?

That you saw the layers in a particular thing

and you were drawn to discovering deeper

and deeper truths about it.

Is that something that was obvious

to you that you couldn't help?

Or is there some actions you had to take

to actually allow yourself to dig deep?

- So in the earliest days of personal computers,

I remember the reference manuals

and the very early ones even had schematics

of computers in the background in the back

of the books as well as firmware listings and things.

And I could look at that

and at that time when I was a younger teenager,

I didn't understand a lot of that stuff.

How the different things worked.

I was pulling out the information that I could get,

but I always wanted to know all of that.

There was like kind of magical

information sitting down there.

It's like the elder lore that some gray beard wizard,

who is the keeper of,

and so I always felt that pull for wanting to know more,

wanting to explore the mysterious areas there.

And you know,

and that followed right in through all the things

that got the value, exploring the video cards leading

to the scrolling advantages,

exploring some of the academic papers and things,

learning about BSP trees

and the different things that I could do

with those systems

and just the huge phases going through aerospace,

just reading bookshelves full of books.

I mean, again, that point

where I have enough money I can buy all the books I want.

It was so valuable there where I was terrible

with my money when I was a kid.

My mom thought I would always be broke

because I'd buy my comic books and just be outta money.

But it was like all the pizza I want,

all the diet coke I want, video games and then books.

- [Lex] Books.

- And it didn't take that much.

- [Lex] Yeah.

- As soon as I was making 27K a year, I felt rich

and I was just getting all the things that I wanted.

But that sense of,

that's books have always been magical to me.

And that was one of the things that really made me smile

is I, Andre had said he found, when he came over

to my house, he said he found my library inspiring

just that I have.

And it was great to see,

I still look at him, he's kind of a younger guy.

I sometimes wonder if younger people these days have

the same relationship with books that I do

where they were such a cornerstone for me in so many ways.

But that sense that, yeah, I always wanted to know it all.

I know I can't.

And that was like one of the last things I said,

you know, you can't know everything,

but you should convince yourself

that you can know anything, any one particular thing.

It was created and discovered by humans.

You can learn it, you can find out what you need on there.

- And you can learn it deeply.

- Yeah, you can drive a nail down

through whatever layer cake problem space you've got

and learn a cross section there.

- And not only can you have an impact doing that,

you can attain happiness doing that.

There's something so fulfilling

about becoming a craftsman of a thing.

- Yeah and I don't want to tell people that, look,

this is a good career move.

Just grit your teeth and bear it.

You know, you want people,

and I do think it's possible sometimes

to find the joy in something

like it might not immediately appeal to you,

but I had told people early on, like in software times

that a lot of game developers are in it just

because they're so passionate about games.

But I was always really more flexible

in what appealed to me, where I said,

I think I could be quite engaged doing operating system work

or even database work.

I would find the interest in that

because I think most things

that are significant in the world have a lot of layers

and complexity to them

and a lot of opportunities hidden within them.

So that would probably be the most important thing

to encourage to people is that I am, you can,

it's like weaponized curiosity.

You can deploy your curiosity to find,

to kind of like make things useful and valuable to you,

even if they don't immediately appear that way.

- Deploy your curiosity.

Yeah, that's very true.

We've mentioned this debate point, whether mortality

or fear of mortality is fundamental to creating an AGI,

but let's talk

about whether it's fundamental to human beings.

Do you think about your own mortality?

- I really don't.

And you probably always have

to like take with a grain of salt

anything somebody says about fundamental things like that,

but I don't think about really aging,

impending death, legacy with my children, things like that.

And clearly it seems most

of the world does a lot more than I do.

- [Lex] Yeah.

- So I mean, I think I'm an outlier in that

where it's, yeah, it doesn't wind up being a real part

of my thinking and motivation about things.

- So daily existence is about sort of the people you love

and the problems before you.

- Yeah, I'm very much focused

on what I'm working on right now.

I do take that back.

There's one aspect where the kind of finiteness

of the life does impact me

and that is about thinking about the scope of the problems

that I'm working on when I decided to work on,

when I was like nuclear fission or AGI,

these are big ticket things that I,

that are impact large fractions of the world.

And I was thinking to myself at some level that okay,

I mean I may have a couple more swings at bat

with me at full capability,

but yes, my mental abilities will decay with age,

mostly inevitably.

I don't think it's a 0% chance that we will address some

of that before it becomes a problem for me,

I think exciting medical stuff in the next couple decades,

but I do have this kind of vague plan

that when I'm not at the top of my game

and I don't feel that I'm in a position

to put a dent in the world some way

that I'll probably wind up doing some kind

of recreational retro programming

or I'll work on something

that I would not devote my life to now,

but I can while away my time

as the old man gardening in the code worlds.

- And then to step back given bigger.

Let me ask you about why we're here we human beings,

what's the meaning of it all?

What's the meaning of life John Carmack?

- So very similar with that last question.

I know a lot of people fret about this question a lot,

and I just really don't.

- I really don't give damn.

- No, we are biological creatures.

That happenstance of evolution,

we have innate drives that evolution crafted for survival

and passing on of genetic codes.

I don't find a lot of value in trying

to go much deeper than that.

I have my motivations,

some of which are probably genetically coded

and many of which are contingent on my upbringing

and the path that I've had through my life.

I don't run into like states of depression or envy

or anything that winds up being a challenge

and forcing a degree of soul searching

with things like that.

I seem to be okay, kind of without that.

- As a brilliant ant in the ant colony without looking up

to the sky wondering why the hell am I here again?

- Yeah.

- So the the why of it, the incredible mystery

of the fact that we started, first of all the origin

of life on earth and from that, from single cell organisms,

the entirety of the evolutionary process took us somehow

to this incredibly intelligent thing

that is able to build Wolfenstein 3D and Doom and Quake

and take a crack at the problem of AGI

and create things that eventually supersede human beings.

That doesn't, the why of it is?

- It's been my experience that people

that don't focus on the here and now,

right in front of them, tend to be less effective.

I mean, it's not a 100%.

- Yeah.

- Vision matters to some people,

but it doesn't seem to be a necessary motivator for me,

and I think that the process

of getting there is usually done.

Again, it's like the magic of gradient descent.

- [Lex] Yeah. - People just don't believe

that just looking locally gets you to all

of these spectacular things

that's been the decades of looking at I really some

of the smartest people in the world

that would just push back forever against this idea

that it's not this grand sophisticated vision of everything,

but little tiny steps.

Local information winds up leading to all the best answers.

- So the meaning of life is following locally

wherever the gradient descent takes you.

This was an incredible conversation,

officially the longest conversation

I've ever done on the podcast, which means a lot to me

because I get to do it with one of my heroes.

John, I can't tell you how much it means to me

that you would sit down with me.

You're an incredible human being.

I can't wait what you do next,

but you've already changed the world.

You're an inspiration to so many people,

and again, we haven't covered

like most of what I was planning to talk about.

So I hope we get a chance

to talk someday in the future

and I can't wait to see what you do next.

Thank you so much again for talking to me.

- Thank you very much.

- Thanks for listening

to this conversation with John Carmack.

To support this podcast,

please check out our sponsors in the description.

And now lemme leave you

with some words from John Carmack himself.

Focused hard work is the real key to success.

Keep your eyes on the goal

and just keep taking the next step towards completing it.

If you aren't sure which way to do something,

do it both ways and see which works better.

Thank you for listening and hope to see you next time.

