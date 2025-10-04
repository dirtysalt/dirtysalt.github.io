# Chapter 1

the following is a conversation with jim keller his second time in the podcast

 jim is a legendary microprocessor

 architect and is widely seen as one of the greatest engineering minds of the computing age

 in a peculiar twist of space-time in our simulation

 jim is also a brother-in-law of jordan peterson

 we talk about this and about computing artificial intelligence

 consciousness

 and life

 quick mention of our sponsors athletic greens all-in-one nutrition drink brooklyn and sheetz expressvpn

 and belcampo

 grass-fed meat click the sponsor links to get a discount and to support this podcast

 as a side note let me say that jim is someone who on a personal level

 inspired me to be myself

 there was something in his words on and off the mic

 or perhaps that he even paid attention to me at all that almost told me

 you're all right kid

 a kind of pat on the back that can

 make the difference

 between a mind that flourishes

 and a mind that is broken down by the cynicism of the world

 so i guess that's just my brief few words of thank you to jim

 and in general

 gratitude for the people who have given me a chance on this podcast

 in my work and in life

 if you enjoy this thing subscribe on youtube review on apple podcast follow on spotify

 support on patreon or connect with me on twitter alex friedman

 and now here's my conversation

 with jim keller

 what's the value and effectiveness of theory versus engineering this dichotomy in building

 good software or hardware systems

 well it's good designs both

 i guess that's pretty obvious

 but engineering do you mean you know reduction of practice of known methods

 and then science is the pursuit of discovering things that people don't understand

 or solving unknown problems

 definitions are interesting here but i was thinking more in theory constructing models

 that kind of generalize about how things work

 and engineering is

 like actually

 building stuff the pragmatic like okay we have these nice models

 but how do we actually get things to work maybe

 economics

 is a nice example

 like economists have all these models of how the economy works and how different

 policies will have an effect

 but then there's the actual

 okay let's call it engineering of like actually deploying the policies

 so computer design is almost all engineering

 and reduction of practice is known message now

 because of the complexity of the computers we built

 you know you could think you're well we'll just go write some code

 and then we'll verify

 it and we'll put it together

 and then you find out that the combination of all that stuff is complicated

 and then you have to be inventive to figure out how to do it

 right so that's that's definitely happens a lot

 and then

 every so often some big idea happens

 but it might be one person

 and that idea is in what in the space of engineering or is it

 in the space

 well i'll give you an example

 so one of the limits

 of computer

 performance

 is branch predictions

 so

 and there's there's a whole bunch of ideas about how good you could predict the branch

 and people said there's a limit to it it's an asthmatic

 curve

 and somebody came up with a better way to do branch prediction

 it was a lot better

 and he published a paper on it and every computer in the world now uses it

 and it was one idea

 so the the engineers who build branch prediction hardware

 were happy to drop the one kind of training array and put it in another one

 so it was it was a real idea

 and branch prediction is is one of the key problems underlying

 all of sort of the lowest level of software it boils down to branch prediction

 boils down to uncertainty

 computers

 are limited by you know single thread computers limited by two things

 the

 predictability of the path of the branches and the predictability of the locality

 of data

 so we have predictors that now predict both of those pretty well

 yeah so memory is you know a couple hundred cycles away

 local cache is couple cycles away

 when you're executing fast virtually all the data has to be in the local cache

 so a simple program says

 you know add one to every element in array

 it's really easy to see what the stream of data will be

 but you might have a more complicated

 program that you know says get a get an element of this array look at something

 make a decision

 go get another element it's kind of random

 and you can think that's really unpredictable

 and then you make this big predictor

 that looks at this kind of pattern and you realize

 well if you get this data in this data then you probably want that one

 and if you get this one and this one and this one you probably

 want that one and is that theory or is that engineering

 like the paper that was written was it well it was asymptotic

 kind of kind of discussion or is it more like here's a hack that works well

 um it's a little bit of both

 like there's information theory in it i think somewhere okay

 so

 that's actually trying to prove yeah but once once you know the method

 implementing it is an engineering problem

 now there's a flip side of this which is

 in a big design team what percentage of people think their

 their their

 their their plan or their life's work is engineering versus design inventing things

 so lots of companies will reward you for filing patents

 yes

 some many big companies

 get stuck because to get promoted

 you have to come up with something

 new

 and then what happens is everybody's trying to do some random new thing 99

 which doesn't matter

 and the basics get neglected

 and or

 they get to there's a dichotomy

 they think like the cell library

 and the basic cad tools

 you know or basic

 you know software validation

 methods

 that's simple stuff you know they want to work on the exciting stuff

 and then they they spend lots of time trying to figure out how to patent something

 and that's mostly useless but the breakthroughs are on the simple stuff

 no no you no you have to do the simple stuff really well

 if you're brilliant building a building out of bricks

 you want great bricks

 so you go to two places to sell bricks so one guy says

 yeah they're over there in an ugly pile and the other guy is like

 lovingly

 tells you about the 50

 kinds

 of bricks

 and how hard

 they are and how beautiful

 they are and

 how square they are and you know which one you can buy bricks from

 which is going to make a better house

 so you're talking about the craftsman the person who understands

 bricks who loves bricks who loves their varieties that's a good word

 you know good engineering

 is great craftsmanship

 and when you start

 thinking engineering is about invention

 and set up a system that rewards invention the craftsmanship gets neglected

 okay so maybe one perspective is the theory the science

 over emphasizes invention

 and engineering emphasizes craftsmanship and therefore

 like

 so if you it doesn't matter what you do in theory well everybody

 knows like read the tech rags they're always talking about some breakthrough

 or intervention

 innovation and everybody thinks that's the most important thing

 but the number of innovative ideas is actually relatively low

 we need them right and innovation creates a whole new opportunity

 like when when some guy invented the internet

 right

 like that was a big thing

 the million people that wrote software against that were mostly doing engineering software writing

 so the elaboration of that idea was huge

 i don't know if you know brendan ike he wrote javascript

 in 10 days and that's an interesting story it makes me wonder

 and it was you know famously

 for many years considered to be a pretty crappy programming language

 still is perhaps it's been improving sort of consistently

 but the interesting thing about that guy is

 you know he doesn't get any awards

 you don't get a nobel prize or a field medal or

 a crappy

 piece of you know that software code

 that is currently the number one programming language in the world that runs

 now is cons

 increasingly running the backhand of the internet what does he end up does he know why

 everybody uses it

 like that would be an interesting thing was it

 the right thing at the right time because like when stuff like javascript

 came out like there's a move from you know writing c programs and c plus plus

 to let's call what they call managed code frameworks

 where

 you write simple code it might be interpreted it has lots of libraries

 productivity is high and you don't have to be an expert

 so you know java was supposed to solve all the world's problems it was complicated

 javascript came out you know after a bunch of other scripting languages

 i'm not an expert on it but

 yeah but was it the right thing at the right time

 or was there something

 you know clever because he wasn't the only one

 there's a few elements

 maybe if he figured out what it was

 no then he'd get a prize

 like that destructive theory yeah

 you know babies probably he hasn't defined this or he this needs a good promoter

 well i think there was a bunch of blog posts written about it which is like

 wrong is right which is

 like doing the crappy thing fast

 just like hacking together the thing that answers some of the needs

 and then iterating

 over time listening to developers

 like listening to people who actually use the thing

 this is something you can do more in software

 but the right time like you have to sense you have to have a good instinct

 of when is the right time for the right tool

 and make it super simple

 and just

 get it out there the problem is this is true with hardware

 this is less true with software is this backward compatibility

 that just drags behind you as

 you know

 as you try to fix all the mistakes of the past but the the timing

 was good there's something about that it wasn't accidental

 you have to like

 give yourself over to the

 you have to have this like broad sense of what's needed now

 and both scientifically and like the community and just like this it was obvious that

 there was no the interesting thing about javascript

 is everything that ran in the browser at the time like java and

 and i think other like scheme other programming languages

 they were all

 in a separate external container

 and then javascript

 was literally just injected

 into the web page it was the dumbest possible thing

 running in the same thread as everything else

 and like

 it was inserted as a comment so javascript code is inserted as a comment

 in the html code and it was i mean it's there's

 it's either genius or super dumb but it's like right so it has no apparatus

 for like a virtual machine and container

 it just executed

 in the framework the program is already running and it was that's cool and then

 because something about that accessibility

 the ease of its use

 resulted in then developers

 innovating on how to actually use it i mean i don't even know what to

 make of that but

 it does seem to echo across different software

 like stories of different software php has the same story really crappy language

 they just took over the world

 i always have a joke that the random length instructions

 that variable length instructions that's always one

 even though they're obviously worse

 like nobody knows why x86 is arguably the worst architecture

 you know on the planet is one of the most popular ones

 well i mean isn't isn't that also the story of risk versus

 i mean is that simplicity

 there's something about simplicity that

 us in this evolutionary process

 is valued

 if it's simple

 it's

 gets it spreads faster it seems like

 yeah or is that not always true that's always true

 yeah it could be simple is good but too simple is bad

 so why did risk win you think so far did risk win

 in the long arc of history

 maybe

 we don't know

 so who who's going to win

 what what's risk what's cisco who's going to win in that space

 in these instruction

 sets

 a ice offers going to win but

 they'll be little computers that run little programs like normal all over the place

 but but we're we're going through another transformation

 so

 but you think instruction sets underneath it all will change

 yeah they evolve slowly

 they don't matter very much

 they don't matter very much okay i mean the limits of performance

 are

 you know predictability of instructions and data i mean that's the big thing

 and then

 the usability of it is some you know

 quality of design quality of tools

 availability

 like right now

 x86 is proprietary

 with intel and amd but they can change it any way they want independently

 right arm is proprietary

 to arm and they won't let anybody else change it so it's like a sole point

 and risk 5 is open source so anybody can change it which is super cool

 but that also

 might mean

 it gets changed in too many random

 ways

 that there's no common

 sub subset of it that people can use

 do you like open

 or do you like clothes

 like if you were to bet all your money

 on one or the other risk

 five versus

 no idea

 it's case dependent well x86

 oddly enough when intel first started developing it they licensed

 like seven people

 so it was the open architecture

 and then they move faster than others and also bought one or two of them

 but there were seven different people making x86

 because at the time there was

 6502

 and z80s and you know 8086

 and you could argue everybody thought z80 was the better instruction set but that was propriety

 proprietary to one place oh and the 6800

 so there's like five or four or five different microprocessors

 intel went open

 got the market

 share because people felt like they had multiple

 sources

 from it and then over time it narrowed down the two

 players

 so why you as a historian

 well why did intel win for so long

 with the

 with their processors

 i mean they were great

 their process development was great

 oh so it's

 just looking back to javascript and brand nike is

 microsoft

 and netscape and all these internet browsers

 microsoft won the browser game because they aggressively stole other people's ideas

 like right after they did it you know i i don't know

 if intel

 was stealing

 other people's ideas they started making a

 just good way they started making rams

 random access memories

 and then

 at the time when the japanese manufacturers came up

 you know they were getting out competed on that and they pivoted the microprocessors

 and they made the first you know integrated microprocessor

 programs

# Chapter 2

 with the

 with their processors

 i mean they were great

 their process development was great

 oh so it's

 just looking back to javascript and brand nike is

 microsoft

 and netscape and all these internet browsers

 microsoft won the browser game because they aggressively stole other people's ideas

 like right after they did it you know i i don't know

 if intel

 was stealing

 other people's ideas they started making a

 just good way they started making rams

 random access memories

 and then

 at the time when the japanese manufacturers came up

 you know they were getting out competed on that and they pivoted the microprocessors

 and they made the first you know integrated microprocessor

 programs

 4004

 or something who was behind that pivot that's a hell of a pivot andy grove

 and he was great

 that's a hell of a pivot and then they led

 semiconductor

 industry

 like they were just a little company ibm

 all kinds of big companies had both loads of money

 and they out innovated everybody

 auto innovated okay yeah yeah so it's not like marketing it's not yeah

 their processor designs were pretty good

 um i think the

 you know core 2 was probably the first one i thought was great

 it was a really fast processor and then haswell was great

 what makes a great processor

 in that delay oh if you just look at it's performance

 versus

 everybody

 else

 it's you know the size of it the you know usability

 of it so it's not specific

 some kind of element that makes it beautiful it's just like literally just raw performance

 is that how you think about processors it's just like raw performance

 of course

 it's like a horse race the fastest one wins now you don't care how [laughter]

 just as long as it was well there's the fastest in the environment

 like

 right you know for years you made the fastest

 one you could and then people started to have power limits

 so then you made the fastest at the right power point

 and then and then when we started doing multiprocessors

 like

 if you could scale your processors

 more than the other guy you could be 10

 faster on like a single thread but you have more threads

 so there's lots of variability

 and then

 arm

 really explored

 like you know they have the a series and the r series and the m series

 like a family of processors for all these different design points from like unbelievably

 small and simple

 and so then when you're doing the design

 it's sort of like this big palette of cpus

 like they're the only ones with a credible you know top to bottom palette and

 what do you mean incredible

 top to bottom well there's people who make microcontrollers

 that are small but they don't have a fast one there's people make fast processors

 but don't have a little a medium one or a small one

 is it hard to do

 that full palette

 that's that seems like a it's a lot of different

 so what's the difference in

 the arm folks and intel

 in terms of the way they're approaching this problem well intel

 almost all their processor designs were you know very custom

 high end you know for the last 15 20 years the fastest force possible yeah

 in one horseshoe

 yeah and then architecture they're really good but the company itself was

 fairly insular

 to what's going on in the industry with cad tools and stuff

 and there's this debate about custom design versus synthesis

 and how do you approach that

 i'd say intel was slow on the getting to synthesize

 processors

 arm

 came in from the bottom and they generated ip which went to all kinds of customers

 so they had very little say how the customer implemented their ip

 so arm is super friendly to the synthesis ip environment

 whereas intel said we're going to make this great

 client chip server chip with our own cad tools with our own process

 with our own

 you know other supporting

 ip and everything only works with our stuff

 so is that

 is arm winning the mobile platform space in terms of processors and so

 in that and

 what you're describing

 is why they're winning well they had lots of people doing lots of different experiments

 so they controlled the processor architecture and ip

 but they let people put in lots of different chips

 and there was a lot of variability

 in what happened there

 whereas

 intel when they made their mobile

 their foray

 into mobile they had one team doing one

 part

 right so it wasn't 10 experiments and then their mindset was pc mindset microsoft software mindset

 and that brought a whole bunch of things along that

 the mobile world embedded world don't do do you think it was possible for intel

 to pivot hard and win the mobile

 market

 that's a hell of a difficult thing to do right for a huge company

 to just pivot

 i mean it's so interesting to because we'll talk about your current work it's like

 it's clear that pcs were dominating for several decades like desktop computers and then mobile

 it's unclear

 it's a leadership question

 like like apple under steve jobs when he came back they pivoted multiple times

 you know they built ipads and itunes

 and phones and tablets

 and great macs like like who knew computers should be made out of aluminum

 nobody knew that

 that they're great it's

 super fun that was steve

 yeah steve jobs like they pivoted

 multiple

 times

 and you know the old intel they they did that multiple times

 they made drams and processors and processes and

 i got to ask this what was it like working with steve

 jobs

 i didn't work with him

 did you interact with him twice

 i said hi to him twice in the cafeteria

 what did he say hi he said hey fellas

 he was friendly

 he was wandering around and with somebody he couldn't find the table because the cafeteria was

 was packed

 and i gave my table

 but i worked for mike colbert who talked to

 like mike was the unofficial

 cto of apple

 and a brilliant guy and he worked for steve for 25 years maybe more

 and he talked to steve multiple times a day

 and

 he was one of the people who could

 put up with steve's let's say brilliance

 and intensity

 and and steve really liked him and steve trusted mike to translate

 the he thought up

 into engineering

 products at work and then mike ran a group called platform architecture

 and i was in that group

 so many times i'd be sitting with mike and the phone would ring

 it'd be steve

 and mike would hold the phone like this because steve

 would be yelling about something

 or other

 yeah

 and he would translate it and he translated

 and then he would say

 steve wants us to do this

 so

 was steve a good engineer or no i don't know

 he was a great idea guy idea person he's a really good selector for talent

 yeah so that seems to be one of the key elements of leadership right

 and then he was a really good first principals

 guy like

 like somebody say something couldn't be done and he would just think

 that's obviously wrong

 right but you know

 maybe it's hard to do maybe it's expensive

 to do maybe we need different people

 you know there's like a whole bunch of you know if you want to do something

 hard

 you know maybe it takes time maybe you have to iterate

 there's a whole bunch of things you could think about

 but saying it can't be done is stupid

 how would you compare

 so it seems like elon musk is more engineering

 centric

 but it's also i think he considers himself a designer

 too he has a design mind

 steve jobs

 feels like he is much more idea space design space versus engineering

 yeah just make it happen

 like the world should be this way

 just figure it out but but he used computers

 you know he had computer people talk to him all the time

 like mike was a really good computer guy he knew what computers

 could do computer meaning computer hardware like

 hardware software

 all of pieces the whole thing and then he would

 you know have an idea about what could we do with this next

 that was grounded in reality it wasn't like he was you know just

 finger painting on the wall and wishing somebody would interpret

 it like

 so he had this interesting

 connection

 because

 no he wasn't a computer architect or a designer

 but he had an intuition from the computers we had to what could happen

 and

 essentially you say intuition because it seems like he was pissing off a lot of engineers

 in his intuition about what canada can't be done those like the

 what is all these stories

 about like floppy

 disks

 and all that kind of stuff like yeah so

 in in steve the first round like he'd go into a lab

 and look at what's going on and hate it and and

 fire people or or ask somebody in the elevator what they're doing for apple

 and you know not be happy

 when he came back my impression was

 is he surrounded himself with this relatively

 small group of people yes and didn't really interact

 outside of that as much

 and then the joke was you'd see like somebody moving a prototype

 through the

 quad with a with a black blanket over it

 and that was because it was secret

 you know partly

 from steve

 because they didn't want

 steve

 to see it until it was ready

 yeah the dynamic with johnny ive and steve

 is interesting it's like you don't wanna

 he ruins as many ideas as he generates yeah

 yeah it's a dangerous kind of

 line to walk

 if you have a lot of ideas like

 like gordon bell was famous for ideas

 right and it wasn't that the percentage of good ideas was way higher than anybody else

 it was he had so many ideas

 and and he was also good at talking people about it and and getting the filters

 right

 and you know seeing through stuff

 whereas elon was like hey i want to build rockets so

 steve would hire a bunch of rocket guys and elon would go read rocket manuals

 so ian is a better engineer a sense like or like more

 like a love and passion for the manuals yeah and the details the details

 the craftsmanship too right well i guess you had craftsmanship too but of a different kind

 what do you make of the

 just the standard

 for just a little longer

 what do you make of like the anger

 and the passion

 and all that the the firing

 and the

 mood swings

 and

 the madness the

 um you know being emotional

 and all that that's

 steve and i i guess elon

 too so what is that a

 is that a bugger feature

 it's a feature

 so there's a graph which is

 y-axis productivity yeah x-axis at zero it's chaos

 yeah and infinity is complete order yeah right so as you go from

 the you know the origin

 as you improve order you improve productivity

 yeah and at some point productivity peaks

 and then it goes back down again yeah too much order nothing can happen yes

 but the question is is

 how close to the chaos

 is that no no no here's the thing

 is once you start moving the directional

 order the force vector to drive you towards order

 is unstoppable

 oh this is the same every organization

 will

 move to the place where their productivity is stymied by order so you need

 so the question is who's the counter force

 like because it also feels really good as you get more organized

 then productivity goes up the organization

 feels it they orient it towards it right to hire more people

 they get more guys who can run process you get bigger

 right and then inevitably inevitably

 the organization gets captured by the bureaucracy that manages all the processes

 right and then humans really like that and so if you just walk into a room

 and say guys

 love what you're doing

 but i need you to have less order

 if you don't have some force behind that nothing will happen

 i i can't tell you on how many levels that's profound so

 so that's why i'd say it's a feature

 now

 could you be nicer about it

 i don't know i don't know any good examples of being nicer about it

 well

 the funny

 thing is to get stuff

 done you need people who can manage

 stuff

 and manage

 people because humans

 are complicated

 they need lots of care and feeding

 and you need to tell them

 they look nice and they're doing good stuff and pat them on the back

 right

 i don't know

 do you tell me is that is that needed

 humans need that i had a friend he started to manage the group and he said

 i figured it out you have to praise them before they do anything

 i was waiting until they were done

 and they're always mad at me now i tell them what a great job they're doing

 while they're doing it

 but then you get stuck

 in that trap

 because then when they're not doing something how do you confront

 these people

 i think a lot of people that had trauma in their childhood who disagree

 with you successful

 people that you just first do the rough stuff and then be nice later

 i don't know

 okay but

 you know nice engineering

 companies

 are full of adults

 who had all kinds of range of childhoods

 you know most people had okay childhoods

 well i don't know if and lots of people only work for praise

 which is weird you mean like everybody

 i'm not that interested in this but well you you're you're probably looking for somebody's approval

 um

 even still

 yeah maybe i should think about that

 maybe somebody who's no longer with this kind of thing

 i don't know

 i used to call it my dad

 and tell him what i was doing

 he was he was

 very excited

 about engineering

 and stuff

 you got his approval

 yeah a lot

 i was lucky

 like he he decided i was

 smart and unusual as a kid and that was okay when i was really young

 so when i like did poorly in school i was dyslexic

 i didn't read until i was third or fourth grade and

 they didn't care my parents were like

 oh he'll be fine

 so that was funny that was cool is he still with us you miss him

 sure yeah he had parkinson's and then cancer his last 10 years were tough

 and i killed him killing a man like that's hard the mind well it's pretty good

 um parkinson's causes slow dementia and the chemotherapy i think accelerated it

 but it was like hallucinogenic dementia so he was clever and funny and interesting and

 was it was pretty unusual

 do you remember conversations

 of course from that time like where do you have fond memories

 of the guy yeah oh yeah anything come to mind

 a friend

 told me one time i could draw

 a computer

 on the whiteboard

 faster

 than anybody

 you'd ever met

 and i said you should meet my dad

 like when i was a kid he'd come home and say

 i was driving

 by this bridge

 and i was thinking

 about it and he pulled out a piece of paper

 and he'd draw

 the whole

 bridge

 he was a mechanical engineer

 yeah

 and he would just draw

 the whole thing

 and then he would

 tell me about

 it and

 tell me how

 you would have changed

 it

 and he had this you know idea that he could understand and conceive anything

 and i i just grew up with that so that was natural

 so if

 you know

 like

 when i interview

 people i ask them to draw a picture of something

 they did on a whiteboard

 and it's really interesting like some people draw a little box

 you know and then they'll say and then this talks to this and

 yeah i'd be like this is frustrating

 and i had this other guy come in one time he says

 well

 i designed

 a floating

 point in this chip

 but i'd really

 like to tell you how the whole thing

 works

 and then tell you how the floating

 point works inside of it do you mind if i do that he covered

 two whiteboards

 yeah like 30 minutes

 and i hired him like yeah he was great

 this is craftsman i mean that's the craftsmanship to that yeah but also

 the the mental agility to understand the whole thing

 right put the pieces in contacts

 like you know real view of the balance of how the design worked

 because

 if you don't understand

 it properly

 when you start to draw it you'll

# Chapter 3

 well

 i designed

 a floating

 point in this chip

 but i'd really

 like to tell you how the whole thing

 works

 and then tell you how the floating

 point works inside of it do you mind if i do that he covered

 two whiteboards

 yeah like 30 minutes

 and i hired him like yeah he was great

 this is craftsman i mean that's the craftsmanship to that yeah but also

 the the mental agility to understand the whole thing

 right put the pieces in contacts

 like you know real view of the balance of how the design worked

 because

 if you don't understand

 it properly

 when you start to draw it you'll

 fill up half the white board with like a little piece of it and you know

 like

 your ability to lay it out in an understandable

 way it takes a lot of understanding

 so

 and be able to zoom into the detail and then zoom out to the zoom

 really fast

 what about the impossible thing you see your dad

 believed that you could do anything

 that's a weird feature for a craftsman

 yeah it seems that that

 echoes in your own behavior

 like that's that's the well it's not that anybody can do anything right now

 right it's

 that if you work

 at it you can get better

 at it

 and there might not be a limit

 and they did funny things like

 like he always wanted to play

 piano

 so at the end of his life he started playing the piano

 when he had parkinson's

 and he was terrible

 but he thought if he really worked

 out in this life maybe

 the next life he'd be better at it

 he might be onto something yeah

 he enjoyed doing it yeah so that's pretty funny

 do you think the perfect is the enemy of the good in hardware and software engineering

 it's like we were talking about javascript a little bit and the messiness of the 10-day

 building process

 yeah it's you know creative tension right

 the creative tension is you have two different ideas that you can't do both

 right right and then but the fact that you want to do both

 causes you to go try to solve that problem that's the creative part

 so if you're building computers

 like some people say we have the schedule

 and anything that doesn't fit in the schedule we can't do

 right so they throw out the perfect because they have a schedule

 i hate that

 then there's other people who say we need to get this perfectly right

 and no matter what you know more people more money right

 and there's a really clear idea about what you want some people are going to articulate

 in it right

 so let's call that the perfect yeah yeah

 all right but that's also terrible because they never ship anything you never hit any goals

 so now you have that now you have your framework

 yes you can't

 throw

 out stuff because you can't get it done today because maybe you get it done tomorrow

 or the next project

 right you can't

 so you have to

 i work with a guy that i really like working with

 but he over filters

 his ideas

 over filters

 he'd start thinking about something

 and as soon as he figure out what's wrong with it you'd throw it out

 and then

 i start thinking about it like you know you come up with an idea

 and then you find out what's wrong with it

 and then you give it a little time to set because sometimes

 you know you figure out how to tweak it or maybe that idea helps some other

 idea

 so idea generation is really funny

 so you have to give your ideas space like spaciousness of mind is key

 but you also have to execute programs and get  done

 and then it turns

 out

 computer

 engineering

 is fun because it takes you know 100

 people to build a computer

 200 to 300 whatever the number is and people are so variable about

 you know temperament and you know skill sets and stuff

 that you know in a big organization

 you find that

 the people who love the perfect ideas

 and the people that want to get stuff done yesterday

 and

 people like to come up with ideas and people like to

 let's say shoot down ideas and it takes the whole

 it takes a large group of people

 some are good at generating ideas some are good at filtering ideas and then all

 in that giant mess you somehow

 i guess the goal is for that giant mess of people to

 find the perfect path through the attention the creative tension

 but like how do you know when

 you said there's some people good at articulating

 what perfect looks like what a good design is like if you're sitting in a

 in a room

 and you have a set of ideas about like how to design

 a better processor how do you know

 this is this is something

 special here this is a good idea

 let's try this

 so have you ever brainstormed

 idea with a couple people that were really smart

 and you kind of go into it and you you don't quite understand

 it and you're working on it

 and then you start you know talking about it putting it on the whiteboard

 maybe it takes days or weeks

 and then your brain start to kind of synchronize it's really weird

 and like you start to see what each other is thinking

 and yeah and it starts to work

 like you can see work like my talent in computer design is i can

 i can see how computers work in my head

 like really well and i know other people can do that too

 and when you're working with people that can do that

 like it is kind of a an amazing experience

 and then

 and every once in a while

 you get to that place and then you find the flaw

 which is kind of funny because you you can you can fool yourself in

 but the two of you kind of drifted along

 yeah into the direction that was useless

 yeah that happens too like you have to

 because you know

 well the nice thing about computer design there's always reduction in practice

 like you come up with your good ideas

 and i know some architects who really love ideas

 and then they work

 on them and they

 put it on the shelf

 they go work on the next

 idea

 and put on the shelf

 they never

 reduce

 the practice

 so they find out what's good and bad because most

 every time i've done something really new by the time it's done

 like the good parts are good but i know all the flaws like

 yeah would you say your career

 just your own experience is your career defined by mostly by flaws or by successes

 like if again there's great tension between those

 if you haven't

 tried hard yeah right and done something new

 right

 then you're not going to be facing

 the challenges

 when you build it then you find out all the problems with it

 and but when you look back you see problems

 okay oh when i look back

 um what do you think earlier in my career

 yeah like eb5

 was the second alpha chip

 i was so embarrassed about the mistake so i could barely talk about it

 and it was in the guinness book of worlds records and it was the fastest processor

 on the planet

 yeah

 so it was and at some point i realized that was really a bad

 mental framework

 to deal with like doing something new we did a bunch of new things

 and some worked

 out great and some were bad

 and we learned a lot from it and then

 the next one we learned a lot that also ev6 also had some

 really cool things in it i think the proportion of good stuff went up but

 it had a couple of fatal flaws in it that were

 painful

 and then

 yeah you learn to channel the pain into like pride not pride really you know just

 realization

 about how the world works okay or how

 that kind of ideas that works life is suffering that's the reality

 what no it's not

 well i know the buddha said that and a couple other people

 are stuck on it no

 it's you know there's this kind of weird combination

 of good and bad

 you know light and darkness that you have to tolerate and you know deal with

 yeah there's definitely lots of suffering in the world

 depends on the perspective it seems like there's way more darkness but

 that makes the light part really nice

 what computing

 hardware

 or just any kind of even software design are you

 do you find beautiful from your own work from

 other people's work that you're just

 we were just talking about the

 the battleground of flaws and mistakes and errors but things that were just

 beautifully done is there something that pops to mind well when things are beautifully done

 usually

 there's a well thought out set of abstraction layers

 so the whole thing works in unison nicely yes

 and and when i say abstraction layer that means two different components when they work together

 they work independently they don't have to know what the other one is doing

 so that decoupling

 yeah so the famous one was the the network stack like there's a seven layer network

 you know data transport and protocol and all the layers

 and the innovation was is when they really wrote got that right

 because networks before that didn't define those very well the layers could innovate independently

 and occasionally the layer boundary would you know the interface would be upgraded

 and that that let you know the the design space breathe and

 you could

 do something

 new in layer

 seven

 without

 having to worry about how layer

 four

 worked

 right and

 so good design does that and you see it in processor designs

 when we did the zen design at amd

 we made several components very modular

 and you know my insistence

 at the top was i wanted all the interfaces

 to find before we wrote the rtl for the pieces

 one of the verification

 leads said if we do this right i can test the pieces

 so well independently when we put it together

 we won't find all these interaction bugs because the floating point knows how the cache works

 and i was a little skeptical but he was mostly right

 that the modularity design greatly improved the quality

 is that universally true in general would you say about good designs the modularity

 is

 like usually

 talked about this before humans are only so smart like

 and we're not getting any smarter

 right but the complexity of things is going up yeah so

 you know a beautiful design can't be bigger than the person doing it

 it's just

 you know their piece of it

 like

 the odds of you doing a really beautiful

 design of something that's way too hard for you is slow

 right

 if it's way too simple for you it's not that interesting

 it's like well anybody could do that but when you get the right match of

 your

 your expertise and you know mental power

 to the right design size

 that's cool but that's not big enough to make a meaningful

 impact in the world

 so now you have to have

 some framework to design the pieces

 so that the whole thing is big and harmonious but

 you know when you put it together it's you know sufficiently

 sufficiently

 interesting to to be used

 and you know so that's like a beautiful design is

 matching the limits of that human cognitive capacity

 to to the module you can create and creating a nice interface between those modules

 and thereby do you think there's a limit to the kind of

 beautiful complex systems we can build with this kind of modular

 design it's like

 you know if we build increasingly more complicated you can think of like the internet

 okay let's scale it up you can think of like social network like twitter as one

 computing system

 and but those are little modules yeah right

 but it's built on it's built on so many components nobody at twitter even understands

 right so

 so so if an alien showed up and looked at twitter

 he wouldn't just see twitter as a beautiful

 simple thing that everybody

 uses

 which is really big

 you would see

 the network

 it runs on the fiber optics the data is transported

 the computers the whole thing is so bloody complicated

 nobody twitter understands it and so i think that's what the alienware

 sees so yeah if an alien showed up and looked at twitter

 or looked at the various different

 networked systems that you can see on earth

 so imagine they were really smart they could comprehend the whole thing

 and then they sort of

 you know evaluated

 the human and thought this is really interesting no human on this planet comprehends

 the system they built

 no individual

 or well would they even see individual

 humans that's the interest

 like we humans

 are very human-centric

 entity-centric

 and so we think

 of us as the organ as the central organism and the networks

 as just the connection of organisms

 but from a perspective of

 an alien from an outside perspective it seems like yeah

 yeah i get it where the ants and they'd see the ant colony

 the ant colony yeah

 or the result the production of the ant colony which is like cities and

 it's it's

 yeah in that sense humans are pretty impressive the modularity that we're able to

 and the

 and how robust we are to noise and mutation

 all that kind of stuff well that's because it's stress tested all the time yeah

 you know you build all these cities with buildings and you get earthquakes occasionally and

 you know some you know wars earthquakes

 viruses every once in a while

 you know changes in business plans for you know like shipping or something like

 like

 as long as it's all stress tested then

 it keeps adapting to the the situation so the

 that's that's a curious phenomena

 well let's go let's talk about moore's law a little bit

 at the broad view of moore's law was just exponential improvement of

 computing capability like openai for example recently published this kind of

 papers looking at the exponential improvement in the training efficiency of neural networks

 for like image net and all that kind of stuff we just got better on

 this is purely software aside

 just figuring out better tricks and algorithms for training neural networks

 and that seems to be improving

 significantly faster than the moore's law prediction

 you know

 so that's in the software space like what do you think

 if moore's law continues or if the general

 version of moore's law continues

 do you think that comes mostly

 from the hardware from the software some mix of the two

 some interesting totally

 so not the reduction of the size of the transistor

 kind of thing but more in the

 in the totally interesting kinds of innovations in the hardware space all that kind of stuff

 well

 there's like a half a dozen things going on in that graph

 so one is

 there's initial innovations that had a lot of had room to be exploited

 so you know the efficiency of the networks has improved dramatically

 and then

 the decomposability

 of those and the use go you know they started running on one computer

 then multiple computers

 and multiple gpus

 and then arrays of gpus

 and

 they're up to thousands

 and at some point

 so

 so it's sort of like they were consumed

 they were going from like a single computer application

 to a thousand

 computer application

 so that's not really a moore's law thing that's an independent

 vector how many computers can i put on this problem

 because the computers themselves are getting better on like a moore's law rate

 but their ability to go from one to ten to a hundred to a thousand

 yeah you know was something and then multiplied

 by

 you know the amount of computes

 it took to resolve like alex

 net to resnet

 the transformers

 it's it's been quite

 you know steady improvements

 but those are like s cars

# Chapter 4

 they're up to thousands

 and at some point

 so

 so it's sort of like they were consumed

 they were going from like a single computer application

 to a thousand

 computer application

 so that's not really a moore's law thing that's an independent

 vector how many computers can i put on this problem

 because the computers themselves are getting better on like a moore's law rate

 but their ability to go from one to ten to a hundred to a thousand

 yeah you know was something and then multiplied

 by

 you know the amount of computes

 it took to resolve like alex

 net to resnet

 the transformers

 it's it's been quite

 you know steady improvements

 but those are like s cars

 aren't they yeah that's the exactly

 kind of

 s-curves

 that are underlying

 moore's law from the very beginning

 so so what what's the biggest what's the most

 productive

 rich source of s-curves

 in in the future do you think

 is it hardware

 is it software

 or is it so hardware

 is going to move along

 relatively slowly

 like you know double performance every two years there are there's still

 i like how you call that slow yeah that's the slow version

 the snail's pace of moore's law maybe we should we should

 we should trademark that one

 whereas the scaling by number of computers

 you know can go much faster

 you know i'm sure at some point google had a

 you know their initial search engine was running on a laptop you know like

 yeah and at some point they really worked on scaling that and then they factored

 the indexer

 from

 you know this piece and this piece and this piece and they spread the data

 on more

 things and

 you know they did a dozen innovations

 but as they scaled up the number of computers on that it kept breaking

 finding new bottlenecks in their software and their schedulers and and made them rethink

 like it seems insane to do a scheduler

 across a thousand computers

 to schedule parts of it and then send the results to one computer

 but if you want to schedule a million searches

 that makes perfect sense

 so so there's the the scaling by just quantity is probably the richest thing but then

 as you scale quantity

 like a network that was great on 100 computers

 may be completely the wrong one you may pick a network that's 10 times slower

 on 10 000 computers like per computer

 but if you go from a hundred to ten thousand that's a hundred times

 so that's one of the things that happened when we did internet scaling is the efficiency

 went down

 not up the future of computing is inefficiency

 not efficiency

 but scales

 in efficient scale it's it's scaling faster than inefficiency

 bites you

 and as long as there's you know dollar value there like scaling costs lots of money

 yeah but google showed

 facebook showed everybody

 showed that

 the scale was where the money was at

 it was and so it was

 worth it financially do you think

 is it possible that like basically the entirety of earth will be like a computing surface

 like this table will be doing computing

 this hedgehog will be doing computing like everything

 really inefficient dumb computing would be fiction books they call it computronium

 computing we turn everything into computing

 well most of the elements aren't very good for anything

 like you're not going to make a computer out of iron like you know silicon and

 carbon have like nice structures

 you know we'll we'll see what what you can do with the rest of it

 people talk about well maybe we can turn the sun into computer but it's it's hydrogen

 and a little bit of helium so

 what i mean is more like actually just adding computers to everything

 oh okay so you're just converting all the mass of the universe into a computer

 no no so not using to be ironic from the simulation point of view is like

 the simulator build mass to simulate

 like

 yeah i mean yeah so

 i mean ultimately

 this is all heading towards the simulation yeah well

 i i think i might have told you the story a tesla they were deciding

 so they want to measure the current coming out of the battery

 and they decide between putting the resistor

 in there

 and putting a computer

 with a sensor in there

 and the computer was faster than the computer i worked on in 1982.

 and we chose the computer because it was cheaper than the resistor

 so so sure this hedgehog you know it costs 13

 and we can put a you know

 an ai that's the smartest you in there for five bucks it'll have

 one

 you know so computers will be you know he'd be everywhere

 i was hoping it wouldn't be smarter than me because

 well everything's going to be smarter than you

 but you were saying it's inefficient

 i thought it was better to have a lot of doubt well

 well moore's law will slowly compact

 that stuff

 so even the dump things will be smarter

 than us

 the dump things are going to be smart or they're going to be smart

 enough to talk to something

 that's really

 smart

 you know it's like

 well just remember

 like a big computer

 chip

 yeah

 you know it's like an inch by an inch

 and you know

 40 microns thick

 it doesn't take very much very many atoms to make a high power computer

 yeah and 10 000 of them can fit in the shoe box

 but you know you have the the cooling

 and power problems

 but you know

 people are working on that

 but they still can't write

 compelling poetry or music or

 understand what love is or have a fear of mortality

 so so we're still winning neither can most of humanity so

 well they can write books about it so [laughter]

 but but speaking about this

 you know this walk along the path of innovation towards

 the dumb things being smarter than humans you are now the cto

 of tens torrent as of two months ago they build hardware for deep learning

 how do you build scalable

 and efficient deep learning this is such a fascinating

 space yeah yeah so it's interesting

 so um

 up until recently i thought there was two kinds of computers there are serial computers

 that run like c programs and then there's parallel computers

 so the way i think about it is you know parallel computers you have given parallelism

 like gpus are great because you have a million pixels

 and modern gpus run a program on every pixel they call the shader program right so

 or

 like finite

 element analysis

 you

 you build something

 you know you make this into little tiny

 chunks

 you give each chunk to a computer

 so you're giving all these chunks a parallel something like that

 but most c programs you write this linear narrative

 and you have to make it go fast

 to make it go fast you predict all the branches

 all the data fetches and you run that more in parallel

 but that's found parallelism

 ai is

 i'm still trying to decide how fundamental this is it's a given parallelism problem

 but the way people describe the neural networks

 and then how they write them in pi torch it makes graphs

 yeah that might be fundamentally different than the gpu

 kind of parallelism yeah it might be because the

 when you run the gpu program on all the pixels you're running

 like you know depends you know this group of pixels

 say it's background blue and that runs a really simple program this pixel

 is

 you know some patch of your face so you have some

 really interesting shader program to give you impression of translucency

 but the pixels themselves don't talk to each other there's no graph

 right

 so you you do the image

 and then you do the next image and you do the next image

 and you run

 8 million pixels 8 million programs every time and modern gpus have like 6 000

 thread engines in them

 so you know

 to get 8 million pixels each one runs a program on you know 10 or 20

 pixels

 and that's how that's how they work but there's no graph

 but you think graph might be a totally

 new

 way to think about hardware so raja gadori and i've been having this good conversation

 about giving versus found parallelism

 and then

 the kind of walk cause we got more transistors

 like you know computers way back when did stuff on scalar data

 then we did it on vector data famous vector machines

 now we're making computers that operate on matrices

 right and then the the category we we said that was next was spatial

 like imagine you have so much data that

 you know you want to do the compute on this data and then when it's done

 it says

 send the result to this pile of data run some software on that

 and it's better to

 to think about it spatially than

 to move all the data to a central processor and do all the work

 so especially

 i mean moving in the space of data as opposed to moving the data

 yeah you have a you have a petabyte data space

 spread across some huge array of computers

 and when you do a computation

 somewhere you send the result of that computation

 or maybe a pointer to the next program some other piece of data and do it

 but i think a better word might be graph

 and all the ai neural networks are graphs

 do some computations

 send the result here do another computation

 do a data transformation

 do a merging do a pooling

 do another computation

 is it possible to compress and say how we make this thing

 efficient

 this whole process efficient that's different

 so first

 the fundamental elements in the graphs are things like matrix multiplies convolutions data manipulations

 and data movements

 so gpus

 emulate those things with their little singles you know basically running a single threaded program

 and then

 there's a you know nvidia calls it a work where they group a bunch of programs

 that are similar together

 so for efficiency and instruction use

 and then at a higher level you kind of

 you take this graph and you say this part of the graph is a matrix multiplier

 which runs on these 32

 threads

 but the model at the bottom was built for

 running programs on pixels not executing graphs so it's emulation

 yes so is it possible to build something that natively runs graphs

 yes so that's what ten storm did

 so

 where are we on that

 how like in the history of that effort

 are we in the early days yeah i think so tense torrance

 started by a friend of mine labisha bajak and i

 i was his first investor so i've been you know kind of

 following him and talking to him about it for years and

 in the fall when i was considering things to do

 i decided you know the

 we we

 held a conference last year with a friend organized it and

 and we we wanted to bring in thinkers and two of the people were andre carpassi

 and chris lattner and

 andre gave this talk on youtube called software 2.0

 which i think is great

 which is we went from programmed computers where you write programs to data program computers

 you know like the futures you know of software as data programs the the networks

 and i think that's true

 and then

 chris has been work he worked on llvm

 the low-level virtual machine which became the intermediate representation

 for all compilers

 and now he's working on another project called mlir which is mid-level intermediate representation which is

 essentially under the graph

 about how do you represent that kind of computation

 and then coordinate large numbers of potentially heterogeneous

 computers

 and and i would say technically tense torrents

 you know two pillars are those those those two ideas software 2.0 and mid-level representation

 but it's in service of executing graph programs

 the hardware is designed to do that so it's including the hardware piece yeah

 and then the other cool thing is

 for a relatively small amount of money they did a test chip and two production chips

 so it's like a super effective teams and

 and unlike some ai startups where if you don't build the hardware

 to run the software that they really want to do

 then you have to fix it by writing lots more software

 so the hardware naturally does matrix multiply convolution the data manipulations

 and the data movement between processing elements that that you can see in the graph

 which i think is all pretty clever and

 that's that's what i'm i'm working on now so

 the i think it's called the grace call processor

 introduced last year it's

 you know there's a bunch of measures of performance we're talking about horses

 it seems to outperform

 368

 trillion operations per second seems to outperform nvidia's tesla t4 system

 so these are just numbers

 what do they actually mean in real world perform like what are the

 metrics

 for you that you're chasing

 in in your horse race like what do you care about

 well first so the the native language of

 you know people who write ai network programs

 is pie torch now by torch tensorflow

 there's a couple others

 the pi torch is one over tensor flows it's just i'm not an expert on that

 i i know many people have switched from tensorflow to pi torch

 yeah and there's technical reasons for it and

 i use both both are still awesome both are still awesome

 but the deepest

 love is for pytorch

 currently

 yeah

 there's more love for that and that that may change

 so the first thing is

 when they write their programs

 can the hardware execute it pretty much as it was written

 right so pi torch turns into a graph

 we have a graph compiler

 that makes that graph

 then

 it fractions

 the graph down so if you have a big matrix

 multiply

 we turn it into right-sized

 chunks that run on the processing

 elements

 it hooks all the graph up it lays out all the data

 there's a couple mid-level representations of it that are also simulatable

 so that

 if you're writing the code you can see how it's going to go through the machine

 which is pretty cool and then at the bottom it schedules kernels like

 math data manipulation data movement kernels which do this stuff so

 we don't have to run write a little program to do matrix

 multiply

 because we have a big matrix multiplier

 like there's no cmd program for that

 but there is scheduling for that

 right so the the one of the goals is if you write

 a piece of pytorch

 code that looks pretty reasonable

 you should be able to compile

 it run it on the hardware

 without having to tweak it and and do all kinds of crazy things to get performance

 there's not a lot of intermediate

 steps

 right it's running directly as right like on a gpu

 if you write a large matrix

 multiply

 naively

 you'll get five to ten percent of the peak performance of the gpu

 right and then there's a bunch there's a bunch of people publish papers

 on this and i read them about

 what steps do you have to do and it goes from

 pretty reasonable

 well transpose one of the matrices so you wrote or not column ordered

 you know

 block it so that you can put a block of the matrix on different

 sms you know groups of threads

 but some of it gets into little details

 like you have to schedule it just so so you don't have registered

 conflicts

 so the the the they call them cuda ninjas

 i love it to get to the optimal point you either write a pre use a

 pre-written

 library

 which is a good strategy

 for some things or you have to be an expert

 in micro architecture

 to program it

 right so the optimization

 step is way more complicated with the gpa so our our goal is

 if you write pi torch that's good pi torch you can do it now there's

 as the networks are evolving you know they've changed from convolutional to matrix multiply

 people are talking about conditional graphs you're talking about very large matrices they're talking about sparsity

 you're talking about problems that scale across many many chips so the the native

# Chapter 5

 you know

 block it so that you can put a block of the matrix on different

 sms you know groups of threads

 but some of it gets into little details

 like you have to schedule it just so so you don't have registered

 conflicts

 so the the the they call them cuda ninjas

 i love it to get to the optimal point you either write a pre use a

 pre-written

 library

 which is a good strategy

 for some things or you have to be an expert

 in micro architecture

 to program it

 right so the optimization

 step is way more complicated with the gpa so our our goal is

 if you write pi torch that's good pi torch you can do it now there's

 as the networks are evolving you know they've changed from convolutional to matrix multiply

 people are talking about conditional graphs you're talking about very large matrices they're talking about sparsity

 you're talking about problems that scale across many many chips so the the native

 you know data item is a as a packet

 like so you send a packet to a processor it gets processed

 it does a bunch of work and then it may send packets to other processors

 and and they execute like a data flow graph kind of methodology

 got it we have a big network on chip and then 16

 the next second chip has 16 ethernet ports they hook lots of them together

 and it's the same graph compiler across multiple chips

 so that's where the scale comes in so it's built to scale naturally

 now

 my experience with scaling is as you scale you run into lots of interesting problems

 so scaling is the mountain to climb

 yeah so the hardware is built to do this and then

 we're in the process of

 is there a software part to this with ethernet and all that

 well the

 you know the protocol at the bottom you know we send you know it's an ethernet

 phi

 but the protocol basically says

 send a packet from here to there it's all point to point

 the header bit says which processor to send it to and we basically

 take a packet off our on-chip network

 put an ethernet header on it send it to the other end

 to strip the header off and send it to the local thing it's pretty straightforward

 human human interaction is pretty straightforward

 too but when you get a million of us we could do some crazy stuff together

 it could be fun

 so is that the goal is scale

 so like for example i've been recently

 doing a bunch of robots at home for my own personal pleasure

 am i going to ever use 10 story or is this more for

 there's all kinds of problems

 like they're small inference problems or small training problems there's big training problems

 what's the big goal is it the big difference

 training problems or the small training problems

 well one of the goals is to scale from 100 milliwatts to a to a megawatt

 you know so

 like really have some range on the problems

 and

 the same kind of ai programs work at all different levels

 so that's cool

 the natural since the natural

 data item is a packet that we can move around

 it's built to scale

 but so many people have you know small problems

 right right but but

 you know like inside that phone is a small problem to solve so

 do you see that storm potentially being inside a phone well

 the power efficiency of local memory local computation

 and the way we built it is pretty good

 and then there's a lot of efficiency on being able to do conditional graphs and sparsity

 i think it

 for complicated networks i want to go in a small factor it's been quite good

 um but we have to prove that that's a

 that's a fun problem and that's the early days of the company right it's a couple

 years you said

 but you think you invested you think they're legit yeah as you join yeah well that's

 well it's also it's a really interesting place to be

 like the ai world is exploding you know and

 i looked at some other opportunities like build a faster processor which people want

 yes but that's more on incremental path than

 what's going to happen in ai in the next 10 years

 so this is kind of

 you know an exciting place to be part of

 the revolutions

 will be happening in the very space

 and then lots of people are working on it but there's lots of technical

 reasons

 why some of them you know aren't going to work out that well and

 and you know that's that's interesting and there's also the same

 problem about getting the basics right like we've talked to customers about exciting features

 and at some point we realized that each unit was realizing

 they want to hear first about memory bandwidth local bandwidth compute intensity programmability

 they want to know the basics power management

 how the network ports work what are the basics do all the basics work

 because it's easy to say we got this great idea that you know the crack gbt3

 but

 the the people we talked to want to say

 if i buy that so we have a pc express card

 with our chip on it if you buy the card

 you plug it in your machine you download the driver

 how long does it take me to get my network to run

 right right you know that's a real question it's a very basic question

 so

 yeah

 is there an answer to that yet or is it trying to our goal is like

 an hour

 okay when can i buy a tesla

 pretty soon for my for the small case training yeah pretty soon

 months good i love the idea of you inside the room with the

 carpathi andre kapathi and chris ladner

 very

 um

 very interesting

 very brilliant

 people very out of the box thinkers but also like first principles thinkers

 well they both

 get stuff done

 they only get stuff done to get their own projects

 done they

 they

 talk about it clearly

 they educate

 large numbers of people and they've created

 platforms

 for other people to go do their stuff on

 yeah the the clear

 thinking

 that's able to be communicated

 is kind of impressive

 it's kind of remarkable to

 yeah i'm a fan

 well let me ask because i talked to chris actually a lot these days he's been

 one of the cool just to give him a shout out and he's been so

 supportive as a human being so everybody's

 quite different like great engineers are different but he's been like sensitive to the human element

 in a way that's been fascinating like he was one of the early people on this

 stupid podcast that i do to say like

 don't quit this thing and also

 talk to whoever the hell you want to talk to

 that kind of from a legit engineer

 to get like

 props and be like you can do this

 that was i mean that's what a good leader does right they just kind of

 let a little kid

 do his thing

 like go

 go do it let's see

 let's see

 see what turns

 out

 that that's a that's a pretty powerful thing but what do you

 um

 what's your sense about he used to be

 he no i think stepped away from google

 right

 he said sci-fi i think

 what

 what's really impressive

 to you about

 the things that chris has worked on because it's that we mentioned

 the optimization

 the compiled design stuff the llvm

 then there's he's also a google work that the tpu stuff

 he's obviously worked on swift

 so the programming language side

 talking about people that work in the entirety of the stack yeah

 what

 from your time interacting with chris

 and knowing the guy

 what's really impressive to you it just inspires you well

 well

 like llvm became

 you know the platform the de facto platform for you know compilers like it's it's amazing

 and you know it was good code quality good design

 choices

 he hit the right level of abstraction

 there's a little bit of the right time in the right place

 and then he built a new programming language called swift

 which you know after you know let's say some adoption resistance became very successful

 i don't know that much about his work at google although i know that

 you know that was the typical

 they started

 tensorflow

 stuff and they you know it was new is you know

 they wrote a lot of code

 and then at some point it needed to be refactored

 to be

 you know because it its development slowed down why

 pytorch

 started a little later and then passed it

 so he did a lot of work on that and then his idea about mlir

 which is

 what people started to realize is the complexity

 of the software stack above

 the low level

 ir

 was getting so high that forcing

 the features

 of that into a level

 was was putting too much of a burden on it so he's splitting that into multiple

 pieces

 and that was one of the inspirations for our software stack where we have

 several intermediate representations

 that are all executable

 and you can look at them and do transformations on them before you lower the level

 so that was i think we started before moir

 really got you know far enough along to use

 but we're interested in that he's really excited about that malaya

 he's that's that's his like little baby so he you know and

 there seems to be some profound

 ideas on that that are really useful so so each one of those things has been

 as the world of software gets more and more complicated

 how do we create the right abstraction

 levels to simplify it in a way that people can now work independently

 on different levels of it

 so i would say all all three of those projects allovm

 swift and mlir

 did that successfully

 so i'm interested

 what's

 what he's going to do next

 in the same kind of way

 yes

 so on either the tpu or maybe the nvidia gpu side

 how does 10 story you think or the ideas underlying it doesn't have to be testosterone

 just this kind of graph focused

 graph centric hardware

 deep learning-centric hardware beat nvidia's

 do you think it's possible for it to basically overtake nvidia sure

 what's what's that process look like what's that

 a journey look like you think well

 gpus were built around shader programs on millions of pixels

 not to run graphs

 yes so there's a hypothesis

 that says

 the way the graphs you know are built

 is going to be really interesting to be inefficient

 on computing this and then the the primitives

 is not a cmd program it's matrix multiply convolution

 and then the data manipulations

 are fairly extensive about

 like how do you do a fast transpose

 with a program

 i don't know if you've ever written the transpose program

 they're ugly and slow but in hardware you can do really well

 like i'll give you an example so

 when gpu accelerators first started doing triangles

 like so you have a triangle which maps on the set of pixels

 so you build it's very easy straightforward

 to build a hardware engine that will find all those pixels

 and it's kind of weird because you walk along the triangle to get to the edge

 and then you have to go back down to the next

 row

 and walk along

 and then you have to decide

 on the edge

 if the line of the triangle is like half on the pixel

 what's

 the pixel

 color

 because it's half of this pixel

 and half the next one that's called rasterization

 because you're saying that could be done in

 in hardware now that's an example of

 that operation

 as a software program is really bad i've written a program that did rasterization

 the hardware that does it has actually less code than

 the software program that does it and it's way faster

 right so there are certain times when the abstraction you have rasterize a triangle

 you know execute a graph you know components of a graph

 the right thing to do in the hardware software boundary is for the hardware to naturally

 do it and so the gpu

 is really optimized

 for the rasterization

 of triangles

 well no that's just well like in a modern you know

 that's a small piece of modern gpus

 what they did is

 that they still rasterize

 triangles

 when you're running the game but for the most part

 most of the computation in the area the gpu is running shader programs

 but they're single threaded programs

 on pixels not graphs

 let's be honest to say i don't actually know the the math behind shader

 shading and lighting and all that kind of stuff i don't know what

 they look like little simple floating point programs or complicated

 ones you can have 8 000 instructions in a shader program

 but i i don't have a good intuition why it could be parallelized

 so easily

 no it's because you have 8 million pixels in every single

 so when you have a light

 right yeah that comes down

 the angle you know the amount of light

 like like say this is a line of pixels across this table

 right the amount of light on each pixel is subtly different

 and each pixel is responsible

 for figuring

 out what figure it out so that pixel

 says

 on this pixel

 i know the angle

 of the light

 i know the occlusion

 i know the color i am

 like every single

 pixel

 here is a different color

 every single

 pixel

 gets a different

 amount of light

 every single pixel has a subtly different translucency

 so to make it look realistic

 the solution

 was you run a separate program

 on every pixel

 see but i thought there's a reflection

 from all over the place

 is

 every picture

 yeah but there is

 so

 so you build a reflection

 map which also

 has some pixelated

 thing

 and then when the pixel is looking at the reflection

 map it has to calculate

 what the normal of the surface is

 and it does it per pixel

 by the way there's both loads of hacks

 on that you're like you may have a lower resolution

 light map reflection map there's all these you know attacks they do

 but at the end of the day it's per pixel computation

 and it so happened that you can map

 graph like computation

 onto the this pixel essentially you could do floating point programs on convolutions

 and matrices

 and nvidia invested for years in cuda

 first for hpc and then they got lucky with the ai

 trend

 but do you think they're going to essentially

 not be able to hardcore pivot out of their we'll see

 that's always interesting how often do big companies hardcore pivot occasionally

 how much do you know about nvidia folks

 so

 some yeah

 well i'm i'm curious as well who's ultimately

 as a

 well

 they've

 innovated

 several

 times

 but they've also

 worked really hard on mobile

 they worked really hard on radios

 you know you know they're fundamentally a gpu company

 well they tried to pivot it's an interesting little

 game and play

 in autonomous vehicles right with

 or semi-autonomous

 like playing with tesla and so on and seeing that's a

 dipping a toe into that kind of pivot

 they came out with this platform which is interesting technically

 yeah but it was like a three thousand watt

 you know you know thousand watt three three thousand dollar you know gpu platform

 i don't know if it's interesting technically it's interesting philosophically

 i i

 technically i don't know if it's the execution that craftsmanship was there i'm not sure

 but that i didn't get a sense they were

 repurposing

 gpus for an automotive solution

 right it's not a real pivot they didn't they didn't build a ground-up solution

 right

 like the

 like the chips inside tesla are pretty cheap like mobile eye has been doing this

 they're they're doing the classic work from the simplest thing

 yeah you know they were building 40 mil square millimeter

 chips

 and nvidia their solution had two 800 millimeter chips and two 200 millimeter chips and

 you know like boatloads are really expensive drams and

 and you know it's a really different approach

 the mobilelite fit the let's say automotive cost and form factor

 and then they added features as it was economically

 viable and nvidia said take the biggest thing and we're gonna go make it work

 you know and and that's also influenced like waymo

 there's a whole bunch of autonomous

 startups where they have a 5000 watt server in their trunk

 right and but that's

 that's because they think well 5000 watts and you know 10 000

 is okay because it's replacing the driver

 elon's approach was that port has to be cheap enough

 to put it in every single tesla whether they turn on it autonomous driving or not

 which

 and mobileye was like

 we need to fit in the bomb and you know cost structure

 that

 car companies

# Chapter 6

 chips

 and nvidia their solution had two 800 millimeter chips and two 200 millimeter chips and

 you know like boatloads are really expensive drams and

 and you know it's a really different approach

 the mobilelite fit the let's say automotive cost and form factor

 and then they added features as it was economically

 viable and nvidia said take the biggest thing and we're gonna go make it work

 you know and and that's also influenced like waymo

 there's a whole bunch of autonomous

 startups where they have a 5000 watt server in their trunk

 right and but that's

 that's because they think well 5000 watts and you know 10 000

 is okay because it's replacing the driver

 elon's approach was that port has to be cheap enough

 to put it in every single tesla whether they turn on it autonomous driving or not

 which

 and mobileye was like

 we need to fit in the bomb and you know cost structure

 that

 car companies

 do so they may sell you a gps for 1500

 bucks

 but the bond for that's like 25

 well and

 for mobile eye it seems like neural networks

 were not first-class citizens

 like the computation

 they didn't start out as a yeah it was a cv problem yeah

 and did classic

 cv

 and found stop

 lights

 and lines

 and they were really good at it

 yeah and they never

 i mean i don't know what's happening now but they never

 fully pivoted

 i mean it's like it's the nvidia

 thing

 and then

 as opposed to so if you look at the new tesla work

 it's like neural networks from the ground up yeah right

 yeah and even tesla started with a lot of cv stuff in it and andre's

 basically been eliminating

 it

 move it move everything into the network

 so

 without

 this isn't like confidential stuff but you sitting on a porch looking over the world

 looking at the work that andre is doing that elon's doing with tesla autopilot

 do you like the trajectory

 of where things are going on the floor they're making serious progress

 i like the videos of people

 driving the beta stuff

 like it's taking some pretty complicated

 intersections and all that but it's it's still an intervention for drive

 i mean i i have autopilot the current autopilot

 my my tesla i use it every day do you have full self-driving

 beta or no no

 so you you like where this is going

 we're making progress it's taking longer than anybody thought

 you know my wonder was

 is you know hardware three is it enough computing

 off by two off by five off by ten off by a hundred yeah

 and

 and i i thought it probably wasn't enough

 but they're doing pretty well with it now yeah and one thing is

 the data set gets bigger the training gets better

 and then there's this interesting thing is

 you sort of train and build an arbitrary size network that solves the problem

 and then you refactor the network down to the thing that you can afford

 to ship

 right so the

 the goal isn't to build the network that fits in the phone it's to build

 something that actually works

 and then then how do you make that most effective on the hardware you have

 and they seem to be doing that much better than a couple years ago

 well

 the one really important thing is also

 what they're doing well is how to iterate that quickly

 which means like it's not just about one time deployment

 one building is constantly entering the network

 and trying to automate as many steps as possible right

 and that's actually the

 principles of the software 2.0 like you mentioned with andre

 is

 it's not just

 i mean i don't know what the actual his description of software 2.0

 is

 if it's just high-level philosophical or their specifics but the interesting thing about

 what that actually looks in the real world is it's that

 what i think andre calls the data engine it's like

 it's the iterative improvement of the thing you have a neural network that

 does stuff

 fails on a bunch of things

 and learns from it over and over and over so you're constantly discovering

 edge cases

 so it's very much about

 like data engineering

 like figuring out

 it's it's kind of what you were talking about with testosterone

 is you have the data landscape

 they have to walk along that data landscape in a way that

 that's constantly improving the

 the

 the neural network and that that feels like that's the central

 piece of it yeah itself

 and there's two pieces

 of it like

 you you find

 edge cases

 that don't work and then you define

 something

 that goes get your data for that

 but then the other constraint

 is whether you have to label it or not

 like the

 the amazing

 thing about like the gpt3

 stuff is it's unsupervised

 so there's essentially infinite amount of data now there's obviously infinite amount of data

 available from cars of people successfully driving

 but you know the

 the current pipelines are mostly running on labeled data which is human limited

 so when that becomes

 unsupervised

 right it it'll create

 unlimited amount of data which then they'll scale

 now the networks that may use that data might be way too big for cars

 but then there'll be the transformation

 from now we have unlimited data i know exactly what i want

 now can i turn that into something that fits in the car

 and that pro that process is going to happen all over the place

 every time you get to the place where you have unlimited data

 and that's what software 2.0 is about unlimited data training networks to do stuff

 without humans writing code to do it

 and ultimately also trying to discover like you're saying the self-supervised

 formulation of the problem so the unsupervised

 formulation of the problem like

 you know in driving there's this really interesting

 thing which is

 you look at a scene that's before you and you have data about what a successful

 human driver did

 in that scene you know one second later

 it's a little piece of data that you can use just like with gpt-3

 as training

 currently even even though tesla says they're using that it's an open question to me

 how much how far can you can you sell all of the driving

 with just

 that

 self-supervised

 piece of data

 and

 like i i think that's what comedy is doing

 that's what common ai is doing but the question is how

 how much data so what comedy ai doesn't have

 is

 as

 good of a data engine for example

 as tesla does that's where the

 like the organization

 of the data

 i mean as far as i know i haven't talked to george

 but they do have the data

 the question is how much data is needed

 because we say infinite very loosely here

 it's it's and then the other question which you said

 i don't know if you think it's still an open question is

 are we in the right order of magnitude for the compute necessary

 that

 is is this is it like what elon said this

 chip that's in there now is enough to do full self-driving

 or do we need another order of magnitude

 i think nobody actually knows the answer to that question

 i like the confidence that elon has but

 yeah we'll see

 and there's another funny thing is you don't learn to drive with infinite amounts of data

 you learn to drive with an intellectual framework that understands physics and color and horizontal surfaces

 and laws and roads and you know all your

 your experience from manipulating your environment

 like look there's so many factors go into that so then when you learn to drive

 like driving is a subset of this conceptual framework that you have

 right and so with self-driving cars right now we're teaching them to drive with driving data

 you never teach a human to do that

 you teach a human all kinds of interesting things like

 language

 like don't do that you know watch

 out

 you know there's all kinds of stuff going on

 well this is where you i think previous

 time with we talked

 about

 where you poetically

 disagreed with my naive notion about humans i just think that

 humans will will make this whole driving thing really difficult

 yeah all right

 like i said humans don't move that slow

 it's a ballistics problem

 it's a ballistic

 human zero ballistics

 problem which is like poetry

 to me

 it's very

 it's very possible

 that in driving

 they're indeed

 purely a ballistics

 problem i

 and i think that's probably the right way to think about it but

 i still

 they still continue to surprise me those and damn pedestrians the cyclists

 other humans and other cars

 and yeah but it's going to be one of these compensating things so

 like when you're driving

 you have an intuition

 about what humans are going to do but you don't have 360

 cameras

 and radars

 and you have an attention problem so yeah

 so so the self-driving

 car comes in with no attention problems 360

 cameras right you know

 a bunch of other features

 yeah so they'll wipe out a whole class of accidents

 right and you know

 you know emergency

 braking with radar and especially as it gets you know ai enhanced will eliminate

 collisions

 right

 but then you have the other problems of these unexpected

 things where you know you think your human intuition

 is helping but then the cars also have

 you know a set of hardware features that you're not even close to

 and the key thing of course is

 if you wipe out

 a huge number of kind of accidents

 then it might be just way safer than the human driver even though

 even if humans are still a problem that's hard to figure out

 yeah

 that's probably what happens

 autonomous

 cars will have

 a small number of accidents humans would have avoided

 but they'll wipe

 they'll get rid of

 the bulk of them

 what do you think about

 like tesla's dojo efforts

 or it can be bigger than tesla in general

 it's kind of like the tense torrent

 trying to innovate like this is the dichotomy like

 should a company try to from scratch build its own neural network training

 hardware

 well first i think it's great so we need lots of experiments

 right and there's lots of startups working on this and they're pursuing different things

 you know i was there when we started dojo

 and it was sort of like what's the unconstrained

 computer solution to go do very large training problems

 and then there's fun stuff like

 you know we said

 well we have this 10 000 watt board to cool

 well you go talk to guys at spacex

 and they think 10 000 watts is a really small number not a big number yeah

 and

 and there's brilliant people working on it i'm curious to see how it'll come out i

 i couldn't tell you

 you know

 i know it pivoted a few times since i left so so the

 cooling does seem to be a big problem i do like what

 elon said about it which is like we don't want to do

 the thing

 unless

 it's way better than the alternative

 whatever the alternative

 is so it has to be way better than like

 racks of gpus

 yeah and the other thing is just like you know

 you know the tesla autonomous driving hardware

 it was only serving one software stack

 and the hardware team and the software team were tightly coupled

 you know if you're building

 a general purpose ai solution

 then you know there's so many different customers

 with so many different needs

 now something andre said is i think this is amazing 10 years ago like vision recommendation

 language were completely different disciplines

 we said the people literally couldn't talk to each other and three years ago

 it was all neural networks

 but the very different neural networks

 and recently it's converging on one set of networks

 they vary a lot in size obviously they vary in data varying outputs

 but the technology

 has converged a good bit

 yeah these transformers behind gbt3

 it seems like they could be applied

 to video they could be applied to a lot of yeah

 and it's like and they're all really

 it was like to literally replace letters with pixels

 yeah it does vision it's amazing

 so and then size actually improves the thing

 so the bigger it gets the more compute you throw at it the better it gets

 the more data you have the better it gets

 so

 so so then you start to wonder well is that a fundamental

 thing or is is this

 just another step to some fundamental understanding about this kind of computation

 which is really interesting

 us humans don't want to believe that that kind of thing will achieve conceptual

 understandings you were saying like you'll figure out physics but maybe it will

 maybe probably will

 well it's worse than that

 it'll understand physics in ways that we can't understand

 i like to hear stephen will from

 talk where he said you know there's three generations of physics there was

 physics by reasoning well big things should false faster than small things right that's reasoning

 and then there's

 physics by equations

 like you know

 but the number of programs in the world that are solved with the single equations relatively

 low almost all programs have you know

 more than one line of code maybe 100 million lines of code

 so you said that now we're going to

 physics by equation which is his project which is cool

 i might point out that there was there was two two generations of physics before reasoning

 habit

 like all animals you know know things fall and you know birds fly and

 you know predators know how to you know solve a differential equation to cut off a

 accelerating you know

 curving animal path yep and then there was you know the gods did it

 right

 so yeah right so you know there's five generations now

 software 2.0 says programming things is not the last step

 data so there's going to be a physics past stephen's wolfram's com that's not explainable

 and and actually

 there's no reason that i can see while that even that's the limit

 like there's something beyond that

 i mean they're usually like usually when you have this hierarchy

 it's not like

 well if you have this step in this step in this step and they're all qualitatively

 different

 and conceptually

 different

 it's not obvious

 why

 you know six

 is the right hand number of hierarchy

 steps

 in not seven

 or eight or

 well then it's

 probably impossible

 for us to

 to comprehend

 something that's beyond the thing that's not explainable

 yeah because i think but the thing that you know understands the thing that's unexplainable

 to us

 we'll conceive the next one and

 like i'm not sure why there's a limit to it

 your brain hurts that's the sad story

 if if we look at our own brain which is an interesting illustrative example

 in your work with testor and trying to design deep learning architectures

 do you do you think about the brain at all maybe from a

 hardware designer perspective

 if you could

 change something about the brain what would you change or do funny question

 like how would you so your brain is really weird

 like you know your cereal cortex where we think we do most of our thinking

 is what like six or seven neurons thick

 yeah like that's weird like all the big networks are way bigger than that

 like way deeper so that seems odd

 and then

 you know when you're thinking if it's if

 if the input

 generates

 a result you can lose it goes really fast but if it can't

 that generates an output that's interesting which turns into an input and then your brain

 to the point where you mold things

 over for days

 and how many

 trips

 through your brain

 is that

 right

 like it's you know

 300 milliseconds or something to get through seven levels of neurons i forget the number exactly

 but then it does it over and over and over as it searches

 and the brain clearly

 is looks like some kind of graph because you have a neuron

 with you know connections and it talks to other ones and

 it's locally very computationally

 intense but it's also

 does sparse computations across a pretty big area

 there's a lot of messy biological type of things and it's it's

 meaning like

 first of all there's mechanical chemical and electrical signals that's all that's going on

 then the there's a the asynchronicity

# Chapter 7

 to the point where you mold things

 over for days

 and how many

 trips

 through your brain

 is that

 right

 like it's you know

 300 milliseconds or something to get through seven levels of neurons i forget the number exactly

 but then it does it over and over and over as it searches

 and the brain clearly

 is looks like some kind of graph because you have a neuron

 with you know connections and it talks to other ones and

 it's locally very computationally

 intense but it's also

 does sparse computations across a pretty big area

 there's a lot of messy biological type of things and it's it's

 meaning like

 first of all there's mechanical chemical and electrical signals that's all that's going on

 then the there's a the asynchronicity

 of signals

 and there's like there's just a lot of variability that seems continuous

 and messy and just a mess of biology

 and it's unclear whether that's a good thing yeah or it's a bad thing because if

 if it's a good thing that we need to run the entirety of the evolution

 well we're going to have to start with basic bacteria to create some imaging we could

 you could build a brain with 10 layers would that be better or worse

 or more more connections or less connections

 or you know we don't know to what level our brains are optimized

 but if i was changing

 things like

 yeah like you know you can only hold like seven numbers

 in your head

 yeah like why not 100 or a million

 never thought of that

 like and why can't like why can't we have like a floating point processor

 that can compute anything we want

 like and see it all properly like that would be kind of fun

 and why can't we we see in four or eight dimensions

 like because you know 3d is kind of a drag

 like all the hard mass transforms are up in multiple dimensions

 so there's that you know you could imagine a brain architecture that

 you know you could

 enhance with a whole bunch of features that would be

 you know really useful for thinking about things it's possible that the limitations

 you're describing are actually

 essential

 for like the constraints are essential for creating

 like the depth of intelligence like that

 the ability to reason

 you know it's hard to say because like your brain is clearly a parallel processor

 you know you know

 10 billion neurons talking to each other at a relatively

 low clock rate

 but

 it produces

 something that looks like a serial

 thought process

 it's a serial narrative in your head

 that's true right but then there are people famously who are visual thinkers

 like

 i think i'm a relatively visual thinker

 i can imagine any object and rotate it in my head and look at it

 and there are people who say they don't think that way at all

 and recently i read an article about people

 people who say they don't have a they don't have a voice in their heads

 they can talk

 but when they you know it's like well what are you thinking

 they'll they'll describe something that's visual

 so that's curious

 now

 if if you're saying

 if we dedicated

 more hardware to holding information

 like you know 10 numbers or a million numbers

 like would that

 just distract us from our ability to form this kind of singular

 identity like it dissipates

 somehow right

 but but maybe

 you know future humans will have many identities

 that

 have some higher level organization but can actually do lots more things in parallel

 yeah there's no reason if we're thinking modularly there's no reason we can't have multiple consciousnesses

 in one brain yeah and maybe there's some way to make it faster so that the

 you know the the area the computation could

 could still have a unified

 feel to it

 but while still having way more ability

 to do parallel stuff at the same time

 could definitely be improved

 it could be improved

 okay well

 it's it's

 pretty good right now actually

 people don't give it enough credit the thing is pretty nice the

 the you know the the fact that the right ends seem to be

 on give a nice like spark

 of

 beauty to the whole experience

 i don't know i don't know if it can be improved easily

 it could be more beautiful

 i don't know how yeah what do you mean

 what do you mean how

 all the ways you can't imagine

 no but that's the whole point

 i wouldn't be able to i'm at

 the fact that i can imagine

 ways

 in

 in

 in which it could be more beautiful

 means so do you know you know ian banks his stories so the the super smart

 ais there live mostly live in the world of what they call infinite fun

 because they can create arbitrary worlds

 so they interact

 and you know the story

 has it they interact

 in the normal

 world and they're very smart

 and they can do all kinds of stuff

 and

 you know a given

 mind can

 you know talk to a million

 humans

 at the same time because we're very

 slow

 and

 for reasons you know artificial the story

 they're interested in people and doing stuff but they mostly live in this

 this other land of thinking my

 inclination is to think that the ability to create infinite fun will

 um will not be so fun

 that's sad

 there are so many things to do imagine be able to make a star

 move planets around

 yeah

 yeah but because we can imagine that as wildlife

 is fun

 if we can if we actually were able to do it it'd be a slippery slope

 where fun wouldn't even have a meaning because we just consistently

 desensitize ourselves by the infinite amounts of fun we're having

 and the sadness the the dark stuff is what makes it fun i think i

 mean that could be the russian

 it could be the could be the fun makes it fun and the sadnesses

 makes it bittersweet

 yeah that's true fun could be the thing that makes it fun

 so what do you think about the expansion

 not through the biology side but through the bci the brain computer interfaces

 yeah you got a chance to check out the neural link stuff it's super interesting

 like like humans like

 like our thoughts to manifest as action

 you know like

 like as a kid you know like shooting a rifle was super fun

 driving a mini bike

 doing things

 and then computer games i think for a lot of kids became the thing where they

 you know they can do what they want they can fly

 a plane

 they can do this they can do this

 right

 but you have to have this physical interaction now imagine

 you know you could just imagine stuff and it happens

 right

 like really richly

 and interestingly

 like we kind of do that when we dream like dream dreams are funny because

 like if you have some control or awareness in your dreams

 like it's very realistic looking

 or not realistic

 it depends on the dream

 but you can also manipulate that

 and you know what what's possible there is

 is is odd and the fact that nobody understands it's hilarious but

 um do you think it's possible to expand that capability through computing sure

 is there some interesting so from a hardware designer perspective is there

 do you think you'll present totally new challenges and the kind of hardware that required

 that like so this hardware isn't

 standalone

 computing well this just knows

 today computer games are rendered by gpus

 right right so but you've seen the gans stuff yep right where

 trained neural networks

 render realistic images but there's no pixels no triangles

 no shaders no light maps no nothing

 so the future of graphics is probably ai

 right yes now that ai is heavily trained by lots of real data

 right so if you have an interface with a aai renderer

 right so if you say render a cat

 it won't

 say

 well

 how

 tall is the cat and how big it you know it'll render

 a cat

 and you might say well a little bigger a little smaller

 you know

 make it a tabby

 shorter hair you know like you could tweak it

 like the the amount of data you'll have to

 send to interact with a very powerful ai renderer could be low but the question is

 for brain computer interfaces would need to

 render not onto a screen but render onto the brain

 and

 like directly

 so that there's a bandwidth

 you could do it both ways

 i mean our eyes are really good sensors

 it could render onto a screen

 and we could feel like we're participating

 in it you know they're gonna

 they're gonna have you know like the oculus

 kind of stuff

 it's gonna be so good when a projection

 to your eyes you think it's real

 you know they're slowly solving those problems

 and i suspect

 when the renderer of that information into your head is also ai mediated

 you know they'll be able to give you

 the cues

 that

 you know you really want for depth and all kinds of stuff

 like

 your your brain is probably faking

 your your visual field right

 like your eyes are twitching around but you don't notice that occasionally

 they blank you don't notice that

 you know there's all kinds of things

 like you think you see over here but you don't really

 see there

 yeah

 it's all fabricated

 yeah so yeah peripheral vision is fascinating

 so if you have an ai renderer that's trained to understand exactly how you see

 and the kind of things that enhance the realism of the experience

 it could be super real actually

 so i don't know what the limits that are

 but obviously

 if if we have a brain interface that goes in

 inside

 your

 you know visual cortex in a better way than your eyes do which is possible

 it's a lot neurons

 yeah

 um

 maybe that will be even cooler

 well the really cool thing is it has to do with the

 the infinite

 fun that you're referring

 to

 which is

 our brains seem to be very limited

 and like you said computational

 so very plastic

 very plastic yeah yeah so it's a it's a com interesting combination

 now the the interesting open question is the limits of that neuroplasticity like how

 how flexible

 is that thing because we don't we haven't really tested it

 we know about that experiments where they they put like a pressure pad on somebody's head

 and had a visual transducer

 pressurize it and somebody slowly learned to see yep that's like it's

 especially

 at a young age

 if you throw

 a lot at it

 like

 what

 what can it

 can it completely so can you like arbitrarily expand it with computing power so

 connected to the internet directly somehow yeah the answer's probably yes

 so the problem with biology

 and ethics is like there's a mess there like us humans are

 perhaps unwilling to take

 risks in

 into directions that are full of uncertainty

 so that's like 90

 of the population is unwilling to take risks the other 10

 is rushing into the risks

 unaided by any infrastructure whatsoever

 and

 you know and that that's where all the fun happens in you know society

 there's been huge transformations

 yeah in the last you know a couple thousand years

 yeah it's funny i mean i got a chance to interact with

 this is matthew johnson from johns hopkins he's doing this large-scale study of psychedelics

 it's it's becoming

 more and more

 i've gotten a chance to interact

 with that community

 of scientists

 working on psychedelics

 but because of that that opened the door to me to

 all these

 what are they called psychonauts

 the people who like you said the ten percent who like

 i don't care i don't know if there's a science behind this i'm taking the spaceship

 to

 if i'm being the first on mars i'll be

 the you know you know psychedelic's interesting in the sense that

 in another dimension

 like you said it's a way to explore the

 with the limits of the human mind like

 what is this thing capable of doing

 because you kind of like when you dream

 you detach it i don't know exactly in your science of it but you detach your

 like reality from

 what your mind

 the images

 your mind is able to conjure

 up and your mind goes into weird

 places

 and like entities appear

 freudian type of

 like trauma is probably connected in there somehow but you start to have like these

 weird vivid worlds that like so do you actively dream

 do you why not

 i had like six six hours of dreams and i it's like really useful time

 i know i do i haven't

 i don't for some reason i just knock out and

 i have sometimes like anxiety inducing kind of like very pragmatic

 like nightmare type of dreams but not nothing fun nothing nothing fun nothing fun

 i i try i unfortunately have mostly have fun

 in the waking world which is very limited in the amount of fun you can have

 it's not that limited either yeah that's what we'll have to talk

 yeah i need instructions yeah there's like a manual for that you might wanna

 i looked it up i'll ask elon what what did you dream

 you know years ago and i i read about you know

 like you know a book about how to have

 you know become aware of your dreams

 i worked on it for a while like there's this trick about

 you know imagine you can see your hands and look out and

 and i got somewhat good at it like

 but my mostly

 when i'm thinking about things or working on problems i i

 i prep myself before i go to sleep it's like i i pull into my

 mind all the things i want to work on or think about

 and then

 that let's say greatly improves the chances that i'll i'll work on that while i'm sleeping

 and then and then i also you know basically asked to remember it

 and i often remember

 very detailed

 within the dream yeah or outside the dream well

 to bring it up in in my dreaming

 and then remember it when i wake up

 it's just it's more of a meditative practice you say

 you know to prepare yourself to

 do that

 like if you go to you know the sleep still

 gnashing your teeth about some random thing that happened

 that you're not that really interested in you'll dream about it

 that's really interesting maybe but but you can direct your dreams

 somewhat by prepping

 you know i'm going to try that it's really interesting

 like the most important the interesting not like

 what what did this guy send

 in an email kind of like stupid

 worry stuff but like fundamental

 problems you're actually concerned about

 prepping and interesting things you're worried about or just

 you're reading or you know some great conversation

 you had or something

 some adventure you want to have like there's there's a lot of

 space there

 and

 and it seems to work

 that

 you know my percentage of interesting dreams and memories went up

 is there

 is that the source of

 if you were able to deconstruct like where some of your best ideas came from

 do is there a process

 that's at the core of that yeah like so some people you know

 walk and think some people like in the shower the best ideas hit them

 if you talk about like newton

 apple hitting them on the head

 no i i found that a long time ago i'm i process things somewhat slowly

 so like in college

 i had friends that could study at the last minute get an a next day

 i can't do that at all

 so i always front loaded all the work like i do all the problems

# Chapter 8

 you had or something

 some adventure you want to have like there's there's a lot of

 space there

 and

 and it seems to work

 that

 you know my percentage of interesting dreams and memories went up

 is there

 is that the source of

 if you were able to deconstruct like where some of your best ideas came from

 do is there a process

 that's at the core of that yeah like so some people you know

 walk and think some people like in the shower the best ideas hit them

 if you talk about like newton

 apple hitting them on the head

 no i i found that a long time ago i'm i process things somewhat slowly

 so like in college

 i had friends that could study at the last minute get an a next day

 i can't do that at all

 so i always front loaded all the work like i do all the problems

 early you know for finals like the last three days i wouldn't look at a book

 because i want you know because

 like a new fact the day before finals may screw up my understanding

 of what i thought i knew so my

 my goal was to always get it in

 and and give it time to soak

 and

 i used to you know

 i remember we were doing like 3d calculus

 i would have these amazing dreams of 3d

 surfaces

 with normal

 you know calculating the gradient and this is like all come up so it was

 really fun

 like very visual

 and and if i got cycles of that that was useful

 um and the other is don't over filter your ideas like i like that process of

 brainstorming

 where lots of ideas can happen i like people who have lots of ideas

 and things but that's what's up

 then there's a yeah let them sit and let it breathe a little bit

 and then reduce it to practice like at some point you really have to

 does it really work like you know is this real or not

 right but you but you have to do both there's creative

 tension there like how do you be both open

 and

 you know precise

 if you had ideas that you just

 that sit in your mind for like years

 before the

 sure

 it's an interesting way to

 is generate ideas and just let them sit let them sit there for a while

 i think i have a few of those ideas you know that was so funny

 yeah i think that's

 you know creativity this one or something

 for the slow thinkers in the in the room i suppose

 as i some people like you said are just like

 like the yeah it's really interesting like there's so much diversity in how people think

 you know how fast or slow they are how well they remember don't

 like you know i'm not super good at remembering facts but processes and methods

 like in our engineering i went to penn state and almost all our engineering

 tests were open book i could remember the page and not the formula

 but as soon as i saw the formula i could remember the whole method

 if i if i'd learned it

 yeah you know so it's just a funny

 or some people could

 you know i i

 swatched

 friends

 like flipping

 through the book trying to find the formula

 even knowing that they'd done just as much work

 and i would just open the book i was on page 27

 about half i could see the whole thing visually

 yeah

 and you know

 and you have to learn that about

 yourself

 and figure out what to do with the

 function

 optimally

 i had a friend who he was always concerned

 he didn't know how he came up with ideas

 he had lots of ideas but he said they just sort of popped up

 like you'd be working on something having this idea like where does it come from

 but you can have more awareness of it like like

 like

 like how you

 how your brain works is a little murky

 as you go down

 from the voice

 in your head or the obvious

 visualizations

 like when you visualize something how does that happen

 yes you know if i say you know visualize volcano

 it's easy to do right

 and what does it actually look like when you visualize

 it i can visualize

 to the point where i don't see

 very much out of my eyes and i see the colors

 of the thing i'm

 visualizing

 yeah but there's like a

 there's a shape there's a texture

 there's a color but there's also conceptual

 visualization

 like

 what are you actually visualizing

 when you're visualizing volcano

 just like with peripheral vision you think you see the whole thing yeah yeah

 that's a good way to say it you know you have this kind of

 almost peripheral vision of your visualizations

 they're like these ghosts

 but if you know if you

 if you work

 on it you can get a pretty high

 level

 of detail

 and somehow you can walk along those visualizations to come up with an idea which is

 but weird but when you're thinking about solving problems

 like you're you're putting information and you're exercising the stuff you do know

 you're sort of teasing the area that's you don't understand and don't know

 but you can almost you know feel

 you know that process happening you know that's that's how i like

 like like i know sometimes when i'm working really hard on something like

 like i get really hot when i'm sleeping and you know it's like

 we got the blank throw i wake up all the blankets are on the floor

 and you know every time it's while i wake up and think wow that was great

 you know are you able to

 to reverse engineer what the hell happened there oh sometimes it's vivid dreams and sometimes

 it's this kind of like you say like shadow

 thinking that you you sort of have this feeling

 you're

 you're going through this stuff but it's it's not that obvious

 isn't that so amazing that the mind just does all these little

 experiments

 i never

 you know i thought i always thought

 it's like a river that you can't you're just there for the ride

 but you're right if you prep it

 no it's all understandable

 meditation

 really helps

 you you got to start figuring out you need to learn language of your own mind

 and there's multiple levels of it

 but the abstractions again right it's somewhat comprehensible

 and observable and

 feelable or whatever the right word is no it's

 you know you're not long for the ride you are the ride

 i have to ask you hardware engineer working on neural networks now

 what's consciousness what the hell is that thing is that

 is that just some little weird quirk of our particular

 computing device

 or is it something fundamental

 that we really need to crack open if we're to

 to build like good computers

 do you ever think about consciousness

 like why it feels like something to be i know it's it's it's really weird

 so yeah

 i mean everything about it is weird first it's a half a second behind reality

 right it's a post-hoc narrative about what happened you've already done stuff

 by the time you're conscious of it

 and your consciousness

 generally is a single threaded thing but we know your brain is 10 billion neurons

 running some crazy

 parallel thing

 and there's a really big sorting

 thing going on there it also seems to be really reflective

 in the sense that

 you create a space in your head right like we don't really see anything right like

 photons hit your eyes it gets turned into signals it goes through multiple layers the neurons

 you know like

 i'm so curious that you know that looks glassy

 and that looks not glassy

 like like how the resolution

 of your vision is so high you have to go through all this processing

 yeah where for most of it it looks nothing like vision

 okay like like there's no theater in your mind

 right so we we have a world in our heads

 we're literally just isolated

 behind our sensors but we can look at it speculate about it speculate about alternatives

 problem solve what if you know there's so many things going on

 and that process is lagging reality

 and it's single threaded

 even though the underlying thing is like massively parallel so it's so

 curious

 so imagine you're building an ai computer if you wanted to replicate

 humans well you'd have huge arrays of neural networks and

 apparently only six or seven deep which

 clarious

 they only remember seven numbers but i think we can upgrade that a lot

 right and then

 somewhere in there

 you would train the network to create basically

 the world that you live in

 right so like tell stories to itself about the world that it's perceiving

 well create this create the world tell stories in the world

 and then have many dimensions

 of

 you know

 like sideshows to it like we have an emotional structure like we have a biological

 structure

 and that seems hierarchical too like

 like if you're hungry it dominates your thinking if you're mad it dominates your thinking

 like

 and we don't know if that's important to consciousness or not but it certainly

 disrupts

 you know in truths in the consciousness

 like so there's lots of structure to that

 and

 we like to dwell

 on the past

 we like to think about the future

 we like to imagine

 we'd like to fantasize

 right and the somewhat circular observation of that is the thing we call consciousness

 now if you created

 a computer

 system

 it did all things create

 world views

 created

 future

 alternate

 histories

 you know dwelled on past events you know accurately or semi-accurately

 you know it's it's

 consciousness just bring up like natural well would that feel look and feel conscious to you

 like do you think

 do you think the thing that looks conscious is conscious like do you

 again this is like an engineering kind of question i think because

 like

 if we want to engineer consciousness is it okay to engineer something that just looks conscious

 or is it is there a difference between well we have all consciousness

 because it's a super effective way to manage our affairs

 yeah it's right the social development yeah well it gives us the planning system

 you know we have a huge amount of stuff

 like when we're talking

 like the reason we can talk really fast is we're modeling

 each other a really

 high level of detail and consciousness

 is required for that right and well

 all those components together manifest consciousness

 right so if we make intelligent

 beings that we want to interact with that we're like

 you know wondering what they're thinking you know you know looking forward to seeing them

 you know when they interact with them they they're interesting surprising

 you know fascinating

 you know

 they will probably

 feel conscious like we do and we'll we'll perceive them as conscious

 i don't know why not but you never know another fun question on this because

 in in from a computing perspective we're trying to create something that's human-like or superhuman-like

 let me ask you about aliens aliens

 do you think there's intelligent alien civilizations out there and do you think their

 technology their computing their ai bots

 their their chips are of the same nature as ours

 yeah i got i have no idea

 i mean

 if there's lots of aliens out there they've been awfully quiet

 you know there's there's speculation about why

 there seems to be more than enough planets out there there's a lot yeah

 um

 there's intelligent life on this planet that seems quite different you know like

 you know dolphins seem like plausibly understandable octopuses don't seem understandable at all

 if they live longer than a year maybe they would be running the planet

 they seem really smart and their neural architecture is completely different than ours

 now who knows how they perceive things

 i mean that's the question is for us intelligent

 beings who might not be able to perceive other kinds of intelligence

 if they become sufficiently different than us so yeah

 we live in the current constrained world that you know it's three-dimensional geometry

 and the geometry defines a certain amount of physics

 and you know you know there's like how time works seems to work

 like there's so many things that

 seem like a whole bunch of the input parameters

 to the you know another conscious being are the same

 yes like if it's biological biological things seem to be in a relatively narrow temperature range

 right because you know organic stones aren't stable too cold or too hot

 you know so so there's if you specified the list of things that

 input to that but as soon as we make really smart

 you know beings

 and they go solve

 about how to think about a billion

 numbers

 at the same time

 and

 and how to think in n

 there's a funny science fiction book where the all the society had uploaded into this matrix

 and at some point some some of the beans in the matrix thought

 i wonder if there's intelligent life out there

 so they had to do a whole bunch of work to figure

 out

 like how to make a physical

 thing

 because their matrix was self-sustaining

 and they made a little spaceship

 and they traveled to another planet when they got there there was like life running around

 but there was no intelligent life

 and then they figured out that there was these huge

 you know organic matrix all over the planet inside there where intelligent beings had uploaded themselves

 into that matrix

 so everywhere intelligent life was as soon as it got smart

 it up leveled itself into something way more interesting than 3d geometry and yeah it escaped

 whatever this is not escaped

 better yeah the the essence of what we think of as an intelligent being

 i tend to like the

 thought experiment of

 the organism like humans aren't the organisms

 i like the notion of like richard dawkins and memes that

 ideas themselves are the organisms

 like that are just using our minds to evolve so like we're just like meat receptacles

 for ideas to breed and multiply and so on and maybe those are the aliens yes

 so

 jordan peterson

 has a line says

 you know you think you have ideas but ideas have you

 yeah right good line which

 and and then we know about the phenomena of groupthink

 and there's so many things that constrain us

 but i think you can examine all that and not be

 completely owned by the ideas and completely sucked into groupthink

 and part of your responsibility as a as a human

 is to escape that kind of phenomena

 which isn't

 you know it's you know it's it's one of the creative tension things again you're constructed

 by it

 but you can still observe

 it and you can think about it and you can make choices

 about

 to some level

 how constrained you are by it

 and you know it's useful to do that

 and

 but but at the same time

 and it could be by doing that

 that you know

 the

 the the group and society

 you're

 you're part of becomes collectively even more interesting

 so you know so the outside observer will think wow

 you know all these lexus running around with all these really independent

 ideas have created

 something even more interesting

 and aggregate

 so

 so i so i don't know i'm

 those are lenses to look at the situation

 but i'll give you some inspiration but i don't think they're constrained

 right you know as a small little quirk of history it seems like you're

 related to jordan peterson like you mentioned he's going through some rough stuff now

 is there some comment you can make about the the roughness of the human journey

 the ups and downs

 well

 i i became an expert in benzo withdrawal

 like which is you took benzodiazepines and at some point they interact with gaba circuits

# Chapter 9

 the

 the the group and society

 you're

 you're part of becomes collectively even more interesting

 so you know so the outside observer will think wow

 you know all these lexus running around with all these really independent

 ideas have created

 something even more interesting

 and aggregate

 so

 so i so i don't know i'm

 those are lenses to look at the situation

 but i'll give you some inspiration but i don't think they're constrained

 right you know as a small little quirk of history it seems like you're

 related to jordan peterson like you mentioned he's going through some rough stuff now

 is there some comment you can make about the the roughness of the human journey

 the ups and downs

 well

 i i became an expert in benzo withdrawal

 like which is you took benzodiazepines and at some point they interact with gaba circuits

 you know to reduce anxiety and do 100 other things like there's actually

 no known list of everything

 they do because they interact with so many parts of your body

 and then once you're on them you habituate

 to them and you're you're

 you have a dependency

 it's not like you're a drug dependency we're trying to get high it's a

 it's a

 metabolic dependency

 and then if you discontinue them

 there's a funny thing called kindling

 which is if you stop

 them and then go you know you'll have a horrible it's for all symptoms

 if you go back on them at the same level you won't be stable

 and

 that unfortunately happened to him

 because it's so deeply

 integrated

 into all the kinds of systems

 in the body it literally

 changes

 the size and numbers

 of

 neurotransmitter

 sites in your brain yeah

 so there's a there's a

 process called the ashton protocol where you taper it down slowly over two years

 to people go through that goes through unbelievable

 hell

 and what jordan went through seemed to be worse because

 the on advice of doctors you know we'll stop taking these and take this

 it was the disaster

 and

 he got some yeah it was pretty tough

 um

 he seems to be doing quite a bit better intellectually

 you can see his brain clicking back together

 i spent a lot of time with i've never seen anybody suffer so much

 well his brain is also like this powerhouse right so i wonder

 does a brain

 that's able to think deeply about the world suffer more through these kinds of withdrawals like

 i don't know i've watched videos of people going through withdrawal

 they they all seem to suffer

 unbelievably

 and you know my work goes out to everybody

 and there's some funny math about this some doctors said as best you can tell

 you know there's the standard recommendations

 don't take them for more than a month and then taper over a couple of weeks

 many doctors prescribe them endlessly which is against the protocol but it's common

 right and then

 something like 75 percent of people when they taper it's you know

 half the people have difficulty but 75

 get off okay

 20 have severe difficulty and 5 have life-threatening difficulty

 and if you're one of those it's really bad

 and the stories that people have on this is

 heartbreaking

 and

 tough

 so you put some of the fault that the doctors

 that just not know what the hell they're doing oh no

 it's hard to say it's

 it's one of those commonly prescribed things like one doctor said what happens is

 if you're prescribed them for a reason and then you have a hard time getting off

 the protocol basically says you're either crazy or dependent

 and you get kind of pushed into

 a different treatment regime you're a drug drug addict or a psychiatric patient

 and so

 like one doctor

 said you know i prescribed

 me for 10 years thinking i was helping my patients

 and i realized

 i was really

 harming

 them

 and you know the awareness of that is slowly coming up

 the fact that they're casually prescribed to people is horrible

 and it's bloody scary

 and some people are stable on them but they're on them for life

 like once you know it's another one of those drugs

 that

 but benzo's long range have real impacts on your personality

 people talk about the benzo bubble where you get disassociated

 from reality and your friends a little bit

 it's it's it's it's really terrible the mind is terrifying we were talking about how

 how the infinite possibility of fun

 but like

 it's the infinite possibility of suffering too which is one of the dangers of

 like expansion of the human mind it's like

 i wonder if all the possible huma experiences that a intelligent computer can have

 is it mostly fun or is it mostly

 suffering

 so like if you if you brute force expand

 the set of possibilities like are you going to run into some trouble

 in terms of like torture and suffering and so on

 maybe our human brain is just protecting

 us from

 much more possible pain and suffering

 maybe the space of pain

 is like much larger than we could possibly imagine and that the world's in the balance

 you know all the all the literature

 on religion and stuff is you know the struggle between

 good and evil is

 is balanced versus

 very finely tuned for reasons that are complicated

 but that's a that's a long philosophical conversation

 speaking of balance that's complicated

 i i wonder because we're living through one of the more important

 moments in human history with this particular virus

 it seems like pandemics

 have at least the ability to

 kill off most of the human population

 at their worst

 and they're just fascinating because there's so many viruses

 in this world there's so many i mean viruses

 basically around the world in the sense that

 they've been around very long time they're everywhere

 they seem to be extremely powerful and they're just in a distributed

 kind of way but at the same time they're not intelligent

 and they're not even living

 do you have like high level thoughts about this virus that

 like in terms of you being fascinated about terrified or not somewhere in between

 so i believe in frameworks right so

 like one of them is the evolution

 like we're evolved creatures right yes

 and one of the things about evolution is it's hyper competitive

 and it's not competitive

 out of a sense of evil it's competitive in the sense of there's endless variation

 in variations that work better when

 and then over time there's so many levels of that competition

 you know like multi-cellular life partly exists because of

 you know the the competition between you know different kinds of life forms

 and we know sex partly exists to scramble our genes so that we have

 you know genetic variation against

 the invasion of the bacteria and the viruses and it's endless

 like

 i read some funny statistic

 like the density

 of viruses

 and bacteria in the ocean is really high

 and one third of the bacteria die every day because the virus is invading them

 like one-third of them

 wow

 like like i don't know if that number is true but it was like it's

 like there's like the amount of competition

 and what's going on is stunning

 and there's a theory as we age we slowly accumulate

 bacterias

 and viruses

 and as our immune system kind of

 goes down you know that's what slowly kills us and

 it just feels so peaceful from a human perspective

 when we sit back and they're able to have a relaxed conversation

 and there's wars going on out there like right now

 you're you're harboring how many bacteria and you know the ones

 many of them are parasites

 on you and some of them are helpful and some of them are modifying

 your behavior and some of them are

 you know it's just really it's really wild

 but you know this particular manifestation is unusual

 you know in the demographic

 how it hit and the political

 you know response that it engendered

 and you know the health care response it engendered

 and the technology

 it's gendered it's kind of wild

 yeah the communication

 on twitter that it

 every level all that kind of stuff at every single level yeah but but

 what usually kills life the big extinctions

 are caused by

 meteors and volcanoes

 that's the one you're worried about as opposed to human-created bombs

 solar flares are another good one

 you know occasionally solar flares hit the planet

 so it's nature

 oh yes yeah it's all pretty wild

 on another historic moment this is perhaps outside but perhaps within your

 space of frameworks that you think about that just happened

 i guess a couple weeks ago is um

 i don't know if you're paying attention at all it's the

 the game stop and

 wall street bets

 so it's really fascinating

 there's kind of a theme to this conversation

 today because it's like you know that works the

 it's cool how there's a large number of people in a distributed way

 almost having a kind of fun we're able to take on the powerful elites

 elite hedge funds centralized powers and overpower them

 do you have thoughts i mean saga

 i don't know enough about finance but it was like the elon

 you know robin hood guy when they talked yeah what do you think about that

 well the robin guy didn't know how the finance system worked

 that was clear

 right he was treating like the the people who settled the transactions

 as a black box

 and suddenly somebody called him up and said hey black box calling you

 your transaction

 volume

 means you need to put up three billion

 dollars

 right now and he's like i don't have three billion dollars

 like i don't even make any money on these trades

 why do i owe three billion

 dollars while you're sponsoring

 the trade

 so so there was a set of abstractions

 that

 you know i don't think either like like now he understands

 it like this happens in chip design like

 you buy wafers from tsmc

 or samsung or intel

 and

 you know they say it works

 like this and you do your design

 based on that and then chip comes back and doesn't work

 and then suddenly you start having to open the black boxes

 like the transistors

 really work like they said you know what's the real issue

 so

 so the

 there's a whole set of things that created this opportunity and somebody spotted it now

 people spot these kinds of opportunities all the times there's been flash crashes there's been

 you know there's always short squeezes are fairly regular

 every ceo i know hates the shorts

 because they're they're manipulating

 they're trying to manipulate their stock in a way that they make money

 and you know deprive value from both this you know the company and the investors

 so the fact that

 you know some of these stocks were so short it's hilarious

 that this hasn't happened before i don't know why and i don't actually know why

 some serious hedge funds didn't do it to other hedge funds

 and some of the hedge funds actually made a lot of money on this yes

 so

 my my guess is we know five percent of what really happened

 and that a lot of the players don't know what happened and

 the people who probably made the most money aren't the people that they're talking about

 yeah that's

 do you think there was something

 i mean this is the this is the cool kind of

 elon

 you're the same kind of conversationalist

 which is like first principles questions of like what the hell happened

 just very basic questions of like was there something shady going on

 what

 you know who are the parties

 involved

 it's the basic

 questions

 that everybody

 wants to know about

 yeah so like we're in a very hyper competitive

 world right but transactions like buying and selling stock is a trust event

 you know i trust the company representing themselves properly

 you know i bought the stock because i think it's going to go up

 i trust that the regulations are solid

 now inside of that there's all kinds of places where you know humans over trust and

 you know this this expose let's say some weak points in the system

 i don't know

 if it's going to get corrected i don't know if the

 i don't know if we have close to the real story

 yeah my suspicion is we don't

 yeah and listen to that guy he was like a little wide-eyed

 about and then he did this and then they did that and it was like

 i think you should know more about that your business than that

 but again there's many businesses when like this layer is really stable

 you stop paying attention to it

 you pay attention to the stuff that's bugging you or new

 you don't pay attention

 to the stuff that just seems to work all the time you just

 you know the sky's blue every day california

 and where once a while the continued rains there was like what do we do

 somebody go bring in the lawn furniture

 you know like

 it's getting

 wet

 we don't know it's getting wet

 yeah it doesn't it was blue for like 100

 days and now it's

 you know so

 but

 part of the problem here with vlad this the ceo of robin hood is the scaling

 is that what we've been talking about is

 there's a lot of

 unexpected things that happen with the scaling and you have to be

 i think the scaling forces you to then return to the fundamentals

 well it's interesting because when you buy and sell stocks the scaling

 is you know the stocks

 only move in a certain

 range

 and if you buy a stock you can only lose that amount of money

 on the short short market you can lose a lot more than you can benefit

 like it has a it has a weird

 cost you know cost function or whatever the right word for that is

 so he was trading in a market where he wasn't actually capitalized

 for the downside

 if it got outside a certain range

 now whether something the various has happened i have no idea but at some point the

 financial risk to both him and his customers was way outside of his financial capacity

 and his understanding how the system work was clearly

 weak or or he didn't represent himself i you know i don't know the person

 when i listened to him nick

 yeah it could have been the surprise question was like and then these guys called and

 you know it sounded like

 he was treating stuff as a black box

 maybe he shouldn't have

 but maybe his whole pilot

 expert somewhere

 else and it was going on i don't i don't know

 yep

 i mean this is

 this is one of the qualities

 of

 a good leader is under fire you have to perform

 and that means to think clearly and to speak clearly

 and he dropped the ball on those things because

 and understand the problem quickly learn and understand the problem like at this like

 basic level like what the hell happened

 and my guess is

 you know at some level it was amateurs trading against

 you know expert slash insiders slash people with you know special information

 outsiders is insiders

 yeah and the insiders

 you know my guess is the next time this happens we'll make money on it

 the insiders always win

 well they have more tools and more incentive i mean this always happens like the outsiders

 are doing this for fun the insiders are doing this 24 7.

 but there's numbers in the outsiders

 this is the interesting thing well there's numbers on the insiders too

 like different kind of numbers different kind of numbers

 but this could be a new era

 because

 i don't know at least i didn't

 expect

 that

 a bunch of redditors

 could you know there's

 you know millions of people who can get together

 the next one won't be a surprise

 but don't you think the the the crowd the people are planning the next attack

 we'll see but it has to be a surprise can't be the same game

 as to the end

 it could be there's

 a very large number of games to play and they can be

 agile

 about it i don't know i'm not an expert

 right that's a good question how the space of games how how restricted is it

 yeah and the system is so complicated it could be relatively unrestricted

# Chapter 10

 this is the interesting thing well there's numbers on the insiders too

 like different kind of numbers different kind of numbers

 but this could be a new era

 because

 i don't know at least i didn't

 expect

 that

 a bunch of redditors

 could you know there's

 you know millions of people who can get together

 the next one won't be a surprise

 but don't you think the the the crowd the people are planning the next attack

 we'll see but it has to be a surprise can't be the same game

 as to the end

 it could be there's

 a very large number of games to play and they can be

 agile

 about it i don't know i'm not an expert

 right that's a good question how the space of games how how restricted is it

 yeah and the system is so complicated it could be relatively unrestricted

 and also like you know during the last couple financial crashes

 you know what set it off was you know sets of derivative events where

 you know the you know nasim talibs

 you know thing is they're they're they're trying to lower

 volatility

 in the short run but creating tail events

 and systems always evolve towards that and then they always crash like

 the gas curve is the

 you know

 star low

 ramp

 plateau

 crash

 it's 100 effective

 in the long run let me ask you some advice to put on your profound hat

 what

 there's a bunch of young folks to listen to this

 thing for no good reason whatsoever

 undergraduate students maybe high school students maybe just young folks a young at heart looking for

 the next steps to taking

 life what advice

 would you give to a young person

 today

 about

 life

 maybe career but also life in general

 get good at some stuff

 well get to know yourself right

 get good at something that you're actually interested

 in you have to love what you're doing to get good at it

 you really got to find that don't waste all your time

 doing stuff that's just

 boring

 or bland

 or numbing

 right don't let old people screw you

 well people get talked into doing all kinds of and wrapping up huge student

 you know student debts and

 like there's so much crap going on

 you know and then it drains your time

 and drains

 yeah the eric weinstein

 you know thesis that you know the older generation

 will let go

 yeah and they're trapping all the young people

 i think there's some truth to that yeah sure

 just because you're old doesn't mean you stop thinking i know lots of really original

 yeah old people

 i'm an old person

 so

 um

 but you have to be conscious about it you can fall into the ruts and then

 do that you know when i hear

 young people spouting opinions that sounds like they come from fox news or cnn

 i think they've been captured by

 groupthink

 and memes and

 supposed to think on their own you know so

 if you find yourself repeating what everybody else is saying

 you're not going to have a good life

 like like that's not how the world works it may be

 it seems safe but it puts you at great jeopardy for

 well being boring

 or unhappy

 or how long did it take you to find the thing that

 you have fun with

 well i don't know

 i've been a fun person since i was pretty little

 so everything

 i've gone through a couple periods of depression

 in my life

 for a good reason or for the reason that doesn't make any sense

 yeah

 like some some things are hard like you go through mental transitions in high school

 i was really depressed for a year and

 i think i had my first midlife crisis at 26.

 i kind of thought is this all there is like i was

 working at a job that i loved

 and but i was going to work and all my time is consumed

 what's what's the escape out of that depression what's the answer to is is

 this all there is well

 a

 friend of mine

 i

 asked him because he was working

 his ass

 off i said what's your

 work-life

 balance

 like

 like there's

 you know work friends family personal time

 are you bouncing in that and he said work 80 family 20 and i try to

 i try to find some time to sleep

 like there's no personal time there's no passion at a time

 because you know young people are often passionate about work

 so and i was certainly like that

 but you need to you need to have some space in your life for different things

 and that's that creates

 that makes you resistant to the whole

 the the the dip

 the the deep dips into depression

 kind of thing yeah well you have to get to know yourself too meditation

 helps

 some physical

 something physically intense helps

 like the weird

 places your mind goes kind of thing like and why does it happen

 why do you do what you do like triggers

 like

 the things that cause your mind to go to different places

 kind of thing or

 events

 like

 you're upbringing

 for better or worse whether your parents are great people or not

 you

 you

 you come into

 you know adulthood with all kinds of emotional burdens

 yeah and you can see some people are so bloody stiff and restrained

 and they think you know the world's fundamentally

 negative

 like you maybe

 you have unexplored territory yeah or you're afraid of something

 definitely afraid of quite a few things then you gotta go face them

 like like what's the worst thing that happened you're going to die right

 like that's inevitable you might as well get over that like a 100 death rate

 like people were worried about the virus but you know the human condition is pretty deadly

 there's something about embarrassment

 let's see i've competed a lot in my life and

 i think the

 if i'm too introspected

 the thing i'm most afraid of is

 being like humiliated

 i think nobody cares about that look you're the only

 person on the planet zack cares about you being humiliated

 exactly

 it's like a really useless

 thought

 it is

 it's like

 you're all humiliating

 something

 happened

 in a room full of people

 and they walk

 out and they didn't think

 about

 it one

 more

 second

 or maybe

 somebody

 told a funny

 story to somebody

 else and then it just

 hates

 it throughout

 yeah

 yeah now i know it too i mean

 i've been really embarrassed about that nobody cared about myself

 yeah it's a funny thing so the worst thing ultimately is just

 yeah but that's the cage

 and then you have to get out of it yeah

 like once you here's the thing once you find something like that

 you have to be determined to break it

 because otherwise you'll just you know slowly accumulate

 that kind of junk and then you die as a

 you know a mess

 so

 the goal i guess it's so

 it's like a cage with

 a cage i guess the goal is to die in the biggest

 possible

 cage

 well ideally you have no cage

 people do get enlightened i've got a few it's great

 you found a few there's a few out there i don't know of course

 um

 either that or they have you know it's a great sales

 pitch there's like enlightened

 people

 writing books and doing all kinds of stuff

 it's a good way to sell a book

 i'll

 give you that you've never met somebody

 you just thought

 they just killed me like this

 like like mental clarity humor

 no 100

 but i just feel like they're living in a bigger cage they have their own

 they don't think there's a cage they're still okay you secretly

 suspect

 there's always the case

 ah there's no there's nothing outside the the unit there's nothing outside the cage [laughter]

 you were you worked in a bunch of companies you led a lot of amazing teams

 um i don't

 i'm not sure if you've ever been like at the early stages of a startup

 but do you have advice for

 somebody that wants to do a startup or build a company

 like build a strong team of engineers that are passionate just want to

 solve a big problem like is there more specifically on that point

 well you have to be really good at stuff

 if you're going to lead and build a team

 you better be really interested in how people work and think

 the people

 or the solution

 to the problems

 there's two things

 right

 one is how people

 work

 and the other is

 actually

 there's there's quite a few successful

 startups it's pretty clear the founders don't know anything about people

 like the idea was so powerful that it propelled them but i suspect somewhere

 early they they hired some people who understood people

 because people really need a lot of care and feeding to collaborate

 and work together and feel engaged and work hard

 you know like startups are all about out producing other people

 like you're nimble because you don't have any legacy

 you don't have

 you know a bunch of people who are depressed about life you know just showing up

 you know so startups have a lot of advantages that way

 you know do you like the the steve jobs talked about this idea of

 a players and b players i don't know if you

 know this formulation yeah no

 um organizations that get taken over by pb player leaders

 often really underperform their rc players that said in big organizations

 there's

 so much work to do

 like

 and there's so many people who are happy

 to do what you know like the leadership

 or the big idea people who can see it consider menial jobs

 and you know you need a place for them but you need an organization that

 both values and rewards them but doesn't let them take over the leadership of it

 got it but so so you need to have an organization that's resistant to that but

 in the early days

 the the notion with with steve was that

 like one b player in a room

 of a players will be like destructive

 to the whole i've seen that happen i i don't know if it's like always true

 like

 you know you you run into people who are clearly

 b players but they think they're very

 players

 and so they have a loud voice

 at the table

 and they make lots of demands

 for that

 but there's other people are like i know who i am

 i just want to work with you know cool people and cool

 and just tell me what to do and i'll go get it done

 yeah you know so you have to again this is like people skills like

 what kind of person is it you know i've met some really great

 people i love working with

 that weren't the biggest id people the most productive

 ever but they show up they get it done

 you know they create connection and community that people value it's it's

 it's pretty diverse so i don't think there's a recipe for that

 i gotta ask you about love

 i heard you're into this now

 into this love thing yeah

 is this is you think this is your solution to your depression

 no i'm just trying to like you said the enlightened

 people on occasion

 trying to sell a book i'm writing a book about

 love you're writing a book about me no

 i'm not

 i'm not

 a

 friend of mine he's gonna

 somebody said you should really write a book about your you know your management philosophy

 he said it'd be a short book [laughter]

 well that one was all pretty well

 what role do you think love family friendship all that kind of

 human stuff play in a successful life you've been exceptionally successful in the space of

 like running teams building cool in this world creating some amazing things

 what did love get in the way did love help

 the family get in the way to family help friendship you want the engineer's answer

 please so but first love is functional right

 it's functional in what way so we habituate ourselves to the environment

 and actually jordan told me jordan peterson told me this line

 so

 you go through life and you just get used to everything

 except

 for the things you love

 they they remain new

 like this is really useful for you know

 like like other people's children and dogs and you know trees

 you just don't pay that much attention to your own kids you monitor them really closely

 like and if they go off a little bit because you love them if you're smart

 if you're going to be a successful parent you notice it right away you don't habituate

 to

 just things you love

 and if you want to be successful at work if you don't love it

 you're not going to put the time in somebody else

 it's somebody else that loves it like

 because it's new and interesting

 and that lets you go to the next level

 so it's the thing it's just a function that generates newness and novelty

 and surprises you know those kind of things

 it's really interesting

 but and there's people

 figured out lots of you know frameworks

 for this you know like

 like humans

 seem to go in partnership

 go through you know interest like somebody suddenly somebody's interesting

 and then you're infatuated with them and then you're in love with them

 and then you you know

 different people have

 ideas

 about parental

 love

 or mature

 love

 like you go through a cycle

 of that

 which keeps us together and it's you know super functional for creating families and

 and creating communities

 and making you support somebody despite the fact that you don't love them

 like and

 and

 it can be really enriching

 you know now in the work life balance scheme if all you do is work

 you think you may be optimizing

 your work potential

 but if you don't love your work or you don't have

 family and friends and things you care about

 your brain isn't well balanced

 like everybody

 knows the experience

 of you works on something

 all week you went home and took two days

 off and you came back

 in

 the odds of you working on the thing you

 picking up right where you left off is zero

 your brain refactored it

 but being in blood is great

 it's like changes the color of the light in the room

 it creates a spaciousness that's that's different it helps you think

 it makes you strong

 buckowski

 had this line about love being a fog that dissipates with the first light of reality

 in the morning it's that's depressing i think it's the other way around

 it lasts

 well you like you said it's a function

 it's a thing that just be the light that actually

 enlivens

 your world and creates the interest and the power and the strength and the

 to go do something

 well it's like

 like that sounds like

 you know there's like physical love emotional of intellectual

 love spiritually yeah right isn't it all the same thing kind of nope

 you should differentiate that maybe that's your problem

 in your book you should you should refine that a little bit different chapters

 yeah there's different

 chapters

 what's that what's

 these

 are there aren't these

 are just different

 layers

 of the same thing

 the stack

 no physical people people

 some people are addicted to physical love and they have no idea about emotional or intellectual

 love

 i don't know if they're the same thing so i think they're different

 that's

 true they could be different

 it'd

 be

 it

 i

 guess the ultimate

 goal is for it to be the same well if you want something

 to be bigger and interesting

 you should find all its components

 and differentiate

 them not climb it together

 people do this all the time they yeah and the modularity

 get your abstraction layers right and then you can you have room to breathe

 well maybe you can write the forward to my book about love

 yeah or the afterwards

 and the after you really tried

 i feel like lex has made a lot of progress in this book but

 well you have things in your life that you love yeah

 yeah you know so and they are you're right they're modular it's

 and you can have multiple

 things with the same person or the same thing and yeah but

 yeah depending on the moment of the day yeah there's

 like what bukowski

 described

 as that moment you go from being in love to having

 a different kind of love yeah

 right and that's the transition

 but when it happens

 if you read the owner's manual and you believed it you would have said

# Chapter 11

 and differentiate

 them not climb it together

 people do this all the time they yeah and the modularity

 get your abstraction layers right and then you can you have room to breathe

 well maybe you can write the forward to my book about love

 yeah or the afterwards

 and the after you really tried

 i feel like lex has made a lot of progress in this book but

 well you have things in your life that you love yeah

 yeah you know so and they are you're right they're modular it's

 and you can have multiple

 things with the same person or the same thing and yeah but

 yeah depending on the moment of the day yeah there's

 like what bukowski

 described

 as that moment you go from being in love to having

 a different kind of love yeah

 right and that's the transition

 but when it happens

 if you read the owner's manual and you believed it you would have said

 oh this happened

 it doesn't mean it's not love it's a different kind of love

 but

 but maybe there's something better about that as you grow old if

 all you do is regret

 how you used to be it's sad

 right you should have learned a lot of things because

 like who you can be in your future self is

 is actually more interesting and possibly delightful than

 you know being a mad kid in love with the the next person like

 that's super fun when it happens but

 that's that's you know five percent of the possibility

 yeah that's right that there's a lot more fun to be had

 in the long lasting stuff

 yeah or meaning you know if that's me

 which is a kind of fun

 it's a deeper kind of fun and it's surprising you know that's

 like like the thing i like is surprises

 you know and you just never know what's gonna happen

 yeah

 but you have to look carefully

 and you have to work at it you have to think about

 it and

 you know it's

 yeah you have to see the surprises

 when they happen right you have to be looking for it

 from the branching perspective

 you mentioned regrets

 do you have regrets about your own trajectory oh yeah of course

 yeah some of it's painful but you want to hear the painful stuff

 i'd say like in terms of working with people

 when people did say stuff i didn't like especially if it was a bit nefarious

 i took it personally and i also

 felt it was personal about them

 but a lot of times like humans are you know most humans are a mess

 right and then they act out and they do stuff

 and i this psychologist

 i heard a long time ago said

 you tend to think somebody does something to you

 but

 really what they're doing is they're doing

 what they're doing

 while they're in front of you

 it's not that much about you

 yeah right and as i got more interested in

 you know when i work with people i think about them and probably analyze them

 and understand them a little bit and then when they do stuff i'm way less surprised

 and i'm wait you know and if it's bad i'm way less hurt

 and i react way less

 like i sort of expect everybody's got their

 yeah and it's not about you it's not about me that much

 it's like you know

 you know you do something and you think you're embarrassed

 but nobody cares

 like and somebody's really mad at you at the odds of it being about

 you

 yeah no they're getting mad the way they're doing that because of some pattern they learned

 and you know and maybe you can help them

 if you care enough about

 it but

 or you could step you could see it coming

 and step

 out of the way

 like

 like i wish i was way better at that i'm i'm a bit of a hothead

 and and

 you said with steve that was a feature not a bug

 yeah well he was using it as the counter force the orderliness

 that would crush his work well you were doing the same

 yeah

 maybe i don't think i don't think my

 my vision was big enough

 it was more like i just got pissed off

 and did stuff

 i'm sure that's just yeah yeah you're telling me i don't know if it had the

 it didn't have the amazing

 effect

 of creating

 the trillion dollar

 company

 it was more like i just got pissed

 off and left

 and or

 made enemies that he shouldn't have been

 yeah it's hard

 like i didn't really understand politics until i worked at apple

 where you know steve was a master player of politics

 and his staff had to be or they wouldn't survive them and

 it was definitely part of the culture

 and then i've been in companies where they say it's political but it's all

 you know fun and games compared to apple and it's not that

 the people apple are bad people it's just they operated politically at a higher level

 you know it's not like oh somebody said something bad about somebody

 somebody else which is most politics

 it's you know they they had strategies about accomplishing their goals

 sometimes you know

 over the dead bodies of their enemies

 you know

 with some communication

 yeah more game of thrones and sophistication

 and like a big time factor rather than a

 you know well that requires a lot of control over your emotions i think

 to do to have a bigger strategy in the way you behave

 yeah and it's it's it's

 effective

 in the sense that coordinating

 thousands of people to do really hard things

 where many of the people in there don't understand themselves much less how they're participating

 yeah creates all kinds of

 you know drama and problems

 that you know our solution is political in nature

 like how do you convince

 people how do you leverage them how do you motivate

 them how do you get rid of them how you know like there's

 there's so many layers

 of that that are interesting

 and even though some some of it let's say may be tough

 it's not

 evil

 unless you know you use that skill to evil purposes which some people obviously do but

 but it's a skill set that operates you know and i wish i'd

 you know i was interested

 in it but i you know it was sort of like i'm an engineer

 i do my thing

 and you know there's there's times when i could have way bigger impact

 if i you know knew how to

 if i paid more attention and knew more about that

 about the human layer of the stack yeah that human political

 power you know expression layer of the stack which is complicated

 and there's lots

 to know about

 it

 i mean people

 are good at it are just

 amazing

 and when they're good at it and let's say

 relatively

 kind and oriented in a good direction you can really feel

 it can get lots of stuff done and coordinate things you never thought possible

 but all people like that also have some pretty hard edges because

 you know it's it's a heavy lift

 and i wish i'd spent more time with that when i was younger but

 but maybe i wasn't ready you know i was a wide-eyed kid for 30 years

 it's a little bit of a kid i know what do you hope

 your legacy is when there's a

 when there's a book like a hitchhiker's

 guide to the galaxy and this is like a one sentence entry ball jim caller

 from like that guy lived at some point

 there's not many you know not many people be remembered

 you're one of the sparkling little

 human creatures

 that had a big impact on the world

 how do you hold you'll be remembered my daughter was trying to get

 she added my wikipedia page to say that i was a legend and a guru

 but they took it out so she put it back in she's 15.

 i think i think that was probably the best part of my legacy [laughter]

 she got her sister they were all excited

 they were like trying to put it in the references

 because there's articles

 in that and they're telling you that

 so the eyes of your kids your

 legend

 well they're pretty skeptical because they'll be better than that they're like dad

 so yeah that's

 that's stupid that kind of stuff is super fun

 in terms of the big legends stuff anchor

 okay legacy i don't really care you're just an engineer

 no they've been thinking about building a big pyramid

 so i had a debate with a friend about whether pyramids or craters are cooler

 and you realize that

 there's craters

 everywhere but you know they built a couple of pyramids

 five thousand years ago in there and they remember you

 think that would be foreign

 those aren't easy to build oh i know

 and they don't actually know how they built them which is great

 it's either agi or aliens could be involved so i think

 i think you're gonna have to figure out quite a few more things than just

 the basics of civil engineering

 so i guess you hope your legacy is pyramids

 that would that would be cool

 and my wikipedia page you know getting updated by my daughter periodically

 like those two things would pretty much make it

 jim it's a huge

 honor talking

 to you again

 i hope we talk many more times

 in the future

 i can't wait to see

 what you do with tennis torrent i can't wait to use it

 i can't wait for you to revolutionize

 yet another space in computing

 it's a huge honor to talk to you thanks for talking today this was fun

 thanks for listening to this conversation with jim keller and thank you to our sponsors

 athletic greens all-in-one nutrition drink

 brooklyn and sheetz

 expressvpn

 and bel campbell grass-fed meat

 click the sponsor links to get a discount and to support this podcast

 and now let me leave you with some words from alan turing

 those who can imagine anything can create the impossible

 thank you for listening and hope to see you next

 time

 you

