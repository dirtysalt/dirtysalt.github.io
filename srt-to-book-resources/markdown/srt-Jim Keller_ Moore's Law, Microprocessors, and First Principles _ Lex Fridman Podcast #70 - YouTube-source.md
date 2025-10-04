# Chapter 1

the following is a conversation with jim keller legendary

 microprocessor engineer who has worked at amd apple tesla

 and now intel he's known for his work on amd k 7 k 8 k 12

 and xen microarchitectures apple a4 and a5 processors

 and co-author of the specification for the x86 64 instruction

 set and hyper transport interconnect he's

 a brilliant first principles engineer

 and out-of-the-box thinker

 and just an interesting

 and fun human being to talk to this is the artificial intelligence podcast

 if you enjoy it subscribe

 on youtube give it five stars an apple podcast follow

 on spotify supported on patreon

 or simply connect with me on twitter alex

 friedman spelled fri d ma a.m. i recently

 started doing ads at the end of the introduction

 i'll do one or two minutes

 after introducing the episode

 and never any ads in the middle that can break the flow of the conversation i

 hope that works for you and doesn't hurt the listening experience

 this show is presented by cash app the number one finance

 i up in the app store i personally

 use cash app to send money to friends but you can also use it to buy sell

 and deposit bitcoin in just seconds cash

 app also has a new investing feature you

 can buy fractions of a stock say $1 worth no

 matter what the stock price is brokers

 services are provided by cash app investing a subsidiary of square

 and member si pc i'm

 excited to be working with cash app to support one of my favorite organizations called first best

 known for their first robotics

 and lego competitions they educate

 and inspire hundreds of thousands of students in over 110

 countries and have a perfect rating a charity navigator which

 means that donated money is used to maximum effectiveness when

 you get cash app from the app store google play

 and use code lex podcast you'll

 get ten dollars and cash app will also donate ten dollars to the first which

 again is an organization

 that i've personally seen inspire girls

 and boys the dream of engineering a better world

 and

 now here's my with jim keller

 what are the differences in similarities

 between the human brain and a computer with

 the microprocessors core let's

 start with a philosophical question perhaps well

 since people don't actually understand

 how human brains work i think

 that's true i think that's true so

 it's hard to compare them computers are

 you know there's really two things there's memory and there's computation right

 and to date almost all computer architectures are global memory which is a thing right

 and then computation

 where you pull data and you do relatively simple operations on it and write data back

 so it's decoupled in modern in modern computers

 and you think in the human brain everything's

 a mesh a mess that's combined together what

 people observe is there's you know some number of layers of neurons

 which have local

 and global connections

 and information is stored in some distributed fashion

 and people build things called neural networks in computers

 where the information is distributed in some kind of fashion you know there's a mathematics behind it i

 don't know that the understandings that is super deep the computations we run on those are straightforward computations

 i don't believe anybody has said a neuron does this computation

 so

 to date it's hard to compare them i

 would say so let's get into the basics before we zoom back out

 how do you build a computer from scratch

 what is a microprocessor

 what is it microarchitecture

 what's an instruction set architecture maybe

 even as far back as what is a transistor

 so

 the special charm of computer engineering is there's a relatively good understanding of abstraction layers

 so down to bottom you have atoms

 and atoms get put together in materials like silicon

 or dope silicon

 or metal

 and we build transistors on top of that we build logic gates

 right and in functional units like an adder or subtractor or an instruction parsing unit

 and we assemble those into you know processing elements modern computers are built out of you

 know probably 10 to 20 locally

 you know organic processing elements

 or coherent processing elements

 and then that runs computer programs right

 so there's abstraction layers and then software

 you know there's an instruction set you run and then there's assembly language c c++ java javascript

 you know there's abstraction layers you

 know essentially from the atom to the data center right

 so when you when you build a computer

 you know first there's a target like what's it for look

 how fast does it have to be which you

 know today there's a whole bunch of metrics about what that is and then

 in an organization of you know a thousand people who build a computer there's

 lots of different disciplines that

 you have to operate on does that make sense and so

 so

 there's a bunch of levels abstraction of in in organizational

 i can tell and in your own vision there's

 a lot of brilliance that comes in it every one of those layers some

 of it is science some was engineering some of his art what's the most

 if you could pick favorites what's the most important your favorite layer on

 these layers of abstractions

 where does the magic enter this hierarchy i

 don't really care that's

 the fun you know i'm somewhat agnostic to that so i would say for

 relatively long periods of time instruction sets are stable

 so the x86 instruction said the arm instruction set what's

 an instruction set so it says how do you encode the basic operations load store multiply add subtract conditional

 branch you know there

 aren't that many interesting instructions look

 if you look at a program

 and it runs you

 know 90% of the execution is on 25 opcodes you know 25 instructions

 on those are stable right

 what does it mean stable until architecture has been around for twenty-five years it

 works it works and that's because the basics you

 know or defined a long time ago right

 now the way an old computer ran is you fetched instructions and you executed them in order to

 the load do the ad do the compare the

 way a modern computer works is you fetch large numbers of instructions say 500

 and then you find the dependency graph between the instructions

 and then you you execute in independent units those little micro graphs

 so a modern computer like people like to say computers should be simple

 and clean

 but it turns out the market for a simple complete clean slow computers is zero right

 we don't sell any simple clean computers

 now you can there's

 how you build it can be clean

 but the computer people want to buy that's say you know phone or data center

 such as

 a large number of instructions computes the dependency graph and then

 executes it in a way that gets the right answers

 and optimizes that graph somehow

 yeah they run deeply out of order

 and then there's

 semantics around how memory ordering

 works and other things work so the the computer sort of has a bunch of bookkeeping

 tables it says what order cds operations finishing

 or appear to finish him but to go fast you have to fetch a lot of instructions

 and find all the parallelism

 now there's a second kind of computer

 which we call gpus today

 and i called the difference there's

 found parallelism like you have a program with a lot of dependent instructions you

 fetch a bunch and then you go figure out the dependency graph and you issues instructions out order that's

 because you have one serial narrative to execute

 which

 in fact is and can be done out of order you call a narrative

 yeah well

 so

 yeah so humans think of serial narrative

 so read read a book right

 there's a you know there's the sends after sentence after sentence

 and there's paragraphs

 now you could diagram that imagine you diagrammed it properly

 and you said

 which sentences could be read in anti order any order without changing the meaning right

 but that's a fascinating question to ask of a book yeah

 yeah you could do that right

 so some paragraphs could be reordered some sentences can be reordered you could say he is tall

 and smart

 and x right

 and it doesn't matter the order of tall and smart

 but

 if you say is that tall man who's

 wearing a red shirt what

 colors you know like

 you can create dependencies right right

 and so

 gpus on the other hand run simple programs on pixels

 but you're given a million of them and the first order the screen

 you're looking at it doesn't care which order you do it in so

 i call that given parallelism simple

 narratives around the large numbers of things

 where you can just say it's parallel

 because you told me it was so found parallelism

 where the narrative is it's sequential

 but you discover like

 little pockets of parallelism of versus turns out large pockets of parallelism large

 so

 how hard is it to discuss well how hard is it that's just transistor count right

 so once you crack the problem you say here's

 how you fetch ten instructions at a time here's

 how you calculated the dependencies between them here's

 how you describe the dependencies here's you know these are pieces right

 so once

 you describe the dependencies then it's just a graph sort of it's an algorithm that finds

 what is that i'm sure there's a graph there is the theoretical answer here that's solved

 well in general programs

 modern programs like human beings right

 how much found

 parallelism is there and on that i max what is 10 next mean oh well

 you execute it in order vs.

 yeah you would get what's called cycles per instruction and it would be about

 you know three instructions three cycles per instruction

 because of the latency of the operations

 and stuff

 and in a modern computer excuse it but like point to 0.25

 cycles per instruction so it's about with today fine 10x

 and there

 and there's two things one is the found parallelism in the narrative right

 and the other is to predictability of the narrative right

 so certain operations

 they do a bunch of calculations and if greater than one do this else do that that

 that decision is predicted in modern computers to high 90% accuracy

 so branches

 happen a lot so imagine you have you have a decision to make every six instructions

 which is about the average right

 but you want to fetch five under instructions

 figure out the graph and execute them all in parallel that means you

 have let's say if you effect 600 instructions it's every six you

 have to fetch you have to predict ninety-nine out of a hundred branches correctly for

 that window to be effective

 okay

 so parallelism you can't paralyze branches

 or you can looking pretty you can what is predict a branch mean

 or

 what open take so imagine you do a computation over

 and over you're in a loop so wow

 and it's greater than one do

 and you

 go through that loop a million times so

 every time you look at the branch you say it's

 probably still greater than one he's

 saying you could do that accurately very accurately monitoring

 comes my mind is blown how

 the heck did you that wait a minute well

 you want to know this is really sad 20 years ago

 yes you simply recorded

 which way the branch went last time and predicted the same thing right

 okay what's the accuracy of that 85%

 so then somebody said

 hey let's keep a couple of bits and have a little counter

 so and it predicts one way we count up and then pins

 so say you have a three bit counter so you count up and then

 count down and if it's you know you can

 use the top bit as the sign bit so you have a sign to bit number

 so if it's greater than one you predict taken and lesson one you predict not-taken right

 or less than zero or whatever the thing is

 and that got us to 92%

 oh

 okay

 i know is this better this branch depends on how you got there

 so

 if you came down the code one way you're talking about bob and jane right

 and then said is just bob

 like jane enoch went one way but if you're talking about

 bob and jill this bob like changes

 you go a different way right

 so that's called history

 so you take the history and a counter that's

 cool but that's not how anything works today they

 use something that looks a little like a neural network

 so

 modern you take all the execution flows and then

 you do basically deep pattern recognition of how the program is executing

 and

 you do that multiple different ways and you have something that chooses

 what the best result is there's a little supercomputer

 inside the computer that's trying to project that calculates

 which way branches go so

 the effective window that it's worth finding grassing gets bigger

 why was that gonna make me sad that's

 amazing it's amazingly complicated

 oh well here's the funny thing so to get to 85% took a thousand bits

 to get to 99% takes

 tens of megabits

 so

 this is one of those to

 get the result you want you know to get from a window of say 50

 instructions to 500 it took three orders of magnitudes

 or four orders of magnitude toward bits

 now

 if you get the prediction of a branch wrong

 what happens then what is the pipe you flush the pipes is just the performance cost

 but it gets even better yeah

# Chapter 2

 and

 you do that multiple different ways and you have something that chooses

 what the best result is there's a little supercomputer

 inside the computer that's trying to project that calculates

 which way branches go so

 the effective window that it's worth finding grassing gets bigger

 why was that gonna make me sad that's

 amazing it's amazingly complicated

 oh well here's the funny thing so to get to 85% took a thousand bits

 to get to 99% takes

 tens of megabits

 so

 this is one of those to

 get the result you want you know to get from a window of say 50

 instructions to 500 it took three orders of magnitudes

 or four orders of magnitude toward bits

 now

 if you get the prediction of a branch wrong

 what happens then what is the pipe you flush the pipes is just the performance cost

 but it gets even better yeah

 so we're starting to look at stuff that says

 so executed down this path and then

 you had two ways to go but far far

 away there's something that doesn't matter which path you went

 so you miss you took the wrong path you executed a bunch of stuff then

 you had to miss predicting

 too backed it up but you remembered

 all the results you already calculated

 some of those are just fine look

 if you read a book and you misunderstand the paragraph your understanding is the next paragraph

 sometimes is invariance i don't understand you sometimes it depends on it

 and you can kind of anticipate that invariance

 yeah well you can keep track of whether that data changed

 and so

 when you come back to a piece of code should you calculate

 it again or do the same thing

 okay

 how much does this is art and how much of it is science

 because it sounds pretty complicated so well

 how do you describe a situation so

 imagine you come to a point in the road we have to make a decision right

 and you have a bunch of knowledge about which way to go maybe you have a map

 so

 you want to go is the shortest way or

 do you want to go the fastest

 way or you want to take the nicest road so it's just

 some set of data so imagine

 you're doing something complicated like a building a computer

 and there's hundreds of decision points all with hundreds of possible ways to go and the

 ways you pick interacts in a complicated way right

 and then you have to pick the right spot right

 so those are there so i don't know yeah avoided the question you just described

 do the robert frost poem road

 less taken i describe

 the robin truss problem

 which we do as computer designers it's all poetry ok great

 yeah

 i don't know how to describe that because some

 people are very good at making those intuitive leaps it seems like the combinations of things some

 people are less good at it but they're really good at evaluating your alternatives right

 and everybody has a different way to do it and some people can't make those sleeps

 but they're really good at analyzing it

 so

 when you see computers are designed by teams of people who have very different skill sets and a

 good team has lots of different kinds of people

 and i suspect you would describe some of them as artistic right

 but not very many unfortunately

 or fortunately fortunately well you know computer science hard it's 99% perspiration

 and the 1% inspiration is really important

 but

 i need the 99

 yeah you got to do a lot of work and then there's there

 are interesting things to do at every level that stack

 so at

 the end of the day if you're on the same program multiple times does

 it always produce the same result is is there some room for fuzziness there that's a math problem

 so

 if you run a correct c program the definition is every

 time you run it you get the same answer yeah that well that's a math statement

 but that's a that's a language definitional statement

 so

 yes for years when people did when we first did 3d acceleration of graphics

 you could run the same scene multiple times and get different answers right right

 and then some

 people thought that was okay and some people thought it was a bad idea and then when

 the hpc world used gpus for calculations

 they thought it's a really bad idea okay

 now in modern ai stuff people are looking at

 networks

 where the precision of the data is low enough that the date has somewhat noisy

 and the observation as the input data is unbelievably noisy

 so why should the calculation be not noisy

 and people

 have experimented with algorithms that say

 can get faster answers by being noisy like

 as the network starts to converge

 if you look at the computation graph it starts out really wide and it gets narrower

 and you can say is that last little bit that important

 or should i start to graph on the next rap rev before

 we would live all the way down to the answer right

 so you can create algorithms that are noisy

 now if you're developing something

 and every time you run it you get a different answer it's really annoying and

 so

 most people think even

 today every time you run the program you get the same answer

 now

 i know but the question is that's the formal

 definition of a programming language there is a definition of languages that don't get the same answer

 but people who use those you always want something because you get a bad answer

 and then you're wondering is it because right

 something in your brother

 because of this and

 so everybody wants a little swish that says no matter what ya do it deterministically

 and it's really weird because almost everything going into monetary calculations is noisy

 so why the answers have to be so clear it's right so

 where do you stand by design computers for people who run programs

 so

 somebody says i want in deterministic answer like

 most people want that can you deliver a deterministic answer i guess is the question like

 when you hopefully sure that's

 what people don't realize is you get a deterministic

 answer even though the execution flow is very own deterministic

 so

 if you run this program a hundred times it never runs the same way twice ever

 and the answer it arises

 the same in but it gets the same answer every time it's just just

 them is just amazing

 okay you've achieved in eyes of

 many people

 legend status as a cheap art architect

 what design creation are you most proud of perhaps

 because it was challenging

 because of its impact

 or

 because of the set of brilliant ideas that that were

 involved in well i find that description odd

 and i has two small children

 and i promise you

 they think it's hilarious this question

 yeah

 so i dude

 so i i'm

 i'm really interested in building computers

 and i've worked with really really smart people i'm not unbelievably smart i'm fascinated by

 how they go together both as a as

 a thing to do and is endeavor that people do

 how people in computers go together yeah like

 how people think

 and build a computer

 and i find sometimes that the best computer architects aren't that interested in people

 or the best people managers aren't that good at designing computers

 so the whole stack of human beings is fascinating

 so the managers individual engineers

 yeah i just i said i realized

 after a lot of years of building computers

 where you sort of build them out of the transistors logic gates functional units come computational elements that

 you could think of people the same way so people are functional units

 yes

 and then you can think of organizational design it's a computer architectural problem

 and then

 it's like oh that's super

 cool because the people are all different just like the computation

 elephants are all different and they

 like to do different things and

 and

 so i had a lot of fun like reframing

 how i think about organizations just like with with

 computers we were saying execution

 paths you can have a lot of different paths that end up at a at

 at the same good destination

 so

 what have you learned about the human

 abstractions from individual functional human units to the broader organization

 what does it take to create something special well

 most people don't think simple enough

 all right so do you know the difference between a recipe

 and understanding

 there's

 probably a philosophical description of this so imagine you can make a loaf of bread yeah

 the recipe says get some flour add some water add some yeast mix it up let it rise put

 it in a pan put it in the oven it's

 a recipe right understanding bread you

 can understand biology supply chains you

 know grain grinders yeast physics

 you know thermodynamics like there's

 so many levels of understanding there and then when people build

 and design things they frequently are executing some stack of recipes right

 and the problem with that is the recipes all have a limited scope look

 if you have a really good recipe

 book for making bread it won't tell you anything about how to make an omelet right right but

 if you have a deep understanding of cooking

 right then bread

 omelets you know sandwich you know there's there's a different you know way of viewing everything

 and most

 people when you get to be an expert at something you

 know you're you're hoping to achieve deeper understanding

 not just a large set of recipes to go execute

 and it's interesting the walk groups of people because xqt

 reps apiece is unbelievably efficient if it's

 what you want to do if it's not what you want to do you're really stuck

 and

 and that difference is crucial

 and ever

 and everybody has a balance of let's say deeper understanding recipes

 and some people are really good at recognizing when

 the problem is to understand something dp deeply that

 make sense it totally makes sense does

 it every stage of development deep on understanding on the team needed

 oh this goes back to the art versus science question sure

 if you constantly unpacked everything for deeper understanding you never get anything done right

 and

 if you don't unpack understanding when you need to you'll do the wrong thing

 and then at every juncture like human beings are these really weird things

 because everything

 you tell them has a million possible outputs all

 right and then they all interact in a hilarious way

 and then having

 some intuition about what you tell them what you do when do you intervene

 when do you not it's it's complicated all right

 so it's you know essentially computationally unsolvable

 yeah it's an intractable problem sure

 humans are a mess but

 with deep understanding do you mean also sort of fundamental questions of things like

 what is a computer

 or

 why like think the why question is why are we even building this like of purpose

 or do you mean more

 like going towards the fundamental limits of physics sort of really getting

 into the core of the sighs well in terms of building the computer thinks

 simple think a little simpler

 so common practice is you build a computer

 and then when somebody says i want to make it 10% faster you'll

 go in and say alright

 i need to make this buffer bigger and maybe i'll add an ad unit or you

 know i have this thing that's three instructions wide i'm going to make it four instructions wide and

 what you see is each piece gets incrementally more complicated right

 and then at some point you hit this limit like adding another feature

 or a buffer doesn't seem to make it any faster and

 then people say well that's because it's a fundamental limit

 and then

 somebody else to look at it and say well actually the way you divided

 the problem up and the way that different features are interacting is limiting

 you and it has to be rethought rewritten right

 so then you refactor it and rewrite it and what people commonly find is

 the rewrite is not only faster

 but half is complicated from scratch

 yes

 so

 how often in your career

 but just have you seen as needed

 maybe more generally to just throw the whole out thing

 out this is where i'm on one end of it every

 three to five years

 which end are you on like rewrite more often right

 and three

 or five years is if you want to really make a lot of progress on computer architecture every

 five years you should do one from scratch

 so

 where does the x86 64 standard come in or

 what how often do you i wrote

 the i was the co-author that's back in 98 that's 20 years ago

 yeah

 so that's still around the instruction set it stuff has been extended quite a few times yes

 and instruction sets are less interesting

 and implementation underneath there's

 been on x86 architecture

 intel's designed a few eames is designed a few very different architectures

 and i

 don't want to go into too much of the detail about how often

 but it's

 there's a tendency to rewrite it every you know 10 years and it really should be every five

 so

 you're saying you're an outlier in that sense in really

 more often we write more often well in here isn't that scary

 yeah of course well scary - who - everybody involved

 because like you said repeating

 the recipe is efficient companies

 want to make money well

 no in the individual juniors want to succeed so you want to incrementally

 improve increase the buffer from three to four well we get

 into the diminishing return curves i think

 steve jobs said this right so every you have a project

 and you start here and it goes up and they have domitian return

 and to get to the next level you have to do a new one in the initial

 starting point will

 be lower than the old optimization

 point but it'll get higher

 so

 now you have two kinds of fear short-term disaster

 and long-term disaster

 and you're you're wrong

 right like

 you know people with a quarter by quarter business objective are terrified about changing everything yeah

 and people who are trying to run a business

 or build a computer for a long term objective know that the short-term limitations block

 them from the long term success

 so

 if you look at leaders of companies

 that had really good long-term success every

 time they saw that they had to redo something they did and

 so somebody has to speak up or you

 do multiple projects in parallel like you optimize

 the old one while you build a new one and

 but the marketing guys they're always like make promise

 me that the new computer is faster on every single thing

 and the computer architect says well the new computer will be faster on the average

 but there's a distribution

 or results in performance

 and you'll have some outliers that are slower

# Chapter 3

 and long-term disaster

 and you're you're wrong

 right like

 you know people with a quarter by quarter business objective are terrified about changing everything yeah

 and people who are trying to run a business

 or build a computer for a long term objective know that the short-term limitations block

 them from the long term success

 so

 if you look at leaders of companies

 that had really good long-term success every

 time they saw that they had to redo something they did and

 so somebody has to speak up or you

 do multiple projects in parallel like you optimize

 the old one while you build a new one and

 but the marketing guys they're always like make promise

 me that the new computer is faster on every single thing

 and the computer architect says well the new computer will be faster on the average

 but there's a distribution

 or results in performance

 and you'll have some outliers that are slower

 and that's very hard because they have one customer cares about that one so speaking

 of the long-term for over 50 years now moore's law has served a for

 me and millions of others as an inspiring beacon

 what kind of amazing future brilliant engineers can build no i'm

 just making your kids laugh all of today it was great

 so

 first in your eyes what is moore's law if you could define for people who don't know

 well the simple

 statement was from gordon moore was double the number of transistors every two years something

 like that and then my operational model is we

 increased the performance of computers by 2x

 every 2 or 3 years and it's wiggled around substantially

 over time and also in

 how we deliver performance has changed

 but the foundational

 idea was to x two transistors every two years the

 current cadence is something like they call it a shrink factor like

 point six every two years which is not 0.5

 but that that's referring strictly again to the original definition of transistor count a shrink

 factors just getting them smaller small as well as you use for a constant chip area

 if you

 make the transistor smaller by 0.6 then you get 1 over 0.6 more transistors

 so can you linger a little longer what's what's

 a broader what do you think should be the broader definition of moore's law we mentioned before how

 you think of performance just

 broadly what's a good way to think about moore's law well

 first of all so

 i i've been aware of moore's law for 30 years in

 what sense well i've been designing computers for 40 just watching

 it before your eyes kind of slow and somewhere

 where i became aware of it i was also informed that

 moore's law was gonna die in 10 to 15 years

 and i thought that was true at first

 but then after 10 years it was gonna die in 10 to 15 years and then

 at one point it was gonna die in 5 years

 and then it went back up to ten years and at some point i decided

 not to worry about that particular

 product mastication for the rest of my life

 which is which is fun

 and then i joined intel

 and everybody said moore's law is dead and i thought that's sad because it's the moore's law company

 and it's not dead and it's always been gonna die and you

 know humans you like these apocryphal

 kind of statements like we'll

 run out of food or run out of air or

 you know something right

 but it's still incredible this lived for as long as it has

 and

 yes

 there's many people who believe now that moore's law instead you know they

 can join the last 50 years of people had the thing yeah there's a long tradition

 but why do you think if you can in touch try

 to understand it why do you think it's not dead well

 for hartley let's just think people

 think moore's law is one thing transistors get smaller

 but actually under the sheets ours literally thousands of innovations

 and almost all those innovations have their own diminishing return curves

 so

 if you graph it it looks like a cascade of diminishing return curves i don't

 know what to call that but the result is an exponential curve at

 least it has been so

 and we

 keep inventing new things so if you're an expert in one of the things on a diminishing return curve

 right

 and you can see it's plateau you will

 probably tell people well this is this is done meanwhile

 some other pile of people are doing something different

 so that's that's just normal

 so then there's the observation of how small could a switching device be

 so a modern transistor is something like a thousand by a thousand by thousand atoms right

 and you get quantum effects down around two to two to ten atoms

 so you can imagine the transistor as small as 10 by 10 by 10

 so that's a million times smaller

 and then the quantum computational people are working away at how to use quantum effects

 so a

 thousand by thousand five thousand atoms

 it's a really clean way of putting it well fin like a modern transistor

 if you look at the fan it's like a hundred

 and twenty atoms wide but

 we can make that thinner and then there's there's a gate wrapped around it

 and under spacing there's a whole bunch of geometry

 and you know a competent transistor designer could count both atoms in every single direction

 like there's techniques now to already put down atoms in a single atomic layer

 and you can place atoms

 if you want to it's

 just you know from

 a manufacturing process if placing an atom takes ten minutes and you need to put

 you know 10 to the 23rd atoms together to make a computer it would take a long time

 so the the methods are you know both shrinking things

 and then coming up with effective ways to control what's happening

 manufacture stabling cheaply

 yeah

 so the innovation stocks

 pretty broad you know there there's

 equipment there's optics there's chemistry there's physics there's material science there's metallurgy there's

 lots of ideas about when you put their four materials together

 how they interact are they stable is i stable

 or temperature you

 know like are they repeatable you know there's look there's like

 literally thousands of technologies involved

 but just for the shrinking you don't think we're quite yet close to the fundamental

 limit in physics i did

 a talk on moore's law and i asked for a road

 map to a path of 100

 and after two weeks they

 said we only got to fifty a hundred what's

 a 100 extra hundred shrink we

 only got 15 i said once you go to another two weeks

 well here's the thing about moore's law right

 so i believe that

 the next 10 or 20 years of shrinking is going to happen right

 now as a computer designer there's

 you have two stances you think it's going to shrink in which case you're designing

 and thinking about architecture in a way that you'll use more transistors

 or

 conversely not be swamped by the complexity of all the transistors you get right

 you have to have a strategy

 you know so you're open to the possibility

 and waiting for the possibility of a whole new army of transistors

 ready to work i'm expecting

 expecting more transistors every two or three years by a number large enough that

 how you think about design

 how you think about architecture has to change like

 imagine you're you build built brick buildings out of bricks and every

 year the bricks are half the size

 or every two years well

 if you kept building bricks the same way you know

 so many bricks per person per day the

 amount of time to build a building would go up exponentially right right but

 if you said i know that's coming

 so

 now i'm going to design equipment

 and moves bricks faster uses them better because

 maybe you're getting something out of the smaller bricks more strengths inner walls you

 know less material efficiency out of that so

 once you have a roadmap with what's going to happen transistors

 they're gonna get we're gonna get more of them then you design

 was collateral rounded to take advantage of it and also to cope with it like

 that's the thing people to understand

 it's like if i didn't

 believe in moore's law and moore's

 law transistors showed up my design teams were all drowned

 so what's the what's the hardest part of this in flood of new transistors

 i mean even

 if you just look historically throughout your career what's

 what's the thing you what

 fundamentally changes when you add more transistors in in the task of designing an architecture no

 there's there's two constants right one is people don't get smarter i

 think by the way there's some size shown that we do get smarter

 because nutrition whatever sorry

 bring that what effect yes nobody understands

 it nobody knows if it's still going on so that's all or whether

 it's real or not but yeah that's a i sort of amen

 but not if i believe for the most part people aren't getting much smarter the

 evidence doesn't support it that's right and then teams can't grow that much right

 all right so human beings understand

 you know we're really good in teams of ten you

 know up two teams of a hundred they can know each other beyond

 that you have to have organizational boundaries so

 you're kind of you have those are pretty hard constraints all

 right so then you have to divide

 and conquer

 like as the designs get bigger you have to divide it into pieces you know

 that the power of abstraction layers is really high we used to build computers out of transistors

 now we have a team that turns transistors

 and logic

 cells and our team that turns them into functional

 you know it's another one it turns in computers right

 so we have abstraction layers in there and

 you

 have to think about when do you shift gears on that we

 also use faster computers to build faster computers so

 some algorithms run twice as fast on new computers

 but a lot about rhythms are n squared

 so you know a computer with twice as many transistors

 and it might take four tom's times as long to run so

 you have to refactor at the software like

 simply using faster computers to build bigger computers doesn't work

 so

 so you have to think about all these things so in terms of computing performance

 and the exciting possibility that more powerful computers bring is shrinking

 the thing we've been talking about

 one of the for you one of the biggest exciting possibilities of advancement in performance

 or is there are other directions that you're interested in like like

 in the direction of sort of enforcing given parallelism

 or like doing

 massive parallelism in terms of many many cpus you

 know stacking cpus on top of each other that kind of that kind of parallelism

 or you kind of well think about it a different way

 so old

 computers you know slow computers you said a equal b plus c times d pretty simple right

 and then we made faster computers with vector units

 and you can do proper equations

 and matrices right

 and then modern like ai computations

 or like convolutional neural networks we you convolve one large data set against another and

 so there's

 sort of this hierarchy of mathematics

 you know from simple

 equation to linear equations to matrix equations to it's a deeper kind of computation

 and the data sets are getting

 so big that people are thinking of data as a topology

 problem you know data is organized in some immense shape

 and then the computation

 which sort of wants to be get

 data from immense shape and do some computation

 on it so the with

 computers of a lot of people to do is how about rhythms go much much further

 so

 that that paper you you reference the sutton paper they

 talked about you know like in a i started

 it was a ploy rule sets to something that's

 a very simple computational situation

 and then when they did first chess thing they solved deep searches

 so have a huge database of moves

 and results deep search but it's still just a search right

 now we we take large numbers of images

 and we use it to train these weight sets that

 we convolve across it's a completely different kind of phenomena we

 call that ai now they're doing the next generation

 and if you look at it they're going up this mathema graph right

 and then computations the both computation

 and data sets support going up that graph

 yeah

 the kind of computation

 of my i mean i would argue that all of it is still a search right just

 like you said a topology problems data says he's searching the data sets for valuable

 data and also the actual optimization of your networks is a kind of search for

 the i don't know if you looked at the inner layers of finding a cat

 it's not a search it's it's a set of endless projection

 so you know projection

 and here's a shadow of this phone

 yeah right then

 you can have a shadow of that onto something a shadow on that or something

 if you look in the layers you'll see this layer actually describes pointy ears and round eyeness

 and fuzziness

 and

 but the computation to tease out the attributes is not search right

 ain't like the inference part might be searched

 but the trainings not search

 okay well 10 then in deep networks

 they look at layers and they don't even know it's represented

 and yet

 if you take the layers out it doesn't work ok

 so if i don't think it's search all

 right well but you have to talk to my mathematician about what that actually is

 oh you disagree

 but the the it's just semantics

 i think it's not but it's certainly not i would say it's absolutely not semantics

 but okay

 all right well

 if you want to go there

 so optimization to me is search

 and we're trying to optimize

 the ability of a neural network to detect cat ears

 and this difference between chess

 and the space the incredibly

 multi-dimensional hundred thousand

 dimensional space that you know networks are trying to optimize over is nothing like the chessboard database

 so it's a totally different kind of thing and okay in that sense you can say

 yeah yeah you

 know i could see how you you might say if if you the

 funny thing is it's the difference between given search space

 and found search space exactly

 yeah maybe that's a different way beautiful

 but okay but you're saying what's your sense in terms of the basic mathematical operations

 and the architectures

 can be hardwired that enables

 those operations do you see the cpus of today still being a really core part of executing

 those mathematical operations

 yes well the operations you know continue to be add subtract loads

 or compare

 and branch it's it's remarkable

 so it's it's interesting that the building blocks of you know computers

 or transistors

 and you know under that atoms

 so you got atoms transistors logic gates computers right

 you know functional units and computers the building blocks of mathematics at some level are things like adds

# Chapter 4

 dimensional space that you know networks are trying to optimize over is nothing like the chessboard database

 so it's a totally different kind of thing and okay in that sense you can say

 yeah yeah you

 know i could see how you you might say if if you the

 funny thing is it's the difference between given search space

 and found search space exactly

 yeah maybe that's a different way beautiful

 but okay but you're saying what's your sense in terms of the basic mathematical operations

 and the architectures

 can be hardwired that enables

 those operations do you see the cpus of today still being a really core part of executing

 those mathematical operations

 yes well the operations you know continue to be add subtract loads

 or compare

 and branch it's it's remarkable

 so it's it's interesting that the building blocks of you know computers

 or transistors

 and you know under that atoms

 so you got atoms transistors logic gates computers right

 you know functional units and computers the building blocks of mathematics at some level are things like adds

 and subtracts and multiplies

 but that's the space mathematics can describe is i think

 essentially infinite

 but the computers that run the algorithms are still doing the same things

 now a given algorithm may say i need sparse data or

 i need 32-bit data

 or

 i need you know like

 a convolution operation that naturally takes 8-bit data multiplies

 it and sums it up a certain way so the like the data types in tensorflow

 imply an optimization set

 but when you go write down a look at the computers it's an inorganic salt applies like

 like that hasn't changed much

 now the quantum researchers think they're going to change that radically

 and then there's people who think about analog computing

 because you look in the brain and it seems to be more analog ish you

 know that maybe there's a way to do that more efficiently

 but we have a million acts on computation

 and i don't know the reference the relationship between computational let's say intensity

 and ability to hit match mathematical abstractions i don't know anyway subscribe dad

 but

 but just like you saw an ai you went from rule

 sets the simple search to complex search does a found search like

 those are you know orders of magnitude more computation to do

 and

 as we get the next two orders of magnitude

 your friend roger godori said like every order magnitude changed the computation

 fundamentally changes

 what the computation is doing here oh you

 know the expression the difference in quantity is the difference in kind

 you know the difference between ant

 and ant hill right

 or neuron

 and brain you know there's there's there's just indefinable place

 where the the quantity changed the quality right

 now we've seen that happen in mathematics multiple times and you

 know my my guess is it's gonna keep happening so your senses

 yeah

 if you focus head down and shrinking a transistor let's

 not just head down and we're aware about

 the software stacks that are running in the computational loads and we're kind of pondering

 what do you do with a petabyte

 of memory that wants to be accessed in a sparse way and

 have you know the kind of calculations ai programmers want

 so there's that there's a dialog interaction

 but when you go in the computer chip you know you find adders

 and subtractors and multipliers

 and

 so

 if you zoom out then with as you mentioned

 which sutton the idea

 that most of the development in the last many decades in the ai research came from just leveraging computation

 and just the simple algorithms

 waiting for the computation to improve well suffer guys have a thing that they called the

 the problem of early optimization right

 so

 if you write a big software stack

 and

 if you start optimizing like

 the first thing you write the odds of that being the performance limiter is low but

 when you get the whole thing working can you make it to x faster by optimizing

 the right things sure while

 you're optimizing that could you've written a new software stack

 which would have been a better choice maybe

 now you have creative tension

 so

 but the whole time as you're doing the writing the

 that's the software we're talking about the hardware underneath gets faster

 which goes back to the moore's laws moore's law is going to continue then your ai research

 should expect

 that to show up and then you make a slightly different set of choices then we've

 hit the wall nothing's

 gonna happen and from here it's just us rewriting algorithms like

 that seems like a failed strategy for the last 30 years of moore's laws death

 so

 so can you just linger on it i think you've answered it

 but it just asked the same dumb question over and over so

 what why do you think moore's law is not going to die

 which is the most promising exciting

 possibility of why it won't done that's five 10 years so is it that continues shrinking the transistor

 or is it another s-curve that steps in and it totally

 so dope shrinking the transistor is literally thousands of innovations right

 so there's so this they're all answers

 and it's there's a whole bunch of s-curves just kind of running their course

 and being reinvented

 and new things you know the the semiconductor

 fabricators

 and technologists have all announced what's called nano wires

 so they they took a fan

 which had a gate around it and turned that into a little wire

 so you have better control that

 and they're smaller

 and then from there there's some obvious steps about how to shrink that

 so the metallurgy around wire stocks

 and stuff has very obvious abilities to shrink and you

 know there's a whole combination of things there to do your

 sense is that we're gonna get a lot

 yes this innovation from just that shrinking

 yeah like a factor of a hundred salade

 yeah i would say that's incredible

 and it's totally it's only 10 or 15 years

 now you're smarter you might know but to me it's totally unpredictable of

 what that hundred x would bring in terms of the nature of the computation

 and people be yeah you familiar with bell's law

 so for a long time those mainframes

 mini's workstation pc mobile moore's law drove faster smaller computers right

 and then we

 were thinking about moore's law rajae godori said every 10x generates a new computation

 so scalar vector made erichs topological computation right

 and

 if you go look at the industry trans there was no mainframes

 and mini-computers and pcs

 and then the internet took off and then we got mobile devices

 and

 now we're building 5g wireless with one millisecond latency and

 people are starting to think about the smart world where everything knows

 you recognizes you like

 like like the transformations are going to be like unpredictable

 how does it make you feel that you're one of the key

 architects of this kind of futures you're not we're not talking about the architects of the high-level

 people who build the angry bird apps

 and flapping

 angry bird of who knows we're gonna be that's the whole point of the universe

 let's take a stand at that and the attention

 distracting nature of mobile

 phones i'll take a stand but anyway in terms of that matters much

 the the side effects of smartphones

 or the attention distraction

 which part well who knows you know where this is all leading it's changing

 so fast wax my parents

 do steal my sister's

 for hiding in the closet with

 a wired phone with a dial on it stop

 talking your friends all day right

 now

 my wife feels with my kids for talking to their friends all day on text looks

 the same to me it's always it's echoes of the same thing okay but you are the one

 of the key people architecting

 the hardware of this future

 how does that make you feel do you feel responsible

 do you feel excited

 so we're we're in a social context

 so there's billions of people on this planet there

 are literally millions of people working on technology i feel lucky to be

 you know what doing

 what i do and getting paid for it and there's an interest in it but

 there's so many things going on in parallel it's like

 the actions are so unpredictable if i wasn't here somebody else are doing the

 the vectors of all these different things are happening all the time

 you know there's a i'm sure some philosopher

 or meta philosophers you know wondering about how we transform our world

 so you can't deny the fact that these tools whether

 that

 these tools are changing our world that's

 right do you think it's

 changing for the better so

 some of these i read this thing recently it said the peat the two disciplines with

 the highest gre scores in college are physics in philosophy right

 and they're both sort of trying to answer the question why is there anything right

 and the philosopher's you know are on the kind of theological side

 and the physicists are obviously on the you know the material side and there's a hundred billion galaxies

 with a hundred billion stars it seems well repetitive at best

 so i you know there's on our way to ten billion people

 i mean it's hard to say what it's all for is that's what you're asking

 yeah i guess i guess i do tend to are significantly increases in complexity

 and i'm curious about

 how

 computation like like our world our physical world inherently generates mathematics it's kind of obvious right

 so we have x y z coordinates you

 take a sphere you make it bigger you get a surface that falls

 you know grows by r-squared like

 it generally generates mathematics

 and the mathematicians

 and the physicists

 have been having a lot of fun talking to each other for years and computation has been let's

 say relatively pedestrian like computation

 in terms of mathematics has been doing binary binary algebra while those guys have been gallivanting

 through the other realms of possibility right

 now recently the computation

 lets you do math m'q mathematical computations that are sophisticated enough that nobody understands

 how the answers came out right

 machine learning machine lying yeah it used to be you get data set you

 guess at a function the function is considered physics if it's predictive of new functions

 data sets modern

 you

 can take a large data set with no intuition

 about what it is and use machine learning to find a pattern that has no function right

 and it can arrive at results that i don't know if they're completely mathematically describable

 so a computation is kind of done

 something interesting compared to a pov plus see there's

 something reminiscent of that step from the basic operations of addition

 to taking a step towards new all networks that's reminiscent of

 what life on earth and its origins was doing do

 you think we're creating sort of the next step in our evolution in creating

 artificial intelligence systems that i don't

 know i mean you

 know if there's so much in the universe

 already it's hard to say

 well i'm

 standing in his hold are human beings working on additional abstraction layers and possibilities yet appear

 so does

 that mean that human beings don't need dogs you

 know no like like there's so many things that are all simultaneously

 interesting

 and useful but you've seen through i agree you've seen great

 and greater level abstractions

 and built in artificial machines

 right do

 you think when you look at humans you think that the look of all life

 on earth as a single organism building

 this thing this machine that greater

 and greater levels of abstraction do you think humans are the peak

 the top of the food chain in this long

 arc of history on earth

 or do you think we're just somewhere in the middle are we are we the basic functional

 operations of a cpu are we the c++

 program the python perl network like somebody's you

 know people have calculated

 like how many operations

 does the brain do and something you

 know i've seen the number 10 to the 18th about bunch of times arrive different ways so

 could you make a computer that did 10 to the 20th operations

 yes sure do

 you think we're gonna do that now is

 there something magical about how brains compute things i don't know you

 know my personal experiences

 interesting cuz you know you think

 you know how you think and then you have all these ideas and

 you can't figure out how they happened

 and

 if you meditate you know the like

 what what you can be aware of is interesting

 so i don't know if brains are magical

 or not you know the physical evidence says no lots of people's personal experiences yes

 so

 what would be funny as if brains are magical

 and yet we can make brains with more computation you

 know i don't know what to say about that but what

 do you think magic is an emergent phenomena

 what would be our than me i don't know

 teller of what what

 what in your view is consciousness

 with with consciousness

 yeah like what you know cautiousness

 love things

 that are these deeply human things that seems to emerge from our brain is that something

 that we'll be able to make

 encode in chips that get faster

 and faster and faster and faster the flick of 10 our conversations

 no but nobody really knows can you summarize it in a couple of couple of words

 many people have observed that

 organisms run at lots of different levels right

 if you got two neurons somebody said you'd have one sensory neuron and one motor neuron right

 so we move towards things and away from things

 and we have physical integrity and safety

 or not right

 and then

 if you look at the animal kingdom

 you can see brains that are a little more complicated

 and at some point there's a planning system

 and then there's an emotional system that's you know happy about being safe or unhappy

 about being threatened right

 and then our brains have massive numbers of structures you know like planning

 and movement

 and thinking

 and feeling

 and drives

 and emotions

 and we seem to have multiple layers of thinking systems

 and we have a brain a dream system that nobody understands whatsoever

 which i find completely hilarious and

 you can think in a way that those

 systems are more independent

 and you can observe you know the different parts of yourself can observe i don't

 know which one's magical i don't know which ones not computational

 so is it possible that it's all computation probably is

 there a limit to computation i don't think so do

# Chapter 5

 if you look at the animal kingdom

 you can see brains that are a little more complicated

 and at some point there's a planning system

 and then there's an emotional system that's you know happy about being safe or unhappy

 about being threatened right

 and then our brains have massive numbers of structures you know like planning

 and movement

 and thinking

 and feeling

 and drives

 and emotions

 and we seem to have multiple layers of thinking systems

 and we have a brain a dream system that nobody understands whatsoever

 which i find completely hilarious and

 you can think in a way that those

 systems are more independent

 and you can observe you know the different parts of yourself can observe i don't

 know which one's magical i don't know which ones not computational

 so is it possible that it's all computation probably is

 there a limit to computation i don't think so do

 you think the universe is a computer i think

 he seems to be it's a weird kind of computer

 because

 if it was a computer right

 like when they do calculations

 on what it how much calculation it takes to describe quantum effects is unbelievably high

 so

 if it was a computer

 when you built it out of something that was easier to compute right

 that's that's a funny it's a funny system

 but then the simulation guys

 have pointed out that the rules are kind of interesting

 like when you look really close it's uncertain

 and the speed of light says you could only look so far and things can't be simultaneous

 except for the odd entanglement problem

 where they seem to be like the rules are all kind of weird

 and somebody

 said physics is like having 50 equations with 50 variables to define 50 variables like

 you know it's it's you

 know like physics itself has been a shitshow for thousands of years it

 seems odd when you get to the corners of everything you know it's either uncomputable

 or on definable

 or uncertain it's

 almost like the designers the simulation are trying to prevent us from understanding it perfectly

 but

 but also the things that require calculations requires

 so much calculation that our idea of the universe of a computer is absurd

 because every single little bit of it takes all the computation in the universe to figure out gee

 that's a weird kind of computer you know you say the simulation is running in the computer

 which has by definition infinite computations not infinite

 oh you mean if the universe is infinite

 yeah

 piece of our universe seems to take infinite computation

 i hit you're out just a lot whoa

 a lot some pretty big number compute this little teeny spot takes all the mass

 in the local one little year by one like your space it's close enough to infinite

 so it's a heck of a computer if it is one i know it's it's

 it's a weird it's a weird description

 because the simulations description seems too the break when you look closely at it but

 the rules in universe seemed to imply something's up that

 seems a little arbitrary the whole the universe the whole thing the the laws of physics you

 know it just seems like like

 how did it come out to be yeah

 the way it is but lots of people talk about that it's you know it's like i

 said the two smartest groups of humans are working on the same problem different different aspects

 and they're both complete failures

 so that's kind of cool

 they might succeed eventually well

 after two thousand years the trend isn't good two

 thousand years is nothing in the span of the history of the universe

 so we have some time but the next thousand years doesn't look good either so that's

 what everybody says that every stage but with

 moore's law as you've just described

 not being dead the exponential

 growth the technology the future seems pretty incredible

 well it'll be interesting that's for sure that's right so

 what are your thoughts on ray

 kurzweil sense that exponential improvement and technology will continue indefinitely that is that how you see moore's law do

 you see moore's law more broadly

 and since the technology of all kinds has a way of stacking

 s curves on top of each other

 where it'll be exponential

 and then we'll see all kinds of what was an exponential of a million mean that's

 that's a pretty amazing number

 and that's just for a local little piece of silicon

 now it's imagine you say decided to get a

 thousand tons of silicon to collaborate in one computer at a million times the density like

 now you know you're talking i don't know 10 to the 20th more computation power then

 our current already unbelievably fast computers like

 nobody knows what that's going to mean you know the sci-fi guys called you know computron 'i'm like

 when like a local civilization turns the nearby star into a computer i like

 i don't that's true

 but so just even when you shrink a transistor

 the that's

 only one dimension of the ripple effects of that but people tend to think about computers

 the cost problem right

 so computers are made out of silicon

 and minor amounts of metals

 and you know this

 and that none of those things cost any money like

 there's plenty of sand like like

 you could just turn the beach and a little bit ocean water in the computers

 so all the cost is

 and equipment to do it and the trend on equipment is once

 you figure out a build the equipment the

 trend of cost is zero elon said first you figure out what

 configuration you want the atoms in and then

 how to put them there right

 yeah cuz well what here's you know his his great insight is people

 are how constrained i have this thing i know how it works and then little

 tweaks to that will generate something as opposed to what do i actually want

 and then figure out how to build it it's a very different mindset

 and almost nobody has it obviously

 well

 let me ask on that topic you

 were one of the key early people in the development of autopilot at least in the hardware side elon

 musk believes that autopilot

 and vehicle autonomy

 if you just look at that problem can follow this kind of exponential improvement in

 terms of the ha the

 how question that we're talking about there's no reason why i can't

 what are your thoughts on this particular space of vehicle autonomy

 and you're a part of it and elon musk's

 and tesla's vision well the computer you need to build was straightforward

 and you can argue well doesn't need to be 2 times faster

 or 5 times or 10 times

 but that's just a matter of time

 or

 price in the short run so that's that's not a big deal you

 don't have to be especially smart to drive a car

 so it's not like a super hard problem

 i mean the big problem with safety is attention

 which computers are really good at not skills

 well let me push back on one you see everything you said it's correct

 but we as humans

 tend to

 tend to take for granted

 how how incredible our vision system is so you can drive a car of 2050 vision

 and you can train a neural network to extract

 a distance of any object in the shape of any surface from a video

 and data

 but that really simple not simple i look that's a simple data problem it's

 not it's not simple it's

 because you because it's not just detecting object it's understanding the scene

 and it's being able to do it in a way that doesn't make errors

 so the beautiful thing about the human vision system

 and the entire brain around the whole thing is we were able to fill in the gaps it's

 not just about perfectly detecting cars it's inferring the occluded

 cars it's trying to it's it's understanding

 the i think it's mostly a bigger problem you

 so you think what data you know with compute with improvement of computation with improvement in collection

 well there is a you know when

 you're driving a car and somebody cuts you off your brain has theories

 about why they did it you

 know they're a bad person they're

 distracted they're dumb you

 know you can listen to yourself right

 so

 you know if you

 think that narrative is important to be able to successfully drive a car then current

 autopilot systems can't do it but if cars

 are ballistic things with tracks and probabilistic changes of speed and direction and roads are fixed

 and given by the way they don't change dynamically

 right you can map the world really thoroughly you can place every object really thoroughly

 right you can calculate trajectories of things really thoroughly right

 but everything you said about really thoroughly has a different degree of difficulty

 so you

 could say at some point computer

 autonomous systems will be way better it's things

 that humans are allows yet like it'll be better at abstention they'll

 always remember there was a pothole in the road that

 humans keep forgetting about they'll

 remember that this set of roads

 how these weirdo lines on it the computers figured out once and especially

 if they get updates

 so if somebody changes a given like that akita robots

 and stuff somebody said is to maximize two givens

 okay right

 so

 though having a robot

 pick up this bottle

 cap is ways you put a red dot on the top

 because

 then you have to figure out you know if you want to do

 a certain thing with it you know maximize

 the givens is the thing and autonomous systems are happily maximizing the givens like humans

 when you drive someplace new you remember

 it because you're processing

 it the whole time and after the 50th time you

 drove to work you

 get to work you don't know how you got there right

 you're on autopilot right

 autonomous cars are always on autopilot

 but the cars have no theories about why they got cut off or why they're in traffic

 so they'll never stop paying attention right

 so i tend to believe you do have deaf theories mental models of other people especially pedestrians cyclists

 but also with other cars everything you said is

 like is actually essential to driving driving is a lot more complicated than people realize

 i think so sort of to push back slightly but cut into traffic right

 yeah you can't just wait for a gap you have to be somewhat aggressive you'd be surprised

 how simple a calculation for that is i may

 be on that particular point but there's a that it may

 be asked you to push back i would be surprised you know

 what yeah i'll just say where i stand i would be very surprised

 but i think it's you might be surprised

 how complicated it is that

 i'd say that i tell people's like progress disappoints

 in the short run the surprises in the long run it's very possible yeah i suspect

 in 10 years it'll be just like taken for granted yeah

 but you're probably right

 now look like it's gonna be a $50 solution that nobody cares about like

 gps is like wow gps is we have satellites in space that

 tell you where your location is it was a really big deal now everything is the gps i

 mean yeah it's true but i do think that systems

 that involve human behavior are more

 complicated than we give them credit for so we

 can do incredible things with technology that don't involve humans

 but when you look humans are less complicated than people you

 know frequently obscure i've maybe i stand off right out of large numbers of patterns

 and just keep doing it over

 but i can't trust you because you're a human that's something something

 a human would say but i might my

 hope was on the point you've made is even if no

 matter who is right eve there i'm hoping

 that there's a lot of things that humans aren't good at that machines

 are definitely good i like you said attention

 and things like that well they'll be

 so much better that the overall picture of safety in autonomy

 will be obviously cars will be safer even if they're not as good i'm

 a big believer in safety

 i mean there are already the current

 safety systems like cruise control that doesn't let you run into people and lane-keeping there

 are so many features that you just look at the pareto of accidents

 and knocking off like 80% of them you

 know super doable just a wing guard on the autopilot team

 and the efforts there the

 it seems to be that there's a very intense scrutiny by the media

 and the public in terms of safety the pressure the bar but before autonomous vehicles

 what are your sort of as a person they're working on the hardware

 and trying to build a system that builds a safe vehicle

 and

 so on what

 was your sense about that pressure is it unfair is it expected of new technology it

 seems reasonable i was interested i talked to both american

 and european regulators

 and i was worried that

 the regulations would write into the rules technology solutions like modern brake systems imply hydraulic brakes

 so

 if you'll read the regulations to meet the letter of the law for brakes it

 sort of has to be hydraulic right

 and the regulator said there they're interested in the use cases like

 a head-on crash an offset crash don't hit pedestrians don't

 run into people don't leave the road don't

 run a red light or a stop light they were very much into the scenarios

 and you know and they had they had all the data about

 which scenarios injured

 or killed to most people

 and for the most part those conversations were like

 what's the right thing to do to

 take the next step

 now elan is very interested also in the benefits

 of autonomous driving or freeing people's time and attention as well as safety

 and i think that's also an interesting thing but

 you know building an autonomous system so they're safe and safer

 and people seemed since the goals to be tannic seifer's

 and people having the bar to be safer than people

 and scrutinizing accidents seems philosophically

 you know correct

 so i think that's a good thing

 what r is

 is different than the things you've worked at new intel amd apple with autopilot chip design

 and hardware design

 what are interesting

 or challenging aspects of building this specialized kind of competing system in the automotive space i mean

 there's two tricks to building like an automotive computer one is to

 software our team the machine learning team is developing algorithms that are changing fast

 so as you're building the the accelerator you have this you know worry

 or intuition that the algorithms will change enough that the accelerator will be the wrong one right

 and there's the generic thing which is if you build a really good general-purpose computers

 hey it's performance is one

 and then gpu guys will deliver about 5x to performance for the same amount of silicon

 because instead of discovering parallelism you're given parallelism

 and then special accelerators get another two to five x on top of a gpu

 because you say i know the math is always 8-bit integers

 and two 32-bit accumulators

 and the operations are the subsets of mathematical possibilities

 so although you know ai accelerators have a claimed performance benefit over gpus

 because in the narrow math space you're nailing the algorithm

# Chapter 6

 so i think that's a good thing

 what r is

 is different than the things you've worked at new intel amd apple with autopilot chip design

 and hardware design

 what are interesting

 or challenging aspects of building this specialized kind of competing system in the automotive space i mean

 there's two tricks to building like an automotive computer one is to

 software our team the machine learning team is developing algorithms that are changing fast

 so as you're building the the accelerator you have this you know worry

 or intuition that the algorithms will change enough that the accelerator will be the wrong one right

 and there's the generic thing which is if you build a really good general-purpose computers

 hey it's performance is one

 and then gpu guys will deliver about 5x to performance for the same amount of silicon

 because instead of discovering parallelism you're given parallelism

 and then special accelerators get another two to five x on top of a gpu

 because you say i know the math is always 8-bit integers

 and two 32-bit accumulators

 and the operations are the subsets of mathematical possibilities

 so although you know ai accelerators have a claimed performance benefit over gpus

 because in the narrow math space you're nailing the algorithm

 now you still try to make it programmable

 but the ai field is changing really fast so there's a you

 know there's little creative tension era of i want the acceleration afforded by specialization

 without being over specialized

 so that the new algorithm is

 so much more effective that you'd have been better off on a gpu

 so there's attention there to

 build a good computer for an application like automotive there's

 all kinds of sensor inputs

 and safety processors

 and a bunch of stuff so one of loans goal is to make it super affordable

 so every car gets an autopilot computer

 so

 some of the recent startups you look at and they have a server in the trunk

 because they're saying i'm going to build this autopilot computer replaces the driver

 so their cost budgets ten or twenty thousand dollars

 and eelain's constraint was i'm gonna put one every in every car whether people buy autonomous

 driving or not so

 the cost constraint he had in mind was great right

 and to hit that you

 had to think about the system design that's complicated it's

 it's fun you know it's like it's like it's craftsmen's

 work like a violin

 maker right you could say stradivarius is this incredible thing the musicians are incredible

 but the guy making the violin

 you know picked wood and sanded it and then he cut it you

 know and he glued it and you know and he waited for the right day

 so

 that when you put the finish on it didn't

 you know do something dumb that's craftsmen's work right

 you may be a genius craftsman

 because you have the best techniques

 and you discover a new one

 but most engineers craftsmen's work and humans really like to do that you know smart humans

 oh no everybody

 oh i

 know i used to i dug ditches when i was in college

 i got really good at it satisfying

 yeah

 so digging ditches is also craft malware

 yeah of course

 so

 so there's an expression called complex mastery behavior

 so when you're learning something that's fun because you're learning something when

 you do something that's wrote and simple it's not that satisfying

 but if the steps that you have to do or complicate it and you're

 good at them it's satisfying to do them and then

 if you're intrigued by it all as you're doing them you sometimes learn new things that

 you can raise your game

 but christmas work is good in engineers like engineering is complicated

 enough that you have to learn a lot of skills and

 then a lot of what you do is then craftsmen's

 work which is fun autonomous

 driving building a very

 a resource-constrained computer

 so computer has to be cheap enough that put in every single car that's

 essentially boils down to

 craftsmen's work it's saying genius

 so there's thoughtful decisions

 and problems to solve and trade-offs

 to make do you need 10 cameron ports or 8 you know you're

 building for the current car or the next one you

 know how do you do the safety stuff

 you know there's there's a whole bunch of details

 but it's fun but it's not like i'm building a new type and they're all networked

 which has a new mathematics

 and a new computer at work do

 you know that that's like there's a there's more invention than that

 but the rejection to practice once you picked the architecture you look inside

 and what do you see adders

 and multipliers

 and memories

 and you know the basics

 so computers is always just this weird set of abstraction layers of ideas

 and thinking that reduction to practice is transistors

 and wires and you know pretty basic stuff

 and that's

 an interesting phenomena by

 the way that like factory work like

 lots of people think factory work is road assembly stuff i've

 been on the assembly line like

 the people work that really liked it it's a really great job it's

 really complicated putting cars together is hard right

 and in the cars moving

 and the parts are moving and sometimes the parts are damaged

 and you have to coordinate putting

 all the stuff together and people are good at it they're

 good at it and i remember one day i went to work and the

 line was shut down for some reason and then

 some of the guys sitting around were really bummed because they they had reorganized

 a bunch of stuff

 and they were gonna hit a new

 record for the number of cars built

 that day and they

 were all gung ho to do it and these were big tough buggers

 yeah you know but

 what they did was complicated

 and you couldn't do it

 yeah

 and

 i mean well

 after

 a while you could but you'd have to work your way up cuz you know like

 putting a bright what's

 called the bright stuff at the trim on a car on a moving assembly line where

 it has to be attached 25

 places in a minute and a half is unbelievably complicated

 and

 and

 and human beings can do it's really good i think

 that's harder than driving a car by the way putting

 together working working on the factory to smart

 people can disagree

 yeah i think drive driving a car will

 get you in the factory something will

 see you're not for us humans driving a car is easy i'm saying building a machine that

 drives a car is not easy ok ok driving a car is easy for humans

 because we've been evolving for billions of years drive cars

 yeah no juice the pail if the cars are super cool no

 now you join the rest of the internet and mocking me ok

 yeah

 yeah intrigued by your you know your anthropology

 yeah it says we have to go dig into that there's some inaccuracies there

 yes ok

 but in general

 what have you learned in terms of thinking about passion

 craftsmanship

 tension chaos

 you know the whole mess of it

 or

 what have you learned have

 taken away from your time working with elon

 musk working at tesla which is known to be a place of chaos innovation

 craftsmanship

 and i really like the way he thought like you think you have an understanding about

 what first principles of something is and then you talk to you alone about it and you you

 didn't scratch the surface you

 know he has a deep belief that

 no matter what you do is a local maximum right

 i had a friend he invented a better electric motor and it

 was like a lot better than what we were using and

 one day he came by he said you know i'm

 a little disappointed cuz

 you know this is really great and you didn't seem that impressed and i said you

 know and the super intelligent aliens come are they gonna be looking for you like

 where is he the guy you built the motor

 yeah probably not you know like like the

 but doing interesting work that's both innovative

 and let's say craftsmen's work on the current thing it's really satisfying it's good and

 and that's cool and then

 elon was good taking everything apart and like what's the deep first principle

 oh no

 what's really what's really you know you know you

 know that that you know ability to look at it without assumptions

 and

 and

 how constraints is super wild you

 know we build rocket ship and using

 the same car you know everything

 and that's super fun and he's into it too like when

 they first landed to spacex rockets at tesla we

 had a video projector in the big room and like five

 hundred people came down and when they landed everybody cheered

 and some people cried it was so cool alright

 but how did you do that well

 it

 was super hard and then

 people say well it's chaotic really to

 get out of all your assumptions you think that's not going to be unbelievably painful

 and there's

 elon tough yeah probably the people look back on it and say boy i'm really happy

 i had that experience to go take

 apart that many layers of assumptions

 sometimes super fun sometimes painful

 so it could be emotionally

 and intellectually painful that whole process just stripping away assumptions

 yeah i imagine 99% of your thought process is protecting your self conception

 and 98% of that's wrong

 yeah

 now you got there math right no

 you think your feeling when you get back into that one bit that's useful

 and

 now you're open

 and you have the ability to do something different i don't

 know if i got the math right it might be ninety nine point nine but in 850

 imagining it the 50% is hard enough yeah

 now for a long time i've suspected you could get better look

 you can think better you can think more clearly you can take things apart and there's

 lots of examples of that people who do that

 so any line is an example of that parent

 or an example says you know if i am i'm

 fun to talk to certainly

 i've learned a lot of stuff right

 well here's the other thing it's like i talk like like i read books and

 people think oh you read books well no i brought a couple books

 awake for 55 years well maybe 50 cuz i didn't read learned read tall as h or something

 and

 and it

 turns out when people write books they often take

 20 years of their life where they passionately

 did something reduce it to to 200 pages that's

 kind of fun and then

 the goat you go online and you can find out

 who wrote the best books and who like you know that's kind of alda

 so there's this wild selection process

 and then you can read it and for the most part to understand it

 and then you can go apply it like

 i went to one company and i thought i haven't managed much before

 so i read 20 management books and i started talking to him basically

 compared to all the vp's running around i'd

 run night read 19

 more management books than anybody else

 was it even that hard

 yeah

 and a half the stuff worked like first time it wasn't even rocket science but at

 the core of that is questioning the assumptions

 okay sort of entering

 the thinking first principles

 thinking sort of looking at the reality of the situation and using it using

 that knowledge applying that knowledge so

 mean yes so i would say my brain has this idea that you can question first assumptions

 and

 but i can

 go days at a time and forget that and

 you have to kind of like circle back data observation

 because it is because part allen gene well it's hard to keep it front

 and center

 because you know you're you operate on so many levels all the time and you

 know getting this done takes priority

 or you know being

 happy takes priority or you know screwing

 around takes priority like like like

 how you go through life it's complicated

 yeah

 and then you remember

 oh yeah i could really i think first principles

 so much that's that's tiring you

 know what you do for a while that's kind of cool

 so

 just as the last question your sense from

 the big picture from the first principles do

 you think you kind of answered already

 but do you think autonomous driving something we can solve on a timeline of years

 so one two three five ten years as opposed to a century yeah definitely just

 to linger and a little longer where's the confidence coming

 from is it the fundamentals of the problem the fundamentals of building a hardware

 and the software as a computational problem understanding

 ballistics roles topography

 it seems pretty solvable

 i mean

 and you can see this you know like like speech recognition

 for a long time people are doing you know frequency

 and domain analysis

 and and all kinds of stuff and that didn't work for at all right

 and then they did deep learning about it and it worked great and it took multiple iterations

 and

 you

 know time is driving his way past the frequency analysis point you

 know use radar don't run into things

 and the data gathering is going up in the computations

 going up and the algorithm understanding is going up and there's

 a whole bunch of problems getting solved

 like that the data side is really powerful but i disagree with both you

 and you and i'll tell you and once again as i did before that that

 when you add human beings into the picture the

 it's no longer a ballistics problem it's something more complicated

 but i could

 be very well proven

 cars are hardly damped in terms are ready to change like

 the steering and the steering systems really slow compared to a computer the acceleration

 of the acceleration is really slow

 yeah on

 a certain time scale on a ballistics

 time scale but human behavior i don't know it

 yeah

 i shouldn't say it beans are really slow to weed weirdly

 we operate you know half a second behind reality nobody

 really understands that one either it's pretty funny

 yeah

 yeah

 so no

 i will be with very well could be surprised

 and i

 think with the rate of improvement in all aspects i'm both the computed in the the the software

 and the hardware there's gonna be pleasant surprises all over the place

 speaking of unpleasant surprises many people have worries about a singularity in the development of ai

 forgive me for such questions you know what

 when ai improves exponentially

 and reaches a point of superhuman level general intelligence you

 know beyond the point there's no looking back do

 you share this worry of existential threats from artificial intelligence from computers

 becoming superhuman level intelligent

 no not really you

 know like we already have a very stratified society

 and then

 if you look at the whole animal kingdom of capabilities

 and abilities and interests

 and you

 know smart people have their niche and you know normal people have their niche and craftsmen's

 have their niche and you know

 animals have their niche i suspect

 that the domains of interest for things that you know astronomically

 different like the whole something

 got 10 times smarter than us and wanted to track us all down because what we

 like to have coffee at starbucks like

 it doesn't seem plausible no is there an existential problem that how

 do you live in a world where there's something way smarter than you and you

 you based your kind of self-esteem on being

 the smartest local person well there's what 0.1% of the population who thinks that because

 the rest of the populations been dealing with it since they were born

 so the the breadth of possible experience that can be interesting is really big and

 you know super intelligence seems likely although we still don't know if we're magical

# Chapter 7

 no not really you

 know like we already have a very stratified society

 and then

 if you look at the whole animal kingdom of capabilities

 and abilities and interests

 and you

 know smart people have their niche and you know normal people have their niche and craftsmen's

 have their niche and you know

 animals have their niche i suspect

 that the domains of interest for things that you know astronomically

 different like the whole something

 got 10 times smarter than us and wanted to track us all down because what we

 like to have coffee at starbucks like

 it doesn't seem plausible no is there an existential problem that how

 do you live in a world where there's something way smarter than you and you

 you based your kind of self-esteem on being

 the smartest local person well there's what 0.1% of the population who thinks that because

 the rest of the populations been dealing with it since they were born

 so the the breadth of possible experience that can be interesting is really big and

 you know super intelligence seems likely although we still don't know if we're magical

 but i suspect we're not

 and it seems likely that'll create possibilities that are interesting for us and it's

 its interests will be interesting for that for whatever it is it's

 not obvious why it's interest would somehow

 want to fight over some square foot of dirt or you know whatever

 then you know the usual fears

 are about so you don't think you'll inherit some of the darker aspects of human nature depends

 on how you think reality is constructed

 so for for whatever reasons human

 beings are and that's a creative tension in opposition with both are good and bad

 forces like there's lots of philosophical understandings of that

 right i don't know why that would be different

 so

 you think the evils is necessary for the good i mean the tension i don't know about evil

 but like we live in a competitive world

 where your good is somebody else's you know evil you

 know there's there's the malignant part of it but that seems to be

 self-limiting although occasionally it's it's super horrible

 but

 yeah look there's a debate over ideas

 and some people have different beliefs

 and that that debate itself is a process

 so the at arriving at something you know i wouldn't continue

 yeah

 just you

 but you don't think that whole process will leave humans behind in a way that's painful an emotionally

 painful yes for the one for the point one percent they'll be there why isn't it already painful

 for a large percentage of the population and

 it is i mean society does have a lot of stress in it about

 the 1% and the bath of this and about to that but you know everybody

 has a lot of stress in their life about what they find satisfying

 and

 and you know know yourself seems to be the proper dictum

 and pursue something that makes your life meaningful seems proper

 and there's

 so many avenues on that like there's

 so much unexplored space at every single level

 you know i'm somewhat of my nephew called me a jaded optimist you

 know

 so it's there's a beautiful tension that in that label

 but

 if you

 were to look back at your life and

 could relive a moment a set of moments

 because there were the happiest times in your life outside of family

 what would that be i

 don't want to relive any moments i like that i like that situation

 where you have some amount of optimism

 and then the anxiety of the unknown

 so

 you love the unknown do you the

 mystery of it i don't know about the mystery it sure gets your blood pumping

 what

 do you think is the meaning of this whole thing of life on this pale blue dot it

 seems to be what it does

 like the universe for whatever reason

 makes atoms

 which makes us

 which we do stuff

 and we figure out things

 and we explore things

 and that's just what it is it's not just

 yeah it is you

 know jim i don't think there's a better place to end it it's a huge honor

 and well

 super fun thank you so much for talking today all right great thanks

 for listening to this conversation and thank you to our presenting sponsor cash app downloaded

 use code lex podcasts you'll

 get ten dollars and ten dollars will go to first a stem education nonprofit

 that inspires hundreds of thousands of young minds to become future leaders and innovators

 if you

 enjoy this podcast subscribe

 on youtube give it five stars an apple podcast follow on spotify supported on patreon

 or simply connect with me on twitter

 and

 now let me leave you with some words of wisdom from gordon moore for

 everything you try works you aren't trying hard enough

 thank you for listening and hope to see you next time

 you

