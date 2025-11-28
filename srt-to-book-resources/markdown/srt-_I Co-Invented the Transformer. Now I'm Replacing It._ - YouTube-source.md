# Chapter 1

despite the fact that i was involved in inventing the transformer

luckily

luckily

no one's been working on them as long as i have rights

with maybe the exception of the other se seven authors.

so i actually made the decision uh

earlier this year

that i'm going to drastically reduce the amounts of of research that i'm doing specifically on the transformer

because of the feeling

that i have

that it's it's an oversaturated space, right? it's not

that there's no more interesting things to be done with them.

and i'm going to make use of the opportunity to do something different, right? to actually turn up the amount of exploration

that i'm doing in my research.

we just released the continuous thought machine.

it's a spotlight at europe's 2025 this year.

you should care about it because it has native adaptive compute.

it's a new way of building a recurrent model that uses higher level concepts for neurons

and a synchronization as a representation that lets us solve problems in ways that seem more human

by being biologically and nature inspired.

the atmosphere in ai research was actually quite different back during the transformer

uh

uh

uh

because it doesn't feel like something similar could actually happen right now.

because of the reduced amount of freedom

that we have, right? the transformers was very very bottom up, right? it's not

that somebody had this grand plan

that came down from on high that this is what we should be working on.

it was a bunch of people talking over lunch, thinking about what the current problems are

and how to solve them

and having the freedom to have, you know,

literally months to dedicate to just trying this idea and having this this new architecture fall out.

we've spent hundreds of millions of dollars.

the biggest sort of evolution based search is probably in the tens of thousands.

we have all this compute.

what happens? what happens if you scale up these search algorithms?

and i'm sure you'll find something interesting, you know,

when someone eventually does bite that bullet and really scale up these evolutionary sort of a life experiments

because i pitched it in an environment where people were just going all in on this one technology.

i got zero interest.

so now i have my own company and i can pursue those directions.

this podcast is supported by cyber fund. > > hey folks,

i'm omar,

product and design lead at google deepmind.

we just launched a revamped vibe coding experience in ai studio that lets you mix

and match ai capabilities to turn your ideas into reality faster than ever.

just describe your app

and gemini will automatically wire up the right models and apis for you.

and if you need a spark, hit

i'm feeling lucky and we'll help you get started.

head to a. studio / build studio / build to create your first app. > >

two for ai labs is a research lab based in zurich.

they've got a team of amazing ml engineers and research scientists.

they're doing some really cool stuff. if you look at their website, for example,

you can see what their approach was for winning the arc agi 3 pub

uh

uh

uh

and they are hiring amazing ml engineers and research scientists.

they also care deeply about ai safety.

so if any of that is a fit for you, please go to two for aolabs

and

and

and

the audience will know i'm a huge fan of kenneth stanley's ideas.

so his book, why greatness cannot be planned, changed my life.

it was absolutely insane.

it was absolutely insane.

that we need to allow people to follow their own gradient of interest

unfettered

by objectives and committees and and so on.

because that is how we do epistemic foraging.

that

when you have too many agendas involved in the mix, you kind of end up with a gray goo

and you don't discover, you know,

interesting novelty and diversity. and i suppose that's basically the thesis of of your company, sakana,

is to lean into those ideas. > > yes, exactly.

um, at the company, we're a massive fan of that book.

we're we're hoping to have him come and talk at our company next week, actually.

and um it's a philosophy

that we we do talk about internally, right? we have copies of the books in

including the

the recent japanese translation. as you know,

one of the co-founders, one of my my main jobs, one of the main things

that i have to keep doing for this company is making sure

that we protect the freedom that the researchers currently have, right?

because it's

it's

it's

it's a privilege really that we have the resources to be able to do that. and inevitably,

as i've seen happen,

as the company grows, more and more pressure comes in and it narrows the freedom.

but i think

because, you know, we we believe in this philosophy so strongly, i'm hoping

that we can give people all the research freedom that we do now

um for as long as possible.

> > and what are those processes that curtail freedom as a company matures?

i mean, how would you describe that?

it's great that there's never been so much interest

and people

and people

and resources

and money in the industry, but unfortunately

that just increases the amount of pressure people have in order to compete with all the other people working on it

and trying to get the the value out of this technology and making money.

and i think that's what just happens, right? as a startup, you have a a feeling of, you know,

excitement and trying something new.

and right at the beginning, you have a bit of a runway.

so, you have the freedom to try different things.

but inevitably, people are starting to ask for returns on their investments

or they're expecting you to churn out some product.

and this just unfortunately reduces the uh

the

the

the

the

the

the

the

or the pressure to to create technology that's actually useful for the products that we have goes up

and so the feeling of autonomy i think starts to go down. but you know

i literally tell people when they start working for the company

i want you to work on what you think is interesting and important

and i mean it there

and i mean it there

and i mean it there

there's a phenomenon called audience capture

> > right > >

and i think there might be a phenomenon called technology capture

which is that in the early days of google

it was quite open-ended and i mean transformers is now the ubiquitous backbone of all ai technology

and it's a huge achievement that that you're involved in

but i mean there's a similar story with with open ai.

they're now starting to see all of these commercialization opportunities. they they can

i mean they're going to become linkedin.

they're going to become an application platform.

they're going to become a search platform.

they're going to become a social network.

and

and i guess this could happen to you guys

that there's a very strong chance, especially with your new paper

that we're going to talk about today, this continuous thought machines.

it it could be a revolutionary technology, but then it will become obvious how it could be commercialized.

and that's how those pressures come in. > > i

i like the i like the audience capture analogy. i think

um

um

by large language models, right? they they worked so well that everyone wanted to work on them.

and i'm really worried that we're kind of stuck in this local minimum now, right?

and we sort of need to try to try to escape it.

so, we spoke about the transformers, but there's a there's a time just before the transformers

that i'd like to talk about

because i think it's quite illustrative.

so, of course, the

the main technology before transformers was recurrent neural networks, right? and there was a similar feeling, right?

when recurrent neural networks came in and we

we

we

we discovered this new sort of sequence of sequence learning,

that was also a massive breakthrough, right? the

that was also a massive breakthrough, right? the

that was also a massive breakthrough, right? the

the

the translation quality went up massively, right? um

the translation quality went up massively, right? um

uh

quality went up massively. and there was this a similar sort of feeling then of like

okay

okay

okay

okay

we found the technology and we just need to sort of perfect this technology

and back then

and back then

and back then

and back then

character level language modeling

right

so every time a new rnn based character level language modeling paper came out

i got quite excited

i got quite excited

i got quite excited

i got quite excited

i got quite excited

i'd want to like

quickly read the paper like okay

quickly read the paper like okay

quickly read the paper like okay

how did they get the improvements

but the papers were always these

just these slight modifications on the same architecture, right? it was lstms and grus

and maybe

and maybe

initializing it with the identity matrix to so that you could use the relu function

or like

or like

or if you

if you layer them in a slightly different way

or if you had gating going upwards as well as as sideways.

um,

um,

um,

uh

like hierarchical lstm where it would actually decide to compute or not compute the different layers.

and if you trained on wikipedia and you looked at the structure of

when it was decided to compute or not compute,

it kind of looked like the structure of of the the sentences were actually being picked up

by the model.

and i used to love that sort of stuff, right? um,

and i used to love that sort of stuff, right? um,

and i used to love that sort of stuff, right? um,

the

the improvements were always like 1. 26 bits per character, 1. 25 bits per character, 1. 24.

that was a result that was publishable, right? that was exciting. but then after the transformer

the team that i went on to

afterwards

afterwards

afterwards

very deep transformer models

decoder only transformer models to language modeling

and we immediately got something like 1. 1

uh

right

so so something that was so good that people actually come to our desk and politely tell us like

uh

uh

uh

like a calculation

do you think it's nats

do you think it's nats

do you think it's nats

do you think it's nats

no

we

we

we

we

we

we

what struck me later is that all of a sudden all of that research

and to be clear

very good research was suddenly made completely redundant. > > yes.

> > right.

all of those endless permutations to to rnn's were suddenly seemingly a waste of time.

we're kind of in the situation right now

where a lot of the papers are just taking the same architecture

and making these endless amount of different tweaks of

like

you know where to put them normalization layer and slightly different ways of training them

and and we might be wasting the time in exactly the same way

right

right

right

i don't think that this is the final architecture

and we just need to keep scaling up

there's some breakthrough that will occur at some point

and then it will once again become obvious that we're kind of wasting a lot of time right now.

> > yeah. so we are a victim of our own success

and this basin of attraction

and this basin of attraction

sarah hooker spoke about the hardware lottery and this is a kind of architecture lottery

and it it

it actually made me think of the um agricultural revolution

which is that this kind of phase change happened

and all of the folks that had these skills that were so necessary, these diverse skills for living

and surviving, they died out.

and that's actually quite paradoxical because we need those skills to take the next step.

m > > and so we

we're now in this regime

we're now in this regime

and the implication is that you can do anything with a foundation model in the corporate world

we used to have data scientists

we used to have data scientists

they were ml engineers doing these architectural tweaks

even in

even in

even in

and now we just have ai engineers who are just doing prompt engineering

and so on.

so you're saying that the fundamental skills that we need to be diverse to think of new solutions

and new architectures, they're dying out.

i think i'm going to disagree with that. i think the problem is we have plenty of very talented

uh

very creative researchers out there, but they're not using their talents. right? for example,

you know,

if you're in academia, there's pressure to publish, right?

and if there's pressure to publish, you think to yourself, okay, well, i have this really cool idea, but it might not work.

it might be too weird, right? it might be difficult to get it accepted

because i have to sort of like sell the idea more.

or i can just try this new positional embedding,

right? the problem is that the current environment both in academia

and in companies are not actually giving people the freedom

that they need to do the research that they probably want to do.

i > > mean there's also this interesting thing that even in spite of great new research

i mean i was speaking to seb hoger

and he's got all of these new architectural ideas and open ai aren't implementing them.

i mean google are doing this diffusion language model

which is quite cool.

and i i'd like to know your opinion on why that is.

so there's a few philosophies floating around like this concept of a universal representation

that there are universal patterns and the the transformer representations resemble those in the brain.

and it's rather led to this idea of

well

well

because if we just have more scale and more compute

then all roads lead to rome.

so why would we bother doing it any differently? > > there's actually better

right? there is actually already architectures that have been shown in the research to work better than transformers.

okay.

but not better enough in order to move the entire industry away from such an established architecture

where you're familiar with it.

you know how to train it.

you know how to train it.

you know how the internals work, right? you know how to fine-tune them.

you have all this software is already set up for training transformers.

fine gening transformers

inference.

so if you want to move the industry away from that,

# Chapter 2

and i i'd like to know your opinion on why that is.

so there's a few philosophies floating around like this concept of a universal representation

that there are universal patterns and the the transformer representations resemble those in the brain.

and it's rather led to this idea of

well

well

because if we just have more scale and more compute

then all roads lead to rome.

so why would we bother doing it any differently? > > there's actually better

right? there is actually already architectures that have been shown in the research to work better than transformers.

okay.

but not better enough in order to move the entire industry away from such an established architecture

where you're familiar with it.

you know how to train it.

you know how to train it.

you know how the internals work, right? you know how to fine-tune them.

you have all this software is already set up for training transformers.

fine gening transformers

inference.

so if you want to move the industry away from that,

being better is not good enough.

it has to be obviously crushingly better.

transformers were that much better over rnns.

okay, transformers

where you just applied it to a new problem

and it just was so so much faster to train

and you just got such higher accuracy that you just had to move.

and i think the deep

the deep learning revolution was also another example of that, right? where you had plenty of skeptics

and people were pushing um neural networks even back then and people are going, " no,

we think symbolic stuff will work better.

" but then they demonstrated it as being so much better that you couldn't ignore it.

this fact makes finding the next thing even harder.

right? that's the gravitational pole of always pull pulling you back to, oh, okay,

but a transformer is good enough. and yeah, you made a cool little architecture over here that

yeah, it looks like it's

it's got better accuracy, but openai over here just made it 10 times bigger and it beats that.

so, let's just keep going. may i also submit that there could be an additional reason

which is

which is

i love that fractured entangled representations paper. um

there's there's this shortcut learning problem

and i think that there's a little bit of a mirage going on here and there

there might be problems with these language models that we don't

you know that we're not fully aware of

and there's also this thing that we're seeing that we are starting to bastardize the architecture.

so we know we need to have adaptive computation for reasoning. we know we want things like uncertainty quantification

and what we're doing is is we're bolting these things on top rather

than having an architecture which intrinsically does all of these things

that we know we need.

> > yeah.

> > yeah.

and i think the the our continuous thought machine is is an attempt at addressing those um more directly, right? which which luke will be able to tell you more about later.

there's something still not quite right with this

the current technology, right? i i think the the phrase

that's becoming popular is jagged intelligence, right? that the fact that you can ask an llm something

and it can solve literally like a phd level problem

and then you know in the next sentence it can say something just so clearly obviously wrong that it

it's

it's

right? and i think this is actually a reflection of something probably quite fundamentally wrong with the current architecture.

as amazing as they are, the current technology is actually too good.

okay.

another reason why it's it's difficult to move away from them, right? so they're too good in in in the following sense.

and you you spoke about the fact that we have these foundation models.

that's okay.

so that we have the foundation that we can do anything with them.

yes, i think current neural networks are so powerful that if you have enough patience

and enough compute and enough data, you can make them do anything.

but i don't necessarily think

that they want to, right? we're sort of forcing them like they're universal pro approximators

but i think there are probably a space of you know function approximators

that will more want to represent things in the way that a human represents them.

so there's actually quite an obscure paper that is my poster child for this. it's called intelligence matrix exponentiation

> > and i think it was actually rejected. so, you know, you can probably project

uh

the image of a figure one,

but there's an image of it's solving, you know, the classical spiral data set of needing to separate the two classes in the spiral.

> > yes. > >

and it has the decision boundary for a for both a classic rnn

and it has the decision boundary for a for both a classic rnn

multi-layer perceptron and a tanh

multi-layer perceptron. and you can see they both solve it, right? technically, they both solve the problem because they

they

they classify all the points correctly

and get a very good test score on this on this very simple data set.

and then they show you the decision boundary for the for the m layer

that they built in this paper

and it's a spiral. the layer represented the spiral as a spiral. sh

shouldn't

shouldn't

shouldn't

you know if the data is a spiral

shouldn't we represent it as a spiral?

and then if you look back at the decision boundaries for for the spiral

and the classic relu multi-layer perceptron, it's clear that you just have these tiny little peacewise linear separations.

um,

um,

if you know if you train these things enough

and you push these little peacewise linear boundaries around enough, it can

it can fit the spiral and get a high accuracy.

it can fit the spiral and get a high accuracy.

when i look at those

that that image that the relu version actually understands that it is a spiral, right?

and

when you represent it as a spiral, it actually extrapolates correctly

because the spiral just keeps going out.

> > you're touching on something fascinating there because,

you know,

you know,

adaptive computation.

um

i'm really inspired by randall bisreerero's spline theory of of neural networks

and we we've had them on many times

and you can look on the tensorflow playground.

you can look what happens when you have a relu network on on this, you know, spiral manifold.

and, you know, you'd be forgiven for thinking that these things are basically a locality sensitive hashing table, right?

because they they do

because they they do

because they they do

because they they do

they partition the space and and they

they can predict the spiral

manifold, right? but we want to do something a little bit more different than that.

and it also comes into this imposttor thing

because just tracing the spiral manifold but not continuing the pattern

there's a big difference between that.

so from an imposttor perspective

just just tracing the pattern is not learning it abstractly or constructively. right? if we learned it constructively

so we

you know

you speak about this in your paper

this complexification the abstract building blocks and you can do adaptive computation. you understand the spiral.

that means that with adaptive computation, you can continue the spiral and then you can update the model's weights

so it has adaptivity

because that's so important for intelligence.

so we know that we need models that can do these things. but for some reason they're

they're so sick of fantic

they're almost better than an adaptive intelligent system because they tell us exactly what we want to hear.

they seem so intelligent, but we know that they're missing these fundamental properties.

> > i'm still fairly skeptical when i see video generation models.

you know, we went through a phase where you could detect them

because of the number of fingers on somebody's hand, right?

and yes, with more data, with more compute, with better training tricks,

okay, they submit.

and now they usually do have five fingers.

and now they usually do have five fingers.

or did we just use more brute force to just you know

force the the neural network to know

it's five fingers

where something that actually had a much better kind of representation space.

it's almost mad that it's controversial to say that we should represent a spiral

like a spiral. but, you know,

something that could do that

generally

generally

if if it represented a human hand the way that, you know,

maybe i represent a human hand, then maybe it would be much easier to count how many fingers are on a on a hand.

it's unfortunate that they work so well.

it's unfortunate that scaling works so well

because it's too easy for people to just sweep these problems under the carpet.

you guys have possibly created what i think might be the best paper of of the year.

this could actually be the innovation which takes us to the next step.

and you did you get the spotlight in europe as well? > > yeah.

> > this year and congratulations on that.

so i think that's testament to how amazing this paper is. > >

the ctm

the ctm

it's actually not that far out outside of the local minimum that we're stuck in.

right? it's not as if we went and found this completely new technology. right? we took quite a um

a simple biologically inspired idea, right, of these of of the fact that neurons synchronize

and not even necessarily in a biologically plausible way, right? brains don't literally have all their neurons wired together in a way

that they work out their synchronization.

but it's it's the sort of research that i want to encourage people to do.

and the way to sell it is quite easy.

i think at no point did we have to worry about being scooped, right?

that stress was taken away from us completely.

so, and there was

so there was no pressure to sort of rush out with this with this idea

because we're like, well, there's probably somebody else working on exactly this.

and i think the reason that we, you know, we were able to get a spotlight is

because we're able to create such a polished paper.

we took the time to do the science properly to get the the base

the baselines that we wanted and do all the the the the tasks that we wanted to try.

encouraging researchers to take a little bit more of a of a risk, right? to try these slightly more speculative long-term ideas, i think

is

is

i don't think it's necessarily a very difficult thing to sell.

and i want to have the ctm as like a poster child of it works,

right? it was a bit of a risk.

we, you know, we didn't know if we were going to find something interesting, but you know, it was our first shot

and we did find something interesting and it became a a successful paper.

if

if we do find a system which can acquire knowledge, design new architectures, do the the open-ended type of science

that you're speaking to, can you see a future

where at some point the locus of progress will be mostly driven

by the models themselves? > > i think so.

whether or not that's going to replace us completely, i go back and forth on. powerful algorithms are finding

uh

uh

right? and i think it might just end up being a more powerful version of that.

right? so i i know the the ai scientist

that we we released, we showed

that you could actually go end to end, right? go from seeding the system with an idea for a research paper

and then just take your hands off and just let it go.

think about the idea, write the code, run the code, collect the results, and write the paper. uh

to the point that we were actually able to get it to

um

a 100 % ai generated paper accepted to to a workshop recently, right? but i think we did

that to show that you could do it right as a sort of demonstration in a real system.

i think i would want it to be much more interactive, right? i would want to be able to seed with an idea

and then have it come back with more ideas, have a discussion with me, then go away to write the code.

i want look at the code and check it and then discuss the results as they're coming out.

so that's the sort of nearterm future that i that i would envision

or how i would like to do research with an ai.

> > and could you introspect on that? is it

because you feel we need supervision because the models don't yet understand?

you know there's this path dependence idea. so we need to do supervision because we have the path dependence

so we can guide the generation of the language models.

maybe in the future the language models will just understand better themselves. but there's also the output dimension

which is that we want to produce artifacts that extend the fogyny of human interest.

we want it to be human relevant.

> > yeah.

> > yeah.

> > yeah.

in that initial seed idea

it's probably impossible to actually describe exactly what you want. it's exactly the same with, you know,

when i have an intern. i can't just have an intern come into the company and i go,

i have this mad idea

and then just explain it to them and then just leave them alone for 4 months.

there's a back and forth

because i have a particular idea that i want to explore

and i need to keep steering them in the direction that i i

you know that i had in my my mind originally.

so i think it's more like that

basically.

you have such a deep understanding. so you have this rich provenence and history and path dependence

and that means you can take creative steps

intuitive steps for you

intuitive steps for you

they respect all of this deep abstract understanding that you have

and interns don't yet have that

> > but maybe ai models in the future will have that. > > yeah

sure.

sure.

if they get to the point where my inputs becomes detrimental

then yeah

then yeah

it's kind of like chess, right? there was a point at which chess engine

and human fusion actually beat chess engines.

that's not that's not true anymore, right? adding a human into the mix actually makes the the bots worse.

> > oh, interesting.

i wasn't aware of that. > > yeah.

i wasn't aware of that. > > yeah.

when that day comes for ai scientists is a is a is a broader discussion.

i think

> > i think now is a good segue to talk about this paper in a little bit more detail.

so this continuous thought machines you were just pointing to it before. luke

first

first

first

first

introduce yourself > > and set this thing up for us. > > my name is luke.

i am a research scientist at sakana ai and

uh

my primary sector of research is this continuous thought machines.

it's took us somewhere in the region of about eight months working on this project with uh

the whole team. um

the whole team. um

i did a lot of the work uh

but we also had a lot of people in different areas and doing different parts of it that

i think an 8-month life cycle for a paper seems a bit long for ai research at the moment.

um

um

to the actual technical points of the paper.

so we call it continuous thought machines.

it originally had a different name. we called it asynchronous thought machines before

but

uh

every single time people asked us what's the asynchronous part

it became a bit confusing. so continuous thought machines basically depends on three novelties.

uh

the first one is having what we call a internal thought dimension

# Chapter 3

i am a research scientist at sakana ai and

uh

my primary sector of research is this continuous thought machines.

it's took us somewhere in the region of about eight months working on this project with uh

the whole team. um

the whole team. um

i did a lot of the work uh

but we also had a lot of people in different areas and doing different parts of it that

i think an 8-month life cycle for a paper seems a bit long for ai research at the moment.

um

um

to the actual technical points of the paper.

so we call it continuous thought machines.

it originally had a different name. we called it asynchronous thought machines before

but

uh

every single time people asked us what's the asynchronous part

it became a bit confusing. so continuous thought machines basically depends on three novelties.

uh

the first one is having what we call a internal thought dimension

and this is not necessarily something new. it's related conceptually to the ideas of latent reasoning. uh

and it's essentially applying compute in a sequential dimension.

and when you start thinking about ideas and problems

and when you start thinking about ideas and problems

in this domain and in in this framework, you start understanding that many problems that look like intell

or solutions to problems that look intelligent

are often solutions that have a sequential nature.

so for instance,

one of the primary tasks that we tested in the continuous thought machines was this maze solving task.

and solving mazes for deep learning is is quite trivial.

it's really easy to do if you make the task easy for machines.

and one of the ways to do this is you give an image of a maze to a neural network

like a convolutional neural network and it outputs a image

uh

same size of the maze

and it's uh

and it's uh

and there's ones where there is a path.

there's some really brilliant work showing how you can train these in a careful way

and scale them up essentially indefinitely.

and this is fascinating

and

and

and

however, when you take that uh approach out of the picture and you ask what is a more human

way to solve this problem, it becomes a sequential problem. you have to say

well

go up, go right, go up, go left, whatever the case may be

to trace a route from start to finish.

and when you constrain that simple problem space

uh

and you you ask a machine learning system to solve it like that

turns out to actually get much much more challenging.

so this became our hello world problem for the ctm

and applying an internal sequential thought dimension to this is how we went about solving this.

uh

two other novelties that we can touch on and talk about.

two other novelties that we can touch on and talk about.

two other novelties that we can touch on and talk about.

we sort of rethought the idea of what neurons should be.

there is a lot of excellent research in this world

uh

uh

particularly exploring how neurons work in biological systems.

and then we get on the other side of the scale how deep learning neurons work

which the quintessential example is a relu.

it's off or on in a sense.

it's off or on in a sense.

very high level abstraction of neurons in the brains feels a little bit myopic.

so we approached this problem and said well

let's let's on a neuron by neuron basis

let this neuron be a little model itself.

and this ended up doing a lot of interesting work on how to build dynamics in the system.

the third novelty here is

the third novelty here is

we have this internal dimension over which thinking happens. we ask the question, well, what is the representation?

what is the representation for a biological system when it's thinking?

is it just the state of the neurons at any given time? does

that capture a thought, if you wish,

if i can be controversial and use the term thinking and thought

and my philosophy with this is no,

it doesn't. that the concept of a thought is something that exists over time.

so, how do we capture that in in engineering speak?

we

instead of measuring the states of the model that is recurrent,

we measure how it synchronizes how neurons synchronize in pairs along with other neurons.

and this opens up the door to a huge array of things

that we can do with this type of representation.

> > you were talking about this um sort of sequential nature of of reasoning and devil's advocate.

i mean there was that anthropic biology paper

and they were talking about planning and thinking and and they they were

they were saying that this thing is planning ahead

because because i think your system

because because i think your system

we can say

does planning it

does planning it

can you explain that > >

yes

i think the boundary in terms of computation from a a cheering machine perspective

if you wish

if you wish

is really interesting because the notion of being able to write your tape

uh

read from a tape and then write again to be in a ting compute system

ting

complete system is

uh

uh

and i think the primary difference with let's talk about transformers versus what we're trying to do with the ctm is

that the process that the ctm thinks in

we can apply that process that internal process to

we can apply that process that internal process to

breaking down a problem.

so the problem itself can be a single

there is a single solution to this problem

and you could do that in one shot. you could

and you could do that in one shot. you could

with the maze

you could just process that in one shot

but there are certain phrasings of problems that are real problems

that doing so becomes exponentially more challenging.

so in the maze task, a really good example is that if you try to predict 100

200 steps down the path in one shot,

no models that we could train,

not even our model could do that.

and we needed to actually build an autocurriculum system where the model first predicted the first step and then

when it could predict the first step,

then it

we started training it on the second and third and fourth step.

and the sort of resultant behavior of this is where it gets interesting.

one of the one of the ways that i like to do research

and

that i encourage people who work with me to do research is understand the if you wish the behavior of a model.

we're getting to a point now

where the models that we build are demonstrably intelligent in ways that keep surprising us

and breaking that down into a single set of metrics

or even a finite single metric about performance

seems maybe not to be the right way to do it for me.

and understanding the behavior and the actions that those models take

when you put them in a system and train them in a certain way

uh

seems to reveal more about what's actually going on under the hood. > > very cool.

and i think i didn't pick up on this. so so you're

you're doing a fixed number of um steps

so you have like a a context window

and did you say that you've set that around 100 steps?

> > so for the

for the maze task

for the maze task

the model always observes the full image at every step.

uh

uh

uh

uh

uh

those images could be tokens from a language

uh

the output of a language model

those

those

those

whatever the case may be

it should be agnostic to data

it should be agnostic to data

but in the maze task

the model can continuously just observe the data

the model can continuously just observe the data

no matter where it can look at the whole image simultaneously

but it uses attention to retrieve information from the data

and it has

let's call it 100 steps that it can think through. and what we do is we pick up

at some point

the model solves three steps through the maze.

so it says i'm going to go up, up, and right. and then it's correct.

but then it makes the wrong turn.

and at that point, we stop supervision.

we only train it to solve the fourth step.

so one more than what it could. in practice, we do it five,

but the principle holds.

and when you do that, it's a self bootstrapping mechanism.

and i think the uh intuitive listener will understand how that extends to other domains, other sequential domains

for instance

like uh language prediction, many tokens ahead, that sort of thing.

> > so i'm really interested in this idea of adaptive computation.

so i i guess

the first question is how sensitive was the performance to the number of steps

and then the next question would be

could you have an arbitrary number of steps

which means that you know

perhaps based on uncertainty

or you know some kind of criterion

or you know some kind of criterion

and then the final question is

could you have potentially like an arbitrary or unbounded number of steps

>

>

>

>

>

i think that i think that i'll answer the uncertainty question first about the sensitivity to steps.

so a very good example of this is we just trained the model on imageet classification

and our last function is quite simple.

what we do is we run it for for example

what we do is we run it for for example

and we pick up two points

two distinct points. the first one is

where is it performing the best

i. e. where is the loss

i. e. where is the loss

i. e. where is the loss

where is it most sure

or where is it most certain

or where is it most certain

or where is it most certain

between 0 and 49

inclusive

inclusive

we just make the last the average of the cross entropy at those points.

so what this does is it induces a behavior

where easy examples are solved almost immediately in one or two steps

whereas more challenging examples will naturally take more thinking

and it enables the model to use the full breadth of time

that it has available to it just in a natural fashion without having to force it to happen.

so you've decided to model every neuron as an mlp

which is really fascinating.

talk about that

talk about that

and i think you use the inner product to determine the extent to which the parameters are are synchronized

and this kind of unfills over over time

as as the driving force. can you explain that in a bit more detail? > > absolutely.

i think it's a it's a good point to explain the uh neuron level models as we call them in the paper

or nlm first

or nlm first

so you can imagine a recurrent system is a state vector, a state vector

that is being updated from step to step.

we track that state vector and that state vector unfolds

and for each individual neuron, each uh i neuron in the system, we have a unfolding time series.

it's a continuous time series. well, it's discreet,

but it's a continuous value.

and those time series define what we call the activations over time.

and synchronization is quite simply just measuring the dotproduct between two of these time series.

so you have a system of d neurons

and essentially you have d over two squared different synchronization pairs.

so neuron one can be related to neuron 2 by how they synchronize

and neuron

and neuron

and neuron

and neuron

the neuron level models

they function by taking in a finite history

like a foq of neuron of activations coming in

and instead of being just a radio activation

they use that history as information to uh

process a single activation out

and that is what moves from what we call pre-activations to post activations.

and the principle here is that this might seem rather arbitrary and does it help for performance?

turns out it does, but that's not really the catch all solution here. that's not what we're after. uh

what we're after here is trying to do something biologically plausible. uh

find the line somewhere between biology, which is how the brain implements things in the biological substrate

that we have

versus deep learning, which is highly parallelizable, super fast to learn, back propanable,

all of the nice properties of that that have got us this far.

and find a line somewhere

where we can take some sprinkling of biological inspiration but still train it with deep learning.

and it turns out that neuron level models is a nice interim that we can do this with.

the concept of synchronization is applied on top of the outputs of those neuron level models.

so on on this

on the scaling

on the scaling

i think the time complexity is quadratic in respect of the dimension of the synchronization matrix

right

and in your paper

you were talking about subsampling to improve the performance

but how how did that affect the

the stability and the you know

like were there any things that that cost you doing that? yeah, it's a neat question.

i think in terms of stability,

what's what we found was kind of fun

what's what we found was kind of fun

that we had throughout the the experiments that we ran with this paper was it tended

no matter what we tried it on it

it just kind of worked with all spreads of hyperparameters. uh

and this

the problems that you have with back prop through time

typically with recurrence models

typically with recurrence models

and lstms it's a challenge

and you run for many internal ticks with the rnns or the lstms and the learning seems to break

down

down

that we use synchronization in some sense touches all of the neurons through all of the time

so it really helps with gradient propagation

so it really helps with gradient propagation

so it really helps with gradient propagation

that's maybe a bit oblique to what you asked about synchronization

is we have a system of d neurons

and like i said earlier there d over two squared possible combinations.

this essentially means that our underlying state

or underlying representation to the system is quite a lot larger

than what you would get with just taking those d neurons.

and as to what that means in terms of downstream computation

and performance and the things that we can do with this is what we're actively exploring right now.

> > you guys used an exponential decay rate.

> > you have the system that unfolds over time.

it would be maybe a little bit too constrained if the synchronization between any two neurons depended on the same time scale.

so for instance,

there are neurons in your brain that are firing over very long time scales and very short time scales.

the way that they fire together impacts other neurons and causes those neurons to fire.

but everything in biological brains happens at diverse time scales. it's why we have uh

different brain waves for different thinking states

different brain waves for different thinking states

different brain waves for different thinking states

but beside

that point, what we do with the exponential decay in the continuous thought machines is it allows us for a very sharp decay to say

that these two neurons that are pairing together,

what only really matters is how they fire together right now.

right?

right?

right?

that's capturing a global sense of how those neurons are firing over an extremely long period of time.

so this was essentially a way of us

so this was essentially a way of us

capturing this idea of how different neurons could maybe fire together very quickly

and other neurons can fire together very slowly or not at all.

and this lets

that representation space that i spoke about that d over2 squ representation space lets it again become more rich

and we can enrich that space with more subtle tweaks to how we compute those representations.

so we were speaking about this yesterday, luke, that um

when folks apply transformers to things like the arc challenge or things that need reasoning.

um

um

so the architects who were the winners of last year's challenge, they did um depth first search sampling

and some folks have been experimenting with using language representations

or you know

or you know

and some part of this is to do with the the

the reachability um

the reachability um

the reachability um

the reachability um

which means you can kind of monotonically

um increase

but if i understand correctly

your system might have some interesting properties for reasoning

and for discrete and sparse domains and also for sample efficiency

because we want

we want to build a system that can actually do well on things like the arc challenge.

but can you kind of explain in simple terms why you think this architecture could be significantly better

than transformers for doing those things? > >

i think a lot of the really fascinating work in the last few years

that i found fascinating in the literature of language models has been related to what one can actually call a new scaling dimension.

i in some sense see continue

i in some sense see continue

chain of thought reasoning as a way of adding more compute to a system.

# Chapter 4

or you know

and some part of this is to do with the the

the reachability um

the reachability um

the reachability um

the reachability um

which means you can kind of monotonically

um increase

but if i understand correctly

your system might have some interesting properties for reasoning

and for discrete and sparse domains and also for sample efficiency

because we want

we want to build a system that can actually do well on things like the arc challenge.

but can you kind of explain in simple terms why you think this architecture could be significantly better

than transformers for doing those things? > >

i think a lot of the really fascinating work in the last few years

that i found fascinating in the literature of language models has been related to what one can actually call a new scaling dimension.

i in some sense see continue

i in some sense see continue

chain of thought reasoning as a way of adding more compute to a system.

that's obviously just one small part of what that really is and what that really means.

but i think it's quite a profound breakthrough

uh

uh

uh

that reasoning component be entirely internal yet still running in some sort of sequential manner.

and i think that that's rather important.

and you spoke earlier about gemini's diffusion language modeling

and i think that there are a lot of different directions that are exploring this right now. uh

i do think that the continuous thought machine with the ideas of synchronization

and multi-hierarchical temporal representations gives a certain flexibility on that space that

uh

uh

and that richness of that space

being able to project the next step to solve the arc challenge

and the next 100

the next 200 steps to be able to break that down into a process that a model can

then

then

then

that process in its highdimensional latent case becomes something that feels like a good approach to take.

> >

do you see any relationship between this architecture and you know alex graves neuro touring machine?

>

>

>

>

>

i think that the one of the the most challenging parts about uh

working with a neural neural touring machine is the concept of writing to memory and reading to memory

because it is a discrete action.

um

um

and yes

uh

i wouldn't go so far as to say that the continuous thought machine is definitively nearing tur

incomplete

but the notion of the notion of doing reasoning in a space that is uh latent

and letting that space unfold in a way that is uh

rich towards a different set of tasks.

and this this actually brings me to a point that i find quite interesting

um

that i'd like to share with you.

consider again the imageet task or any sort of uh classification task. it's

it's a nice test bed.

there are many images that are really easy and there are many images that are really difficult.

when we train for instance

a vit or a cnn

uh

to do this task, it has to nest all of that reasoning in the same space.

it has to put all of its decision-m process for a very simple obvious cat versus some complex weird underrepresented class in

that system in that data set

and it has to nest it all in parallel in a way that is

we get to the last layer and then we classify.

um

um

breaking that down where you have different points in time

where you can say

where you can say

where you can say

versus now i'm done

i can stop

i can stop

and actually naturally segment it into its easy to difficult components.

and i think we know that curriculum learning

and learning in this continuous sense again seems to be a good idea.

it's it's how humans learn.

and if we can get at that architecturally

and just have that fall out in a model, again, this seems like a something worth exploring.

uh

i'm not sure if you know much about model calibration and how neural networks tend to be poorly calibrated.

> > oh, go for it, tommy.

um

um

it's a bit of an old finding, but if you train a neural network for long enough

and it fits really really well and you've regularized it

regularized it really really well,

you'll find that the model is unccalibrated, which essentially means that it is very certain

uh

about some components

where some classes where it's wrong and uncertain for some classes where it's correct.

essentially what you want for a perfectly calibrated model is if it predicts a uh probability

that this is in class

the correct class with 50

%.

%.

%.

and so forth.

so a well-c calibrated model

if it's predicting a probability of 0. 9 that it is a cat

then 90 % of the time it should be correct.

and it's actually turns out that most models that you train for long enough get poorly calibrated.

and there are loads of post hawk tricks

and there are loads of post hawk tricks

to fixing this. we measured the calibration of the ctm after training and it was nearly perfectly calibrated

which is again a little bit of a smoking gun

that this actually seems to be probably a better way to do things.

the flavor of this kind of research is such that we didn't actually go out

and actually try to create a very well-c calibrated model, right?

and we didn't even try to create a model

that was necessarily going to be able to do some kind of adaptive computation time, right? um

i was

i was

i was

i was

i was

i was

adapted computation

time

time

time

time

it had a massive amount of hyperparameter sweeps in it

because in that paper he needed to have a loss on the amount of computation that was being done.

> > because anytime you try to do some sort of adaptive computation time research,

what you're fighting is the fact that neural networks are greedy, right?

because obviously the way to get the lowest loss is to use all the computation

that you have access to.

so unless you had like an extra loss that had a penalty that said

okay

okay

you're not allowed to use all the computation that's and and very very carefully balance loss

that's

when you actually got the interesting dynamic computation time behavior falling out of the the model in that paper.

but was really gratifying to see with the the continuous thought machine is that

because of the way that we set up the loss that luke described earlier,

adaptive computation times seem to just fall out naturally.

so that's more the way that i think research should go. > > okay?

because we we don't actually have like a specific goal

um

um

or a specific problem we're trying to fix like that or something we're trying to invent.

it's more that we have this interesting architecture and that we're just following the gradients of interestingness.

> > yes.

> > yes.

that point, i i think maybe the most exciting thing about your paper is, you know, we were talking about path dependence

and um

and um

which is built step by step, this process of complexification

and u

and u

this is um apppropo in in the theme of world models in in general

and also active inference

and i say active inference in big quotes

because it's not kl friston's active

you know

maybe adaptive inference or something like that but we want to build agents that can continue to learn

that can update their parameters

and most importantly can construct path dependent understanding

and because it that's completely different to just understanding what the thing is.

it's how you got there is very important

and this architecture potentially allows these agents using this algorithm to explore trajectories in spaces

find the best trajectories and actually construct an understanding which carves the world up by the joints.

yeah, that's a

that's a really neat perspective. i haven't actually thought about it like that, but yes, i think

um

that particular stance becomes really interesting when you think about ambiguous problems

because carving the world up in one way is as performant as carving it up in another way.

> > yeah.

> > yeah.

> > yeah.

perhaps the hallucination in language models is carving the world up in some fine way

but it's just not performance

in our measure of this is hallucination

and actually that's not true

but in some other

trace down the path of wanting to carve the world up through a auto

reggressive

reggressive

you end up in a different carve up of that world

and being able to train a model

that can be implicitly aware of the fact

that it is actually carving up the world in a different way

and and explore those manners, those

and and explore those manners, those

descents down the carve up is something that we're after

and i think it's quite an exciting approach to be trying to take a stance of

let's

let's break up this problem into small solvable parts and learn to do it like that

and how can we do this in a natural way without too many hacks.

yeah, it's something i've been thinking about

because um shalet

because um shalet

um ideas is for him adapting to novelty is getting the right answer

and the reason why you gave that answer is very

very important

very important

we have this problem that we

we come up with this kind of cost function that rather leads to this shortcut problem

but you know we could just build a symbolic system

we could be gi and and we could say

we could be gi and and we could say

we need do this um principled kind of construction of knowledge

maintaining semantics.

well, we're not doing that.

we're doing a hybrid system. but there must be some natural way of doing reasoning

where

in spite of the end objective being this cost function

that

because of the way that we traversed these open-ended spaces that we can actually have more confidence

mechanistically

that we're doing reasoning

which is aligned to the world.

i think that's a great way of seeing this particular uh avenue of research

and i think that obviously we're not the only people thinking like this

and we're not the only ones trying to do this.

um

um

and surprisingly

so it wasn't

so it wasn't

so it wasn't

it's not the goal to to do this type of research.

it's not the goal to be able to break the world down into these small uh chunks

that we can actually reason over in in a way that seems natural.

instead, what we did was pay respect to the brain, pay respect to nature and say, well,

if we build these inspired things, what what actually happens? what

what different ways of approaching a problem emerge?

and then when those different ways of approaching a problem emerge, what big philosophical and

uh

intelligence-based questions can we then start to ask? and that's where we're at right now.

so it might feel at times, especially for me, uh

too many questions and too few hands to answer those questions.

but i think the fun and exciting thing and the encouraging thing that i i can

you know

try to encourage other younger researchers out there is that

uh

uh

do what you're passion passionate about

and figure out how to build the things that you care about and then see what that does.

see what doors that opens up and see how to explore deeper into those domains.

> > we were talking about this yesterday, weren't we?

that you can think of language as being a kind of maze.

> > yes.

like what is to stop us from taking this architecture and building the next generation language model with it.

i mean that that's honestly

i mean that that's honestly

something that i am actively trying to explore right now

and uh

and uh

i think the maze

the maze task gets really interesting

when you add ambiguity to it when there are many ways to solve the maze

and honestly

this isn't something i've tried yet

and maybe it's something i should try next week

but it's essentially you can imagine an agent or the ctm

in this case

observing the maze and taking a trajectory

and surprisingly we saw this

we have a section in our recently updated paper on ar archive

the final camera ready version of this paper

where we added an extra supplementary section that is not in the main technical report

and that supplementary section is basically hey we saw this cool stuff happen

and we list

i think 14 different interesting things that happened while we were doing the research

um

that obviously didn't make it into the paper

but we wanted people to know about these strange things that happened

and this is one of the strange things where

and this is one of the strange things where

we watched during training

what was happening.

and at some time during training, maybe halfway through the training run, we could see what the model would do is it would start going one path in the maze

and then suddenly it would realize, oh no,

damn,

i'm wrong. and would backtrack and then take another path. but eventually it gets really good

and it does you some sort of distributed learning in this

because it's got a attention mechanism with multiple heads.

so it can actually just figure out how to do this pretty well and refine its solution.

but sometime early on in the the learning it descends multiple paths and comes back and backtracks.

we have a really fascinating set of experiments that also showed

and this

and this

we actually have some supplementary material online showing this where

uh

and i don't really know what this says. it's kind of a deep philosophical thing

but if you're trying to solve a maze

but you don't have enough time. turns out that there's a there's a foster algorithm to do it.

and this was

this blew my mind when i saw it.

so if we constrain the amount of thinking time that the model has

but still get it to try solve a long maze

instead of tracing out that maze,

what it does is it quickly jumps ahead to approximately

where it needs to be and it traces backwards and it fills in that path backwards

and then it jumps forward again leaprogs over the top and traces that section backwards and then leap frogs

and it does this fascinating leaprogging behavior that is based on the constraint of the system. and again,

you know,

this is just an observation we made

and what that means

and what that means

and what that means

and what that means

giving a model time to think versus not

and is it enough time to think?

and is it enough time to think?

what different algorithms does the model learn

when you constrain it in this way? i find that quite fascinating and an interesting thing to explore.

does it tell us something about how humans think? does it tell us something about how how we think under constrained settings versus open-ended settings? there's a number of cool questions you can ask on this front.

> > you

you guys are both huge fans of um

you guys are both huge fans of um

population methods and collective intelligence

and because we can

we can scale this thing up and we can scale it out

and what would it mean to scale this thing out not only just in a kind of um

what do they call it trivial paralization but in terms of having some kind of weight sharing between parallel models

and so on.

and so on.

what

what would

what would

what would that give you potentially? > >

uh

uh

uh

so one of the active things that we're trying to explore in our team is

uh

uh

long-term memory

and what what does this mean for a system like this? so an experiment that one can construct

for instance

is to put some agents in a maze and let them try

solve this maze

solve this maze

but in a very constrained setting where a agent can only see maybe a 5x5 region around it

and we give that agent some mechanism for saving and retrieving memories

and the task if you wish is to solve that maze

find your way to the end

and the model needs to learn how to construct memory such that it can get back to a point

# Chapter 5

what would

what would

what would that give you potentially? > >

uh

uh

uh

so one of the active things that we're trying to explore in our team is

uh

uh

long-term memory

and what what does this mean for a system like this? so an experiment that one can construct

for instance

is to put some agents in a maze and let them try

solve this maze

solve this maze

but in a very constrained setting where a agent can only see maybe a 5x5 region around it

and we give that agent some mechanism for saving and retrieving memories

and the task if you wish is to solve that maze

find your way to the end

and the model needs to learn how to construct memory such that it can get back to a point

where it's seen before

and know i did the wrong thing last time

and go a different route and you can then see this with uh

parallel agents in the same maze with a shared memory structure and see what actually happens

when you can all access that memory structure and have a shared global like

almost like a cultural memory that we can access and solve this global task

by having many agents trying to use this memory system

and i do think

that memory is going to be a very key element to what we need to do in the future for ai in general.

> > so the subject of uh reasoning came up just a second ago

and i think there's a perception that recently we made a lot of progress in reasoning right

because it's actually one of the main things that i think people are are working on.

we released a data set recently called uh sudoku bench

and i was actually quite happy to see it come up organically on your uh podcast a few weeks ago.

> > chris moore, > > right? > > yes.

so, i i wanted to tell you a little bit about this benchmark

because i think i've been having a little bit of issue promoting it

because it doesn't on the surface sound particularly interesting

because sudoku has a sort of a feeling

that it's already been solved, right? so, how interesting can a collection of of sudokus be for reasoning?

exactly. we're not talking about normal sedokus.

we're talking about variant sodokas.

and what variant sodokas are are usually normal sedokus,

right? so put the numbers one to nine in the row, the column,

and the box, but then literally any additional rules on top of that.

and they're all handcrafted.

they all have extremely different constraints. um constraints that actually require very strong natural language understanding.

so for example, there's one puzzle in the data set

where it tells you the constraints of the puzzle in natural language and then says, " oh,

by the way,

by the way,

" right? so you have to be able to meta reason about the rules themselves even before you start

uh

solving the puzzle. there are other puzzles where you have um

a maze overlaid on the sodoku

and the rat has to work out a way through the maze by following

uh

a path to the cheese.

but then there are constraints on the path that it takes of like what numbers

and what they can be add up to.

and what they can be add up to.

it's difficult to really describe how varied these these

uh

uh

and i think they're so varied that if anyone was actually be able to beat our benchmark

they would necessarily have to have created an extremely powerful reasoning system. right now, the best models um

get around 15 %, but they're only the very

very simplest and the very

very simplest and the very

very simplest and the very

um

we're going to be putting out a blog post about um gpt5's performance and it is a jump

but it's still completely unable to solve puzzles

but it's still completely unable to solve puzzles

you know

humans can can solve. and what i really like about this data

uh

data set

data set

and actually was the catalyst for me creating it in the first place

it was that there was a

it was that there was a

it was that there was a

it was that there was a

so we have all this data

it's from the internet

um

but what you really want

but what you really want

but what you really want

you wouldn't want all of the text that humans have ever created

you would actually want the thought traces in their head as they were creating the text, right? if you could actually learn from

that, then you would get something really powerful.

and i thought to myself, well, that data must exist somewhere. my first thought was maybe philosophy like

uh

uh

uh

there's a type of philosophy where you just write down your thoughts without thinking like just stream of consciousness.

i thought maybe that could work.

um,

but then when i wasn't thinking about it and i was, you know,

in my leisure time, i was watching a youtube channel called cracking the cryptic. > > yes.

> > where these

uh

these two british gentlemen will solve these extremely difficult sudoku puzzles for you. right.

sometimes their

their videos are four hours long and they they're professionals

like this is their job. and what was perfect

i realized is they tell you in agonizing detail

exactly what reasoning they used to solve those particular puzzles.

right? so we

with their permission took all of their videos which represents thousands of hours of very high quality human reasoning

like thought traces and scraped them and made that available for imitation learning.

right? um

right? um

right? um

that i did a little bit too much of a good job of really creating a very difficult benchmark.

right. so, we're still trying to get that stuff working and we'll publish it that if we

if we have some success. um, yeah,

i want to

i want to

that this this reasoning benchmark really is different, right? not only do you get something

that's super grounded, like you know exactly if it's right

or wrong,

so you can do rl to your heart's consent, but you can't generalize very easily.

each puzzle is deliberately designed

by hand to have a new and unique twist on the rules called a breakin

that you have to understand.

and right now, despite all the progress we've made, the current ai models can't take that leap.

they can't find these breakins, right? they'll fall back to, okay, i'll try

no,

i'll try five, i'll try six, i'll try seven, right? the

the reasoning becomes really boring and nothing like what you see in the transcripts that we've

we've open sourced from this from this youtube channel.

so i just want to put the challenge out there right that this

this is a a really difficult benchmark

and i think progress on this benchmark will really mean progress in ai generally.

> > could you reflect a bit so

after watching this um

cracking the cryptic youtube channel? how diverse were the patterns? because um

chris was saying to me, oh

chris was saying to me, oh

they go on discord

servers, they get these creative crazy ideas and i'm i'm obsessed. maybe it

maybe i'm just being idealistic, but i love this idea of there being a deductive closure of knowledge, right?

that that there's this big tree of of reasoning

and we're all in possession of different parts of the tree to different depths.

so the smarter and the more knowledgeable you are, the deeper down the tree you go.

but in this idealized form, there is one tree and all knowledge kind of, you know,

originates or emanates from these abstract principles.

and we could in principle build reasoning engines that could just reason from first principles and it might be

um

um

so so you have to perform all of the steps.

and it feels like because we're not in possession of the full tree.

what we need to do is kind of fish around. we fish around to find lego blocks.

oh, that's a good lego block.

i can apply that to this problem.

and maybe

that's just what we need to do in ai for the time being is is is we need to just acquire as much of the tree as possible.

but could

could we just do it all the way down? > > yeah, fascinating question.

that tree is probably massive, right? > >

and as a human is solving these puzzles, they're definitely learning in real time

and discovering new parts of this tree.

and it's it's sort of a meta task, right? because it's not just reasoning, you're reasoning about the reasoning.

and i don't think we can.

we have that in ai right now.

because if you watch the videos, they'll say something like, " okay, this looks like a parask

or this is a set theoretic problem

or, you know,

or, you know,

i should get my path tool out and trace this this around.

"

"

"

this already massive collection of reasoning

lego blocks

as you say in their head. so they'll recognize

okay

okay

it's actually fascinating to watch how good they are at

just intuitively knowing where you know

someone like me haven't solved as many needs

to spend a lot of time looking around like

okay

okay

or maybe i try this one. um,

but even they're not perfect.

so, you can watch them take a certain kind of reasoning and start building up.

okay, maybe we should solve it like this and then go and know that doesn't disambiguate it enough

and then backtrack and then go down another path.

again, something that we do not see current ai doing when they're trying to solve

uh

uh

the tree is very big

and i guess the phoggenetic distance between many of these motifs in in the tree is just so large.

so it's so difficult to jump between and and and i

and i think that's why as a collective intelligence

we work so well together

because we actually find ways to jump to different parts of the tree, > > right?

and i and i think that's probably why the rl

the

the current state of the rl algorithms that we're trying to apply to this just isn't working

because in order to learn how to get these breakthroughs to to understand what the sort of nuance reasoning is to get these puzzles, you have to sample them.

and that it's

it's such a rare space, you know,

it's

it's such an specific kind of reasoning that's required to get to the

the specific breakthrough that this kind of technique doesn't work, right?

and there's definitely a feeling in the community like, okay, this is how you just solve things now.

like we have rl,

yes,

we can get these language models to do what we want.

it doesn't work for this for this data set. > > guys,

it's been an absolute honor having you on the show.

just before we go, are you hiring? because we've got a

we've got a great audience of ml engineers and scientists

and um

i think working for zakano would be the dream job.

> > that's very kind of you. yes,

we are definitely hiring

and as i said earlier in this interview, i honestly want to give people as much research freedom as possible.

i'm willing to make that bet, right? i think things that are very interesting will come out of this.

and i think we've already seen plenty of interesting things coming out of this.

so if you want to work on what you think is interesting and important, come to japan.

> > and japan just happens to be the most civilized culture in the world.

> > all right. > > it might be the opportunity of a lifetime, folks.

so um yeah, get in touch, guys.

seriously, thank you so much.

it's been an honor having you both on the show.

> > thank you very much. > > thank you so much. it's been great.

