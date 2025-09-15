# Chapter 1

It's hard for us humans to make any kind of clean predictions about highly non-linear dynamical systems.

But again, to your point, we might be very surprised what classical learning systems might be able to do about even fluid.

Yes, exactly.

I mean, fluid dynamics, Navier–Stokes equations, these are traditionally thought of as very

very difficult, intractable problems to do on classical systems.

They take enormous amounts of compute.

You know, weather prediction systems, you know

these kind of things all involve fluid dynamics calculations.

But again, if you look at something like Veo

our video generation model, it can model liquids quite well

surprisingly well, and materials, specular lighting.

I love the ones where, you know

there's, there's people who generate videos where there's

like, clear liquids going through hydraulic presses and then it's being squeezed out.

I, I used to write, uh, physics engines and graphics engines in

in my early days in gaming.

And I know, uh, it's so painstakingly hard to build programs that can do that

and yet somehow these systems are, you know

reverse engineering from just watching YouTube videos.

So th- presumably what's happening is it's extracting some underlying structure around how these materials behave.

So perhaps there is some kind of lower dimensional manifold that can be learned if we actually fully understood what's going on under the hood.

That's maybe, you know, maybe true of most of reality.

The following is a conversation with Demis Hassabis

his second time on the podcast.

He is the leader of Google DeepMind and is now a Nobel Prize winner.

Demis is one of the most brilliant and fascinating minds in the world today

working on understanding and building intelligence, and exploring the big mysteries of our universe.

This was truly an honor and a pleasure for me.

This is the Lex Fridman Podcast.

To support it, please check out our sponsors in the description and consider subscribing to this channel.

And now, dear friends, here's Demis Hassabis.

In your Nobel Prize lecture, you proposed what I think is a super interesting conjecture that

quote, "Any pattern that can be generated or found in nature can be efficiently discovered and modeled by a classical learning algorithm.

" What kind of patterns or systems might in- be included in that?

Biology, chemistry, physics, maybe cosmology?

Yup.

Neuroscience?

What, what are we talking about?

Sure.

Well, look, uh, I felt that it's sort of a tradition

I think, of Nobel Prize lectures that you're supposed to be a little bit provocative

and I wanted to follow that tradition.

What I was talking about there is, if you take a step back and you look at

um, all the work that we've done

especially with the AlphaX projects, so I'm thinking AlphaGo

of course AlphaFold, what they really are is we're building models of very combinatorially high dimensional spaces that

you know, if you tried to brute force a solution

find the best move in Go, or find the

the exact shape of a protein, and if you enumerated all the possibilities

you, there wouldn't be enough time in the

in the, you know, the time of the universe.

So you have to do something much smarter.

And what we did in both cases was build models of those environments

um, and that guided the search in a

in a smart way, and that makes it tractable.

So if you think about protein folding, which is obviously a natural system

you know, why should that be possible?

How does physics do that?

You know, proteins fold in milliseconds in our bodies

so somehow physics solves this problem that we've now also solved computationally.

And I think the reason that's possible is that in nature

natural systems have structure because they were subject to evolutionary processes that

that shaped them.

And if that's true, then you can maybe learn

uh, uh, what that structure is.

Th- this perspective, I think, is a really interesting one.

You've hinted at, at it, which is almost like

uh, crudely stated.

Anything that can be evolved can be efficiently modeled.

Think there's some truth to that?

Yeah, I sometimes call it survival of the stablest

or something like that, because, uh, i- you know

it's, it's.

..

Of course there's evolution for life, uh

living things, but there's also, you know

if you think about geological times, so the shape of mountains

that's been shaped by weathering processes, right

over thousands of years.

But then you can even take it cosmological

the orbits of planets, the, um, shapes of asteroids.

These have all been.

..

Survived kind of processes that have acted on them many

many times.

So if that's true, then there should be some sort of pattern

um, that you can kind of reverse learn and

uh, a kind of manifold really that helps you

uh, uh, search to the right solution

to the right shape, um, and actually allow you to predict things about it

uh, in an efficient way, because it's not a random pattern

right?

So, um, it may not be possible for

for manmade things or abstract things like factorizing large numbers because.

..

unless there's patterns in the number space, which there might be.

But if there's not and it's uniform, then there's no pattern to learn

there's no model to learn that will help you search

so you have to do brute force.

So in that case, you, you know

you maybe need a quantum computer, something like this.

But in most things in nature that we're interested in

uh, are not like that.

They have structure, um, that evolved for a reason and survived over time.

And if that's true, I think that's potentially learnable by a neural network.

It's like nature's doing a search process, and it's so fascinating that it's

in that search process, it's creating systems that could be efficiently modeled.

That's right.

Yeah.

It's so interesting.

So they can be efficiently rediscovered or recovered

um, because nature's not random, right?

These, uh, uh, everything that we see around us

including, like, the elements that are more stable

all of those things, they're subject to

um, some kind of selection process, pressure.

Do you think, because you're also a fan of theoretical computer science and complexity

do you think we can come up with a kind of complexity class

like a complexity zoo type of class, where maybe it's the set of learnable systems

the set of.

..

..

. learnable natural systems, LNS?

Yeah.

 This is a Demis Hassabis- A new class.

 .

..

new class of systems that could be actually learnable by classical systems in this kind of way

natural systems that can be, uh, modeled efficiently.

Yeah.

I mean, I'm, I've always been fascinated by the P equals NP question and what is modelable by classical systems

i.

e.

non-quantum systems, you know, Turing machines, in effect.

And that's exactly what I'm working on, actually

in kind of my few moments of spare time with a few colleagues

about w- is should there be, you know

maybe a new class or problem that is solvable by this type of neural network process and kind of mapped onto these natural systems

so, you know, the things that exist in physics and have structure.

So I think that could be a very interesting

uh, new way of thinking about it.

And it sort of fits with the way I think about physics in general

which is the, you know, I think information is primary.

Information's the most sort of fundamental unit of the universe

more fundamental than energy and matter.

I think they can all be converted into each other

but I think of the universe as a kind of informational system.

So when you think of it, the universe is an informational system

then the P equals NP question is a

is a physics question.

That's right.

 And, and it's a question that can help us actually solve the entirety of this whole thing going on.

Yeah, I think it's one of the most

uh, fundamental questions, actually, if you think of physics as informational

uh, and, and the answer to that

I think, is gonna be, you know

very enlightening.

More specific to the P and NP question

this, again, some of the stuff we're saying is kinda crazy right now

just like the Christian Anfinsen Nobel Prize speech controversial thing that he said sounded crazy

and then you went and got a Nobel Prize for this with John Jumper

solved the problem.

So let me, let me just stick to the P equals NP.

Do you think there's something in this thing we're talking about that could be shown if you g- can do something like

uh, polynomial time or constant time compute ahead of time and construct this gigantic model

then you can solve some of these extremely difficult problems

in a theoretical computer science kind of way?

Yeah, I think that there are, uh

actually a huge class of problems that could be couched in this way

the way we did AlphaGo and the way we did AlphaFold

where, you know, you, you model what the dynamics of the system is

the, the, the, the properties of that system

the environment that you're trying to understand, and then that makes the search for the solution or the prediction of the next step efficient

basically polynomial time, so tractable by a

uh, classical system, uh, which a neural network is.

It runs on normal computers, right, classical computers

uh, Turing machines in effect.

And, um, I think it's one of the most interesting questions there is

is how far can that paradigm go?

You know, I think we've proven, uh

and the AI community in general, that classical systems

Turing machines, can go a lot further than we previously thought.

You know, they can do things like model the structures of proteins and play Go to better than world champion level

and, uh, you know, a lot of people would've thought maybe 10

20 years ago that was decades away, or maybe you would need some sort of quantum machines to

to, quantum systems to be able to do things like protein folding.

And so, I think we haven't really

uh, even sort of scratched the surface yet of what

uh, classical systems, so-called, uh, uh

could do.

And of course, AGI being built on a

on a neural network system, on top of a neural network system

on top of a classical computer would be the ultimate expression of that.

And I think the limit, the, you know

the, the, what, what the bounds of that kind of system

what it can do is a very interesting question and

and, and directly speaks to the P equals NP question.

What, what do you think, again, hypothetical

might be outside of this, maybe emergent phenomena?

Like if you look at cellular automata- Mm-hmm.

.

..

some of the, you have extremely simple systems and then some complexity emerges.

Yes.

Maybe that would be outside, or even would you guess even that might be amenable to efficient modeling by a classical machine?

Yeah, I think those systems would be right on the boundary

right?

So, um, I think most emergent systems

cellular automata, things like that, could be modelable by a classical system.

You just sort of do a forward simulation of it and it'd probably be efficient enough.

Um, of course, there's the question of things like chaotic systems where the initial conditions really matter

and then you get to some, you know

uncorrelated end state.

Now, those could be difficult to model.

So I think these are kind of the open questions

but I think when you step back and look at what we've done with the systems and the

and the problems that we've solved, and then you look at things like VO3 on like video generation sort of rendering physics and lighting and things like that

you know, really core fundamental things in physics

um, it's pretty interesting.

I think it's telling us something quite fundamental about how the universe is structured

in my opinion.

Um, so, you know, in, in a way

that's what I want to build AGI for

is to help, uh, us, uh

as scientists answer these questions, uh, like P equals NP.

Yeah, I think, uh, we might be continuously surprised about what is modelable by classical computers.

I mean, AlphaFold 3 on the interaction side is surprising

that you can make any kind of progress on that direction.

Alpha Genome is surprising, that you can map the genetic code to the function.

..

. kind of playing with the emergent kind of phenomena

you think there's so many combinatorial options that

and then here you go-  .

..

is you can find the kernel that is efficiently modeled.

Yes, because, uh, there's some structure

there's some landscape, you know, in the energy landscape or whatever it is that you can follow

some grading you can follow.

And of course, what neural networks are very good at is following gradients.

And so if there's one to follow an object- and you can specify the objective function correctly

you know, you don't have to deal with all that complexity

which I think is how we maybe have naively thought about it for decades

those problems.

If you just enumerate all the possibilities, it looks totally intractable and there's many

many problems like that.

And then you think, well, it's like 10 to 300 pop- possible protein structures

uh, 10 to the 100 and, you know

70 possible go positions.

All of these are way more than atoms in the universe.

So how could one possibly find the, the right solution or predict the next step and

and it.

..

but it turns out that it is possible and of course reality nature does do it

right?

Proteins do fold.

So that, that gives you confidence that there must be.

..

if we understood how physics was doing that

uh, in a sense, uh, then.

..

and we could mimic that process, I model that process

uh, it should be possible on our classical systems is

is, is basically what the conjecture is about.

And of course there's non-linear dynamical systems, highly non-linear dynamical systems

everything involving fluid.

Yes.

Right.

You know, there.

..

recently a conversation with Terence Tao who mathematically

uh, he contends with a very difficult aspect of systems that have some singularities in them that break the mathematics and it's just hard for us humans to make any kind of clean predictions about highly non-linear dynamical systems.

But again, to your point, we might be very surprised what classical learning systems might be able to do about even fluid.

Yes, exactly.

I mean, fluid dynamics, Navier-Stokes equations, these are traditionally thought of as very

very difficult intractable kind of problems to do on classical systems.

They take enormous amounts of compute, you know

weather prediction systems, you know, these kind of things all involve fluid dynamics calculations.

And, um.

..

but again, if you look at something like Veo

our video generation model, it can model liquids quite well

surprisingly well.

And materials, specular lighting.

I love the ones where, you know

there's, there's people who generate videos where there's like clear liquids going through hydraulic presses and then it's being squeezed out.

I used to write, uh, physics engines and graphics engines in

in my early days in gaming and I know it's just so painstakingly hard to build programs that can do that and yet somehow these systems are

you know, reverse engineering from just watching YouTube videos.

So presumably what's happening is it's extracting some underlying structure around how these materials behave.

So perhaps there is some kind of lower dimensional manifold that can be learned if we actually fully understood what's going on under the hood.

That's maybe, you know, maybe true of most of reality.

Yeah, I've been continuously precisely by this aspect of Veo 3.

I think a lot of people highlight different aspects including the comedic and the media- Yes.

.

..

all that kind of stuff.

And then th- the ultra-realistic ability to capture humans in a really nice way that's compelling and g- feels close to reality and then combine that with native audio.

All of those are marvelous things about Veo 3

but the exactly the thing you're mentioning which is the physics- Yeah.

.

..

is not perfect but it's pretty damn good.

And then the, the really interesting scientific question is what is it understanding about our world in order to be able to do that?

# Chapter 2

I love the ones where, you know

there's, there's people who generate videos where there's like clear liquids going through hydraulic presses and then it's being squeezed out.

I used to write, uh, physics engines and graphics engines in

in my early days in gaming and I know it's just so painstakingly hard to build programs that can do that and yet somehow these systems are

you know, reverse engineering from just watching YouTube videos.

So presumably what's happening is it's extracting some underlying structure around how these materials behave.

So perhaps there is some kind of lower dimensional manifold that can be learned if we actually fully understood what's going on under the hood.

That's maybe, you know, maybe true of most of reality.

Yeah, I've been continuously precisely by this aspect of Veo 3.

I think a lot of people highlight different aspects including the comedic and the media- Yes.

.

..

all that kind of stuff.

And then th- the ultra-realistic ability to capture humans in a really nice way that's compelling and g- feels close to reality and then combine that with native audio.

All of those are marvelous things about Veo 3

but the exactly the thing you're mentioning which is the physics- Yeah.

.

..

is not perfect but it's pretty damn good.

And then the, the really interesting scientific question is what is it understanding about our world in order to be able to do that?

Because if the cynical take with diffusion models

there's no way it understands anything.

Mm-hmm.

But it seems.

..

I mean, I don't think you can generate that kind of video without understanding and then our own philosophical notion of what it means to understand then is like brought to the surface.

Like, do.

..

to what degree do you think Veo 3 understands our world?

I think to the extent that it can predict the next frames

you know, in a coherent way, that's some.

..

that is a form, you know, of understanding

right?

Not in the anthropomorphic version of, you know

it's not some kind of deep philosophical understanding of what's going on.

I don't think these systems have that, but they

they certainly have, uh, modeled enough of the dynamics

you know, put it that way, that they can pretty accurately generate whatever it is

eight seconds of consistent video that by eye at least

you know, kind of a glance is quite hard to distinguish what the issues are.

And imagine that in two or three more years time

that's the thing I'm thinking about and how incredible that will.

..

they will look, uh, given where we've come from

you know, the early versions of that

uh, uh, one or two years ago.

And so, um, the rate of progress is incredible and I think

um, I'm like you is like a lot of people love all of the

the, the stand-up comedians and the, the.

..

it actually captures a lot of human dynamics very well and

and body language but actually the thing I'm most impressed with and fascinated by is the physics behavior

the lighting and materials and liquids and it's pretty amazing that it can do that.

And I think that shows, uh, that it has some notion of at least intuitive physics

right?

Um, how things are supposed to work

uh, intuitively maybe the way that, uh

a human child would understand physics, right?

As opposed to a, you know, a PhD student really

uh, being able to unpack all the equations.

It's more of an intuitive physics understanding.

Well, that intuitive physics understanding, that's the base layer

that's the thing people sometimes call a common sense.

Mm-hmm.

It really understands something that I think that really surprises a lot of people.

It blows my mind that I just didn't think it would be possible to generate that level of realism without understanding.

Mm-hmm.

There's this notion that you can only understand the physical world by having an embodied AI system

a robot that interacts with that world.

That's the only way to construct an understanding of that world.

Yeah.

But Veo 3 is directly challenging that- Right.

.

..

it feels like.

Yes.

And this is very interesting, you know

even now if we.

..

if you were to ask me five, 10 years ago

I would have said even though I was immersed in all of this

I would have said, "Well yeah, you probably need to understand intuitive physics.

" You know, like if I push this off the table

this glass it will maybe shatter, you know

um, and the, and the liquid will spill out

right?

So we know all of these things.

But I thought that, you know, and there's a lot of theories in neuroscience

it's called action and perception, where, you know

you, you need to act in the world to really truly perceive it in a deep way.

And there was a lot of theories about

you need embodied intelligence or robotics or something

or maybe at least simulated action, uh

so that you would understand things like intuitive physics.

But it seems like, um, you can understand it through passive observation

which is pretty surprising to me, and

and again, I think hints at something underlying about the nature of

uh, reality, in, in, in my opinion

beyond, um, just the, you know

the cool videos that it generates.

Um, and, and of course there's next stages is maybe even making those videos interactive so

uh, one can actually step into them and move around them

um, which would be really mind-blowing, especially given my games background.

 So  you can imagine.

Uh, and then, and then I think

you know, you're, we're starting to get towards what I would call a world model

a model of how the world works, the mechanics of the world

the physics of the world, and the things in that world.

And of course that's what you would need for a true AGI system.

I have to talk to you about video games.

Yes.

So you, you were being a bit trolly.

  I, I think you're, you're having more and more fun on Twitter

on X, which is great to see.

So a guy named Jimmy Apples tweeted, "Let me play a video game of my VO3 videos already.

Uh, Google cooked so good.

Playable world models wen?

" Spelled W-E-N question mark.

Um, and then you quote tweeted that with

"Now wouldn't that be something.

" Mm-hmm.

So how, how hard is it to build game worlds with AI?

Maybe can you look out into the future

uh, of video games- Mm.

.

..

five, 10 years out?

Mm.

What do you think that looks like?

Well, games were my first love really

and doing AI for games was the first thing I did professionally in

in my teenage years, and, and was the first

uh, major AI systems that I built.

And, uh, I always wanna, I have

I wanna scratch that itch one day and come back to that.

So, you know, and I will do

I think, and, um, I think I'd sort of dream about

you know, what would I have done back in the '90s if I'd had access to the kind of AI systems we have today?

And I think you could build absolutely mind-blowing games.

Um, and I think the next stage is

I always used to love making.

..

All the games I've made are open-world games.

Mm-hmm.

So they're games where there's a simulation and then there's AI characters

and then the player, uh, interacts with that simulation and the simulation adapts to the way the player plays.

And I always thought they were the coolest games because

uh, so games like Theme Park that I worked on where everybody's game experience would be unique to them

right, because you're kinda co-creating the game

right?

Uh, we set up the parameters, we set up initial conditions

and then you as the player immersed in it

and then you are co-creating it with the

with the simulation.

But of course, it's very hard to program open-world games.

You know, you've got to be able to create

uh, content whichever direction the player goes in

and you want it to be compelling no matter what the player chooses.

Um, and so it was always quite difficult to build

uh, things like Cellular Automata, actually, type of

those kind of classical systems which created some emergent behavior.

Um, but they're always a little bit fragile

a little bit limited.

Now we're maybe on the cusp in the next few years

five, 10 years, of having AI systems that can truly create around your imagination

um, can nar- and sort of dynamically change the story and storytell the narrative around

uh, and make it dramatic no matter what you end up choosing.

So it's like the ultimate choose-your-own-adventure sort of game.

And, uh, you know, I think maybe we're within reach if you think of a kind of interactive version of VO

uh, and then f- wind that forward five to 10 years and

um, you know, imagine how good it's gonna be.

Yeah.

So you said a lot of super interesting stuff there.

So one, the open world, built into that is a deep personalization

the way you've described it.

Mm.

So it's not just that it's open world

like you can open any door and there'll be something there.

It's that the choice of which door you open in an unconstrained way defines the worlds you see.

So some games try to do that, they give you choice- Yes.

.

..

but it's really just an illusion of choice- Yes.

.

..

because the only, uh, uh, like

like Stanley Parable, is, is- Yeah.

.

..

a game I recently  played.

It's, it's, it's really, there's a couple of doors and it really just takes you down a narrative.

Stanley Parable is a great video game I recommend people play- Yeah.

.

..

that kinda, uh, in a meta way

uh,  mocks the illusion of choice and there's philosophical notions of free will and so on.

But, uh, I do, like one of my favorite games of Elder Scrolls is Daggerfall

I believe, that they really played with the

like, random generation of the dungeons- Yeah.

.

..

of if you could step in and they- Yes.

.

.

give you this feeling of an open world.

And there, you mentioned interactivity, you don't need to interact.

That, that's a first step, is you don't need to interact that much

you just, when you open the door

whatever you see is randomly generated for you.

Yeah.

And that's already an incredible experience, because you might be the only person to ever see that.

Yeah.

Exactly.

And- and so.

..

But what you'd like is a little bit better than sort- sort of a random generation

right?

So you'd like, uh.

..

And- and also better than a simple A

B hardcoded choice, right?

That's not really a open world, right?

Like as, as you say, it's just giving you the illusion of choice.

What you want to be able to do is

uh, is potentially anything in that game environment.

Um, and I think the only way you can do that is to have

uh, generated systems, systems that, uh

will generate that on the fly.

Of course you can't create infinite amounts of game assets

right?

It's expensive enough already how triple A games are made today.

And that was obvious to, to us back in the '90s when I was working on all these games.

I think maybe Black & White, uh

was the game that I worked on early stages of that

that had the, still probably the best AI

learning AI, in it.

It was an early reinforcement learning system that you

you know, you were, you were looking after this mythical creature and growing it and nurturing it

and depending how you treated it, it would treat the villagers in that world in the same way.

So if you were mean to it, it would be mean.

If you were good, it would be protective.

And so it was really a reflection of the way you played it.

So actually, all of the, uh.

..

I've been working on sort of simulations and AI

uh, uh, through the medium of games at the beginning of my career

and, and really the whole of what I do today is still a follow-on from

uh, those early more hardcoded ways of doing the AI to now

you know, fully general learning systems that- that are trying to achieve the same thing.

Yeah.

It's been, uh, interesting, hilarious, and

uh, fun to watch you and Elon obviously itching to create games

'cause you're both gamers.

And one of the sad aspects of your-.

..

uh, incredible success in so many domains of science

like serious adult stuff- Yeah.

.

..

that you might not have time to really create a game.

You might end up creating the tooling that others would create the game.

Right.

And you have to watch-  Yeah, exactly.

.

..

other, others create the thing you've always dreamed of.

Do you think it's possible you can somehow in your extremely busy schedule actually find time to create something like Black & White

some, some, uh, an actual video game.

Where, like, you could m- m- make the childhood dream- Yeah.

.

.

 become, become a reality?

Well, you know, uh, there's two things one can think about that is maybe

uh, with vibe coding as it gets better-  Yes.

.

.

there's a possibility that I could, you know- Sure.

.

.

one could do that actually in, in your spare time.

So I'm quite excited about that as a

as-  That would be my project if

if I got the time to do some vibe coding.

Um, I'm actually itching to do that.

And then the other thing is, you know

maybe it's a sabbatical after AGI has been safely stewarded into the world and delivered into the world

you know, that and then working on my physics theory

you know, as we talked about in the beginning

those would be the two.

..

my, my two post-AGI projects, let's call it that way.

I would, I would love to see which post- The ultimate game.

.

..

post-AGI, which you choose.

Solving, uh, the,  the problem that some of the smartest people in human history contended with

so P equals NP,  or creating a cool video game.

Yeah.

Well, but they- Right?

.

.

but they might.

..

But in my world, they'd be related- Sure.

.

.

because it would be an open world simulated game

uh, as realistic as possible.

So, you know, what, what is

what is the universe?

That's, that's, that's speaking to the same question

right?

NP equals NP.

I think all these things are related, at least in my mind.

I mean, in a really serious way

I think v- video games sometimes are looked down upon as just this fun side activity

but especially as, uh, AI does more and more of

um, the difficult, uh, boring tasks

something that we in, in modern world call work

you know, video games is the thing in which we may find meaning

in w- which we may find, like

what to do with our time.

You could create incredibly rich, meaningful experiences.

Like, that's what human life is.

And then in video games, you can create more sophisticated

more diverse ways of living.

Yeah.

Right?

That's the whole idea.

I think so.

I mean, those of us who love games

and I still do, is, is, is

um, you know, it almost can let your imagination run wild

right?

Like, I, I used to love games

um, and working on games so much because it's the fusion

especially in the '90s and 2- early 2000s

the sort of golden era, maybe the '80s of

of, of ga- of the games industry

and it was all being discovered, new genres were being discovered.

We weren't just making games.

We felt we were, we were creating a new entertainment medium that never existed before

uh, especially with these open world games and simulation games where you would co-create.

..

you, as the player, were co-creating the story.

There's no other media, uh, entertainment media where you do that

where you as the audience actually co-create the

the story.

And of course now with multiplayer games as well

it can be a s- very social activity

and can explore all kinds of interesting worlds in that.

But on the other hand, you know

it's very important to, um, also enjoy and experience

uh, the physical world.

But the question is then, you know

I think we're gonna have to kind of confront the question again of what is the fundamental n- nature of reality

uh, what is g- gonna be the difference between these increasingly realistic simulations and

uh, multiplayer ones, and e- emergent, um

and what we do in the real world?

Yeah, there's clearly a huge amount of value to experiencing the real world

nature.

There's also a huge amount of value in experiencing other humans directly in person

the way we're sitting here today.

Yes.

But we need to really scientifically, rigorously answer the question

why?

Yeah.

Exactly.

And which aspect of that can be mapped- Yeah.

.

..

into the virtual world?

Exactly.

And- And it's not, it's not enough to say

"Yeah, you should go touch grass and hang out in nature.

" It's like, why- Yeah.

.

.

exactly- Yeah.

.

..

is that valuable?

Yes.

And I guess that's maybe the thing that's been

uh, haunting me or obsessing me from the beginning of my career.

If, if you think about all the different things I've done

that's.

..

they're all related in that way.

The simulation, nature of reality, and what is the bounds of

you know, what can be modeled.

Sorry for the ridiculous questions, but so far

what is the greatest video game of all time?

 What's up there?

What, what makes- Well, my favorite one of all time is Civilization

I, I have to say.

That, that was the, the, the Civilization I and Civilization II are my favorite games of all time.

Um- I can only assume you've avoided the most recent one because it would probably.

..

you would d- that would be your sabbatical

that w- you would disappear.

Yes.

 Exactly.

They take a lot of time, these Civilization games

so, uh, I got to be careful with them.

Fun question.

You and Elon seem to be somehow solid gamers.

Uh, is there a connection between being great at gaming and

and, uh, being great leaders of AI companies?

I don't know.

I.

..

It's an interesting one.

I mean, uh, we both love games and

uh, it's interesting, he wrote games as well to start off with.

It's probably a v- especially in the era I grew up in where home computers were.

..

just became a thing, you know, in the late '80s and '90s

especially in the UK.

I had a Spectrum and then a, a Commodore Amiga 500

which was my- Nice.

.

.

m- my favorite computer ever, and that's where I learned all my programming.

And of course, it's a very fun thing

uh, to program is to program games.

So I think it's a great way to learn programming

probably still is, and, um, and then of course

I immediately took it in directions of AI and simulations

which.

..

so I ma- was able to express my interest in

in games, uh, and my sort of wider scientific interests all together.

And then the final thing I think that's great about games is it fuses

# Chapter 3

uh, it's interesting, he wrote games as well to start off with.

It's probably a v- especially in the era I grew up in where home computers were.

..

just became a thing, you know, in the late '80s and '90s

especially in the UK.

I had a Spectrum and then a, a Commodore Amiga 500

which was my- Nice.

.

.

m- my favorite computer ever, and that's where I learned all my programming.

And of course, it's a very fun thing

uh, to program is to program games.

So I think it's a great way to learn programming

probably still is, and, um, and then of course

I immediately took it in directions of AI and simulations

which.

..

so I ma- was able to express my interest in

in games, uh, and my sort of wider scientific interests all together.

And then the final thing I think that's great about games is it fuses

um, artistic design, you know, art

with the, the, the most cutting-edge programming.

Um, so again, in the '90s, all of the most interesting

uh, technical advances were happening in gaming

whether that was AI, graphics, physics engines

uh, hardware, even GPUs, of course

were designed for gaming originally.

Um, so e- everything that was pushing computing forward in the

in the '90s was due to gaming.

So u- interestingly, that was where the forefront of research was going on

and there was this incredible fusion with, with art

um, y- you know, graphics, but also music

and just a whole new media of storytelling

and I love that.

For me, it's this sort of multidisciplinary kind of effort is

again, something I've enjoyed my whole, my whole life.

I have to ask you, I almost forgot about w- one of the many

and I would say one of the most incredible things recently

uh, that somehow didn't yet get enough attention is AlphaEvolve.

We talked about evolution a little bit, but it's the Google DeepMind system that evolves algorithms.

Yeah.

Are these kinds of evolution-like techniques promising as a component of a future superintelligent system?

So for people who don't know, it's kind of

um.

..

I don't know if it's fair to say it's LLM-guided evolution search.

Yeah.

So it's ev- e- evolution algorithms are doing the search

and LLMs are telling you where.

Yes, exactly.

So LLMs are kind of proposing some possible solutions

and then you do, you use evolutionary computing on top to

to, to find some novel part of the

of the search space.

So actually, I think it's an example of very promising directions

where you combine LLMs or foundation models with other computational techniques.

Evolutionary methods is one, but you could also imagine Monte Carlo tree search.

Basically, many types of search algorithms or reasoning algorithms sort of on top of

or using, the foundation models as a basis.

So I actually think there's quite a lot of interesting

uh, things to be discovered probably with these sort of hybrid systems

let's call them.

But not to romanticize evolution- Yeah.

.

..

I'm only human, but do, do you think there's some value in whatever that mechanism is?

'Cause we already talked about natural systems.

Do you think where there's a lot of low-hanging fruit of us understanding being mo- being able to model

um, being able to simulate evolution and then using that

whatever we understand about that nature-inspired mechanism to

to then do search better and better and better?

Yes.

So if you think about, uh, again

br- a b- uh, breaking down the sys- sort of systems we've built

uh, to their really fundamental core, you've got

like, the model of the, of the underlying dynamics of the system.

Uh, and then if you want to discover something new

something novel that hasn't been seen before, um

then you need some kind of search process on top to take you to a novel region of the

of the, of the search space.

And, um, you can do that in a number of ways.

Evolutionary computing is one.

Um, with AlphaGo, we just used Monte Carlo tree search

right?

And that's what found Move 37, the new

uh, kind of never-seen-before strategy in Go.

And so that's how you can go beyond potentially what is already known.

So the model can model everything that you currently know about

right?

All the data that you currently have.

But then how do you go beyond that?

So that starts to speak about the ideas of creativity.

How can these systems create something new, fi- discover something new?

Obviously, this is super relevant for scientific discovery or pushing med.

..

science and medicine forward, which we want to do with these systems.

And you can actually bolt on some, uh

fairly simple search systems on top of these models and get you into a new region of space.

Of course, you also have to, um

make sure that, uh, you're not searching that space totally randomly or it would be too big.

So you have to have some objective function that you're trying to optimize and hill climb towards

and that guides that search.

But there's some mechanism of evolution that are interesting

maybe in the space of programs, but then the space of programs is an extremely important space because you can probably generalize to

uh, to everything.

You know?

Uh, but, you know, for example

mutation.

So it's not just Monte Carlo tree search where it's like a search.

Mm-hmm.

You could, every once in a while alt- Combine things

yeah.

Combine things- Yeah.

.

.

alter c- like, sub.

..

like components of a thing.

Yes.

So then, you know, what evolution is really good at is not just the natural selection.

It's combining things and building increasingly complex hierar- hierarchical systems.

Yes.

So that component's super interesting- Yeah.

.

..

especially like with AlphaEvolve and the space of programs.

Yeah, exactly.

So there's a b- You can get a bit of an extra property out of evolutionary systems

which is some new emergent capability may come about.

Mm-hmm.

Yes.

Right?

Of course, like happened with life.

Interestingly, with naive, uh, sort of traditional evolutionary computing methods without LLMs and the modern AI

the problem with them were.

..

they were.

..

there was a.

..

they were very well studied in the '90s an

an, an, an early 2000s and some promising results.

But the problem was they could never work out how to evolve new properties

new emergent properties.

You always had a sort of subset of the properties that you put into the system.

But maybe if we combine them with these foundation models

perhaps we can overcome that limitation.

Obviously, uh, natural evolution clearly did, because it evo- it did evolve new capabilities

right?

So, uh, bacteria to where we are now.

So clearly the.

..

it must be possible with evolutionary systems to generate

uh, new patterns, you know, f- going back to the first thing we talked about

and, uh, new capabilities and emergent properties.

And maybe we're on the cusp of discovering how to do that.

Yeah, listen, uh, AlphaEvolve is one of the coolest things I've ever seen.

I've, I've, uh.

..

Uh, uh, on my desk at home

you know, most of my time is spent behind that computer just programming.

And next to the, the three screens is a s- a skull of a

a Tiktaalik which is one of the early organisms that crawled out of the water onto land.

And I just kind of watch that little guy.

 And it's like you.

..

The, the.

..

whatever the computation mechanism of evolution is, it's quite incredible.

Yes.

It's truly, truly incredible.

Yeah.

Now, whether that's exactly the thing we need to do to do our search

but never, never, uh, dismiss the power of nature what

what it did here.

Yeah.

And it's amazing.

Um, whi- which is a relatively simple algorithm

right?

Effectively.

And it can generate all of this immense complexity

emerges.

Obviously running over, you know, 4 billion years of time

but, but it's, it's, it's.

..

You know, you can think about that as

again, a, a, a proc- a search process that ran over the physics substrate of the universe for

uh, a long amount of computational time.

But then it generated all this incredible, uh

rich diversity.

So, uh, so many questions I wanna ask you.

So one, you do have a dream.

One of the natural systems you want to

uh, try to model is a, is a cell.

Yes.

That's a beautiful dream.

Uh, I could ask you about that.

I also just, for that purpose, on the AI scientist front

just broadly.

So there's a essay, uh, from Daniel Kakutaiyo

Scott Alexander, and others that outline steps along the way to get to ASI and has a lot of interesting ideas

uh, in it.

One of which is, uh, including a superhuman coder and a superhuman AI researcher and in that

there's a term of research taste that's really interesting.

So in everything you've seen, do you think it's possible for AI systems to have research taste to help you in the way that AI co-scientist does to help steer human

um, human brilliant scientists and then bo- potentially by itself to figure out what are the directions

eh, where you want to gen- generate truly novel ideas?

'Cause that seems to be like a really important component of how to do great science.

Yeah.

I think that's gonna be one of the hardest things to

to, uh, mimic or model is, is this

this idea of taste or, or judgment.

I think that's what separates the, you know

the, the great scientists from the good scientists.

Like all, all professional scientists are good technically

right?

Otherwise they wouldn't have bi- made it, uh

that far in, in academia and things like that.

But then do you have the taste to sort of sniff out what the right direction is

what the right experiment is, what the right question is?

So the qu- it's the, it's.

..

Picking the right question is, is the hardest part of science

um, and, and making the right hypothesis and

um, that's what, you know, today's systems definitely they can't do.

So, you know, I often say it's harder to come up with a conjecture

a really good conjecture than it is to solve it.

So we may have systems soon that can solve pretty hard conjectures.

Um, you know, I, I.

..

Um, in math Olympiad problems where we

we, you know, Alpha proved last year our system got

you know, silver medal in that.

Really hard problems.

Maybe eventually we'll be able to solve a Millennium Prize kind of problem

but could a system come up with a conjecture worthy of study that someone like Terence Tao would have gone

"You know what?

That's a really deep question about the nature of maths or the nature of numbers or the nature of physics"?

And that is far harder type of creativity and we don't really know.

..

Today's systems clearly can't do that and we're not quite sure what that mechanism would be.

This kind of leap of imagination like, like Einstein had when he came up with

you know, special relativity and then general relativity with the knowledge he had at the time.

As for, for conjecture, the.

..

You want to come up with a thing that's interesting and it's amenable to proof.

Yes.

So, like, it's easy to come up with a thing that's extremely difficult.

Yeah.

It's easy to come up with a thing that's extremely easy but tha- at that very edge- That sweet spot

right?

Of, of basically advancing the science and splitting the hypothesis space into two ideally

right?

Whether if it's true or not true, you

you've learnt something really useful and, um

and, and that's hard and, and, and making something that's also

uh, you know, falsifiable and within sort of the technologies that you have

you currently have available.

So it's a very creative process actually, highly creative process that

um, I, I think just the kind of naive search on top of a model won't be enough for that.

Okay.

The idea of splitting the hypothesis space in two is super interesting.

So, uh, I've heard you say that there's basically no failure in.

..

Or failure's extremely valuable if it's done.

..

if you construct the questions right, if you construct the experiments right

if you design them right, that failure and success are both useful.

So- Yes.

.

..

perhaps because it splits the hypothesis base in two.

It's like a binary- Yes.

.

.

search?

That's right.

So when you do, like, you know

real blue sky research, there's no such thing as failure really as long as you're picking experiments and hypotheses that

that, that, that meaningfully split the hypothesis space so

you know, and you learn something, you can learn something kind of equally valuable from a

an experiment that doesn't work.

That should tell you if you've designed an experiment well and your hypotheses are

are interesting, it should tell you a lot about where to go next.

And, um, and then it's j- you're

you're effectively doing a search process, um

and using that information in, in, you know

very helpful ways.

So to go to your dream of, uh

modeling a cell, um, what are the big challenges that lay ahead for us to make that happen?

We should maybe highlight that AlphaFold.

..

I mean, there's just so many leaps.

Yeah.

So AlphaFold solved, if it's fair to say

protein folding and there's so many incredible things we could talk about there including the open sourcing

uh, the, everything you've released.

AlphaFold3 is doing protein RNA, DNA interactions- Mm-hmm.

.

..

which is super complicated and, and fascinating.

There's a amenable to modeling.

Alpha Genome, uh, predicts how small genetic changes

like if we think about single mutations, how they link to actual

uh, function.

So, um, those are.

..

It seems like it's creeping along .

Yes.

So sophistic8.

..

To, to much more complicated, uh, things like a cell but a cell has a lot of really complicated components.

Yeah.

So what I've tried to do throughout my career is I have these really grand dreams and then I try to

as you've noticed, and then I try to break but I try to break them down.

Uh, an- you know, it's easy to have a kind of

a, a c- crazy ambitious dream but the

the, the trick is how do you break it down into manageable

achievable, uh, interim steps that are meaningful and useful in their own right?

And so Virtual Cell, which is what I call the project of modeling a cell

uh, I've had this idea, you know

of wanting to do that for maybe more like 25 years and

uh, I used to talk with Paul Nurse who is a bit of a mentor of mine in biology.

He runs the, the, you know, he founded the Crick Institute and

and won the Nobel Prize in, in 2001.

Uh, i- i- is, is.

..

We've been talking about it since-.

..

you know, t- before the- you know

in the 90s.

And, um, and I come, used to come back to it every five years

is like, what would you need to model of the full internals of a cell so that you could do experiments on the virtual cell and what those experiment

p- you know, in silico, and those predictions would be useful for you to save you a lot of time in the wet lab

right?

That would be the dream.

Maybe you could 100X speed up experiments by doing most of it in silico.

The search in silico and then you do the validation step in the wet lab.

That would be, that's the, that's the dream.

And so, um, but maybe now, finally

uh, so I was trying to build these components

AlphaFold being one, that, that would, uh

allow you eventually to model the full interaction

a full simulation of a cell.

And I'd probably start with a yeast cell

and partly that's what Paul Nurse studied, because a yeast cell is like a full organism that's a single cell

right?

So it's a kind of simplest single cell organism.

And so it's not just a cell, it's a full organism.

And, um, and yeast is very well understood and so that would be a good candidate for uh

uh, uh a kind of full simulated model.

Now, AlphaFold is the, is the solution to the kind of static picture of what does a

what does a protein look, 3D structure protein look like

a static picture of it.

But we know that biology, all the interesting things happen with the dynamics

the interactions.

And that's what AlphaFold3 is, is the first step towards

is modeling those interactions.

So first of all pairwise, you know

proteins with proteins, proteins with RNA and DNA.

But then, um, the next step after that would be modeling maybe a whole pathway

maybe like the TOR pathway that's involved in cancer or something like this

and then eventually you might be able to model

you know, a whole cell.

Also, there's another complexity here that stuff in a cell happens at different timescales.

Is that tricky?

It's like there, you know, protein, uh

folding is, you know, super fast.

Yes.

Um, I don't know all the biological mechanisms- Yeah.

.

..

but some of them take a long time.

Yeah.

And so is that, that's a level

so the levels of interaction has a different temporal scale- Yeah.

.

..

that you have to be able to model.

So that would be hard.

So you'd probably need several simulated systems that can interact at these different temporal dynamics

or at least, uh, maybe it's like a hierarchical system

so, um, you can jump up or down the

the different temporal stages.

So can you avoid, I mean one of the challenges here is not

# Chapter 4

Is that tricky?

It's like there, you know, protein, uh

folding is, you know, super fast.

Yes.

Um, I don't know all the biological mechanisms- Yeah.

.

..

but some of them take a long time.

Yeah.

And so is that, that's a level

so the levels of interaction has a different temporal scale- Yeah.

.

..

that you have to be able to model.

So that would be hard.

So you'd probably need several simulated systems that can interact at these different temporal dynamics

or at least, uh, maybe it's like a hierarchical system

so, um, you can jump up or down the

the different temporal stages.

So can you avoid, I mean one of the challenges here is not

avoid simulating, for example, the, the

the quantum mechanical aspects of any of this

right?

You want to not over model.

You could skip ahead to just model the really high level things that get you a really good estimate of what's going to happen.

Yes.

So you, you got to make a decision when you're modeling any natural system what is the cutoff level of the granularity that you're going to model it to that then captures the dynamics that you're interested in.

So probably for a cell I, I would hope that would be the protein level

uh, and that one wouldn't have to go down to the atomic level.

Um, so, you know, but of course that's where AlphaFold stuff kicks in.

So that would be kind of the basis

and then you'd build these, um, uh

higher level simulations that, um, take those as building blocks and then you get the emergent behavior.

Apologize for the pothead questions ahead of time but

uh, will-  .

..

do you think, uh, we'll be able to simulate or model the origin of life?

So being able to simulate the first from

from non-living organisms the, the birth of a living organism.

I think that's, uh, one of the

of course one of the deepest and most fascinating questions.

Um, I love that area of biology.

You know, uh, there's people, like there's a great book by Nick Lane

one of the top, top experts in this area called The

The Ten Great Inventions of, of, of Evolution.

I think it's fantastic and it also speaks to what the great filters might be be- you know

prior or are they ahead of us.

I think, I think they're most likely in the past if you read that book

of how unlikely to go, you know

have any life at all and then single cell to multi-cell seems an unbelievably big jump that took like a billion years I think- Yeah.

.

..

and on earth to do, right?

So it shows you how hard it was

right?

 Bacteria were super happy for a very long time.

For a very long time before they captured mitochondria somehow

right?

I don't see why not, why AI couldn't help with that

some kind of simulation.

Again, it's again, it's a bit of a search process through a combinatorial space.

Here's like all the, you know, the chemical soup that

that you start with, the primordial soup that

you know, maybe was on earth near these hot vents

here's some initial conditions.

Can you, uh, generate something that looks like a cell?

So perhaps that would be a next stage after the Virtual Cell project is well how

how could you actually, um, something like that emerge from the chemical soup?

Well, I would love it if there was a Move 37 for the origin of life.

Yeah.

 I think that's one of the sort of great mysteries.

I think ultimately what we'll figure out is they're a continuum

there's no such thing as a line between non-living and living.

But if we can make that rigorous- Yes.

.

..

th- that the very thing from the bi- Big Bang to today

it's been the same process.

If we can break down that wall that we've constructed in our minds of the actual origin of

from non-living to living and it's not a line

that it's a continuum that connects physics and chemistry and biology.

Yeah.

There's no line.

I mean this is my whole reason why I worked on AI and AGI my whole life because I think it can be the ultimate tool to help us answer these kind of questions.

And I don't really understand why, um

you know, the average person doesn't think

like worry about this stuff more.

 Like how, how can we not have a good definition of life and non- and non- living and non-living and-  .

..

the nature of time and let alone consciousness and gravity and all these things.

It's, it's just and quantum mechanics weirdness.

It's just, to me it's, I've always had this

this sort of screaming at me in my face.

 The whole, and that scream is getting louder.

You know it's like how, what is going on here?

You know in, in, and I mean that in the deeper sense like in the

you know, the nature of reality which has to be the ultimate question- Yeah.

.

..

uh, that would answer all of these things.

It's sort of crazy if you think about it.

We can stare at each other and e- all these living things all the time we can inspect it with microscopes and take it apart

uh, almost down to the atomic level and yet we still can't answer that clearly- Yeah.

.

..

in a simple way, that question of how do you define living?

Yeah.

..

. it's kind of amazing.

Yeah.

Living, you can kind of talk your way out of thinking about

but, like, consciousness?

Like we have this very obviously subjective conscious experience

like we're at the center of our own world and it

it feels like something and then how, how

how are you not screaming-  Yeah.

.

..

at the mystery of it all?

Right.

We haven't.

..

I mean, but really, humans have been contending with the mystery of the world around them for a long

long.

..

There's a lot of mysteries, like what's up with the sun and

and the rain?

Yeah.

Like what's that about?

And then like last year, we had a lot of rain

and this year, we don't have rain.

Like what did we do wrong?

Humans have been asking that question - Yeah.

.

.

for a long time.

Exactly.

So we're quite.

..

I guess we've developed a lot of mechanisms to cope with this- Yeah.

.

..

uh, these deep mysteries that we can't fully.

..

we can see, but we can't fully understand

and we have to, have to just get on with daily life.

Yeah.

And, and, and we get.

..

we keep ourselves busy, right?

In a way that we keep ourselves distracted.

  I mean, weather is one of the most important questions of human history.

We still.

..

That's, that's the go-to small talk direction of-  Yes.

 .

..

of the weather.

Especially in England.

Yeah.

 And then it's.

..

Which is, you know, famously is an extremely difficult system to model.

Yeah.

And, uh, even that system, uh

uh, Google DeepMind has made progress on.

Yes.

We've.

..

Yeah.

We've created the, the best weather prediction systems in the world

and they're better than traditional fluid dynamics sort of systems that are usually calculated on massive supercomputers

takes days to calculate it.

Um, we've managed to model a lot of the weather dynamics with neural network systems

with our WeatherNext system and, again, it's interesting that those kinds of dynamics can be modeled even though they're very complicated

almost bordering on chaotic systems in some cases.

A lot of the interesting aspects of that

um, uh, can be modeled by these neural network systems

including very recently we had, you know

cyclone prediction of where, you know, paths of hurricanes might go.

Of course, super useful, super important for the world

and, and, and it's super important to do that very timely and very quickly and as well as accurately.

And, uh, I think it's a very promising direction

again, of, you know, simulating and

uh, uh, so that you can run forward predictions and simulations of very complicated real-world systems.

I should mention that, uh, I've got a chance in

uh, Texas to meet a community of folks called the Storm Chasers.

Yes.

And w- what's really incredible about them, I need to talk to them more

is they're extremely tech-savvy.

Mm-hmm.

Because what they have to do is they have to use models to predict where the storm is.

Yeah.

 So they're.

..

 It's this.

..

it's, it's this beautiful mix of, like

crazy- Yeah.

.

..

enough to, like, go into the eye of the storm- Yeah.

.

..

and, like, in order to protect your life and predict where the extreme events are going to be

they have to have increasingly sophisticated models of

uh, of weather.

Yeah.

Yeah.

It's a, it's a b- a beautiful balance of

like, being in it as living organisms and the

the cutting edge of science.

Um, they actually might be using, uh

DeepMind's system, so that's.

..

Yeah, they are.

Hopefully, they are.

And I'd, I'd love to join them on one of those trips.

 They look amazing, right?

That's great.

To actually experience it one time.

E- exactly.

Yeah.

And then also to experience the correct prediction- Yeah.

.

..

of where something will come- Yeah.

.

..

and how it's going to evolve.

It's incredible.

Yeah.

You've estimated that we'll have AGI by 2030.

Um, so there's interesting questions around that.

How will we actually know that we got there

uh, and, uh, what may be the move

quote, "Move 37" of AGI?

My estimate is sort of 50% chance by

in the next five years, so, you know

by 2030, let's say.

And, uh, so I think there's a good chance that that could happen.

Part of it is what, what is your definition of AGI?

Of course, people are arguing about that now and

and, uh, mine's quite a high bar and always has been of

like, can we match the cognitive functions that the brain has

right?

So we know our brains are pretty much general Turing machines

approximate, and of course, we created incredible modern civilization with our minds

so that sh- also speaks to how general the brain is.

And, um, for us to know we have a

a true AGI, we would have to

like, make sure that it has all those capabilities.

It isn't kind of a jagged intelligence where some things it's really good at

like today's systems, but other things it's really

uh, flawed at.

And, and that's what we currently have with today's systems

they're not consistent, so you'd want that consistency of intelligence across the board.

And then we have some missing, I think

capabilities, like sort of, uh, the true invention capabilities and creativity that we were talking about earlier

so you'd want to see those.

How you test that?

Um, I think you just test it.

One way to do it would be kind of brute force test of tens of thousands of cognitive tasks that- Mm-hmm.

.

..

um, you know, we know that humans can do

uh, and maybe also make the system available to

uh, a few hundred of the world's top experts

uh, the Terence Taus of each, each subject area

and see if they can find.

..

You know, give th- give them a month or two and see if they can find a

an obvious flaw in the system.

And if they can't, then I think you're

you're pretty, uh, you know, pretty.

..

you can be pretty confident we have a

a fully general system.

Maybe to push back a little bit, it seems like humans are really incredible as the

the intelligence improves across all domains to take it for granted.

Mm-hmm.

Uh, like you mentioned Terence Tau, uh

th- these brilliant experts, they might quickly

in a span of weeks, take for granted all the incredible things they can do and then focus in

"Well, ha ha, right there.

" You know, I, I consider myself a h- first of all

human.

Yeah.

 That's good.

Yeah.

 Uh, I identify as human.

Um,  the.

..

I.

..

You know, some people listen to me talk and they're like

"That guy is not good at talking, the stuttering

the.

..

" You know.

 So, like, e- even humans have obvious

across domains, limits, uh, even just outside of- Of course.

.

.

calc.

..

mathematics and physics and so on.

It.

..

I, I, I wonder if it will take something like a Move 37

so on the positive side- Yeah.

.

.

versus like a barrage of 10,000 cognitive tasks- Yeah.

.

.

where.

..

It'll be one or two where it's like- Yes.

.

..

holy shit, this is special.

So I think there are, exactly.

So I think there's the sort of blanket testing to just make sure you've got the consistency

but I think there are the sort of lighthouse moments

like the Move 37, that w- I would be looking for.

So one would be inventing a new conjecture or a new hypothesis about physics

like Einstein did.

So maybe you could even run the back test of that very rigorously

like l- have a cutoff of, knowledge cutoff of 1900 and then give the system everything that was

you know, that was written up to 1900 and then

and then see if it could come up with special relativity and general relativity

right, like Einstein did.

Mm-hmm.

That, that would be an interesting test.

Another one would be, can it invent a game like Go?

Not just come up with Move 37, a new strategy

but can it invent a game that's as deep

as aesthetically beautiful, as elegant as Go?

And those are the sorts of things I would be looking out for.

Uh, uh, a- and probably a system being able to do

uh, uh, several of those things, right?

For it to be very general, um

not just one domain.

And so I think that would be the signs

at least that I would be looking for

that we've got a system that's AGI level.

And then maybe to fill that out, you would also check the consistency

you know, make sure there's no holes in that system either.

Yeah, something like a, a new conjecture or scientific discovery

that would be a cool feeling.

Yeah.

That would be amazing.

So it's not, not just helping us do that

but actually coming up with something brand new.

And you would be in the room for that.

Exactly.

And so it would be like probably two or three months before announcing it.

Mm-hmm.

And you would just be sitting there trying not to tweet.

  Something like that, exactly.

It's like, what is this amazing new- Yeah.

.

..

you know, physics, uh, idea.

And then we'd probably check it with world experts in that domain- Yeah.

.

..

right, and validate it and kind of go through its workings.

And it, I guess it would be explaining its workings too.

Um, yeah, be an amazing moment.

Do you worry that we as humans, even expert humans like you

might miss it?

Might miss- Well, it may be c- pretty complicated

so it could be.

..

The analogy I give there is I don't think it will be

um, uh, uh, totally mysterious to the

to the best human scientists, but it may be a bit like

for example, in chess if I was to talk to Garry Kasparov or Magnus Carlsen and play a game with them and they make a brilliant move

I might not be able to come up with that move

but they could explain why afterwards that move made sense.

And we would be able to understand it to some degree.

Not to the level they do, but i- i- you know

if they were good at explaining, which is actually part of intelligence too

is being able to explain in a simple way that what you're thinking about

um, uh, I, I think that that would be very possible for the best human scientists.

But I wonder, maybe you can, you can educate me on this side of Go

I wonder if there's moves for Magnus or Garry where they at first will dismiss it as a bad move.

Yeah, sure.

There could be.

But then afterwards, they'll figure out with their intuition that

that this, why this works and then

and then, and then empirically.

..

The nice thing about games is, one of the great things about games is you can em- it's

it's a sort of scientific test.

Does it.

..

Do you win the game or not win?

And then, um, that tells you, okay

that move in the end was good.

That strategy was good.

And then you can go back and analyze that and

and, and, and, and explain even to yourself a little bit more why.

Explore around it.

And that's how chess analysis and things like that work.

So perhaps that's why my brain works like that

'cause I, I've been doing that since I was four and you're train- you know

tra- it's sort of hardcore training in that way.

But even, even now like when I generate code

there, there is this kind of nuanced fascinating con- contention that's happening where I might at first identify as a set of generated code is incorrect in

in some interesting nuanced ways, but then I'm always have to ask the question

is there a deeper insight here that, uh

that I'm the one who's incorrect?

Mm-hmm.

And th- that's going to.

..

As the systems get more and more intelligent

you're gonna have to contend with that.

It's like what, what, what do you m- is this a bug or a- Yes.

.

.

feature, what you just came up with.

Yeah, and they're gonna be pretty complicated to do

but of course it will be.

..

You could imagine also AI systems that are producing that code or whatever that is

and then human programmers looking at, but also not unaided

with the help of AI tools as well.

So it's gonna be kind of an interesting.

..

You know, d- maybe different AI tools to the ones- Yeah.

.

..

that they're more va- you know, mo- kind of monitoring tools to the ones that generated it.

So if we look at a AGI system

sorry to bring it back up, but AlphaEvolve.

Yeah.

Super cool.

So AlphaEvolve enables, on the programming side

something like recursive self-improvement, uh, potentially.

Like what.

..

If we can imagine what that AGI system

maybe not the first version, but a few versions beyond that

what does that actually look like?

Do you think it will be simple?

Do you think it will be something like a self-improving program and a simple one?

I mean, potentially that's possible, I would say.

Um, I'm not sure it's even desirable

because that's a kind of like hard take off scenario.

Yeah.

But, but you, y- these current systems like AlphaEvolve

# Chapter 5

..

that they're more va- you know, mo- kind of monitoring tools to the ones that generated it.

So if we look at a AGI system

sorry to bring it back up, but AlphaEvolve.

Yeah.

Super cool.

So AlphaEvolve enables, on the programming side

something like recursive self-improvement, uh, potentially.

Like what.

..

If we can imagine what that AGI system

maybe not the first version, but a few versions beyond that

what does that actually look like?

Do you think it will be simple?

Do you think it will be something like a self-improving program and a simple one?

I mean, potentially that's possible, I would say.

Um, I'm not sure it's even desirable

because that's a kind of like hard take off scenario.

Yeah.

But, but you, y- these current systems like AlphaEvolve

they have, you know, human in the loop deciding on various things.

They're separate hybrid systems that interact.

Uh, one could imagine eventually doing that end-to-end.

I don't see why that wouldn't be possible

but right now, um, you know, I think the systems are not good enough to do that in terms of coming up with the architecture of the code.

Um, and again, it's a little bit reconnected to this idea of coming up with a new conjectural hypothesis.

How.

..

Like, they, they're good if you give them very specific instructions about what you're trying to do.

Um, but if you give them a very vague high level instruction

that wouldn't work currently.

Like, uh, and I think that's related to this idea of like invent a game as good as Go

right?

Imagine that was the prompt.

That's, that's pretty underspecified.

And so the current systems wouldn't know, I think

what to do with that, how to narrow that down to something tractable.

And I think there's similar like, look

just make a better version of yourself, that's too

that's too unconstrained.

But we've done it in s- you know

in, and as you know with AlphaEvolve

like things like faster matrix multiplication.

Mm-hmm.

So when you, when you hone it down to a very specific thing you want

um, it's very good at incrementally improving that.

For sure.

But at the moment these are more like incremental improvements

sort of small iterations.

Whereas if, you know, i- i- if you wanted a big leap in

uh, understanding, you'd need a, you'd need a much larger

uh, advance.

Yeah, but it could also be sort of

to push back against hard take off scenario

it could be just a sequence of-.

..

um, incremental improvements, like matrix multiplication.

Like it has to sit there for days thinking how to incrementally improve a thing

and that it does so recursively.

And as you do more and more improvement

it'll slow down.

Right.

So there'll be like a- like a- the path to AGI won't be like a

a.

..

It'll be a gradual improvement over time.

Yes.

If it was just incremental improvements, that's how it would look.

So the question is, could it come up with a new leap

like the transformers architecture?

Yeah.

Like could it have done that back in 2017 when

you know, we did it and Brain did it?

And it's- it's not clear that- that these systems

something like AlphaFold wouldn't be able to do

make such a big leap.

So for sure these systems are good.

We have systems I think that can do incremental hill climbing.

Mm-hmm.

And that's a kind of bigger question about is that all that's needed from here or do we actually need one or two more

um, uh, big breakthroughs?

And can the same kind of systems provide the breakthroughs also?

So make it a bunch of S-curves.

Like incremental improvement, but also every once in a while

leaps.

Yeah, I don't think a- a- anyone has systems that can sh- have shown unequivocally those big leaps.

The- the- the.

..

Right?

We have a lot of systems that do the hill climbing of the S-curve that you're currently on.

Yeah.

And that would be the Move 37, is a leap.

Yeah, I think would be a leap.

Um, something like that.

Uh, do you think s- the scaling laws are holding strong on the pre-training

post-training, test time, compute?

Uh, do you, uh, on the flip side of that anticipate AI progress hitting a wall?

We certainly feel there's a lot more room just in the scaling

so, um, actually all steps, pre-training

post-training and inference time.

So, uh, there's sort of three scalings that are happening c- concurrently.

Um, and we.

..

A- again there, it's about how innovative you can be

and we, you know, we pride ourselves on having the broadest and

um, deepest research bench.

Uh, we have amazing, you know, incredible

uh, researchers and, uh, people like Noam Shazeer who

you know, came up with transformers and s- and Dave Silver

you know, who led the AlphaGo project and so on.

And, um, it's- it's- it's w- that research base means that if some new- new breakthrough is required

like an AlphaGo or transformers, uh, I would back us to be the place that does that.

So I actually quite like it when the terrain gets harder

right?

Because then it veers more from just engineering-  Yeah.

.

..

to- to true research, and, you know

re- or research plus engineering, and that's our sweet spot

and I- I think that's harder.

It's harder to invent things than to- than to

um, you know, fast follow.

And, um, so, you know, we don't know.

I would say it's a, it's kind of 50/50 whether new things are needed or whether the scaling the existing stuff is gonna be enough.

And so in true kind of empirical fashion

we're pushing both of those as hard as possible.

The new blue sky ideas and, you know

maybe about half our resources are on that

and then- and then, uh, scaling to the max the- the current- the current capabilities.

And, um, we're still seeing some, you know

fantastic progress on, uh, each different version of Gemini.

That's interesting the way you put it in- in terms of the deep bench

that if, uh, progress towards AGI is more than just scaling compute

and so the engineering side of the problem

and is more on the scientific side where there's breakthroughs needed

then you feel confident DeepMind is well, uh

Google DeepMind is well-positioned to- Yes.

.

..

ki- kick ass in that domain.

Well, I mean, if you look at the history of the last decade or 15 years- Yeah.

.

..

um, it's been, uh, you know

maybe, I don't know, 80, 90% of the breakthroughs that mo- that underpins modern AI field today was from

you know, originally Google Brain, Google Research and DeepMind

so yeah.

I would back that to continue hopefully.

  Uh, so on the data side

are you concerned about running out of high-quality data

especially high-quality human data?

I'm not very worried about that, partly because I think there's enough data

uh, on, and it's b- been proven to get the systems to be pretty good.

And this goes back to simulations again.

If you- do we have enough data to make simulations or so that you can create more synthetic data that are from the right distribution?

Obviously that's the key.

So you need enough real world data in order to be able to

uh, uh, create those kinds of generator

data generators.

And, um, I think that we're at that step at the moment.

Yeah, you've done a lot of incredible stuff on the side of science and biology.

Mm-hmm.

D- doing a lot with not so much data.

Yeah.

I mean, it's still a lot of data

but I guess enough to get off- To get that going.

Exactly.

Yeah.

Yeah.

It's.

..

Exactly.

Uh, how crucial is the scaling of compute to building AGI?

This is a question that's an engineering question.

It's a almost a geopolitical question- Mm-hmm.

.

..

because it also integrated into that is the supply chains and energy.

Yes.

A thing that you care a lot about

which is, um, potentially fusion.

Yes.

So innovating on the side of energy also.

Yeah.

Do you think we're gonna keep scaling compute?

I think so, for several reasons.

I think compute, there's- there's the amount of compute you have for training.

Uh, often it needs to be co-located

so actually even like, you know, uh

bandwidth constraints between data centers can affect that.

So it's- it's- it's, there's additional constraints even there.

And that- that's important for training obviously the largest models you can.

But there's also because now AI systems are in products and being used by billions of people around the world

you need a ton of inference compute now.

Um, and then on top of that

there's the thinking systems, the new paradigm

uh, of the last year that, uh

where they get smarter the longer amount of inference time you give them at test time.

So all of those things need a lot of compute

and I don't really see that slowing down.

Um, and, uh, as AI systems become better

they'll become more useful and there'll be more demand for them.

So both from the training side, the training side actually is- is only just one part of that

may even become the smaller part of- of what's needed-  yeah.

.

.

um, uh, uh, in the overall compute that- that's required.

Yeah, that's one sort of almost memey kind of thing

which is like the success and the incredible aspects of VO3.

 There's, uh.

..

People kind of make fun of, like

the more successful it becomes, you know

the servers are sweating.

Yes.

 Exactly.

They're melting.

To do inference.

 Yeah, yeah.

Exactly.

We did a little video of, of the se- of the servers frying eggs and things.

Yeah.

And, um, that's right.

And, and, and we're gonna have to figure out how to do that.

Um, there's a lot of interesting hardware innovations that we do.

As you know, we have our own TPU line and we're looking at

like, inference-only things, inference-only chips and how we can make those more efficient.

We're also very interested in building AI systems and we have done the help with energy usage.

So help, um, data center energy, like

for the cooling systems be efficient, um

grid optimization, um, and then eventually, things like helping with

uh, plasma containment fusion reactors.

We've done lots of work on that with Commonwealth Fusion and also

uh, one could imagine reactor design, um

and then material design, I think, is one of the most exciting new types of solar material

solar panel material, superc- room temperature superconductors has always been on my list of dream breakthroughs and

um, optimal batteries.

And I think a solution to any, you know

one of those things would be absolutely revolutionary for

you know, climate and energy usage.

And we're probably close, you know, again

in the next five years to having AI systems that can materially help with those problems.

If you were to bet.

..

Sorry for the ridiculous question.

Yeah.

But what, what is the main source of energy

uh, in, like, 20, 30, 40 years?

Do you think it's gonna be nuclear fusion?

I think fusion and solar are the two that I

I would bet on.

Um, solar, I mean, you know

it's the fusion reactor in the sky, of course.

And I think really, the, the problem there is

is, is batteries and transmission.

So, you know, as well as more efficient

more and more efficient solar material, perhaps eventually

you know, in space, you know, these kind of Dyson sphere type ideas.

And fusion, I think, is definitely doable

it seems, uh, if we have the right design of reactor and we can control the plasma and

uh, fast enough and so on.

And I think both of those things will actually get solved.

So we'll probably have at least.

..

Those are probably the two primary sources of renewable

clean, almost free, or perhaps free energy.

What a time to be alive.

If I, uh, traveled into the future with you

100 years from now, how much would you be surprised if we've passed a type I Kardashev scale civilization?

I would not be that surprised if there's a h- like a 100-year time scale from here.

I mean, I think it's pretty clear if we crack the energy problems in one of the ways we've just discussed

fusion or, or very efficient solar.

Um, then if energy is kind of free and renewable and clean

um, then that solves a whole bunch of other problems.

So for example, the water access problem goes away because you can just use desalination.

We have the technology, it's just too expensive.

So only, you know, uh, fairly wealthy countries like Singapore and Israel and so on

like, actually use it.

But, but if it was, uh, cheap

then ev- then, you know, all countries that have a coast could.

But also, you'd have unlimited rocket fuel.

You could just separate seawater out into hydrogen and oxygen using energy

and that's rocket fuel.

So, uh, combined with, you know

Elon's amazing self-landing rockets, then it could be like- it would sort of- like a bus service to

to space.

So that opens up, you know, incredible new resources and domains.

Uh, asteroid mining I think will become a thing and maximum human flourishing to the stars.

Like, that's what I, uh, dream about as well

is like Carl Sagan's sort of idea of bringing consciousness to the universe

waking up the universe.

And I, I think human civilization will do that in the full sense of time if we get AI right and

uh, and, and, and crack some of these problems with it.

Yeah, I wonder what it would look like if you're just

uh, tourists flying through space.

You would probably notice Earth.

..

Because if you solve the energy problem, you would see a lot of space rockets probably.

Mm-hmm.

So it would be like traffic  here in London- Yep.

.

..

but in space.

 Yes, exactly.

It's just a lot of rockets.

Yes.

And then you would probably see, floating in space

some kind of source of energy like solar- Yeah.

.

..

potentially.

So Earth would just look more, on the surface

more, um, technological.

And then, then you would use the power of that energy then to preserve the natural- Yes.

.

..

like, the rainforest and all that kind of stuff.

Exactly.

Because for the first time in, in human history

we wouldn't be, uh, resource constrained.

Mm-hmm.

And I think that could be amazing new era for humanity where it's not zero sum

right?

Mm-hmm.

I have this land, you don't have it.

Or if we take.

..

You know, if the tigers have their forest

then the, the local villagers can't.

..

What are they gonna use?

I, I, I think that this will help a lot.

No, it won't solve all problems because there's still other human

uh, foibles that will, will, will still exist

but it will at least remove one, I think

one of the big vectors which is scarcity of resources

you know, including land and raw materials and energy.

And, um, we know we should be.

..

Some of us call it, like, and others call it about this kind of radical abundance era where

um, there's plenty of resources to go around.

Of course, the next big question is making sure that that's fairly

you know, shared fairly, uh, and everyone in society benefits from that.

So there is something about human nature where I go.

..

You know, it's like , it's like Borat

like, "My neighbor.

" Like.

..

 Like, you start trouble.

We, we, we do start conflicts and that's why games throughout

as I'm learning actually more and more, even in ancient history

served the purpose of pushing people away from war- Yes.

.

.

actual hot war.

So maybe we can figure out increasingly sophisticated video games that pull us.

..

They, they give us that, uh- Visual.

Scratch the itch- Yeah.

.

..

of, like, conflict, whatever that is abo- about us

the human nature, and then avoid the actual hot wars that would come with increasingly sophisticated technologies because we're now.

..

We've long passed the stage where the weapons we're able to create can actually just destroy all of human civilizations.

Yeah.

So it's no longer.

..

Um, that's no longer a great way.

..

..

. to, uh, start shit with your neighbor.

It's better to play a game of chess and- Or football.

.

..

or football.

Or, or.

..

Yeah.

Yeah.

And I think.

..

I mean, I think that's what, why modern sport is so.

..

And I love football, watching it and

and I just feel like, uh.

..

And I used to play it a lot as well and it's

it's, it's, it's, it's very visceral and it's tribal- Mm-hmm.

.

..

and I think it does channel a lot of those energies into a.

..

Which I think is a kinda human need to belong to some

some group.

And, um, but into a, into a

into a fun way, a, a healthy way

and, and a not, a not destructive way

kinda constructive, uh, thing.

And I think going back to games again is I think they're originally why they're so great as well for kids to play things like chess is they're great little microcosm simulations of the world.

Mm-hmm.

They, they are simulations of the world too.

They're simplified versions of some real-world situation, whether it's poker or

or Go or chess, different aspects.

..

Or diplomacy.

Mm-hmm.

Different aspects of, of the real world.

And it allows you to practice at them too and

and 'cause, you know, how many times do you get to practice a massive decision moment in your life?

You know, what job to take, what university to go to.

You know, you get maybe, I don't know

a dozen or so key decisions one has to make

and you gotta make those as best as you can.

Um, and games is a kind of safe environment

repeatable environment, where you can get better at your decision-making process.

Um, and it maybe has this in- a- additional benefit of channeling some energies into

# Chapter 6

and, and a not, a not destructive way

kinda constructive, uh, thing.

And I think going back to games again is I think they're originally why they're so great as well for kids to play things like chess is they're great little microcosm simulations of the world.

Mm-hmm.

They, they are simulations of the world too.

They're simplified versions of some real-world situation, whether it's poker or

or Go or chess, different aspects.

..

Or diplomacy.

Mm-hmm.

Different aspects of, of the real world.

And it allows you to practice at them too and

and 'cause, you know, how many times do you get to practice a massive decision moment in your life?

You know, what job to take, what university to go to.

You know, you get maybe, I don't know

a dozen or so key decisions one has to make

and you gotta make those as best as you can.

Um, and games is a kind of safe environment

repeatable environment, where you can get better at your decision-making process.

Um, and it maybe has this in- a- additional benefit of channeling some energies into

uh, into more creative and constructive pursuits.

Well, I think it's also really important to practice

um, losing and winning.

Right.

Like losing is a really.

..

You know, that's why I love games.

That's why I love even, um, things like

uh, Brazilian jiu-jitsu- Yeah.

.

..

where you can get your ass kicked in a safe environment over and over.

It reminds you about the way.

..

about physics, about the way the world works

about sometimes you lose, sometimes you win.

You can still be friends with everybody.

Yeah.

But that, that feeling of losing, I mean

it's a weird one for us humans to

like, really, like, make sense of.

Like, that's just part of life.

That is a fundamental part of life is losing.

Yeah.

And I think in martial arts as I understand it

but also in things like, like chess

is a lo-.

..

At least the way I took it, it's a lot to do with self-improvement- Mm-hmm.

.

..

self-knowledge.

You know, the, "Okay, so I did this thing.

" It's not about really being the other person.

It's about maximizing your own potential.

If you do it in a healthy way

you learn to use victory and losses in a way.

Don't get carried away with victory- Yeah.

.

..

and, and think you're the just the best in the world.

Keep.

..

And, and, and the losses keep you humble and always knowing there's always something more to learn

there's always a bigger expert that you can mentor you.

You know, I think you learn that

I, I, I'm pretty sure, in martial arts and

and, and I think that's also, uh

the way that at least I was trained in chess.

And so in the same way, and it can be very hardcore and very important

and, of course, you wanna win, but you also need to learn how to deal with setbacks

uh, in a, in a healthy way that.

..

Um, and, and, and wire that

that feeling that you have when you lose something into a constructive thing of

"Next time, I'm gonna improve this," right?

Or, "get better at this.

" There is something that's a source of happiness

a source of meaning, that improvement step.

It's not about the winning or losing.

Yeah, it's the mastery.

Yeah.

There's nothing more satisfying in a way.

It's like, "Oh, wow, this thing I couldn't do before

now I can.

" And, and, and again, games and physical sports and

and mental sports, their wa- their ways of measuring

they're beautiful because you can measure that, that progress.

Yeah.

Right?

I mean, th- there's something about.

..

That is why I love role-playing games, like the

uh, number go up of, like, my-  Yes.

.

..

on the skill tree.

Exactly.

 Like literally, that is a source of meaning for us humans.

Whatever our- Yeah, we're quite, we're, we're quite addicted to this sort of-  Yeah.

These numbers going up and, uh, and

and- Yeah.

.

.

and, and, and maybe-  .

..

that's why we make games like that- Yeah.

.

..

because obviously that is something we're.

..

We're, we're hill-climbing systems ourselves, right?

Yeah, it's.

..

It would be quite sad if we didn't have- Yeah.

.

.

any mechanism by- Different color belts.

 Exactly.

All of the.

..

We do, we do this everywhere, right?

Where we just-  .

..

have this thing that it's great.

It's.

..

And, uh, I don't wanna dismiss that

that there is a source of deep meaning- Yeah.

.

..

as humans.

Uh, so one of the incredible stories on the business

on the leadership side is, um, what Google has

has done over the past year.

 So I, uh, I think it's fair to say that Google was losing on the LLM product side

uh, a year ago when Gemini won five

and now it's winning- Mm-hmm.

.

..

with Gemini 2.

5 and you took the helm and you led this effort.

What did it take to go from, let's say

quote-unquote, "losing" to, quote-unquote, "winning" in the

in, in the span of a year?

Yeah, well, firstly, it's absolutely incredible team that we have

you know, led by Koray and Jeff Dean and

and Oriol and the amazing team we have on Gemini

absolutely world-class.

So you can't do it without the best talent.

Um, and of course, you have.

..

You know, we have a lot of great compute as well

but then it's the research culture we've created- Mm-hmm.

.

..

right?

And basically coming together, both different groups in

in Google.

You know, there was Google Brain, world-class team

and, and then the old DeepMind, and pulling together all the best people and the best ideas and gathering around to make the absolute greatest system we could.

And it has been hard, um, but we're all very competitive

uh, and we, you know, love research.

This is so fun to do.

Um, and we've.

..

You know, it's great to see our trajectory.

It wasn't a given, but we're very pleased with

um, the, the.

..

where we are and the rate of progress is the most important thing.

So if you look at where we've come

two.

..

from two years ago to one year ago to now

you know, I think our, we call it relentless progress

along with relentless shipping of that progress, is

um, being very successful.

And, you know, um, it's unbelievably competitive

uh, the whole space, the whole AI space

with some of the greatest entrepreneurs and leaders

uh, and companies in the world all competing now because everyone's realized how important AI is.

Um, and it's very, you know, been pleasing for us to see that progress.

You know, Google's a gigantic company.

Uh, can you speak to.

..

..

. the natural things that happen in that case is the bureaucracy that emerges.

Like you want to be careful.

Like, you know, like, the- the- the natural kind of there's- there's meetings and there's- Yeah.

.

..

managers and that.

Like what- what are some of the challenges from a leadership perspective of breaking through that in order to

like you said, ship?

Like the amou- Yeah.

.

..

the number of products- Yeah.

.

..

Gemini-related products that's been shipped over the past year is just insane.

Right.

It is.

 Yeah, exactly.

That's- that's what relentlessness looks like.

Um, I think it's- it's a question of like any big company

you know, ends up having, uh, a- a lot of layers of management and things like that.

It's sort of the nature of how it works.

Um, but I still operate, and I was always operating with old DeepMind as a- as a startup still.

Mm-hmm.

Large one, but still as a startup.

And that's what we still act like today in- as- with Google DeepMind.

And acting with decisiveness and the energy that you get from the best smaller organizations.

And we try to get the best of both worlds where we have this incredible billions of users

surfaces, uh, incredible products that we can power up with our AI and our- and our research.

Um, and that's amazing.

And you can.

..

You know, there's very few places in the world you can get that.

Do incredible world-class research on the one hand

and then plug it in and- and improve billions of people's lives the next day.

Uh, that's a pretty amazing combination.

And we're continually fighting and cutting away bureaucracy to allow the research culture and the relentless shipping culture to flourish.

And I think we've got a pretty good balance whilst being responsible with it

you know, as you have to be

uh, as a large company and also

uh, with a number of, you know

uh, huge product surfaces that we have.

Uh, so funny thing you mentioned about like the- the surface with a billion.

I- I had a conversation with a guy named

um, brilliant guy, uh, here at the British Museum called Irvin Finkel.

He's a world expert at cuneiforms, which is a ancient writing on tablets.

Yep.

And he doesn't know about ChatGPT or Gemini.

Mm-hmm.

He doesn't even know anything about AI.

Mm-hmm.

But his first encounter with this AI is AI mode on  Google.

Yes.

Yes.

He's like, "Is that what you're talking about?

" Yeah.

"This AI mode?

"   And then, you know, it's just inc- it's just a reminder that there's a large part of the world that doesn't know about this AI thing.

Yeah.

 And then- I know, it's funny

because if you live on, uh, X and Twitter and I mean

it's sort of, at least my feed

it's all AI.

And- and there's certain places where, you know

in the Valley and certain pockets where everyone's just

all they're thinking about is AI.

But a lot of the normal world hasn't- hasn't come across it yet

but- And that's a great responsibility to w- the- their first interaction- Yeah.

.

..

on the- the- the grand scale of the rural India or an- anywhere across the world

like you get to- Right.

Right.

And we want it to be as good as possible.

And in a lot of cases, it's just under the hood

powering, making something like maps or search work better.

And, um, and e- ideally for a lot of those people

it should just be seamless.

It's just new technology that makes their lives more

you know, productive and- and- and helps them.

A bunch of folks on the Gemini product and engineering teams spoken extremely highly of you on another dimension that I almost didn't e- even expect

because I kind of th- think of you as the like deep scientist in caring about these big research scientific questions.

But they also said you're a great product guy.

Like how to create a thing that a lot of people would use and enjoy using.

Mm-hmm.

So can you maybe speak to what it takes to create a- a- AI-based product that a lot of people would enjoy using?

Yeah.

Well, I mean, again, that comes back from my game design days where I used to design games for millions of gamers.

People forget about that.

I've- I've had experience with cutting edge technology in product.

Right.

That- that- that- that is how games was in the '90s.

And so I love actually the combination of cutting edge research and then being applied in a product and- and to power a new experience.

And so, um, I think it's the same skill really of- of

you know, imagining what it would be like to use it viscerally

um, and having good taste, coming back to earlier.

The same thing that's useful in science, um

I think is- is- can also be useful in- in product design.

And, um, I- I've just had a very

you know, always been a sort of multidisciplinary person

so I don't see, uh, the boundaries really between

you know, arts and sciences or product and research.

It's- it's a continuum for me.

I mean, I only work on.

..

I like working on products that are cutting edge.

I wouldn't be able to, you know

have cutting edge technology under the hood.

I wouldn't be excited about them if they were just run-of-the-mill products.

Um, so it requires this invention, creativity cap- capability.

Mm-hmm.

What are some specific things you kind of learned about when you

um, even on the LLM side, you're interacting with Gemini.

Yeah.

You're like, this doesn't feel like the layout

the- the interface- Yeah.

.

..

maybe the trade-off between the latency, like how- how to present to the user

how long to wait- Mm-hmm.

.

..

and how that waiting is shown or the reasoning capabilities.

There's some interesting things, because like you said

it's a very cutting edge.

We don't know- Yeah.

.

..

how to present it- how to present it correctly.

So is there some specific things you've- you've learned?

I mean, i- it's such a fast evolving space.

We're evaluating this all the time.

But where we are today is that you want to continually simplify things

um, the int- whether that's the interface or- or- Simplify

yeah.

.

.

the inter- uh, the- what you build on top of the model.

You kind of want to get out of the way of the model.

The model train is coming down the track and it's improving unbelievably fast

this relentless progress we talked about earlier.

You know, you look at 2.

5 versus 1.

5 and it's just a gigantic improvement.

And we expect that again for the future versions.

And so the models are becoming more capable.

So you've got.

..

The interesting thing about the design space in- in- in today's world

these AI first products is you've got to design not for what the thing can do today

the technology can do today, but in a year's time.

So you actually have to be a very technical product person

because, uh, you've got to kind of have a good intuition for and feel for

okay, that thing that I'm dreaming about now can't be done today

but is the research track on schedule to basically intercept that in six months or a year's time?

So you kind of got to intercept where this highly changing technology is going

as well as the, um, uh, uh

new capabilities are coming online all the time that you- you didn't realize before that can allow like deep research to work

or now we've got video generation.

What do we do with that?

Um, this multimodal stuff, you know, is it.

..

One question I have is, is it really going to be the current UI that we have today

these textbox chats?

It seems very unlikely give- once you think about these super multimodal

uh, uh, systems.

Shouldn't it be something more like Minority Report where you're- Mm-hmm.

.

..

you're sort of vibing with it in a- in a co- in a kind of collaborative way

right?

It seems very restricted today.

I think we'll look back on today's interfaces and products and systems as quite archaic in maybe in a

just a couple of years.

So I think there's a lot of sp- space actually for innovation to happen on the product side as well as the- the research side.

And then we were offline talking about this keyboard is the- the open question is how

when, and how much will we move to audio?

..

. as a primary way of interacting with the machines around us

versus typing stuff.

Yeah.

I mean, typing is a very low bandwidth way of doing it

even if you're a very fast, you know

typer.

And I think we're gonna have to start utilizing other devices

whether that's smart glasses, you know, i- uh

audio, earbuds, um, and eventually maybe some sorts of neural devices

where we can increase the, the input and the output bandwidth to something

uh, you know, maybe 100X of what it is today.

I think that, you know, underappreciated art form is the interface design because I think you cannot unlock the power of the intelligence of a system if you don't have the right interface.

Mm-hmm.

The interface is really the way you unlock its power.

Yeah.

And it's such an interesting question of how to do that.

Yeah.

So how, how.

..

You would think, like, getting out of the way is a real art form.

Yes.

You know, it's the sort of thing that I guess Steve Jobs always talked about

right?

It's simplicity, beauty, and elegance that we want

right?

And we're not the.

..

nobody's there yet, in my opinion, and that's what I would like us to get to.

Again, it sort of speaks to like Go again

right, as a game, the most elegant

beautiful game.

Can you.

..

You know, the.

..

Uh, uh, can you make an interface as beautiful as that?

And actually, I think we're gonna enter an era of

uh, AI-generated interfaces that are probably personalized to you so it fits the way that you.

..

your aesthetic, your feel, the way that your brain works.

And, um, and, and, and the AI kind of generates that depending on the task

you know?

It feels like that's probably the direction we'll end up in.

Yeah, 'cause some people are power users and they want every single parameter on the screen- Right.

.

..

everything, e- everything based like perhaps me with a keyboard- Yeah.

.

..

keyboard-based navigation, I like to have shortcuts for everything

and some people like the minimalism of- Just hide all of that complexity

yeah, exactly.

.

..

c- completely.

Yeah.

Uh, well, I'm glad you have a Steve Jobs mode in you as well.

.

This is great.

Einstein mode, Steve Jobs mode.

Um, all right, let me try to trick you into answering a question.

When, when will Gemini 3 come out?

.

Is it before or after GTA 6?

.

The world waits for both.

And what does it take to go from 2.

5 to 3.

0, because it seems like there's been a lot of releases of 2.

5 which are already leaps in performance?

Mm.

So what, what does it even mean to go to a new version?

Is it e- about performance?

Is this about a completely different flavor of an experience?

Yeah.

Well, so the way it works with our different

uh, version numbers is we.

..

you know, we try to collect.

..

So maybe it takes, you know, roughly six months or something to

to do a new, uh, kind of full run and the full productization of a new version.

And during that time, lots of new interesting research

iterations, and ideas come up.

Mm-hmm.

And we sort of collect them all together that

you know, you could imagine the last six months worth of interesting ideas on the architecture front

um, maybe it's on the data front

it's like many different possible things, and we collect

package that all up, test which ones are likely to be useful for the next iteration

and then bundle that all together, and then we start the new

you know, giant hero training run.

.

Right?

And, and then, uh, and then of course

that gets monitored.

Uh, and then at the end, then there's the.

..

o- of the pre-training, then there's all the post-training

there's many different ways of doing that, different ways of patching it

so there's a whole experimenting phase there, which you can also get a lot of gains out

and that's where you see the version numbers usually referring to the base model

the pre-train model- Mm-hmm.

.

.

and then the interim versions of 2.

# Chapter 7

you know, you could imagine the last six months worth of interesting ideas on the architecture front

um, maybe it's on the data front

it's like many different possible things, and we collect

package that all up, test which ones are likely to be useful for the next iteration

and then bundle that all together, and then we start the new

you know, giant hero training run.

.

Right?

And, and then, uh, and then of course

that gets monitored.

Uh, and then at the end, then there's the.

..

o- of the pre-training, then there's all the post-training

there's many different ways of doing that, different ways of patching it

so there's a whole experimenting phase there, which you can also get a lot of gains out

and that's where you see the version numbers usually referring to the base model

the pre-train model- Mm-hmm.

.

.

and then the interim versions of 2.

5, you know, and the different sizes

and the different little, uh, additions, they're often

uh, patches or post-training ideas that can be done afterwards

uh, off the same basic architecture.

And then of course, on top of that

we also have different sizes, Pro and Flash and Flash Lite

that are often distilled from the biggest ones

you know, the Flash model from the Pro model.

And that means we have a range of different choices

uh, if you are the developer, of do you wanna pri- prioritize performance or speed

right- Mm-hmm.

.

.

and cost?

And we like to think of this Pareto frontier well of

of, you know, on the one hand

uh, the y-axis is, you know, like performance

and then the, the, the x-axis is

you know, cost or latency and, and speed

uh, basically, and we, we have models that completely define the frontier.

So whatever your trade-off is that you want as an individual user or as a

as a developer, you should find one of our models satisfies that constraint.

So behind the version changes, there is a big hero run.

Yes.

And then there's, uh, just an insane complexity of productization

then there's the distillation of the different sizes along that Pareto front

and then as, uh, with each step you take

you realize there might be a cool product

these side quests.

Yes, exactly.

But.

..

And then you also don't want to take too many side quests because then you have a million versions of a million products- Yes

yes, precisely.

.

..

and it's very, it's very unclear.

Yeah.

But you also get super excited 'cause it's super cool.

Yeah.

Like how does even.

..

You look at Veo's, v- very cool.

Yeah.

How does it fit into the bigger thing

right?

Yes, exactly.

Yeah.

Exactly.

And then you're constantly.

..

this process of converging upstream we call it

you know, ideas from the, from the product surfaces or

or, or from the post-training, and, and even further downstream

and that.

..

you, you kind of upstream that into the

the core model training for the next run.

Mm-hmm.

Right?

So then the main model, the main Gemini track becomes more and more general.

Mm-hmm.

And eventually, you know, AGI.

.

.

One hero run at a time.

Yes, exactly.

.

A few hero runs later.

Uh, yeah.

So sometimes when you release these new versions

or every version really, uh, are benchmarks

um, productive or counterproductive for showing the performance of a model?

You need them, and, and I.

..

but it's important that you don't overfit to them

right?

So they shouldn't be the end, the be-all and end-all.

So there's, there's LM Arena, or it used to be called LMSYS

that's one of them that turned out sort of organically to be one of the

the main ways people like to test these systems

at least the chatbots.

Um, obviously there's loads of academic benchmarks on.

..

from, from the test, uh, mathematics and coding ability

general language ability, science ability, and so on

and then we have our own internal benchmarks that we care about.

It's a kind of multi-objective, y- you know

optimization problem, right?

You w- you don't wanna be good at just one thing.

We're trying to build general systems that are good across the board.

And you try and make no-regret, uh, improvements.

So where you're improving, like- Yeah.

.

.

you know, coding, uh, but it doesn't reduce your performance in other areas

right?

So that's the hard part because you, you can.

..

Of course, you could put more coding data in or you could put more

um, I don't know, gaming data in.

But then does it make worse your language

uh, system or, or, uh, in

in your translation systems and other things that you care about?

So it's.

..

You've got to kind of continually monitor this l- increasingly larger and larger suite of

of benchmarks.

And also there's, uh, when you stick them into products

these models, you also care about the direct usage and the direct stats and the signals that you're getting from the end users

whether they're coders or, or, or the average person using

uh, using the chat interfaces.

Yeah, because ultimately you want to measure the usefulness

but it's so hard to convert that into a number.

Right.

It's, it's really vibe-based benchmarks- Yes.

.

..

across a large number of users and it's hard to know.

And I.

..

It would be just terrifying to me to.

..

You know you have a much smarter model

but it's just something vibe-based.

It's not, not, not quite working.

That's just sc- scary because.

..

And everything you just said, it has to be smart and useful across so many domains.

So you, you get super excited because it's all of a sudden solving programming problems it'd never been able to solve before

but now it's crappy at poetry or something.

Yes.

Right.

And it's just.

..

I don't know.

That's a stressful.

..

That's so difficult, um, because- To balance

yeah.

.

..

to balance and because you can't really trust the benchmarks- Mm-hmm.

.

..

you really have to trust the end users.

Yeah.

And then other things that are even more esoteric come into play like

um, you know, the style of the persona of the

the, the system, you know, how it.

..

You know, is it verbose?

Is it succinct?

Is it humorous?

You know, and they.

..

And different people like different things.

Mm-hmm.

So, um, you know, it's very interesting.

It's almost like cutting edge part of psychology research or pers- personality research.

You know, I used to do that in my PhD

like five factor personality.

What do we actually want our assistants to be like?

And different people will like different things as well.

So these are all just sort of new problems in product space that I don't think have ever really been tackled before but

um, we're going to sort of ha- rapidly have to deal with now.

 I think it's a super fascinating space

developing the character of the thing.

Yeah.

And in so doing, it puts a mirror to ourselves

what are the kind of things, um

that we like?

Because prompt engineering allows you to control a lot of those elements but can the product

uh, make it easier for you to

uh, control the different flavors of those experiences

the different characters that you interact with?

Yeah, exactly.

So.

..

So what's the probability of Google DeepMind winning?

Well, I don't see it as sort of winning.

I mean, I think we need to.

..

I think winning is the wrong way to look at it given how important and consequential what it is we're building.

So funnily enough, I don't.

..

I try not to view it like a game or competition even though that's a lot of my mindset.

It's, it's about st-.

..

In my view, all of us have.

..

those of us at the leading edge, uh

have a responsibility to, um, steward this unbelievable technology that could be used for incredible good but also has risks

um, steward it safely into the world for the benefit of humanity.

That's always, um, what I've, um

uh, uh, I dreamed about and what we've always tried to do.

And I hope that's what eventually the community

maybe the international community, will rally around when it becomes obvious that as we get closer and closer to

to AGI that, um, that's what's needed.

I agree with you.

I think that's beautifully put.

You've said that, um, you talk to and are on good terms with the leads of some of these

uh, labs as the competition heats up.

Uh, how hard is it to maintain sort of those relationships?

It's been okay so far.

I try to pride myself in being, uh

collaborative.

I'm a collaborative person.

Research is a collaborative endeavor.

Science is a collaborative endeavor, right?

It's all good for humanity in the end if you cure incredible

you know, terrible diseases and you come up with an incredible cure.

This is net win for humanity.

And the same with energy, all of the things that I'm interested in

in, in helping solve with AI.

So I just want that technology to exist in the world and be used for the right things and

and, and the kind of.

..

The benefits of that, the productivity benefits of that being shared for every.

..

the benefit of everyone.

So I try to maintain good relations with all the leading lab

uh, people.

They have very interesting characters, many of them

as you might expect.

Yeah .

Um, but yeah, I'm on good terms

I, I hope with pretty much all of them and

uh, I, I think that's gonna be important when

when things get even more serious than they are now

uh, that there are those communication channels.

Mm-hmm.

And, uh, that's what will facilitate, uh

cooperation or collaboration if that's what rec- is required

especially on things like safety.

Yeah, I hope there's some collaboration on stuff that's

uh, sort of less high stakes and in so doing serves as a mechanism for maintaining friendships and relationships.

So for example, I think the internet would love it if you and Elon somehow collaborated on creating a video game

that kind of thing.

Right .

That.

..

I think that enables camaraderie and good terms.

And also you two are legit gamers so it's just fun to- Yeah.

.

..

fun to create something.

Yeah, that would be awesome and we've talked about that in the past and it may be a cool thing that

that, you know, we can do.

And I agree with you, it'd be nice to have

um, kind of side projects in a way where

where w- one can just lean in to the collaboration aspect of it and it's a sort of

uh, win-win for both sides and it's

um.

..

And it kind of builds up that, that

that, uh, collaborative muscle.

I see the scientific endeavor as that kind of side project for humanity.

Yeah.

And I, I think Deep.

..

Google DeepMind has been really pushing that.

Uh, I would love it if.

..

to see other labs do more scientific stuff and then collaborate because it just seems like easier to collaborate on the big scientific questions.

I agree and, uh, I would love to see.

..

A lot of people.

..

All of the other labs talk about science but I think we're really the only ones- Yeah.

.

..

using it for science and doing that and that's why projects like AlphaFold are so important to me and I think to our mission is to show

uh, how AI can.

..

This.

..

You know, be clearly used in a very concrete way for the benefit of humanity and

and also we spun out companies like Isomorphic off the back of AlphaFold to do drug discovery and it's going really well and build sort of.

..

You know, you can think of build additional AlphaFold type

type systems to go into chemistry space to help accelerate drug design.

And the examples I think we need to show

uh, and society needs to understand are where AI can bring these huge benefits.

Well, from the bottom of my heart, thank you for pushing the scientific efforts forward w- with rigor

with fun, with humility, all of it.

I just love to see it.

And still talking about P equals NP, I mean

it's just incredible.

So I love it.

Uh, there are- there- there's been 

uh, seemingly a war for talent.

Some of it is meme, I don't know.

Um, what do you think about Meta buying up talent with huge salaries and- and the heating up of this battle for talent?

And I- I should say that I think a lot of people see DeepMind as a really great place to do

uh, cutting edge work- Mm-hmm.

.

..

for the reasons that you've outlined is- Yeah.

.

.

like there's this vibrant scientific culture.

Yeah.

Well, look, uh, of course, um

you know, there's a strategy that- that Meta is taking right now.

I think that, um, from my perspective at least

I think the people that are real, uh

believers in the mission of AGI and what it can do and understand the real consequences

both good and bad from that and what's- what that responsibility entails

I think they're mostly doing it to be

like myself, to be on the frontier of that research.

So, you know, they can help influence the way that goes and steward that technology safely into the world.

And, you know, Meta right now are not at the frontier

maybe they'll- they'll manage to get back on there

and, um, you know, it's probably rational what they're doing from their perspective because they're behind and they need to do something.

But I think, um, there's more important things than- than just money.

Of course, one has to pay, you know

people at market rates and all of these things

and that continues to go up.

 Um, but as pro- And- and- and I was expecting this because more and more people are finally realizing

leaders or companies, what I've always known for 30 plus years now

which is that AGI is the most important technology probably that's ever gonna be invented.

So in some senses it's- it's rational to be doing that.

But I also think there's a much bigger question.

I mean, people in AI these days are very well paid.

You know, I- I remember when we were starting out back in 2010

you know, I didn't even pay myself for a couple of years 'cause it wasn't enough money.

We couldn't raise any money.

And these days interns are being paid, you know

the amount-  .

..

that we raised as our first entire seed round.

So it's pretty funny.

And I remember the days where we used to- I used to have to- to work for free and p- and almost pay my own way to do an internship

right?

Now it's all the other way around.

But that's just how it is.

It's the new world.

And, um, but I think that, you know

we've been discussing like what happens post-AGI and energy systems are solved and so on

what is even money going to mean?

So I think, uh, you know, and the economy and- and we're gonna have much bigger issues to work through and how does the economy function in that world and companies.

So I think, you know, it's a little bit

uh, of a side issue about, uh

uh, salaries and things of like that today.

Yeah, when you're facing such gigantic consequences and- and g- gigantic fascinating scientific questions

for sure.

Right.

Which may be only a few years away

so.

So on a practical sort of pragmatic sense

uh, if we zoom in on jobs and can look at programmers

because it seems like AI systems are currently doing incredibly well at programming

and increasingly so.

So a lot of people that, uh

program for a living, love programming, are worried they will lose their jobs.

How worried should they be, do you think?

And what's the right way to, uh

sort of adjust to the new reality and ensure that you survive and thrive as a human in the programming world?

Well, it's interesting that programming, and it's again counterintuitive to what we thought

uh, years ago maybe, that some of the skills that we think of as harder skills are turned out maybe to be the easier ones for various reasons.

But, you know, coding and math because you can create a lot of synthetic data and verify if that data's correct.

Mm-hmm.

So b- because of that nature of that

it's easier to make things like synthetic data to train from.

Um, it's also an area, of course

we're all interested in 'cause we- as programmers

right?

To help us, um, get faster at it and more productive.

So I think the- for the next era

like the next five, 10 years, I think what we're gonna find is people who are kind of embraced these technologies become almost at one with them

um, whether that's in the creative industries or the technical industries

will become sort of superhumanly productive, I think.

So the great programmers will be even better but they'll be even 10x even what they are today.

And because there you'll be able to use their skills to utilize the- the tools to the maximum

uh, you know, exploit them to the maximum.

And, um, so I think that's what we're gonna see in the next domain.

Um, so that's gonna cause quite a lot of change

right?

And so that's coming.

A lot of people benefit from that.

So I think one example of that is if coding becomes easier

um, m- it becomes available to many more creatives to do more.

Uh, and, uh, but I think the top programmers will still have huge advantages as terms of specifying

going back to specifying what the architecture should be

the question should be how to guide these

um, uh, coding assistants in a way that's useful

you know, check whether the code they produce is good.

So I think there's plenty of, um

uh, headroom there for the foreseeable, you know

next few years.

So I think there's- th- there's several interesting things there.

One is there's a- a lot of imperative to just get better and better consistently of using these tools so that you're- that you're riding the wave of the improvement- improving models- Yes.

.

..

versus like competing against them.

Yeah.

But s- sadly, but that's the- the nature of- of life on Earth.

Um, there could be a huge amount of value to certain kinds of programming at the cutting edge

and less value to other kinds.

For example, it could be like, you know

front end- Mm-hmm.

.

.

web design might, uh, be more amenable to-.

..

to, to, as you, as you mentioned

to generation- Hmm.

.

..

uh, by AI systems.

It may be, for example, game engine design or something like this- Yeah.

.

.

or backend design or, or guiding systems in high performance situations

# Chapter 8

versus like competing against them.

Yeah.

But s- sadly, but that's the- the nature of- of life on Earth.

Um, there could be a huge amount of value to certain kinds of programming at the cutting edge

and less value to other kinds.

For example, it could be like, you know

front end- Mm-hmm.

.

.

web design might, uh, be more amenable to-.

..

to, to, as you, as you mentioned

to generation- Hmm.

.

..

uh, by AI systems.

It may be, for example, game engine design or something like this- Yeah.

.

.

or backend design or, or guiding systems in high performance situations

high performance programming type of design decisions.

That might be extremely valuable.

Mm-hmm.

But it will shift- Yeah.

.

..

where the humans are needed most and that's scary for people to address.

Yeah, I can.

..

I think that's right.

The, the.

..

A- any time where there's a lot of disruption and change.

You know, and we've had this.

It's not just this time.

We've had this in many times in human history with the internet

um, mobile, but before that was the Industrial Revolution.

Um, and it's gonna be one of those eras where there will be a lot of change.

I think there will be new jobs we can't even imagine today

just like the internet created.

And then those people with the right skillsets to ride that wave will become incredibly

uh, valuable.

Right?

Those skills.

But maybe people will have to relearn or adapt a bit

uh, their current skills.

And it's the, the thing that's gonna be harder to deal with this time around is the.

..

I think what we're gonna see is something like probably 10 times the impact the Industrial Revolution had and

but 10 times faster as well.

Right?

So instead of 100 years, it takes 10 years.

And so that's gonna make.

..

You know, it's like 100X, uh, the impact and the speed combined.

So that's what's I think gonna make it more difficult for society to

to, to deal with and, it's g- there's a lot to think through

and I think we need to be discussing that right now.

And I, I, you know, I encourage top economists in the world and philosophers to start thinking about

um, uh, how should, is society gonna be affected by this and what should we do

including things like, um, u- you know

uh, universal basic provision or something like that.

Where a lot of the, um, inc- increased productivity

uh, gets shared out and distributed, uh

to society.

Um, and maybe in the form of surface- services and other things

where if you want more than that, you still go and get some incredibly rare skills and things like that

um, and, and make yourself unique.

Um, but, uh, uh, but there's a basic provision that is provided.

And if you think of government as technology

there's also interesting questions, not just in economics but just politics.

How do you design a system that's responding to the rapidly changing times such that you can represent the different pain that people feel from the different groups?

And how do you reallocate resources in a way that

um, addresses that pain and represents the hope and the pain and the fears of different people

uh, in a way that doesn't lead to division?

Because politicians are often really good at sort of fueling the division and using that to get elected.

The other m- c- defining the other and then saying- Yeah.

.

.

"That's bad," and so based on that.

I think that's often counterproductive to leveraging a rapidly changing technology

how to, uh, help the world flourish.

So we almost, uh, need to improve our political s- systems as well rapidly if you think of them as a technology.

Definitely.

And I think, I think we'll need new governance

uh, structures, institutions probably, to help with this transition.

So I think political philosophy and political science is gonna be key

uh, to that.

But I think the number one thing, first of all

uh, is to create more abundance of resources

right?

Mm-hmm.

Then there's the qu- So that's the number one thing.

Increase productivity, get more resources.

Maybe eventually get out of the zero-some situation.

Then the second question is how to use

uh, those resources and distribute those resources.

But yeah.

You can't do that without having that abundance first.

Uh, you mentioned to me, uh, the book The Maniac

uh, by Benjamin Libetut.

A book on, uh, first of all

about you.

There's a bio about you.

Um, - It's strange, yeah.

It's unclear.

Yes, sure.

 It's unclear how much is fiction, how much is reality.

Um, but I think the central figure there is

uh, John von Neumann.

I would say it's a haunting and beautiful exploration of madness and genius

and let's say the double-edge, uh, sword of discovery.

And, you know, for, um, people who don't know

John von Neumann is a kind of legendary mind.

He contributed to quantum mechanics.

He was on the Manhattan Project.

He is widely considered to be the father of

or pioneer of the modern computer and AI and so on.

So there's.

..

Many people say he's, like, one of the smartest humans ever.

Mm-hmm.

Which is fascinating.

And what's also fascinating is as a person who saw nuclear science and physics become the atomic bomb

so you, you got to see ideas become a thing that has a huge amount of impact on the world.

He also foresaw the same thing for computing.

Yeah.

He s- he.

..

And that's the, a little bit, again

beautiful and haunting aspect of the book, um

than taking a leap forward and looking at this Lee Sedol

AlphaZero, AlphaGo, AlphaZero big moment that maybe John v- von Neumann's thinking was brought to

to, to, to reality.

So I, I, I guess the question is

um, what do you think if you got to hang out with John von Neumann

uh, now?

What, what would he say-  .

..

about what's going on?

Well, that would be an amazing experience.

You know, he's a f- a fantastic mind and

and I also love the way he, he spent a lot of his time at Princeton at the Institute of Advanced Study.

It's a very special place for thinking.

And, um, it's amazing at how much of a polymath he was and the

the spread of things he helped invent, including

of course, the von Neumann architecture that all the modern computers are based on.

And, um, he had amazing foresight.

I think he would've loved where we are today

and he would've, um.

..

I think he would've really enjoyed AlphaGo- Okay.

 .

..

being a, you know, games- Yes.

He also did game theory.

I think he foresaw a lot of what would happen with learning machine systems that

that, that are kind of grown, I think he called it

rather than programmed.

I'm not sure how even.

..

Maybe he wouldn't even be that surprised.

There's the fruition of what I think he already foresaw in the 1950s.

I wonder what advice he would give.

He got to see- Hmm.

.

..

the building of the atomic bomb with the Manhattan Project.

Yeah.

I'm sure there is interesting stuff that maybe is not talked about enough

maybe some bureaucratic aspect, maybe the influence of politicians

maybe, maybe not enough of picking up the phone and talking to people that are called enemies- Hmm.

.

..

by the said politicians.

There might be something like deep wisdom that we just may have lost from that time

actually.

Yeah, I'm sure, I'm sure there is.

I mean, I've t- we, we, you know

studied.

..

I read a lot of books for that time as well

chronical time, um, and some brilliant people involved.

But I, I agree with you.

I think maybe there needs to be more dialogue and understanding.

Um, I hope we can learn from those

those times.

I think the difference here is that the AI has so many.

..

it's a multi-use technology.

Obviously, we're trying to do things like the.

..

like solve, you know, all diseases, um

uh, help with energy, uh, and scarcity

these incredible things.

This is why all of us and, and myself

you know, I worked, started on this journey 30 plus years ago.

And, um, but of course there are risks too.

And probably von Neumann, my guess is he foresaw both.

And, um, and I think he sort of said

I think is to his wife, that

that, that it would be a.

..

this is.

..

computers would be even more impactful in the world.

And as we just discussed, you know

I think that's right.

I think it's going to be ten times at least of the industrial revolution.

So I think he's right.

So I think he would have been, I imagine

fascinated by, uh, uh, uh, where we are now.

And I think one of the.

..

maybe you can correct me, but one of the takeaways from the book is that reason

as, uh, said in the book, mad dreams of reason

is not enough for guiding humanity as we build these super powerful technology

that there's something else.

I mean, there's also like a religious component.

Hmm.

Whatever God, whatever religion gives, it give.

..

it pulls at something in the human spirit that raw

cold reason doesn't give us.

And I, I agree with that.

I think we need to approach it with whatever you want to call it

the, uh, spiritual dimension or humanist dimension.

It doesn't have to be to do with religion

right?

But this idea of, of a soul

what makes us human, this spark that we have

perhaps it's to do with consciousness when we finally understand that

um, I think that has to be at the heart of the endeavor.

Mm-hmm, mm-hmm.

Um, and technology, I've always seen technology as the enabler

right?

The tools the- that enable us to, to flourish and to understand more about the

the world.

And I, I'm sort of with Feynman on this

and he used to always talk about science and art being companions

right?

You can understand it from both sides, the beauty of a flower

how beautiful it is, and also understand why the colors of the flower evolved like that

right?

That just makes it more beautiful that, that

that just the intrinsic beauty of the flower.

And, and I've always sort of seen it like that.

And maybe, you know, in the Renaissance times

the great discovers then, like people like da Vinci

you know, they were.

..

I don't think he saw any difference between science and art

uh, and perhaps religion, right?

They were.

..

everything was.

..

it's just part of being human and, um

being inspired about the world around us.

And that's what I.

..

the philosophy I try to take.

And, um, one of my favorite philosophers is Spinoza

and I think he combined that all very well

you know, this idea of trying to understand the universe and understanding our place in it

and that was his kind of way of understanding religion.

And I think that's quite beautiful.

And for me, every.

..

all of these things are related, interrelated

the technology and, um, what it means to be human.

And, uh, I think it's very important though that we remember that as.

..

when we're immersed in the technology and the

the research.

I think a lot of researchers that I see in

in our field are a little bit too narrow and only understand the technology.

And I think also that's why it's important for

um, this to be debated at.

..

by society at large.

And I'm very supportive of things like this

the AI summits that will happen and governments understanding it

and I think that's one good thing about the chatbot era and the product era of AI is that everyday person can actually feel and

and interact with cutting edge AI and, and

and feel, feel it for themselves.

Yeah, because they, they force the technologist to have the human conversation.

Yeah, for sure.

Yeah.

That's the hopeful aspect of it, like you said

it's a dual use technology that we're forcefully integrating the entire humanity into it by.

..

into the discussion about AI- Mm-hmm.

.

..

because ultimately AI, AGI will be used for things that states use technologies for

which is, uh, conflict and so on.

And the more we, uh, uh, integrate humans into this picture by having  chats with them

the more it will guide- Yeah, be able to adapt.

..

society will be able to adapt to these technologies like we've always done in the past with

with, uh, the incredible technologies we've invented in the past.

Do you think there will be something like a Manhattan Project where

um, there will be an escalation of the power of this technology and states in their old way of thinking will try to use it as weapons technologies and there will be this kind of escalation?

I hope not.

Um, I think that would be, uh

very dangerous to do, and I think also

um, you know, not the right use of the technology.

I, I hope we'll end up with more

something more collaborative if needed, like more like a

like a CERN project- Yeah.

.

..

you know, where, um, it's research focused and the best minds in the world come together to carefully complete the final steps and make sure it's responsibly done before

you know, like, uh, deploying it to the world.

We'll see.

I mean, it's difficult with the current geopolitical climate

I think, uh, to, to see cooperation

but things can change and, um, I think at least on the scientific level

it's important for the researchers to, to

to, to keep in touch and, and

and keep close to each other on.

..

at least on those kinds of topics.

Yeah, and I, I personally believe on the education side and

um, immigration side, it would be great if both directions

uh, people from the West-.

..

China and China back.

I mean, there is some like family human aspect of people just intermixing- Yeah.

.

..

and thereby those ties grow strong.

So you can't sort of divide against each other this kind of old-school way of thinking and so uh multi uh multicultural multidisciplinary research teams working on scientific questions that's like the hope.

Don't, don't let the warm, the leaders that are warmongers divide us.

I think science is the ultimately really beautiful connector.

Yeah.

Science has always been uh I think quite uh a very collaborative endeavor.

Mm-hmm.

And you know scientists know that it's, it's

it's a collective endeavor as well and we can all learn from each other.

So perhaps it could be a vector to get a bit of cooperation.

What's your ridiculous question?

What's your PDOOM?

Probability that human civilization destroys itself.

Well look, I-I don't have a  it's a

you know, I don't have a PDOOM number.

The reason I don't is because I think it would imply a level of precision that is not there.

So like I don't know how people are getting their PDOOM numbers.

I think it's a kind of a little bit of a ridiculous notion because um what I would say is

it's definitely non-zero and it's probably non-neg- negligible.

So that in itself is pretty sobering and my-my view is it's just hugely uncertain

right?

What this technology is going to be able to do?

How fast are they going to take off?

How controllable are they going to be?

Some things may turn out to be and hopefully like way easier than we thought

right?

Um, but it may be there's some really hard um uh-uh problems that are harder than we guess today.

And I think uh we don't know that for sure and so in under those conditions of a lot of uncertainty but huge stakes both ways.

You know on the one hand we, we could solve all diseases

energy problems, the, the, the scarcity problem and then travel to the stars and conquerors of the stars and maximum human flourishing.

On the other hand, is this sort of PDOOM scenarios.

So given the uncertainty around it and the importance of it

it's clear to me the only rational sensible approach is to proceed with cautious optimism.

So we want the outc- we want the um eh the benefits of course uh and uh all of the

the amazing things that AI can bring and actually I would be really worried for humanity if I if given the o-other challenges that we have

climate, dise- you know aging, resources, all of that.

If I didn't know something like AI was coming down the line- Mm-hmm.

.

.

right?

How would we solve all those other problems?

I think it's hard.

Um, so I think we, you know it could be amazingly transformative for good.

Um, but on the other hand you know there are these risks that we know are there but we can't quite quantify.

So the, the best thing to do is to use the scientific method to do more research to try and uh more precisely define those risks and of course address them.

Um, and I think that's what we're doing.

I think there probably needs to be uh ten times more effort on that than there is now as we're getting closer and closer to the

to the, to the AGI line.

# Chapter 9

You know on the one hand we, we could solve all diseases

energy problems, the, the, the scarcity problem and then travel to the stars and conquerors of the stars and maximum human flourishing.

On the other hand, is this sort of PDOOM scenarios.

So given the uncertainty around it and the importance of it

it's clear to me the only rational sensible approach is to proceed with cautious optimism.

So we want the outc- we want the um eh the benefits of course uh and uh all of the

the amazing things that AI can bring and actually I would be really worried for humanity if I if given the o-other challenges that we have

climate, dise- you know aging, resources, all of that.

If I didn't know something like AI was coming down the line- Mm-hmm.

.

.

right?

How would we solve all those other problems?

I think it's hard.

Um, so I think we, you know it could be amazingly transformative for good.

Um, but on the other hand you know there are these risks that we know are there but we can't quite quantify.

So the, the best thing to do is to use the scientific method to do more research to try and uh more precisely define those risks and of course address them.

Um, and I think that's what we're doing.

I think there probably needs to be uh ten times more effort on that than there is now as we're getting closer and closer to the

to the, to the AGI line.

What would be the source of worry for you more?

Would it be human caused or AI, AGI caused?

Yeah.

Humans abusing the technology versus AGI itself through mechanism that you've spoken about which is fascinating deception or this kind of stuff- Yes.

.

..

getting better and better and better secretly and then escapes.

I think they, they operate over different time scales and they're equally important to address.

So there's just the, the, the common garden or variety of like you know bad actors using new technology uh in this case general purpose technology and repurposing it for harmful ends.

And that's a huge uh risk and I think there has a lot of complications because generally you know I'm in huge favor of open science and open source and in fact we did it with all our science projects like AlphaFold and all of those things uh for the benefit of

of the scientific community.

Um, but how does one restrict bad actors access to these powerful systems whether they're individuals or even rogue states uh and but enable access at the same time to good actors to maximally build on top of?

It's a pretty tricky problem that there's I've not heard a clear solution to.

So there's the bad actor use case problem and then there's obviously uh as the systems become more agentic and closer to AGI um and more autonomous

how do we ensure the guard rails and they stick to what we want them to do uh and under our control?

Yeah I tend to maybe my mind is limited worry more about the humans

so the bad actors.

Mm.

And there it could be uh in part how do you not put destructive technology in the hands of bad actors but another part from again geopolitical technology perspective how do you reduce the number of bad actors in the world?

That's, that's also an interesting human problem.

Yeah.

It's a hard problem.

I mean look we, we can um maybe also use the technology itself to help um uh early warning on some of the bad actor use cases right?

Whether that's bio or nuclear or whatever it is like AI could be potentially helpful there as long as the AI that you're using is itself reliable

right?

So it's a sort of interlocking problem and that's what makes it very tricky and

and again it may require some agreement internationally at least between China and the- and the US of some uh basic standards

right.

I have to ask you about the book The Maniac.

There's this, this the hand of God moment

Lee Sedol's move 78- Mm.

.

..

that perhaps  the last time a human did a move of sort of pure human genius.

And beat AlphaGo or, like, broke its brain.

Yes.

If, sorry to anthropomorphize, but it's an interesting moment because I think in so many domains it will keep happening.

Yeah.

It's a special moment and, you know

it was great for Lee Sedol and, you know

I think it's in a way they were sort of inspiring each other.

We as a team were inspired by Lee Sedol's brilliance and nobleness

and then maybe he got inspired by, you know

what AlphaGo was doing to then conjure this incredible inspirational moment.

It's all, you know, captured very well in the

in the documentary about it.

It is.

And, um, I think that'll continue in many domains where there's this

at least for the, for the, again

for the foreseeable, uh, future of, like

yeah, the hu- humans bringing in their ingenuity

um, and asking the right question, let's say

uh, and then utilizing these tools, uh

in a way that, um, then cracks a problem.

Yeah.

What.

..

As the AI becomes smarter and smarter, one of the interesting questions we can ask ourselves is what makes humans special?

It does feel, um, perhaps biased that we humans are deeply special.

I don't know if it's our intelligence.

Uh, it could be something else that

that other thing that's outside the mad dreams of reason.

I think that's what I've always imagined, uh

when I was a kid and starting on this journey of

like, um, I was of course fascinated by things like consciousness.

Did, did a neuroscience PhD to look at how the brain works

especially imagination and memory.

I focused on the hippocampus.

And it's sort of gonna be interesting.

I always thought the best way.

..

Of course one can come philosophize about it and have thought experiments and maybe even do actual experiments like you do in neuroscience on

on real brains, but in the end I always imagine that building AI

a kind of intelligent artifact, and then comparing that to the human mind and seeing what the differences were

uh, would be the best way to uncover what's special about the human mind

if indeed there is anything special.

And I suspect there probably is, but it's gonna be hard to de-.

..

You know, I think this journey we're on will help us

uh, understand that and define that.

And, you know, there may be a difference between carbon-based substrates that we are and silicon ones when they process information.

You know, one of the best definitions I like of

of, of consciousness is it's the way information feels when we process it

right?

 Yeah.

Um, it could be.

I mean, it doesn't help.

..

It's not a very helpful scientific explanation- Right.

.

..

but I think it's kind of interesting intuit- intuitive one.

And, um, and so, you know

on this, this, this journey, this scientific journey we're on

we'll, I think, um, help uncover that mystery.

Yeah.

What I cannot create, I do not understand.

That's, uh, somebody you deeply admire, Richard Feynman

like you mentioned.

You also reach, um, for the, the Wigner's dreams of universality that he saw in constrained domains

but also broadly generally in, in mathematics and so on and so on.

Mm-hmm.

So many aspects on which you're pushing towards.

Not to start trouble at the end, but

uh,  Roger Penrose.

Yes.

Okay.

  So, uh, you know, do

do you think consciousness.

..

There's this hard problem of consciousness, how information feels.

Um, do you think consciousness, first of all

is a computation?

And if it is, if it's information processing

like you said everything is- Mm-hmm.

.

..

is it something that could be modeled by a classical computer?

Yeah.

Or is it a quantum mechanical in nature?

Well, look, Penrose is an amazing thinker

one of the greatest of the modern era

and he, we've had a lot of discussions about this.

Of course, we cordially disagree, which is

you know, I, I feel like, um.

..

I mean, he collaborated with a lot of good neuroscientists to see if he could find mechanisms for quantum mechanics behavior in the brain and they.

..

Uh, to my knowledge, they haven't found anything

um, convincing yet.

So my betting is there is.

..

is.

..

that, that, that it's mostly, you know

it is just classical computing that's going on in the brain

which suggests that all the phenomena, uh

are modelable or mimickable by a classical computer.

But we'll see.

You know, there, there may be this final mysterious things of the feeling of consciousness

the qualia, these kinds of things that philosophers debate where it's unique to the substrate.

We may even come towards understanding that when.

..

if we do things like Neuralink and, and o- uh

have neural interfaces to the AI systems, which I think we probably will eventually

um, maybe to keep up with the AI systems.

Uh, we might actually be able to feel for ourselves what it's like to compute on silicon

right?

So, um, and maybe that will tell us.

Uh, so I think-  Yeah.

.

.

it's, it's gonna be interesting.

And I, I had a debate once with the late Daniel Dennett about why do we think each other are conscious?

Okay, so it's for two reasons.

One is you're exhibiting the same behavior that I am.

So that's one thing.

Behaviorally, you seem like a conscious being

if I am.

But the second thing, which is often overlooked

is that we're all running on the same substrate.

So if you're behaving in the same way and we're running on the same substrate

it's most parsimonious to assume you're feeling the same experience that I'm feeling.

But with a AI our that's on silicon

we won't be able to rely on the second part.

Even if it exhibits the first part, the behavior looks like a behavior of a conscious being

it might even claim it is, um

but we.

..

but, but we wouldn't know how it actually felt.

Um, and it probably couldn't know we.

..

what we felt.

At least in the first stages.

Maybe when we get to super intelligence and the technologies that builds

perhaps we'll, we'll be able to, um

bridge that.

No, I mean, that's a huge test for radical empathy is to empathize with a different substrate.

Right.

Exactly.

 I mean- We never had to confront that before.

Yeah.

Yeah.

So maybe, maybe through brain-computer inter- interfaces

be able to truly empathize what it feels like to be a computer.

To compute- Well, for information to be computed not on a carbon system.

I mean, that's d- deeply excite.

..

I mean, some people kind of think about that with plants

with other life forms, which are different.

Yes, it could be.

Exactly.

Sim- similar substrate, but d- d- sufficiently far enough-.

..

on the, uh, evolutionary tree.

Yup.

That it's- requires a radical empathy, but to do that with a computer.

..

I mean, no, we sort of- there are animal studies on this of like- of course higher animals like

you know, killer whales and dolphins and dogs and

and monkeys.

You know, they have some- and elephants.

You know, they have some aspects certainly of consciousness

right, even though they're not- might not be that- that- that smart on an IQ sense.

So it's a- we can already empathize with that and maybe even some of our systems one day.

Like we built this thing called Dolphin Gemma

you know, which can- we- have one- a version of our system was trained on dolphin and whale sounds

and maybe we'll be able to build a- an interpreter or translator at some point

which would be pretty cool.

What gives you hope for the future of human civilization?

Well, what gives me hope is, I think our almost limitless ingenuity

first of all.

I think the best of us and the best human minds are incredible.

Um, and, you know, I love l- w- you know

meeting and watching, uh, any human that's the top of their game

whether that's sport or science or art.

You know, it's- it's- it's just nothing more wonderful than that

seeing them in their element, in flow.

Um, I think it's almost limitless.

You know, our brains are general systems

intelligent systems.

So, I think it's almost limitless what we can potentially do with them.

And then the other thing is our extreme adaptability.

I think it's gonna be okay in terms of- there's gonna be a lot of change

but the- but look where we are now with our- effectively our hunter-gatherer brains.

How is it we can, you know

we can c- cope with the modern world

right?

F- flying on planes.

..

 .

..

doing podcasts.

..

 Yeah.

.

..

you know, playing computer games and virtual simulations.

Yeah.

I mean, it's already mind-blowing given that our mind was- was developed for

you know, hunting buffalos on the- on the tundra.

And- and so, w- I think this is just the next step and

and- and it's actually kind of interesting to see how h- h- society has already adapted to this mind-blowing AI technology.

..

Yeah.

.

..

we have today already.

Yeah.

It's sort of like, "Oh, I talk to chatbots.

"  Totally fine.

Like- And it's, uh, very possible that this very podcast activity

which I'm here for, will be completely replaced by AI.

 Well.

..

I'm very replaceable and I'm r- waiting for it.

Not to the level that you can do it

Lex, I don't think.

Ah, thank you.

That's-  That's what we humans do to each other.

Yes.

 We complement.

Exactly.

All right.

And, uh, I'm, uh, deeply grateful for us humans to have this c- uh

infinite capacity for curiosity, adaptability, like you said

and also compassion and ability to love.

..

Exactly.

.

..

all of those human things.

All the things that are deeply human.

Well, this is a huge honor, Demis.

You're one of the truly special humans in the world.

Uh, thank you so much for doing what you do and for talking today.

Oh, thank you very much, Lex.

Thanks for listening to this conversation with Demis Hassabis.

To support this podcast, please check out our sponsors in the description and consider subscribing to this channel.

And now, let me answer some questions and try to articulate some things I've been thinking about.

If you would like to submit questions, including in audio and video form

go to lexfrumman.

com/ama.

I got a lot of amazing questions, thoughts

and requests from folks.

I'll keep trying to pick some, uh

randomly and comment on it at the end of every episode.

I got a note on May 21st this year that said

"Hi Lex.

20 years ago today, David Foster Wallace delivered his famous 'This is water' speech at

uh, Kenyon College.

What do you think of this speech?

" Well, first, I think this is probably one of the greatest and most unique commencement speeches ever given.

But of course I have many favorites, including the one by Steve Jobs.

And David Foster Wallace is one of my favorite writers and one of my favorite humans.

There's a tragic honesty to his work, and it always felt as if he was engaging in a- a constant battle with his own mind

and the writing, his writing, were kind of his notes from the front lines of that battle.

Now, on to the speech.

Let me quote some parts.

There's of course the parable of the fish and the water that goes

"There are these two young fish swimming along and they happen to meet an older fish swimming the other way

who nods at them and says, 'Morning

boys.

How's the water?

' And the two young fish swim on for a bit

and then eventually one of them looks over at the other and goes

'What the hell is water?

'" In this speech, David Foster Wallace goes on to say

"The point of the fish story is merely that the most obvious important realities are often the ones that are hardest to see and talk about.

Stated as an English sentence, of course

this is just a banal platitude, but the fact is that in the day-to-day trenches of adult existence

banal platitudes can have a life or death importance

or so I wish to suggest to you in this dry and lovely morning.

" I have several takeaways from this parable and the speech that follows.

First, I think we must question everything

and in particular the most basic assumptions about our reality

our life, and the very nature of existence

and that this project is a deeply personal one.

In some fundamental sense, nobody can really help you in this process of discovery.

The call to action here, I think

from, uh, David Foster Wallace, as he puts it

is to, quote, "To be just a little less arrogant

to have just a little more critical awareness about myself and my certainties

because a huge percentage of the stuff that I tend to be automatically certain of is

it turns out, totally wrong and deluded.

" All right, back to me, Lex speaking.

Second takeaway is that the central spiritual battles of our life are not fought on a

uh, mountaintop somewhere at a meditation retreat.

But it is fought in the mundane moments of daily life.

Third takeaway is that we too easily give away our time and attention to the multitude of distractions that the world feeds us

the insatiable black holes of attention.

David Foster Wallace's call to action in this case is to be deeply aware of the beauty in each moment

# Chapter 10

or so I wish to suggest to you in this dry and lovely morning.

" I have several takeaways from this parable and the speech that follows.

First, I think we must question everything

and in particular the most basic assumptions about our reality

our life, and the very nature of existence

and that this project is a deeply personal one.

In some fundamental sense, nobody can really help you in this process of discovery.

The call to action here, I think

from, uh, David Foster Wallace, as he puts it

is to, quote, "To be just a little less arrogant

to have just a little more critical awareness about myself and my certainties

because a huge percentage of the stuff that I tend to be automatically certain of is

it turns out, totally wrong and deluded.

" All right, back to me, Lex speaking.

Second takeaway is that the central spiritual battles of our life are not fought on a

uh, mountaintop somewhere at a meditation retreat.

But it is fought in the mundane moments of daily life.

Third takeaway is that we too easily give away our time and attention to the multitude of distractions that the world feeds us

the insatiable black holes of attention.

David Foster Wallace's call to action in this case is to be deeply aware of the beauty in each moment

and to find meaning in the mundane.

I often quote David Foster Wallace in his advice that

"The key to life is to be un-borable

" and I think this is exactly right.

Every moment, every object, every experience, when looked at closely enough

contains within it infinite richness to explore.

And since, uh, Demis Hassabis of this very podcast episode and I are such fans of Richard Feynman

allow me to, uh, also quote Mr.

Feynman on this topic as well.

Quote, "I have a friend who's an artist and has sometimes taken a view which I don't agree with very well.

He'll hold up a flower and say, 'Look how beautiful it is

' and I'll agree.

Then he says, 'I, as an artist

can see how beautiful this is, but you

as a scientist, take this all apart and it becomes a dull thing.

' And I think that's kind of nutty.

First of all, the beauty that he sees is available to other people

and to me too, I believe.

Although I may not be quite as refined aesthetically as he is

I can appreciate the beauty of a flower.

At the same time, I see much more about the flower than he sees.

I can imagine the cells in there, the complicated actions inside which also have beauty.

I mean, it's not just beauty at this dimension

at one centimeter.

There's also beauty at the smaller dimensions, the inner structure.

Also, the processes.

The fact that the colors in the flower evolved in order to attract insects to pollinate it is interesting.

It means that the insects can see the color.

It adds a question.

Does this aesthetic sense also exist in lower forms?

Why is it aesthetic?

All kinds of interesting questions which the science knowledge only adds to the excitement

the mystery, and the awe of a flower.

It only adds.

" All right, back to, uh, David Foster Wallace's speech.

He has a great story in there that I particularly enjoy.

It goes.

..

There are these two guys sitting together in a bar in the remote Alaskan wilderness.

One of the guys is religious, the other is an atheist.

And the two are arguing about the existence of God with that special intensity that comes after about the fourth beer.

And the atheist says, "Look, it's not like I don't have actual reasons for not believing in God.

It's not like I haven't ever experimented with the whole God and prayer thing.

Just last month, I got caught away from the camp in that terrible blizzard

and I was totally lost, and I couldn't see a thing

and it was 50 below.

And so I tried it.

I fell to my knees in the snow and cried out

'Oh God, if there is a God

I'm lost in this blizzard and I'm gonna die if you don't help me.

'" And now back in the bar, the religious guy looks at the atheist

all puzzled.

"Well, then you must believe now," he says.

"After all, there you are, alive.

" The atheist just rolls his eyes.

"No, man.

All that happened was a couple of Eskimos happened to be wandering by and showed me the way back to the camp.

" All this, I think, teaches us that everything is a matter of perspective

and that wisdom may arrive if we have the humility to keep shifting and expanding our perspective on the world.

Thank you for allowing me to talk a bit about David Foster Wallace.

He's one of my favorite writers, and he's a beautiful soul.

If I may, one more thing I wanted to briefly comment on.

I find myself to be in this strange position of getting attacked online often from all sides

including being lied about, sometimes through selective misrepresentation

but often through downright lies.

I don't know how else to put it.

This all breaks my heart, frankly, but I've come to understand that it's the way of the internet and the cost of the path I've chosen.

There's been days when it's been rough on me mentally.

It's not fun being lied about, especially when it's about things that are usually

for a long time, have been a source of happiness and joy for me.

But again, that's life.

I'll continue exploring the world of people and ideas with empathy and rigor

wearing my heart on my sleeve as much as I can.

For me, that's the only way to live.

Anyway, a common attack on me is about my time at MIT and Drexel

two great universities I love and have tremendous respect for.

Since a bunch of lies have accumulated online about me on these topics

to a sad, and at times hilarious degree

I thought I would once more state the obvious facts about my bio for the small number of you who may care.

TL;DR, two things.

First, as I say often, including in a recent podcast episode that somehow was listened to by many millions of people

I proudly went to Drexel University for my bachelor's

master's, and doctorate degrees.

Second, I am a research scientist at MIT and have been there in a paid research position for the last 10 years.

Allow me to elaborate a bit more on these two things now

but please skip if this is not at all interesting.

So like I said, a common attack on me is that I have no real affiliation with MIT.

The accusation, I guess, is that I'm falsely claiming an MIT affiliation because I taught a lecture there once.

Nope, that accusation against me is a complete lie.

I have been at MIT for over 10 years in a paid research position from 2015 to today.

To be extra clear, I'm a research scientist at MIT working in LIDS

the Laboratory for Information and Decision Systems, in the College of Computing.

For now, since I'm still at MIT

you can, uh, see me in the directory and on the various lab pages.

I have indeed given many lectures at MIT over the years

a small fraction of which I posted online.

Teaching, for me, always has been just for fun and not part of my research work.

I personally think I suck at it, but I have always learned and grown from the experience.

It's like Feynman spoke about, if you want to understand something deeply

it's good to try to teach it.

But like I said, my main focus has always been on research.

I published many peer-reviewed papers that you can see in my Google Scholar profile.

For my first four years at MIT, I worked extremely intensively

most weeks were 80 to 100-hour workweeks.

After that, in 2019, I still kept my research scientist position

but I split my time taking a leap to pursue projects in AI and robotics outside MIT

and to dedicate a lot of focus to the podcast.

As I've said, I've been continuously surprised just how many hours preparing for an episode takes.

There are many episodes of the podcast for which I have to read

write and think per 100, 200 or more hours across multiple weeks and months.

Since 2020, I have not actively published research papers.

Just like the podcast, I think it's something that's a serious full-time effort.

But not publishing and doing full-time research has been eating at me

because I love research, and I love programming and building systems that test out interesting technical ideas

especially in the context of human-AI or human-robot interaction.

I hope to change this in the coming months and years.

What I've come to realize about myself is

if I don't publish or if I don't launch systems that people use

I definitely feel like a piece of me is missing.

It legitimately is a source of happiness for me.

Anyway, I'm proud of my time at MIT.

I was and am constantly surrounded by people much smarter than me

many of whom have become lifelong colleagues and friends.

MIT is a place I go to escape the world

to focus on exploring fascinating questions at the cutting edge of science and engineering.

This, again, makes me truly happy, and it does hit pretty hard on a psychological level when I'm getting attacked over this.

Perhaps I'm doing something wrong.

If I am, I will try to do better.

In all this discussion of academic work, I hope you know that I don't ever mean to say that I'm an expert at anything.

In the podcast and in my private life

I don't claim to be smart.

In fact, I often call myself an idiot

and mean it.

I try to make fun of myself as much as possible

and in general, to celebrate others instead.

Now, to talk about Drexel University, which I also love

am proud of, and am deeply grateful for my time there.

As I said, I went to Drexel for my bachelor's

master's, and doctorate degrees in computer science and electrical engineering.

I've talked about Drexel many times, including

as I mentioned, at the end of a recent podcast

the Donald Trump episode, funny enough, that was listened to by many millions of people

where I answered a question about graduate school and explained my own journey at Drexel and how grateful I am for it.

If it's at all interesting to you, please go listen to the end of that episode or watch the related clip.

At Drexel, I met and worked with many brilliant researchers and mentors from whom I've learned a lot about engineering

science, and life.

There are many valuable things I gained from my time at Drexel.

First, I took a large number of very difficult math and theoretical computer science courses.

They taught me how to think deeply and rigorously

and also how to work hard and not give up

even if it feels like I'm too dumb to find a solution to a technical problem.

Second, I programmed a lot during that time

mostly C, C++.

I programmed robots, optimization algorithms, computer vision systems

wireless network protocols, multimodal machine learning systems

and all kinds of simulations of physical systems.

This is where I really developed a love for programming

including, yes, Emacs and the Kinesis Keyboard.

Uh, I also, during that time, read a lot.

I played a lot of guitar, wrote a lot of crappy poetry

and, uh, trained a lot of, uh

in judo and jujitsu, which I cannot sing enough praises to.

Jujitsu humbled me on a daily basis throughout my 20s

and it still does to this very day whenever I get a chance to train.

Anyway, I hope that the folks who occasionally get swept up in the chanting online crowds that want to tear down others don't lose themselves in it too much.

In the end, I still think there's more good than bad in people

but we're all, each of us, a mixed bag.

I know I am very much flawed.

I speak awkwardly.

I sometimes say stupid shit.

I can get irrationally emotional.

I can be too much of a dick when I should be kind.

I can lose myself in a biased rabbit hole before I wake up to the bigger

more accurate picture of reality.

I'm human, and so are you, for better or for worse.

And I do still believe we're in this whole beautiful mess together.

I love you all.

