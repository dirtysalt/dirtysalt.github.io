# Chapter 1

The following is a conversation with Ilya Sutskever

co-founder and chief scientist of OpenAI, one of the most cited computer scientists in history with over 165

000 citations, and to me, one of the most brilliant and insightful minds ever in the field of deep learning.

There are very few people in this world who I would rather talk to and brainstorm with about deep learning

intelligence, and life in general than Ilya

on and off the mic.

This was an honor and a pleasure.

This conversation was recorded before the outbreak of the pandemic.

For everyone feeling the medical, psychological, and financial burden of this crisis

I'm sending love your way.

Stay strong.

We're in this together.

We'll beat this thing.

This is the Artificial Intelligence podcast.

If you enjoy it, subscribe on YouTube

review it with five stars on Apple podcast

support on Patreon, or simply connect with me on Twitter @lexfridman

spelled F-R-I-D-M-A-N.

As usual, I'll do a few minutes of ads now

and never any ads in the middle that can break the flow of the conversation.

I hope that works for you and doesn't hurt the listening experience.

This show is presented by Cash App, the number one finance app in the App Store.

When you get it, use code LEXPODCAST.

Cash App lets you send money to friends

buy Bitcoin, invest in the stock market with as little as $1.

Since Cash App allows you to buy Bitcoin

let me mention that cryptocurrency in the context of the history of money is fascinating.

I recommend A Cent of Money as a great book on this history.

Both the book and audiobook are great.

Debits and credits on ledgers started around 30

000 years ago.

The US dollar created over 200 years ago

and Bitcoin, the first decentralized cryptocurrency released just over 10 years ago.

So given that history, cryptocurrency is still very much in its early days of development

but it's still aiming to, and just might

redefine the nature of money.

So again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST

you get $10, and Cash App will also donate $10 to FIRST

an organization that is helping advance robotics and STEM education for young people around the world.

And now here's my conversation with Ilya Sutskever.

You were one of the three authors, with Alex Krizhevsky

Geoff Hinton, of the famed AlexNet paper that is arguably

uh, the paper that marked the big catalytic moment that launched the deep learning revolution.

At that time.

..

Take us back to that time.

What was your intuition about neural networks, about the representational power of neural networks?

And maybe you could mention, how did that evolve over the next few years up to today

over the 10 years?

Yeah, I can answer that question.

At some point, in about 2010 or 2011

I connected two facts in my mind.

Basically, the realization was this.

At some point, we realized that we can train very large.

..

I shouldn't say very.

You know, they were tiny by today's standards

but large and deep neural networks end-to-end with backpropagation.

At some point, different people obtained this result.

I obtained this result.

The first th- the first moment in which I realized that deep neural networks are powerful was when James Martens invented the Hessian-free optimizer in 2010

and he trained a 10-layer neural network end-to-end without pre-training from scratch.

And when that happened, I thought, "This is it.

" Because if you can train a big neural network

a big neural network can represent very complicated function.

Because if you have a neural network with 10 layers

it's as though you allow the human brain to run for some number of milliseconds.

Neuron firings are slow, and so in maybe 100 milliseconds

uh, your neurons only fire 10 times.

So it's also kind of like 10 layers

and in 100 milliseconds, you can perfectly recognize any object.

So I thought.

..

So I already had the idea then that we need to train a very big neural network on lots of supervised data

and then it must succeed because we can find the best neural network.

And then there's also theory that if you have more data than parameters

you won't overfit.

Today, we know that actually this theory is very incomplete and you won't overfit even if you have less data than parameters.

But definitely, if you have more data than parameters

you won't overfit.

So the fact that neural networks were heavily over-parameterized wasn't discouraging to you?

So y- y- you were thinking about the theory that the number of parameters

the fact there's a huge number of parameters is okay?

It's gonna be okay?

I mean, there was some evidence before that it was okay-ish

but the theory was most, the theory was that if you had a big data set and a big neural net

it was going to work.

The over-parameterization just didn't really, um, figure much as

as a problem.

I thought, well, with images, you're just gonna add some data augmentation and it's gonna be okay.

So where was any doubt coming from?

The, the main doubt was, can we train a big ne- will we have enough computer to train a big enough neural net?

With backpropagation.

Backpropagation I thought was, would work.

The thing which wasn't clear would, was whether there would be enough compute to get a very convincing result.

And then at some point, Alex Krizhevsky wrote these insanely fast CUDA kernels for training convolutional neural nets

and that was, bam, let's do this.

Let's get ImageNet, and it's gonna be the greatest thing.

Was your intuition, most of your intuition from empirical results by you and by others?

So, like, just actually demonstrating that a piece of program can train a 10-layer neural network?

Or was there some pen and paper or marker and whiteboard thinking intuition?

Like, 'cause you just connected a 10-layer large neural network to the brain.

So you just mentioned the brain.

So in your intuition about neural networks, does the human brain come into play as a intuition builder?

Definitely.

I mean, you, you know, you gotta be precise with these analogies between neural art- artificial neural networks and the brain.

But.

..

There is no question that the brain is a huge source of intuition and inspiration for deep learning researchers since all the way from Rosenblatt in the '60s.

Like, if you look at- the wh- the whole idea of a neural network is directly inspired by the brain.

You had people like McCollum and Pitts who were saying

"Hey, you got these n- n- neurons in the brain.

And hey, we recently learned about the computer and automata.

Can we use some ideas from the computer and automata to design some kind of computational object that's going to be simple

computational, and kind of like the brain?

" And they invented the neuron.

So, they were inspired by it back then.

Then you had the convolutional neural network from Fukushima

and then later Yann LeCun, who said

"Hey, if you limit the receptive fields of a neural network

it's going to be especially suitable for images

" as it turned out to be true.

So, there was- there was a very small number of examples where analogies to the brain were successful

and I thought, "Well, probably an artificial neuron is not that different from the brain if you squint hard enough.

So, let's just assume it is and r- and roll with it.

" So, now, we're now at a time where deep learning is very successful.

So, let us squint less, and say

let's, uh, open our eyes and say

w- what to you is an interesting difference between the human brain .

..

Now, I know you're probably not an expert

uh, neither a neuroscientist and neurobiologist, but loosely speaking

what's the difference between the human brain and artificial neural networks that's interesting to you for the next decade or two?

That's a good question to ask.

What is in- what is an interesting difference between the neurons betwe- between the brain and our artificial neural networks?

So, I feel like today, artificial neural networks .

..

So, we all agree that there are certain dimensions in which the human brain vastly outperforms our models.

But I also think that there are some ways in which our artificial neural networks have a number of very important advantages over the brain.

Look- looking at the- the advantages versus disadvantages is a good way to figure out what is the important difference.

So, the brain uses spikes which may or may not be important.

Yeah, that's a really interesting question.

Do- do you think it's important or not?

My- That- that's one big architectural difference between- Yeah.

.

.

artificial neural networks and .

..

It's hard to tell, but my prior is not very high

and I can te- I can say why.

You know, there are people who are interested in spike in neural networks

and basically what they figured out is that they need to simulate the non-spiking neural networks in spikes.

Hmm.

And that's how they're gonna make- make them work.

If you don't simulate the non-spiking neural networks in spikes

it's not going to work, because the question is

why should it work?

And that connects to questions around back propagation

and questions around deep learning.

You've got this giant neural network.

Why should it work at all?

Why should the learning rule work at all?

It's not a self-evident question, especially if you

let's say, if you were just starting in the field and you read the very early papers.

You can say, "Hey, people are saying

'Let's build neural networks.

'" That's a great idea, because the brain is a neural network

so it would be useful to build neural networks.

Yep.

Now, let's figure out how to train them.

It should be possible to train them, probably

but how?

And so the big idea is the cost function.

That's the big idea.

The cost function is a way of measuring the performance of the system according to some measure.

By the way, that is a big .

..

Well, l- actually, let me think.

Is that- is that, uh, one, a difficult idea to arrive at?

And how big of an idea is that

that there's a single cost function .

..

Let me- sorry, let me take a pause.

Is supervised learning a difficult concept to come to?

I don't know.

All concepts are very easy in retrospect.

Yeah, that's why it seems trivial now

but I .

..

'Cause- 'cause the reason I ask that, and we'll talk about it

is there other things?

Is there things that don't necessarily have a cost function

or maybe have many cost functions, or maybe have dynamic cost functions

or maybe a totally different kind of architectures?

Yeah.

'Cause we have to think like that in order to arrive at something new

right?

So, the only- so the good examples of things which don't have clear cost functions are GANs.

Right.

In a GAN, you have a game.

So, instead of thinking of a cost function

where you wanna optimize, but you know that you have an algorithm gradient descent which will optimize the cost function

and then you can reason about the behavior of your system in terms of what it optimizes.

With a GAN, you say, "I have a game

and I'll reason abo- about the behavior of the system in terms of the equilibria of the game.

" But it's all about coming up with these mathematical objects that help us reason about the behavior of our system.

Right, that's really interesting.

Yeah, so GAN is the only one.

It's kind of a com- the cost function is emergent from the comparison.

It's- I don't- I don't know if it has a cost function.

I don't know if it's meaningful to talk about the cost function of a GAN.

It's kind of like the cost function of biological evolution

or the cost function of the economy.

It's- you can talk about regions to which it could be- go towards

but I don't think .

..

I don't think the cost function analogy is the most useful for GAN.

So, if evolution doesn't .

..

That's really interesting.

So, if evolution doesn't really have a cost function

like, a cost function based on its .

..

Something akin to our mathematical conception of a cost function

then do you think cost functions in deep learning are holding us back?

Yeah, I .

..

So, you- you just kinda mentioned that cost function is a- is a nice first profound idea.

Do you think that's a good idea?

Do you think it's an idea we'll go past?

So, self-play starts to touch on that a little bit

uh, in reinforcement learning, uh, systems.

That's right.

Self-play, and also ideas around exploration where you're trying to take action that sur- that surprise a predictor.

I'm a big fan of cost functions.

I think cost functions are great and they serve us really well

and I think that whenever we can do things we c- with cost functions

we should.

And, you know, maybe there is a chance that we will come up with some yet another profound way of looking at things that will involve cost functions in a less central way.

But I don't know.

I think cost functions are, I mean

I would not bet against cost functions.

Is there other things about the brain that pop into your mind that might be different and interesting for us to consider in designing artificial neural networks?

So we talked about spiking a little bit.

I mean, one- one thing which may potentially be useful

I think people, neuroscientists have figured out something about the learning rule of the brain

or s- I'm talking about spike-timing-dependent plasticity, and it would be nice if some people were to study that in simulation.

Wait, sorry, spike-time-independent plasticity?

Yeah, that's right.

What's that?

STDP, it's- it's a particular learning rule that uses spike timing to figure out how to- to determine how to update the synapses.

So it's kind of like, if a synapse fires into the neuron before the neuron fires

then it strengthen the synapse, and if the synapse fires into the neuron shortly after the neuron fired

then it weakens the synapse.

Something along this line.

I am 90% sure it's right, so if I said something wrong here

don't-  .

..

don't get too angry.

But you sounded brilliant while saying it.

But the timing, d- that's one thing that's missing

the- the temporal dynamics is not captured.

I think that's like a fundamental property of the brain

is the timing of the s- of the signals.

Well, we have recurrent neural networks.

But, you- you think of that as the s- I mean

that's a very crude simplified, uh, what's that called?

The- the- there's a clock, I guess

to, uh, recurrent neural networks.

Mm-hmm.

It's this- this seems like the brain is the general

the continuous version of that, the- the generalization

where all possible timings are possible, and then within those timings is contained some information.

You think recurrent neural networks, the recurrence in recurrent neural networks can capture the same kind of phenomena as the timing that seems to be important for the brain

i- i- in the- in the firing of neurons in the brain?

I- I mean, I think, I think recurrent neural netwo- r- recurrent neural networks are amazing

and they can do, I think they can do anything we- we'd want them to- we'd want a system to do.

Right now, recurrent neural networks have been superseded by transformers

but maybe one day they'll make a comeback

maybe they'll be back.

We'll see.

 Let me, uh, on a small tangent say

do you think they'll be back?

So, so much of, uh, the breakthroughs recently that we'll talk about on

uh, natural language processing and language modeling has been with transformers that don't emphasize recurrence.

Do you think recurrence will make a comeback?

Well, some kind of recurrence I think very likely.

Recurrent neural networks for proc- as they're typically thought of for processing sequences

I think it's also possible.

W- what- w- what is, to you

a recurrent neural network?

In generally speaking, I guess, what is a recurrent neural network?

You have a neural network which maintains a high dimensional hidden state.

And then when an observation arrives, it updates its high dimensional hidden state through its connections in some way.

# Chapter 2

i- i- in the- in the firing of neurons in the brain?

I- I mean, I think, I think recurrent neural netwo- r- recurrent neural networks are amazing

and they can do, I think they can do anything we- we'd want them to- we'd want a system to do.

Right now, recurrent neural networks have been superseded by transformers

but maybe one day they'll make a comeback

maybe they'll be back.

We'll see.

 Let me, uh, on a small tangent say

do you think they'll be back?

So, so much of, uh, the breakthroughs recently that we'll talk about on

uh, natural language processing and language modeling has been with transformers that don't emphasize recurrence.

Do you think recurrence will make a comeback?

Well, some kind of recurrence I think very likely.

Recurrent neural networks for proc- as they're typically thought of for processing sequences

I think it's also possible.

W- what- w- what is, to you

a recurrent neural network?

In generally speaking, I guess, what is a recurrent neural network?

You have a neural network which maintains a high dimensional hidden state.

And then when an observation arrives, it updates its high dimensional hidden state through its connections in some way.

So do you think, you know, that's what

like, expert systems did, right?

Symbolic AI, uh, the knowledge-based, growing a knowledge base is- is maintaining a hidden state

which is its knowledge base and is growing it by sequential processing.

Do you think of it more generally in that way

or is it simply, is it the more constrained form th- of- of a hidden state with certain kind of gating units that we think of as today with LSTMs and that?

I mean, the hidden state is technically what you described there

the hidden state that goes inside the LSTM or the RNN or something like this.

But then what should be contained, you know

if you want to make the expert system

um, analogy, I'm not.

..

I mean, you could say that the knowledge is stored in the- in the connections

and then the short-term processing is- is done in the- in the hidden state.

Yes.

Could you say that?

Yes.

So, uh, sort of, do you think there's a future of building large-scale knowledge bases within the neural networks?

Definitely.

 So, we're gonna pause on that confidence 'cause I wanna explore that

but let me zoom back out and ask

um, back to the history of ImageNet

neural networks have been around for many decades

as you mentioned.

What do you think were the key ideas that led to their success

that ImageNet moment and beyond, the- the success in the past 10 years?

Okay, so the question is, to make sure I didn't miss anything

the key ideas that led to the success of deep learning over the past 10 years.

Exactly, even though the fundamental thing behind deep learning has been around for much longer.

So, the key idea about deep learning

or rather, the s- the key fact about deep learning

before deep learning started to be successful, is that it was underestimated.

People who worked in machine learning simply didn't think that n- neural networks could do much.

People didn't believe that large neural networks could be trained.

People thought that, well, there was lots of

there was a lot of debate going on in machine learning about what are the right methods and so on

and people were arguing because there were no

there- there were- there were no- there was no way to get hard facts.

And by that I mean there were no benchmarks which were truly hard

that if you s- do really well on them

then you can say, "Look, here is my system.

" That's when you switch from.

..

Th- that's when this field becomes a little bit more of an engineering field.

So in terms of deep learning, to answer the question directly

the ideas were all there.

The thing that was missing was a lot of supervised data and a lot of compute.

Once you have a lot of supervised data and a lot of compute

then there is a third thing which is needed as well

and that is conviction.

Conviction that if you take the right stuff which already exists and apply and mix with a lot of data and a lot of compute

that it will in fact work.

And so that was the missing piece.

It was, you had the.

..

You needed the, the data, you needed the compute which showed up in terms of GPUs

and you needed the conviction to realize that you need to mix them together.

So that's really interesting.

So, uh, I- I guess the presence of compute and the presence of supervised data allowed the empirical evidence to do the convincing of the majority of the computer science community.

So, I guess there's a key moment with

uh, uh, Jitendra Malik and, uh

Alex, uh, Alyosha Efros who were very skeptical

right?

And then there's a Geoffrey Hinton that was the opposite of skeptical

and there was a convincing moment, and I think ImageNet served as that moment.

That's right.

And it represented this kind of.

..

Or the big pillars of computer vision community kind of.

..

 The- the wizards got together, and then all of a sudden

there was a shift.

And it's not enough for the ideas to all be there and the compute to be there.

It's for it to convince the cynicism that existed that- that.

..

It's interesting that people just didn't believe for a couple of decades.

Yeah, well, but it was more than that.

It's kind of.

..

When- when- when- when put this way, it sounds like

"Well, you know, those silly people who didn't believe what were

what were they missing.

" But in reality, things were confusing because neural networks really did not work on anything.

Right.

And they were not the best method on pretty much anything as well.

And it was pretty rational to say, "Yeah

this stuff doesn't have any traction.

" And that's why you need to have these very hard tasks which are

which produce undeniable evidence, and that's how we make progress.

And that's why the field is making progress today

because we have these hard benchmarks which represent true progress.

And so.

..

And this is why we are able to avoid endless debate.

So, incredibly, you've contributed some of the biggest recent ideas in AI in

in computer vision, language, natural language processing

reinforcement learning, sort of everything in between.

Maybe not GANs.

 Is there.

..

 There may not be a topic you haven't touched

and of course the, the fundamental science of deep learning.

What is the difference to you between vision

language, and as in reinforcement learning, action as learning problems

and what are the commonalities?

Do you see them as all interconnected?

Are they fundamentally different domains that require different approaches?

Okay, that's a good question.

Machine learning is a field with a lot of unity

a huge amount of unity.

In fact- What do you mean by unity?

Like, overlap of ideas?

Overlap of ideas, overlap of principles.

In fact, there is only one or two or three principles which are very

very simple.

And then they, then they apply in almost the same way

in almost the same way to the different modalities

to the different problems.

And that's why today, when someone writes a paper on improving optimization of deep learning and vision

it improves the different NLP applications and it improves the different reinforcement learning applications.

Reinforcement learn- So, I would say that computer vision and NLP are very similar to each other.

Today, they differ in that they have slightly different architectures.

We use transformers in NLP, and we use convolutional neural networks in vision.

But it's also possible that one day, this will change and everything will be unified with a single architecture.

Because if you go back a few years ago in natural language processing

there were a hu- a huge number of architectures

for every different tiny problem had its own architecture.

Today, there's just one transformer for all those different tasks.

And if you go back in time even more

you had even more and more fragmentation.

And every little problem in AI had its own little sub-specialization and sub-

you know, little set of collection of skills

people who would know how to engineer the features.

Now, it's all been subsumed by deep learning.

We have this unification.

And so I expect vision to become unified with natural language as well.

Or rather, I shouldn't say "expect," I think it's possible.

I don't want to be too sure, because I think on the conventional neural net is very computationally efficient.

RL is different.

RL does require slightly different techniques, because you really do need to take action.

You really do need to do something about exploration.

Your variance is much higher.

But I think there is a lot of unity even there.

And I would expect, for example, that at some point

there will be some broader unification between RL and supervised learning

where somehow the RL will be making decisions to make the supervised learning go better.

And it will be, I imagine, one big black box and you just throw ev- you know

you shovel, shovel things into it and it just figures out what to do with whatever you shovel at it.

I mean, reinforcement learning has some aspects of language and vision combined almost.

There's elements of a long-term memory that you should be utilizing

and there's elements of a really rich sensory space.

So it seems like the.

..

It's- it's like the union of the two or something like that.

I'd- I'd say something slightly differently.

I'd say that reinforcement learning is neither, but it naturally interfaces and integrates with the two of them.

Do you think action is fundamentally different?

So yeah, what is interesting about.

..

What is unique about policy of learning to act?

Well, so one example, for instance, is that when you learn to act

you are fundamentally in a non-stationary world, because as your actions change

the things you see s- start changing.

You, you experience the world in a different way

and this is not the case for the more traditional static problem where you have a dist- some distribution and you just apply a model to that distribution.

You think it's a fundamentally different problem, or is it just a more difficult general- it's a generalization of the problem of understanding?

I mean, it's- it's- it's a question of definitions almost.

There is a huge- I mean, there is a huge amount of commonality for sure.

You take gradients, you try- you take gradients

we try to approximate gradients in both cases.

In some ca- in the case of reinforcement learning

you have some tools to reduce the variance of the gradients

you do that.

..

. there's lots of commonality, use the same neural net in both cases

you compute the gradient, you apply Adam in both cases.

So, I mean, there's lots in common for sure

but there are some small differences which are not completely insignificant.

It's really just a matter of your po- of your point of view what frame of reference you

what, h- how much do you zoom

wanna zoom in or out as you look at these problems.

Which problem do you think is harder?

So, people like Noam Chomsky believe that language is fundamental to everything

so it underlies everything.

Do you think language understanding is harder than visual scene understanding

or vice versa?

I think that asking if a problem is hard is slightly wrong.

I think the question is a little bit wrong

and I wanna explain why.

So, what does it mean for a problem to be hard?

Okay.

The non-interesting dumb answer to that is there's this s- s- is a benchmark

and there's a human level of performance on that benchmark.

And how is the effort required to reach the human level- Okay.

.

..

benchmark.

So, from the perspective of how much until we get to human level.

..

On a very good benchmark.

Yeah, like some.

..

I- I- I under- I understand what you mean by that.

So, what I was going, going to say that a lot of it depends on

you know, once you solve a problem

it stops being hard.

And that's- Right.

 .

..

all, all, that's always true, and so- That's a.

..

..

..

but if something is hard or not depends on what our tools can do today.

So, you know, we say today, true human level language understanding and visual perception are hard in the sense that there is no way of solving the problem completely in the next three months.

Right.

So, I agree with that statement.

Beyond that, I'm just, I'd be, my s- my guess would be as good as yours

I don't know.

Oh, okay.

So, you don't have a fundamental intuition about how hard language understanding is?

Well, I think I, I, I

now I changed my mind.

I'd say language is probably going to be harder.

..

I mean, it depends on how you define it.

Like, if you mean absolute top-notch 100% language understanding

I'll go with language.

And so, uh, th- But then if I show you a piece of paper with letters on it

is that.

..

You, you see what I mean?

And so, you have a vision system

you say it's the best f- human level vision system.

I show you.

..

I open a book and I show you letters.

Will it understand how these letters form into word and sentences and meaning?

Is this part of the vision problem?

Where does vision end and language begin?

Yeah, so Chomsky would say it starts at language.

So, vision is just a little example of the kind of

uh, structuring we.

..

And, you know, fundamental hierarchy of ideas that's already represented in our brain somehow

that's represented through language.

But where does vision stop and language begin?

That's a really interesting, uh, question.

 It.

..

So, one possibility is that it's impossible to achieve really deep understanding in either images or language without basically using the same kind of system.

So, you're going to get the other for free.

 I think, I think it's pretty likely that

yes, if we can get one, we prob- our machine learning is probably that good that we can get the other.

But it's not 100.

..

I'm not 100% sure.

And also, uh, I think a lot r- a lo- a lot of it really does depend on your definitions.

Definitions of?

Of, like, perfect vision.

Because ra- you know, reading is vision

but should it count?

Yeah.

Uh, to me, sort of my definition is if a system looked at an image

and then a system looked at a piece of text and then told me something about that

and I was really impressed.

That's relative.

You'll be impressed for half an hour, and then you're gonna say

"Well, I mean, all the systems do that

but here's the thing they don't do.

" Yeah.

But I, I don't have that with humans.

Humans continue to impress me.

Is that true?

Well, th- the ones.

..

Okay.

So, uh, I'm a fan of monogamy

so I, I like the idea of marrying somebody

being with them for several decades.

 So, I s- I believe in the fact that

yes, it's possible to have somebody continuously giving you

uh, ple- pleasurable, interesting, witty, new ideas

friends.

Yeah.

I think, I think so.

They continue to surprise you.

The surprise, it's, um, you know

that injection of randomness that seems to be a

th- it seems to be a, a nice source of

yeah, continued, uh, inspiration.

Like, the, the wit, the humor

I think.

..

Yeah.

That, that, the, that would be a.

..

It's a very subjective test, but I think if you have enough humans in the room.

Yeah.

I, I, I understand what you mean.

Yeah.

I feel like I, I, I misunderstood what you meant by impressing you.

I thought you meant to impress you with its intelligence

with how, how, with how good, well it understands

um, an image.

I wo- I, I thought you meant something like

"I'm gonna show it a really complicated image

and it's gonna get it right.

And you're gonna say, 'Wow.

'" Right.

"That's really cool.

Our systems of, you know, January 2020 have not been doing that.

" Yeah.

No, I, I, I think it all boils down to

like, the reason people click like on stuff on the internet

which is, like, it makes them laugh.

So, it's, like, humor or wit- Yeah.

.

..

or insight.

We'll, we'll.

..

I'm, I'm sure we'll get it as

get that as well.

So, forgive the romanticized question, but looking back

to you, what is the most beautiful or surprising idea in deep learning or AI in general you've come across?

So, I think the most beautiful thing about deep learning is that it actually works.

 And I mean it, because you got these ideas

you got the little neural network, you got the back propagation algorithm

and then you got some theories as to

you know, this is kinda like the brain.

So, maybe if you make it large

# Chapter 3

" Yeah.

No, I, I, I think it all boils down to

like, the reason people click like on stuff on the internet

which is, like, it makes them laugh.

So, it's, like, humor or wit- Yeah.

.

..

or insight.

We'll, we'll.

..

I'm, I'm sure we'll get it as

get that as well.

So, forgive the romanticized question, but looking back

to you, what is the most beautiful or surprising idea in deep learning or AI in general you've come across?

So, I think the most beautiful thing about deep learning is that it actually works.

 And I mean it, because you got these ideas

you got the little neural network, you got the back propagation algorithm

and then you got some theories as to

you know, this is kinda like the brain.

So, maybe if you make it large

if you make the neural network large, and you train it on a lot of data

then it will do the same function that the brain does.

And it turns out to be true.

That's crazy.

 And now we just train these neural networks and you make them larger and they keep getting better.

..

. and I find it unbelievable.

I find it unbelievable that this whole AI stuff with neural networks works.

Have you built up an intuition of why?

Are there little bits and pieces of intuitions

of insights of why this whole thing works?

I mean, some, definitely.

While we know that optimization .

..

we, we now have good re- you know

we've take, we- we've had lots of empirical

you know, huge amounts of empirical reasons to believe that optimization should work on all

most problems we care about.

Do you have insights of what .

..

so you just said empirical evidence.

Is most of your .

..

s- sort of empirical evidence kind of convinces you.

It's like evolution is empirical.

It shows you that, look, this evolutionary process seems to be a good way to design

uh, organisms that survive in their environment.

But it doesn't really get you to the insights of how the whole thing works.

Well, I think it's, it's .

..

a, a good analogy is physics.

You know how you say, "Hey, let's do some physics calculation and come up with some new physics theory and make some prediction.

" But then you've gotta run the experiment.

You know, you've gotta run the experiment.

It's important.

So it's a bit the- the same here

except that maybe some- sometimes the experiment came before the theory.

But it still is the case.

You know, you have some data, and you come up with some prediction.

You say, "Yeah, let's make a big neural network.

Let's train it.

And it's going to work much better than anything before it

and it will, in fact, continue to get better as we make it larger.

" And it turns out to be true

that's- that's amazing when a theory is validated like this

you know.

It's not a mathematical theory.

It's more of a biological theory almost.

So I think there are not-terrible analogies between deep learning and biology.

I would say it's like the geometric mean of biology and physics.

 That's deep learning.

The geometric mean of biology and physics.

I think I'm gonna need a few hours to wrap my head around that.

Uh, 'cause just to find the geometric .

..

just to find, uh, the set of what biology represents.

Well, biology, p- in, in biology

things are really complicated.

Yeah.

And theories are really, really .

..

it's really hard to have good predictive theory.

And if .

..

in physics, the theories are too good.

F- i- in, in theory, in physics

people make these super precise theories which make these amazing predictions.

And in machine learning, we're kinda in between.

Kind of in between, but it would be nice if machine learning somehow helped us discover the unification of the two

as opposed to sort of the in between.

But you're right.

That's .

..

you're, you're kinda trying to juggle both.

So do you think there's still beautiful and mysterious properties in neural networks that are yet to be discovered?

Definitely.

I think that we are still massively underestimating deep learning.

What do you think it will look like?

Like, what .

..

?

If I knew, I would've done it

you know?

 So, uh, but if you look at all the progress from the past 10 years

I would say most of it, I would say there have been a few cases where some .

..

where things that felt like really new ideas showed up.

But by and large, it was every year we thought

"Okay, deep learning goes this far.

Nope, it actually goes further.

"  And then the next year, "Okay

now it .

..

you .

..

now this is, this is peak deep learning.

We are really done.

Nope, goes further.

" It just keeps going further each year.

Mm-hmm.

So that means that we keep underestimating, we keep not understanding it.

Has surprising properties all the time.

Do you think it's getting harder and harder?

To make progress?

Yeah, to make progress.

It depends on what you mean.

I think the field will continue to make very robust progress for quite a while.

I think for individual researchers, especially people who are doing r- um

research, it can be harder, because there is a very large number of researchers right now.

I think that if you have a lot of compute

then you can make a lot of very interesting discoveries.

But then you have to deal with the challenge of managing a huge computes- a huge clus- a huge compute cluster to run your experiments.

It's a little bit harder.

So I'm asking you all these questions that nobody knows the answer to.

But you're one of the smartest people I know

so I'm gonna keep asking.

The .

..

so let's imagine all the breakthroughs that happen in the next 30 years in deep learning.

Do you think most of those breakthroughs can be done by one person with one computer?

Sort of in the space of breakthroughs, do you think compute will be

uh, compute and large efforts will be necessary?

I mean, I can't be sure.

A- when you say one computer, you mean how- how large?

 Ah, you're, uh, you're clever.

I mean, one com- one GPU.

I see.

I think it's pretty unlikely.

I think it's pretty unlikely.

I think that there are many .

..

the, the stack of deep learning is starting to be quite deep.

If you look at it, you've got all the way from the ideas

the systems to build the datasets, the distributed programming

the building the actual cluster, the GPU programming

putting it all together.

So now the stack is getting really deep

and I think it becomes .

..

it can be quite hard for a single person to become

to be world-class in every single layer of the stack.

What about the, what, like, Vladimir Vapnik really insists on is taking MNIST and trying to learn from very few examples.

So being able to learn e- more efficiently.

Do you think that's .

..

there will be breakthroughs in that space that would may not need the huge compute?

I think there will be hu- a ver- I think there will be a large number of breakthroughs in general that will not need a huge amount of compute.

So maybe I should clarify that.

I think that some breakthroughs will require a lot of compute.

Sure.

And I think building systems which actually do things will require a huge amount of computes.

That one is pretty obvious.

If you want to do X- Right.

.

..

and X requires a huge neural net, you gotta get a huge neural net.

But I think there will be lots of .

..

I think there is lots of room for very important work being done by small groups and individuals.

Can you maybe, sort of o- on the topic of the

the science of deep learning, talk about one of the recent papers that you released?

Sure.

The deep double descent?

Mm-hmm.

Where bigger models and more data hurt.

Uh, I think it's a really interesting paper.

Can you, can you describe the main idea and .

..

Yeah, definitely.

So what happened is that some .

..

Over, over the years, some small number of researchers noticed that it is kind of weird that when you make the neural network larger

it works better.

And it seems to go in contradiction with statistical ideas.

And then some people made an analysis showing that actually you got this double descent bump.

And what we've done was to show that double descent occurs for all

for pretty much all practical deep learning systems.

And that it will be also- So can you step back?

Um, what's the X axis and the Y axis of a double descent plot?

Okay, great.

So you can, you can look, you can do things like

you can take a neural network and you can start increasing its size slowly while keeping your data set fixed.

So if you increase the size of the neural network slowly

and if you don't do early stopping, that's a pretty important detail

then when the neural network is really small

you make it larger, you get a very rapid increase in performance.

Then you continue to make it larger, and at some point performance will get worse.

And it gets, and- and it gets the worst exactly at the point at which it achieves zero training error

precisely zero training loss.

And then as you make it large, it starts to get better again.

And it's kind of counterintuitive because you'd expect deep learning phenomena to be monotonic.

And it's hard to be sure what it means

but it also occurs in, in the case of linear classifiers.

And the intuition basically boils down to the following.

When you, when you have a lot

when you have a large data set and a small model

then small, tiny, random.

..

So, so basically what is overfitting?

Overfitting is when your model is somehow very sensitive to the small random unimportant stuff in your data set.

In the training data.

In the training data set, precisely.

So if you have a small model and you have a big data set

and there may be some random thing, you know

some training cases are randomly in the data set and others may not be there.

But the small model, but the small model is kind of insensitive to this randomness because it's the sa- you

there is pretty much no uncertainty about the model when the data set is large.

So, okay.

So at the very basic level, to me

it is the most surprising thing that neural networks don't overfit every time very quickly

uh,  before ever being able to learn anything.

The huge number of parameters.

So here is, so there is one way.

..

Okay, so maybe the, so let, let me try to give the explanation

maybe that will be, that will work.

So you got a huge neural network.

Let's suppose you've got a.

..

You are, you have a huge neural network

you have a huge number of parameters.

And now let's pretend everything is linear, which is not

but let's just pretend.

Then there is this big subspace where your neural network achieves zero error.

Mm-hmm.

And SGT is going to find approximately the point- Stochastic gradient

yeah.

That's right, yeah, approximately the point with the smallest norm in that subspace.

Okay.

And that can also be proven to be insensitive to the small randomness in the data when the dimensionality is high.

But when the dimensionality of the data is equal to the dimensionality of the model

then there is a one-to-one correspondence between all the data sets and the models.

So small changes in the data set actually lead to large changes in the model

and that's why performance gets worse.

So this is the best explanation more or less.

So then it would be good for the model to have more parameters

sort of, um, to be bigger than the data?

That's right.

But o- only if you don't early stop.

If you introduce early stop in your regularization

you can make the double s- descent bump almost completely disappear.

What is early stop?

Early stopping is when you train your model and you monitor your test

your validation performance.

And then if at some point validation performance starts to get worse

you say, "Okay, let's stop training.

We are good.

We are good.

We are good enough.

" So the, the magic happens after, after that moment.

So you don't want to do the early stopping?

Well, if you don't do the early stopping

you get these very, you get a very pronounced double descent.

Do you have any intuition why this happens?

Double descent?

Oh, sorry, early stopping?

No, the double descent.

So the- Oh, yeah.

So I try, let's see.

The intuition is basically is this, that when the data set has as many degrees of freedom as the model

then there is a one-to-one correspondence between them.

And so small changes to the data set lead to noticeable changes in the model.

So your model is very sensitive to all the randomness.

It is unable to discard it.

Whereas it turns out that when you have a lot more data than parameters or a lot more parameters than data

the resulting solution will be insensitive to small changes in the data set.

Oh, so it's able to, that's nicely put

discard the small changes, the, the randomnessaa.

..

Randomness, exactly.

The, the, the, the spurious correlations which you don't want.

Geoff Hinton suggested we need to throw backpropagation.

We already kind of talked about this a little bit

but he suggested we need to throw away backpropagation and start over.

I mean, o- of course some of that is a little bit

um, wit and humor.

But what do you think?

What could be an alternative method of training neural networks?

Well, the thing that he said precisely is that to the extent that you can't find backpropagation in the brain

it's worth seeing if we can learn something from how the brain learns.

But backpropagation is very useful and we should keep using it.

Oh, you're saying that once we discover the mechanism of learning in the brain or any aspects of that mechanism

we should also try to implement that in neural networks?

If it turns out that we can't find backpropagation in the brain.

If we can't find backpropagation in the brain.

Well, so I guess your answer to that is backpropagation is pretty damn useful.

So w- why are we complaining?

I mean, I, I personally am a big fan of backpropagation.

I think it's a great algorithm because it solves an extremely fundamental problem

which is finding a neural circuit subject to some constraints.

..

. and I don't see that problem going away.

So, that's why I- I really, I think it's pretty unlikely that we'll have anything which is going to be dramatically different.

It could happen, but I wouldn't bet on it right now.

So, let me ask a sort of big picture question.

Do you think can- do you think neural networks can be made to reason?

Why not?

 Well, if you look for example at AlphaGo or AlphaZero

the neural network of AlphaZero plays Go, which a g- which we all agree is a game that requires reasoning

better than 99.

9% of all humans.

Just the neural network, without the search

just the neural network itself.

Doesn't that give us an existence proof that neural networks can reason?

To push back and disagree a little bit

we all agree that Go is reasoning.

Uh, I think I- I agree, I don't think that's a trivial.

..

So obviously, reasoning, like intelligence, is

um, is a loose, gray area term

a little bit.

Maybe you disagree with that.

But yes, I think it has some of the same elements of reasoning.

Reasoning is almost, like, akin to search

right?

There's a sequential element of stepwise consideration of possibilities

and sort of building on top of those possibilities in a sequential manner until you arrive at some insight.

Sort of, yeah, I guess playing Go is kind of like that

and when you have a single neural network doing that without search

it's kind of like that.

So, there's an existent proof in a particular constrained environment that a- a process akin to what many people call reasoning exists

but more general kind of reasoning.

So, off the board.

There is one other existence proof.

Oh, boy.

Which one?

 Us humans?

Yes.

Okay.

All right.

So, do you think the architecture that will allow neural networks to reason will look similar to the neural network architectures we have today?

I think it will.

I think.

..

Well, I don't want to make too o- overly definitive statements.

I think it's definitely possible that the neural networks that will produce the reasoning breakthroughs of the future will be very similar to the architectures that exist today.

Maybe a little bit more recurrent, maybe a little bit deeper.

But, but these- these neural nets are so insanely powerful.

Why wouldn't they be able to learn to reason?

# Chapter 4

it's kind of like that.

So, there's an existent proof in a particular constrained environment that a- a process akin to what many people call reasoning exists

but more general kind of reasoning.

So, off the board.

There is one other existence proof.

Oh, boy.

Which one?

 Us humans?

Yes.

Okay.

All right.

So, do you think the architecture that will allow neural networks to reason will look similar to the neural network architectures we have today?

I think it will.

I think.

..

Well, I don't want to make too o- overly definitive statements.

I think it's definitely possible that the neural networks that will produce the reasoning breakthroughs of the future will be very similar to the architectures that exist today.

Maybe a little bit more recurrent, maybe a little bit deeper.

But, but these- these neural nets are so insanely powerful.

Why wouldn't they be able to learn to reason?

Humans can reason.

So, why can't neural networks?

So, do you think the kind of stuff we've seen neural networks do is a kind of just weak reasoning?

So, it's not a fundamentally different process?

Again, this is stuff we don't- nobody knows the answer to.

So, when it comes to our neural networks

I would- the thing which I would say is that neural networks are capable of reasoning.

But if you train a neural network on a task which doesn't require reasoning

it's not going to reason.

This is a well-known effect, where the neural network will solve exactly the- it will solve the problem that you pose in front of it in the easiest way possible.

Right.

That takes us to the- to o- o- one of the brilliant sort of ways you've described neural networks

which is, uh, you've referred to neural networks as the search for small circuits

and maybe general intelligence as the search for small programs

which I found as a metaphor very compelling.

Can you elaborate on that difference?

Yeah.

So, the thing which I said precisely was that if you can find the shortest program that outputs the data in your- at your disposal

then you will be able to use it to make the best prediction possible.

Mm-hmm.

And that's a theoretical statement which can be proven mathematically.

Now, you can also prove mathematically that it is- that finding the shortest program regenerates some data is not com- is not a computable operation.

No, uh, finite amount of compute can do this.

So then, with- with neural networks, neural networks are the next best thing that actually works in practice.

We are not able to find the best- the shortest program which generates our data

but we are able to find, you know

a small, but now- now that statement should be amended

even a large circuit which fits our data in some way.

Well, I think what you meant by the small circuit is the smallest needed circuit.

Well, I- s- the thing- the thing which I would change now

back- back then, I really have- I haven't fully internalized the over-parametr- the over-parameterized results.

The re- the things we know about over-parameterized neural nets

now I would phrase it as, "A large circuit that can- wh- whose weights contain a small amount of information

" which I think is what's going on.

If you imagine the training process of a neural network as you slowly transmit entropy from the data set to the parameters

then somehow, the amount of information in the weights ends up being not very large

which would explain why they generalize so well.

So that's- there the large circuit might be one that's helpful for the regulariz- for the generalization?

Yeah, something like this.

But do you see their- do you see it important to be able to try to learn something like programs?

I mean, if we can, definitely.

I think it's kind of- the answer is kind of yes

if we can do it.

We should do things that we can do it.

 It's- it's- the reason we are pushing on deep learning

the fundamental reason, the cau- the- the- the- the root cause is that we are able to train them.

So, in other words, training comes first.

We've got our pillar, which is the training pillar

and now we are trying to contort our neural networks around the training pillar.

We gotta stay trainable.

This is an invo- this is an invariant we cannot violate.

And so.

..

..

. being trainable means starting from scratch, knowing nothing

you can actually pretty quickly converge towards knowing a lot.

Or even slowly.

But it means that given the resources at your disposal

you can train the neural net and get it to achieve useful performance.

Yeah, that's a pillar we can't move away from.

That's right.

Because if you c- and whereas, if you say

"Hey, let's find the shortest program," well

we can't do that.

So it doesn't matter how useful that would be

we can't do it.

So we won't.

So do you think.

..

You kind of mentioned that neural networks are good at finding small circuits or large circuits.

Do you think then the matter of finding small programs is just the data?

No.

So do.

..

the ki- sorry, not, not the size or character

the qual- the, the, the type of data.

Sort of ask, giving it programs.

Well, I think the thing is that right now

finding.

..

there are no good precedents of people successfully finding programs really well.

And so the way you'd find programs is you'd train a deep neural network to do it basically.

Right.

Which is, which is the right way to go about it.

But there's not good, uh, illustrations of that yet.

It has- hasn't been yet.

But I- in, in principle, it should be possible.

Can you elaborate another bit?

Do you.

..

what's your insight in principle?

Well- Put another way, you don't see why it's not possible.

Well, it's kind of like more, it's more a statement of.

..

I think that it's, I thi- I think that it's unwise to bet against deep learning and-  .

..

if it's a fun- if it's a cognitive function that humans seem to be able to do

then it doesn't take too long for some deep neural net to pop up that can do it too.

 Yeah.

I'm, I'm, I'm, I'm there with you.

I can.

..

I've, I've stopped betting against neural networks at this point

because they continue to surprise us.

What about long-term memory?

Can neural networks have long-term memory or something like knowledge bases?

So being able to aggregate important information over long periods of time that would then serve as useful sort of representations of state that

uh, you could make decisions by, so have a long-term context based on which you're making the decision.

So in some sense, the parameters already do that.

The parameters are an aggregation of the da- of the neural.

..

of the entirety of the neural net's experience

and so they count as the long- as long-form

long-term knowledge.

And people have trained various neural nets to act as knowledge bases and

you know, investigated th- invest.

..

people have investigated language models as knowledge bases.

So there is work, there is work there.

Yeah, but in some sense.

Do you think in every sense?

Do you think there's a.

..

it's- it's all just a, a matter of coming up with a better mechanism of forgetting the useless stuff and remembering the useful stuff?

'Cause right now, I mean, there's not been mechanisms that do remember really long-term information.

What do you mean by that precisely?

Precisely.

..

I like, I like the word precisely.

So I'm thinking of the kind of compression of information the knowledge bases represent

sort of creating a.

..

Now, I apologize for my sort of human-centric thinking about what knowledge is

'cause n- neural networks aren't in-interpretable necessarily with the kind of knowledge they have discovered.

But a good example for me is knowledge bases

being able to build up over time something like the knowledge that Wikipedia represents.

It's a really compressed, structured, f- uh

knowledge base.

O- obviously not the actual Wikipedia or the language

but like a semantic web, the dream that a semantic web represented.

So it's a really nice compressed knowledge base

or something akin to that in a non-interpretable sense as

um, neural networks would have.

Well, the neural networks would be non-interpretable if you look at their weights

but their outputs should be very interpretable.

Okay, so yeah, how do you.

..

how do you make very smart neural networks

like language models, interpretable?

Well, you ask them to generate some text and the text will generally be interpretable.

Do you find that the epitome of interpretability?

Like, uh, can you do better?

Like c- can you a- 'cause you can't.

..

Okay, I would like to know what does it know and what doesn't it know.

I would like the neural network to come up with examples where it's completely dumb and examples where it's completely brilliant.

And the only way I know how to do that now is to generate a lot of examples and use my human judgment.

But it would be nice if a neural network had some aware- self-awareness about.

..

 Yeah, 100%.

I'm, I'm a big believer in self-awareness and I think that.

..

 I think, I think new- neural net self-awareness will allow for things like the capabilities like the ones you described

like for them to know what they know and what they don't know and for them to know where to invest to increase their skills most optimally.

And to your question of interpretability, there are actually two answers to that question.

One answer is, you know, we have the neural net

so we can analyze the neurons and we can try to understand what the different neurons and different layers mean and you can actually do that and OpenAI has done some work on that.

But there is a different answer which is that

I would say this is the human-centric answer where you say

you know, you look at a human being

you can't read.

..

you know, h- h- how do you know what a human being is thinking?

You ask them, you say, "Hey, what do you think about this?

What do you think about that?

" And you get some answers.

The answers you get are sticky in the sense you already have a mental model.

You already have an.

..

uh, yeah, a mental model of that human being.

You already have an understanding of like a b- a big conception of what it.

..

of that human being, how they think

what they know, how they see the world and then everything you ask

you're s- adding on to that.

..

. and that stickiness seems to be- that's one of the really interesting qualities of the- the human being

is that information is sticky.

You don't- you seem to remember the useful stuff

aggregate it well, and forget most of the information that's not useful.

Th- that process, but that's also pretty similar to the process that neural networks do.

It's just that neural networks are much crappier at it at this time.

It's n- it doesn't seem to be fundamentally that different.

But just to stick on reasoning for a little longer

 you said, "Why not?

Why can't I reason?

" What- what's a good impressive feat, benchmark

to you, of reasoning that you would be impressed by if neural networks were able to do?

Is that something you already have in mind?

Well, I think writing, writing really good code.

I think proving really hard theorems, solving open-ended problems with out-of-the-box solutions.

And, uh, sort of theorem type mathematical problems?

Yeah, I think tho- tho- those ones are a very natural example as well.

You know, if you can prove an unproven theorem

then it's hard to argue you don't reason.

And so, by the way, and this comes back to the point about the hard results

you know, if you got a har- if you have b- machine learning

deep learning as a field is very fortunate

because we have the ability to sometimes produce these unambiguous results and when they happen

uh, the debate changes, the conversation changes.

It's a convers- y- we, we have the ability to produce conversation-changing results.

Conversation, and then, of course, just like you said

people kind of take that for granted and say

"That wasn't actually a hard problem.

" Well, I mean, at some point

we'll probably run out of hard problems.

Yeah, that whole mortality thing is kind of s- kind of a sticky problem that we haven't s- quite figured out.

Maybe we'll solve that one.

I think one of the fascinating things in- in your entire body of work

but also the work at OpenAI recently, one of the conversation-changers has been in the world of language models.

Can you briefly kinda try to describe the recent history of using neural networks in the domain of language and text?

Well, there's been lots of history.

I think, I think the Elman network was

was a s- was a s- was a small

tiny recurrent neural network applied to language back in the '80s.

So the history's really, you know, fairly long

at least.

And the thing that started- th- the thing that changed the trajectory of neural networks and language is the thing that changed the trajectory of all deep learning

and that's data and compute.

So suddenly, you move from small language models which learn a little bit

and with language models in particular, you can- there's a very clear explanation for why they need to be large to be good

because they're trying to predict the next word.

Mm-hmm.

So we don't- when you don't know anything

you'll notice very, very broad strokes, surface level patterns

like sometimes there are characters and there is space between those characters.

You'll notice this pattern, and you'll notice that sometimes there is a comma and then the next character is a capital letter.

You'll notice that pattern.

Eventually, you may start to notice that there are certain words th- occur often.

You may notice that spellings are a thing.

You may notice syntax.

And when you get really good at all these

you start to notice the semantics.

You start to notice the facts.

But for that to happen, the language model needs to be larger.

So that's- let's linger on that, 'cause that's where you and Noam Chomsky disagree.

 So you think we're actually taking, uh

incremental steps, a sort of larger network

larger compute will be able to get to the semantics

be able to understand language without what, uh

Noam likes to sort of think of as a fundamental understandings of the structure of language

like, uh, imposing your theory of language onto the learning mechanism?

So you're saying the learning, you can learn from raw data the mechanism that underlies language?

Well, I thi- I think it's pretty likely

but I also want to say that I don't really k- know precisely what is- what

uh, Chomsky means b- when he talks about im- y- you said something about imposing your structure on language.

I'm not 100% sure what he means, but empirically

it seems that when you inspect those larger language models

they exhibit signs of understanding the semantics, whereas the smaller language models do not.

We've seen that a few years ago when we did work on the sentiment neuron.

We trained a small, you know, smallish LSTM to predict the next character in Amazon reviews

and we noticed that when you increase the size of the LSTM from 500 s- LSTM cells to 4

000 LSTM cells, then one of the neurons starts to represent the sentiment of the article

oh, sorry, of the review.

Now, why is that?

S- sentiment is a pretty semantic attribute.

It's not a syntactic attribute.

And for people who might not know, I don't know if that's a standard term

but sentiment is whether it's a positive or a negative review.

That's right, like this, is the person happy with something

or is the person unhappy with something?

And so here we had very clear evidence that a small neural net does not capture sentiment

while a large neural net does.

And why is that?

Well, our theory is that at some point you run out of syntax to model

# Chapter 5

uh, Chomsky means b- when he talks about im- y- you said something about imposing your structure on language.

I'm not 100% sure what he means, but empirically

it seems that when you inspect those larger language models

they exhibit signs of understanding the semantics, whereas the smaller language models do not.

We've seen that a few years ago when we did work on the sentiment neuron.

We trained a small, you know, smallish LSTM to predict the next character in Amazon reviews

and we noticed that when you increase the size of the LSTM from 500 s- LSTM cells to 4

000 LSTM cells, then one of the neurons starts to represent the sentiment of the article

oh, sorry, of the review.

Now, why is that?

S- sentiment is a pretty semantic attribute.

It's not a syntactic attribute.

And for people who might not know, I don't know if that's a standard term

but sentiment is whether it's a positive or a negative review.

That's right, like this, is the person happy with something

or is the person unhappy with something?

And so here we had very clear evidence that a small neural net does not capture sentiment

while a large neural net does.

And why is that?

Well, our theory is that at some point you run out of syntax to model

so you start, gotta focus on something else.

And with size, you quickly run out of syntax to model

and then you really start to focus on the semantics

is- would be the idea.

That's right.

And so I don't wa- I don't want to imply that our models have complete semantic understanding

because that's not true, but they definitely are showing signs of semantic understanding

partial semantic understanding, but the smaller models do not show that

those signs.

Can you take a step back and say what is GPT-2

which is one of the big language models that was the conversation-changer in the past couple of years?

Yeah, so it's, so, so GPT-2 is a transformer-.

..

with one and a half billion parameters that was trained on a

on about 40 billion tokens of text, which were obtained from web pages that were linked to

from Reddit articles with more than three up votes.

And what's a transformer?

The transformer is the most important advance in neural network architectures in recent history.

What is attention maybe too?

'Cause I think that's an interesting idea, not necessarily sort of technically speaking

but the idea of attention versus maybe what recr- rec- recurrent neural networks represent.

Yeah.

So the thing is, the transformer is a combination of multiple ideas simultaneously of which attention is one.

Do you think attention is the key?

No.

It's a key, but it's not the key.

The transformer is successful because it is the simultaneous combination of multiple ideas.

And if you were to remove either idea

it would be much less successful.

So, the transformer uses a lot of attention

but attention existed for a few years, so that can't be the main innovation.

The transformer is designed in such a way that it runs really fast on the GPU

and that makes a huge amount of difference.

This is one thing.

The second thing is a transformer is not recurrent

and that is really important too because it is more shallow and therefore much easier to optimize.

So, in other words, it uses attention.

It is, it is a, a really great fit to the GPU.

And it is not recurrent, so therefore less deep and easier to optimize.

And the combination of those factors make it successful.

So, now it makes, it makes great use of your GPU.

It allows you to achieve better results for the same amount of compute

and that's why it's successful.

Were you surprised how well transformers worked and GPT-2 worked?

So, you worked on language.

..

You've had a lot of great ideas before transformers came about in language

so you got to see the whole set of revolutions before and after.

Were you surprised?

Yeah, a little.

A little?

 Yeah.

I mean, it's hard, it's hard to remember because you adapt really quickly

but it definitely was surprising.

It definitely was.

In fact, I'll.

..

You know what?

I'll, I'll retract my statement.

It was, it was pretty amazing.

It was just amazing to see it generate this text

all this- and you know, you gotta keep in mind that we've seen- at that time

we've seen all this progress in GANs, in improving th- you know

the samples produced by GANs were just amazing.

Mm-hmm.

You have these realistic faces.

But text hasn't really moved that much.

And suddenly, we moved from, you know

whatever GANs were in 2015 to the best

most amazing GANs in one step.

Right.

And that was really stunning.

Even though theory predicted, yeah, you train a big language model

of course you should get this.

But then to see it with your own eyes

it's something else.

And yet, we adapt really quickly, and now there's

uh, sort of.

..

Some cognitive scientists write articles saying that GPT-2 models don't truly understand language.

So, we adapt quickly to how amazing the fact that they're able to model the language so well is.

So, what do you think is the bar?

For what?

For impressing us that it.

..

I don't know.

Do you think that bar will continuously be moved?

Definitely.

 I, I, I think when you start to see really dramatic economic impact

that's when.

I think that's in some sense- I see.

.

.

the next barrier, because right now, if you think about the work in AI

it's really confusing.

It's really hard to know what to make of all these advances.

It's kind of like, okay, you got an advance

and now you can do, uh, more things.

And you got another improvement, and you got another cool demo.

At some point, I think people who are outside of AI

they can no longer distinguish this progress anymore.

So, we were talking offline about translating Russian to English and how there's a lot of brilliant work in Russian that the

the rest of the world doesn't know about.

That's true for Chinese.

That's true for a lot of, uh

for, for a lot of scientists and just artistic work in general.

Do you think translation is the place where we're going to see sort of economic big impact?

I, I don't know.

I, I think, I think there is a huge number of applic- I mean

so first of all, I would wanna s- I wanna point out that translation already today- That's true.

.

..

is huge.

I think billions of people interact with, uh

big chunks of the internet primarily through translation.

So, translation is already huge, and it's hu- hugely

hugely positive too.

I think self-driving is going to be tr- hugely impactful.

And that's, you know, it's, it's unknown exactly when it happens.

But again, I would, I would not bet against deep learning

so I- So, that's deep learning in general.

But you, you th- you think- Deep learning for self-driving.

Yes.

Deep learning for self-driving, but I, I was talking about sort of language models.

I see.

Ju- just to ch- just to check- I veered

I veered off a little bit.

Just to check, you're not seeing a connection between driving and language?

No, no.

Okay.

Or rather, they both use neural nets.

That would be a poetic connection.

I think there might be some.

And like you said, there might be some kind of unification towards

uh, a kind of multitask transformers that can take on both language and vision tasks

and be an interesting unification.

Uh, let's see.

What can I ask about GPT-2 more?

Um.

..

It's simple.

There's not much to ask.

 It's- So- You take a, you take a

you take a transformer, you make it bigger

you give it more data, and suddenly it does all those amazing things.

Yeah, one of the beautiful things is that GPT

the transformers are fundamentally simple to explain, to train.

Do you think bigger will continue to show better results in language?

Probably.

Sort of like, what are the next steps with GPT-2

do you think?

I mean, for, I think for, for

for sure seeing what, uh, larger versions can do is one direction.

Also, I mean, there are, there are many questions.

There's one question which I'm curious about, and that's the following.

So, right now, GPT-2 So we feed it all this data from the internet

which means that it needs to memorize all those random facts about everything in the internet.

And it would be nice if.

..

..

. the model could somehow use its own intelligence to decide what data it wants to sta- a- a- accept

and what data it wants to reject.

Just like people.

People don't learn all data indiscriminately.

We are super selective about what we learn.

And I think this kind of active learning

I think, would be very nice to have.

Yeah.

T- listen, I love active learning.

So, let,  let me ask, does the selection of data.

..

Can you just elaborate that a little bit more?

Do you think the selection of data is

um.

..

Like, I- I have this kind of sense that the optimization of how you select data

so the active learning process, is going to be a place for a lot of breakthroughs

even in the near future.

Because there just hasn't been many breakthroughs there that are public.

I feel like there might be private breakthroughs that companies keep to themselves

'cause it's a fundamental problem that has to be solved if you wanna solve self-driving

if you wanna solve a particular task.

But d- do you.

..

Wha- what do you think about this space in general?

Yeah.

So, I think that for something like active learning

or in fact, for any kind of capability

like active learning, the thing that it really needs is a problem.

It needs a problem that requires it.

It's very hard to do research about a capability if you don't have a task

because then what's going to happen is it

you will come up with an artificial task

get good results, but not really convince anyone.

Right.

Like, we're- we're now past the stage where getting a result on MNIST

some clever formulation of MNIST, will- will convince people.

That's right.

In fact, you could quite easily come up with a simple active learning scheme on MNIST and get a 10X speedup.

But then, so what?

And I think that with active learning, there needs

there need.

..

Uh, active learning will naturally arise as there are.

..

as problems that require it pop up.

That's how I would.

..

That's my- my take on it.

There's another interesting thing that OpenAI has brought up with GPT-2

which is when you create a- a powerful artificial intelligence system.

..

And it was unclear what kind of detrimental.

..

once you release GPT-2, what kind of detrimental effect it'll have.

Because if you have an- a model that can generate pretty realistic text

you can start to imagine that, you know

on the.

..

it would be used by bots in some- some way that we can't even imagine.

So, like, there's this nervousness about what it's possible to do.

So, you- you did a really kind of brave and I think profound thing

which is start a conversation about this.

Like, how do we release powerful artificial intelligence models to the public

if we do at all?

How do we privately discuss with other even competitors about how we manage the use of the systems and so on?

So, from that, this whole experience, you released a report on it.

But, in general, are there any insights that you've gathered from just thinking about this

about how you release models like this?

I mean, I think that.

..

My take on this is that the field of AI has been in a state of childhood

and now it's exiting that state, and it's entering a state of maturity.

What that means is that AI is very successful and also very impactful.

And its impact is not only large, but it's also growing.

And so, for that reason, it seems wise to start thinking about the impact of our systems before releasing them maybe a little bit too soon

rather than a little bit too late.

And with the case of GPT-2, like I mentioned earlier

the results really were stunning.

And it seemed plausible.

It didn't seem certain.

It seemed plausible that something like GPT-2 could easily be used to reduce the cost of disinformation.

And so, there was a question of

what's the best way to release it?

And a staged release seemed logical.

A small model was released, and there was time to see the.

..

Many people used these models in lots of cool ways.

There've been lots of really cool applications.

There haven't been any negative application that we know of

and so eventually it was released.

But also other people replicated similar models.

That's an interesting question though, "that we know of.

" So, in your view, staged release is

um, at least part of the answer to the question of how do we.

..

Uh, how.

..

What do we do once we create a system like this?

It's part of the answer, yes.

Uh, uh, is there any other insights?

Like, say you don't want to release the model at all

because it's useful to you for whatever the business is.

Well, there are plen- plen- ple- plenty of people don't release models already.

Right.

Of course.

But is there some moral, ethical responsibility when you have a very powerful model to sort of communicate?

Like, just as you said, when you had GPT-2

it was unclear how much it could be used for misinformation.

It's an open question.

And getting an answer to that might require that you talk to other really smart people that are outside of

uh, uh, outside of your particular group.

I- uh, have you.

..

Please tell me there is some optimistic pathway for people across the world to collaborate on these kinds of cases.

Or, is it still really difficult from- from one company to talk to another company?

So, it's definitely possible.

It's definitely possible to discuss these kind of models with colleagues elsewhere

and to get the- get their take on what's

uh, on what to do.

How hard is it though?

I mean.

..

Do you see that happening?

I think that's- that's a place where it's important to gradually build trust between companies.

Because ultimately, all the AI developers are building technology which is be- going to be increasingly more powerful.

And so, it's.

..

The way to think about it is that ultimately we're all in it together.

Yeah, it's, uh, I tend to believe in the

uh, th- the better angels of our nature.

But I do hope that, um, that when you build a really powerful AI system in a particular domain

that you also think about the potential negative consequences of

um.

..

Yeah.

 It's an interesting and scary possibility that there will be a race for AI dev- AI development that would push people to close that development

and not share ideas with others.

I don't love this.

I've been in acad- a pure academic for 10 years.

I really like sharing ideas, and it's fun.

It's exciting.

What do you think it takes to.

..

Let's talk about AGI a little bit.

Wh- what do you think it takes to build a system of human-level intelligence?

We talked about reasoning.

We talked about long-term memory.

But in general, what does it take

do you think?

Well, I can't be sure, but I think that deep learning plus maybe another small idea.

Do you think self-play will be involved?

Sort of like, you've spoken about the powerful mechanism of self-play

where systems learn by sort of, uh

exploring the world in a competitive setting against other entities that are similarly skilled as them

and so incrementally improve in this way.

Do you think self-play will be a component of building an AGI system?

Yeah.

So, what I would say, to build AGI

I think is going to be deep learning plus some ideas.

And I think self-play will be one of those ideas.

I think that that is a very.

..

Self-play has this amazing property that it can surprise us in truly novel ways.

For example, like, we.

..

I mean, pretty much every self-play system

both our Dota bot.

..

I don't know if em- eh- OpenAI had a release about multi-agent

where you had two little agents who were playing hide and seek.

Mm-hmm.

And, of course, also AlphaZero.

They were all produced surprising behaviors.

# Chapter 6

exploring the world in a competitive setting against other entities that are similarly skilled as them

and so incrementally improve in this way.

Do you think self-play will be a component of building an AGI system?

Yeah.

So, what I would say, to build AGI

I think is going to be deep learning plus some ideas.

And I think self-play will be one of those ideas.

I think that that is a very.

..

Self-play has this amazing property that it can surprise us in truly novel ways.

For example, like, we.

..

I mean, pretty much every self-play system

both our Dota bot.

..

I don't know if em- eh- OpenAI had a release about multi-agent

where you had two little agents who were playing hide and seek.

Mm-hmm.

And, of course, also AlphaZero.

They were all produced surprising behaviors.

They all produced behaviors that we didn't expect.

They are creative solutions to problems.

And that seems like an important part of AGI that our systems don't exhibit routinely right now.

And so, that's why I like this area

I like this direction, because of its ability to surprise us.

To surprise us.

And an AG- And what- AGI system would surprise us fundamentally.

Yes.

But- and to be precise, not just a r- not just a random surprise

but to find a surprising solution to a problem that's also useful.

Right.

Now, a lot of the self-play mechanisms have been used in the game context

or at least in the simulation context.

W- how much, how much do- how far along the path to AGI do you think will be done in simulation?

How much faith, promise, do you have in simulation

versus having to have a system that operates in the real world

wheth- whether it's the real world of digital real world data or real world like actual physical world with robotics?

I don't think it's an either/or.

I think simulation is a tool, and it helps.

It has certain strengths and certain weaknesses, and we should use it.

Yeah, but- Okay.

.

..

uh, I understand that.

That's, um, that's true.

But one of the criticisms of self-play, one of the criticisms in reinforcement learning is one of the

the.

..

Its current power, its current results, while amazing

have been demonstrated in a simulated environments or very constrained physical environments.

Do you think it's possible to escape them

escape the simulated environments and be able to learn in non-simulated environments?

Or do you think it's possible to also just simulate in the photorealistic and physics realistic way the real world in a way that we can solve real problems with self-play in simulation?

So, I think that sim- transfer from simulation to the real world is definitely possible

and is- and has been exhibited many times in

by many different groups.

It's been especially successful in vision.

Also, OpenAI in the summer has demonstrated a robot hand which was trained entirely in simulation in a certain way that allowed for sim-to-real transfer to occur.

Is this, uh, for the Rubik's Cube?

Yeah, that's right.

And so that- I wasn't aware that was trained in simulation.

It was trained in simulation entirely.

R- really?

So, it wasn't in the phys- the

the hand wasn't trained?

No.

100% of the training was done in simulation.

And the policy that was learned in simulation was trained to be very adaptive

so adaptive that when you transfer it, it could very quickly adapt to the physical

to the physical world.

So, the kind of perturbations with the giraffe or whatever the heck it was

those weren't.

..

Were those part of the sim- simulation?

Well, the simulation was generally.

..

So, the s- the simulation was trained to be robust to many different things

but not the kind of perturbations we've had in the video.

So- I see.

.

.

it's never been trained with a glove.

It's never been trained with a, uh

uh, stuffed giraffe.

So, in theory, these are novel perturbations?

Correct.

It's not in theory, in practice, in pr- Uh

that those are novel perturbations?

Well, that's.

..

Okay.

Yeah.

That's a clean, small scale, but clean example of a transfer from the simulated world to the

to the physical world.

Yeah, and I will also say that I expect the transfer capabilities of deep learning to increase in general.

And the better the transfer capabilities are, the more useful simulation will become.

Because then you could take.

..

You could experience something in simulation, and then learn a moral of the story

which you could then carry with you to the real world.

Right.

As humans do all the time when they play computer games.

So, let me ask sort of a embodied question

staying on AGI for a sec.

Uh, do you think, uh, AGI system would need to have a body?

..

. we need to have some of those human elements of self-awareness

consciousness, sort of f- fear of mortality

sort of self-preservation in the physical space, which comes with having a body?

I think having a body will be useful.

I don't think it's necessary.

But I think it's very useful to have a body

for sure, because you can learn a whole new.

..

You- you can learn things which cannot be learned without a body.

But, at the same time, I think that you can co- if you don't have a body

you could compensate for it and still succeed.

You think so?

Yes.

Well, there is evidence for this.

For example, there are many people who were born deaf and blind

and they were able to compensate for the lack of modalities.

I'm thinking about Hel- Helen Keller specifically.

So, even if you're not able to physically interact with the world

and if you're not able to.

..

I mean, I actually was getting at.

..

Maybe let me ask on the more particular.

..

I'm not sure if it's connected to having a body or not

but, uh, the idea of consciousness, and a more constrained version of that is self-awareness.

Do you think an AGI system should have consciousness?

It's what.

..

We can't define con- whatever the heck you think consciousness is.

Yeah.

Hard question to answer, given how hard it is to define it.

Do you think it's useful to think about?

I mean, it's- it's- it's definitely interesting.

It's fascinating.

I think it's definitely possible that our systems will be conscious.

Do you think that's an emergent thing that just comes from.

..

Do you think consciousness could emerge from the representation that's stored within your networks?

So, like, that it naturally just emerges when you become more and more.

..

You're able to represent more and more of the world?

Well, let's say, I'd make the following argument

which is, humans are conscious.

And if you believe that artificial neural nets are sufficiently similar to the brain

then there- there should at least exist artificial neural nets who should be conscious

too.

 You're leaning on that existence proof pretty heavily.

Okay.

It- it- so- But it's- it's- So- so- .

..

that- that- that's the best answer I can give.

No, I- I know.

I know.

I know.

Um, there's still an open question if there's not some magic in the brain that we're not.

..

I mean, I don't mean a non-materialistic magic

but that, um- that the brain might be a lot more complicated and interesting than we give it credit for.

If that's the case, then it should show up

and at some point- At some point.

.

.

we will- we will find out if we can't continue to make progress.

It just- But I think- I think it's unlikely.

So, we talk about consciousness, but let me talk about another poorly defined concept of intelligence.

Again, we've talked about reasoning.

We've talked about memory.

What do you think is a good test of intelligence for you?

Are you impressed by the test that Alan Turing formulated with the imitation game of na- with natural language?

Is there something in your mind that you would be deeply impressed by if a system was able to do?

I mean, lots of things.

There's certain- there's a certain frontier- there is a certain frontier of capabilities today.

Yeah.

And there exists things outside of that frontier

and I would be impressed by any such thing.

Like, for example, I would be impressed by a deep learning system which solves a very pedestrian

you know, pedestrian task, like machine translation or computer vision task or something

which never makes mistake a human would make under any circumstances.

I think that is something which have not yet been demonstrated and I would find it very impressive.

Yeah.

So right now, they make mistakes in diff- they might be more accurate than human beings

but they still- they make a different set of mistakes.

So my- my- I would guess that a lot of the skepticism that some people have about deep learning is when they look at their mistakes and they say

"Well, those mistakes, they make no sense.

Like, if you understood the concept, you wouldn't make that mistake.

" Yes.

And I think that changing that would be- would- would- that would- that would inspire me.

That would be, yes, this is- this- this is- this is progress.

Yeah.

That's re- that's a really nice way to put it.

But I also just don't like that human instinct to criticize a model as not intelligent.

That's the same instinct as we do when we criticize any group of creatures as the other

because it's very possible that, uh, GPT-2 is much smarter than human beings at many things.

And- That's definitely true.

It has a lot more breadth of knowledge.

Yes.

Breadth of knowledge, and even- and even perhaps depth on certain topics.

It's kind of hard to judge what depth means

but there's definitely a sense in which humans don't make mistakes that these models do.

Yes.

The same is applied to autonomous vehicles.

The same is probably gonna continue being applied to a lot of artificial intelligence systems.

We find.

..

This is the annoying thing.

This is the process of.

..

In the 21st century, the process of analyzing the progress of AI is the search for one case where the system fails in a big way where humans would not

and then many people writing articles about it

and then broadly as a com- as a- the public generally gets convinced that the system is not intelligent.

And we, like, pacify ourselves by thinking it's not intelligent because of this one anecdotal case.

And this can- seems to continue happening.

Yeah.

I mean, there is truth to that.

Though there is peop- although I'm sure that plenty of people are also extremely impressed by the systems that exist today.

But I think this connects to the earlier point we discussed

that it's just confusing to judge progress in AI.

Yeah.

And, you know, you have a new robot demonstrating something.

How impressed should you be?

And I th- and I think that people will start to be impressed once AI starts to really move the needle on the GDP.

So, you're one of the people that might be able to create an AGI system here.

Not you, but you and OpenAI.

If- if you do create an AGI system

and you get to spend sort of the evening with it

him, her, what would you talk about

do you think?

..

. the very first time?

First time.

Well, the first time, I would just- I would just ask all kinds of questions and try to make it- to get it to make a mistake and I would be amazed that it doesn't make mistakes.

And I'd just keep- keep asking broad que- What- what- what kind of questions do you think

uh, would they be factual or would they be personal

emotional, psychological?

What do you think?

All of the above.

 Would you ask for advice?

Definitely.

 I mean, why- why would I limit myself- Yeah.

.

..

talking to a system like this?

Now, again, let me emphasize the fact that you truly are one of the people that might be in the room where this happens.

So let me ask a sort of a profound question about

um.

..

I've just talked to a Stalin historian,  I've been talking to a lot of people who are studying power.

Uh, Abraham Lincoln said, "Nearly all men can stand adversity

but if you want to test a man's character

give him power.

" I would say the power of the 21st century

maybe the 22nd, but hopefully the 21st

would be the creation of an AGI system and the people who have control

direct possession and control of the AGI system.

So what do you think, after spending that evening  having a discussion with the AGI system

what do you think you would do?

Well, the ideal world I'd like to imagine is one where humanity are like the board- the board members of a company where the AGI is the CEO.

So it would be.

..

I would like the- the picture which I would imagine is you have some kinda different entities

different countries or cities, and the people that live there vote for what the AGI that represents them should do.

And then the AGI that represents them goes and does it.

I think a picture like that, I find very appealing.

And you could have multiple A- you would have an AGI for a city

for a country, and it would be- it would be trying to

in effect, take the democratic process to the next level.

And the board can always fire the CEO?

Essentially.

Press the reset button, say.

Press the reset- Re- re-randomize the parameters, yeah.

Well, let me sort of.

..

That- that's actually.

..

Okay, that- that's a beautiful vision, I think

as long as it's possible to con- to press the reset button.

Do you think it will always be possible to press the reset button?

So I think that it def- it definitely will be possible to build.

So you're talking.

..

So the question that I really understand from you is will- will- will humans or

you know, humans people have control over the AI systems that they build?

Yes.

And my answer is, it's definitely possible to build AI systems which will want to be controlled by other humans.

Wow, that's part of their.

..

So it's not that just they can't help but be controlled

but that's- that's, um, the- they exist- th- one of the objectives of their existence is to be controlled?

In the same way that human parents generally want to help their children

they want their children to succeed.

It's not a burden for them.

They are excited to help the children and to feed them and to dress them and to take care of them.

And I believe, with high c- conviction

that the same will be possible for an AGI.

It will be possible to program an AGI

to design it in such a way that it will have a similar deep drive that it will be delighted to fulfill.

And the drive will be to help humans flourish.

But let me take a step back to that moment where you create the AGI system.

I think this is a really crucial moment.

And between that moment and the- the democratic board members with the AGI at the head

there has to be a relinquishing of power.

So as George Washington, despite all the bad things he did

one of the big things he did is he relinquished power.

He, first of all, didn't want to be president 

and even when he became president, he gave- he didn't keep just serving as most dictators do for indefinitely.

Do you see yourself being able to relinquish control over an AGI system given how much power you can have over the world?

At first, financial, just make a lot of money

right?

And then control by having possession as AGI system.

I- I- I'd find it trivial to do that.

I'd find it trivial to, like, relinquish this- this kind of po- I mean

# Chapter 7

They are excited to help the children and to feed them and to dress them and to take care of them.

And I believe, with high c- conviction

that the same will be possible for an AGI.

It will be possible to program an AGI

to design it in such a way that it will have a similar deep drive that it will be delighted to fulfill.

And the drive will be to help humans flourish.

But let me take a step back to that moment where you create the AGI system.

I think this is a really crucial moment.

And between that moment and the- the democratic board members with the AGI at the head

there has to be a relinquishing of power.

So as George Washington, despite all the bad things he did

one of the big things he did is he relinquished power.

He, first of all, didn't want to be president 

and even when he became president, he gave- he didn't keep just serving as most dictators do for indefinitely.

Do you see yourself being able to relinquish control over an AGI system given how much power you can have over the world?

At first, financial, just make a lot of money

right?

And then control by having possession as AGI system.

I- I- I'd find it trivial to do that.

I'd find it trivial to, like, relinquish this- this kind of po- I mean

you know, the- the kind of scenario you are describing sounds terrifying to me.

That's all.

I would absolutely not want to be in that position.

 Do you think you represent the majority or the minority of people in the AI community?

Well, I- I mean, I- It's a open question

an important one.

"Are most people good?

" is another way to ask it .

So I don't know if most people are good

but I think that when it really counts

people can be better than we think.

That is beautifully put, yeah.

Are there specific mechanism you can think of of aligning AI gene values to human values?

Is that.

..

Do you think about these problems of continued alignment as we develop the AI systems?

Yeah, definitely.

In some sense, the kinda question which you are asking is.

..

So if I were to translate that question to today's terms- Yes.

.

..

it would be a question about how to get an RL agent that's optimizing a value function which itself has learned.

And if you look at humans, humans are like that

because the reward function, the value function of humans is not external

it is internal.

That's right.

And.

..

there are definite ideas of how to train a value function.

Basically, an objective, you know, a- as objective as possible perception system that will be trained separately to recognize

to internalize human judgments on different situations, and then that component would then be integrated as the value

as the base value function for some more

more capable RL system.

You could imagine a process like this.

I'm not saying this is the process.

I'm saying this is an example of the kind of thing you could do.

So, o- on that topic of the objective functions of human existence

what do you, what do you think is the objective function that's implicit in human existence?

What's the meaning of life?

Oh.

..

I think the question is w- is, is wrong in some way.

I think that the question implies that there is an ex- there is an objective answer

which is an external answer, you know.

Your meaning of life is X.

Right.

I think what's going on is that we exist

and that's amazing, and we should try to make the most of it

and try to maximize our own value and enjoyment of a very short time while we do exist.

It's, it's funny, because action does require an objective function.

It's definitely there s- in some form, but it's difficult to make it explicit

and maybe impossible to make it explicit, I guess is what you're getting at.

And that's an interesting fact of an RL environment .

Well, what.

..

N- I was making a slightly different point

is that humans want things, and their wants create the drives that cause them to.

..

You know, our wants are our objective functions

our individual objective functions.

We can later decide that we want to change

that what we wanted before is no longer good and we want something else.

Yeah, but they're so dynamic.

The- there's got to be some underlying, sort of Freud.

..

There's, uh, there's like sexual stuff.

There's people who think it's the fear of

fear of death, and there's also, uh

the desire for knowledge and, you know

all these kinds of things.

Uh, procreation.

Th- the sort of all the evolutionary arguments.

There seems to be.

..

There might be some kind of fundamental objective function from

uh, from which everything else, um, emerges.

But it seems like it's, that's very difficult to make explicit.

I mean, I think, I think, I think that probably is an evolutionary objective function

which is to survive and procreate and make sh- make your children succeed.

That would be my guess.

But it doesn't give an answer to the question of what's the meaning of life.

I think you can see how humans are part of this big process

this ancient process.

We are o- we are.

..

We exist on a small planet, and that's it.

So given that we exist, try to make the most of it

and try to enjoy more and suffer less as much as we can.

Let me ask two silly questions about life.

One, do you have regrets?

Moments that if you, uh, went back

you would do differently?

And two, are there moments that you're especially proud of

that made you truly happy?

So I can answer that.

I can answer both questions.

 Of c- of course, there are m- there's a huge number of choices and decisions that I've made that

with the benefit of hindsight, I wouldn't have made them

and I do experience some regret.

But, you know, I try to take solace in the knowledge that

at the time, I did the best I could.

And in terms of things that I'm proud of

there are.

..

I'm very fortunate to have things I'm pro- to have done things I'm proud of

and they made me happy for m- for some time

but I don't think that that is the source of happiness.

So your academic accomplishments, all the papers

you're one of the most cited people in the world

all of the breakthroughs I mentioned in computer vision and language and so on.

Is.

..

What is the source of happiness and pride for you?

I mean, all those things are a source of pride

for sure.

I'm very grateful for having done all those things

and it was very fun to do them.

But happiness comes.

..

But, you know, you can.

..

Ha- happiness.

..

Well, my current view is that happiness comes from our.

..

To a large, to a very large degree

from the way we look at things.

You know, you can have a simple meal and be quite happy as a result

or you can talk to someone and be happy as a result as well.

Or, con- conversely, you can have a meal and be disappointed that the meal wasn't a better meal.

So I think hap- a lot of happiness comes from that.

But I'm not sure.

I don't want to be too confident.

I.

..

 Being humble in the face of the uncertainty seems to be also a part of this whole happiness thing.

Well, I don't think there's a better way to end it than

uh, meaning of life and discussions of happiness.

So, Ilya, thank you so much.

You've given me a few incredible ideas.

You've given the world many incredible ideas.

I really appreciate it, and thanks for talking today.

Yeah.

Thanks for stop- stopping by.

I really enjoyed it.

Thanks for listening to this conversation with Ilya Sutskever

and thank you to our presenting sponsor, Cash App.

Please consider supporting the podcast by downloading Cash App and using code LEXPODCAST.

If you enjoy this podcast, subscribe on YouTube

review it with five stars on Apple Podcasts

support it on Patreon, or simply connect with me on Twitter @LexFridman.

And now, let me leave you with some words from Alan Turing on machine learning.

"Instead of trying to produce a program to simulate the adult mind

why not rather try to produce one which simulates the child's?

If this were then subjected to an appropriate course of education

one would obtain the adult brain.

" Thank you for listening, and hope to see you next time.

