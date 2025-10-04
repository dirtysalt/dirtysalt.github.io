# Chapter 1

- Humans are by far the hardest part of computer graphics

because millions of years of evolution

have given us dedicated brain systems

to detect patterns and faces and infer emotions and intent

because cavemen had to,

when they see a stranger determine whether they were

likely friendly or they might be trying to kill them.

And so people in the world have extraordinarily

detailed expectations of a face

and we can notice imperfections,

especially perfect arising

from computer graphics limitations.

Okay, one part is capturing humans.

And so it involved really advanced, dedicated hardware

that puts a human in a capture sphere

with dozens of cameras in them, taking high resolution,

high frame rate video of them as they go

through a range of motions.

And then capturing the human face is complicated

because the nuance detail of our faces

and how all the muscles and sinews

and fat work together to give us different expressions.

So it's not only about the shape of a person's face,

but it's also about the entire range of motion

that they might go through.

So that's the data problem.

There's a lot of other problems with computer graphics.

You know, there's technology for rendering hair,

which is really hard 'cause you can't render every, again,

we know the laws of physics.

It would be easy to just render every hair.

It would just be a billion times too slow.

So you need approximations that capture the net effect

of hair on rendering and on pixels

without calculating every single interaction

of every light with every strand of hair.

That's one part of it.

There's detailed features for different parts of faces.

There's subsurface scattering

because we think of humans as opaque.

But really our skin is, we light travels through it.

It's not completely opaque.

And the way in which light travels

through skin has a huge impact on our appearance.

And this is why there's no way you can paint a mannequin

to look realistic for a human.

You know, it's just a solid surface

and we'll never have the sort of detail you see.

- That kind of blew my mind, like thinking through that.

I think I heard that sort of the oiliness of the skin

creates very specific, nuanced, complex reflections

and then some light is absorbed

and travels through the skin

and that creates textures that are humanized,

able to perceive and it creates the thing

that we consider human, whatever that is.

All of that, while considering all the muscles involved

in making the nuance expression, just the subtle squinting

of the eyes or the subtle formation of a smile,

it's a subtlety of human faces that you have to capture.

Like the difference between a real smile and a fake smile.

But the way to show like beginning of a formation of a smile

that actually reveals a deep sadness.

All of that, like when I watch a human face,

I can like read that.

I could see that.

You have to have the tools

that in real time can render something like that.

And that's incredibly difficult.

- That's right, getting faces right requires the interplay

of literally dozens of different systems

and aspects of computer graphics.

And if any one of them is wrong,

your eye is completely drawn to that

and you find it on the wrong side of uncanny valley.

- The following is a conversation with Tim Sweeney,

a legendary video game programmer,

Founder and CEO of Epic Games

that created many incredible games of technologies,

including the Unreal Engine and "Fortnite,"

which both revolutionized the video game industry

and the experience of playing and creating video games.

This is the Lex Fridman podcast.

To support it, please check out our sponsors

in the description.

And now, dear friends, here's Tim Sweeney.

When did you first fall in love with computers

and maybe with programming?

- I had a brother, Steve Sweeney,

who 16 years older than me,

and at some point when I was a little kid,

he went off to work in California for a tech company

and he'd gotten one of the first IBM PCs.

And so for one summer, I think I was about 11,

I went to visit him in California.

It was my first like trip away from my family

just to hang out with him.

And he had this brand new IBM computer

and I learned to program over the course of a few days

in BASIC, I was just blown away with the capabilities

of computers at the time.

It was unbelievable what they could accomplish.

And I was hooked from that point onward

and very much wanted to be a programmer.

- Do you remember what you wrote in BASIC?

Is it a video game type thing?

Is it like for loop, some numerical thing?

Do you remember?

- Yeah, it's funny, I have a perfectly vivid memory

of all of the first things I learned to program. (laughs)

I have a hard time remembering people's names,

but like code really sticks with me.

Every step and every challenge there were lessons learned

and you know, some of which I've come to realize

were just like me getting over some learning hurdles.

But other things were actually shortcomings

of programming languages

and the realization that there are actually better ways than

what a programmer is learning to program for the first time.

You know, a lot of what they're facing

isn't the challenge of learning a new art.

It's friction introduced by failures

of programming language design.

And so I've constantly come back to those early lessons

there as I've progressed and done more

and more things including building programming languages.

- Yeah, the friction and the pain is the guide

to learning in programming.

Like if I were to describe programming journey

that would be marked by pain.

And that pain, you shouldn't escape the pain.

The pain is instructive for you

to understand programming languages.

But do you remember what kind of stuff you were writing

at that time?

Just the early programs?

- Yeah, in the early days

I wrote a little bit of everything.

I wrote some games.

The first game I wrote on the Apple II was...

Since I only knew how to program in text mode,

the computer would throw asterisks across the screen.

They'd flow from left to right

and you'd have a parentheses on the right hand side

of the screen and yeah, looks like a baseball mitt

and you're supposed to catch the asterisks.

That was my very first game.

It took about a couple hours to build

and tune and I went from there.

But I built a lot of things.

I built databases at different points.

I built a programming language

and a full compiler for a language like Pascal

'Cause I didn't know where you went to buy one of those.

So I made my own.

And you know, one of the fun things at that time

was Bulletin Boards.

Before we had the internet in the hands of consumers,

you used your modem and you dialed into a local phone number

and connected to whoever was running the computer there.

And every town or city

had hundreds of these Bulletin Boards

run by different people

with their own personalities and teams.

And so I spent a lot of time Bulletin Board program

and learning how to deal

with database management and user interface

and dealing with multiple users concurrently and things.

And so I don't know, I'd probably spend about 10,000

or 15,000 hours writing code just on my own as a kid

between like age 10 and you know, age 20

before I actually shipped a program to the outside world.

- 10,000 to 15,000 hours.

What was the value of the hours as a kid you put in,

in programming that led

to the success you've had in later life?

Maybe this is by way of advice to younger people

in terms of how they allocate the hours of their early life.

- Yeah, you know, it's not just hours.

It's really striving to learn to understand

what knowledge you have, what knowledge you lack,

and to continually do experiments

and work on projects that improve your knowledge base.

And I didn't do this with a great amount

of structure or planning.

I was rather just going from project to project,

doing things that I thought would be fun and cool.

And with each project I learned new things.

You know, learning about how to store and manage data,

learning how to deal with advanced data structures,

how to write complex programs

that have deeply nested data and control flow.

Each one of those, you know, provided a lesson

which were later essential, you know,

when in 1991 I released my first game

and over the course of that decade we went from,

you know, zero commercial releases

to the first generation Unreal Engine.

But you know, this was largely just using the knowledge

that I'd built up over the previous decade

just doing fun hobby projects.

And if I hadn't done all of that work,

there's no way I could have ever built

the things that came later.

- All the experimentation and all the exploration

somehow contributed, somehow made sense later on.

Like all of that is integrated

somehow in the stuff you build.

It's funny how life works,

the pieces kind of come together eventually.

- Yeah, you know, there are definitely "Karate Kid" moments.

'Cause you know,

all this time I was learning math in high school

and in college I studied mechanical engineering.

And so, you know, you learn all kinds of math,

calculus and vector math and matrices

and you know, all of these related fields,

physics and stress and strain and how to, you know,

deal with complex physical systems.

And yeah, I wasn't really sure

how engineers would actually make use of that knowledge.

Do you just like forget about it

when you actually go off to do work?

Or do you write down equations on paper?

It was actually not clear as an early engineering student

what you do.

But when I started writing the first generation

Unreal Engine and I was dealing with 3D math, I was like,

wait, I know this stuff, I learned this.

(Tim and Lex laughing)

And you know, suddenly like the "Karate Kid", you know,

you get to paint the fence and wax the car

and suddenly you put all the pieces together into, you know,

a 3D engine based on whole lot

of accumulated programming language

and math knowledge that

often knowledge gained without ever anticipating

that I might use it in that way.

- Also, I think what's useful

is over and over learning a hard thing

and then showing to yourself, you know, that you can do it.

That you can learn a hard thing.

So then when you come to having to write a 3D engine

that in ways that haven't been done before,

you're like, I've been here,

I've been here in this experience.

Like I don't know what to do, but we'll figure it out.

We'll learn, I'll learn all the necessary components.

So just not being afraid of something new.

- That's right, and constantly striving to make connections

between these fields and look for their applications.

Long after I chipped on Unreal Engine,

it was like going back through an engineering textbook

and looking at, oh yeah, I used that,

I used that, I use that.

And then I got to the section on eigenvalues,

I'm like, don't know what the hell this is.

But you know, it turns out eigenvectors

and eigenvalue were the critical breakthrough

that made the Google search engine technology work

and stand apart from the rest.

Because they found if you threw all the links

that exist in the web

and you know, links from in two different sites

and you put them in a giant matrix

and you conclude it, you found a dominant eigenvalues,

then those eigenvectors described the best search results

for different things.

And so constantly picking up knowledge

and looking for ways to put it together is the thing to do.

And if you aspire to be a programmer,

you've gotta write a lot of code

and you've gotta continually learn new things and improve.

And if you wanna be an artist, you've gotta continually

draw artwork all styles and all kinds

and constantly push yourself to learn more and more

because you never know exactly

what you're gonna end up doing in the long run.

But the more knowledge you have and the more skills,

the more chance you have putting it together

and being successful.

- And whether you're a programmer or an artist,

you should probably take linear algebra,

even though it doesn't make sense at the time.

- I found getting an engineering degree

and then never working in an engineering field, you know,

just being a computer programmer was immensely valuable.

You know, I went to University of Maryland,

which for some disciplines

it's kind of known as a party school,

but they worked the engineers to death,

worked really hard. (Lex laughing)

And if you learn any engineering discipline,

you learn massive amounts of math

and you learn the rigor of problem solving.

You know, not just what you find from the Wikipedia article,

but going through all the exercises

of solving complex problems

and building up series of solutions

to derive in an answer.

It's valuable and it embodies the knowledge

that you need as a programmer.

And you know, people often go to university

and think, okay, my goal here is to get good grades,

so I get a diploma and I prove

to an employer they're invaluable.

Like, no, that's just kind

of the superficial bookkeeping of the university.

The real purpose of all of this is to learn.

And whether you learn formally or you learn on your own,

it's the learnings that are really valuable in a career.

And especially if you're going to be entrepreneur anywhere,

it's really knowing the stuff that matters

and not having the diplomas is into, yeah,

there's ever more pressure to make rebuild society

more and more around credentials.

Do you have this certificate? Do you have that proof?

But like, you know, companies

that are focused on just building great products

and doing great things gravitate towards

people who do the great work.

- Yeah, one of the great things about youth

is there's more freedom.

There's just more time to learn.

And people, when they go to high school,

they sometimes think, "Wow, I can't wait to get out of this

and be an adult and be free."

But it's not quite freedom.

When you get a job and you start a family,

all wonderful things, you get more and more busy

and less and less time to learn in the general sense,

learn whatever the hell you want.

That is a wonderful time in life.

The teenage years, the early 20s.

The 20s when you could just learn random shit.

- Yeah, you know, I think this is something

that's kind of changing in America.

There's so much focus on grades and homework

and structure around kids' lives.

You know, when I was growing up, you know,

my mom would feed me and my neighbor's, you know,

my neighbor's moms would feed them breakfast

and they'd, you know, be like, "Well be back by dark."

(Lex laughing)

- And you know, we'd go out and we'd play

and we'd do all sorts of things.

We'd, you know, explore the woods, we'd build go-karts,

we'd, you know, salvage old pieces of electronics

and build you what we thought were

our spacecraft control panels for the, you know,

fake spaceships we were building as play.

And we'd have an enormous amount of freedom.

And you know, from basically being a little kid

through the time I went off to college,

it had an enormous amount of free time.

And some people just used that and waste it, and watched TV.

Some people socialized

and some people really got into serious projects.

So many people at all times were doing cool things.

You know, I was programming, I was learning to build things.

I was, you know, before I was releasing games to the world,

I'd be like, yeah, having neighborhood folks over

to play the things I was working on and check them out.

And sometimes they're impressed and sometimes they weren't

and they'd have their own projects

and often we'd have spare time jobs

and everybody was entrepreneurial.

Like everybody, you know, had a side gig.

Sometimes you go around and mow people's lawns

or you'd, you know, rake the leaves up

and, you know, earn money and do...

The freedom there,

and the organic learning that occurred there,

I think is something that is really critical

to the American experience.

I worry is increasingly going away

# Chapter 2

Some people socialized

and some people really got into serious projects.

So many people at all times were doing cool things.

You know, I was programming, I was learning to build things.

I was, you know, before I was releasing games to the world,

I'd be like, yeah, having neighborhood folks over

to play the things I was working on and check them out.

And sometimes they're impressed and sometimes they weren't

and they'd have their own projects

and often we'd have spare time jobs

and everybody was entrepreneurial.

Like everybody, you know, had a side gig.

Sometimes you go around and mow people's lawns

or you'd, you know, rake the leaves up

and, you know, earn money and do...

The freedom there,

and the organic learning that occurred there,

I think is something that is really critical

to the American experience.

I worry is increasingly going away

as society is ever more protective and sheltering

and makes it harder to get these experiences.

- So on the video game side,

when did you first fall in love with video games?

- I've had a funny relationship with games

because my real aspiration has always been

to program cool stuff.

I get more enjoyment of programming

than anything else in the world.

And so, you know, my first really two formative experience

with games were playing

this game called "Adventure" for the Atari 2600.

It was like you moved this dot around the screen

and picked up objects like swords and fought dragons

and invaded castles and solved puzzles.

Very, very simple iconic stuff, you know,

rather than realistic graphics.

And then the other game that really got immersed in

was "Zork," which was a text of adventure game.

It would tell you where you are and what you see

and you type in commands like "go north" or "pickup sword"

or "open door" and explore a world that way.

So the game didn't have any graphics,

but in your mind you had this elaborate picture

of what you're seeing there.

And it really brought inspired imagination

more than other things.

And playing those games led me to (indistinct)

and where I learn to program everything that I saw there

and that drove a lot of my programming.

I learned how to move a player around the screen.

I learned how to, you know, build a design tool

so I could build castles and save them off

and then play them in a game.

And I realized there was a separation between the tools

that you use to build a game and the game itself.

And that if the more powerful tools you had,

the more creativity you could unleash in yourself or others.

And you know, I learned all the programming techniques

that supported games, how to parse text, you know,

pick up sword and go north, how do you make that sentence

into an actual series of commands on the computer?

And that was really, really exciting.

I have to say, until the time that "Fortnite" came out,

I played video games primarily to learn what they were doing

so I could go off and do that myself.

You know, I'd sit down, you know,

when "Wolfenstein" tying came out

and then "Doom" came out, you know, I'd go through

and look at pixel by pixel, I'd move the mouse very slightly

and look exactly what was happening to figure out.

- That's great.

- What technique was being used there

and that was a puzzle solving at a grand scale.

And it was so fun.

- So, take me there in the early '90s.

So you launched Epic Games in 1991,

so the writing of your first big video game, "ZZT".

What was it like? What was the technical challenges?

What were the psychological challenges of building that?

- It was a funny project

because I didn't start out to build a video game.

I just moved from an Apple II that,

so my brother bought my family an Apple II

right after I'd visited him in California.

So I've been programming on that for a few years.

Learned a lot of techniques,

but weren't many Apple II users around still

by the time that cycle came to an end.

And so I'd just gotten an IBM PC of my own, I was learning

to program and I realized I needed to text editor.

So I started writing a text editor, you know,

a text editor is a program to edit text files.

You have logic to move the cursor around

and let people type things and backspace and delete

and do all of those, you know, mundane actions.

And you know, one night I was like, I finished it up

and I was like, well, okay,

I have a text editor, but this is pretty boring.

And so I made the cursor into a smiley face character

and I had the like different characters you could place

in this document, perform different gameplay actions.

Some would be walls and some would kill you

and some would be moving objects

that could fly around the screen.

And so this text editor that I made evolved

into little game editors.

So I was building these levels for a game.

I put a lot of time into like building an editor

and a primitive set of objects,

about 20 or 30 different objects,

enough to build a really cool and compelling game,

but not so many that players would lose track

of what they're seeing.

I started off just building different game levels.

You know, the idea is you'd be on a series of board,

they'd be connected by, you know, going north

passed the end of the current board would take you

to a new one if it was open

or maybe it was block and you couldn't go there.

I built the whole game world around that

and you know, this was the game that became "ZZT."

And I was having fun with it, building it and playing it,

but I didn't know if it would really work.

So I did this experiment.

I started inviting neighbors over, like some adults,

some kids of all different ages and sat them down from it

and said like, "Here's a game I made.

Figure it out." (Lex laughing)

And you know, I had to force myself not to tell them

what they need to do, right?

Because I really wanted to learn if they were able to,

you know, discover it all for themselves.

You know, today we would call this, you know,

user experience test

and there's a whole field to research

around user experience research,

but back then it was just inviting

some kids over to play the game.

I took notes about what they got stuck on

and what they enjoyed and where they felt bored

and just iteratively polished the game

until I felt it was good and I put it out

and released it on, well this was before the internet,

so there were Bulletin Boards.

I upload it to a bunch of local Bulletin Boards

and from there it started spreading

because, you know, the way to build up cred

for Bulletin Board users was to upload new files

and to claim that,

"Hey, I was the first that brought this to you."

And you know, so there was a natural tendency

of the software to spread.

I decided to use the sharer model, you know,

so I didn't just build this one game.

I built a trilogy of three games.

And I released the first one for free

and I said, "Hey, if you'd like this, buy the two sequels."

And yeah, I included my parents' mailing address

and said, you know, "Send us $30

and you can get the sequels to this game."

And the checks started coming in within a few days. (laughs)

And I was making like, getting three or four orders a day,

I was making like $100 a day.

I'm like, "Woo, I'm rich." (laughs)

Because, you know, being a 20-year-old,

that was like a pretty big deal.

- What did that feel like, just getting money

and probably feeling this immense success

from something you've created?

- Well, you know, I looked at money always just as a tool

to help you fund accomplishing cool things.

And you know, having enough

to do the things you wanna do is the critical thing.

It's always been just very utilitarian,

but the knowledge that other people all around the country

and all then, you know, and a month later,

all around the world were playing the game

that was mind-boggling.

You know, that me, like this little kid, who'd put out

a game on a local Bulletin Board

could be doing international business

and shipping discs all over the world to players,

you know, because the software was spreading on its own.

It was just magical.

And that was a new thing for software.

Like that did not happen with mechanical devices.

Like you manufactured one, you sold it to somebody

and they had it and that was it.

But software could spread.

That was just really cool to see.

And it made me realize there's really no upward limit

on the potential for business like that.

You know, we saw Microsoft as a big juggernaut company

at the time, but it was like, hey, you know,

if that Epic does games good enough, you know,

we could accomplish what they've accomplished

with operating systems.

And the sky was the limit.

And I think this is the age we live in now,

you don't have to be an industrialist

manufacturing physical products.

Anybody who builds anything digitally,

if it's good enough you can reach the entire world

and build the, you know, next Microsoft or Meta or Apple

or Google or Epic Games.

- It's such a cool origin story though.

You start out building a text editor,

so you're looking at this project,

you're playing around with it, you're building up the tools

and it's such an inspiring moment

'cause a lot of us start out building a project

and to allow yourself to see the potential pivots,

the potential trajectories that can go is really nice.

To sit back, allow yourself to be bored

and like, "Ah, I'm gonna go this way."

I mean, that's like a crossroads.

You came to a crossroads.

I mean, you built, you know, compilers,

you design your own programming language,

you built compilers, databases,

all this things you mentioned.

And you started building a text editor

and then here came to this crossroad,

I'm gonna make this fun.

And then from there, you know,

one of the most legendary gaming companies was created.

It's kind of cool,

like that's an inspiring thing for sort of developers.

Like be open to the possibility of creating something

you didn't plan to create and just go with it.

Right, that's cool.

- Yeah, and it was a bunch of learnings emerged

really quickly there.

The neat thing I did with "ZZT" was I didn't just release

the game, I also released the editor with it.

I built this tool so I could make these "ZZT" boards

that people could play, but I also gave it

to all of the players themselves.

And you know, like 30 years later I still run into people,

you know, when I go to a game industry event, it was like,

you know, "I grew up playing 'ZZT.'"

And you know, here's an adult who grew up playing my game.

(Tim laughing)

And it was because it enabled anybody

to become a creator too.

It had, you know, this old board editor

and it also had a little scripting language

so you could learn a little bit of programming in it too.

And it kind of impressed

and it really set a formative principle of Epic,

which was that, you know, the company's mission

is to make awesome entertainment, but also awesome tools

and to share those tools with everybody

so that they can build their own amazing things too.

And when we got into Unreal Engine a few years later,

the interplay between us building a game

and us building tools that were widely used

by others was a critical part of that.

And I think that's the sole reason

that Epic has been massively successful.

And actually the reason that we've survived

all of this time is that by serving both creators

and gamers, we've been able to weather

the ups and downs of the game industry.

It's a brutal place for companies.

We've been able to survive every financial downturn

and sometimes the Engine's been funding the business

because we didn't have a game.

And sometimes the games have been funding the business

and it really set a principle in our culture

that's persevered and is continually

bought to their forefront.

- But on the editor front,

that's such a fascinating philosophy

that you always allow people to create their own worlds.

You have an engine from which you simulate the world

that the game is in.

You have the actual game

and you also have the freedom for creators to create

various, you know, in "Fortnite" islands of their own.

It's like with everything you ship,

that freedom to create is always there.

That's really interesting.

- Yeah, and it's something we aim to do

more and more fully over time.

You know, in the course of building "Fortnite,"

we've built a lot of other tools,

they're useful for us too

because it's not just a game powered by Unreal Engine,

but it's also, you know, a social ecosystem

where people can make friends and voice chat

and get together and parties.

And we've opened up all of those social features

into Epic Online Services

and we give them away to all developers for free

because we all benefit from growth and that user base.

And, you know, our goal is ultimately

to build the company's products

and the same technology that we share with everybody else.

And to hope that foster a bigger and bigger ecosystem

over time where everybody benefits.

- If we could just linger on the '90s, (laughs)

so you said Bulletin Boards, maybe you can explain

what that's like and also explain the birth of the internet,

what that was like?

What was the internet like in the '90s?

- So the internet is a funny thing.

It started out as this Defense Department research project

called the ARPANET,

the Advanced Research Project Agency Network.

And it's kind of like this secret thing.

That became more and more open

as they connected universities.

Universities connected to the internet in the,

you know, mid 1980s.

And so if you're at a prestigious institution

with access to computers, you could get on there.

But as a consumer, back then we had these modems, you know,

this thing you plug into your phone line

and it dials up on phone number

and then, you know, it sends wild sound effects

over the telephone line

to send digital signals back and forth.

And these were really slow three, you know,

the first modem I had was 300 bauds.

That means 30 characters per second of data.

So you're like sitting there watching a sentence

like slowly emerge character by character

as you're going online.

But you know, that's how we got online

and we talked with each other.

So you dial up to a local Bulletin Board,

it'll be run by a person.

Usually they have a computer or two sitting in their kitchen

or something that's running the Bulletin Board

and they have a small community

of a few hundred users all competing

to connect to that one phone line.

It was often busy and you couldn't get in.

And the more popular Bulletin Boards were hardest to get to.

But you had all kinds of communities develop,

you know, and you could see like there was

the programming communities

where people talked about programming.

There was the news and events, you know, community.

I lived in the outskirts of Washington DC

so that was like a big thing.

But then there was like the pirate community

where they're sharing pirate at Apple II games

and you know, very different community ethos

and mantras out there.

But all, you know, all really nice and also very small.

These Bulletin Board couldn't grow to the size of Facebook

'cause your phone line couldn't take that many calls.

And, you know, then later in the 1990s,

the internet which had been fostered in these colleges,

that started opening up for the public

and anybody could connect to it.

And suddenly the world took on life of its own.

It became much, much easier to reach global audience faster.

- And you would start shipping games to the internet,

which is a bit of a crazy thing to do

because you're supposed to have like a, you know,

a physical copy,

but to post on the internet is pretty innovative.

Even shareware is pretty innovative.

- Yeah, yeah, it's been a funny transition

for the game business.

You know, Epic started out making shareware games

distributed digitally,

but you know, as the first 3D games took off,

like "Wolfenstein" and "Doom" from id Software

and then Unreal from us, took off, you know,

to reach a huge audience of billions of users,

we had to go into retail stores.

So we worked with a retail publisher and they made a box

and they put CD ROMs in the box .

And you know, then the world started transitioning

back to digitally, like,

and that transition didn't start well, right?

The initial transition of gaming to digital

was all but BitTorrent, all piracy.

And the other horror stories about games that would,

you know, sell like 100,000 copies

but have 2 million users

'cause most people pirated it.

And then, you know, Steam came along

and introduced digital distribution

and made digital distribution of legit games so convenient

that most players moved away from piracy towards that.

And you know, their practices followed by others

and the early digital industry took form.

- Yeah, it's fascinating.

I mean, pirates do lead the way for innovation. (laughs)

The same as the story of Spotify.

You basically, I think most people when they derive value

from things like video games,

want to pay for those video games,

they just want it to be easy.

And so the same thing with music with Spotify.

But maybe just staying on the '90s,

they're gonna be a lot of indie game developers

will listen to us talking today.

# Chapter 3

you know, sell like 100,000 copies

but have 2 million users

'cause most people pirated it.

And then, you know, Steam came along

and introduced digital distribution

and made digital distribution of legit games so convenient

that most players moved away from piracy towards that.

And you know, their practices followed by others

and the early digital industry took form.

- Yeah, it's fascinating.

I mean, pirates do lead the way for innovation. (laughs)

The same as the story of Spotify.

You basically, I think most people when they derive value

from things like video games,

want to pay for those video games,

they just want it to be easy.

And so the same thing with music with Spotify.

But maybe just staying on the '90s,

they're gonna be a lot of indie game developers

will listen to us talking today.

Can you go back to that mindset

and try to derive some wisdom

and advice to those folks when you were just

a solo developer, maybe just a small group of people

creating your early games

that eventually became this huge gaming company.

But in the early days,

what were you going through?

What were the ups and downs?

What did it take to sort of stay strong and persevere?

- Well, you know, one of the critical things

that Epic always worked hard to do was

to make something different that nobody else was doing.

And to try to satisfy a small audience

rather than competing globally

with the game juggernauts.

You know, back in the 1990s, Epic was new,

but Electronic Arts and Activision

and the other big publishers had been around for a decade.

And they were huge companies.

It had giant retail distribution networks.

You know, if I tried to make a game

and then convinced them to publish it,

I doubt I could have had a chance.

And I doubt even if I made a successful game,

that I would've made much money from it,

though they might have.

And you know, so the really unique angle to Epic

then was shareware.

And that was just the idea

that if we distribute our game differently,

then we can reach a much larger audience

than these bigger competitors

by virtue of this first episode of the game being free.

You know, it was kind of the advent of

what later became free to play.

And the logic of that is just as true now as it was then.

If the thing is free and anybody can get into it,

then it's kind of spread from friend to friend

as people bring, you know, their real world friends

into the games they're playing

and, you know, have the opportunity

to build up a community around that.

You know, so the other lesson there was just minimize

the friction of people getting into your game.

Make it easy to get into and make it fun.

And I think the other, well I was very fortunate,

"ZZT" was a funny game.

It was not like, much like any other game,

it was had much worse graphics

'cause it was all just text characters, smiley faces

and, you know, other Greek letters

and things participating in this game simulation.

They were kind of iconic representations of characters

rather than real ones.

And you know, this was decades into the age

of real graphical games with interesting graphics.

And so it wasn't even trying to compete in that area,

but it was able to compete in a different area,

which is that, you know,

it wasn't just the three games I'd made

and shipped as a trilogy that were successful

and drove the success of the product.

It was the fact I released an editor

and there's a whole community around it.

And you see that trend is repeated itself.

Like there was know "ZZT" was one of it.

Before that there was

"Bill Budge's Pinball Construction Set,"

that was a 1980s Apple game

that let users build their own pinball tables.

And since then you've had

some of the world's most successful games follow that path.

Like "Minecraft," you can build your own stuff.

"Roblox", now "Fortnite Creative"

and underwriter for "Fortnite."

You know, games that become platforms for other people

to build stuff was a real opportunity.

You know, I think the big thing to realize

as for indie developers right now is like there's massive,

massive competition in every major genre.

And it's very unlikely unless you just happen

to be the world's best at a particular thing,

that you're gonna release a game

in an existing highly competitive genre and win.

A much better chance of success

is in releasing something that hasn't been done before.

Being really unique and reaching an audience,

even if big or medium size or small, reaching an audience

and becoming really popular with that.

Making some money from it and being able to reinvest

and then expand towards your ultimate dream.

You know, I think the one shot go from idea

to commercial success at massive scale is a lot less likely

than the multi-step process of continually build better

and better stuff over time

until you get into a position of excellence.

- And constantly try to do something

that others aren't doing.

- Yeah, that's right.

'Cause if you look at every market,

there's a few markets where the current leader

came late to the space,

usually because the prior leader failed to horribly.

But most of the time the, you know, the company

that's succeeding and winning in a market is the first

or second entrant there.

They've just continually buoyed their success.

- Great advice and fascinating.

But on a human level, was it lonely?

Was it scary you sitting there as a developer?

- I'd say it was the opposite of lonely

because, you know, the thing that spurred me

to actually release this was seeing kids playing the game

in my neighborhood and having fun.

I mean like, this is really good.

And seeing them enjoying it and laughing

and pointing at the screen and, you know, getting together

and just wanting to play more.

- [Lex] That's awesome.

- Yeah, and the human element was always pervasive,

you know, because I did not only receive orders,

but people would actually write letters.

You know, we wrote letters back then in the 1990s.

People would say how much they're enjoying the game

and how their kids were playing the game

and so on and so on.

So, you know, they felt very connected.

And you know, I think a lot of businesses have

to make scary decisions

because you're spending, you know, potentially

all of the money you have to take a shot at something

that you're not sure will succeed.

I was very fortunate starting a business like this

because it didn't really need any capital.

The capital is, well,

the several thousand dollars in computers I'd bought

by mowing lawns. (laughs)

And it wasn't much risk if that hadn't succeeded,

I guess I could have figured out

how people get mechanical engineering jobs and pursued that.

But once it took off and once the orders started coming in

and people started writing letters saying

they're enjoying the game, I knew I was gonna go all out

and try to build a company there and succeed.

And that was like gonna be, you know, my big goal.

- So I'm sure people know,

but Epic Games was created in 1991

and went on to transform the gaming industry several times,

one of which is Unreal Engine.

So let's talk through the origin story of that.

You said that when "Wolfenstein" and "Doom" came out,

that changed everything.

So take me to that moment.

- Yeah, that was a very interesting time.

Epic had, after my first couple of games

that had recruited developers, you know,

usually college students, high school students

who are just working on their own, had real skills

but didn't have an outlet for their work.

Epic had been matchmaking the best artists

and programmers together from all over the world.

Like "Jazz Jackrabbit" was Cliff Bleszinski,

a high school kid in California,

who had made a really cool adventure game

together with Arjan Brussee,

a demo coder from Holland

who would make amazing graphical stuff

and had built a 2D game engine and connected them together

and a musician Robert Allen in California.

And they, you know, by telephone and modem and so on,

we were building these little 2D games

and having quite a lot of success.

You know, there were a bunch of people making

thousands of dollars a month while they were still students

and royalties from the games.

The Epic was kind of producing

and by coordinating people and publishing through shareware.

And that was all going great.

The company had a little office

and we were, you know, copying floppy disks

and mailing them out.

But when "Wolfenstein" came out, we realized like

the future of gaming is gonna be 3D.

There had been a lot of experiments in 3D before

that hadn't been great.

You know, there were 3D renderings of mazes

that were not in real time

and you're always looking north, south, east or west.

And then there were vector graphics

with little wire frames moving around and things.

But you know, "Wolfenstein" was the first game

that was fast enough, you know,

running at 30 frames per second.

It really felt immersive.

It felt like you were there,

like you were, you know,

in this castle Wolfenstein fighting Nazis.

And that was a really amazing and immersive experience.

3D graphics were pretty primitive then,

id Software followed shockingly fast with "Doom",

which was much, much more capable 3D engine,

which had, you know, stairs

and though it was still what we saw,

2.5D it was environments

that were very realistic textures that were very realistic.

You know, a form of lighting that was approximate

but incredibly realistic

and just such great artistry and sound effects.

It feeled completely visceral and real.

You know, you might look at it today from a,

you know, point of view of a modern, you know,

game player with, you know, 20 teraflops of computing power

in your device

and say, "Oh, that's not very impressive."

But it was amazing at the time.

- I mean, for me, just sorry to pause on that.

I think "Wolfenstein" was one of

the most amazing moments of my own life.

Just being able to, like you said,

in real time move about a three-dimensional world.

I just remember just moving around

just in like, what is that feeling like?

I mean, you feel transported into another world.

- You feel that you're there, yeah.

And especially when you turn the lights down in your room

and you turn the sound up on your speakers

and it'll scare you. (laughs)

and you'll feel like, you know,

that fireball that's coming at you is gonna kill you.

That was an amazing time

'cause we hadn't experienced that before.

There was nothing like that.

You know, you'd watch a movie,

a scary movie or whatever, you know,

it was just this thing that was happening.

This was you, this was you in a 3D world.

- So how did that change Epic,

this realization that the future of gaming

is going to be 3D?

- Well, at first I was really depressed, I think

(Lex laughing)

because the wizardry of "Doom" especially was so incredible

that I gave up on programming for like six months.

I was like, "I won't be able to compete with this.

I have no idea what we're gonna do."

We just keep making 2D games

and hope that the business goes on.

But like, that was the nature of Carmack's wizardry.

He had done things that were like,

not just one innovation leap ahead,

but like a dozen simultaneously,

interplaying in a way that you couldn't pick them apart

into their component pieces.

But funny thing happened,

Michael Abrash, long timer in computer graphics

that wrote a book on the techniques

for 3D graphics and texture mapping.

And he wrote some articles

in one of the programming magazines of the day

and explained it and showed assembly code

to do texture mapping, you know,

drawing these 3D graphics on the screen.

And it was actually really simple stuff.

I was like, "Oh, I can do that." (laughs)

And you know, so a bunch of us Epic independently went off

and started writing our own 3D graphics code

to figure it out.

And we found at one point we had a number of people

dabbling in this, doing different parts of it.

And at that point we decide, okay, this is 3D graphics

and 3D gaming is gonna completely change the world.

We need to go all in on this.

And so we took the best people

from our best 2D game development teams

and put them all together to make a 3D game.

We didn't really know what we were doing at the time.

None of us had ever shipped a 3D game

and most of us were still learning,

but everybody was like trying different disciplines

to see what they were best at.

And it was a combination of a bunch of people

who came together to make Unreal.

I'd initially volunteered to make the 3D editor

for the thing, and James Schmaltz

who had made "Epic Pinball."

"Epic Pinball," now that wasn't a crazy game.

This was one of the 2D shareware games.

He made it while he was in college

and he was making like $30,000 a month from, you know,

the royalties from this game

because everybody had wanted an awesome pinball game,

it was massively successful.

But he was a multidisciplinary person.

He wrote the code for the game, the art for the game,

and did basically everything.

And the code was 30,000 lines of assembly language.

(Tim and Lex laughing)

And so he was initially gonna write the 3D engine

and I was gonna write the editor

and he sent me his code

so I could integrate into the editor.

It was like just a giant pile of assembly code.

I was like, "Hmm, why don't I just write this myself?"

And so James instead started going off

and building 3D models

and 3D animations using the tools at the time.

And so Cliff, who had done a lot of design work

and built the level on "Jazz Jackrabbit" went off

and started learning basics of level design.

And so I was writing this editor

and Cliff Lesinski was customer number one for it,

starting to go off and build levels.

And James Schmaltz was drawing awesome creatures,

sending them to me.

I get them implemented in game.

And then we brought an animator to bring them into life

and we brought in, you know,

more and more people until

at the peak of Unreal 1 development

we had about 20 people working on,

which was a huge team for the time

and was really stretching Epic finances

nearly to the breaking point.

We barely survived

and almost ran out of money a number of times,

but somehow we always pulled through.

And it was a crazy project

because it was three and a half years of development

in a game that we always thought was six months

from shipping. (Tim and Lex laughing)

You know, it was like a, you know, three and a half years

of 70 or 80 hour weeks for most everybody

working on the project,

not even knowing what problems we'd need to solve next

because we were so immersed in the current ones.

- Were there moments when you were losing hope

that this might take too long

and the company will run outta money?

- We were always very financially stressed,

so I was continually worried about that.

I had total confidence

that we'd work out all the technical and artistic problems

'cause yeah, we knew the pieces

and it was largely a matter of typing code in

and solving some problems.

And kind of like we knew we could ship a version of it.

And the thing that was continually

really interesting was the ongoing discovery of

new techniques as we went.

You know, 'cause at the time "Quake" had shipped,

it had a little bit of dynamic lighting.

Unreal really pushed dynamic lighting much higher

than anybody else had done before.

Even colored dynamic lights

with some shadow casting capabilities,

statically or moving lights without shadows.

And figured out how to do volumetric fog

so you could have foggy areas that were full of lights

and you get the kind of glow of the lights

standing out in the fog

and affecting the appearance of the level.

A whole lot of amazing techniques came together to build

a game that, you know, made a number of leaps

ahead of the state of the art at the time.

Yeah, it was really crazy,

but like, I think most companies

wouldn't have survived that,

but the sheer talent of the people involved

made it possible.

Epic has often done things that

most companies would've failed at and we succeed.

Like, not because of awesome management or awesome planning

or awesome financing, but because of the sheer talent

and willpower of the people involved to make it happen.

- What about the interdisciplinary aspect of it?

Like you said, sort of artists, engineers

or programmers, designers, all of them working together.

What was that the 20 people,

What was the dynamic there, like working insane hours?

Like what was it like to sort of make a team like that

work together well as an orchestra

to actually deliver the game?

# Chapter 4

a game that, you know, made a number of leaps

ahead of the state of the art at the time.

Yeah, it was really crazy,

but like, I think most companies

wouldn't have survived that,

but the sheer talent of the people involved

made it possible.

Epic has often done things that

most companies would've failed at and we succeed.

Like, not because of awesome management or awesome planning

or awesome financing, but because of the sheer talent

and willpower of the people involved to make it happen.

- What about the interdisciplinary aspect of it?

Like you said, sort of artists, engineers

or programmers, designers, all of them working together.

What was that the 20 people,

What was the dynamic there, like working insane hours?

Like what was it like to sort of make a team like that

work together well as an orchestra

to actually deliver the game?

- Yeah, that's one of the really unique things

to exist in gaming.

Not in normal big tech companies, which are just engineering

and business driven,

but gaming really does require all the best people

across all the creative disciplines working together.

And, you know, Epic had grown organically

by recruiting people with awesome talent.

We always had a limited budget we could never pay to hire,

you know, bid up people's salaries

and hire them away by paying them more.

We just had to find awesome people who were

at the beginning of their career and put them together.

And, you know, so everybody was very new to this

and didn't have any assumptions about how companies worked.

And so, you know, you put all these people together

and, you know, it was really a constant interplay of talent

as people were learning how to work together as a team.

Nobody had management experience.

Most people hadn't chipped at a game

before they worked with Epic.

And we were figuring out as we went,

but it was a constant iterative cycle.

You know, we'd make several new versions

of the game every day.

Be a new compile, introduce a new feature

or fix some bugs, get to the artist,

artist improve their levels, continue building stuff,

and then we see what they're doing in their levels.

Like, ah, I see what you need now.

We'd constantly be improving the tools

and just the iterative process

and the speed at which that improves products

is the critical element to success in games.

The slower the iteration cycle,

if you make a build every week

and you go through one iteration every week,

you're gonna be way, way, way worse by the end

of your project than a game company

that makes, you know, new stuff every day.

And that was the magic that happened together.

And there was really nothing but passion

and everybody's individual dedication to it

that made it work.

- I heard you still program,

but how much programming were you doing back then?

You mentioned the hours, probably insane hours.

So like, it'd be almost fun to talk about your setup set up.

What a day in the life of Tim Sweeney in the '90s

when you were building Unreal look like?

- Well, we'd all gravitated towards

a work schedule that maximized productivity

and that usually meant waking up late.

I get to like, usually get to work around noon

and usually work till like 2:00 AM or so 3:00 AM sometimes.

And, you know, I didn't have anything else going on

in my life,

so usually just work and sleep and occasional eating

and yeah, I found I always needed eight or nine hours

of sleep a night.

Without good sleep, I would just become a zombie

and wouldn't be nearly at my best.

So I always needed to get sleep,

but I didn't need anything else going on.

So the programming itself was so energizing and drawing.

Yeah, so it was a, you know, three and a half years of that

during the project.

Mostly spent programming, I'd say probably 60 hours a week

of programming, five hours a week of coordinating

with other people and iterating

and you know, sitting down with them

and looking at what's going on and screen

and figuring out what they needed.

Maybe five hours of business stuff, you know,

there's a good division of labor then.

I didn't have a big executive team,

but it was like basically myself running the technical

and development part of the company

and Mark Rein running the business part of it,

doing deals and, you know, maxing out his credit card

and going around the world

bringing in sources of revenue to keep the company funded.

- What programming language, are we talking about C?

Because you mentioned there's this pile of assembly,

what was your decision in choosing

the programming language

that Unreal Engine would be written in?

- I'd grown up learning with Pascal as my favorite language.

In order to just get maximum performance

and get the latest operating system features

I had to move to C for my second game, "Joel of the Jungle,"

well, Nintendo style platformer.

And so when I started Unreal Engine, it was

on 16 bit Windows using the C programming language.

And over the course of the first year

it moved to 30 terabit one,

you know, 30 terabit, you know, using these Doss extenders

and then using Windows NT.

And I moved to the C++ language

and just because it simplified the code so much.

Went from a really complicated pile of code

to a much simpler one making that transition.

And so almost the entirety of Unreal Engine development,

about two and a half years of it was all on C++ 30 terabit,

completely stay of the art then,

like 30 terabit protected mode

was kind of a magical thing having come from the days

when computers were much less reliable

and crashed all the time.

- Yeah, and turned out to be a pretty good bet

'cause C++ out of all those languages

ended up being the dominant sort of

performance oriented language that survives to this day.

- Yeah, yeah, it's because it solves

all the problems at scale,

often through manual pain, but always solves them.

And yeah, a lot of other languages do better

and a lot of like theoretical aspects

and are better for some usage cases,

but you can't do everything

and that's really very limiting.

- All right, so ridiculous questions,

but like, did you have one monitor, two monitors?

Were you picky on the keyboard?

Were you picky on the chair?

What are we talking about?

Let's paint a picture.

- Okay, I went through a big transition there.

So I started out being pretty lazy.

I'd had a bunch of, like, I bought used computers

'cause you'd often get them at half the price of a new one.

They'd be good enough.

So I had this old 46 I was developing on,

I guess it was a 15 inch monitor at the time it was all,

it was a poor workstation set up,

but it was very economical.

And so as we started on Unreal, I realized that

like I had to write a ton of code.

I had to write absolute maximum productivity.

So I had to rearrange my entire life

around delivering maximum output.

And so at that point I realized like actually spending money

on getting good equipment was a good investment.

And we're not talking about millions of dollars here,

or billions if you're building a GPU farm.

We're just talking about buying some basic hardware.

And so I bought the biggest CRT you could buy at the time.

'Cause this was a CRT or it was 24 inches,

it weighed like a hundred pounds. (laughs)

I had back pain for a week after I installed it,

but it got me 1920 by 1200 view

- Wow, nice state of the art.

- In 1996, that was pretty cool.

So I'd upgraded to a 90 megahertz Pentium (indistinct)

programming on that.

It was on the 90 megahertz,

these were the main consumer computers at the time.

And I'd optimized the Unreal Engine software render on that,

which was, you know, the Pentium was

the first super scaler architecture in consumer computing.

It could run up to two instructions at a time.

And if you wrote your assembly code very carefully,

you could get absolute maximum throughput.

You know, so I'd gotten my texture mapping code down

to six CPU cycles, comprising 11 instructions.

And, you know, that was required

for every pixel on the screen.

And that was just enough performance to deliver that.

But Dell came out with these new workstations

and Intel I just launched the Pentium Pro,

the first out-of-order processor.

And so I like basically bought the absolute maximum

configuration that money can buy.

It costs $7,000.

I had a gigabyte of memory in 1996

and a 200 megahertz CPU. - [Lex] Wow.

- So it like tripled the speed of compiles

and just made me massively more productive.

So that's what I was using

throughout Unreal Engine development and chipped with that.

- By the way, people in the '90s would've been blown away

by this workstation. (Lex laughing)

I love it, yeah, yeah.

In writing, were you considering the hardware much?

Was there a sense like, so you know, for people

who don't know on Unreal Engine rendering,

I guess is all software doesn't use the hardware,

but were you trying to optimize, as I understand,

maybe you can correct me, but like were you trying

to optimize to the hardware at all?

- Well, at the time,

so we did most Unreal Engine development

before the first real GPUs came out.

And, you know, the 3D effects Voodoo 1.

The first GPU actually delivered serious performance

compared to software rendering.

The first GPU that was really gainful came

into the development and we supported it really quickly,

but it was not the target all along.

And so development was focused on just building,

there are two parts of the engine, right?

There's all of the gameplay systems

that manage the simulation and physics and so on.

That's all written in very high level C++ code

and maintainability is as much of a goal as performance.

You know, because we had to build massive amounts

of systems over time.

But one thing that was really bottleneck was graphics.

You know, the cost of rendering a single pixel

was really high.

And so you had to do everything you possibly could

to optimize the rendering of pixels on screen.

And you know, so we were talking about how many CPU cycles,

you know, and you say your CPU runs at a gigahertz

or whatever, it's a, you know,

a billion instructions per second.

How many instructions do you need to run

to get APIX on screen?

And so there was a constant challenge to optimize that down.

And you know, there was also competition

among all of the graphics programmers

who often send the emails,

you know, like bragging to each other about

what new technique they've discovered, you know,

to try to get the cost down.

And Abrash's original articles took like 12 CPU cycles

to render a pixel and you know,

everybody else had figured out how to get it to like

down to six or sometimes even four cycles.

And, you know, that involved lots of different trade-offs

of caching and memory hierarchy and so on.

It was just like a magical time

where a human could actually understand exactly

what the CPU was doing under the hood

and could write code that exactly targeted that.

And that's largely lost now.

When we talk about optimization and software now,

it's largely about heuristics

and statistically your, you know,

this memory access is likely to hit the cache

and you know, this algorithm is faster than that algorithm

because CPUs now have such advanced out-of-order execution

that you really can't micromanage what's happening

on an instruction by instruction basis,

you can only manage the aggregate performance of code.

And so there's kind of this lost art.

Some people miss it, some people don't,

in which the programmer had absolute control

over the machine and could work miracles

in special cases if you tried.

- It seems like there's still value to that art

when it comes to GPUs and ASICs.

So basically trying to understand

the nuances of the hardware

and how to truly, truly optimize it,

whether it's for machine learning applications

or for ultra realistic real-time graphics applications.

Is that true?

- Yeah, that's absolutely so.

You know, the optimization problems have just moved around.

In a system like Nanite,

the virtualized micro polygon geometry system

that Brian Karis, a brilliant engineer with Epic built,

was just one of those multi-year optimization efforts that,

you know, required him understanding everything

from the highest levels to the lowest levels of the hardware

to figure out how to,

you know, make this breakthrough technique work in a way

that was actually maximally performant on GPUs.

- And so Nanite is the system will jump around in time

that takes us to today with Unreal Engine 5.

It's the system that does the geometry?

- [Tim] Yeah. - So rendering

the world sort of geometric, there's many layers to this.

We'll probably sneak up to each of those,

but one, you have to actually create the geometry

of the world around you

and do that in real time and really efficiently.

And there's a bunch of different ways

to optimize that.

Can you just speak to it?

- Yeah, you know, with the advanced art tools we have today,

it's really easy to create a scene

with billions of polygons.

The hard part is how to render it efficiently

because you can't render billions of polygons in a frame.

Basically you wanna render an image

that's indistinguishable from the full detailed geometry

if you rendered it at ridiculous cost.

And so the challenge is how to simplify every component

of the rendering, you know, the geometry, the lighting

and so on down to real-time techniques.

They're efficient, they capture a realistic view

of what's around you.

And so when an object is up close to you,

you want to render it with a lot more polygons

than when it's far away.

But one of the cool principles of f max

is the Nyquist sampling theorem that says

if you're trying to reconstruct a signal, there's a limit

to the amount of data you need to bother capturing.

If you wanna render a texture at a certain resolution,

then you never need more than twice the pixels

than in the texture that you have on the screen.

And that, you know, that's called the Nyquist limit.

And so one of the challenges of computer graphics

is given the need to render objects

at extreme closeup distances and extreme faraway distances,

you always want to be able

to generate the right amount of geometry

so that you have enough to be indistinguishable

from reality, but not any more than necessary.

And you know, with geometry, the idea is that

if you render two triangles per pixel, you should get

an image that is indistinguishable

from thousands of triangles per pixel.

If you render less than two triangles per pixel,

you're going to start to see visible artifacts of the loss.

And GPUs have this amazing hardware

in a lot of different pipelines,

but it's all very fixed function.

There's pixel shader hardware,

there's geometry processing hardware,

and then there's triangle rasterization hardware.

And one of the limits of GPUs

is that the triangle rasterizers

are built for pretty large triangles.

If you're building a triangle

or rendering a triangle with 10 pixels,

that's pretty efficient.

But if you're building or rendering a triangle

with one pixel, it's very inefficient.

So one of the breakthroughs Brian made was

to design an entire pipeline

for avoiding the rasterization hardware in the GPU

and just going straight to pixels

and calculating what should be done with that pixel

as a result of some ray tracing

and geometry intersection calculations

done in a pixel shader.

So instead of using the triangle pipeline,

we're just using pixel pipeline

and... - Wow.

- [Tim] Getting a better result.

- Because of the limitations

of the triangle rasterizer in the GPUs, that's fascinating.

Because as you described, you need tiny triangles

for the detail, for the stuff that's up close.

I mean, this might seem obvious to people,

but it's not just stuff up close.

It's like, depends where you're looking,

like the human eye and the human focus

and the human attention mechanism

defines how much detail you wanna show

because the thing that the human is likely to be

giving attention to, you want that

to be super high resolution.

And everything else, including due to distance,

can have less geometry and less texture,

less information in it.

- Yeah, yeah, that's right.

But there's a lot of challenges like that.

It turns out it's a lot easier to render one frame

that looks perfect than it is to render a, you know,

# Chapter 5

- Because of the limitations

of the triangle rasterizer in the GPUs, that's fascinating.

Because as you described, you need tiny triangles

for the detail, for the stuff that's up close.

I mean, this might seem obvious to people,

but it's not just stuff up close.

It's like, depends where you're looking,

like the human eye and the human focus

and the human attention mechanism

defines how much detail you wanna show

because the thing that the human is likely to be

giving attention to, you want that

to be super high resolution.

And everything else, including due to distance,

can have less geometry and less texture,

less information in it.

- Yeah, yeah, that's right.

But there's a lot of challenges like that.

It turns out it's a lot easier to render one frame

that looks perfect than it is to render a, you know,

a series of frames in motion that look perfect.

A lot of the problems with the earlier algorithms

that aspired to do the sort of things was popping.

You know, you'd be running some number of triangles

for a while and then you'd switch

to a different number of triangles

and you'd see a visible transition

and screen would look like it got shaken up.

You know, it's a disturbing artifact

that distracts you from the game.

And so one of the magical trade-offs of Nanite was how

to avoid all of the visible transitions

and get them down to a point

where though they exist statistically,

they're not really perceptible

to a person looking at it.

- You look at something like Nanite, I mean,

there's a nice blog post,

there's nice descriptions about the details,

but you can tell even under the details,

there's just incredible engineering that goes on.

It's so cool.

It's so cool how underneath this,

you know, the actual experience

of beautiful detailed scenery,

there's just incredible engineering

to bring to you simulation, ultra realistic simulation

of reality in real time.

Like lights changing everything.

And then, you know, it just takes you back to

that feeling I had with "Wolfenstein", but like more,

and you can completely lose yourself in that world

and you would forget that this real world exists.

What is the real world anyway, you know?

So it's that coupling of great engineering

and great storytelling

in terms of just feeling is super cool.

It's great to know, it's great to know

that these teams behind it.

And it's cool that you're also releasing

a bunch of details around it.

At least for folks like me.

It's inspiring to see.

So Unreal Engine is this fascinating creation.

It's a big, bold, crazy bet that you made.

Maybe it's good to actually explain what Unreal Engine is

for people sort of outside this world.

I would say it transformed the gaming industry,

but that was a big bet in 1995

that most of the effort would be on creating

the gaming engine, not the game.

- Yeah, Unreal Engine is a big bundle of code and tools,

a huge software package

that provides all the functions you need to build

any sort of a 3D graphics application.

Game developers use it to make games

and that's the predominant use.

But it's also used in Hollywood film

and television production to create 3D scenery in real time

for production sets to do pre-visualization.

It's used by car makers to visualize their cars

before they're constructed or manufactured.

It's used by architects to preview buildings

before they're made and industrial designers of all sorts.

And it provides, you know,

all of the 3D simulation features you need

both for creating highly realistic 3D graphics,

but also physics and interactions

between objects and making things happen

like you might see in the real world.

And supports a huge variety of styles

from Pixar stylized movies to cel shading to photorealism.

And it can be used for anything

that needs real-time 3D graphics.

- Including humans that populate

those three dimensional worlds.

And we'll probably talk a bunch of the details

involved in the process of creating ultra realistic humans

because we humans care about how other humans look

and how they convey emotion

and express how they speak, all that kind of stuff.

But so yes, it's the 3D objects that are static,

the 3D objects that are dynamic

and on the dynamic front,

including humans that are ultra dynamic.

So all of that, you have to create this engine

that simulates that world.

This beautiful world that we know and love.

Okay, but you know, you're early so

you see "Doom" and you're trying to create this world

and trying to create an engine

that would not just power "Unreal" the video game,

but future video games.

So how do you go about it?

What are you thinking and that,

I should sort of linger on that,

that is a crazy bet that we're going

to build an engine as a company.

- Yeah, well you know, the philosophy began with "ZZT"

and continued onward.

We're not just building a game for players to play,

we're also building tools that could be used

for building that game or any other game.

And catering to all the artists

and designers who had used the tool.

And so that philosophy started,

it's a very early parts of Unreal development.

I was building the tools for, you know,

level designers like Cliff Bleszinski

and artists like James Schwaltz.

And you know, as we began marketing the game

thinking it was six months away,

we were constantly releasing screenshots

and things like that.

Other companies started calling us

and saying they wanted to build 3D games too,

but they didn't have the expertise for that

and they wanted to license our 3D engine.

And this was one of the coolest pivots in Epic's history.

MicroProse called up Mark Rein, our, you know,

Vice President and longtime business guy

and said they wanted to license our engine.

And Mark Rein was like, "Oh, what?

You wanna license what?

An engine, what engine?"

And they explained to him what they wanted to license.

He's like, "Oh that engine.

Yeah, yeah, that's very expensive."

(Tim and Lex laughing)

But this was one of the critical things that kept Epic going

through that three and a half years.

We were starting to license our engine out

to other developers.

MicroProse took two licenses

and we got in half a million dollars from that

and company GT Interactive licensed our engine

to build another game and we got paid for that.

And so we had this revenue stream funding

the development of Unreal Engine from other games

that were being built by other developers.

And because they were the lifeline for the company,

we took the engine business very seriously from the start.

We set up, you know, mailing lists

so that our partners could ask us questions

and all the developers and artists working on our games

were participating in helping customers.

Everybody took that very seriously

'cause it was our funding source.

And you know, that's kind of set this dual spirit of Epic

of boning technology

and supporting game developers simultaneous

with building games and supporting gamers.

It's continued onward and just grown over time.

- Can you just go back to that, you programming,

what are some interesting technical challenges

you had to overcome?

You mentioned dynamic lighting, like create, you know,

create this three dimensional world

and try to figure out the puzzle of how you actually

do that at a time when nobody, Carmack and you (laughs)

doing this kind of thing.

It's a totally open wild west.

So what are some interesting technical challenges

you had to try to solve?

- There's a lot, some of them are visible on screen

and some are behind the scenes

and still require a lot of innovation.

All the graphical techniques

were really interesting challenges

and Unreal Engine in those early days

went a lot further than the quake engine

and building environments

using constructive solid geometry with a realtime editor.

And that was a really interesting technical challenge.

You know, the idea is building is extremely tedious

if you are only adding objects to the world.

If you wanna build a door, then you need

to add like a dozen different pieces of door frames

and add a bunch of different walls together

to fit together in the right shape.

It sure would be easier if you could just start

with a wall and subtract the door out.

And so we had this way of adding geometry to the world

and subtracting geometry and the engine would perform

all of the calculations on that.

And this is something

that I'd been anticipating was possible for a long time,

but when I finally got around to it,

it took this 30 hour coding session

to like figure out all the special cases of the code

that needed to be implemented to make that work.

But you know, in the course of 30 hours

I got constructive solid geometry up and running.

I started doing a, you know, like handed it

to James Schmaltz the next time we were together

and it's like, "Okay, I think you're cheating here."

So you create a giant Taurus

and then add another giant Taurus interlocked with it

and then subtracted a cylinder from it

and like created this really advanced composite object

with just three operations.

He was like, "Whoa, I can't believe this."

It's like, "Yeah, we figured it out."

And that was cool to see it for the first time,

but it was probably the first time somebody

had done constructive solid geometry in real time.

But it was also a really useful artist tool

that all the artists appreciated immediately,

began making use of.

- Can you actually speak to that, the 30 hour session?

I mean this is not, from everything I know about

computational geometry, doing this kind of thing

from your perspective, that's not easy.

That's, what is it?

The uncertainty, the open questions involved.

I mean even just on the algorithm front,

how to do that efficiently

and then plus the usual programming thing of debugging,

like suffering through the trickiness of it.

And we don't have really,

at that time you don't have the tooling

to really visualize everything that's going on really well.

And you probably like using some crappy editor.

I mean there's just a lot of like friction here.

So the 30 hour session is one that's probably rough.

It's a rough one.

- Your brain works in different ways

and depending on your state, right?

There are some things that require

really working on a problem fresh.

Where you've put together a bunch of logical pieces

and now you just need to write a whole lot of code

to make it all work together.

And, you know, plumb a whole lot of data

between a whole lot of different algorithms.

But, you know, I think our brains

have vastly more horsepower

than we're able to directly access

by thinking of what code to type next.

And you know, after you've been working

for a very long time,

you can get into a sleep deprived state

where you have much, much more direct access

to that low level knowledge.

(Lex laughing)

- That's great, yeah.

- You know, because you know their symptoms

that are well studied of sleep deprivation,

one of them is short-term memory loss.

And so you're working without like

the easy recall of the code you just typed,

but your brain is then freed to think about other problems.

And you know, I built up this intuition

over a very long period of time, you know.

So the foundation for the subject

is the binary space partitioning tree.

This data structure invaded by a computer.

Graphics researcher, Bruce Naylor.

Carmack had picked up on that and had used the technique

in "Doom" to really great effect.

And I'd picked up on that

and Unreal Engine was using this technique

for all of its graphics and rendering,

but it, yeah, it was just additive geometry everywhere

and it had a lot of overlapping polygons

and was pretty inefficient.

So I had the idea that if we had a BSP tree,

there was a really efficient way

to do constructive solid geometry.

And to do that you had to break down the ways

that different pieces of geometry can fit together.

I broke it down into like 14 different cases

and most of them are pretty simple, cranked them out.

Anyways, I got towards the end, you know,

there were some pretty complicated things like,

well how do you deal with coplanar polygons?

They're in the same plane

and pointing in the same direction

versus the other direction.

In what cases should you keep them?

What cases should you eliminate them?

And so on and so on

to create really efficient geometry output.

And you know, just plowing through it, eventually

through mostly deduction, but some trial and error too.

Like sometimes you just have to try the possibilities

and see what works.

Yeah, I cranked it out and it worked

and the next day I came in like kind of weary

and I was like, "Oh wow, this actually did work.

It wasn't just a dream."

- So you're considering the edge cases also.

I mean that's the problem with geometry is like

there's probably just gonna be all kinds of weird polygons

that you have to...

So you're like thinking through,

you're imagining the edge cases

and trying to see how do I not create inefficiencies

in this algorithm while still considering the edge cases,

allowing for the edge cases.

- Yeah, you know, it's pretty easy to write software

that's like 99% correct.

It's the 1% that's the really hard part

and where the devil lies in the details.

- What about like lighting?

Is there other interesting...

- Well the funny answer is like,

we know the laws of physics, so it's actually really easy

to do everything in computer graphics.

But the direct solution of the laws of physics

is immensely so.

And so what we're finding are approximations

rather than complete solutions.

'Cause you need something that's a million times faster

than the brute force answer.

- We should say that the physics of the scene

is you just take a bunch of photons,

bounce them around, that's how light works.

That's going to be very inefficient

because it's a lot of bouncing

and a lot of photons.

- Yeah, yeah, photon tracing is the subject matter

that does brute force calculation of pixels on a screen

from all of the light in the scene.

And it works and it's correct

and it just is an implementation of laws of physics

and it's millions or billions of times slower

than what we do.

But Carmack had figured out how to do

really cool lighting algorithms,

including real-time lighting with objects moving around.

And I hadn't taken it very far.

So with Unreal Engine I'd realized like

we don't have nearly enough computing performance

on our CPU to compute the light of every pixel on the screen

from all of the light sources that affect it.

Yeah, we were at a six cycle texture mapper

and we couldn't afford 30 more cycles for lighting.

And so the answer had to be some approximation.

And the one that Carmack had picked up on

in the "Quake" engine was light mapping.

Instead of calculating all the lighting on every pixel,

what if we like made a big texture

that we placed over all of the walls

in the scene that was like wallpaper.

And what if we say every foot,

we're gonna compute a lighting value

for just that one foot grid on the object

rather than computing it everywhere.

And then what if we just linear interpolate that

over the course of it?

You know, you get a lighting and solution

that actually works pretty well and is fast enough to work.

And so a lot of Unreal Engine's lighting techniques

were based on light mapping.

We introduced colored lighting

so you could have colored light sources.

Then we realized, oh, since we're doing this

and we're doing it on light maps,

we can actually do some pretty expensive calculations,

hundreds of cycles since we're only calculating it

for every one foot of world space rather than every pixel.

And so we introduced a whole bunch

of elaborate lighting effects like torch flickering

and you know, the caustic effects of water

bouncing off of a surface and so on.

And like pulsing lights

and blinking lights and everything else.

And I created a system for compositing them together.

# Chapter 6

And then what if we just linear interpolate that

over the course of it?

You know, you get a lighting and solution

that actually works pretty well and is fast enough to work.

And so a lot of Unreal Engine's lighting techniques

were based on light mapping.

We introduced colored lighting

so you could have colored light sources.

Then we realized, oh, since we're doing this

and we're doing it on light maps,

we can actually do some pretty expensive calculations,

hundreds of cycles since we're only calculating it

for every one foot of world space rather than every pixel.

And so we introduced a whole bunch

of elaborate lighting effects like torch flickering

and you know, the caustic effects of water

bouncing off of a surface and so on.

And like pulsing lights

and blinking lights and everything else.

And I created a system for compositing them together.

So if you had an arbitrary number of light sources,

they could all do that.

And you know, then I implemented a shadowing algorithm.

You know, if you cast a ray from a point

from a light to a point on a surface

and see if whether it intersects in the other geometry,

if it doesn't intersect and the light hits the object

and if it does intersect

then the light hits something else first

and that pixel on the object should be dark.

So I built a real-time version of this

and it ran at about a half a frame a second.

(Tim and Lex laughing)

So I was running around at half a frame a second,

like shooting out light projectiles

and looking at dynamic lighting, it was like,

"Someday computers will be fast enough

for this, but not today."

So I made a non-real-time version

that precalculate all the lighting

and realized, oh wait, if you precalculated the shadowing

on an object, you can still apply the lighting dynamically

as long as the light's not moving.

So you could do torch flickering with shadows

and you know, figure it out all the cases of dynamic

and static lighting that were actually practical

on a computer at the time and exposed them to artists.

And this was the wonderful thing.

I was just like typing in these old features,

exposing them to artists

and every day they'd find like a dropdown

with some more lighting options available to them

and they'd start using them and they'd do things

that I never thought possible.

And this was always the coolest thing,

as a programmer building an engine,

you might think you know the implications

of the feature you're building, but artists are so clever

that you always find that you've built the capability

of doing vastly more than you ever anticipated as they start

to use combinations of features together

in concert to do ever more amazing things.

- That's the genius of artists is they're given constraints

and within those constraints they create something

you could have never possibly imagined

given the constraints.

That's such a beautiful coupling

between engineering and artistry and art.

- That's right, and it's timeless, you know,

what did the renaissance painters do with paints

and what do the early game artists do with early engines?

You know, everybody's figuring out the capabilities

of their medium and you're seeing a revolution.

- This is blowing my mind. This is so fun.

What about fog? You mentioned fog.

I don't even know, how do you even do fog?

So you mentioned "Unreal," so the first version had fog.

- Yeah, well it was a funny thing.

So this graphics hardware company had just started up

in Finland and they released a screenshot

of what their GPU was doing

and they showed a scene filled with volumetric fog.

She had a foggy room with some light sources in it.

And when that happens in the real world, what you see are

glows around the lights

as the light brightens the fog around it.

But the brightening of the fog diminishes over time

because the fog absorbs some lighting.

And so the further you get away from the light,

the more falloff there is.

And you know, you have a bunch of colored lights

overlapping together in a space like that.

The effect is just absolutely magical.

You know, like being out on a foggy light

with street lamps above.

It's something that's surreal and looked just beautiful.

So I was like, "Oh my God, they figured out

how to do realtime value metric fog.

I have to figure it out myself."

And so that was another like 30 hour coding section.

(Lex laughing) - Nice.

- But like at the core I realized, okay,

what's happening here is we have this lighting function

saying that light at a particular point in space

is like, you know,

falling off with the inverse square of the light,

light the distance from the light source, right?

The inverse square is all from Isaac Newton,

which applies to lighting.

What I had to realize was the way the fog interacted

with the light was that you calculate the view

from your eyes position to a point on the surface

in the world.

It's going through fog and you're accumulating more

and more light as a function of the amount

of light illuminating the fog at that point in time.

And so, well, you know, I'd studied that (laughs)

in mechanical engineering without even knowing it.

That's the line integral, you know,

you have an integral over a line of some function.

Well this is exactly what it's for.

It's for accumulating the values of a function

over a continuous space and time.

And you know, I did a bunch of math

and realized that oh wow, the integral,

and then I looked in a reference book

of all of the integrals and you know,

thankfully people had solved them all.

And I realized the integral of, you know,

this transformed one over R squared turns out

to be solved by the arc tangent of R.

And so, you know,

if you calculate some parameters

based on the position of the eye

and the position of the surface

point you're at ultimately seeing,

then you calculate exactly

how much fog you can accumulate from that.

But of course you can't do that per pixel

'cause that's hundreds of cycles of CPU time.

And so what we had to do is calculate volumetric fog

on something equivalent to a light map,

but calculating fog every square meter in the world.

And so, you know, we had enough performance for that,

built volumetric lighting and gave it to the artists

and they started building magically detailed levels

with volumetric fog and in real time.

And then, you know, decades later

I was talking to one of the engineers

who'd worked on that hardware

and asked about their volumetric fog

and told them how it inspired me to, you know,

figure out how to do it in real time myself.

And I was like, "Oh no, we cheated,

we just rendered it our 3D Studio Max."

- That's awesome. That is so awesome.

That is so inspiring on so many levels.

That you saw that maybe it's possible even if it was

kind of smoke and mirrors

and then you actually made it happen.

It's so inspiring to hear these kind of stories

when there's so much uncertainty

and so many constraints

and you figure out how to bring it to life in real time

and create this world that Unreal did.

Maybe if we could just pause,

since you mentioned John Carmack a few times.

As a fellow pioneer in the game industry at that time,

what do you admire about John?

- John singularly has this intense dedication

to getting the best result from his code

and having absolutely no attachment to passed code.

And some of the legendary things he did,

the end result was an absolute breakthrough

in real-time computer graphics.

Weren't his first try.

They were like his seventh or eighth try

after he'd done something time and time again,

tried it, found a better approach,

thrown out the old one, build it again

and continually re-wrote out his code

until he found the absolute best solution to a problem.

And you know, I think that stands as a lesson

for every programmer to pick up on.

When something is really, really important,

its performance is absolutely critical to the product

or its quality or its capabilities.

Just iterate on it until you've achieved perfection

and don't settle for the first

or second solution is good enough.

- And it's, you know, the result of that,

both you and him sort of define the future of gaming,

of gaming worlds.

It's so beautiful to see.

It's just fascinating.

It's inspiring because like under so much uncertainty,

under so many constraints, you figure out a way

and that, you know, actually continues to this day

because yes, the hardware is improved incredibly,

but in order to create an ultra realistic,

highly dynamic, real-time rendering of the world around us,

it's still really, really difficult.

And there's all these kinds of optimization,

like you mentioned.

Maybe you can speak to that

Unreal Engine 1 journey

from 1 to 5.5 or 0.6 now.

For 30 years you've been creating virtual worlds,

what's it like evolving a game engine

for those 30 years

when the hardware under you

is improving exponentially?

What are some things

that changed and what are some universal truths

that have not changed?

- It's been an astonishing experience.

Nobody 30 years ago had anticipated

that we'd see the performance gains in hardware

that we've actually seen in that timeframe.

It's something like a hundred thousand times

higher CPU performance

between multiple cores and higher clock rates

and more parallelism.

Like, you know, if we had that in aviation,

then we'd be like taking a trip to neighboring stars.

- [Lex] Alpha Centauri, yeah. - Exactly.

And in graphics it's been even more so.

It's something like literally 10 million times more

net usable GP performance

than we had back running on a Pentium 90 CPU

all in 30 years.

And you know, it's really made me appreciate

that over the generations,

some areas of our engine development

have absolutely kept up with technology.

And you know, the rendering team

that works on Unreal Engine

are the real miracle workers there.

Just about every generation of Unreal we've replaced

most of the rendering code and you know,

the different leaders and different points in times

and the different luminaries have built systems

that were absolutely rethought

and optimized for the latest generation of hardware.

You know, Unreal Engine 1 was built for software entering

and then the Voodoo 1 came along late in the cycle

and we had support for it,

but it wasn't fully capable and utilized.

Unreal Engine 2 was about bringing

all the latest GPU hardware acceleration features

to the engine and you know, keeping forward

and honing some new features like vehicles

and a few other capabilities.

And this was in the early GPU era

before GPU had really broken out of, you know,

everybody's expectations of Moore's Law.

But that breakout occurred with DirectX 9

and the capabilities of, you know,

programmable shaders.

Once you had control of writing code running on the GPU

that could color every pixel on the screen.

And that GPU code was literally a factor

of a hundred times faster than the equivalent code

I wrote a few years earlier in the Pentium 90.

And so that DirectX 9 generation was a godsend.

And Andrew Scheidecker,

a longtime Epic luminary wrote the core

of the Unreal Engine 3 render around

real-time pixel shading, real-time lighting,

being able to do dynamic shadows

using several different techniques

and multi-thread the render to support bits of, you know,

the early dual core CPUs that were starting

to show up at the time.

And it was a massive, massive graphical upgrade.

Unreal Engine 4 made a number of improvements

and just continued to add features to give artists

more and more options for lighting

and for geometry that created realism.

But then I think probably our biggest single level of leap

came with Unreal Engine 5

with a Nanite micropolygon geometry solution,

and with Lumen the global illumination lighting solution.

You know, which I think really bridged the gap

from, you know, game-ish computer graphics to,

you know, total observable photo realism

for artists who wanted to create that.

And so that's been the evolution

and the progress on the graphics side

is absolutely astonishing.

As it is on the audio side and a number of other areas.

But parts of the engine also haven't changed

all that much since the version I wrote and chipped in 1998.

You know, the a file management system

has been optimized a number of times,

but it hasn't been completely rethought.

And the networking system, the ways that clients

and servers talk together and negotiate game state

is still an evolution of the thing I wrote.

And you know, it's feeling kind of dated now.

You still see networking bugs in "Fortnite" where like

for some reason when you're spectating you're not seeing

some parameters update.

Well that's because of the lossful nature

of that networking model.

And the biggest limitation that's built up over time

is the single-threaded nature of game simulation

on Unreal Engine.

We run a single-threaded simulation.

You know, if you have a 16 core CPU, we're using one core

for game simulation

and running the rest of the complicated game logic

because single-thread programming is orders of magnitude

easier than multi-thread programming.

And we didn't want to burden either ourselves

or our partners or the community

with the complications of multi-threading.

And you know, over time

that becomes increasing limitation, you know,

so we're really thinking about

and working on the next generation of technology

and that, you know, being Unreal Engine 6

and that's the generation we're actually going to go

and address a number of the really core limitations

that have been with us over the history of Unreal Engine

and get those on the, you know, a better foundation

that, you know, the modern world deserves, given everything

that's been learned in the field of computing

in that timeframe,

- That's a terrifyingly challenging engineering problem.

And it seems like every version of Unreal Engine,

the amazing teams behind it are willing

to just throw away most of the code. (laughs)

And maybe I'm being a little bit too dramatic,

but basically throw away the old approaches

like you mentioned with Carmack

and start again, like with Nanite and Lumen,

just keep optimizing to the current hardware,

but even like rethinking how it's all done.

But going from single-threaded to multi-threaded.

Oh boy, that's terrifying.

And that's in part we'll talk about it,

why maybe you have to rethink

even the programming language that's being used

to rethink a lot of things.

That's fascinating. Can we just stick on Unreal Engine 5?

So I watched a bunch of stuff,

but the state of Unreal in GGC 2024.

(Lex laughing)

Thank you, I was just giggling

with excitement watching some of this stuff,

so just if we can talk about different things here

just to nerd out a little bit.

So people should go watch this video.

They talked about the dirt,

just the ultra realistic,

and this is for "Marvel 1943,"

which is kind of putting the Marvel universe

into Nazi occupied France in the winter.

So there's snow.

And you know, that's a moment in history,

that's a very intense moment in history

and it really creates a feeling and puts you there

and there's so much to that including the snow.

But just, you know, looking at the dirt is a really nice way

to show like how do you (sighs)

add a lot of details to the scene in real time

that like gives this experience

like infinite detail.

Like this is real, this is super real.

And then I think in the talk they describe

what's entailed in the generation of the geometry,

what's entailed in the lighting, all that kind of stuff.

Maybe can you speak about dirt? (laughs)

# Chapter 7

They talked about the dirt,

just the ultra realistic,

and this is for "Marvel 1943,"

which is kind of putting the Marvel universe

into Nazi occupied France in the winter.

So there's snow.

And you know, that's a moment in history,

that's a very intense moment in history

and it really creates a feeling and puts you there

and there's so much to that including the snow.

But just, you know, looking at the dirt is a really nice way

to show like how do you (sighs)

add a lot of details to the scene in real time

that like gives this experience

like infinite detail.

Like this is real, this is super real.

And then I think in the talk they describe

what's entailed in the generation of the geometry,

what's entailed in the lighting, all that kind of stuff.

Maybe can you speak about dirt? (laughs)

What are the components for people

who might not know in like creating this ultra realistic,

the texture, the lighting, the geometry, all of that.

Like how Nanite, how Lumen all come together

in this beautiful orchestra to paint in real time

the dirt in Nazi occupied France in 1943. (laughs)

- Yeah, there's a lot happening here on screen

and you know, the real hero of of this image isn't Epic,

it's the artists and technical artists

who work together to build this environment because it,

and the reason we showed it at GDC was it went way, way

beyond what we realized the system was capable of doing.

You know, largely because of their brilliance.

And this is the magic of computer graphics.

There's not one feature that makes this cool.

There's a dozen technical features that each interplay

and because of the ways that they interplay with each other,

it's hard to actually identify

the individual components of it.

One thing that's happening here that's really critical...

Oh yeah, now we're seeing it being turned off is

the lighting happening.

The Lumen lighting system

that's powering the scene is doing different

kinds of lighting calculations at different scales.

This was the work of Daniel Wright following a decade

of moving the state of the art of lighting forward.

But his theory, which was rather controversial at the time,

was that if you have enough levels of lighting calculation,

then you can get everything

global illumination working everywhere

from the absolute highest levels of a scene,

you know, that buildings are casting crack shadows,

all the way down to details like you see on the dirt here,

all working in concert

and without distinguishable boundaries.

So there is a good decade of foundational work there

to make the lighting work.

In particular when you see the very detailed shadows

interplaying between the, you know,

the ice and the dirt there, that's screen space lighting.

There's actually shadow calculation going on,

not based on the world but on the pixels on the screen

because that is the only way

that we could possibly do those calculations fast enough

running them on a pixel shader.

- Yeah, watch this,

watch when you add the objects, when you add the textures,

the different layering all the shadows

that have to be computed.

- Yeah, yeah. - Boy. (laughs)

- That shadowing is the amazing thing.

But you know, the reason that works is counterintuitive.

When somebody first explained it to me, I was like,

"That's really clever, but I don't think that will work."

But it does work

because if you observe the positions of incoming lights

and you know the z coordinates

of the different pixels on the screen, you can figure out

how, you know, geometry there is likely

to occlude other geometry.

And even though it's only an approximation

and not isn't perfect, it looks perfectly good

to the human eye and gives you the subtle shadowing

that you see in a scene like this

that it makes it look highly realistic

and the shadowing influences other things.

There's also, you know,

some really interesting things happening with the color here

and I'm not even sure what's causing, you know,

it looks like color is bleeding from some parts of the snow

onto other parts of the snow.

It looks like there's some subsurface scattering going on.

I'm not even sure if that's being used in the scene.

And then there's a material layering system for laying down,

you know, layers of material, dirt and snow

and other things all making that work.

And then there's the light bouncing off of the geometry,

which is another system for lighting

on top of the global illumination system.

- What about reflections too?

Is that count as the light balance?

So there's a light balancing off of stuff

to light it up in different interesting ways,

but then there's also actually literal reflections

in like we're looking at a puddle in the dirt.

- Yeah, yeah, that's right.

But the engine supports a number

of different reflection techniques.

One is calculating basically textures that reflect,

that capture all the lighting in the scene

and then bouncing that off of texture maps.

So you can see different lights bouncing off

of different pixels in different ways.

And then there's individual lighting

casting reflections off of things too.

And a lot of this is under the control of designers

and you know, one of the things that's yet to do problem

for the future is you don't just like press a few buttons

and this kind of scene magically appears.

This is a lot of work from some highly skilled people,

not only building out this particular scene,

but in setting up the material layers

so that you get the dirt with the ice layered on top

and all the reflections working

and they need to make a number of technical art decisions

to make this work.

And if a novice who hadn't, you know,

worked very hard built the kind of scene like this,

it wouldn't look nearly as good.

So one of the challenges we have is

to make building this kind of quality level

even easier and more seamless and automatic.

You'd like to just build a scene

and say, use this material here

and have this appearance come out of it.

- Yeah, and I mean once you create the scene

you could do things.

I remember where they said like,

"Can you turn off the headlights?"

I forget you could control the lighting.

I mean all of this we should say like, this is dynamic.

So you could change the position of the light,

you can turn on the lights and off the lights,

that's incredible.

So this is all real time.

The geometry, the lighting, the textures,

all of it, real time.

- This is the power of awesome technical art,

three decades of feature development,

and like you have to give credit

also to the 20 teraflops of graphics performance,

that NVIDIA's delivering.

- Thanks NVIDIA. (Tim and Lex laughing)

- 90 megahertz to this, 90 megahertz is 90 megaflops.

This is 20 teraflops. That's a big change.

- That's a lot.

So one of the other things

that they talk about in the presentation is about snow.

So you have to, if you're talking about 1943 Nazi Germany

in the winter, you know,

you have to create a feeling,

one of which is the season, the winter, the cold,

and you can control the, you know,

you have to cover everything in snow.

And here shown is the ability to control

how much snow covers the objects.

So the ability to do that for the artist is incredible.

Like just to control

how much snow is in the scene dynamically like that.

That's cool.

- Yeah, yeah. - That's really cool.

- It's a cool system for material layering

and a dozen pieces coming together here.

You also notice, you know, there's a fogginess

and there's some hot objects emanating fog.

You know, an artist did that,

that didn't just arise automatically.

- So that's called material layering.

So an artist creates the different materials

and are able to like layer the scene with it.

- Yeah, layer materials on top of each other

and see how much of each material should be protruding

in different places with the engine handling transitions

and things like that.

- And that's on top of the sort of the geometry

that creates the structure of the scene

and all the occlusions that have to be computed, man.

Okay, I gotta go to the other one

that was just blowing my mind, which is smoke.

Let me see that, look at that.

- Yeah. Yeah. (Lex laughing)

- Oh, there's a fire,

there's a fire in a trash can with the smoke

and the lighting and the shadows

interplaying on the smoke.

This is real time?

- Yeah, that's all real time.

- What the hell?

How do you do that? (laughs)

How do you do the smoke?

Well there's a really powerful particle system underneath,

it's providing the technological foundations

for this sort of thing.

But there's awesome artistry on top of that

and an awesome physics engine powering it.

It's hard to tell exactly which piece is doing what,

but you have several different particle systems there.

There's one for the fire

and then there's another one for the smoke coming out of it.

The really interesting thing happening

with the smoke here is that it's occluding light.

You know, there's calculation of

how the light should diminish as it travels through smoke.

And so you're seeing the lighting on the smoke

being the really interesting thing.

And there have been a lot of attempts,

but this was the first demo

where I felt like this kind of smoke had really,

it no longer looked like a video game.

It looked like just, you know, a burning trash can,

billowing out dark smoke.

And yeah, it's the artist sophistication.

It's a very, very, very large part of it.

- So yeah, again, it's the interplay between the tooling

and the artist.

But yeah, like I could watch that for a long time.

I mean there's something magical

sitting around a fire in real life

and just watching the fire and the smoke.

I mean humans have been doing that for, I don't know,

hundreds of thousands of years maybe.

And then that same, I was just staring at that

and I wish the people would just stop talking

and I could just watch the fire infinitely.

(Tim and Lex laughing)

And that, I mean that's immersion.

That's like I want to be in that.

I want to sit around that trash can with a fire

and the smoke and watch and maybe warm my...

'Cause I was also feeling cold because of the snow.

You're like, you really get immersed into the thing.

I mean it's so beautiful.

It's true art. It's true art.

It's just really wonderfully done. But, okay.

So I gotta ask you about the humans.

We talked about what's it like to create the scenes,

but you know, creating realistic humans is really tough.

Can you speak to that?

How to create ultra realistic humans?

So you have an actor behind this to convey emotion,

show the nuances and the details of the faces

and maybe this is a good opportunity

to also mention MetaHuman Creator

that's part of Unreal Engine.

- Yeah, that's right.

Humans are by far the hardest part of computer graphics

because millions of years of evolution

have given us dedicated brain systems

to detect patterns and faces and infer emotions and intent

because cavemen had to,

when they see a stranger determine whether they were likely

friendly or they might be trying to kill them.

And so humans, we people in the world

have extraordinarily detailed expectations of a face

and we can notice imperfections

especially perfections arising

from computer graphics limitations,

but it becomes by far the hardest problem.

So the MetaHumans effort is part of a decade long initiative

that Vlad Mastilovic,

the most talented digital humans visionary in the world

has been working on

for generations and generations of games.

You know, serving individual clients

around the game industry for a while

and then joining Epic as part of the three lateral team.

And leading now a worldwide effort to build

all of the technologies required

to make digital humans realistic.

Okay, one part is capturing humans.

And so we built really advanced dedicated hardware

that puts a human in a capture sphere

with dozens of cameras in them taking high resolution,

high frame rate video of them

as they go through a range of motions.

And then capturing the human face is complicated

because the nuanced detail of our faces

and how all the muscles and sinews and fat work together

to give us different expressions.

So it's not only about the shape of a person's face,

but it's also about the entire range of motion

that they might go through.

Capturing one human requires,

you know, a few hours of capture work

in a dedicated environment like that.

Then thousands of hours of processing work to capture

a precise and, you know, real time replicatable version

of that human in the environment.

And so one of the things that

that's done is just capturing an actor

or actress in the real world

and then using them in a video game.

But the much more interesting thing going on is capturing

thousands of humans to form a data set whose goal is

to encompass the entire range of faces in all of humanity.

So, you know, going around every culture, every continent,

every age and every face of variety

and capturing representative people

so the entire range of faces is represented.

And then being able to combine

and merge those together

to enable recreating an arbitrary face

that the system's never seen before.

So you know, one of the ideas is capture giant amounts

of this high precision data

and you use it to reconstruct a face at a consumer level.

Like maybe, you know, take an iPhone photo

of somebody's face and then capture a very accurate

depiction of that, not by synthesizing it then

and there on that device,

but by combining all the known details of human faces

to accurately capture

the most accurate representation of that.

So that's the data problem.

There's a lot of other problems with computer graphics.

You know, there's technology for rendering hair,

which is really hard 'cause you can't render every, again,

we know the laws of physics,

it would be easy to just render every hair.

It would just be a billion times too slow.

So you need approximations that capture the net effect

of hair on rendering and on pixels

without calculating every single interaction

of every light with every strand of hair.

That's one part of it.

There's detailed features for different parts of faces.

There's subsurface scattering

because we think of humans as opaque,

but really our skin is light travels through it,

it's not completely opaque.

And the way in which light travels through skin

has a huge impact on her appearance.

You know, this is why there's no way you can paint

a mannequin to look realistic for a human.

You know, it's just a solid surface

and we'll never have the sort of detail you see.

- We should actually just linger on that.

That kind of blew my mind like thinking through that.

I think I heard that sort of the oiliness of the skin

creates very specific nuanced,

complex reflections and then some light is absorbed

and travels through the skin and that creates,

would it be fair to say like micro shadows or something?

It creates like textures that our human eyes able

to perceive and it creates the thing

that we consider human, whatever that is.

And so like you have to compute both that, the reflection,

how light interacts with the oiliness of the skin

and how it is also absorbed in

and all of that while considering all the muscles

involved in making the nuance expression.

Just the subtle squinting of the eyes

or the subtle formation of a smile.

It's a stupid annoying subtlety of human faces

that you have to capture.

Like the difference between a real smile and a fake smile.

Man, I love human faces.

I love humans in general.

But the way to show like beginning of a formation of a smile

that actually reveals a deep sadness, all of that.

Like when I watch a human face, I can like read that.

I could see that.

Again, this is the engineering and the artist.

# Chapter 8

It creates like textures that our human eyes able

to perceive and it creates the thing

that we consider human, whatever that is.

And so like you have to compute both that, the reflection,

how light interacts with the oiliness of the skin

and how it is also absorbed in

and all of that while considering all the muscles

involved in making the nuance expression.

Just the subtle squinting of the eyes

or the subtle formation of a smile.

It's a stupid annoying subtlety of human faces

that you have to capture.

Like the difference between a real smile and a fake smile.

Man, I love human faces.

I love humans in general.

But the way to show like beginning of a formation of a smile

that actually reveals a deep sadness, all of that.

Like when I watch a human face, I can like read that.

I could see that.

Again, this is the engineering and the artist.

You have to have the tools

that in real time can render something like that.

And that's incredibly difficult. But anyway, sorry.

So yeah, so there's a lot of this kind of complexity

in even just the lighting of a face.

- That's right, getting faces right requires the interplay

of literally dozens of different systems

and aspects of computer graphics.

And if any one of them is wrong,

your eye is completely drawn to that

and you find it on the wrong side of uncanny valley.

So the level of perfection needed in this area is vastly,

vastly higher than, you know, world rendering or grass

or any of these other things.

You know, if the shadows on a work of architecture

are slightly wrong,

you're pretty forgiving with that actually.

Your brain doesn't really care that much.

But if anything wrong with the human

it's totally jarring.

- Can you speak more to the creation of digital humans

with MetaHuman, both on the editor side

and sort of bringing it to life side?

It seems like, 'cause I've watched a bunch of videos,

a bunch of individual developers doing it,

it's not too difficult to bring a human to life

using the tooling

that Unreal Engine editor provides.

- There are two main tools.

You know, compared to the old days

where every face was created by hand

by an artist from scratch.

One is a MetaHuman Creator tool for creating faces

where you have a huge number of parameters you can adjust

to create a unique human

by adjusting all the different capabilities of them.

And you can then get that MetaHuman Creator

into Unreal Engine,

and then you can add all kinds of computer graphics features

they're in the engine.

You could add clothing using the cloth simulation system

and you can adjust the hair

and all these other parameters on the thing.

And then there's Metahuman Animator,

a tool for animating a human based on a facial capture,

which can be done on a device as simple as like an iPhone.

And transfers the captured animation to the human you want,

which is not straightforward.

If the actor has one face shape

and the character on screen has another face shape,

the translation that needs to be done

from the actor to the face

is actually really sophisticated and non-obvious.

And if you just applied it literally,

then it would be completely wrong from your point of view.

So those are the main tools that people are using now.

And then when within the Unreal Engine,

then you have a face and you can do

absolutely anything you want to it.

And you could also, you know, if you decide to go outside

of the Metahuman geometry pipeline,

you could build your own face, like, you know, any creature

of any sort, and then use the animation tools to animate it.

But, you know, this is 30 years into a project

that's probably like 50 years in total

to get to absolute photo realism

and controllability for absolutely everything.

So there's vast amounts of work still to do.

And you know, we don't feel like we've solved

the problem at all.

We've just given artists a big productivity multiplier

and a quality multiplier.

But this is not in a state that we would say is done.

- But nevertheless,

I've seen people use it really effectively.

I saw it almost like plugins, maybe external services

where you can get the faces

to approximate the mouth movements

required to speak a thing.

So like that's a really useful feature.

- Yeah, that's right.

When you have an artist or actor in your studio

and you're recording a specific performance,

you can just capture their facial motion and apply it.

But if all you have is a voice recording

or you're generating a voice recording or it's parametric

or procedural or AI generated,

yeah, then you need the system to translate that speech,

not only to movement of the mouth and lips,

but also to facial expressions

and the whole intent.

You know, when we're speaking,

it's our whole face that's active

and emoting in different ways

and it's not just a mechanical motion of the pieces.

- So we spoke a bit about Nanite, so the magic behind

the virtualized geometry system.

But can you speak a little bit to Lumen

and in general what it takes

to dynamically light in all the complicated ways,

the faces, the scenes that we discussed?

Like what are some interesting things to you

that made the magic of it happen?

- Lumen is a system for global illumination.

Being, it's supposed to calculate the interaction of light

with the entire scene in a way that mimics reality.

The first generation of engines that did lighting just said,

well, the light casts light

and the surfaces that hits are lit

and the surfaces that doesn't directly hit are dark.

And that's just all the techniques we have.

So you'd have an area that wasn't hit by any light

being completely black,

but in reality, light bounces

around the entire scene dynamically.

When a light hits a red wall,

then most of the blue and green light is absorbed,

but the red light reflects off

and now is hitting other things.

And so if you have a red wall with a white floor,

light is bouncing off of the red wall into the floor,

and now the floor is being turned red.

And so the entire bouncing of light around the scene

through multiple bounces is the critical challenge

to solve here.

And again, laws of physics are known.

And so the complete solution to this,

it was written down in the 1950s, I think.

The real magic here in Lumen is this system

that Daniel Wright developed over the course

of many years based on ideas formed

over a longer period of time

to calculate the way lighting bounces

around at different scales, ranging from, you know,

the scale of miles or kilometers,

down to the scale of pixels and millimeters.

And to not only calculated at each level,

but integrate it seamlessly at each level

to give the appearance

of completely seamless and accurate lighting.

And previous techniques were highly specialized

and artist had to make a decision for each light

about exactly what it did.

And a lot of the practice with Nanite now

is you build a scene, you place lights in it,

and it just works to make it that much easier.

- Yeah, I mean, we're watching, so I recommend people go

through this blog post, like, look at that so dynamically.

I mean, we should say that,

so there's the indoors and the outdoors,

and to be able to dynamically compute the impact

of outdoor light.

Just look at that.

Look how gorgeous that is.

Just the lighting, like,

we're looking now at an image of a cave.

So external light lighting

the intricate complexity of insides of a cave.

Look at that.

- Light in the real world goes through a lot of bounces

and the effect of it are very, very subtle.

But when they're not there, you miss them.

Often a person can't point out why a scene is wrong,

but they know it looks wrong.

And it's the lack of the subtle lighting cues

that we're seeing here.

- And you know, for great,

'cause we mentioned for great video games,

but also for great films, lighting can make a film

and we're just looking at sort

of a very dramatic lighting of a scene.

Like imagine stepping into the scene,

it's exciting, it's terrifying.

And all of that has to do with light,

the interplay between light and darkness.

It's incredible, it's really, truly, truly incredible.

Like light is everything, and then to put the power

of the tooling in the hands of an artist

that is really special.

- Yeah, the industry's gone through a massive evolution

and there's so many supporting systems to make this awesome.

And always artists.

(Lex laughing)

- We're looking at reflections on smooth surfaces.

Oh boy, oh boy, look at how gorgeous that is.

- Yeah, that's right. - Wow.

- And you have to appreciate,

the algorithms are doing quite a lot here.

You can have a, you know, a scene with a huge number

of not just lights, but also bright objects

that reflect light off of them.

Every one of those has to be captured in the reflections

in order for it to be realistic.

And, you know, you can't calculate

every photon in the scene,

and so you need really detailed approximations.

And that's the field of computer graphics.

It's about increasingly effective approximations

of the laws of physics, which are just totally intractable.

- But the result of that graphics is the feelings

and experience by the viewer.

And it's just to me, as a fan of,

well, let's say beauty in the world,

it's exciting that we can create

that synthetically, artificially via graphics

and that just, it blows wide open

the possibilities of storytelling.

So outside of video games,

a lot of people are using Unreal Engine

for movies, for films.

And big congrats, I saw "Wars is Over" short film

that was made with Unreal Engine won an Oscar.

So you can add that to the resume. (laughs)

So that's huge, you know,

an Oscar winning film made with Unreal Engine.

So what do you see as the future of

the use of Unreal Engine

and creating stories in the film industry?

- Increasing capabilities and productivity.

You know, the limiting factor

in every one of these businesses is cost.

And the more the engine can make their jobs easier,

the more power that brings them.

One of the big revolutions we've seen in Hollywood

is that moving away from doing computer graphics integration

into a human scene with green screens,

to moving to these large LED wall panels,

they're displaying real-time computer graphics

powered by the Unreal Engine.

And that's a massive improvement in quality.

You can recognize the old green screen movies

because the lighting on the characters is just wrong.

And you know, as much as they try to fix it up,

it never really works.

When you're filming in front of a LED panel

with LED light emitters in front of you as well,

the actor not only picks up all the lighting

from the actual natural scene that they're supposed

to appear in the movie, but they also can look around

and see it, and they're aware of exactly

what set they're acting in.

And just the overall end result is that much higher.

It's as much because the actors are able

to do their jobs better seeing the scene they're in

because the technology is enabling

a better lighting calculation

and a better interplay of virtual light

and real world light to make the end result awesome.

- So there's a lot of excitement around generative AI.

What do you think is the future of the interplay

between what a human artist creates

and what an AI system can create in Unreal Engine?

- I think a lot of people in the industry

are overly optimistic about the rate of progress of AI

for video and other things like that.

The real problem is consistency,

like spurting out an image is really high quality,

but with video over the course of seeing, you know,

all the AI approaches have consistency issues

going from one place to another.

And I don't think that those will just be remedied.

Fundamentally AI just doesn't have anything resembling

an understanding of the entire scene they're in,

the entire arc of the movie or plot therein

and the entirety of the world around them

and how it might affect a scene.

Whereas game engines have that

exactly where they need to be.

And so I think what we're gonna see

in the space of world-class high quality productions

isn't just everybody moves to AI

and a large part of the human creatives contributing

to that are obsolete.

I think what we're gonna see is AI becoming

a multiplying force on the power of human creatives,

making them able to create better stuff more quickly

and with higher quality end results.

And I think unlike the fields of generative 2D art

and generative text, I think the future of AI

is much more complex and nuanced.

And I think your interview with Mark Zuckerberg

conducted in VR was a really

good first example of this.

So you did this VR discussion, it was capturing your faces

and then rendering a completely 3D

computer graphics model of your faces.

And then the end result was patched up

by an AI image enhancer that was able to add

an awful lot of the missing subtleties that are lost

by normal computer graphics rendering.

And that's the first step.

You know, you can imagine the output of Unreal Engine

being enhanced by an AI pixel shading post processor

is one thing.

You can imagine creation of objects being enhanced

and especially mashing up high quality objects

that have already been created.

Like Epic's Quixel team went around the world

and scanned tens of thousands of real world objects

at extremely high levels of quality.

They have everything from rocks to trees

to archeological finds and so on.

All captured there.

And we have an awesome library of them

on the Fab content site.

What it's missing is the ability

to create arbitrary amounts of new content.

And you know, I think using data like that

and AI to create completely new trees

that meet your specification from all of the knowledge

that has built up of high quality scanned trees

is gonna be a really valuable thing.

But you know, I don't see this reducing the need

for people or the role of people,

rather, I think it actually is probably an enhancer on that.

I can't help but think when I go on Amazon

and Netflix to watch a movie,

there's awful lot of linear content

and most of it isn't very good

because you know of the limitations of the media

and the budgets and of other things.

If we can use AI as an enhancer on that,

then, you know, everybody's gonna have

even more opportunity than they have now.

And every single technological revolution

has changed the way that people work,

but it's ultimately created more opportunity for people.

And you know, the (indistinct) its predicting

that this might be the last,

but I think just the opposite.

I'm an optimist on this

and an optimist that it's going

to create opportunity for everyone.

- Do you think it would be possible to generate,

so use generative AI to create

dynamic objects like you mentioned trees

in the Unreal Engine world, so create meshes and textures

and empower the creator

to create faster use meta knobs,

like hyper parameters versus very nuanced

where you can control much faster the look of a face,

the look of a tree, all that kind of stuff.

- Yeah, I think that's the central challenge

of the next decade of game engines and AI for,

you know, content creation of all sorts.

Because you have two very different models of the world

that are emerging.

There's the scene graph, the technical term we use

to describe the set of all of the objects in the world

in a 3D world maintained by Unreal Engine

or another engine, you know,

so in the videos you saw, it's the rocks and the trees

and the snow and the bridge

and the people and all of these things.

And each one has enormous amounts of data attached to it.

Some are like texture maps, some are sound files,

some are animation files

and enormous amounts of detail all stored there

in that procedural,

in this precise computer graphics representation

that enables rendering it from any perspective

with any settings and so on.

It's a completely general system

that has complete context

about the state of the world at any point.

And so you can always precisely reproduce it.

If you play the same scene 10 times in a row,

it's always the same.

It's never randomly changing.

# Chapter 9

in a 3D world maintained by Unreal Engine

or another engine, you know,

so in the videos you saw, it's the rocks and the trees

and the snow and the bridge

and the people and all of these things.

And each one has enormous amounts of data attached to it.

Some are like texture maps, some are sound files,

some are animation files

and enormous amounts of detail all stored there

in that procedural,

in this precise computer graphics representation

that enables rendering it from any perspective

with any settings and so on.

It's a completely general system

that has complete context

about the state of the world at any point.

And so you can always precisely reproduce it.

If you play the same scene 10 times in a row,

it's always the same.

It's never randomly changing.

You're like, "Oh no, why did it

that this character's face change midstream?"

But it's also, you know, rather limited

because you have to build everything manually

and it's costly and it's time consuming.

It requires expertise.

And then you have this other model of the world,

which is what AI sees or thinks.

You know, if we could peer into what's really happening

in its parameters,

there's something like the mushy connections of neurons

in a brain.

It has a vast amount of knowledge about the world

and about graphics and about images and about people

and about everything else.

It's stored in a human incomprehensible form,

but it can be extracted through queries

like asking it to produce an image from a prompt

or a video from a prompt or whoever.

But the huge problem with that is it's very mushy data.

We don't know how to give it a command

that will give us a precise result.

And if it produces one image one time

and we change our prompt slightly,

it might produce something completely different

and we were unable to art direct it.

And so it's this completely untamed tool.

And I think, you know, when we figure out more

and more ways to merge these

and connect these two together,

you can imagine AI enhancing the process of content creation

in a traditional scene representation.

You can re imagine the scene representation

being cured with AI.

So the AI not only sees a prompt,

but also here's a list of all of the objects in the world

and the characteristics and so on.

It can learn more about how those objects

should move and interact.

And so if you get a constant feedback cycle

going back and forth between an engine and AI,

and I think you can get the best of both worlds,

stable scenes, but also the higher productivity

of being able to get content out

and the ability to like select specific parts of it

and art direct those.

And to have those art directions stick

and be recognized

as part of this permanent scene representation.

- Yeah, I can't wait until AI can operate

not in the space of pixels,

but in the space of scene graphs.

Creating objects in the scene graph,

whether it's like you mentioned audio

or any of the things that you mentioned about

that empower the creator.

Yeah, that's a super exciting future.

I wonder if you could speak to a fear

that people have on this topic of artists,

engineers fear losing their jobs,

being replaced by AI.

Are there words of hope that you could offer them?

- This is certainly the most extreme example of it

because AI is just so far ahead of prior technologies,

but similar fears were had in every other industry.

There's a fear that digital music synthesis

would obsolete musicians.

And there's a very brief period of time

in which songs with digital music instruments,

like there are early mini mugs

and Yamaha synthesizers weren't allowed

to win certain music industry awards

because they weren't considered real music.

And then, you know, over time the people were educated

and realized, oh,

these are just instruments people are playing

and they're controlling them the same way they did before.

There's similar questions about is, you know,

computer art built in Photoshop really art,

or is it just, you know, goofy computer stuff?

And you know, I think nowadays digital artists

have gained respect and I think, you know,

if you look at just the tools that existed in Photoshop,

some of them are pretty sophisticated

and nowadays AI features,

but I think AI is ultimately gonna be another tool

in the artist's tool set.

And you know, I think it's gonna become

a more powerful directable

and human serving tool in the future.

And I think a lot of the alienation comes from the prompt

either being immensely powerful

at giving you an entire creation,

but then being completely unwilling

to let you control the nuances of it.

That feels alienating.

You give it an image, but you're like, you know,

replace this part of it with this thing

or make that object green.

And it just like, it can't do it.

Often it can't be convinced with any number of words

in the prompt.

And that makes it feel like the computer's taken

control away from us, you know, humans and artists

and is refusing to do what we want

and has its own opinions, right?

It feels like a competitor.

Or I think when we have much, much, much more nuanced

control of it and artists can join and just,

you know, like, yeah, let's enhance this object,

do this, do that, do that.

They'll feel it's a, you know, like some of the tools

that exist in Photoshop, which are in some ways compared

to a paintbrush or superpowers already,

AI will come to feel like that too.

And will increasingly serve creators creating

and enhancing a work in a way

that feels just a natural extension of their own, you know,

their own bodies and minds.

- And of course there is a real human pain to layoffs

and there is a hype around AI

and then companies might try to implement AI systems

and then so doing layoff a bunch of folks

and the pain that those folks feel is real.

I think there's always going to be pain

with these kinds of transformation that's happening.

And it's a terrible pain.

Pain in general in the human experience is terrible,

but I think I'm personally excited

by the human AI collaboration

as you've described in this whole process.

So I think if you just keep being open

to using the tools,

constantly trying the cutting edge tools,

how they can make you more productive,

how can they empower you as a creator, as an artist

or as an engineer, I think you're gonna just keep winning.

- Yeah, there's a lot of complicated trends underway

and it can be hard to break them down and distinguish.

And I think a lot of people like the theories

that get the biggest traction on social media

often don't capture the real underlying

mode of forces at play there.

But yeah, I think AI involved in code production

will probably create a net benefit for the need for humanity

to be involved in coding.

It may change parts of jobs,

but I don't think it's gonna obsolete anybody

who's willing to learn new ways of doing things.

And it's always been this way.

And I think that there's also a lot of over hype in AI.

AI is really great at spewing out code that does something

that a million GitHub repositories already do

because it's, you know,

kind of learned the underlying pattern.

It's notoriously hard to get to do something new,

it hasn't been done before,

especially when it's a complex task.

And you know, the bigger amount of code you ask AI for,

the more it leaves you

with just a massive code that sort of works, right?

And that's the problem with code it like 99% works,

but the 1%.

Might be harder to get to 100% with AI

than with hand coding.

And everybody who's looking at this topic should actually

try using the coding assistance on hard problems

and see how they do there.

- Yeah, I think it, for me personally, it makes it more fun

and faster to generate boiler plate code

so I can focus on the harder decisions,

harder big picture decisions

and harder innovative decisions and all that kind of stuff.

And just makes programming more fun for me

because I feel less lonely.

(Lex laughing)

I have like, even when it gives the wrong code,

I feel like, oh, okay, well that's a way to do it.

That's interesting, and then you could talk to it maybe.

Maybe that shows something about the programming experience

that it is in part sometimes a bit lonely.

- The topic of boiler plate code is an interesting one

because like the mere distance of boiler plate code

is a failure of programming language

and of the idea of creating software modules, right?

You know, you ask AI to create a sorting function, great,

now you have another sorting function

that might be buggy alongside the million others

that different people have written.

It would be better to have a sorting function

that's been written and tested and optimized

and everybody relies on it.

And more modular software,

I think will actually reduce the opportunity of AI

because, you know, people doing programming work

will largely be solving unique problems.

They're actually hard problems in themselves

and not just connecting other widgets.

- Yeah, I think as in many cases,

AI will just help improve the human systems

by shining a mirror to ourselves.

I have to apologize for the pothead question ahead of time,

but let's talk about the metaverse broadly.

You've been a big proponent of the idea of the metaverse.

We'll talk more specifically what that means today,

but we've been talking about simulating reality

better and better and better.

(Lex sighing)

So the pothead question is, what does it take

to simulate reality to the level

we see around us today?

How far away from that are we

to simulate this ultra realistic,

immersive fun reality that earth is?

What does it take?

- We're going to get shockingly close over the coming years,

certainly less than 20 years.

If you look at the progress, what areas

where we have achieved total photo realism

and what areas where we fall short?

We're getting very close in awe,

non-human interactions you see in the world,

walking through a jungle or a city,

all the lighting, it's very close.

And that might be just a few years away,

but then all of the problems that involve humans,

human dialogue and intent have a much, much, much higher bar

that they need to meet to satisfy our brains

and convince us that they're realistic and/or real.

And yeah, I think that's gonna be the primary challenge

of graphics development

and simulation development over the coming decade.

- So the realistic humans, that's gonna be the bottom line.

Yeah, so, and visual and behavior too, so everything?

- Yeah, I was asked about this about 10 years ago

and I said that even if you gave us an infinite amount

of computing power, we couldn't simulate realistic humans

because we simply don't have the algorithms,

we have no idea how to simulate human intelligence.

And that was absolutely the case then,

but it's not really true anymore.

You know, what we're seeing

with generative text AI is not only at a level

that you could say that it's actually doing

a pretty good job of simulating human, at least humans

at the text level, not at the emotional level yet,

but at least at the level of words spoken and find more

and more ways of training it on more and more scenarios

that, you know, you might have

a very, very compelling human simulation going on

in the next five years even.

I'm not saying it's a good idea,

but I like think the arc of the technology

is inextricably heading in that way

and it's heading at a shocking, shocking rate.

- You know, we don't say this enough,

but the current state of LLMs, I mean

if you put Alan Turing in conversation with ChatGPT,

I mean it really passes the Turing test

like almost definitively passes the Turing test.

Of course we like keep raising the bar.

Well, the Turing test is not a real test,

it's not a useful test, whatever.

We just keep raising the bar for AI where it's always going

to be lesser than.

But yeah, you have increasingly ultra realistic faces

and bodies combined with increasingly moving

and powerful full of emotion, speech, text.

You know, I work with this amazing company

called ElevenLabs that does text-to-speech well.

There's companies that specialize

in bringing text to life, right?

That's going to increase,

different companies do that very well.

And then all of a sudden you have

this synthetically created scene where human is speaking

and you're moved to the point of tears because of the scene.

Beautifully lit face in the full darkness, the emotion,

the drama of the scene.

Yeah, I think so you're saying five, 10 years maybe 20.

- Yeah, absolutely.

We'll definitely see it in our lifetimes.

- Increasing the level of potheadness in my question.

Do you think we might live in a simulation?

And if we do or don't,

how hard would it be to build such a simulation

where we're fully convinced we're in it?

- Well, I don't think

that these questions are necessarily unanswerable.

I think I'd like to see more actual effort

to ascertain like what is the underlying

mechanism of the universe.

And I don't think we're here for no reason at all.

I think the world's a pretty cool place

and the fact that we can exist

and, you know, the laws of physics

and especially a standard model of physics

and all of the parameters that lead to, you know,

these atoms and life evolving

and the presence of thermodynamic gradients,

that's really cool.

And I think it's a worthy field

to study more about that holistically.

I dunno, the question of are we living in a simulation

ourselves always boils down to, well,

if we are living in simulation, what are they living in?

Because at some point there has to be some base reality.

Or, you know, one of the philosophical theories

that was put forth seriously was

that there is no physical reality.

If you have a system of equations, you know,

such as the laws of physics, then all possible evolutions

of dynamical systems under those equations

kind of have a physical reality.

So we just are kind of a manifestation of laws of math

rather than needing an actual universe around us.

I dunno, I like dabbling into that philosophy.

And as we see AI becoming smarter and smarter

and we get closer and closer

to really capturing the full laws of physics,

these questions become quite a lot more compelling.

- You know, you start to think,

if we're not living in a simulation,

what are the things about this reality

that are not simulatable?

So what are the big mysteries around us?

It feels like the physics is simulatable.

It feels like a lot of the incredible stuff

that we talked about while super nice seems simulatable.

But then there's the flame of consciousness,

the feeling of it, whatever that is

that lights up in our eyes as humans.

Maybe that's not simulatable.

Maybe that is the thing.

Maybe that's a thread that connects to the explanation

of the mechanism, as you said, of the universe

that's really important to understand.

And we're completely clueless about that mechanism.

I mean, a lot of the religious texts sneak up on

what that mechanism is, but we're still mostly clueless.

We only have these like leaps of faith

in believing what that mechanism might be.

- So, you know, the whole idea

of nested simulations perhaps, you know,

given an sufficiently advanced technology is kind of mooted

such that if you wanted to simulate another reality,

you're kind of just actually creating the reality.

You're doing, you know, quantum mechanical operations

that would produce the same result anyway

and you're running them at full performance.

So it's not really a nested simulation,

it's just another thing that's happening in the universe.

So that would be interesting.

But I think it's ultimately a theological question

and because it's no longer cool to deal with theology

as part of science, there's not been much work on that.

You can't publish results on those topics

in a respected physics journal.

So I think it's kind of been set aside,

but it's interesting to note that the laws

of quantum mechanics themselves have a place for, you know,

god or souls or whatever external source of input you might

want to attach to such a thing.

# Chapter 10

of nested simulations perhaps, you know,

given an sufficiently advanced technology is kind of mooted

such that if you wanted to simulate another reality,

you're kind of just actually creating the reality.

You're doing, you know, quantum mechanical operations

that would produce the same result anyway

and you're running them at full performance.

So it's not really a nested simulation,

it's just another thing that's happening in the universe.

So that would be interesting.

But I think it's ultimately a theological question

and because it's no longer cool to deal with theology

as part of science, there's not been much work on that.

You can't publish results on those topics

in a respected physics journal.

So I think it's kind of been set aside,

but it's interesting to note that the laws

of quantum mechanics themselves have a place for, you know,

god or souls or whatever external source of input you might

want to attach to such a thing.

And that, you know, that there's this idea

of quantum ways function collapse, that when we, you know,

look at a quantum system evolving

and perfect super position of many possibilities

and you go to observe it, you actually just see

a specific possibility.

In the multi-slit experiment,

the light ultimately ends up being observed

going through one slit or the other.

And that's a place where there's this random number

being injected into everything around us.

You know, trillions of trillions of trillions

of times per second and everything we're observing.

And if you want to ex attach some external input,

well there's a place. (Tim and Lex laughing)

- And it could be seriously accessible

to the rigors of science, but we just know so little there.

- Yeah, it's funny, and in that area,

we know nothing more than cavemen knew whatsoever.

We know than the laws of quantum mechanics.

And we have computers that maybe

soon more advanced than we are,

but we just don't have any answers

to the fundamental questions about life,

the universe and everything.

- Do you think sort of more practically,

do you think we'll create video game worlds

of the metaverse variety in which humans will want to stay?

So I mean, to me, this kind of discussion

of a simulated reality, the real test of immersion is like

not wanting to go back to the real world.

As a perfectly healthy, excited, normal human being,

choosing to stay in that world.

How hard is that, do you think?

- Well, I think the technology is coming

and then there's a human question

of should we go that far?

- [Lex] Should we? Yeah.

- And certainly as a game developer ourselves,

Epic doesn't aspire to that.

We make fun games.

And you know, the ultimate manifestation

that we found is fun games that people play together

to have fun in between, you know, work

and the other things in their real lives.

But as the simulations get more and more realistic

and the capabilities become more and more real,

I think we have to ask ourselves some hard questions

about how should humanity operate in that space?

What are the limits that we should go to

and what are the limits we should set?

- Yeah, I think there's gonna be some hard questions

and I think maybe I'm just being human-centric here,

but there should probably be some legal bounds

on two things,

sort of not creating a reality

in which humans would want to stay too long.

Sort of, yeah, focusing more on the game side.

And more importantly,

not creating simulations of humans

that could suffer.

To me, you know, as we talked about

creating ultra realistic humans,

eventually that means creating humans that can suffer,

that can fall in love and experience heartbreak and loss.

It can fear death.

And the more you simulate that to the full reality

of the human condition, the more you get to this place

where you have assimilated humans

that is able to suffer.

And I think legally speaking, I think you have to get

to a place where that's not allowed.

Like there is a line you can't cross.

And that's a hard thing for humans to deal with.

That's gonna be some interesting Supreme Court cases.

Once you create a human sufficiently realistic to

where they can suffer, means that human could be tortured

and you know, terrible things to that human

that's "artificial" quote unquote.

But boy, that still feels wrong.

I don't know what that is,

but you feel wrong

to torture a simulated human.

Now when you play a video game and it's a shooter

and everybody's having fun, that doesn't feel wrong,

but there's a line and that's gonna be a fascinating line

for the Supreme Court to explore. (laughs)

Oh man, what an exciting future we're living in, huh?

- Yeah, you know, I think the thing to appreciate

is like game developers have just generally

been on the good spirited side of things.

If you look at the worst things that people do

and in popular video games today, it's like what?

You rob a bank in "GTA."

Well, it's clearly fictional and awe and fun

and not serious and over the top.

Yeah, I think, yeah, as things get more realistic,

especially simulation of humans,

yeah, there are some hard questions

that will have to be answered there.

But I think the thing that all games developers

need to remember is we're here to make people's lives better

by entertaining them,

providing them with fun and a diversion from other things

and being a part of their lives

and not trying to be too big or being too much

and not trying to provide an alternate to reality,

but to just provide a fun source of entertainment

like the many other things that people do for fun.

- So you spoken,

like I mentioned about the metaverse for many years.

Let's step back, what is the metaverse?

And speaking of fun, you know, "Fortnite," (laughs)

you know, just hundreds of millions of people

just enjoying themselves in this huge scale social game.

You could call it a metaverse,

maybe you can describe the different flavors,

the layers of how you see what the metaverse is.

- You know, the metaverse is an idea whose stock price

goes up and down depending on who says what

on what day.

And some have an ability to drive it way down (laughs)

by opening their mouths.

But ultimately this is about

multiplayer social gaming experiences.

You and your friends getting together in a 3D world

and having fun together in any way you want.

You know, if you're playing "Fortnite: Battle Royale,"

in my view, that is capturing the essence of the metaverse.

And it's, especially in "Fortnite" when we got Sony on board

so that all players on all platforms in "Fortnite"

could play together, could voice chat together

and could be part of a single game experience.

It really took on a new nature,

which was not just like a multiplayer game in, you know,

with Heritage from "Doom",

but also a true social experience

between you and your friends.

And yeah, "Fortnite: Battle Royal"

is just one manifestation of that.

Another one is like "Rec Room VR", where you're standing

around in VR with friends playing billiards

or shooting hoops and we're doing other

like light entertainment things.

I think every game that has a huge number of players

who play together socially as part of their, you know,

entertainment lives.

Yeah, I think is really getting at the core essence

of the, you know, aspiration for the metaverse.

And, you know, we're still in the very early days of it.

You know, I was on the internet and like 1992 or so,

and you know, it was a pretty bare bones thing.

I think when we look back at the state of gaming today,

we'll realize that there's a lot further

to go to get to the ultimate version of it.

But, you know, I think it's all on track.

And I think it was the time we released

"Fortnite: Battle Royale" and started playing together,

all the people at Epic and Squads

and experiencing that world that we realized

that this trend was afoot and that we needed

to do everything we could

to bring in other creators so that anybody could, you know,

pile on to the work we were doing

by creating their own worlds, you know,

for through "Fortnite Creative" and UEFN

and creating more games

and more genres that people could play

and ever expanding the repertoire of fun.

- Yeah, I would love to sort of talk about

different aspects of that a little bit more

because, you know, Epic has created a lot of amazing games

"Unreal Tournament", "Gears of War,"

but the game that I think is fair to say

that transformed the gaming industry was "Fortnite,"

or "Fortnite: Battle Royale" especially.

Can you explain the origin story of "Fortnite"?

- Well, "Fortnite" has humble beginnings.

In 2011, we just been in the final days

of finishing one of the "Gears of War" games

and we wanted to explore ideas for new games

and we'd had a general idea that we would like to build,

you know, some smaller games, online games

or to learn more about, you know, that space

and not just have one single massive game in production

at all times and only one.

And so everybody in the company was given a week

to form a team and work with whichever coworkers they wanted

and build a game, you know, using Unreal Engine

so you can actually build something

pretty interesting in a week.

And one of the teams built

the very first version of what became "Fortnite."

The very first version of it had a different art style,

but it had the idea at the core that you're going

to build forts by day using this building system.

Then night would come

and you'd defend the forts against zombies.

And you know, the longer you could go,

the more elaborate forts you could build

and the more survival, you know, waves you could withstand

and it would get cooler and cooler with time.

And you know, that game was in development

for a very long time.

We always saw the potential, just the building aspect

of it was incredibly fun.

But we made different pivots at different times.

At one point we moved

to the current "Fortnite" art style,

away from kind of more of a realistic style.

Made it, you know, more in the Pixar vein of, you know,

cool stylized characters.

- What was that decision like?

'cause you mentioned "Gears of War" is this like incredible,

like shows off the graphics to the fullest,

different than the artistic style of "Fortnite."

It's amazing that the same company would make this like fun,

silly graphic style of "Fortnite," you know.

- People come to Epic because they wanna work

with the best people in the world

and artists bring a lot of different

personal art aspirations and style capabilities

and many of them are very multi-talented,

can produce photo reel content or highly stylized content.

And a lot of the best artists on "Fortnite"

were a lot of the best artists on "Gears of War"

to change styles,

but continue doing awesome work.

We'd realized that "Fortnite" could be mainstream

and it could be a game people play for a long time.

And so having a, you know, more visually pleasing art style

that's, you know, not as stressful as like a "Call of Duty"

game where you're constantly like pixel hunting,

you know, a dark scene for a, you know,

somebody's rifle scope. (Tim and Lex laughing)

That was the goal, so, you know, a few of the artists

got through into finding a new art style and we moved to it

and at different points it evolved towards being

kind of like a light MMO like "Destiny"

with rather complex RPG and stat systems.

And that evolved into a, you know, kind of an UMO like

tower defense game.

UMO only in that persistence of items and stats, you know,

which became "Fortnite: Save the World" mode,

which we launched in early 2017.

And it was a moderate success, you know,

it paid its budget and we'd come out ahead.

And then at the same time

the "Battle Royale" genre was booming.

"PubG" had just come out,

tons of people at Epic were playing that.

They're like, "Oh, this would be so cool

if it had 'Fortnite' building."

And so we assembled a team in a war room, you know,

like 30 people in one big room.

And you know, they worked insanely hard for four weeks

to build "Battle Royale."

So the nice thing is all the content for "Fortnite"

had been built over the previous seven years.

They had a huge library of content

but no gameplay of the type they wanted.

So they had to build it all in that four weeks and ship it.

And that put Epic on an exponential growth curve

where we went from 300 employees to, you know,

to thousands of employees

and went from about a hundred million dollars in revenue

to billions of dollars in revenue.

And, you know, kinda became the center of the gaming world

at the time.

- Can you actually speak to the technical challenge

of going from mostly not online

large scale gaming platform

to being able to support with "Battle Royale,"

a huge number of people playing with each other

at the same exact time?

Like what's the technical four weeks,

what's the technical challenges

there that had to be overcome?

- Since 2012, we've been building online backend system

to support player accounts and login

and you know, all of the different systems there

needed to make a multiplayer game.

And we've been building them to be scalable.

And by some miracle we built them stably enough

that they were able to scale up.

And you know, so the online team was responsible

for patching that code.

Spent a year of intense work getting it

to scale from like 40,000 concurrent users

to 15 million concurrent users.

Yeah, I mean they're scaling and there scaling,

that's a lot.

- That's immense, but they'd done such an awesome job

of building the foundations that it was tractable,

it was doable.

If they hadn't done that,

then the company would've died that, you know,

"Fortnite" just wouldn't have been playable

and the whole thing would've failed.

- I mean there's just so much detail there

that makes all the difference

because I mean that's what Spotify has talked about

that like the latency,

it's like how quickly you can deliver the song

changes the product from being this shitty thing

that I'd rather pirate the songs to like this is good enough

to where I really enjoy the experience, I want to use it.

And so like yeah, that's really important

to create an experience for 15 million concurrent users

to where it's not lagging

or it actually works, right?

Is there something you could say to the sort of like

how difficult that is to pull off?

- You know, the trend nowadays

for building online services is microservices.

There's not one big server that handles

all of the interactions with "Fortnite."

There's game servers running a hundred player game instances

for each Battle Royale session

and then there's an account server

and many instances of it all talking to a shared database

and there's hundreds of different microservices

talking to each other.

And so scaling is a matter of identifying

what are the bottlenecks in that system

and making sure that each one can scale

and has enough redundancy to be able to handle the load.

Thank God for Amazon Web Services and cloud hosting

because Epic went to 15 million concurrent users

without buying any server hardware.

We are able to just call up Amazon and say, "We need more."

And there was a period of time there

where "Fortnite" was undergoing this exponential growth

and we'd find like one week we ran out of servers in Brazil

during a heavy weekend of play

and next week we had an even heavier weekend of play

and there were servers to handle it.

Like somebody at Amazon had dropped shipped, you know,

millions of dollars of server hardware into Brazil

and turned it on just in time for "Fortnite" to need it.

And you know, there are a lot of unsung heroes

in that story, many of whom we've never heard of.

- Yeah, I mean behind AWS many unsung heroes.

It's like so much of those folks who run

# Chapter 11

what are the bottlenecks in that system

and making sure that each one can scale

and has enough redundancy to be able to handle the load.

Thank God for Amazon Web Services and cloud hosting

because Epic went to 15 million concurrent users

without buying any server hardware.

We are able to just call up Amazon and say, "We need more."

And there was a period of time there

where "Fortnite" was undergoing this exponential growth

and we'd find like one week we ran out of servers in Brazil

during a heavy weekend of play

and next week we had an even heavier weekend of play

and there were servers to handle it.

Like somebody at Amazon had dropped shipped, you know,

millions of dollars of server hardware into Brazil

and turned it on just in time for "Fortnite" to need it.

And you know, there are a lot of unsung heroes

in that story, many of whom we've never heard of.

- Yeah, I mean behind AWS many unsung heroes.

It's like so much of those folks who run

the modern internet, all the incredible services, the games,

the services that we take for granted

are currently being run on AWS

or were originally and Google Cloud and so on.

Yeah, can you speak to how much money "Fortnite" made?

(Lex laughing)

So this is like one of the greatest successes

in the history of video games also.

- "Fortnite" makes billions of dollars a year

and that's the majority of Epic's revenue

that we have a robust business

around on Unreal Engine licensing, "Rocket League"

and "Fall Guys"

and some other tools like the Fab content marketplace.

But the majority of it is "Fortnite"

because we've chosen to reinvest heavily in building

what we think is the future of technology.

We're spending more every year than we're making.

And for a bit of time we were spending

over a billion dollars a year more than we were making

and we found that to be unsustainable

and we went through some painful layoffs at that time

and then we stabilize and now we're spending

several hundred million dollars a year

more than we're making,

which we can very well afford to do

because we have billions of dollars in the bank.

You know, thanks to a combination of the profits we made

when we were a very small company with a very big game.

And because of investment we've raised.

We're not an pumping oil out of the ground at

where we discovered oil.

We are growing to be a future technology powerhouse

and we think that 3D space

and the future of real-time 3D simulations is going

to be one of the major facets of technology for humanity.

And we're all investing in that.

- Yeah, it's exciting to see

that investing in a long-term future,

sort of taking the risk of doing the research

and defining the next chapter of Epic.

So using the successes of the day

to invest into the successes of tomorrow,

that might look very different, like completely different.

And part of that is investing in the developments,

the research and the innovation in the Unreal Engine.

- That's right, we're a company

that can start working on a project knowing

that we won't reach fruition or make any money

from it at all for three years, four years, five years.

We're totally okay with that.

And you know, that's the cycle

that's fueled our growth over time.

It's constantly investing in the future

and you know, being a serious company that's doing

serious R and D side by side

with shipping and maintaining products

and earning money from them.

- So can you speak to,

I mean there's several directions here.

So one of them sort of the future evolution

of this idea of the metaverse,

so potentially creating communities.

So "Fortnite" is this incredible,

huge community of humans interacting,

but your vision is to go outside of just one game.

So what is the kinds of standards

that you're thinking about building

such that people can sort of have an identity

to almost travel between games and that kind of thing?

- Lemme start with the present of gaming and why it sucks.

(Tim and Lex laughing)

- Like that's a good start, sure.

- "Fortnite" is an awesome thing.

You go into "Fortnite," there's, you know,

a hundred million monthly active users there,

a huge number of your own friends are there,

you can play with them,

go from experience to experience seamlessly

without leaving the app.

There a hundred thousand different islands you can play on.

And some of them are really awesome

and they're constant new ones coming out

and constant things to do.

If you wanna play "Roblox", all right, you quit

out of the "Fortnite" app, you launch the "Roblox" app,

different program, different friend system,

different account names, your username in "Fortnite"

and your username and "Roblox" are different names

and they're not connected to each other.

So you have to remake all of your friends

and then find different, you know, things to play.

And now the controls are different.

So you have to relearn how, you know,

the joystick, mouse, keyboard controller works in

that experience and you have to go from place to place.

And you buy some stuff in "Fortnite" and it's really cool

and you can use it anywhere in "Fortnite."

And then you go in "Roblox"

and you don't have that stuff,

you have to buy different stuff

and that stuff only works in "Roblox".

And same with "Call of Duty", it's another isolated place.

And same with "World of Warcraft",

and same with "League of Legends"

and every place you go is its own unique place,

different friends, different account names,

different people.

And there's no social cohesion between them at all.

And long time ago, console was set out to solve this problem

by creating their console-wide friend system in account.

So your friend on PlayStation in one game is your friends

on PlayStation in another game, but only on PlayStation.

If you're on Xbox you can't see PlayStation friends.

And so you have two basically orthogonal

and cross-cutting divisions of the world into fiefdoms,

you know, which were not created with bad intentions

but arose and are, you know, separated, isolated islands.

One is the platforms and their social services,

Xbox, PlayStation, Nintendo,

it's Steam, Epic if you add it to the list.

And the other is these different games people play

and you know, because of this weird historical artifact

where we're left in a world

where people can't seamlessly move from games to games,

bringing their friends and their stuff.

So the solution to this is to federate

and connect all of the systems together.

All of the players on all the different platforms

can be recognized by their name

and put the @ sign in it,

so your Xbox names and your "Fortnite" or Epic names

and your Steam names can all live together

and operate together in a single space.

So unifying the social ecosystems

is one thing that needs to happen.

The next and bigger challenge is to unify the economies too.

Now I'm not talking about like a sword you have in

"World of Warcraft" should work in "Fortnite".

(Lex laughing)

Every game's gonna have its own gameplay rules

and a lot of games are gonna have stuff

that only works in them.

But you know, there's a huge set of games

that have in common the idea of a cosmetic system

that does not affect gameplay outcomes

but is, you know, purely cool looks and cool appearances.

Most of the major multiplayer games have them

and you know,

if you look at games you could probably bundle it together

about 70% of them and say they're similar enough

that they could actually interoperate.

That you could own an outfit in "Fortnite,"

own an outfit in "Roblox",

and own the same outfit in maybe "Call of Duty"

and maybe, you know, a hundred or 200 other games

and actually expect they would work together.

And you find other kinds of items

are probably interoperable too.

Like "Fortnite" has car outfits so you can, you know,

buy different appearances of a car.

And when you find a physical car in the world of "Fortnite,"

if you're the first person to get into it in that session,

boom, it takes on your, you know, your chosen car cosmetic

and now you have a cool car that's identifiable as yours.

You know, we realized early on with "Fortnite" that the key

to making "Fortnite" work as a creator economy

was to open up the revenue from the item shop

to all of those sources of engagement, right?

There are two big things happening in "Fortnite"

that make it work as a product and as a business.

One is the game modes, "Fortnite: Battle Royale",

and all of the user modes and everything else

are sources of engagement.

People play there because it's super fun.

And because they're playing there, they're willing

to buy cool stuff to make their character look cooler.

And so you have all of these sources of engagement,

but the sources of engagement don't make money directly.

You can't spend money in "Fortnite: Battle Royale"

to buy a game item like everything's, you know,

the gameplay is not pay to win and it's all just a game.

So we make money from the item shop

and the item shop only exists

because of the sources of engagement.

If you weren't playing "Battle Royale," trust me,

nobody would wanna buy a "Fortnite" outfit.

If you weren't playing any "Fortnite" games,

why would you buy "Fortnite" outfits?

And so you have all the revenue in this item shop economy

and all of the engagement in this engagement economy.

And the thing that magically makes the "Fortnite" creator

economy works is revenue sharing.

Item shop spending according to sources of engagement,

buy engagement, if you buy an item

and you've played, you know, 40% of your time

in Battle Royale and 60% of your time in these user modes,

the amount you spent, the portion of that

that's profit can be separated out

and paid out to all the different creators

who participate in that economy.

And that's why "Fortnite" scaled up

to a $400 million creator economy so far and is growing.

- It's amazing.

- One of the really critical things we aim

to do in designing that is ensure it's a creator economy

that could scale to other companies, other ecosystems.

And say, you know, right now we have

many industry standards bodies,

so one standardized game ratings, you know,

age ratings of games, another standardized file formats

for the web, another style, you know,

standardizing file formats for 3D

like Khronos Groups in the Metaverse standards form.

If we had a standards body standardize

what are portable outfits in games, you know,

game outfits you could buy in one game that work in another.

What are their, you know, dimensions

and what are their capabilities

and what can you do

and what can't you do and so on.

Then you could have an item economy where every game agrees

to respect each other's item purchases of that sort.

And revenue is shared between ecosystems as well.

- That would be incredible.

That would be so amazing.

Is there, first of all, just it seems silly maybe

for people who don't play video games,

but an outfit is an important...

If an outfit can be persistent across video games,

I mean, I don't know what's the purpose of life?

Like, why do we wear clothing?

Clothing is a part of our identity.

It's how we present ourselves to the world.

It's, you know, I wear the stupid suit and tie.

It feels good.

It feels good when I put it on.

And even like the other outfit, I have two outfits,

this and then a black t-shirt and jeans.

And it feels good to wear that.

It feels like me when I look in the mirror.

Okay, I know that guy.

And to be able to have that outfit go from game to game

to game maybe across years, that would be wonderful.

I wonder if you could just even comment,

could there also be another standardization about the value?

So for more complicated items, so, you know,

take a sword from "Diablo"

and transfer to a gun in "Fortnite."

But based on the value some, you know,

some generic concept of money.

So the value of a thing in one game

versus the value of a thing in another game

where you're almost operating in a space of value

versus the actual items.

Or is that already getting too general?

- I think this can be done, yeah.

We did a lot of analysis of the "Fortnite" economy

and found that some "Fortnite" experiences

lead to or correlate with higher spending than others.

And you know, "Battle Royale" is relatively strong

in that area because you see your character from behind

and see all of your other characters from the front,

and you have lots of opportunities to really see who you are

and to emote and to interact with other players.

And a lot of games have that characteristic.

One funny anomaly stood out.

There was this game

that was one of the big breakthroughs

in "Fortnite," "Only Up."

It's a game where you're just climbing up in the up

by following pads of stacks of objects and things.

It was just stupid fun. (Lex laughing)

Everybody loved, okay, but we found people weren't spending

a lot of money on outfits

when they were playing "Only Up".

It's kind of intuitive actually.

Like you're not seeing other players,

like if you see anything, like you're seeing their butt

as you're like trying to catch up to them,

jumping from object to object and they're above you.

And so, you know, it wasn't a mode

that shut off outfits very much,

but you could, you know,

you can determine the economic correlation

between a game mode and spending.

- That's so fascinating.

I mean, "Fortnite" is this gigantic economy

where you could do those kinds of studies,

you can understand markets, the digital markets

as they emerge amongst humans and what they value.

And from that value, you can probably have a very stable

kind of money that emerges.

- Yeah, I think so.

You don't need like an alternate currency system,

you know, unfortunately, a bunch of ideas have conflated

because people were trying to hype up different things.

But you know, this idea of large scale multiplayer

social gaming, you know, that notion of the metaverse,

you know, there's 600 to 800 million people playing

that kind of game every month.

So like, you know, that's real and that's happening

and it's, you know, very much underway.

VR has a much smaller audience.

I don't think you need VR to have anything like this.

Like VR is hardware that may or may not enhance

the experience for some usage cases.

For some it'll probably be better

and for some it'll probably be worse,

but certainly there's not any set

of "Battle Royale" players flocking to VR.

And the other thing is NFT is it's like you trying

to equate digital or cryptocurrency to the metaverse.

It's just a way of denoting money or value exchange.

You can do that with money or you can do it with NFTs

or whatever, but there's nothing about this future digital

economy that fundamentally requires

cryptocurrency or whatever.

What you need is interoperability.

Interoperability can happen through a blockchain,

it can happen through a database,

it can happen through standards bodies

with defining standards and protocols.

And we've been doing it for hundreds of years

since the railroads were standardized.

And you know, it's not something

that totally requires a novel technological solution.

- Yeah, I mean even on the topic of cryptocurrency,

it's very frustrating.

You know, blockchain and crypto is a really powerful

technology that I think can enable

a lot of the things that we're talking about.

But so many people use it to try to make money

to create these bubbles.

And the hype and the meme coins and the so on and so forth,

that becomes much less about

that drifts far away and rapidly

from things that are actually of value,

which is the experience of playing "Fortnite"

and how you look when you play "Battle Royale."

I mean, it sounds ridiculous to say, but it's true.

But that's valuable.

That's like, you know,

you have like gold in the physical space.

We know that holds value.

How your outfit looks like in "Fortnite" that,

as you're saying, provably holds value.

And so you want to connect

like a standard definition of money value

to that and not let it become this hype thing which NFTs

that you mentioned are just become that.

Like quickly drifts away

into the land of people trying to buy

and sell and try to make money versus like staying close

to the thing that people actually value.

Forget the money, it's more about exchanging

valuable experiences or things of value.

So you can play "Fortnite"

# Chapter 12

which is the experience of playing "Fortnite"

and how you look when you play "Battle Royale."

I mean, it sounds ridiculous to say, but it's true.

But that's valuable.

That's like, you know,

you have like gold in the physical space.

We know that holds value.

How your outfit looks like in "Fortnite" that,

as you're saying, provably holds value.

And so you want to connect

like a standard definition of money value

to that and not let it become this hype thing which NFTs

that you mentioned are just become that.

Like quickly drifts away

into the land of people trying to buy

and sell and try to make money versus like staying close

to the thing that people actually value.

Forget the money, it's more about exchanging

valuable experiences or things of value.

So you can play "Fortnite"

and then go to another video game

and continue the valuable experience

and then come back to "Fortnite" and do that kind of thing.

So you're saying there might be a way to do that

and to basically create standards

the way the web has different standards

for displaying websites and all this kind of stuff

or the communication

that's required on the networking side.

So all the different standards that make the web work,

there need to be those kinds of standards.

Like what would those standards look like

to enable the metaverse?

- We need a lot of different things.

The one area where the standards bodies

have been very successful in creating working standards

implemented by all the major engines today

is in low level file formats for data interchange.

You know, the web has PNG files for 2D images

and in MP3 files for audio.

And 3D has the Pixar USD file format,

the universal scene description, which is a description

of the scene graph, the entire set of objects in the scene

and all of their parameters so that any engine

that supports those features could import that

and then render the same scene as the engine they came from.

You know, large parts of this work across Unreal Engine

and Unity and Blender

and all of these 3D packages of different sorts.

Then there's the GLTF texture format, which stores textures

and geometry and other low level data for 3D objects.

You know, when you see a "Fortnite" character

that file format together with the image file formats

can store their static appearance,

you know, the shape of their body,

even their animations and their different poses

and the appearance of them,

the different standard file formats could store

all of the sounds they make in their emotes.

But we're still missing a bunch of pieces.

The biggest missing piece is the programming language

that's at the center of standardizing the metaverse.

Now if you look at the web, the web is a combination

of a bunch of different technologies.

The two biggest ones are HTML,

which describes the 2D scene graph or the, you know,

2D layout of controls and objects on the webpage.

But that's just static data.

It's just a non-moving, non animating webpage.

And then you have the JavaScript programming language,

which is used to manipulate that to display things

to the user and to implement anything

you could implement in code.

So it's a little programming language

that runs in your web browser.

And the Metaverse needs something

that performs that similar role.

But the Metaverse and 3D gaming in general needs something

that's rather more powerful, more safe, more scalable,

and more capable than JavaScript

because the metaverse is actually more difficult

technical problem than a webpage.

A webpage like an app is just a single bundle of code

and content that somebody, a company, has prepared

and they release it and it stays exactly what it is

until they release a new version

and it's upgraded from version to version as it goes.

But the metaverse needs to be a composite of code

and content built by millions of different people

that could potentially form a seamless world together.

- Yeah, it's fully distributed collaborative.

First of all, also the amount of data,

I mean it doesn't have to be that way,

but websites are showing very little information.

The metaverse, even when it looks like something like

"Fortnite," just the amount of information

that's conveyed in the scene graph

as the individual players are collaborating is a huge,

huge, huge amount.

- Yeah, the highest detail of "Fortnite" updates

amount to about 60 gigabytes of data.

And you know, that's just a small part of

what exists in the "Fortnite" creative economy.

And if you look at what this might be in a decade

as standards emerge, you might have exabytes

of data out there.

"Fortnite: Battle Royale" is I don't think

the ultimate manifestation of gameplay that will,

you know, ever be invented.

What we've seen time and time again is that

as we gain more technical capabilities,

graphics gets more capable, CPUs become more performant.

You know, web services become ever more scalable.

We've seen new genres of games that emerge

that weren't possible before

and you know, "Doom" ushered in the era of Death Match

and the first time 3D multiplayer game

was even possible at all.

You know, the early "Battle Royale" games

starting about 10 years or 15 years ago

only became possible back then.

You couldn't have built one 20 years ago

because you just couldn't have rendered an environment

that's as large as a VR game with that many players,

with that level of interaction and performance.

It was just not possible to run it.

So you got a certain level of technical capabilities

and a genre came out that proved to be

by far the best shooter genre ever invented.

But I think there are numerous, numerous more genres,

some of which are better than any of the existing ones

that will be invented as we get more and more capabilities.

You know, some of the capabilities we're lacking now

are the ability to build environments and game simulations

that span more work than a single company

can possibly create.

And you know, you see kind of the birth

of that idea in "Fortnite" and "Roblox"

where there are tens of thousands creators,

each building content.

And users are playing meaningful amounts of it all.

And so there's an ecosystem

that's scaled larger than company,

but it's still very much you go into one island

and you play that creator's work.

The other direction of its scalability is putting more

and more of people's work together in a seamless continuous

play space for games where that makes sense.

You know, you can imagine a game taking place

in an environment that is the size of a continent

or earth in which you can like go from place to place

and then see different areas

which are maintained by different people.

So you go into different spaces,

the game rules are customized according to that

and you can go from experience to experience

and instead of having just one company's authorship

ever present wherever you are,

yeah you'd see you'd be driving a car built

by one person, carrying weapons built by 20 other people

and you know, taking place in a simulation in an environment

that's built by thousands of other people, you know,

and working for separate companies or their own,

you know, entrepreneurs or indies or enthusiasts

all working together simultaneously.

And we totally lack the programming foundations for that.

You know, the kinds of code you would need

to write now to make that happen are just not practical.

And so we're investing massively in building

new programming language technologies around Verse

and our proposed standards for, you know,

future metaverse programming

that we hope will solve those kinds of problems

and make that kind of world possible.

- So first of all, that's a super exciting future where,

you know, it's not hundreds or thousands,

it's millions of creators that can just create

different small or big elements of a world as big as earth.

Just if you sort of close your eyes and imagine that world,

that's really exciting.

Where it's not a centralized company controlling

the release of a particular island or so on.

It's people constantly dynamically modifying

all the islands of reality in this digital world.

So if you could speak to some of the technology

that can enable that,

you mentioned the Verse programming language.

First of all also, how legit is it for you CEO of Epic Games

to be a co-author?

The programming language theorists are losing their mind.

(Tim and Lex laughing)

So co-author in a paper that's describing

some of the sort of nuance details

of a programming language.

So maybe you could speak

to this programming language called Verse,

it's a functional logic language.

What is it?

What are some cool features of Verse?

- Verse is a programming language that we're building

for large scale simulation programming.

It's designed to make it easy to write code

that can scale up to

not only you building a "Fortnite" island

but you building modules

or components that can be used by millions

of other programmers and coexist in a huge environment

and also can scale up to a huge scale simulation.

Some games will be small "Battle Royale" might find

that, you know, a hundred players is actually optimal.

It might be the a thousand player version of "Battle Royale"

would be worse,

but I bet there are a thousand, million

and tens of million player experiences,

they're even better than that

that will yet to be discovered.

And so... - Wait, wait a minute,

tens of millions of players together.

- Sure we've had "Fortnite" events

that have attracted 15 million concurrent users

but you know, the fact that they're all divided up

into servers with a hundred players each

for those events isn't really a positive.

It's just a limitation of the technology.

Tracing back to Unreal Engine 1

and its single threading decisions.

You know, if we could build a concert

where all the concert participants,

potentially tens of millions of them,

could participate together simultaneously

and see that there's that massive a crowd

and they could all do interesting things

and interact with each other, that would be way cooler.

- Just if we just, sorry I'm just loading it in,

just imagining together

in one scene graph, 10 million people interacting,

what a cool world that is.

- Sure, well, you know, 10 million people,

you have less than 10 million pixels on your screen.

So what does the Nyquist sampling theorem say?

It says that you don't need full overhead for every player,

you need to render the players around you

in some approximation of everything else.

- Yeah, too, but there's also a networking component

like yeah you're speaking to the rendering but like, oh boy.

(Lex laughing)

- There's a lot of work that has to happen there

but you know, this is what we do for a living,

we solve hard problems. - [Lex] I understand

- 'Cause if they're easy then other people

could have solved them already.

- That's really cool though.

Just sort of the possibility,

the vision of that is really cool.

Even just, you know, even a hundred thousand people

were like bring 10,000 together just to...

I mean there's a reason in the physical world

when you go to a concert

and you have all those people around you,

that energy or you go to a football game,

that energy is unlike anything else.

And if you can bring that energy to the digital world,

that's amazing.

Yeah, but anyway, so sorry.

So on the technology side of bringing that to life

on the programming language side,

can you continue, as I rudely interrupt you

talking about Verse.

- Versus the functional logic language

because we think that's the way to make the most simple

and powerful language simultaneously.

Back in the 1970s, the programming language designer

who built Pascal, one of the early programming languages,

Niklaus Wirth or Nicholas Wirth,

as Americans might call him, stated this principle

that programming language should achieve

a high degree of power not by having a lot of features

but having by having a small number of features

that work together and can be composed together arbitrarily.

So that you have to learn a relatively small set of things

and then the real knowledge comes as you learn ways

to combine them to achieve bigger and bigger programs.

And so, you know, there's long history

to the field of programming languages,

but in the 1950s the first programming language designers

got together and built the first standardized language

called ALGOL.

And there was this meeting in 1956,

very few people even know about,

but it's where all the major foundations

of modern programming languages were decided on.

That the C family of languages inherited.

And so we're very much living in a world

that was defined by them.

And thankfully they got a whole lot of things right.

They defined how functions should work,

how variable should work and how recursion should work.

And you know, thank God they got those things right

but they got a few things wrong

and Verse is trying to fix those.

And that's the functional logic part of it.

The interesting thing about functional logic language

is that in an old school language

an expression produces a value.

In a functional logic language,

an expression can produce zero, one or multiple values.

If it produces zero values, we might say it fails.

If it produces one value, we say it succeeds.

And if it produces multiple values, it's kind

providing a set of values you could iterate over.

And so there are a bunch of features

in today's programming languages that were defined

in an ad hoc way without really thinking this through

this zero, one or many values way.

And that's the problem

that functional logic languages address.

The most basic example,

an if statement in a programming language.

If some condition holds, then do this thing,

otherwise do that thing.

And in the language today this is done with variables

of type boolean or expressions that produce booleans.

We have boolean variables that are either true or false.

We have expressions that evaluate to boolens.

And so you can express a condition

as a bunch of these features together,

but you've lost any computation you've done

in doing that boolen expression evaluation.

So in a functional logic language,

your condition wouldn't do that.

It would either succeed

and produce a value or it would fail.

If it succeeds, it goes to then branch,

your operation succeeded. now you're operating, you know,

running this one batch of code.

And if your expression failed

then you go to the else branch.

But the exciting thing about that is your expression

that succeeds or fails can produce values

and bind variables that are then accessed

by the then branch.

So you can write a conditional where you can only get

to the inside of the condition the then

if a bunch of variables have successfully

been bound to variables.

So it lets you test if some conditions hold

and then use the results of those tests.

And that gives you a much higher level of reliability.

And then a for loop in a traditional language,

it's just a bunch of imperative code that's woven together

to produce a bunch of values iteratively.

It's rather awkward to do complicated things in for loops.

And so you often end up with either ever more complicated

constructs built to work around that,

like iterators and other things.

The idea of functional logic languages

is your for loop can just produce multiple values

and if it produces zero values

you got to reiterate zero iterations.

And it produces a bunch of values,

you got all of those as your iterations.

Rather than having a bunch of nested loops,

you can write arbitrary things

that look like SQL queries in a condition

or in a for loop that bind a bunch of variables,

do a bunch of tests, produce a series of results

and in some order that you're iterating over

and then you can handle all of them and produce a result.

So you kind of gain the power of SQL queries,

you know, large complex queries over data structures

in a language that is much simpler

in which your code is just performing

simple iterative operations.

And so it kind of gives you the best of databases

and of regular programming in a much more uniform way.

# Chapter 13

The idea of functional logic languages

is your for loop can just produce multiple values

and if it produces zero values

you got to reiterate zero iterations.

And it produces a bunch of values,

you got all of those as your iterations.

Rather than having a bunch of nested loops,

you can write arbitrary things

that look like SQL queries in a condition

or in a for loop that bind a bunch of variables,

do a bunch of tests, produce a series of results

and in some order that you're iterating over

and then you can handle all of them and produce a result.

So you kind of gain the power of SQL queries,

you know, large complex queries over data structures

in a language that is much simpler

in which your code is just performing

simple iterative operations.

And so it kind of gives you the best of databases

and of regular programming in a much more uniform way.

And the power of this is now users can write functions

that not only produce a value,

you can write functions that might fail.

And so you can write a function that answers a question.

The answer can be either a yes and my value is this or no.

And you can combine these together into arbitrary queries.

And if you like, the funny thing

is that this is not how C++ works.

And so when we have Epic programmers moving over from C++

and writing their first Verse code,

they try to write C++ code and versatile

and it actually ends up being convoluted code

that's worse than good C++ or good Verse.

But after a few months they get up to speed

and they're writing really awesome code that's tighter

and more compact than before

and with users who've never programmed before

but are learning programming for the first time

in the context of "Fortnite," it's really fascinating.

You see these users are learning this kind of as

it becomes their intuition.

They just assume programming works this way

and they're writing way more advanced

and interesting for loops and conditions

than we're often writing internally

because they've kind of rocked the core concept.

- Yeah, I mean you said a lot of really interesting stuff.

First of all, it's very interesting

that there's a bunch of people,

a lot of people learning programming

for the first time with Verse,

which is a very different way to look at programming

and some deep sense as you're saying,

a very intuitive way to learn programming.

But there's a lot of properties about this being

a logical language,

one of which will maybe speak also about confluence

but also correctness.

So being able to prove the correctness of a code

is basically easier to write bug free code.

Can you just speak to that

and the importance of that

when you're building the metaverse?

- Yeah, right, so the challenge with the metaverse

is first of all that it's a huge base of code

that's evolving over time and written by many authors.

So you might see every second a new module is updated

somewhere and you expect in this live ever running

simulation that never shuts down for everything

to upgrade live in place.

And so one critical component that is the ability to

release an update to something you've already published

and be sure that it's backwards compatible with the one

that you've already released.

And that's essentially a type checking problem,

checking that your new interface is backwards compatible

with your old one.

And that comes down to the type system of the language.

There's been a lot of very interesting research

on type systems over the years, most of which

hasn't ever made it

into the C++ programming language unfortunately.

But you see several branches of that whole field.

One of the really interesting things that Java

and C# did in the early days and then later abandoned

and didn't bother update was defining a very rigorous

set of rules for if you publish a module

with one set of types today,

then what changes can you make to that module

for your future updates to it

that don't break backwards compatibility.

And that's a problem for type checking.

You know like say you have a function that promises

to return some integer, when in the future you could say

that returns some natural number

'cause every natural number is an integer.

So that's a backwards compatible change.

But you can't say it returns a rational number

'cause some rational numbers are not integers.

So the, you know, system ought

to reject that kind of change.

But the much, much, much more interesting thing

about type checking, it was the realization

it was actually made in the 1930s

that if you design a programming language type system

in a very particular way, then it becomes not only useful

for expressing types of variables.

A traditional thing every type system does is say

like variable X is of type integer.

But if you design a type system in a certain way,

then your types can express theorems

like mathematical theorems.

You know the Pythagorean theorem is a cool one.

But one theorem you might set of

in a program is like the theorem

that this function takes an array of integers

and returns an array of the same integers

but the result is sorted.

If you express that as a theorem

and you follow this system of type theory,

then you can actually require that anybody who writes

that sorting function to prove

that it has actually sorted its result.

And so you have types or theorems

and values constructed a certain way

can be proofs of those theorems.

And, you know, nowadays in mathematical literature

you see more and more theorems

are being proven mechanically.

Mathematicians are proving theorems in a way

that is verified by computer to be a correct proof.

In the old days of math, people would write down

like language.

If you look at all of Euclid's theorems,

it was just language.

It was just writing an ancient Greek

to say the steps of the proof

to convince the reader that the thing is true.

Starting in the 1930s,

mathematicians move towards rigorous formal proofs

in which there's a series of steps

that can be mechanically verified, they're proving things.

And when mathematicians say

they've done a computer proof of a theorem,

what they really mean is they've written

the program in a proof language.

Like Lean is theorem prover

a Coq is theorem prover and there are several others.

It means they've written a mechanical proof in that language

that a computer is checked so that it's impossible to lie.

If you say that you've proven a thing

and the computer verifies it, then it's definitely true.

And you know, this is a feature

of mathematical proof languages

but it's also I think an idea

that's making its way into programming language

is gradually over time.

And our aim for Verse is

to be the first mainstream programming language

that fully adopts that approach and that technique

and not only adopts it

but adopts it in a way that's really user friendly.

So you don't have to do that.

And the idea of this is

that you want gradually more information

to be incorporated in the types of variables.

The property you want of a programming language is

that if your compiler accepts your program and doesn't beep

and tell you there is an error,

then your program should work.

Now there are all kinds of ways humans

can make mistakes there

so that we'll never achieve that ideal,

but we can get closer and closer to it by having more

and more language features that enable the compiler

to catch more human coding errors

and tell the user what went wrong.

And you know, that becomes extremely important

in the metaverse, the cost of fixing a bug

that's made it through to a runtime and is in users' hands.

The cost of fixing a bug in a shipping program is

hundreds of times higher

than fixing a bug that you've just observed

as you're running your code yourself.

When it's running on your computer,

you just fix a line of code and your bugs fixed.

When you have to fix it live, you have to release a patch,

you have to release patch notes,

you have to test the patch, you have to check

for all the other bugs that might have been introduced

and everything becomes vastly, vastly more expensive.

So you know, the real aim of the Verse program

and approach is to catch all of these errors at compile time

and make the metaverse a very reliable place.

- Do you see a world where like at compile time

you could prove that the program is correct

in some sense of correctness?

- Proving things becomes commentorially harder

as they get larger, right?

And so the really important thing

about this whole field is that you should be able

to adopt these capabilities gradually

and apply it where you really need it.

Like if you're writing something

like a cryptography algorithm,

that's a good place to prove stuff.

If you're writing a data decompressor that's gonna be used

by an entire ecosystem, like proving that

that doesn't overrun memory, it's actually really important.

And a lot of the reason

that security vulnerabilities happen today

is because in a different language a compiler

could have caught, we're not caught in C

because it just doesn't have this feature.

But yet we shouldn't see this as scary.

Everybody working in a type language like C

or C # or Java is proving theorems all the time.

If you have a variable of type integer

and you assign some value to it, you've proven

to the compiler that value was an integer

'cause otherwise it would've rejected it.

And so, you know, as we add more and more advanced proofs,

we'll get compositional properties flying out of our systems

that they're easy to use and you know, people prefer to use.

And we might think in a future

where we have AI helping us write certain kinds of code.

The big problem with AI is you ask it to do something

and ask you to write a fragment of code that does something,

it might give you a perfectly valid fragment of code

that compiles but does the wrong thing.

And if we had languages where you could say,

write a function that sorts these disarray

and prove that it did that it could actually write the proof

and you could, if the compiler didn't beep with it,

you could trust it was actually sorting the array

and otherwise you could go back to the AI

and say, well that didn't work.

But you know, getting to the point where we know

that our programs do what we say they're going to do

or think they're going to do is a very important thing.

- And by the way, I should mention that you sent me a note

about Curry-Howard correspondence,

which I went down a rabbit hole

and that's a whole fascinating field which shows

the mathematical relationship between programs and proofs.

- That's right, this is a result from the 1930s.

It's one of the most important results of computer science

that almost nobody knows about.

But they did this rigorous breakdown of type systems

and the 1930s formulation of programming

and established that everything you can prove

in mathematical logic you can prove within a type system

if it has certain features.

And you know, if you break down what is a proof,

well a proof that integer exist as some integer,

like five is a proof that integer exist.

So when you have, you know, something like var xn

and you say X equals five, well you're proving

to the compiler that five is an integer, you know,

that comes as secondhand nature.

But you can prove more advanced things.

You know, if you wanna prove that a pair of things are true,

that like theorem A is true and theorem B is true,

then you need to provide a pair of values,

one that proves theorem A and one that proves theorem B

and that's the conjunctive law of proofs.

And there's a disjunctive law too.

And then there's an implication law for proofs.

And it turns out that's really satisfied by functions.

When you write a function of programming language,

you're saying if you give me this thing,

I will give you that thing.

If you give me a parameter of type something,

then I'll give you a result of some other type.

And by writing that function,

you're proving that given one of these things

you can produce another thing.

And that's a proof of an implication.

And with only like seven laws, you can construct

all of mathematical logic in a type system.

And you know, one of the important thing

for programming language is hasn't been given

enough attention is some aspects of programming languages

are just subjective.

They're just machinations

of the programming language designer, you know.

And Guido van Rossum decided

that Python should support indentation a certain way.

And you know, as long as you're dealing

with things like human notation and naming of things,

there's always going to be that subjective layer.

But there are other parts of programming languages

that are not subjective but should be fundamental.

And when you look at type systems,

there is a way to do type systems

that gives you mathematical proofs.

And every other way of type systems

that doesn't give you mathematical proofs is just worse

and should ultimately be rejected.

And so I think one of the jobs of computing is to identify

what have we actually done right in the past

and what have we done wrong

and for everything we've done wrong

actually going back and fixing it

otherwise we just keep accumulating so much croft

that our systems eventually are crushed

under their own complexity.

And you know, there've been massive announcements

of horrible vulnerabilities in software

and services over the past year.

You know, turns out like some nation state backdoored

a bunch of Teleco's surveillance systems for wiretaps,

like huge problem there.

But you know, ultimately when you break it down

it's probably because of some buffer overrun

in some C program.

Like these decisions about programming languages

have long-term implications.

- It's really fascinating that in building these systems

that hundreds of millions of people use,

you're rethinking about like

how do you actually build it from first principles?

So I should mention that Verse's primary design goals,

it should be simple enough to learn

as a first time programmer,

general enough for writing any kind of code and data.

Productive in the context of building, iterating

and shipping a project in a team setting.

Statically verified to catch as many categories

of runtime problems as possible at compile time

as we were talking about.

Performant for real-time, open-world multiplayer games.

We didn't really quite talk about performance,

maybe I could ask you about that in a second.

Complete so that every feature

of the language support program are abstraction

over that feature.

Timeless, built for the needs of today

and for foreseeable future needs, yeah.

And then there's some design goals

that we talked about that is strongly typed.

Multi-paradigm to use the best of functional programming,

object-oriented programming and imperative programming.

So it's as deterministic as possible.

You know if you run it over and over,

it runs in exact same way.

You know, failable expressions as you talked about.

It's super fascinating.

There's so many cool features in this,

speculative execution, concurrency.

Maybe can you talk about concurrency?

Like what is it about Verse that allows for concurrency

at the scale that you need?

- This is the one biggest technical problem

that we're working to solve in this generation

and that is taming concurrency

so that any ordinary programmer can achieve it

by just writing ordinary code.

- It's hard.

- Programming on a single threaded computer

is hard enough but it is completely predictable.

If you have a language that's deterministic

and you're on the same code over and over,

it's always gonna do exactly the same thing

and there's no unpredictability

about what might happen, right?

You're reading and writing variables in some order

and you're always gonna see it behave the same.

The problem is when you introduce multiple threads

or multiple nodes in a data center all working together

on a single problem, is that they each want to read

and write different pieces of data

and change the state of the world as they go.

And still almost all concurrency

and real world programs today is achieved manually.

Programmers are writing this code

that might run in multiple threads very, very carefully

so that they are negotiating among each thread to get access

to data in a way that's going

to give them predictable results.

And it's incredibly hard.

It's so hard that in five generations of Unreal Engine,

every single generation decided we're not

going to try to scale up all of our gameplay code

to multiple threads manually.

It's just much, much, much too likely to go wrong.

Not only for ourselves, but for every partner company

who licenses Unreal Engine

and tries to use it for building a game,

it's just a massive foot gun.

There's a variety of solutions to concurrency

# Chapter 14

and write different pieces of data

and change the state of the world as they go.

And still almost all concurrency

and real world programs today is achieved manually.

Programmers are writing this code

that might run in multiple threads very, very carefully

so that they are negotiating among each thread to get access

to data in a way that's going

to give them predictable results.

And it's incredibly hard.

It's so hard that in five generations of Unreal Engine,

every single generation decided we're not

going to try to scale up all of our gameplay code

to multiple threads manually.

It's just much, much, much too likely to go wrong.

Not only for ourselves, but for every partner company

who licenses Unreal Engine

and tries to use it for building a game,

it's just a massive foot gun.

There's a variety of solutions to concurrency

that are all rather suboptimal.

One attempted solution was like,

"Oh, just don't try to solve this problem at all.

Let's break our program down into microservices.

And almost all online websites have massive scale

like amazon.com work with the hundreds of microservices

where different servers negotiate with each other

by sending messages to each other.

And by programmers writing those things very carefully,

they eventually get to being able to take your orders

and not make a mess of them reliably.

But you know, this is totally not scalable to the metaverse

where you have millions of programmers

who are like mostly not gonna be computer scientists,

they're mostly gonna be hobbyists and enthusiasts

and first time programmers doing stuff for fun.

That's never gonna work for them

because they'll never be able to envision

all the different dependencies

between different computations they're running in parallel.

But it turns out that there was amazing foundational work

done in the 1980s

that was made very real by paper on Haskell concurrency

"Composable Memory Transactions" is the name of the paper.

And it describes the system for

transactional updates to programs.

And the idea of a transaction is

a transaction is a block of code that does a bunch

of operations on memory, might read, might write,

it might process an order, it might accept an order

and/or reject an order.

It might transfer money

between one bank account and another.

It might make conditional decisions like,

oh you asked to transfer $100 from your account

to this guy's account, we're gonna see if you

have $100.

If you don't, we're gonna reject it

and if you have $100,

we're gonna take $100 out of your account

and add it to this other guy's account.

Without transactions, if everybody's just randomly adding

and subtracting each other's bank balances,

then you might have somebody read a bank balance,

subtract a hundred and write it out.

But in the meantime somebody has out written something else

in the meantime.

And so you might get inconsistent bank balances

arising if you don't have a way of ensuring

that these all run in a specific order.

So the idea of transactions is,

it's a way of dividing an entire program into updates,

you know, self-contained updates that do an arbitrary amount

of computation but must run in a single threaded manner.

And in the case of a game engine,

that's a gameplay object update.

When you're playing "Fortnite," you see a gameplay object.

Every other player is a gameplay object.

Every enemy is in a gameplay object.

Every rocket and projectile and car

and thing you see moving around and interacting.

It's not just a fixed static part of the world,

that's a separate game object.

And each of those objects is updated at, you know,

a rate of one update per frame at 60 frames per second.

And so then in the course

of "Fortnite: Battle Royale" gameplay,

you have tens of thousands of object updates

happening every frame with a hundred players.

In a simulation with billions of players,

you'd have a whole lot more than that.

So right now that's done single threaded.

Yeah that's done single threaded in each game session.

This is why "Fortnite" is a hundred players limitation.

If you absolutely maxed out a server,

maybe today you could get up to 140 or something,

but, you know, it's not going to thousands

or millions or billions.

And so what we need is a technique

for magically automatically scaling our code to that.

And transactions are the idea.

And the idea is a transaction is a granule of code

that runs its entirety.

And so the idea of this transactional memory concept

is that we're gonna have programmers

write completely ordinary code,

that reads and writes variables in a completely ordinary way

and they're not gonna have to worry

about concurrency at all.

And then the system, like today a program,

a computer just runs your program.

There's no amount of speculation going on

at the programming language level.

Value of transactions is,

since we have a bunch of operations we need to know,

we apply a large set of them concurrently,

but instead of each one reading and writing

from global memory shared by all,

in which case they might be reading and writing

and contending with each other for the same data

and might be doing contradictory things to it.

We're gonna track all of our rights locally.

We're not gonna write changes out to global memory.

We're gonna keep track of it in a buffer.

It's just for that one transaction.

So it's gonna look to that code exactly

as if it's running on the global system

affecting global game state,

but it's gonna be isolated to just that one transaction

and it's gonna be set aside

and buffered up for consideration later.

We're gonna run tens or hundreds or thousands

of the updates concurrently.

We're gonna see which ones had read-write conflicts

because if two transactions don't read and write

any of the same data, then you could have run them in

either order or simultaneously

and it wouldn't have changed the end result.

- Yeah, the order doesn't matter.

This is so fascinating to imagine this kind of system

arbitrarily concurrent

running millions of updates

in parallel of gameplay objects.

That's the thing that enables the thing

that we're talking about, which is, you know,

tens of millions of people together in one scene.

- Yeah, exactly, and the key is

that you're running these updates speculatively

and you're not committing their changes to memory

until you're sure that they're free of conflict.

So you might update 10,000 objects,

you might find 9,000 of them were conflict free.

So you apply those 9,000 updates to memory

and they could have run in any order

and it wouldn't have changed the result.

- [Lex] That's so cool.

- Now there's a thousand objects left over.

Now you have to run those again.

Try them, maybe interleave in a different way to get them

to eventually commit to memory.

And in the meantime you just throw

all their computations away and redo them later.

And by doing this, like we're moving this

from being a programming problem

for the programmer to deal with,

to being a language problem

for us language designers to deal with.

And we're moving a vast amount of pain

that would be imposed on a million people instead

to a vast amount of pain

imposed on a small number of people

to have to actually make this work.

- That's amazing, that's really incredible.

So what's the state of things with Verse

and I guess what you're outlining is if,

and hopefully it is successful, this would be a big part

of Unreal Engine 6.

So what's the timeline?

Where do we stand today?

- Well there's a lot going on in parallel.

The key thing with Verse

is that we have been specifying like

what we think is the ultimate version of the language

with all the features we want.

Whereas we've been shipping more modest

versions of language over time

and we've released dozens of updates

to it over the past year and a half.

And the idea is that the shipping version gains

more and more features over time,

but each maintaining backwards compatibility

with old versions and each continuing to improve

and approach the ultimate version of it as we go.

And we've been doing this experiment entirely

within the world of Unreal Editor for "Fortnite" for now.

We wanna test this and iterate

with "Fortnite" creators in just the metaverse usage case

before we make it available to all of our partners

using Unreal Engine for all of their projects.

And the idea is to iteratively improve it and build it out.

'Cause right now UEFN has relatively

few features for programming.

It needs a lot more and everything we add makes the world

a much better place for "Fortnite" creators

and we're adding major, major new APIs every few months

throughout the course of this year.

Whereas Unreal Engine licensees

who are building standalone games

already have access to the full engine through C++.

They have massive, massive expectations of an API.

And so we can't release this to them

until we've built up all of the essential features

that they'll need for building

their game play in the future.

And so, you know,

we have these two different tendrils of progress.

There's Unreal Engine 5 for game developers

and there's Unreal Engine 5

targeting the "Fortnite" community.

And there's different bits of development

that are only in one area of it,

there aren't applied to both.

Like not all of the Unreal Engine 5 features

are actually available in "Fortnite"

because some of them we haven't figured out

or haven't gotten to the point where we can deploy them

to all seven platforms in a platform independent way.

And so the place where all of these different

threads of development come together is Unreal Engine 6.

And it's a few years away.

We don't have an exact timeframe

but you know, we could be seeing preview versions of it

perhaps two to three years from now

and we're making continuous progress towards it.

- So that's really nice.

So there's this ultimate version of a language

that you're constantly working on and thinking through.

Then there's the shipped version of the language

that's used by a large number of people

but still in the constrained environment

of the Unreal Editor for "Fortnite."

So for the "Fortnite" game.

And then there awaits the more general

Unreal Editor, Unreal Engine

for the lessons learned in the "Fortnite" context

to be integrated in the more general context

of creating simulated worlds for all kinds of games,

including "Fortnite."

It's a really nice setup

'cause it's a testing ground of the language in "Fortnite"

and you're keeping an eye on

what the ultimate thing will look like also,

necessary to deliver all the features

that we mentioned, brilliant.

- You know the aim for UE 6 is to bring

the best of both worlds together.

A much easier gameplay programming

for the "Fortnite" community and for licensees,

more scalability to large scale simulations of all sorts.

Greater ease of use, meaning it'll be easier

to hire programmers who are familiar with

and experienced with the thing,

but also ensure that every game developer

has the full deployment capabilities

so that it can build a game once

and then ship it anywhere.

Like the Autumn version of this enables a game developer

to build a game of any sort

or simultaneously both ship it into "Fortnite"

as a "Fortnite" island that players can go into,

bring their "Fortnite" items and cosmetics

and interoperate properly

or ship as a standalone game or both.

And if they ship as a standalone game,

they shouldn't be missing out on the, you know,

open economy either

because in this timeframe we'll have opened up

the "Fortnite" item economy

to third party developers of all sort.

Hopefully there is standards body,

but there might be multiple phases of it

so that if you choose to ship a standalone game

you can still choose to, you know,

have "Fortnite" items work in your game

and have your game items work in "Fortnite"

and have your item economy integrated

with the overall metaverse economy

and solve the really core problem of the game industry

that Matthew Ball has been documenting

over the past few years.

- Yeah, by the way, Matthew Ball has been really helpful.

He wrote a really great book

that I recommend people check out.

There's an updated version.

Let me just ask for, 'cause again, there's a bunch

of indie developers listening to this.

I saw that a lot of solo developers out there,

they're using Unreal Engine

that they're basically creating video games solo.

I can highly recommend it's great, "Choo-Choo Charles,"

it's a great video game. (laughs)

Gavin Eisenbeisz, a great guy.

He's solo created this game that's I think quite popular.

I believe he says he used visual,

he didn't even use C++.

He used visual scripting, he used blueprints to create it.

Okay, so I mean all that to say

people should go check it out,

support indie developer, support Gavin,

support everybody like that.

I think it's important to say

'cause there's so much genius and artistry out there

that we wanna support the crazy dreamers out there.

Anyway, all that to say, what are the ways you think Epic

can support indie developers like that?

People like Gavin, like give them superpowers

to create games from which they can make at the very least

enough money that they can keep doing their art.

- Yeah, well that's really about productivity

because to be successful with a game,

you have to have a great game.

If you're building a type of game

that nobody's ever built before, you might be able

to build a smaller, simpler game than if you're competing

in a massive genre that has huge expectations.

But it's all about enabling somebody to do that

in a reasonable amount of time that they can spend

and to be able to finish it and chip it

and maintain it successfully.

The tools are a big part of that.

Having the tools be as productive as possible.

But there are a lot of other facets as well.

Like having a content marketplace is a big thing.

You know, just off the shelf piles of content, some free,

some paid built by other creators

can enable a small indie team to build a big game

and just be able to focus on the unique content of the game.

Being able to write their gameplay

and lay out their environments the way they want,

but not have to build every tree and rock.

Yeah, because somebody's already built one

and there's is probably like, you know, perfectly suitable

for your game.

And over time there'll be more and more.

You know, there's also a lot of indie developers

living as content creators.

They'll be releasing content on Fab marketplace

or the Unity Asset Store and earn living for that.

But specialization of labor

is a really, really valuable thing.

In the early days,

pretty much one person would build one game.

Like that's how a lot of the games were built in the 1980s.

Over time you had a separation

where artists became specialized and then programmers

and then gameplay programmers and engine programmers.

Now you have technical artists

and you have, you know, dozens of different specialties

contributing to a AAA 3D game now.

And the more we can modularize those bits of content

so you could get something off the shelf

rather than having to build it or have to com,

you know, engine synthesize it for you,

the more we can enable creators

to create stuff fast and successfully.

- So we should talk about the fact

that amongst many other things you've been

philosophically and spiritually battling monopolies

in general.

Sort of one of which is sort of the Apple marketplace

that charges 30% from developers.

Can you speak about this idea

that you believe that Apple

and other companies valves should not be charging

that kind of revenue cut?

- Sure, well let's start

from a very basic principle of computing.

The first computer I owned was an Apple II +, you know,

designed by Steve Wozniak and marketed by Apple

and then an IBM PC.

And in those days anybody could write code.

Your computer literally turned on

with a programming language prompt in front of you.

You had to actually do work to not write a program

and to instead run somebody else's program.

That was incredibly empowering.

And anybody could write a program,

anybody could put it on a floppy desk,

anybody could share it with their friends.

Anybody could make copies of that, put it in a store,

they could sell it, they could build a business around it.

And they were completely able to,

without seeking any big tech corporation's permission,

do whoever they want.

Even from IBM, remember IBM

was the dominant computer company on Earth at the time

that they released IBM PC as an open platform.

And you know, so it's really been firmly implanted

in my mind that this was a magical

and wonderful time of unmatched economic progress

# Chapter 15

And in those days anybody could write code.

Your computer literally turned on

with a programming language prompt in front of you.

You had to actually do work to not write a program

and to instead run somebody else's program.

That was incredibly empowering.

And anybody could write a program,

anybody could put it on a floppy desk,

anybody could share it with their friends.

Anybody could make copies of that, put it in a store,

they could sell it, they could build a business around it.

And they were completely able to,

without seeking any big tech corporation's permission,

do whoever they want.

Even from IBM, remember IBM

was the dominant computer company on Earth at the time

that they released IBM PC as an open platform.

And you know, so it's really been firmly implanted

in my mind that this was a magical

and wonderful time of unmatched economic progress

for technology in the entire world.

And you know, over time the big companies have realized

that they could shut down

and just block software makers from releasing software

on their own and block software makers from doing business

with customers directly.

And yeah, I've always viewed this practice

as terribly abusive

because when you buy a computer or a phone,

you spend good money on it,

it's your money you spend on that phone

and now you own that phone.

And there's absolutely no reason that Apple should block you

from installing apps

from other developers directly if you want,

going to their webpage or writing your own apps

without their permission and running them yourself

without having to get a developer account,

without having to go through their bureaucracy.

And there's no reason that any consumer

who gets an app shouldn't be able to do business directly

with the developer of the consumer.

You already bought that phone.

Why should Apple be adding a 30% junk fee

to all commerce you do.

And why do they selectively apply it

to some things and not others?

I've always viewed this as deeply abusive

and that it shuts down the competitive engine

that once fueled the app and software economy.

It's still a vibrant competitive engine on Windows

and on the internet, but it's no longer with mobile apps

because these stores have popped up

and they don't provide any useful value to the user.

Yes, they're a search function to find software,

but there's no reason other companies

couldn't build a better one.

And I bet if you had Steam

or if you had Valve build Steam for iPhone,

I bet Steam for iPhone would be a much better app store

than the iOS App Store.

And a lot of people would use it.

And that Apple would be forced

to build a better app store in competition

and everybody would improve their products as a result.

But you know, Apple and Google shutting down

the competitive engine that drives the software economy

has massive implications for everything.

And you know, one of them is reshaping

the nature of mobile apps to be really offensive

to gamer sensibilities.

You know, if you go on console,

the best console games you see listed in the store,

on the storefronts, the best console games

that you see reviewed are awesome games

that really have a lot of creative merit.

The ones that sell the best are really enormous values

for their money

or their product of an immense amount of work.

You don't see that on iPhone.

The top apps on iPhone or the top games on iPhone

at almost all times are these ridiculously greedy,

high monetizing, you know, whale games,

which are pervaded with pay to win and loot box practices,

you know, they have a sort of a legalized a form of gambling

and you know, these games are not driven by fun,

they're driven by manipulation

of the players to greedy ends.

And you know, it's very hard for the fun-based games

to actually succeed there.

And you know, the cost of operating these online games

now are enormously high.

So you have a game that's based on fun,

it's not loot box heavy, you know, you have to pay 30%

of your revenue to Apple

in order to just get access to the platform.

And 30% is way, way, way more than most gaming companies

make in profits right now.

And so if the that fee is more than the profit

from a natural company,

then they can only stay in business by raising prices.

So these 30% fees are raising prices of all digital goods.

It's just inflationary as a force in the economy.

That's just the first drag text.

But then to reach users, when a user searches for like,

before Apple blocked "Fortnite" on iOS,

when a user searched for "Fortnite,"

the first result was always some competing game.

Like it's utterly anti-user.

Like you search for Steam for a game

and if that game's on Steam, it's the first result always.

'Cause Steam's not getting in inshitified

with advertising, Apple is.

And you know, they do that

so they can make even more than 30%.

So if you wanna be the first search result

for your game, you're probably paying more like 45%.

If you wanna reach users on social media,

you're paying another 20%.

So literally something like 70% of the revenue

for your game is just going into junk fees

to acquire users and get them in your game.

And the money that's left over is only enough to fund these,

you know, games with rather abusive practices

that do not look to normal gamers like games

for the most part.

Now there are some exceptions.

There are some great games on iOS

and there's some games with good practices,

but you know, the engine has been really corrupted in a way

that competition would fix.

If you unleashed lots of competing stores on iOS,

then you'd have lots of awesome options

and you'd have much better deals and much better prices.

- I had a quick chat with Matthew.

He asked me to ask you this question of

why don't more companies fight Apple in the way openly

and totally as Epic has been.

What makes you, what makes Epic

so unique in this regard?

And I should say, I think everything you said

I agree with fully.

I think what Apple is doing is just wrong.

I think Apple in many dimensions is an incredible company.

They have brought so much good for the world.

In this regard,

I just think it's straight up wrong what they're doing.

That they're not providing the value of 30%.

And even if they were the monopolization,

the centralized control without competition is wrong.

Anyway, why are you fearlessly fighting Apple on this?

And other companies don't seem to wanna step up?

- All companies are terrified of Apple

because Apple can destroy their business.

Epic was in a unique position with "Fortnite,"

first of all having the, you know,

the biggest game in the world at the time

we started the fight with Apple.

And second of all, having a majority of our users

playing on PC and console

meant that if we lost access to iOS during a fight,

then we would still be able to survive.

That a bigger part,

Spotify, Facebook, you name the top 10 mobile apps,

I think none of them would be able to survive without Apple.

Like literally their business would be destroyed

if Apple blocked access to them.

And Apple is incredibly clear with developers

that they're willing to deprive all users of access

to any app if they get in a fight.

And they've, you know, if you look at how they dealt

with Epic, they were not just legally maneuvering

with the intent of winning the court case against us,

they were also sending a message

to all developers in the world.

We will destroy your business

or we will try our best if you fight us.

And a very small number of vocal developers

have been willing to speak up

and Apple was actually refrained from crushing

their businesses when they weren't violating

any Apple policies.

And that took a bit of discipline,

which I think is also amount of calculation by Apple

that they couldn't survive being seen as the company killer,

that if you criticize us will crush your company.

But you know, the other thing that Apple has,

that they can and will readily deploy

against every developer is soft power.

When they take 30% and advertising is so expensive,

soft power by Apple, like approving your updates faster

or slowing down all of your updates

by a couple weeks can also have a dramatic effect

on your ability to compete successfully.

And Apple, it's a very long history of playing

cat and mouse games with developers.

It's like a developer isn't in Apple's good graces,

so just slow down the updates.

So they've been slowing down updates

for several major tech companies, sometimes for weeks,

sometimes for months without all going under the radar

because everybody's afraid to challenge them publicly.

And so Apple's wielding a soft power can change

a company's economics for the worse,

enough to deter almost any public company.

And you know, Epic is in the fight

because I firmly believe

that something like the metaverse will only arise,

it's something like a billion plus user, you know,

real-time 3D social ecosystem that grows to encompass

potentially all or most major games

by all major developers tied together into an open economy

where they all participate as peers

and they all compete to give users the best deals

and they grow and, you know, do business

with their customers directly.

That thing can only exist if the Apple

and Google gatekeeping monopolies are lifted.

And it's not just the 30% fees.

30% fees are economically ruin us,

but they impose other levels of control.

Apple prevents all web browsers on iOS from implementing

web standards better than Apple does.

So Apple has really limited data storage capabilities

and 3D graphics capabilities on, you know, the iOS web APIs.

So APIs you can access from web apps

running within a web browser.

And you know, that's to eventually cripple those apps

to ensure that they can't possibly compete with native apps.

And by depriving web apps of those features,

they prevent web apps from competing with native apps.

Well, you know, Apple,

if they treat the Metaverse the way they treat the web,

they'll say you can only use Apple's metaverse engine.

Unreal Engine is disallowed.

And then they can impose all of their own limitations

on the metaverse to force all commerce through Apple

or force it to be so uncompetitive

and lousy that it can't compete.

And you know, they have this giant array

of these anti-competitive techniques that they use

to disadvantage other app developers, you know,

saying only Apple can build certain kinds of apps

or only Apple can integrate certain features.

In Europe, even where the DMA law requires Apple

to allow competing stores,

they say a store can only be a store.

You can't build a store into Facebook,

you can't build a social network into a store.

A store must only be a store

because a store that's more than a store might be able

to compete with us more effectively.

It's just a giant, you know, to use the Soviet term,

it's a defense in depth strategy

where they've constructed a massive series of barriers,

each are fatal to any attempt to compete

so that even if one barrier is overcome,

the others remain in place and shut down the whole scheme.

And that's playing out in Europe where Apple has enabled us

to launch the Epic Game Store, but has made it so difficult

and uncompetitive both for Epic

and for clients who we want to do business with that,

you know, it has no chance of success

until the European Union

and starts to really enforce the DMA law and impose harsh

and serious penalties on Apple to force compliance.

- I think it should be said, once again, I think it's wrong

what they're doing there and I hope there's public pressure

and government pressure for them to open up the platform.

And I believe as a person

who loves Apple, I believe this is also good for Apple.

There's the natural thing in companies to want to close

and control and crush competition.

But like Apple is full of brilliant engineers,

open it up and win, it's going to create the right

kind of competitive incentive to make the Apple Store better

to make, you know,

'cause they're great at creating great interfaces,

but competition will sharpen the sword.

I mean, it's just gonna make everything much better.

So I do hope there's a lot of public pressure

and I deeply appreciate

that you're speaking out in this way, sort of putting

that pressure and letting people know

like it's okay to say that this is wrong.

- Thanks, competition makes everybody better.

You have a monopoly that's forced to compete,

suddenly the monopolies products get much better,

the offerings to consumers get much better.

You see so many areas where Apple could be the best,

but what they have is just really, really lousy.

And it's this old guard of leadership who is clinging

to these old policies, turning themselves into the enemy

of every developer, every regulator.

And I think it's ultimately massively to their detriment.

And I can't wait for a new generation to come in

and, you know, paint a bright path to the future.

Epic was an awesome partner to Apple

for more than a decade of demos and partnership

and technology usage together.

And we did amazing things together.

Love nothing more than to have that Apple, you know,

bringing back Steve Wozniak's original views.

Just the Apple II was such an amazing thing.

It's a completely open platform.

The manual to the Apple II included a listing

for all the ROMs, the source code to the ROMs,

so you could understand exactly what was happening there

and you could learn from it.

It included a hardware schematic of the entire computer

so you could learn how to make a peripheral and plug it in

and an open ecosystem.

And that's the awesome Apple,

that company would be the best company in the world.

Again, I think the current one is just

on the wrong side of history and needs to change.

- Well I hope Epic and Apple find a path forward together

and flourishing together

and Apple embraces competition better.

One of the things I admire about this conversation

that you mentioned Steam a bunch, with kind words,

supportive and basically never mentioned Epic Game Store.

I love that.

So I really love that.

It really embodies the fact that you want variety,

you want freedom for people to choose the best thing

and in so doing, create this large network

of humans interacting freely with each other.

Okay, that said, one of the competitive pressures

that Epic has created a few years ago

was by launching the Epic Game Store.

And instead of Steam's 30% revenue cut,

you went with 12% revenue cut

creating the competitive pressure saying, you know,

"Listen, this shouldn't be that high of a cut."

Which I thought was like amazing.

This is a brilliant idea

and I think it still is a brilliant idea, it's wonderful.

Now in preparing for this conversation,

I looked on the internet and I saw

there's a lot of criticism of EGS at Big Game Store.

First of all, I should say the internet, (laughs)

it's full of drama and criticism.

Like there's not enough celebrating of awesome shit,

that let's get...

If I can ask the internet as a blob one request,

can we just celebrate awesome and also criticize.

But just like there's not enough celebration.

Anyway, the two directions of criticism

is just straight up the Launcher interface is clunky

and lacks a lot of the features of Steam.

And then the second set of criticism

is the exclusive contracts

which were made with some of the games

that are on Epic Game Store.

So first huge props on the 12%.

# Chapter 16

This is a brilliant idea

and I think it still is a brilliant idea, it's wonderful.

Now in preparing for this conversation,

I looked on the internet and I saw

there's a lot of criticism of EGS at Big Game Store.

First of all, I should say the internet, (laughs)

it's full of drama and criticism.

Like there's not enough celebrating of awesome shit,

that let's get...

If I can ask the internet as a blob one request,

can we just celebrate awesome and also criticize.

But just like there's not enough celebration.

Anyway, the two directions of criticism

is just straight up the Launcher interface is clunky

and lacks a lot of the features of Steam.

And then the second set of criticism

is the exclusive contracts

which were made with some of the games

that are on Epic Game Store.

So first huge props on the 12%.

Maybe you could speak to the vision of that.

And second, can you comment on those two criticisms?

- Sure, yeah, I think, one of the reasons that people

characterize the Epic Games launcher is clunky

is because like the Epic Games launcher is clunky

and we need to improve this. (laughs)

You know, there's a lot of work going on there

and you know, I wish we'd gotten better

at addressing quality of life features

and prioritize them above all of the other features.

You know, because Steam has 15 years of built up work

by many of the best programmers in the whole industry

working on that.

A much larger team working on Steam

and a lot more time working on it.

And so we've had to make a lot of prioritization decisions

about what do we support with the Epic Game Store and when.

A lot of the time it's been supporting commercial features

like merchandising, offering multiple versions of a game

for sale and offering upgrades from the regular edition

to the deluxe edition and other things that partners work.

And you know, other priorities have been quality of life

and launcher load times and other things.

And we've not put enough emphasis

on the quality of life features.

We've recognized this very clearly multiple times

and we've gone through multiple refactorings.

But you know, that's definitely been a disappointment to us

and to a lot of users.

And I think one thing it took us a while to realize

was it's not in uniform.

Depending on your proximity to a CDN

and the size of your game collection,

it can be either awesome or really clunky.

And the users for whom it's really clunky

are the people like I think

are a large part of the complaints.

- They're gonna speak up.

And I should also say that the Steam launcher

for a long time, from my memory,

but also just looking online was also very clunky

in the beginning.

- Yeah and you know, one of the criticisms of Epic Game

Store from the beginning was you don't have

all of the features of Steam,

but we very much don't want

to have all of the features of Steam.

Like Steam has forums to get to your game

and like we decide we don't wanna create forums

and our partners when we talk to them,

generally didn't want us to create Epic Game Store forums

for their games

because there's already, you know,

channels that they prefer to them.

There's social media and a number of platforms

and there's Reddit and there's lots of places for gamers

to discuss their game

and they preferred those discussions to be there.

And so it's very much not our goal to mimic everything

of Steam, but we do wanna have

all of the convenience features that makes it as easy

and fun to use as Steam.

So there's a long journey ahead,

but you know, we continue to reinvest in

and you know, we're working

to build a multi-billion dollar business there

and think we'll succeed.

Already at the Epic Game Store,

yeah, supports an immense amount of Epic games commerce

in "Fortnite," on PC, now on Android and iOS

and the European Union too.

So it's a forever facet of the industry

and we are never losing heart in it.

And we think at some point, you know,

I really feel that the benefits of the Epic Games approach

are gonna outweigh the benefits of this Steam approach,

especially as gaming becomes multi-platform.

One of the things that really sucks for all gamers is that,

you know, you have a lot of friends in the real world,

everyone has different platforms.

Your Steam friends aren't connected to your Xbox friends

and they're not connected to your PlayStation friends,

or your Nintendo friends.

And so you're very much bottling up PC gaming

into a kind of a hard core group of PC only folks

and making all of the other aspects of it difficult.

You know, a lot of games have flocked towards Discord,

which is a mess in itself.

Can now your Steam name is not your Discord name

and that's not your PlayStation name.

And so now you have two people in a game

and they have four different identities and that sucks.

You know, our aim for that is, you know,

with Epic Online Services and the social systems

that we built for "Fortnite" opened up

to all developers to have cross kept platform social

features be super easy and free for all developers.

This is not something we're trying to gatekeep

or rent seek on or lock people into.

It's just a way that we're making social gaming easier

for everybody.

As more and more games follow the "Fortnite" approach

of being multi-platform, especially multi-player games.

You know, Metcalfe's law is a very real phenomena

in the industry.

It's the thing that's upending some games

and causing growth in other games.

It is the number one trend

for pervading the world of gaming today.

And it says that, you know, your game is

quadratic more valuable the more percentage

of a user's real world friends they can connect to.

Your game vastly benefits by connecting

all of its players together and not, you know,

segregating them off into different online platform

populations and so on.

And so, you know, I think the future trend

is in that direction.

I wish Velvet opened up Steam Works

to just work on all platforms.

They could have easily done it, we did it,

but you know, they seem to be using it as a lever

to keep people locked into the Steam PC game store.

And you know, that's gonna be a long long running battle

because there's always a very toxic group of Steam users

who, like, they even created an entire subreddit dedicated

to criticizing Epic on our store.

And they create, you know, basically harassment campaigns

at times against developers who use Epic Online Services.

You know, developers do that

so they can connect their players across platforms

and have friends across platform

and voices across platforms.

But, you know, suddenly that's trying

to be turned into a negative.

- It's clear that Epic wants developers to win,

wants gamers to win

and wants Steam to do awesome also.

And in the competition between Steam and Epic Game Store,

like create awesome stuff together.

I mean there's just, it's obvious to me

if you don't read this stuff online,

but online it's like there is this just negativity

that I don't think is constructive in general.

I give a big sort of positive

thank you and props for the push to multi-platform

that was always there with for "Fortnite."

Perhaps before the pressure

that Epic created on breaking the barriers of Xbox

and PlayStation and PC and be being multi-platform.

Like I got a chance to play with "Fortnite" a little bit

with you and all the people in the group...

By the way awesome interface audio chat, really fun.

But you could see like a couple of PC folks,

a PlayStation person, Xbox person all together.

You can't really tell what they're using

except for a little icon.

And it's nice, it's like all these barriers

that we've created with these platforms are gone

and you creating the pressure with Epic Game Store

and just everything you're doing with "Fortnite" platform,

it's really nice.

There's no reason to create these silos

'cause ultimately you should put the gamer first

and let everybody interact

with actual real life friends

and make new friends across the entire network of humans.

So anyway, thank you for that.

Thank you for creating that pressure.

- Thanks, yeah, that was an interesting time.

Sony had a long running policy

preventing cross-platform play

and we had a long series of conversations

which got pretty harsh towards the end,

but Sony ultimately came around

and they opened up PlayStation

and you know, through a series of private conversations

they did the right thing.

And not only that, our partnership with Sony has increased,

you know, since that argument back in 2018.

And we've gotten closer and closer

and done ever more things with, you know, Sony, you know,

brand IP like the characters from "God of War"

and other games coming into "Fortnite"

and you know, all kinds of crossovers.

Massive Unreal Engine adoption

and Sony for making games,

for making movies at Sony Pictures,

music partnerships with Sony Music.

That's been an absolutely wonderful relationship.

And I think, you know, that stands as an awesome example

of a company that, you know,

because of historic reasons got, you know,

stuck with a policy that no longer made sense for the future

and you know, following a serious discussion

with a close partner, righted it and did an awesome thing

and now Sony's much better off and Epic's better off

and all game developers are better off

and the whole console industry

I think it's a lot stronger now than it would've been if,

you know, these silos had continue to be playing out.

And despite the kind of potential concern

that like maybe blocking platform play

with Xbox gave Sony advantage, you know.

Sony's actually grown in market share

relative to Xbox since that time.

And so you can't say that anything

but goodness came of that time.

And I think a better version of Apple would've received

the email I sent to Senior Apple Management

and been like, "Huh, there's an issue here.

We should have a discussion,

we should reconsider this, we should listen."

And you know, they didn't and that's why we're in the midst

of a five-year battle with Apple

and in, you know, hopefully they're,

still the early days of a 15 plus year partnership

with Sony.

- Come on Apple, we love you Apple,

do a little bit better.

The second line of criticism that I mentioned,

the exclusive contracts with some of the games.

Can you just speak to that

because in so much of the journey of Epic

you've been sort of against exclusivity.

- Let's back up and talk about the principles at work here.

Apple forcing other companies

to use their payment service is a cursive decision by Apple.

- But if Apple convinced other developers

to use their payment service by offering benefits

or a better deal or funding

or any other positive incentive,

then that would be perfectly fine.

One is preventing competition

and the other is actual competition.

Epic has never forced any developer

into any sort of exclusivity relationship.

Rather we've offered developers payment or incentives

or marketing or any number of things of value to them

in exchange for coming to our store exclusively.

And it's their game.

So it's entirely rightfully up to them

to decide how to distribute it

and to make the decisions about their business.

It's their game.

If they wanna distribute it through Steam, they can.

If they wanna distribute it

through Epic exclusively, they can.

If they wanna distribute it through both,

then they could do that as well.

And if we pay them money

or other things of value in exchange

for them coming exclusively to the Epic Game Store,

I think that's their right.

And this is an example of Epic, an underdog

with a tiny fraction of Steam's market share,

working to proactively compete with Steam

by offering a better supply of games.

And some consumers who prefer Steam might prefer

that the game be on Steam,

but the developer in each case has decided

that they believe they would benefit more

by doing this exclusive deal in exchange for benefits

than by being on Steam.

And you know, like one of the key exhibits

in the Epic-Google trial was it's opening exhibit,

which was trying to point out to the jury in the trial

the benefits of exclusives.

Like imagine a new store popping up.

The store has a big sign outside of it,

"We're the new store store, we have everything

that the other store has and it's at the same price."

Are you gonna go to the new store? No.

You know, nobody's gonna switch from Steam

if Steam has all of the same games as the competing store

and everything's priced just the same.

And so we looked at initially two ways

of competing with Steam strongly.

We wanted to sell BET games at a better price than Steam

by agreeing on the amount of money

we pay each game developer, you know,

if the game's gonna sell for $50 and we take 12%,

we'd actually lower the price

and potentially even lose some money to offer a better deal.

Well, you know, we tried to pursue this,

but very quickly every developer told us

that they wouldn't agree to better pricing

because if they did then Steam would stop giving them,

you know, marketing featuring and benefits

and the console makers would be mad

and all their relationships would be harmed,

you know, so there's an undercurrent of powerful platforms

and ecosystems encouraging developers

not to compete on price.

So not being able to compete on price,

we decided to compete on supply by doing exclusive deals

and we signed a lot of them,

paid developers lots and lots of money.

I think we distributed over a billion dollars

in net expenditures to developers beyond

the revenue we actually made from games

in order to get a whole lot of exclusive games.

Some are successful, some weren't.

"Borderlands" did awesomely on the Epic Games tour

and Gearbox felt that it did just as well through Epic

as it would've done on Steam

because you know, the players who wanted "Borderlands"

wanted "Borderlands" and they came and got it.

Whereas a lot of other games, you know,

some smaller games especially

that didn't have a dedicated audience

that was absolutely gonna play the game

typically benefited from exposure on Steam.

They were reaching an audience

that wouldn't have reached organically.

And so some of them in the end we

and they concluded that they did worse

by being on the Epic Game Store exclusively

in terms of, you know, reaching fewer customers.

And so, you know,

we had these limited time exclusives,

when they ran out, they put their games on Steam

and you know, lots of data was gathered

to understand what worked.

And so this worked well for some games,

didn't work for other games.

But you know, companies

seeking to compete,

especially underdogs seeking to compete,

have to offer some unique value, have to offer something

that's not available through their competitors.

And I get that Steam users who just prefer using Steam

and buying games on Steam and wanna have their library

in one place don't like this.

But you're never gonna have competition

for better deals if you don't support

the competitive mechanisms

that allow competitors to come about.

And I think if Valve were forced

through Epic Game Store's success to compete

with Epic Game Store, then developers would be getting

a better deal, consumers would be getting a better deal

and these 30% fees would be driven down

quite a lot towards the actual costs

that are required to support the stores.

- Yeah, I mean there's a lot to be said there.

You know, I've gotten to watch Spotify

try to do this with podcasts, you know,

enter as the underdog into the space

and try to attract, you know, they made exclusive deals

with, for example, for Joe Rogan

where the podcast would only be published on Spotify.

I personally think long term what I would love to see

for EGS for Epic Game Store is to not do any exclusivity.

Similar to what Spotify's doing now.

Even with Joe Rogan, they let go, it's wide open.

And instead compete on the space of just

# Chapter 17

that allow competitors to come about.

And I think if Valve were forced

through Epic Game Store's success to compete

with Epic Game Store, then developers would be getting

a better deal, consumers would be getting a better deal

and these 30% fees would be driven down

quite a lot towards the actual costs

that are required to support the stores.

- Yeah, I mean there's a lot to be said there.

You know, I've gotten to watch Spotify

try to do this with podcasts, you know,

enter as the underdog into the space

and try to attract, you know, they made exclusive deals

with, for example, for Joe Rogan

where the podcast would only be published on Spotify.

I personally think long term what I would love to see

for EGS for Epic Game Store is to not do any exclusivity.

Similar to what Spotify's doing now.

Even with Joe Rogan, they let go, it's wide open.

And instead compete on the space of just

the non-clunkiness of the interface

because the foundation of what

Epic games still represent with 12%,

it's just philosophically.

So you're also competing on the sort of spiritual realm

of like what it stands for, ethically.

That's also a really powerful way to win.

So now that there's enough number of people

using at the Epic Game Store, like to drift away,

to move away from exclusivity.

It's understandable that it's needed for the competition

for the underdog to enter the scene.

But it goes against the sort of the freedom,

the free spirit of choice that I think you represent

in a lot of the decisions you've made,

which is making the games cross platform.

And just yes, giving freedom to the developers,

giving freedom to the gamers to choose.

So in that way I think exclusivity a little bit

goes against that.

- Well here's the conundrum, the exercise of soft power

by all of the competing stores

has made it intractable for almost any developer

to offer a better price

through the Epic Game Store than through Steam.

You can imagine that if the effective Epic revenue

sharing 12% to developers was

that games just cost 22% less on Epic Games,

sorry 18% less on Epic Game Store.

That would actually start

to reshape consumer behavior significantly.

People would start coming here for the better deals.

But I feel like Steam, you know,

giving developers nasty phone calls

and so on, when they propose to do that

prevents developers from passing on savings to consumer,

then what's the mechanism that drives users away

from the incumbent store to the store

that offers a better deal.

If basically developers are fearful of competing on price

through stores, you know,

what can possibly be done to get a dominant store with,

you know, something like 90% of revenue share from,

you know, multi publisher stores,

you know, in line so that a much,

much smaller store can compete.

I think some answers required there.

A better UI is great.

Like Steam is super polished.

Epic Game Store and you know,

time will hopefully be as polished.

You know, how does that overcome the fact

that your entire library over the past 15 years is there.

If developers have been afraid

to exercise their own economic interest

because there's own developer's interest to sell on Epic

and you know, 18% more of the revenue.

You know, I think there's a real power to incumbents.

It's very hard to overcome through just being there

and being as good.

- Ultimately, where I hope it converges to

is less exclusivity.

And where the competition can be the kind I love the most,

which is on the UI,

on the experience, on the just...

And then on the Steam side, on the 12%.

So it can go from 30%

and start to support the developer

by lowering it from 30% closer to 12%.

So anyway, I'm a big supporter

and I don't like the criticism of Epic Game Store,

but I also have to say that I don't love the exclusivity

but I understand.

I understand the reality of the world is

that you have to have some mechanism to get people

to switch or not to switch

but to at least get some of their games to try out,

to experience, to allocate some of their library

to the underdog.

So I totally understand.

And hope the UI keeps improving.

(Tim laughing)

- Thanks, one more bit on that exclusivity point

is that when we told Google that we were going

to launch "Fortnite" outside of Google Play

and go into competition with them, they viewed exclusivity

as such a powerful competitive force

that they went around to the top 30 publishers

and paid out hundreds of millions of dollars to them

in order to agree not to do exclusive deals

with competitors.

And that was called Project HUG, H-U-G

Hold developers Close.

And that was one of the major pieces of evidence

on which the jury found their practices

to be illegal and anti-competitive.

And the one more data point on that,

you know, we talk about 30%

and there's always a lot of people defending Steam.

Well of course they have more costs

because they have more features than Epic.

We have data on that's very detailed.

The all in cost of operating the Google Play store,

stocking it, maintaining it, the software,

the entire ecosystem is around 6% of revenue.

So you know, in a competitive market,

what a company whose cost is 6%,

people to charge 30%, like absolutely not.

And Apple's costs are similar.

Apple runs an even more efficient

and lean operation than Google.

So their costs are also likely in the range of 6% all in.

They mark it up from 6% to 30%.

Like only a monopoly can do that.

Look at competitive businesses,

they have a margin of a few percentage.

The numbers there are strikingly supportive

of just outright anti-competitive distortions.

- Okay, what do you think

is the future of the gaming industry?

So we've said to me a bunch of exciting stuff

about indie developers so, you know,

do what are called AAA video game companies,

so these big gaming companies, do they have a future?

What is their role?

How do you see like in the next 5, 10, 20 years

the evolution of these big companies and indie developers?

- Yeah, there's one constant in gaming

that I think the industry manages to lose sight of

from time to time astonishingly and that's fun

and people play games for fun.

Our whole job is to deliver fun.

And when you look at a lot of the games

that failed recently, they just didn't deliver fun

or they didn't deliver fun in a manner

that was nearly competitive

with the other sources of fun just in people's lives.

And so, you know,

at a basic level we don't need a terribly complicated theory

to explain a lot of the malas in the game industry.

There's just been a degradation of the capabilities

of a lot of publishers,

partly because of competition for talent.

You know, companies like really vibrant game businesses

like Epic or Riot or others are hiring the best developers

and accumulating them and big tech companies are hiring

the best game developers 'cause there's super talent there.

And so in some cases the companies aren't competing

robustly or getting worse.

They're making games that are less fun.

And you know, I think everything else

that's happened is kind of a side show to that.

You know, there's always political drama and so,

and I think the core is of failure to deliver fun.

And you know, the nature of fun is changing.

It turns out that playing a game together

with your friends in a really socially

and engaging way with voice chat is just way more fun

than playing a solitary game for the most part.

And there are exceptions to that,

but I think we're seeing much, much play time

shifting towards games you're playing

together with your friends.

And not just random internet strangers who happen to play

that game too, but the people actually

you know in the real world.

And that's certainly been the case with me

and with almost everybody I know who's playing

"Fortnite" or similar games.

And that has really significant effect in reshaping

the whole game business.

Because like a single player game,

if you have 20 people with 20 different opinions

of which game to play, each one might buy

a different single player game.

But in a multiplayer game, if there are 20 games out

and each one might have their own completely individual

preference and each one or independently choosing

which game to play, each one might buy a different game.

But they're all realizing that they wanna play together.

And so what players are doing increasingly is playing

a game they like and accept together with their friends,

even if it's not the game that every one of them

might be preferring to play themselves.

Like if you have, and you know,

that's certainly the case in, you know,

different "Fortnite" groups I play with from time to time.

It's like, you know, one player might have been preferring

to play "COD", one might have been

preferring "League of Legends,"

somebody else, something completely random,

but it's just so fun to play together, we're doing that.

And that means that there's really strong

Metcalfe's law effect in games

which are able to attract a large percentage

of your friends are more able to attract you

and not only attract, but also retain.

And so, you know, I think Matthew Ball's analysis

of this over the years has really documented

the trend towards, you know, you can call it the metaverse

or you can call it large scale multiplayer social gaming.

He is really documented this trend

and you know, over the past year or so it's taken a really,

really strong turn towards increasing rate of change,

increasing numbers of players coming to "Fortnite."

You know, we hit an all time high

of 110 million monthly active users about a year ago.

(Lex laughing)

- That's crazy. - And another

like close to peak this time.

"Roblox" is bigger than ever.

And you know, this trend is players consolidating

into multi-player experiences of play together.

And we're seeing another trend overlaid with that,

which is like when an awesome single player game comes out

or a small multi-player game comes out,

people often will like treat it as a vacation.

They'll go off and play that game for a while,

then come back.

And I think "Wukong" was an awesome example of

that wonderful game from a brilliant team.

In China they made a game that's like,

no western players had really seen

that type of thing done before.

And it was awesome and it did well,

but most players play it for a while and move back on.

And that could be lucrative.

But a business that's building that kind of game,

it's gonna have to build a new one every few years

and build a business around that while the other games

continue to accrete users.

But you know, when you have a large number of gamers

migrating to a small number of games,

the effect of that is increasing revenue for those games,

increasing reinvestment.

And you know, there are things that Epic can do

with a team of thousands of people building "Fortnite."

Internally and tens of thousands contributing to "Fortnite"

as independent creators.

You know, there are just things that can happen

with that level of investment

that can't happen in a smaller game.

And so there's somewhat of an increasing

winner take all dynamic

where the biggest games reinvest more

to make their games more fun,

to gain fun at a faster rate than other games.

And you know, the industry is changing around that.

And you know, so I think the lesson for the game industry

now is that there are really two big opportunities

being pursued.

There's big games or games that have the potential

to be really big multiplayer experiences

that keep players around, you know, indefinitely

for very long periods of time.

And then there are just really good single player

and small scale games

that people are taking a break from their big games for.

And you know, the trend there is going

to be towards efficiently developing those games.

You can't build one of those games

with a $300 million budget,

but if you can do it with a $40 million budget,

you can make a lot of money.

So I think that's the main reshaping going on

and I think that it creates a rather bleak outlook

for a lot of the category of like single player games

that don't have a huge audience to reach.

But this is just one of the really trends

of restructuring the business around

the technology and changes of the day.

- Okay, this is gonna be a ridiculous question,

but aside from the games you've created,

what are some of the greatest video games

ever created to you?

Like what video games have been like

either impactful to you in your life

or maybe you've seen created

and you're like, "Huh, that's a beautiful art piece."

Like it could be in a totally different realm.

Like obviously for me, I returned too often

to the single player domain of role playing games.

Of the "Elder Scroll" series, "Skyrim",

that was like a world that they created.

A recent game, "Baldurs Gate 3",

that was really incredible piece of work and art

and doing a lot of innovative stuff

again in the single player domain.

Is there games like that outside the ones you've created?

- I'm most impressed with the games that have created

what appears to be a full living, breathing world.

You know, games that give you the sense that

you're just a part of it and there's a lot more happening

and there's, you know, always more.

And you know, gives you the sense that you could go anywhere

and do anything.

Even though these games really do have finite limitations

and there are places you can't go.

It really creating that sense of wonder

is just a magical thing.

Like "Zelda: Breath of the Wild,"

yeah "Skyrim," "Red Dead Redemption"

- [Lex] "Red Dead" is great, yeah.

- It's like there's an entire ecology simulator in there.

I have a high school classmate

that got into studying river ecology

and he was commenting on like

"This is one of the very few games

that's hydrologically sound."

The way, like they actually went to the effort

of shaping the rivers

to follow like erosion dynamics and so on.

It is the attention to detail.

There's something there, it's big,

and it's been funny through the industry.

Like I last designed a game in 1992,

I'm not a game designer.

Yeah, I have a very open-minded

like the best game genre that will ever exist

has not yet been invented.

And as we get more technological capabilities

and creatives, people use that to,

and you know, hopefully empowered

by higher productivity tools and so on that will see more

and more cool things emerge

that we'd never dreamed possible.

And you know, the idea of a world simulator

is actually really interesting there.

It's been tried a lot.

It's, you know, usually extremely slow

and expensive to create,

but over time maybe we'll get better at that

and that will be a thing too.

- You said so many interesting things there.

New city builders. - [Tim] Yeah.

"Civilization," it's a mind boggling

they built a game with that depth that can evolve

so dependent on your actions.

- To do that scale of world,

but to where you can step into it

and be in it, you know.

I think "Red Dead" is a great example,

but to do "Red Dead" redemption in a way

where you can walk around with friends at a large scale.

And I guess what you have given

so many years to is creating the tools

that enable the artists to give that attention to detail

# Chapter 18

is actually really interesting there.

It's been tried a lot.

It's, you know, usually extremely slow

and expensive to create,

but over time maybe we'll get better at that

and that will be a thing too.

- You said so many interesting things there.

New city builders. - [Tim] Yeah.

"Civilization," it's a mind boggling

they built a game with that depth that can evolve

so dependent on your actions.

- To do that scale of world,

but to where you can step into it

and be in it, you know.

I think "Red Dead" is a great example,

but to do "Red Dead" redemption in a way

where you can walk around with friends at a large scale.

And I guess what you have given

so many years to is creating the tools

that enable the artists to give that attention to detail

that "Red Dead" does on several of the things.

And once you do, there's something magical about that.

Like once you give that attention to detail,

like, I don't know what it is,

but the love of the artist comes through somehow

and you could feel the care that they put into it.

- That's right, the best games of a soul.

You can really sense it.

You know, like "Call of Duty" has a very different soul

than "Fortnite" and it just kind of exudes not only

in what you see in the game,

but also in how players interact with it

and interact with each other online.

And that's a really fascinating thing

I wish would be studied more.

(Lex laughing)

- I think we talked about the soul on several fronts, right?

I wish it would be studied more.

- Yeah, yeah, all game design decisions

the designers make have a profound impact on what players

think of the game and seeing the game.

You know, "Fortnite: Battle Royale"

always had a sense of mystery to it.

You're on this island but you're not sure

exactly what's happening here.

There are all these houses, they're abandoned, why?

And you know, I'm not the secret holder,

you know, I'm not on the design team.

I experienced "Fortnite" as a player,

but it really exudes a lot of that

and a good spiritedness as well

'cause even when you're eliminated in "Fortnite," you know,

there's not like blood spurts and there's not jibs.

You're just, you know, teleported out of the simulation

and often, you know, you end up losing the game in a way

that's hilarious enough to like,

actually you're laughing at it

or you're like, respect to that player

who just won because that was clever.

And you know, it creates a very different dynamic

than these other games where players

tend to be very, very positive towards each other.

One of the things I like to do in "Fortnite,"

just to kind of gauge how the game is going

is I play full squads

so you get match made with the, you know,

three other random players and play a game together.

Sometimes they have voice chat, sometimes they don't.

And you know, back when our matchmaking regions were bigger,

I learned a little bit of like battlefield Spanish

so I could speak with the people who were down.

- [Lex] Battlefield Spanish - As far south as, yeah.

Mexico City, and you know, the positivity

of the interactions there among just every kind of person

you might ever meet online were really quite impressive

and completely unlike what you would see in a game

like "Call of Duty",

where it's always, you know,

everybody's gotta be an Edge Lord.

(Lex laughing)

- Ah, I love online gaming culture.

I have to ask it 'cause it's kind of like one of

the legendary games is "Grand Theft Auto,"

speaking of the worlds that are just like...

I mean that's a whole, it's that's its own thing, right?

That's that world, the characters,

the style, the edginess, all of that.

But the interesting thing about "Grand Theft Auto 6" to me

that I want to ask you about is they took forever.

It's the six month thing that you mentioned before.

You know, there's some games like that just take years

to bring to the conclusion.

What can you say about that process that, you know,

you eventually were able to take Unreal to completion.

If you were to look from the outside,

why does it take Grand Theft Auto that long

or other companies

to take the games to the conclusion

and I mean, just insight into what that process is like.

- Making games is very hard

and especially when you're pushing

the boundaries of something.

You know, with "Grand Theft Auto,"

it's just the realism

and feeling that you're in this huge city

and anything can happen and it's all living

and breathing in you're just a part of it.

The level with which Rockstar has brought quality

to that genre is astonishing.

And when you're building something at a level of quality

and detail that's never been achieved before,

you can't predict how long it will take.

Whatever problems you're solving today to get to, you know,

the next iteration of quality on it,

you don't know what new problems that will unlock.

And often, you know, you fix one thing

and make it super realistic

and that just highlights the unrealism of other things

that you then need to fix.

And I think the, you know, the thing that always

comes to mind is that shipping a game is easy

if you don't have a high quality standard,

we also won't have much success.

What we've seen from Rockstar is they take a long time,

but they ship amazing games and it's worth it in the end.

Right, a bad game is bad forever.

The late good game is eventually game is released

and is good.

- Do you ever feel, like Rockstar is a good example of that,

the pressure of delivering quality.

You know, Epic has not missed recently

that I'm aware of in terms of delivering quality.

Do you feel the pressure of that,

that you're not allowed misses?

- We certainly do.

Everybody's often working very much to the last minute

to make something excellent.

And it's really hard with these fast delivery timeframes

because you really have to get a lot of stuff up and running

before you can judge it,

like a new "Fortnite" season holistically.

You know, it's not until like the last month or so

that you really know what you've built

and you really understand it.

And if any late breaking problems emerge in like balance

or anything else, it's usually towards the end

and that usually leads to a rapid push to fix it.

And then other lessons you can only learn live.

And you know, from experience

and that means accepting a game that like

it's a live experience and it's also an experiment

and it's gonna continually be improving.

And anytime there's some things that some people don't like

and you learn from it and you improve it and you move on.

- Let me ask you a big philosophical question.

So you've created these gigantic worlds

that bring so much fun to humanity,

but you also get to learn about humanity.

What gives you hope about us humans,

about the future of humans, the future of humanity?

- You know, I see two contrasting worlds that, you know,

have been brought about in the digital age.

One is the world of social networks

and people typing at each other

and just, you know, massive negativity and politics

and, you know, hucksterism

and, you know, curation by engagement

often promoting negativity and toxicity.

That's a harsh world, I think is a step

backwards in many ways.

Like, I think that the foundation of the world

is actually a little bit shaky

because of just the social dynamic

that those platforms have have brought on.

But then I compare that with the good spiritedness

of what's happening online when you're connected

to real people, like actually playing "Fortnite."

Playing "Fortnite," full squads with people

you've never met before, never talked to,

and just judging what, you know,

human connections develop there

and whether they're positive.

I found those to be really, really excellent and endearing.

I think the lesson from all of that is that humans talking

to humans and being together in the real world

or virtual world is

a naturally empathetic medium at which naturally leads

to bonding and though conflict sometimes occurs,

it's just generally so much more promoting

of our social norms

and good interactions between people

and positivity promoting.

Whereas kind of the, you know,

typing angry message is thing at each other

as a self-reinforcing negative dynamic that's negative.

And then I think you though, you look at social media

and you look at gaming that is increasingly social

and I couldn't see a bigger divide between any two medium

as I see there in terms of the actual social dynamics.

One super positive, one super toxic at times.

- Yeah, that's actually really the text-based medium.

Now that could even be around gaming.

You could look at Discord, it could be a real toxic in text,

but you place humans together

in the real world, here in the room.

I literally have never, like,

I very rarely see humans not get along

in the physical space.

And the degree to which you can create a digital space,

like a metaverse type of space

where it's sufficiently immersive,

where you feel the other person, the empathy comes out

and then the joy that's derived from the empathy comes out.

And it's just a reminder that humans like,

I don't know that humans are good

and they wanna see the good in others,

they wanna share the goodness.

And then, you know, like when they get in

that group together, there's love there.

Now they might talk shit about some other group,

this is the dark side of humans, (laughs)

but together in terms of the dynamics

of that group, is joyful.

So yeah, that gives me hope as well.

And the more degree which we can create those worlds

online that make it super easy for us to connect

in that empathic way, the better.

And I am grateful that you are pushing the boundaries

of what's possible in creating such worlds.

And I'm grateful that you would talk with me today, Tim.

This was amazing and it's an honor to talk to you.

- Oh, thank you very much, it's been fun.

- Thanks for listening to this conversation

with Tim Sweeney.

To support this podcast,

please check out our sponsors in the description.

And now let me leave you some words from Benjamin Franklin.

"We do not stop playing because we grow old,

we grow old because we stop playing."

Thank you for listening, I hope to see you next time.

