# Chapter 1

- I see the danger of this concentration of power

through proprietary AI systems

as a much bigger danger than everything else.

What works against this

is people who think that for reasons of security,

we should keep AI systems under lock and key

because it's too dangerous

to put it in the hands of everybody.

That would lead to a very bad future

in which all of our information diet

is controlled by a small number of companies

through proprietary systems.

- I believe that people are fundamentally good

and so if AI, especially open source AI

can make them smarter,

it just empowers the goodness in humans.

- So I share that feeling.

Okay?

I think people are fundamentally good. (laughing)

And in fact a lot of doomers are doomers

because they don't think that people are fundamentally good.

- The following is a conversation with Yann LeCun,

his third time on this podcast.

He is the chief AI scientist at Meta,

professor at NYU,

Turing Award winner

and one of the seminal figures

in the history of artificial intelligence.

He and Meta AI

have been big proponents of open sourcing AI development,

and have been walking the walk

by open sourcing many of their biggest models,

including LLaMA 2 and eventually LLaMA 3.

Also, Yann has been an outspoken critic

of those people in the AI community

who warn about the looming danger

and existential threat of AGI.

He believes the AGI will be created one day,

but it will be good.

It will not escape human control

nor will it dominate and kill all humans.

At this moment of rapid AI development,

this happens to be somewhat a controversial position.

And so it's been fun

seeing Yann get into a lot of intense

and fascinating discussions online

as we do in this very conversation.

This is the Lex Fridman podcast.

To support it,

please check out our sponsors in the description.

And now, dear friends, here's Yann LeCun.

You've had some strong statements,

technical statements

about the future of artificial intelligence recently,

throughout your career actually but recently as well.

You've said that autoregressive LLMs

are not the way we're going to make progress

towards superhuman intelligence.

These are the large language models

like GPT-4, like LLaMA 2 and 3 soon and so on.

How do they work

and why are they not going to take us all the way?

- For a number of reasons.

The first is that there is a number of characteristics

of intelligent behavior.

For example, the capacity to understand the world,

understand the physical world,

the ability to remember and retrieve things,

persistent memory,

the ability to reason and the ability to plan.

Those are four essential characteristic

of intelligent systems or entities,

humans, animals.

LLMs can do none of those,

or they can only do them in a very primitive way.

And they don't really understand the physical world,

they don't really have persistent memory,

they can't really reason

and they certainly can't plan.

And so if you expect the system to become intelligent

just without having the possibility of doing those things,

you're making a mistake.

That is not to say that autoregressive LLMs are not useful,

they're certainly useful.

That they're not interesting,

that we can't build

a whole ecosystem of applications around them,

of course we can.

But as a path towards human level intelligence,

they're missing essential components.

And then there is another tidbit or fact

that I think is very interesting;

those LLMs are trained on enormous amounts of text.

Basically the entirety

of all publicly available text on the internet, right?

That's typically on the order of 10 to the 13 tokens.

Each token is typically two bytes.

So that's two 10 to the 13 bytes as training data.

It would take you or me 170,000 years

to just read through this at eight hours a day. (laughs)

So it seems like an enormous amount of knowledge, right?

That those systems can accumulate.

But then you realize it's really not that much data.

If you talk to developmental psychologists,

and they tell you a 4-year-old

has been awake for 16,000 hours in his or her life,

and the amount of information

that has reached the visual cortex of that child

in four years

is about 10 to 15 bytes.

And you can compute this

by estimating that the optical nerve

carry about 20 megabytes per second, roughly.

And so 10 to the 15 bytes for a 4-year-old

versus two times 10 to the 13 bytes

for 170,000 years worth of reading.

What that tells you is that through sensory input,

we see a lot more information

than we do through language.

And that despite our intuition,

most of what we learn and most of our knowledge

is through our observation and interaction

with the real world,

not through language.

Everything that we learn in the first few years of life,

and certainly everything that animals learn

has nothing to do with language.

- So it would be good

to maybe push against some of the intuition

behind what you're saying.

So it is true there's several orders of magnitude

more data coming into the human mind, much faster,

and the human mind is able to learn very quickly from that,

filter the data very quickly.

Somebody might argue

your comparison between sensory data versus language.

That language is already very compressed.

It already contains a lot more information

than the bytes it takes to store them,

if you compare it to visual data.

So there's a lot of wisdom in language.

There's words and the way we stitch them together,

it already contains a lot of information.

So is it possible that language alone

already has enough wisdom and knowledge in there

to be able to, from that language construct a world model

and understanding of the world,

an understanding of the physical world

that you're saying LLMs lack?

- So it's a big debate among philosophers

and also cognitive scientists,

like whether intelligence needs to be grounded in reality.

I'm clearly in the camp

that yes, intelligence cannot appear

without some grounding in some reality.

It doesn't need to be physical reality,

it could be simulated

but the environment is just much richer

than what you can express in language.

Language is a very approximate representation or percepts

and or mental models, right?

I mean, there's a lot of tasks that we accomplish

where we manipulate a mental model of the situation at hand,

and that has nothing to do with language.

Everything that's physical, mechanical, whatever,

when we build something,

when we accomplish a task,

a moderate task of grabbing something, et cetera,

we plan our action sequences,

and we do this

by essentially imagining the result

of the outcome of sequence of actions that we might imagine.

And that requires mental models

that don't have much to do with language.

And that's, I would argue,

most of our knowledge

is derived from that interaction with the physical world.

So a lot of my colleagues

who are more interested in things like computer vision

are really on that camp

that AI needs to be embodied, essentially.

And then other people coming from the NLP side

or maybe some other motivation

don't necessarily agree with that.

And philosophers are split as well.

And the complexity of the world is hard to imagine.

It's hard to represent all the complexities

that we take completely for granted in the real world

that we don't even imagine require intelligence, right?

This is the old Moravec's paradox

from the pioneer of robotics, Hans Moravec,

who said, how is it that with computers,

it seems to be easy to do high level complex tasks

like playing chess and solving integrals

and doing things like that,

whereas the thing we take for granted that we do every day,

like, I don't know, learning to drive a car

or grabbing an object,

we can't do with computers. (laughs)

And we have LLMs that can pass the bar exam,

so they must be smart.

But then they can't launch a drive in 20 hours

like any 17-year-old.

They can't learn to clear out the dinner table

and fill out the dishwasher

like any 10-year-old can learn in one shot.

Why is that?

Like what are we missing?

What type of learning

or reasoning architecture or whatever are we missing

that basically prevent us

from having level five self-driving cars

and domestic robots?

- Can a large language model construct a world model

that does know how to drive

and does know how to fill a dishwasher,

but just doesn't know

how to deal with visual data at this time?

So it can operate in a space of concepts.

- So yeah, that's what a lot of people are working on.

So the answer,

the short answer is no.

And the more complex answer is

you can use all kind of tricks

to get an LLM to basically digest visual representations

of images or video or audio for that matter.

And a classical way of doing this

is you train a vision system in some way,

and we have a number of ways to train vision systems,

either supervised, unsupervised, self-supervised,

all kinds of different ways.

That will turn any image into a high level representation.

Basically, a list of tokens

that are really similar to the kind of tokens

that a typical LLM takes as an input.

And then you just feed that to the LLM

in addition to the text,

and you just expect the LLM during training

to kind of be able to use those representations

to help make decisions.

I mean, there's been work along those lines

for quite a long time.

And now you see those systems, right?

I mean, there are LLMs that have some vision extension.

But they're basically hacks

in the sense that those things

are not like trained to handle,

to really understand the world.

They're not trained with video, for example.

They don't really understand intuitive physics,

at least not at the moment.

- So you don't think

there's something special to you about intuitive physics,

about sort of common sense reasoning

about the physical space, about physical reality?

That to you is a giant leap

that LLMs are just not able to do?

- We're not gonna be able to do this

with the type of LLMs that we are working with today.

And there's a number of reasons for this,

but the main reason is

the way LLMs are trained is that you take a piece of text,

you remove some of the words in that text, you mask them,

you replace them by black markers,

and you train a gigantic neural net

to predict the words that are missing.

And if you build this neural net in a particular way

so that it can only look at words

that are to the left of the one it's trying to predict,

then what you have is a system

that basically is trying to predict

the next word in a text, right?

So then you can feed it a text, a prompt,

and you can ask it to predict the next word.

It can never predict the next word exactly.

And so what it's gonna do

is produce a probability distribution

of all the possible words in the dictionary.

In fact, it doesn't predict words,

it predicts tokens that are kind of subword units.

And so it's easy to handle the uncertainty

in the prediction there

because there's only a finite number

of possible words in the dictionary,

and you can just compute a distribution over them.

Then what the system does

is that it picks a word from that distribution.

Of course, there's a higher chance of picking words

that have a higher probability within that distribution.

So you sample from that distribution

to actually produce a word,

and then you shift that word into the input.

And so that allows the system now

to predict the second word, right?

And once you do this,

you shift it into the input, et cetera.

That's called autoregressive prediction,

which is why those LLMs

should be called autoregressive LLMs,

but we just call them at LLMs.

And there is a difference between this kind of process

and a process by which before producing a word,

when you talk.

When you and I talk,

you and I are bilinguals.

We think about what we're gonna say,

and it's relatively independent

of the language in which we're gonna say.

When we talk about like, I don't know,

let's say a mathematical concept or something.

The kind of thinking that we're doing

and the answer that we're planning to produce

is not linked to whether we're gonna say it

in French or Russian or English.

- Chomsky just rolled his eyes, but I understand.

So you're saying that there's a bigger abstraction

that goes before language-

- [Yann] Yeah. - And maps onto language.

- Right.

It's certainly true for a lot of thinking that we do.

- Is that obvious that we don't?

Like you're saying your thinking is same in French

as it is in English?

- Yeah, pretty much.

- Pretty much or is this...

Like how flexible are you,

like if there's a probability distribution?

(both laugh)

- Well, it depends what kind of thinking, right?

If it's like producing puns,

I get much better in French than English about that (laughs)

or much worse-

- Is there an abstract representation of puns?

# Chapter 2

in French or Russian or English.

- Chomsky just rolled his eyes, but I understand.

So you're saying that there's a bigger abstraction

that goes before language-

- [Yann] Yeah. - And maps onto language.

- Right.

It's certainly true for a lot of thinking that we do.

- Is that obvious that we don't?

Like you're saying your thinking is same in French

as it is in English?

- Yeah, pretty much.

- Pretty much or is this...

Like how flexible are you,

like if there's a probability distribution?

(both laugh)

- Well, it depends what kind of thinking, right?

If it's like producing puns,

I get much better in French than English about that (laughs)

or much worse-

- Is there an abstract representation of puns?

Like is your humor an abstract...

Like when you tweet

and your tweets are sometimes a little bit spicy,

is there an abstract representation in your brain of a tweet

before it maps onto English?

- There is an abstract representation

of imagining the reaction of a reader to that text.

- Oh, you start with laughter

and then figure out how to make that happen?

- Figure out like a reaction you wanna cause

and then figure out how to say it

so that it causes that reaction.

But that's like really close to language.

But think about like a mathematical concept

or imagining something you want to build out of wood

or something like this, right?

The kind of thinking you're doing

has absolutely nothing to do with language, really.

Like it's not like you have necessarily

like an internal monologue in any particular language.

You're imagining mental models of the thing, right?

I mean, if I ask you to like imagine

what this water bottle will look like

if I rotate it 90 degrees,

that has nothing to do with language.

And so clearly

there is a more abstract level of representation

in which we do most of our thinking

and we plan what we're gonna say

if the output is uttered words

as opposed to an output being muscle actions, right?

We plan our answer before we produce it.

And LLMs don't do that,

they just produce one word after the other,

instinctively if you want.

It's a bit like the subconscious actions where you don't...

Like you're distracted.

You're doing something,

you're completely concentrated

and someone comes to you and asks you a question.

And you kind of answer the question.

You don't have time to think about the answer,

but the answer is easy

so you don't need to pay attention

and you sort of respond automatically.

That's kind of what an LLM does, right?

It doesn't think about its answer, really.

It retrieves it because it's accumulated a lot of knowledge,

so it can retrieve some things,

but it's going to just spit out one token after the other

without planning the answer.

- But you're making it sound just one token after the other,

one token at a time generation is bound to be simplistic.

But if the world model is sufficiently sophisticated,

that one token at a time,

the most likely thing it generates as a sequence of tokens

is going to be a deeply profound thing.

- Okay.

But then that assumes that those systems

actually possess an internal world model.

- So it really goes to the...

I think the fundamental question is

can you build a really complete world model?

Not complete,

but one that has a deep understanding of the world.

- Yeah.

So can you build this first of all by prediction?

- [Lex] Right.

- And the answer is probably yes.

Can you build it by predicting words?

And the answer is most probably no,

because language is very poor in terms of...

Or weak or low bandwidth if you want,

there's just not enough information there.

So building world models means observing the world

and understanding why the world is evolving the way it is.

And then the extra component of a world model

is something that can predict

how the world is going to evolve

as a consequence of an action you might take, right?

So one model really is,

here is my idea of the state of the world at time T,

here is an action I might take.

What is the predicted state of the world

at time T plus one?

Now, that state of the world

does not need to represent everything about the world,

it just needs to represent

enough that's relevant for this planning of the action,

but not necessarily all the details.

Now, here is the problem.

You're not going to be able to do this

with generative models.

So a generative model that's trained on video,

and we've tried to do this for 10 years.

You take a video,

show a system a piece of video

and then ask you to predict the reminder of the video.

Basically predict what's gonna happen.

- One frame at a time.

Do the same thing as sort of the autoregressive LLMs do,

but for video.

- Right.

Either one frame at a time or a group of frames at a time.

But yeah, a large video model, if you want. (laughing)

The idea of doing this

has been floating around for a long time.

And at FAIR,

some colleagues and I

have been trying to do this for about 10 years.

And you can't really do the same trick as with LLMs,

because LLMs, as I said,

you can't predict exactly which word is gonna follow

a sequence of words,

but you can predict the distribution of the words.

Now, if you go to video,

what you would have to do

is predict the distribution

of all possible frames in a video.

And we don't really know how to do that properly.

We do not know how to represent distributions

over high dimensional continuous spaces

in ways that are useful.

And there lies the main issue.

And the reason we can do this

is because the world

is incredibly more complicated and richer

in terms of information than text.

Text is discreet.

Video is high dimensional and continuous.

A lot of details in this.

So if I take a video of this room,

and the video is a camera panning around,

there is no way I can predict

everything that's gonna be in the room as I pan around,

the system cannot predict what's gonna be in the room

as the camera is panning.

Maybe it's gonna predict,

this is a room where there's a light and there is a wall

and things like that.

It can't predict what the painting of the wall looks like

or what the texture of the couch looks like.

Certainly not the texture of the carpet.

So there's no way it can predict all those details.

So the way to handle this

is one way to possibly to handle this,

which we've been working for a long time,

is to have a model that has what's called a latent variable.

And the latent variable is fed to a neural net,

and it's supposed to represent

all the information about the world

that you don't perceive yet.

And that you need to augment the system

for the prediction to do a good job at predicting pixels,

including the fine texture of the carpet and the couch

and the painting on the wall.

That has been a complete failure, essentially.

And we've tried lots of things.

We tried just straight neural nets,

we tried GANs,

we tried VAEs,

all kinds of regularized auto encoders,

we tried many things.

We also tried those kind of methods

to learn good representations of images or video

that could then be used as input

for example, an image classification system.

And that also has basically failed.

Like all the systems that attempt to predict missing parts

of an image or a video

from a corrupted version of it, basically.

So, right, take an image or a video,

corrupt it or transform it in some way,

and then try to reconstruct the complete video or image

from the corrupted version.

And then hope that internally,

the system will develop good representations of images

that you can use for object recognition,

segmentation, whatever it is.

That has been essentially a complete failure.

And it works really well for text.

That's the principle that is used for LLMs, right?

- So where's the failure exactly?

Is it that it is very difficult to form

a good representation of an image,

like a good embedding

of all the important information in the image?

Is it in terms of the consistency

of image to image to image to image that forms the video?

If we do a highlight reel of all the ways you failed.

What's that look like?

- Okay.

So the reason this doesn't work is...

First of all, I have to tell you exactly what doesn't work

because there is something else that does work.

So the thing that does not work

is training the system to learn representations of images

by training it to reconstruct a good image

from a corrupted version of it.

Okay.

That's what doesn't work.

And we have a whole slew of techniques for this

that are variant of then using auto encoders.

Something called MAE,

developed by some of my colleagues at FAIR,

masked autoencoder.

So it's basically like the LLMs or things like this

where you train the system by corrupting text,

except you corrupt images.

You remove patches from it

and you train a gigantic neural network to reconstruct.

The features you get are not good.

And you know they're not good

because if you now train the same architecture,

but you train it to supervise with label data,

with textual descriptions of images, et cetera,

you do get good representations.

And the performance on recognition tasks is much better

than if you do this self supervised free training.

- So the architecture is good.

- The architecture is good.

The architecture of the encoder is good.

Okay?

But the fact that you train the system to reconstruct images

does not lead it to produce

long good generic features of images.

- [Lex] When you train it in a self supervised way.

- Self supervised by reconstruction.

- [Lex] Yeah, by reconstruction.

- Okay, so what's the alternative?

(both laugh)

The alternative is joint embedding.

- What is joint embedding?

What are these architectures that you're so excited about?

- Okay, so now instead of training a system

to encode the image

and then training it to reconstruct the full image

from a corrupted version,

you take the full image,

you take the corrupted or transformed version,

you run them both through encoders,

which in general are identical but not necessarily.

And then you train a predictor on top of those encoders

to predict the representation of the full input

from the representation of the corrupted one.

Okay?

So joint embedding,

because you're taking the full input

and the corrupted version or transformed version,

run them both through encoders

so you get a joint embedding.

And then you're saying

can I predict the representation of the full one

from the representation of the corrupted one?

Okay?

And I call this a JEPA,

so that means joint embedding predictive architecture

because there's joint embedding

and there is this predictor

that predicts the representation

of the good guy from the bad guy.

And the big question is

how do you train something like this?

And until five years ago or six years ago,

we didn't have particularly good answers

for how you train those things,

except for one called contrastive learning.

And the idea of contrastive learning

is you take a pair of images

that are, again, an image and a corrupted version

or degraded version somehow

or transformed version of the original one.

And you train the predicted representation

to be the same as that.

If you only do this,

this system collapses.

It basically completely ignores the input

and produces representations that are constant.

So the contrastive methods avoid this.

And those things have been around since the early '90s,

I had a paper on this in 1993,

is you also show pairs of images that you know are different

and then you push away the representations from each other.

So you say not only do representations of things

that we know are the same,

should be the same or should be similar,

but representation of things that we know are different

should be different.

And that prevents the collapse,

but it has some limitation.

And there's a whole bunch of techniques

that have appeared over the last six, seven years

that can revive this type of method.

Some of them from FAIR,

some of them from Google and other places.

But there are limitations to those contrastive methods.

What has changed in the last three, four years

is now we have methods that are non-contrastive.

So they don't require those negative contrastive samples

of images that we know are different.

You train them only with images

that are different versions

or different views of the same thing.

And you rely on some other tweaks

to prevent the system from collapsing.

And we have half a dozen different methods for this now.

- So what is the fundamental difference

between joint embedding architectures and LLMs?

So can JEPA take us to AGI?

Whether we should say that you don't like the term AGI

and we'll probably argue,

I think every single time I've talked to you

we've argued about the G in AGI.

- [Yann] Yes.

- I get it, I get it, I get it. (laughing)

Well we'll probably continue to argue about it.

It's great.

Because you're like French,

and ami is I guess friend in French-

- [Yann] Yes.

- And AMI stands for advanced machine intelligence-

- [Yann] Right.

- But either way, can JEPA take us to that,

towards that advanced machine intelligence?

- Well, so it's a first step.

Okay?

So first of all, what's the difference

with generative architectures like LLMs?

So LLMs or vision systems that are trained by reconstruction

generate the inputs, right?

They generate the original input

that is non-corrupted, non-transformed, right?

So you have to predict all the pixels.

And there is a huge amount of resources spent in the system

to actually predict all those pixels, all the details.

In a JEPA, you're not trying to predict all the pixels,

you're only trying to predict

an abstract representation of the inputs, right?

And that's much easier in many ways.

So what the JEPA system

when it's being trained is trying to do,

is extract as much information as possible from the input,

but yet only extract information

that is relatively easily predictable.

# Chapter 3

- Well, so it's a first step.

Okay?

So first of all, what's the difference

with generative architectures like LLMs?

So LLMs or vision systems that are trained by reconstruction

generate the inputs, right?

They generate the original input

that is non-corrupted, non-transformed, right?

So you have to predict all the pixels.

And there is a huge amount of resources spent in the system

to actually predict all those pixels, all the details.

In a JEPA, you're not trying to predict all the pixels,

you're only trying to predict

an abstract representation of the inputs, right?

And that's much easier in many ways.

So what the JEPA system

when it's being trained is trying to do,

is extract as much information as possible from the input,

but yet only extract information

that is relatively easily predictable.

Okay.

So there's a lot of things in the world

that we cannot predict.

Like for example, if you have a self driving car

driving down the street or road.

There may be trees around the road.

And it could be a windy day,

so the leaves on the tree are kind of moving

in kind of semi chaotic random ways

that you can't predict and you don't care,

you don't want to predict.

So what you want is your encoder

to basically eliminate all those details.

It'll tell you there's moving leaves,

but it's not gonna keep the details

of exactly what's going on.

And so when you do the prediction in representation space,

you're not going to have to predict

every single pixel of every leaf.

And that not only is a lot simpler,

but also it allows the system

to essentially learn an abstract representation of the world

where what can be modeled and predicted is preserved

and the rest is viewed as noise

and eliminated by the encoder.

So it kind of lifts the level of abstraction

of the representation.

If you think about this,

this is something we do absolutely all the time.

Whenever we describe a phenomenon,

we describe it at a particular level of abstraction.

And we don't always describe every natural phenomenon

in terms of quantum field theory, right?

That would be impossible, right?

So we have multiple levels of abstraction

to describe what happens in the world.

Starting from quantum field theory

to like atomic theory and molecules in chemistry,

materials,

all the way up to kind of concrete objects in the real world

and things like that.

So we can't just only model everything at the lowest level.

And that's what the idea of JEPA is really about.

Learn abstract representation in a self supervised manner.

And you can do it hierarchically as well.

So that I think is an essential component

of an intelligent system.

And in language, we can get away without doing this

because language is already to some level abstract

and already has eliminated a lot of information

that is not predictable.

And so we can get away without doing the joint embedding,

without lifting the abstraction level

and by directly predicting words.

- So joint embedding.

It's still generative,

but it's generative in this abstract representation space.

- [Yann] Yeah.

- And you're saying language,

we were lazy with language

'cause we already got the abstract representation for free

and now we have to zoom out,

actually think about generally intelligent systems,

we have to deal with the full mess

of physical of reality, of reality.

And you do have to do this step

of jumping from the full, rich, detailed reality

to an abstract representation of that reality

based on what you can then reason

and all that kind of stuff.

- Right.

And the thing is those self supervised algorithms

that learn by prediction,

even in representation space,

they learn more concept

if the input data you feed them is more redundant.

The more redundancy there is in the data,

the more they're able to capture

some internal structure of it.

And so there,

there is way more redundancy in the structure

in perceptual inputs, sensory input like vision,

than there is in text,

which is not nearly as redundant.

This is back to the question you were asking

a few minutes ago.

Language might represent more information really

because it's already compressed,

you're right about that.

But that means it's also less redundant.

And so self supervised only will not work as well.

- Is it possible to join

the self supervised training on visual data

and self supervised training on language data?

There is a huge amount of knowledge

even though you talk down about those 10 to the 13 tokens.

Those 10 to the 13 tokens

represent the entirety,

a large fraction of what us humans have figured out.

Both the shit talk on Reddit

and the contents of all the books and the articles

and the full spectrum of human intellectual creation.

So is it possible to join those two together?

- Well, eventually, yes,

but I think if we do this too early,

we run the risk of being tempted to cheat.

And in fact, that's what people are doing at the moment

with vision language model.

We're basically cheating.

We are using language as a crutch

to help the deficiencies of our vision systems

to kind of learn good representations from images and video.

And the problem with this

is that we might improve our vision language system a bit,

I mean our language models by feeding them images.

But we're not gonna get to the level

of even the intelligence

or level of understanding of the world

of a cat or a dog which doesn't have language.

They don't have language

and they understand the world much better than any LLM.

They can plan really complex actions

and sort of imagine the result of a bunch of actions.

How do we get machines to learn that

before we combine that with language?

Obviously, if we combine this with language,

this is gonna be a winner,

but before that we have to focus

on like how do we get systems to learn how the world works?

- So this kind of joint embedding predictive architecture,

for you, that's gonna be able to learn

something like common sense,

something like what a cat uses

to predict how to mess with its owner most optimally

by knocking over a thing.

- That's the hope.

In fact, the techniques we're using are non-contrastive.

So not only is the architecture non-generative,

the learning procedures we're using are non-contrastive.

We have two sets of techniques.

One set is based on distillation

and there's a number of methods that use this principle.

One by DeepMind called BYOL.

A couple by FAIR,

one called VICReg and another one called I-JEPA.

And VICReg, I should say,

is not a distillation method actually,

but I-JEPA and BYOL certainly are.

And there's another one also called DINO or Dino,

also produced at FAIR.

And the idea of those things

is that you take the full input, let's say an image.

You run it through an encoder,

produces a representation.

And then you corrupt that input or transform it,

run it through essentially what amounts to the same encoder

with some minor differences.

And then train a predictor.

Sometimes a predictor is very simple,

sometimes it doesn't exist.

But train a predictor to predict a representation

of the first uncorrupted input from the corrupted input.

But you only train the second branch.

You only train the part of the network

that is fed with the corrupted input.

The other network, you don't train.

But since they share the same weight,

when you modify the first one,

it also modifies the second one.

And with various tricks,

you can prevent the system from collapsing

with the collapse of the type I was explaining before

where the system basically ignores the input.

So that works very well.

The two techniques we've developed at FAIR,

DINO and I-JEPA work really well for that.

- So what kind of data are we talking about here?

- So there's several scenarios.

One scenario is you take an image,

you corrupt it by changing the cropping, for example,

changing the size a little bit,

maybe changing the orientation, blurring it,

changing the colors,

doing all kinds of horrible things to it-

- But basic horrible things.

- Basic horrible things

that sort of degrade the quality a little bit

and change the framing,

crop the image.

And in some cases, in the case of I-JEPA,

you don't need to do any of this,

you just mask some parts of it, right?

You just basically remove some regions

like a big block, essentially.

And then run through the encoders

and train the entire system,

encoder and predictor,

to predict the representation of the good one

from the representation of the corrupted one.

So that's the I-JEPA.

It doesn't need to know that it's an image, for example,

because the only thing it needs to know

is how to do this masking.

Whereas with DINO,

you need to know it's an image

because you need to do things

like geometry transformation and blurring

and things like that that are really image specific.

A more recent version of this that we have is called V-JEPA.

So it's basically the same idea as I-JEPA

except it's applied to video.

So now you take a whole video

and you mask a whole chunk of it.

And what we mask is actually kind of a temporal tube.

So like a whole segment of each frame in the video

over the entire video.

- And that tube is like statically positioned

throughout the frames?

It's literally just a straight tube?

- Throughout the tube, yeah.

Typically it's 16 frames or something,

and we mask the same region over the entire 16 frames.

It's a different one for every video, obviously.

And then again, train that system

so as to predict the representation of the full video

from the partially masked video.

And that works really well.

It's the first system that we have

that learns good representations of video

so that when you feed those representations

to a supervised classifier head,

it can tell you what action is taking place in the video

with pretty good accuracy.

So it's the first time we get something of that quality.

- So that's a good test

that a good representation is formed.

That means there's something to this.

- Yeah.

We also preliminary result

that seem to indicate

that the representation allows our system to tell

whether the video is physically possible

or completely impossible

because some object disappeared

or an object suddenly jumped from one location to another

or changed shape or something.

- So it's able to capture some physics based constraints

about the reality represented in the video?

- [Yann] Yeah.

- About the appearance and the disappearance of objects?

- Yeah.

That's really new.

- Okay, but can this actually

get us to this kind of world model

that understands enough about the world

to be able to drive a car?

- Possibly.

And this is gonna take a while

before we get to that point.

And there are systems already, robotic systems,

that are based on this idea.

What you need for this

is a slightly modified version of this

where imagine that you have a video,

a complete video,

and what you're doing to this video

is that you are either translating it in time

towards the future.

So you'll only see the beginning of the video,

but you don't see the latter part of it

that is in the original one.

Or you just mask the second half of the video, for example.

And then you train this I-JEPA system

or the type I described,

to predict representation of the full video

from the shifted one.

But you also feed the predictor with an action.

For example, the wheel is turned

10 degrees to the right or something, right?

So if it's a dash cam in a car

and you know the angle of the wheel,

you should be able to predict to some extent

what's going to happen to what you see.

You're not gonna be able to predict all the details

of objects that appear in the view, obviously,

but at an abstract representation level,

you can probably predict what's gonna happen.

So now what you have is an internal model

that says, here is my idea

of the state of the world at time T,

here is an action I'm taking,

here is a prediction

of the state of the world at time T plus one,

T plus delta T,

T plus two seconds, whatever it is.

If you have a model of this type,

you can use it for planning.

So now you can do what LLMs cannot do,

which is planning what you're gonna do

so as you arrive at a particular outcome

or satisfy a particular objective, right?

So you can have a number of objectives, right?

I can predict that if I have an object like this, right?

And I open my hand,

it's gonna fall, right?

And if I push it with a particular force on the table,

it's gonna move.

If I push the table itself,

it's probably not gonna move with the same force.

So we have this internal model of the world in our mind,

which allows us to plan sequences of actions

to arrive at a particular goal.

And so now if you have this world model,

we can imagine a sequence of actions,

predict what the outcome

of the sequence of action is going to be,

measure to what extent the final state

satisfies a particular objective

like moving the bottle to the left of the table.

And then plan a sequence of actions

that will minimize this objective at runtime.

We're not talking about learning,

we're talking about inference time, right?

So this is planning, really.

And in optimal control,

this is a very classical thing.

It's called model predictive control.

You have a model of the system you want to control

that can predict the sequence of states

corresponding to a sequence of commands.

And you are planning a sequence of commands

so that according to your world model,

the end state of the system

will satisfy any objectives that you fix.

This is the way rocket trajectories have been planned

since computers have been around.

So since the early '60s, essentially.

- So yes, for a model predictive control,

but you also often talk about hierarchical planning.

- [Yann] Yeah.

- Can hierarchical planning emerge from this somehow?

- Well, so no.

You will have to build a specific architecture

to allow for hierarchical planning.

So hierarchical planning is absolutely necessary

if you want to plan complex actions.

If I wanna go from, let's say, from New York to Paris,

this the example I use all the time.

And I'm sitting in my office at NYU.

My objective that I need to minimize

is my distance to Paris.

At a high level,

a very abstract representation of my location,

I would have to decompose this into two sub-goals.

First one is go to the airport,

# Chapter 4

since computers have been around.

So since the early '60s, essentially.

- So yes, for a model predictive control,

but you also often talk about hierarchical planning.

- [Yann] Yeah.

- Can hierarchical planning emerge from this somehow?

- Well, so no.

You will have to build a specific architecture

to allow for hierarchical planning.

So hierarchical planning is absolutely necessary

if you want to plan complex actions.

If I wanna go from, let's say, from New York to Paris,

this the example I use all the time.

And I'm sitting in my office at NYU.

My objective that I need to minimize

is my distance to Paris.

At a high level,

a very abstract representation of my location,

I would have to decompose this into two sub-goals.

First one is go to the airport,

second one is catch a plane to Paris.

Okay.

So my sub-goal is now going to the airport.

My objective function is my distance to the airport.

How do I go to the airport?

Well, I have to go in the street and hail a taxi,

which you can do in New York.

Okay, now I have another sub-goal.

Go down on the street.

Well, that means going to the elevator,

going down the elevator,

walk out to the street.

How do I go to the elevator?

I have to stand up from my chair,

open the door of my office,

go to the elevator, push the button.

How do I get up for my chair?

Like you can imagine going down all the way down

to basically what amounts

to millisecond by millisecond muscle control.

Okay?

And obviously you're not going to plan your entire trip

from New York to Paris

in terms of millisecond by millisecond muscle control.

First, that would be incredibly expensive,

but it will also be completely impossible

because you don't know all the conditions

of what's gonna happen.

How long it's gonna take to catch a taxi

or to go to the airport with traffic.

I mean, you would have to know exactly

the condition of everything

to be able to do this planning,

and you don't have the information.

So you have to do this hierarchical planning

so that you can start acting

and then sort of re-planning as you go.

And nobody really knows how to do this in AI.

Nobody knows how to train a system

to learn the appropriate multiple levels of representation

so that hierarchical planning works.

- Does something like that already emerge?

So like can you use an LLM,

state-of-the-art LLM,

to get you from New York to Paris

by doing exactly the kind of detailed

set of questions that you just did?

Which is can you give me a list of 10 steps I need to do

to get from New York to Paris?

And then for each of those steps,

can you give me a list of 10 steps

how I make that step happen?

And for each of those steps,

can you give me a list of 10 steps

to make each one of those,

until you're moving your individual muscles?

Maybe not.

Whatever you can actually act upon

using your own mind.

- Right.

So there's a lot of questions

that are also implied by this, right?

So the first thing is LLMs will be able to answer

some of those questions

down to some level of abstraction.

Under the condition that they've been trained

with similar scenarios in their training set.

- They would be able to answer all of those questions.

But some of them may be hallucinated,

meaning non-factual.

- Yeah, true.

I mean they'll probably produce some answer.

Except they're not gonna be able

to really kind of produce

millisecond by millisecond muscle control

of how you stand up from your chair, right?

But down to some level of abstraction

where you can describe things by words,

they might be able to give you a plan,

but only under the condition that they've been trained

to produce those kind of plans, right?

They're not gonna be able to plan for situations

they never encountered before.

They basically are going to have to regurgitate the template

that they've been trained on.

- But where, just for the example of New York to Paris,

is it gonna start getting into trouble?

Like at which layer of abstraction

do you think you'll start?

Because like I can imagine

almost every single part of that,

an LLM will be able to answer somewhat accurately,

especially when you're talking about New York and Paris,

major cities.

- So I mean certainly an LLM

would be able to solve that problem

if you fine tune it for it.

- [Lex] Sure.

- And so I can't say that an LLM cannot do this,

it can't do this if you train it for it,

there's no question,

down to a certain level

where things can be formulated in terms of words.

But like if you wanna go down

to like how do you climb down the stairs

or just stand up from your chair in terms of words,

like you can't do it.

That's one of the reasons you need

experience of the physical world,

which is much higher bandwidth

than what you can express in words,

in human language.

- So everything we've been talking about

on the joint embedding space,

is it possible that that's what we need

for like the interaction with physical reality

on the robotics front?

And then just the LLMs are the thing that sits on top of it

for the bigger reasoning

about like the fact that I need to book a plane ticket

and I need to know know how to go to the websites and so on.

- Sure.

And a lot of plans that people know about

that are relatively high level are actually learned.

Most people don't invent the plans by themselves.

We have some ability to do this, of course, obviously,

but most plans that people use

are plans that have been trained on.

Like they've seen other people use those plans

or they've been told how to do things, right?

That you can't invent how you like take a person

who's never heard of airplanes

and tell them like, how do you go from New York to Paris?

They're probably not going to be able

to kind of deconstruct the whole plan

unless they've seen examples of that before.

So certainly LLMs are gonna be able to do this.

But then how you link this from the low level of actions,

that needs to be done with things like JEPA,

that basically lift the abstraction level

of the representation

without attempting to reconstruct

every detail of the situation.

That's why we need JEPAs for.

- I would love to sort of linger on your skepticism

around autoregressive LLMs.

So one way I would like to test that skepticism is

everything you say makes a lot of sense,

but if I apply everything you said today and in general

to like, I don't know,

10 years ago, maybe a little bit less.

No, let's say three years ago.

I wouldn't be able to predict the success of LLMs.

So does it make sense to you

that autoregressive LLMs are able to be so damn good?

- [Yann] Yes.

- Can you explain your intuition?

Because if I were to take your wisdom and intuition

at face value,

I would say there's no way autoregressive LLMs

one token at a time,

would be able to do the kind of things they're doing.

- No, there's one thing that autoregressive LLMs

or that LLMs in general, not just the autoregressive ones,

but including the BERT style bidirectional ones,

are exploiting and its self supervised running.

And I've been a very, very strong advocate

of self supervised running for many years.

So those things are an incredibly impressive demonstration

that self supervised learning actually works.

The idea that started...

It didn't start with BERT,

but it was really kind of a good demonstration with this.

So the idea that you take a piece of text, you corrupt it,

and then you train some gigantic neural net

to reconstruct the parts that are missing.

That has been an enormous...

Produced an enormous amount of benefits.

It allowed us to create systems that understand language,

systems that can translate

hundreds of languages in any direction,

systems that are multilingual.

It's a single system

that can be trained to understand hundreds of languages

and translate in any direction

and produce summaries

and then answer questions and produce text.

And then there's a special case of it,

which is the autoregressive trick

where you constrain the system

to not elaborate a representation of the text

from looking at the entire text,

but only predicting a word

from the words that have come before.

Right?

And you do this

by constraining the architecture of the network.

And that's what you can build an autoregressive LLM from.

So there was a surprise many years ago

with what's called decoder only LLM.

So systems of this type

that are just trying to produce words from the previous one.

And the fact that when you scale them up,

they tend to really kind of understand more about language.

When you train them on lots of data,

you make them really big.

That was kind of a surprise.

And that surprise occurred quite a while back.

Like with work from Google, Meta, OpenAI, et cetera,

going back to the GPT

kind of general pre-trained transformers.

- You mean like GPT-2?

Like there's a certain place

where you start to realize

scaling might actually keep giving us an emergent benefit.

- Yeah, I mean there were work from various places,

but if you want to kind of place it in the GPT timeline,

that would be around GPT-2, yeah.

- Well, 'cause you said it,

you're so charismatic and you said so many words,

but self supervised learning, yes.

But again, the same intuition you're applying

to saying that autoregressive LLMs

cannot have a deep understanding of the world,

if we just apply that same intuition,

does it make sense to you

that they're able to form enough

of a representation in the world

to be damn convincing,

essentially passing the original Turing test

with flying colors.

- Well, we're fooled by their fluency, right?

We just assume that if a system is fluent

in manipulating language,

then it has all the characteristics of human intelligence.

But that impression is false.

We're really fooled by it.

- Well, what do you think Alan Turing would say?

Without understanding anything,

just hanging out with it-

- Alan Turing would decide

that a Turing test is a really bad test.

(Lex chuckles)

Okay.

This is what the AI community has decided many years ago

that the Turing test was a really bad test of intelligence.

- What would Hans Moravec say

about the large language models?

- Hans Moravec would say

the Moravec's paradox still applies.

- [Lex] Okay.

- Okay?

Okay, we can pass-

- You don't think he would be really impressed.

- No, of course everybody would be impressed.

(laughs)

But it is not a question of being impressed or not,

it is a question of knowing

what the limit of those systems can do.

Again, they are impressive.

They can do a lot of useful things.

There's a whole industry that is being built around them.

They're gonna make progress,

but there is a lot of things they cannot do.

And we have to realize what they cannot do

and then figure out how we get there.

And I'm not saying this...

I'm saying this from basically 10 years of research

on the idea of self supervised running,

actually that's going back more than 10 years,

but the idea of self supervised learning.

So basically capturing the internal structure

of a piece of a set of inputs

without training the system for any particular task, right?

Learning representations.

The conference I co-founded 14 years ago

is called International Conference

on Learning Representations,

that's the entire issue that deep learning is dealing with.

Right?

And it's been my obsession for almost 40 years now.

So learning representation is really the thing.

For the longest time

we could only do this with supervised learning.

And then we started working on

what we used to call unsupervised learning

and sort of revived the idea of unsupervised learning

in the early 2000s with Yoshua Bengio and Jeff Hinton.

Then discovered that supervised learning

actually works pretty well

if you can collect enough data.

And so the whole idea of unsupervised self supervision

took a backseat for a bit

and then I kind of tried to revive it in a big way,

starting in 2014 basically when we started FAIR,

and really pushing for like finding new methods

to do self supervised running,

both for text and for images and for video and audio.

And some of that work has been incredibly successful.

I mean, the reason why we have

multilingual translation system,

things to do,

content moderation on Meta, for example, on Facebook

that are multilingual,

that understand whether piece of text

is hate speech or not, or something

is due to their progress

using self supervised running for NLP,

combining this with transformer architectures

and blah blah blah.

But that's the big success of self supervised running.

We had similar success in speech recognition,

a system called Wav2Vec,

which is also a joint embedding architecture by the way,

trained with contrastive learning.

And that system also can produce

speech recognition systems that are multilingual

with mostly unlabeled data

and only need a few minutes of labeled data

to actually do speech recognition.

That's amazing.

We have systems now based on those combination of ideas

that can do real time translation

of hundreds of languages into each other,

speech to speech.

- Speech to speech,

even including, which is fascinating,

languages that don't have written forms-

- That's right. - They're spoken only.

- That's right.

We don't go through text,

it goes directly from speech to speech

using an internal representation

of kinda speech units that are discrete.

But it's called Textless NLP.

We used to call it this way.

But yeah.

I mean incredible success there.

And then for 10 years we tried to apply this idea

to learning representations of images

by training a system to predict videos,

learning intuitive physics

by training a system to predict

what's gonna happen in the video.

And tried and tried and failed and failed

with generative models,

with models that predict pixels.

We could not get them to learn

good representations of images,

we could not get them to learn good presentations of videos.

And we tried many times,

we published lots of papers on it.

They kind of sort of worked, but not really great.

It started working,

we abandoned this idea of predicting every pixel

and basically just doing the joint embedding and predicting

in representation space.

That works.

So there's ample evidence

that we're not gonna be able to learn good representations

of the real world

using generative model.

So I'm telling people,

everybody's talking about generative AI.

If you're really interested in human level AI,

abandon the idea of generative AI.

(Lex laughs)

- Okay.

But you really think it's possible

to get far with joint embedding representation?

So like there's common sense reasoning

and then there's high level reasoning.

# Chapter 5

They kind of sort of worked, but not really great.

It started working,

we abandoned this idea of predicting every pixel

and basically just doing the joint embedding and predicting

in representation space.

That works.

So there's ample evidence

that we're not gonna be able to learn good representations

of the real world

using generative model.

So I'm telling people,

everybody's talking about generative AI.

If you're really interested in human level AI,

abandon the idea of generative AI.

(Lex laughs)

- Okay.

But you really think it's possible

to get far with joint embedding representation?

So like there's common sense reasoning

and then there's high level reasoning.

Like I feel like those are two...

The kind of reasoning that LLMs are able to do.

Okay, let me not use the word reasoning,

but the kind of stuff that LLMs are able to do

seems fundamentally different

than the common sense reasoning we use

to navigate the world.

- [Yann] Yeah.

- It seems like we're gonna need both-

- Sure. - Would you be able to get,

with the joint embedding which is a JEPA type of approach,

looking at video, would you be able to learn,

let's see,

well, how to get from New York to Paris,

or how to understand the state of politics in the world?

(both laugh)

Right?

These are things where various humans

generate a lot of language and opinions on,

in the space of language,

but don't visually represent that

in any clearly compressible way.

- Right.

Well, there's a lot of situations

that might be difficult

for a purely language based system to know.

Like, okay, you can probably learn from reading texts,

the entirety of the publicly available text in the world

that I cannot get from New York to Paris

by snapping my fingers.

That's not gonna work, right?

- [Lex] Yes.

- But there's probably sort of more complex

scenarios of this type

which an LLM may never have encountered

and may not be able to determine

whether it's possible or not.

So that link from the low level to the high level...

The thing is that the high level that language expresses

is based on the common experience of the low level,

which LLMs currently do not have.

When we talk to each other,

we know we have a common experience of the world.

Like a lot of it is similar.

And LLMs don't have that.

- But see, there it's present.

You and I have a common experience of the world

in terms of the physics of how gravity works

and stuff like this.

And that common knowledge of the world,

I feel like is there in the language.

We don't explicitly express it,

but if you have a huge amount of text,

you're going to get this stuff that's between the lines.

In order to form a consistent world model,

you're going to have to understand how gravity works,

even if you don't have an explicit explanation of gravity.

So even though, in the case of gravity,

there is explicit explanation.

There's gravity in Wikipedia.

But like the stuff that we think of

as common sense reasoning,

I feel like to generate language correctly,

you're going to have to figure that out.

Now, you could say as you have,

there's not enough text- - Well, I agree.

- Sorry.

Okay, yeah.

(laughs)

You don't think so?

- No, I agree with what you just said,

which is that to be able to do high level common sense...

To have high level common sense,

you need to have the low level common sense

to build on top of.

- [Lex] Yeah.

But that's not there.

- That's not there in LLMs.

LLMs are purely trained from text.

So then the other statement you made,

I would not agree

with the fact that implicit in all languages in the world

is the underlying reality.

There's a lot about underlying reality

which is not expressed in language.

- Is that obvious to you?

- Yeah, totally.

- So like all the conversations we have...

Okay, there's the dark web,

meaning whatever,

the private conversations like DMs and stuff like this,

which is much, much larger probably than what's available,

what LLMs are trained on.

- You don't need to communicate

the stuff that is common.

- But the humor, all of it.

No, you do.

You don't need to, but it comes through.

Like if I accidentally knock this over,

you'll probably make fun of me.

And in the content of the you making fun of me

will be explanation of the fact that cups fall

and then gravity works in this way.

And then you'll have some very vague information

about what kind of things explode when they hit the ground.

And then maybe you'll make a joke about entropy

or something like this

and we will never be able to reconstruct this again.

Like, okay, you'll make a little joke like this

and there'll be trillion of other jokes.

And from the jokes,

you can piece together the fact that gravity works

and mugs can break and all this kind of stuff,

you don't need to see...

It'll be very inefficient.

It's easier for like

to not knock the thing over. (laughing)

- [Yann] Yeah.

- But I feel like it would be there

if you have enough of that data.

- I just think that most of the information of this type

that we have accumulated when we were babies

is just not present in text,

in any description, essentially.

And the sensory data is a much richer source

for getting that kind of understanding.

I mean, that's the 16,000 hours

of wake time of a 4-year-old.

And tend to do 15 bytes, going through vision.

Just vision, right?

There is a similar bandwidth of touch

and a little less through audio.

And then text doesn't...

Language doesn't come in until like a year in life.

And by the time you are nine years old,

you've learned about gravity,

you know about inertia,

you know about gravity,

you know there's stability,

you know about the distinction

between animate and inanimate objects.

By 18 months,

you know about like why people want to do things

and you help them if they can't.

I mean there's a lot of things that you learn

mostly by observation,

really not even through interaction.

In the first few months of life,

babies don't really have any influence on the world.

They can only observe, right?

And you accumulate like a gigantic amount of knowledge

just from that.

So that's what we're missing from current AI systems.

- I think in one of your slides you have this nice plot

that is one of the ways you show that LLMs are limited.

I wonder if you could talk about hallucinations

from your perspectives.

Why hallucinations happen from large language models,

and to what degree is that a fundamental flaw

of large language models.

- Right.

So because of the autoregressive prediction,

every time an LLM produces a token or a word,

there is some level of probability for that word

to take you out of the set of reasonable answers.

And if you assume,

which is a very strong assumption,

that the probability of such error

is those errors are independent

across a sequence of tokens being produced.

What that means is that every time you produce a token,

the probability

that you stay within the set of correct answer decreases

and it decreases exponentially.

- So there's a strong, like you said, assumption there

that if there's a non-zero probability of making a mistake,

which there appears to be,

then there's going to be a kind of drift.

- Yeah.

And that drift is exponential.

It's like errors accumulate, right?

So the probability that an answer would be nonsensical

increases exponentially with the number of tokens.

- Is that obvious to you by the way?

Well, so mathematically speaking maybe,

but like isn't there a kind of gravitational pull

towards the truth?

Because on average, hopefully,

the truth is well represented in the training set.

- No, it's basically a struggle

against the curse of dimensionality.

So the way you can correct for this

is that you fine tune the system

by having it produce answers

for all kinds of questions that people might come up with.

And people are people,

so a lot of the questions that they have

are very similar to each other.

So you can probably cover,

you know, 80% or whatever of questions that people will ask

by collecting data.

And then you fine tune the system

to produce good answers for all of those things.

And it's probably gonna be able to learn that

because it's got a lot of capacity to learn.

But then there is the enormous set of prompts

that you have not covered during training.

And that set is enormous.

Like within the set of all possible prompts,

the proportion of prompts that have been used for training

is absolutely tiny.

It's a tiny, tiny, tiny subset of all possible prompts.

And so the system will behave properly

on the prompts that it's been either trained,

pre-trained or fine tuned.

But then there is an entire space of things

that it cannot possibly have been trained on

because it's just the number is gigantic.

So whatever training the system

has been subject to produce appropriate answers,

you can break it by finding out a prompt

that will be outside of the set of prompts

it's been trained on

or things that are similar,

and then it will just spew complete nonsense.

- When you say prompt,

do you mean that exact prompt

or do you mean a prompt that's like,

in many parts very different than...

Is it that easy to ask a question

or to say a thing that hasn't been said before

on the internet?

- I mean, people have come up with things

where like you put essentially

a random sequence of characters in a prompt

and that's enough to kind of throw the system into a mode

where it's gonna answer something completely different

than it would have answered without this.

So that's a way to jailbreak the system, basically.

Go outside of its conditioning, right?

- So that's a very clear demonstration of it.

But of course, that goes outside

of what it's designed to do, right?

If you actually stitch together

reasonably grammatical sentences,

is it that easy to break it?

- Yeah.

Some people have done things like

you write a sentence in English

or you ask a question in English

and it produces a perfectly fine answer.

And then you just substitute a few words

by the same word in another language,

and all of a sudden the answer is complete nonsense.

- Yeah.

So I guess what I'm saying is like,

which fraction of prompts that humans are likely to generate

are going to break the system?

- So the problem is that there is a long tail.

- [Lex] Yes.

- This is an issue that a lot of people have realized

in social networks and stuff like that,

which is there's a very, very long tail

of things that people will ask.

And you can fine tune the system

for the 80% or whatever

of the things that most people will ask.

And then this long tail is so large

that you're not gonna be able to fine tune the system

for all the conditions.

And in the end,

the system ends up being

kind of a giant lookup table, right? (laughing)

Essentially.

Which is not really what you want.

You want systems that can reason,

certainly that can plan.

So the type of reasoning that takes place in LLM

is very, very primitive.

And the reason you can tell it's primitive

is because the amount of computation

that is spent per token produced is constant.

So if you ask a question

and that question has an answer in a given number of token,

the amount of computation devoted to computing that answer

can be exactly estimated.

It's the size of the prediction network

with its 36 layers or 92 layers or whatever it is,

multiplied by number of tokens.

That's it.

And so essentially,

it doesn't matter if the question being asked

is simple to answer, complicated to answer,

impossible to answer

because it's decided, well, there's something.

The amount of computation

the system will be able to devote to the answer is constant

or is proportional to the number of token produced

in the answer, right?

This is not the way we work,

the way we reason is that

when we are faced with a complex problem

or a complex question,

we spend more time trying to solve it and answer it, right?

Because it's more difficult.

- There's a prediction element,

there's an iterative element

where you're like adjusting your understanding of a thing

by going over and over and over.

There's a hierarchical elements on.

Does this mean it's a fundamental flaw of LLMs-

- [Yann] Yeah.

- Or does it mean that... (laughs)

There's more part to that question?

(laughs)

Now you're just behaving like an LLM.

(laughs)

Immediately answering.

No, that it's just the low level world model

on top of which we can then build

some of these kinds of mechanisms,

like you said, persistent long-term memory or reasoning,

so on.

But we need that world model that comes from language.

Maybe it is not so difficult

to build this kind of reasoning system

on top of a well constructed world model.

- Okay.

Whether it's difficult or not,

the near future will say,

because a lot of people are working on reasoning

and planning abilities for dialogue systems.

I mean, even if we restrict ourselves to language,

just having the ability

to plan your answer before you answer,

in terms that are not necessarily linked

with the language you're gonna use to produce the answer.

Right?

So this idea of this mental model

that allows you to plan what you're gonna say

before you say it.

That is very important.

I think there's going to be a lot of systems

over the next few years

that are going to have this capability,

but the blueprint of those systems

will be extremely different from autoregressive LLMs.

So it's the same difference

as the difference between

what psychology has called system one and system two

in humans, right?

So system one is the type of task that you can accomplish

without like deliberately consciously think about

how you do them.

You just do them.

You've done them enough

that you can just do it subconsciously, right?

Without thinking about them.

If you're an experienced driver,

you can drive without really thinking about it

and you can talk to someone at the same time

or listen to the radio, right?

If you are a very experienced chess player,

you can play against a non-experienced chess player

without really thinking either,

you just recognize the pattern and you play, right?

That's system one.

# Chapter 6

So it's the same difference

as the difference between

what psychology has called system one and system two

in humans, right?

So system one is the type of task that you can accomplish

without like deliberately consciously think about

how you do them.

You just do them.

You've done them enough

that you can just do it subconsciously, right?

Without thinking about them.

If you're an experienced driver,

you can drive without really thinking about it

and you can talk to someone at the same time

or listen to the radio, right?

If you are a very experienced chess player,

you can play against a non-experienced chess player

without really thinking either,

you just recognize the pattern and you play, right?

That's system one.

So all the things that you do instinctively

without really having to deliberately plan

and think about it.

And then there is other tasks where you need to plan.

So if you are a not too experienced chess player

or you are experienced

but you play against another experienced chess player,

you think about all kinds of options, right?

You think about it for a while, right?

And you're much better if you have time to think about it

than you are if you play blitz with limited time.

And so this type of deliberate planning,

which uses your internal world model, that's system two,

this is what LLMs currently cannot do.

How do we get them to do this, right?

How do we build a system

that can do this kind of planning or reasoning

that devotes more resources

to complex problems than to simple problems.

And it's not going to be

autoregressive prediction of tokens,

it's going to be more something akin to inference

of latent variables

in what used to be called probabilistic models

or graphical models and things of that type.

So basically the principle is like this.

The prompt is like observed variables.

And what the model does

is that it's basically a measure of...

It can measure to what extent an answer

is a good answer for a prompt.

Okay?

So think of it as some gigantic neural net,

but it's got only one output.

And that output is a scaler number,

which is let's say zero

if the answer is a good answer for the question,

and a large number

if the answer is not a good answer for the question.

Imagine you had this model.

If you had such a model,

you could use it to produce good answers.

The way you would do is produce the prompt

and then search through the space of possible answers

for one that minimizes that number.

That's called an energy based model.

- But that energy based model

would need the model constructed by the LLM.

- Well, so really what you need to do

would be to not search over possible strings of text

that minimize that energy.

But what you would do

is do this in abstract representation space.

So in sort of the space of abstract thoughts,

you would elaborate a thought, right?

Using this process of minimizing the output of your model.

Okay?

Which is just a scaler.

It's an optimization process, right?

So now the way the system produces its answer

is through optimization

by minimizing an objective function basically, right?

And this is, we're talking about inference,

we're not talking about training, right?

The system has been trained already.

So now we have an abstract representation

of the thought of the answer,

representation of the answer.

We feed that to basically an autoregressive decoder,

which can be very simple,

that turns this into a text that expresses this thought.

Okay?

So that in my opinion

is the blueprint of future data systems.

They will think about their answer,

plan their answer by optimization

before turning it into text.

And that is turning complete.

- Can you explain exactly

what the optimization problem there is?

Like what's the objective function?

Just linger on it.

You kind of briefly described it,

but over what space are you optimizing?

- The space of representations-

- Goes abstract representation.

- That's right.

So you have an abstract representation inside the system.

You have a prompt.

The prompt goes through an encoder,

produces a representation,

perhaps goes through a predictor

that predicts a representation of the answer,

of the proper answer.

But that representation may not be a good answer

because there might be some complicated reasoning

you need to do, right?

So then you have another process

that takes the representation of the answers and modifies it

so as to minimize a cost function

that measures to what extent

the answer is a good answer for the question.

Now we sort of ignore the fact for...

I mean, the issue for a moment

of how you train that system

to measure whether an answer is a good answer for sure.

- But suppose such a system could be created,

what's the process?

This kind of search like process.

- It's an optimization process.

You can do this if the entire system is differentiable,

that scaler output

is the result of running through some neural net,

running the answer,

the representation of the answer through some neural net.

Then by gradient descent,

by back propagating gradients,

you can figure out

like how to modify the representation of the answers

so as to minimize that.

- So that's still a gradient based.

- It's gradient based inference.

So now you have a representation of the answer

in abstract space.

Now you can turn it into text, right?

And the cool thing about this

is that the representation now

can be optimized through gradient descent,

but also is independent of the language

in which you're going to express the answer.

- Right.

So you're operating in the substruct of representation.

I mean this goes back to the joint embedding.

- [Yann] Right.

- That it's better to work in the space of...

I don't know.

Or to romanticize the notion

like space of concepts

versus the space of concrete sensory information.

- Right.

- Okay.

But can this do something like reasoning,

which is what we're talking about?

- Well, not really,

only in a very simple way.

I mean basically you can think of those things as doing

the kind of optimization I was talking about,

except they're optimizing the discrete space

which is the space of possible sequences of tokens.

And they do this optimization in a horribly inefficient way,

which is generate a lot of hypothesis

and then select the best ones.

And that's incredibly wasteful

in terms of competition,

'cause you basically have to run your LLM

for like every possible generative sequence.

And it's incredibly wasteful.

So it's much better to do an optimization

in continuous space

where you can do gradient descent

as opposed to like generate tons of things

and then select the best,

you just iteratively refine your answer

to go towards the best, right?

That's much more efficient.

But you can only do this in continuous spaces

with differentiable functions.

- You're talking about the reasoning,

like ability to think deeply or to reason deeply.

How do you know what is an answer

that's better or worse based on deep reasoning?

- Right.

So then we're asking the question,

of conceptually, how do you train an energy based model?

Right?

So energy based model

is a function with a scaler output, just a number.

You give it two inputs, X and Y,

and it tells you whether Y is compatible with X or not.

X you observe,

let's say it's a prompt, an image, a video, whatever.

And Y is a proposal for an answer,

a continuation of video, whatever.

And it tells you whether Y is compatible with X.

And the way it tells you that Y is compatible with X

is that the output of that function would be zero

if Y is compatible with X,

it would be a positive number, non-zero

if Y is not compatible with X.

Okay.

How do you train a system like this?

At a completely general level,

is you show it pairs of X and Ys that are compatible,

a question and the corresponding answer.

And you train the parameters of the big neural net inside

to produce zero.

Okay.

Now that doesn't completely work

because the system might decide,

well, I'm just gonna say zero for everything.

So now you have to have a process

to make sure that for a wrong Y,

the energy will be larger than zero.

And there you have two options,

one is contrastive methods.

So contrastive method is you show an X and a bad Y,

and you tell the system,

well, give a high energy to this.

Like push up the energy, right?

Change the weights in the neural net that compute the energy

so that it goes up.

So that's contrasting methods.

The problem with this is if the space of Y is large,

the number of such contrasted samples

you're gonna have to show is gigantic.

But people do this.

They do this when you train a system with RLHF,

basically what you're training

is what's called a reward model,

which is basically an objective function

that tells you whether an answer is good or bad.

And that's basically exactly what this is.

So we already do this to some extent.

We're just not using it for inference,

we're just using it for training.

There is another set of methods

which are non-contrastive, and I prefer those.

And those non-contrastive method basically say,

okay, the energy function

needs to have low energy on pairs of XYs that are compatible

that come from your training set.

How do you make sure that the energy

is gonna be higher everywhere else?

And the way you do this

is by having a regularizer, a criterion,

a term in your cost function

that basically minimizes the volume of space

that can take low energy.

And the precise way to do this,

there's all kinds of different specific ways to do this

depending on the architecture,

but that's the basic principle.

So that if you push down the energy function

for particular regions in the XY space,

it will automatically go up in other places

because there's only a limited volume of space

that can take low energy.

Okay?

By the construction of the system

or by the regularizing function.

- We've been talking very generally,

but what is a good X and a good Y?

What is a good representation of X and Y?

Because we've been talking about language.

And if you just take language directly,

that presumably is not good,

so there has to be

some kind of abstract representation of ideas.

- Yeah.

I mean you can do this with language directly

by just, you know, X is a text

and Y is the continuation of that text.

- [Lex] Yes.

- Or X is a question, Y is the answer.

- But you're saying that's not gonna take it.

I mean, that's going to do what LLMs are doing.

- Well, no.

It depends on how the internal structure of the system

is built.

If the internal structure of the system

is built in such a way that inside of the system

there is a latent variable,

let's called it Z,

that you can manipulate

so as to minimize the output energy,

then that Z can be viewed as representation of a good answer

that you can translate into a Y that is a good answer.

- So this kind of system could be trained

in a very similar way?

- Very similar way.

But you have to have this way of preventing collapse,

of ensuring that there is high energy

for things you don't train it on.

And currently it's very implicit in LLMs.

It is done in a way

that people don't realize it's being done,

but it is being done.

It's due to the fact

that when you give a high probability to a word,

automatically you give low probability to other words

because you only have

a finite amount of probability to go around. (laughing)

Right?

They have to sub to one.

So when you minimize the cross entropy or whatever,

when you train your LLM to predict the next word,

you are increasing the probability

your system will give to the correct word,

but you're also decreasing the probability

it will give to the incorrect words.

Now, indirectly, that gives a low probability to...

A high probability to sequences of words that are good

and low probability two sequences of words that are bad,

but it's very indirect.

It's not obvious why this actually works at all,

because you're not doing it on a joint probability

of all the symbols in a sequence,

you're just doing it kind of,

sort of factorized that probability

in terms of conditional probabilities

over successive tokens.

- So how do you do this for visual data?

- So we've been doing this

with all JEPA architectures, basically the-

- [Lex] The joint embedding?

- I-JEPA.

So there, the compatibility between two things

is here's an image or a video,

here is a corrupted, shifted or transformed version

of that image or video or masked.

Okay?

And then the energy of the system

is the prediction error of the representation.

The predicted representation of the good thing

versus the actual representation of the good thing, right?

So you run the corrupted image to the system,

predict the representation of the good input uncorrupted,

and then compute the prediction error.

That's the energy of the system.

So this system will tell you,

this is a good image and this is a corrupted version.

It will give you zero energy

if those two things are effectively,

one of them is a corrupted version of the other,

give you a high energy

if the two images are completely different.

- And hopefully that whole process

gives you a really nice compressed representation

of reality, of visual reality.

- And we know it does

because then we use those presentations

as input to a classification system or something,

and it works- - And then

that classification system works really nicely.

Okay.

Well, so to summarize,

you recommend in a spicy way that only Yann LeCun can,

you recommend that we abandon generative models

in favor of joint embedding architectures?

- [Yann] Yes.

- Abandon autoregressive generation.

- [Yann] Yes.

- Abandon... (laughs)

This feels like court testimony.

Abandon probabilistic models

in favor of energy based models, as we talked about.

Abandon contrastive methods

in favor of regularized methods.

And let me ask you about this;

you've been for a while, a critic of reinforcement learning.

- [Yann] Yes.

- So the last recommendation is that we abandon RL

in favor of model predictive control,

as you were talking about.

And only use RL

when planning doesn't yield the predicted outcome.

And we use RL in that case

to adjust the world model or the critic.

- [Yann] Yes.

- So you've mentioned RLHF,

reinforcement learning with human feedback.

Why do you still hate reinforcement learning?

- [Yann] I don't hate reinforcement learning,

and I think it's- - So it's all love?

# Chapter 7

Abandon probabilistic models

in favor of energy based models, as we talked about.

Abandon contrastive methods

in favor of regularized methods.

And let me ask you about this;

you've been for a while, a critic of reinforcement learning.

- [Yann] Yes.

- So the last recommendation is that we abandon RL

in favor of model predictive control,

as you were talking about.

And only use RL

when planning doesn't yield the predicted outcome.

And we use RL in that case

to adjust the world model or the critic.

- [Yann] Yes.

- So you've mentioned RLHF,

reinforcement learning with human feedback.

Why do you still hate reinforcement learning?

- [Yann] I don't hate reinforcement learning,

and I think it's- - So it's all love?

- I think it should not be abandoned completely,

but I think it's use should be minimized

because it's incredibly inefficient in terms of samples.

And so the proper way to train a system

is to first have it learn

good representations of the world and world models

from mostly observation,

maybe a little bit of interactions.

- And then steer it based on that.

If the representation is good,

then the adjustments should be minimal.

- Yeah.

Now there's two things.

If you've learned the world model,

you can use the world model to plan a sequence of actions

to arrive at a particular objective.

You don't need RL,

unless the way you measure whether you succeed

might be inexact.

Your idea of whether you were gonna fall from your bike

might be wrong,

or whether the person you're fighting with MMA

was gonna do something

and they do something else. (laughing)

So there's two ways you can be wrong.

Either your objective function

does not reflect

the actual objective function you want to optimize,

or your world model is inaccurate, right?

So the prediction you were making

about what was gonna happen in the world is inaccurate.

So if you want to adjust your world model

while you are operating the world

or your objective function,

that is basically in the realm of RL.

This is what RL deals with to some extent, right?

So adjust your world model.

And the way to adjust your world model, even in advance,

is to explore parts of the space with your world model,

where you know that your world model is inaccurate.

That's called curiosity basically, or play, right?

When you play,

you kind of explore part of the state space

that you don't want to do for real

because it might be dangerous,

but you can adjust your world model

without killing yourself basically. (laughs)

So that's what you want to use RL for.

When it comes time to learning a particular task,

you already have all the good representations,

you already have your world model,

but you need to adjust it for the situation at hand.

That's when you use RL.

- Why do you think RLHF works so well?

This enforcement learning with human feedback,

why did it have such a transformational effect

on large language models that came before?

- So what's had the transformational effect

is human feedback.

There is many ways to use it

and some of it is just purely supervised, actually,

it's not really reinforcement learning.

- So it's the HF. (laughing)

- It's the HF.

And then there is various ways to use human feedback, right?

So you can ask humans to rate answers,

multiple answers that are produced by a world model.

And then what you do is you train an objective function

to predict that rating.

And then you can use that objective function

to predict whether an answer is good,

and you can back propagate really through this

to fine tune your system

so that it only produces highly rated answers.

Okay?

So that's one way.

So that's like in RL,

that means training what's called a reward model, right?

So something that,

basically your small neural net

that estimates to what extent an answer is good, right?

It's very similar to the objective

I was talking about earlier for planning,

except now it's not used for planning,

it's used for fine tuning your system.

I think it would be much more efficient

to use it for planning,

but currently it's used

to fine tune the parameters of the system.

Now, there's several ways to do this.

Some of them are supervised.

You just ask a human person,

like what is a good answer for this, right?

Then you just type the answer.

I mean, there's lots of ways

that those systems are being adjusted.

- Now, a lot of people have been very critical

of the recently released Google's Gemini 1.5

for essentially, in my words, I could say super woke.

Woke in the negative connotation of that word.

There is some almost hilariously absurd things that it does,

like it modifies history,

like generating images of a black George Washington

or perhaps more seriously

something that you commented on Twitter,

which is refusing to comment on or generate images of,

or even descriptions of Tiananmen Square or the tank men,

one of the most sort of legendary protest images in history.

And of course, these images are highly censored

by the Chinese government.

And therefore everybody started asking questions

of what is the process of designing these LLMs?

What is the role of censorship in these,

and all that kind of stuff.

So you commented on Twitter

saying that open source is the answer.

(laughs) - Yeah.

- Essentially.

So can you explain?

- I actually made that comment

on just about every social network I can.

(Lex laughs)

And I've made that point multiple times in various forums.

Here's my point of view on this.

People can complain that AI systems are biased,

and they generally are biased

by the distribution of the training data

that they've been trained on

that reflects biases in society.

And that is potentially offensive to some people

or potentially not.

And some techniques to de-bias

then become offensive to some people

because of historical incorrectness and things like that.

And so you can ask the question.

You can ask two questions.

The first question is,

is it possible to produce an AI system that is not biased?

And the answer is absolutely not.

And it's not because of technological challenges,

although there are technological challenges to that.

It's because bias is in the eye of the beholder.

Different people may have different ideas

about what constitutes bias for a lot of things.

I mean there are facts that are indisputable,

but there are a lot of opinions or things

that can be expressed in different ways.

And so you cannot have an unbiased system,

that's just an impossibility.

And so what's the answer to this?

And the answer is the same answer that we found

in liberal democracy about the press.

The press needs to be free and diverse.

We have free speech for a good reason.

It's because we don't want all of our information

to come from a unique source,

'cause that's opposite to the whole idea of democracy

and progressive ideas and even science, right?

In science, people have to argue for different opinions.

And science makes progress when people disagree

and they come up with an answer

and a consensus forms, right?

And it's true in all democracies around the world.

So there is a future which is already happening

where every single one of our interaction

with the digital world

will be mediated by AI systems,

AI assistance, right?

We're gonna have smart glasses.

You can already buy them from Meta, (laughing)

the Ray-Ban Meta.

Where you can talk to them

and they are connected with an LLM

and you can get answers on any question you have.

Or you can be looking at a monument

and there is a camera in the system, in the glasses,

you can ask it like what can you tell me

about this building or this monument?

You can be looking at a menu in a foreign language

and the thing we will translate it for you.

We can do real time translation

if we speak different languages.

So a lot of our interactions with the digital world

are going to be mediated by those systems

in the near future.

Increasingly, the search engines that we're gonna use

are not gonna be search engines,

they're gonna be dialogue systems

that we just ask a question,

and it will answer

and then point you

to the perhaps appropriate reference for it.

But here is the thing,

we cannot afford those systems

to come from a handful of companies

on the west coast of the US

because those systems will constitute

the repository of all human knowledge.

And we cannot have that be controlled

by a small number of people, right?

It has to be diverse

for the same reason the press has to be diverse.

So how do we get a diverse set of AI assistance?

It's very expensive and difficult

to train a base model, right?

A base LLM at the moment.

In the future might be something different,

but at the moment that's an LLM.

So only a few companies can do this properly.

And if some of those subsystems are open source,

anybody can use them,

anybody can fine tune them.

If we put in place some systems

that allows any group of people,

whether they are individual citizens,

groups of citizens,

government organizations,

NGOs, companies, whatever,

to take those open source systems, AI systems,

and fine tune them for their own purpose on their own data,

there we're gonna have a very large diversity

of different AI systems

that are specialized for all of those things, right?

So I'll tell you,

I talked to the French government quite a bit

and the French government will not accept

that the digital diet of all their citizens

be controlled by three companies

on the west coast of the US.

That's just not acceptable.

It's a danger to democracy.

Regardless of how well intentioned

those companies are, right?

And it's also a danger to local culture,

to values, to language, right?

I was talking with the founder of Infosys in India.

He's funding a project to fine tune LLaMA 2,

the open source model produced by Meta.

So that LLaMA 2 speaks all 22 official languages in India.

It's very important for people in India.

I was talking to a former colleague of mine,

Moustapha Cisse,

who used to be a scientist at FAIR,

and then moved back to Africa

and created a research lab for Google in Africa

and now has a new startup Kera.

And what he's trying to do is basically have LLM

that speaks the local languages in Senegal

so that people can have access to medical information,

'cause they don't have access to doctors,

it's a very small number of doctors per capita in Senegal.

I mean, you can't have any of this

unless you have open source platforms.

So with open source platforms,

you can have AI systems

that are not only diverse in terms of political opinions

or things of that type,

but in terms of language, culture, value systems,

political opinions, technical abilities in various domains.

And you can have an industry,

an ecosystem of companies

that fine tune those open source systems

for vertical applications in industry, right?

You have, I don't know, a publisher has thousands of books

and they want to build a system

that allows a customer to just ask a question

about the content of any of their books.

You need to train on their proprietary data, right?

You have a company,

we have one within Meta it's called Meta Mate.

And it's basically an LLM

that can answer any question

about internal stuff about about the company.

Very useful.

A lot of companies want this, right?

A lot of companies want this not just for their employees,

but also for their customers,

to take care of their customers.

So the only way you're gonna have an AI industry,

the only way you're gonna have AI systems

that are not uniquely biased,

is if you have open source platforms

on top of which any group can build specialized systems.

So the inevitable direction of history

is that the vast majority of AI systems

will be built on top of open source platforms.

- So that's a beautiful vision.

So meaning like a company like Meta or Google or so on,

should take only minimal fine tuning steps

after the building, the foundation, pre-trained model.

As few steps as possible.

- Basically.

(Lex sighs)

- Can Meta afford to do that?

- No.

- So I don't know if you know this,

but companies are supposed to make money somehow.

And open source is like giving away...

I don't know, Mark made a video,

Mark Zuckerberg.

A very sexy video talking about 350,000 Nvidia H100s.

The math of that is,

just for the GPUs, that's a hundred billion,

plus the infrastructure for training everything.

So I'm no business guy,

but how do you make money on that?

So the vision you paint is a really powerful one,

but how is it possible to make money?

- Okay.

So you have several business models, right?

The business model that Meta is built around

is you offer a service,

and the financing of that service

is either through ads or through business customers.

So for example, if you have an LLM

that can help a mom-and-pop pizza place

by talking to their customers through WhatsApp,

and so the customers can just order a pizza

and the system will just ask them,

like what topping do you want or what size, blah blah, blah.

# Chapter 8

A very sexy video talking about 350,000 Nvidia H100s.

The math of that is,

just for the GPUs, that's a hundred billion,

plus the infrastructure for training everything.

So I'm no business guy,

but how do you make money on that?

So the vision you paint is a really powerful one,

but how is it possible to make money?

- Okay.

So you have several business models, right?

The business model that Meta is built around

is you offer a service,

and the financing of that service

is either through ads or through business customers.

So for example, if you have an LLM

that can help a mom-and-pop pizza place

by talking to their customers through WhatsApp,

and so the customers can just order a pizza

and the system will just ask them,

like what topping do you want or what size, blah blah, blah.

The business will pay for that.

Okay?

That's a model.

And otherwise, if it's a system

that is on the more kind of classical services,

it can be ad supported or there's several models.

But the point is,

if you have a big enough potential customer base

and you need to build that system anyway for them,

it doesn't hurt you

to actually distribute it to open source.

- Again, I'm no business guy,

but if you release the open source model,

then other people can do the same kind of task

and compete on it.

Basically provide fine tuned models for businesses,

is the bet that Meta is making...

By the way, I'm a huge fan of all this.

But is the bet that Meta is making

is like, "we'll do a better job of it?"

- Well, no.

The bet is more,

we already have a huge user base and customer base.

- [Lex] Ah, right. - Right?

So it's gonna be useful to them.

Whatever we offer them is gonna be useful

and there is a way to derive revenue from this.

- [Lex] Sure.

- And it doesn't hurt

that we provide that system or the base model, right?

The foundation model in open source

for others to build applications on top of it too.

If those applications

turn out to be useful for our customers,

we can just buy it for them.

It could be that they will improve the platform.

In fact, we see this already.

I mean there is literally millions of downloads of LLaMA 2

and thousands of people who have provided ideas

about how to make it better.

So this clearly accelerates progress

to make the system available

to sort of a wide community of people.

And there is literally thousands of businesses

who are building applications with it.

Meta's ability to derive revenue from this technology

is not impaired by the distribution

of base models in open source.

- The fundamental criticism that Gemini is getting

is that, as you pointed out on the west coast...

Just to clarify,

we're currently in the east coast,

where I would suppose Meta AI headquarters would be.

(laughs)

So strong words about the west coast.

But I guess the issue that happens is,

I think it's fair to say that most tech people

have a political affiliation with the left wing.

They lean left.

And so the problem that people are criticizing Gemini with

is that in that de-biasing process that you mentioned,

that their ideological lean becomes obvious.

Is this something that could be escaped?

You're saying open source is the only way?

- [Yann] Yeah.

- Have you witnessed this kind of ideological lean

that makes engineering difficult?

- No, I don't think it has to do...

I don't think the issue has to do

with the political leaning

of the people designing those systems.

It has to do with the acceptability or political leanings

of their customer base or audience, right?

So a big company cannot afford to offend too many people.

So they're going to make sure

that whatever product they put out is "safe,"

whatever that means.

And it's very possible to overdo it.

And it's also very possible to...

It's impossible to do it properly for everyone.

You're not going to satisfy everyone.

So that's what I said before,

you cannot have a system that is unbiased

and is perceived as unbiased by everyone.

It's gonna be,

you push it in one way,

one set of people are gonna see it as biased.

And then you push it the other way

and another set of people is gonna see it as biased.

And then in addition to this,

there's the issue of if you push the system

perhaps a little too far in one direction,

it's gonna be non-factual, right?

You're gonna have black Nazi soldiers in-

- Yeah.

So we should mention image generation

of black Nazi soldiers,

which is not factually accurate.

- Right.

And can be offensive for some people as well, right?

So it's gonna be impossible

to kind of produce systems that are unbiased for everyone.

So the only solution that I see is diversity.

- And diversity in full meaning of that word,

diversity in every possible way.

- [Yann] Yeah.

- Marc Andreessen just tweeted today,

let me do a TL;DR.

The conclusion is only startups and open source

can avoid the issue that he's highlighting with big tech.

He's asking,

can big tech actually field generative AI products?

One, ever escalating demands from internal activists,

employee mobs, crazed executives,

broken boards, pressure groups,

extremist regulators, government agencies, the press,

in quotes "experts,"

and everything corrupting the output.

Two, constant risk of generating a bad answer

or drawing a bad picture or rendering a bad video.

Who knows what it's going to say or do at any moment?

Three, legal exposure, product liability, slander,

election law, many other things and so on.

Anything that makes Congress mad.

Four, continuous attempts

to tighten grip on acceptable output,

degrade the model,

like how good it actually is

in terms of usable and pleasant to use and effective

and all that kind of stuff.

And five, publicity of bad text, images, video,

actual puts those examples into the training data

for the next version.

And so on.

So he just highlights how difficult this is.

From all kinds of people being unhappy.

He just said you can't create a system

that makes everybody happy.

- [Yann] Yes.

- So if you're going to do the fine tuning yourself

and keep a close source,

essentially the problem there

is then trying to minimize the number of people

who are going to be unhappy.

- [Yann] Yeah.

- And you're saying like the only...

That that's almost impossible to do, right?

And the better way is to do open source.

- Basically, yeah.

I mean Marc is right about a number of things that he lists

that indeed scare large companies.

Certainly, congressional investigations is one of them.

Legal liability.

Making things

that get people to hurt themselves or hurt others.

Like big companies are really careful

about not producing things of this type,

because they have...

They don't want to hurt anyone, first of all.

And then second, they wanna preserve their business.

So it's essentially impossible for systems like this

that can inevitably formulate political opinions

and opinions about various things

that may be political or not,

but that people may disagree about.

About, you know, moral issues

and things about like questions about religion

and things like that, right?

Or cultural issues

that people from different communities

would disagree with in the first place.

So there's only kind of a relatively small number of things

that people will sort of agree on,

basic principles.

But beyond that,

if you want those systems to be useful,

they will necessarily have to offend a number of people,

inevitably.

- And so open source is just better-

- [Yann] Diversity is better, right?

- And open source enables diversity.

- That's right.

Open source enables diversity.

- This can be a fascinating world

where if it's true that the open source world,

if Meta leads the way

and creates this kind of open source foundation model world,

there's going to be,

like governments will have a fine tuned model. (laughing)

- [Yann] Yeah.

- And then potentially,

people that vote left and right

will have their own model and preference

to be able to choose.

And it will potentially divide us even more

but that's on us humans.

We get to figure out...

Basically the technology enables humans

to human more effectively.

And all the difficult ethical questions that humans raise

we'll just leave it up to us to figure that out.

- Yeah, I mean there are some limits to what...

The same way there are limits to free speech,

there has to be some limit to the kind of stuff

that those systems might be authorized to produce,

some guardrails.

So I mean, that's one thing I've been interested in,

which is in the type of architecture

that we were discussing before,

where the output of the system

is a result of an inference to satisfy an objective.

That objective can include guardrails.

And we can put guardrails in open source systems.

I mean, if we eventually have systems

that are built with this blueprint,

we can put guardrails in those systems

that guarantee

that there is sort of a minimum set of guardrails

that make the system non-dangerous and non-toxic, et cetera.

Basic things that everybody would agree on.

And then the fine tuning that people will add

or the additional guardrails that people will add

will kind of cater to their community, whatever it is.

- And yeah, the fine tuning

would be more about the gray areas of what is hate speech,

what is dangerous and all that kind of stuff.

I mean, you've-

- [Yann] Or different value systems.

- Different value systems.

But still even with the objectives

of how to build a bio weapon, for example,

I think something you've commented on,

or at least there's a paper

where a collection of researchers

is trying to understand the social impacts of these LLMs.

And I guess one threshold that's nice

is like does the LLM make it any easier than a search would,

like a Google search would?

- Right.

So the increasing number of studies on this

seems to point to the fact that it doesn't help.

So having an LLM doesn't help you

design or build a bio weapon or a chemical weapon

if you already have access to a search engine and a library.

And so the sort of increased information you get

or the ease with which you get it doesn't really help you.

That's the first thing.

The second thing is,

it's one thing to have a list of instructions

of how to make a chemical weapon, for example, a bio weapon.

It's another thing to actually build it.

And it's much harder than you might think,

and then LLM will not help you with that.

In fact, nobody in the world,

not even like countries use bio weapons

because most of the time they have no idea

how to protect their own populations against it.

So it's too dangerous actually to kind of ever use.

And it's in fact banned by international treaties.

Chemical weapons is different.

It's also banned by treaties,

but it's the same problem.

It's difficult to use

in situations that doesn't turn against the perpetrators.

But we could ask Elon Musk.

Like I can give you a very precise list of instructions

of how you build a rocket engine.

And even if you have a team of 50 engineers

that are really experienced building it,

you're still gonna have to blow up a dozen of them

before you get one that works.

And it's the same with chemical weapons or bio weapons

or things like this.

It requires expertise in the real world

that the LLM is not gonna help you with.

- And it requires even the common sense expertise

that we've been talking about,

which is how to take language based instructions

and materialize them in the physical world

requires a lot of knowledge that's not in the instructions.

- Yeah, exactly.

A lot of biologists have posted on this actually

in response to those things

saying like do you realize how hard it is

to actually do the lab work?

Like this is not trivial.

- Yeah.

And that's Hans Moravec comes to light once again.

Just to linger on LLaMA.

Mark announced that LLaMA 3 is coming out eventually,

I don't think there's a release date,

but what are you most excited about?

First of all, LLaMA 2 that's already out there,

and maybe the future LLaMA 3, 4, 5, 6, 10,

just the future of the open source under Meta?

- Well, a number of things.

So there's gonna be like various versions of LLaMA

that are improvements of previous LLaMAs.

Bigger, better, multimodal, things like that.

And then in future generations,

systems that are capable of planning,

that really understand how the world works,

maybe are trained from video so they have some world model.

Maybe capable of the type of reasoning and planning

I was talking about earlier.

Like how long is that gonna take?

Like when is the research that is going in that direction

going to sort of feed into the product line, if you want,

of LLaMA?

I don't know, I can't tell you.

And there's a few breakthroughs

that we have to basically go through

before we can get there.

But you'll be able to monitor our progress

because we publish our research, right?

So last week we published the V-JEPA work,

which is sort of a first step

towards training systems from video.

And then the next step is gonna be world models

based on kind of this type of idea,

training from video.

There's similar work at DeepMind also taking place,

and also at UC Berkeley on world models and video.

A lot of people are working on this.

I think a lot of good ideas are appearing.

My bet is that those systems are gonna be JEPA-like,

they're not gonna be generative models.

And we'll see what the future will tell.

There's really good work at...

A gentleman called Danijar Hafner who is now DeepMind,

who's worked on kind of models of this type

that learn representations

and then use them for planning or learning tasks

by reinforcement training.

And a lot of work at Berkeley

by Pieter Abbeel, Sergey Levine,

a bunch of other people of that type.

# Chapter 9

towards training systems from video.

And then the next step is gonna be world models

based on kind of this type of idea,

training from video.

There's similar work at DeepMind also taking place,

and also at UC Berkeley on world models and video.

A lot of people are working on this.

I think a lot of good ideas are appearing.

My bet is that those systems are gonna be JEPA-like,

they're not gonna be generative models.

And we'll see what the future will tell.

There's really good work at...

A gentleman called Danijar Hafner who is now DeepMind,

who's worked on kind of models of this type

that learn representations

and then use them for planning or learning tasks

by reinforcement training.

And a lot of work at Berkeley

by Pieter Abbeel, Sergey Levine,

a bunch of other people of that type.

I'm collaborating with actually

in the context of some grants with my NYU hat.

And then collaborations also through Meta,

'cause the lab at Berkeley

is associated with Meta in some way, with FAIR.

So I think it's very exciting.

I think I'm super excited about...

I haven't been that excited

about like the direction of machine learning and AI

since 10 years ago when FAIR was started,

and before that, 30 years ago,

when we were working on,

sorry 35,

on combination nets and the early days of neural net.

So I'm super excited

because I see a path towards

potentially human level intelligence

with systems that can understand the world,

remember, plan, reason.

There is some set of ideas to make progress there

that might have a chance of working.

And I'm really excited about this.

What I like is that

somewhat we get onto like a good direction

and perhaps succeed before my brain turns to a white sauce

or before I need to retire.

(laughs)

- Yeah.

Yeah.

Are you also excited by...

Is it beautiful to you just the amount of GPUs involved,

sort of the whole training process on this much compute?

Just zooming out,

just looking at earth and humans together

have built these computing devices

and are able to train this one brain,

we then open source.

(laughs)

Like giving birth to this open source brain

trained on this gigantic compute system.

There's just the details of how to train on that,

how to build the infrastructure and the hardware,

the cooling, all of this kind of stuff.

Are you just still the most of your excitement

is in the theory aspect of it?

Meaning like the software.

- Well, I used to be a hardware guy many years ago.

(laughs) - Yes, yes, that's right.

- Decades ago.

- Hardware has improved a little bit.

Changed a little bit, yeah.

- I mean, certainly scale is necessary but not sufficient.

- [Lex] Absolutely.

- So we certainly need computation.

I mean, we're still far in terms of compute power

from what we would need

to match the compute power of the human brain.

This may occur in the next couple decades,

but we're still some ways away.

And certainly in terms of power efficiency,

we're really far.

So a lot of progress to make in hardware.

And right now a lot of the progress is not...

I mean, there's a bit coming from Silicon technology,

but a lot of it coming from architectural innovation

and quite a bit coming from like more efficient ways

of implementing the architectures that have become popular.

Basically combination of transformers and com net, right?

And so there's still some ways to go

until we are going to saturate.

We're gonna have to come up

with like new principles, new fabrication technology,

new basic components,

perhaps based on sort of different principles

than those classical digital CMOS.

- Interesting.

So you think in order to build AmI, ami,

we potentially might need some hardware innovation too?

- Well, if we wanna make it ubiquitous,

yeah, certainly.

Because we're gonna have to reduce the power consumption.

A GPU today, right?

Is half a kilowatt to a kilowatt.

Human brain is about 25 watts.

And the GPU is way below the power of human brain.

You need something like a hundred thousand

or a million to match it.

So we are off by a huge factor.

- You often say that AGI is not coming soon.

Meaning like not this year, not the next few years,

potentially farther away.

What's your basic intuition behind that?

- So first of all, it's not to be an event, right?

The idea somehow

which is popularized by science fiction in Hollywood

that somehow somebody is gonna discover the secret,

the secret to AGI or human level AI or AmI,

whatever you wanna call it,

and then turn on a machine and then we have AGI.

That's just not going to happen.

It's not going to be an event.

It's gonna be gradual progress.

Are we gonna have systems

that can learn from video how the world works

and learn good representations?

Yeah.

Before we get them to the scale and performance

that we observe in humans,

it's gonna take quite a while.

It's not gonna happen in one day.

Are we gonna get systems

that can have large amount of associated memories

so they can remember stuff?

Yeah.

But same, it's not gonna happen tomorrow.

I mean, there is some basic techniques

that need to be developed.

We have a lot of them,

but like to get this to work together with a full system

is another story.

Are we gonna have systems that can reason and plan,

perhaps along the lines of objective driven AI architectures

that I described before?

Yeah, but like before we get this to work properly,

it's gonna take a while.

And before we get all those things to work together.

And then on top of this,

have systems that can learn like hierarchical planning,

hierarchical representations,

systems that can be configured

for a lot of different situation at hands

the way the human brain can.

All of this is gonna take at least a decade,

probably much more,

because there are a lot of problems

that we're not seeing right now

that we have not encountered.

And so we don't know if there is an easy solution

within this framework.

It's not just around the corner.

I mean, I've been hearing people for the last 12, 15 years

claiming that AGI is just around the corner

and being systematically wrong.

And I knew they were wrong when they were saying it.

I called it bullshit.

(laughs)

- Why do you think people have been calling...

First of all, I mean, from the beginning of,

from the birth of the term artificial intelligence,

there has been an eternal optimism

that's perhaps unlike other technologies.

Is it Moravec's paradox?

Is it the explanation

for why people are so optimistic about AGI?

- I don't think it's just Moravec's paradox.

Moravec's paradox is a consequence

of realizing that the world is not as easy as we think.

So first of all, intelligence is not a linear thing

that you can measure with a scaler,

with a single number.

Can you say that humans are smarter than orangutans?

In some ways, yes,

but in some ways orangutans are smarter than humans

in a lot of domains

that allows them to survive in the forest, (laughing)

for example.

- So IQ is a very limited measure of intelligence.

True intelligence

is bigger than what IQ, for example, measures.

- Well, IQ can measure approximately something for humans,

but because humans kind of come

in relatively kind of uniform form, right?

- [Lex] Yeah.

- But it only measures one type of ability

that may be relevant for some tasks, but not others.

But then if you are talking about other intelligent entities

for which the basic things that are easy to them

is very different,

then it doesn't mean anything.

So intelligence is a collection of skills

and an ability to acquire new skills efficiently.

Right?

And the collection of skills

that a particular intelligent entity possess

or is capable of learning quickly

is different from the collection of skills of another one.

And because it's a multidimensional thing,

the set of skills is a high dimensional space,

you can't measure.

You cannot compare two things

as to whether one is more intelligent than the other.

It's multidimensional.

- So you push back against what are called AI doomers a lot.

Can you explain their perspective

and why you think they're wrong?

- Okay.

So AI doomers imagine all kinds of catastrophe scenarios

of how AI could escape our control

and basically kill us all. (laughs)

And that relies on a whole bunch of assumptions

that are mostly false.

So the first assumption

is that the emergence of super intelligence

could be an event.

That at some point we're going to figure out the secret

and we'll turn on a machine that is super intelligent.

And because we'd never done it before,

it's gonna take over the world and kill us all.

That is false.

It's not gonna be an event.

We're gonna have systems that are like as smart as a cat,

have all the characteristics of human level intelligence,

but their level of intelligence

would be like a cat or a parrot maybe or something.

And then we're gonna walk our way up

to kind of make those things more intelligent.

And as we make them more intelligent,

we're also gonna put some guardrails in them

and learn how to kind of put some guardrails

so they behave properly.

And we're not gonna do this with just one...

It's not gonna be one effort,

but it's gonna be lots of different people doing this.

And some of them are gonna succeed

at making intelligent systems that are controllable and safe

and have the right guardrails.

And if some other goes rogue,

then we can use the good ones to go against the rogue ones.

(laughs)

So it's gonna be smart AI police against your rogue AI.

So it's not gonna be like we're gonna be exposed

to like a single rogue AI that's gonna kill us all.

That's just not happening.

Now, there is another fallacy,

which is the fact that because the system is intelligent,

it necessarily wants to take over.

And there is several arguments

that make people scared of this,

which I think are completely false as well.

So one of them is in nature,

it seems to be that the more intelligent species

are the ones that end up dominating the other.

And even extinguishing the others

sometimes by design, sometimes just by mistake.

And so there is sort of a thinking

by which you say, well, if AI systems

are more intelligent than us,

surely they're going to eliminate us,

if not by design,

simply because they don't care about us.

And that's just preposterous for a number of reasons.

First reason is they're not going to be a species.

They're not gonna be a species that competes with us.

They're not gonna have the desire to dominate

because the desire to dominate

is something that has to be hardwired

into an intelligent system.

It is hardwired in humans,

it is hardwired in baboons,

in chimpanzees, in wolves,

not in orangutans.

The species in which this desire to dominate or submit

or attain status in other ways

is specific to social species.

Non-social species like orangutans don't have it.

Right?

And they are as smart as we are, almost.

Right?

- And to you, there's not significant incentive

for humans to encode that into the AI systems.

And to the degree they do,

there'll be other AIs that sort of punish them for it.

Out-compete them over-

- Well, there's all kinds of incentive

to make AI systems submissive to humans.

Right? - [Lex] Right.

- I mean, this is the way we're gonna build them, right?

And so then people say, oh, but look at LLMs.

LLMs are not controllable.

And they're right,

LLMs are not controllable.

But objective driven AI,

so systems that derive their answers

by optimization of an objective

means they have to optimize this objective,

and that objective can include guardrails.

One guardrail is obey humans.

Another guardrail is don't obey humans

if it's hurting other humans-

- I've heard that before somewhere, I don't remember-

- [Yann] Yes. (Lex laughs)

Maybe in a book. (laughs)

- Yeah.

But speaking of that book,

could there be unintended consequences also

from all of this?

- No, of course.

So this is not a simple problem, right?

I mean designing those guardrails

so that the system behaves properly

is not gonna be a simple issue

for which there is a silver bullet,

for which you have a mathematical proof

that the system can be safe.

It's gonna be very progressive,

iterative design system

where we put those guardrails

in such a way that the system behave properly.

And sometimes they're going to do something

that was unexpected because the guardrail wasn't right,

and we're gonna correct them so that they do it right.

The idea somehow that we can't get it slightly wrong,

because if we get it slightly wrong we all die,

is ridiculous.

We're just gonna go progressively.

The analogy I've used many times is turbojet design.

How did we figure out

how to make turbojets so unbelievably reliable, right?

I mean, those are like incredibly complex pieces of hardware

that run at really high temperatures

for 20 hours at a time sometimes.

And we can fly halfway around the world

on a two engine jet liner at near the speed of sound.

Like how incredible is this?

It is just unbelievable.

And did we do this

because we invented like a general principle

of how to make turbojets safe?

No, it took decades

to kind of fine tune the design of those systems

so that they were safe.

Is there a separate group

within General Electric or Snecma or whatever

that is specialized in turbojet safety?

No.

The design is all about safety.

Because a better turbojet is also a safer turbojet,

a more reliable one.

It's the same for AI.

Like do you need specific provisions to make AI safe?

No, you need to make better AI systems

and they will be safe

because they are designed to be more useful

# Chapter 10

Like how incredible is this?

It is just unbelievable.

And did we do this

because we invented like a general principle

of how to make turbojets safe?

No, it took decades

to kind of fine tune the design of those systems

so that they were safe.

Is there a separate group

within General Electric or Snecma or whatever

that is specialized in turbojet safety?

No.

The design is all about safety.

Because a better turbojet is also a safer turbojet,

a more reliable one.

It's the same for AI.

Like do you need specific provisions to make AI safe?

No, you need to make better AI systems

and they will be safe

because they are designed to be more useful

and more controllable.

- So let's imagine a system,

AI system that's able to be incredibly convincing

and can convince you of anything.

I can at least imagine such a system.

And I can see such a system be weapon-like,

because it can control people's minds,

we're pretty gullible.

We want to believe a thing.

And you can have an AI system that controls it

and you could see governments using that as a weapon.

So do you think if you imagine such a system,

there's any parallel to something like nuclear weapons?

- [Yann] No.

- So why is that technology different?

So you're saying there's going to be gradual development?

- [Yann] Yeah.

- I mean it might be rapid,

but they'll be iterative.

And then we'll be able to kind of respond and so on.

- So that AI system designed by Vladimir Putin or whatever,

or his minions (laughing)

is gonna be like trying to talk to every American

to convince them to vote for-

- [Lex] Whoever.

- Whoever pleases Putin or whatever.

Or rile people up against each other

as they've been trying to do.

They're not gonna be talking to you,

they're gonna be talking to your AI assistant

which is going to be as smart as theirs, right?

Because as I said, in the future,

every single one of your interaction with the digital world

will be mediated by your AI assistant.

So the first thing you're gonna ask is, is this a scam?

Like is this thing like telling me the truth?

Like it's not even going to be able to get to you

because it's only going to talk to your AI assistant,

and your AI is not even going to...

It's gonna be like a spam filter, right?

You're not even seeing the email, the spam email, right?

It's automatically put in a folder that you never see.

It's gonna be the same thing.

That AI system that tries to convince you of something,

it's gonna be talking to an AI system

which is gonna be at least as smart as it.

And is gonna say, this is spam. (laughs)

It's not even going to bring it to your attention.

- So to you it's very difficult for any one AI system

to take such a big leap ahead

to where it can convince even the other AI systems?

So like there's always going to be this kind of race

where nobody's way ahead?

- That's the history of the world.

History of the world

is whenever there is a progress someplace,

there is a countermeasure.

And it's a cat and mouse game.

- Mostly yes,

but this is why nuclear weapons are so interesting

because that was such a powerful weapon

that it mattered who got it first.

That you could imagine Hitler, Stalin, Mao

getting the weapon first

and that having a different kind of impact on the world

than the United States getting the weapon first.

To you, nuclear weapons is like...

You don't imagine a breakthrough discovery

and then Manhattan project like effort for AI?

- No.

As I said, it's not going to be an event.

It's gonna be continuous progress.

And whenever one breakthrough occurs,

it's gonna be widely disseminated really quickly.

Probably first within industry.

I mean, this is not a domain

where government or military organizations

are particularly innovative,

and they're in fact way behind.

And so this is gonna come from industry.

And this kind of information disseminates extremely quickly.

We've seen this over the last few years, right?

Where you have a new...

Like even take AlphaGo.

This was reproduced within three months

even without like particularly detailed information, right?

- Yeah.

This is an industry that's not good at secrecy.

(laughs)

- But even if there is,

just the fact that you know that something is possible

makes you like realize

that it's worth investing the time to actually do it.

You may be the second person to do it but you'll do it.

Say for all the innovations

of self supervised running transformers,

decoder only architectures, LLMs.

I mean those things,

you don't need to know exactly the details of how they work

to know that it's possible

because it's deployed and then it's getting reproduced.

And then people who work for those companies move.

They go from one company to another.

And the information disseminates.

What makes the success of the US tech industry

and Silicon Valley in particular, is exactly that,

is because information circulates really, really quickly

and disseminates very quickly.

And so the whole region sort of is ahead

because of that circulation of information.

- Maybe just to linger on the psychology of AI doomers.

You give in the classic Yann LeCun way,

a pretty good example

of just when a new technology comes to be,

you say engineer says,

"I invented this new thing, I call it a ballpen."

And then the TwitterSphere responds,

"OMG people could write horrible things with it

like misinformation, propaganda, hate speech.

Ban it now!"

Then writing doomers come in,

akin to the AI doomers,

"imagine if everyone can get a ballpen.

This could destroy society.

There should be a law

against using ballpen to write hate speech,

regulate ballpens now."

And then the pencil industry mogul says,

"yeah, ballpens are very dangerous,

unlike pencil writing which is erasable,

ballpen writing stays forever.

Government should require a license for a pen manufacturer."

I mean, this does seem to be part of human psychology

when it comes up against new technology.

What deep insights can you speak to about this?

- Well, there is a natural fear of new technology

and the impact it can have on society.

And people have kind of instinctive reaction

to the world they know

being threatened by major transformations

that are either cultural phenomena

or technological revolutions.

And they fear for their culture,

they fear for their job,

they fear for the future of their children

and their way of life, right?

So any change is feared.

And you see this along history,

like any technological revolution or cultural phenomenon

was always accompanied by groups or reaction in the media

that basically attributed all the problems,

the current problems of society

to that particular change, right?

Electricity was going to kill everyone at some point.

The train was going to be a horrible thing

because you can't breathe past 50 kilometers an hour.

And so there's a wonderful website

called a Pessimists Archive, right?

Which has all those newspaper clips (laughing)

of all the horrible things people imagined would arrive

because of either technological innovation

or a cultural phenomenon.

Wonderful examples of jazz or comic books

being blamed for unemployment

or young people not wanting to work anymore

and things like that, right?

And that has existed for centuries.

And it's knee jerk reactions.

The question is do we embrace change or do we resist it?

And what are the real dangers

as opposed to the imagined imagined ones?

- So people worry about...

I think one thing they worry about with big tech,

something we've been talking about over and over

but I think worth mentioning again,

they worry about how powerful AI will be

and they worry about it

being in the hands of one centralized power

of just a handful of central control.

And so that's the skepticism with big tech.

These companies can make a huge amount of money

and control this technology.

And by so doing,

take advantage, abuse the little guy in society.

- Well, that's exactly why we need open source platforms.

- Yeah.

I just wanted to... (laughs)

Nail the point home more and more.

- [Yann] Yes.

- So let me ask you on your...

Like I said, you do get a little bit

flavorful on the internet.

Joscha Bach tweeted something that you LOL'd at

in reference to HAL 9,000.

Quote,

"I appreciate your argument

and I fully understand your frustration,

but whether the pod bay doors should be opened or closed

is a complex and nuanced issue."

So you're at the head of Meta AI.

This is something that really worries me,

that our AI overlords

will speak down to us with corporate speak of this nature

and you sort of resist that with your way of being.

Is this something you can just comment on

sort of working at a big company,

how you can avoid the over fearing, I suppose,

the through caution create harm?

- Yeah.

Again, I think the answer to this is open source platforms

and then enabling a widely diverse set of people

to build AI assistants

that represent the diversity

of cultures, opinions, languages,

and value systems across the world.

So that you're not bound to just be brainwashed

by a particular way of thinking

because of a single AI entity.

So I mean, I think it's a really, really important question

for society.

And the problem I'm seeing,

which is why I've been so vocal

and sometimes a little sardonic about it-

- Never stop.

Never stop, Yann.

(both laugh)

We love it. - Is because I see the danger

of this concentration of power

through proprietary AI systems

as a much bigger danger than everything else.

That if we really want diversity of opinion AI systems

that in the future

that we'll all be interacting through AI systems,

we need those to be diverse

for the preservation of a diversity of ideas

and creeds and political opinions and whatever,

and the preservation of democracy.

And what works against this

is people who think that for reasons of security,

we should keep AI systems under lock and key

because it's too dangerous

to put it in the hands of everybody

because it could be used by terrorists or something.

That would lead to potentially a very bad future

in which all of our information diet

is controlled by a small number of companies

through proprietary systems.

- So you trust humans with this technology

to build systems that are on the whole good for humanity?

- Isn't that what democracy and free speech is all about?

- I think so.

- Do you trust institutions to do the right thing?

Do you trust people to do the right thing?

And yeah, there's bad people who are gonna do bad things,

but they're not going to have superior technology

to the good people.

So then it's gonna be my good AI against your bad AI, right?

I mean it's the examples that we were just talking about

of maybe some rogue country will build some AI system

that's gonna try to convince everybody

to go into a civil war or something

or elect a favorable ruler.

But then they will have to go past our AI systems, right?

(laughs)

- An AI system with a strong Russian accent

will be trying to convince our-

- And doesn't put any articles in their sentences.

(both laugh)

- Well, it'll be at the very least, absurdly comedic.

Okay.

So since we talked about sort of the physical reality,

I'd love to ask your vision of the future with robots

in this physical reality.

So many of the kinds of intelligence

you've been speaking about

would empower robots

to be more effective collaborators with us humans.

So since Tesla's Optimus team

has been showing us some progress in humanoid robots,

I think it really reinvigorated the whole industry

that I think Boston Dynamics has been leading

for a very, very long time.

So now there's all kinds of companies,

Figure AI, obviously Boston Dynamics-

- [Yann] Unitree.

- Unitree.

But there's like a lot of them.

It's great.

It's great.

I mean I love it.

So do you think there'll be millions of humanoid robots

walking around soon?

- Not soon, but it's gonna happen.

Like the next decade

I think is gonna be really interesting in robots.

Like the emergence of the robotics industry

has been in the waiting for 10, 20 years,

without really emerging

other than for like kind of pre-program behavior

and stuff like that.

And the main issue is again, the Moravec's paradox.

Like how do we get the systems

to understand how the world works

and kind of plan actions?

And so we can do it for really specialized tasks.

# Chapter 11

- Unitree.

But there's like a lot of them.

It's great.

It's great.

I mean I love it.

So do you think there'll be millions of humanoid robots

walking around soon?

- Not soon, but it's gonna happen.

Like the next decade

I think is gonna be really interesting in robots.

Like the emergence of the robotics industry

has been in the waiting for 10, 20 years,

without really emerging

other than for like kind of pre-program behavior

and stuff like that.

And the main issue is again, the Moravec's paradox.

Like how do we get the systems

to understand how the world works

and kind of plan actions?

And so we can do it for really specialized tasks.

And the way Boston Dynamics goes about it

is basically with a lot of handcrafted dynamical models

and careful planning in advance,

which is very classical robotics with a lot of innovation,

a little bit of perception,

but it's still not...

Like they can't build a domestic robot, right?

And we're still some distance away

from completely autonomous level five driving.

And we're certainly very far away

from having level five autonomous driving

by a system that can train itself

by driving 20 hours, like any 17-year-old.

So until we have, again, world models,

systems that can train themselves

to understand how the world works,

we're not gonna have significant progress in robotics.

So a lot of the people

working on robotic hardware at the moment

are betting or banking

on the fact that AI

is gonna make sufficient progress towards that.

- And they're hoping to discover a product in it too-

- [Yann] Yeah.

- Before you have a really strong world model,

there'll be an almost strong world model.

And people are trying to find a product

in a clumsy robot, I suppose.

Like not a perfectly efficient robot.

So there's the factory setting

where humanoid robots

can help automate some aspects of the factory.

I think that's a crazy difficult task

'cause of all the safety required

and all this kind of stuff,

I think in the home is more interesting.

But then you start to think...

I think you mentioned loading the dishwasher, right?

- [Yann] Yeah.

- Like I suppose that's one of the main problems

you're working on.

- I mean there's cleaning up. (laughs)

- [Lex] Yeah.

- Cleaning the house,

clearing up the table after a meal,

washing the dishes, all those tasks, cooking.

I mean all the tasks that in principle could be automated

but are actually incredibly sophisticated,

really complicated.

- But even just basic navigation

around a space full of uncertainty.

- That sort of works.

Like you can sort of do this now.

Navigation is fine.

- Well, navigation in a way that's compelling to us humans

is a different thing.

- Yeah.

It's not gonna be necessarily...

I mean we have demos actually

'cause there is a so-called embodied AI group at FAIR

and they've been not building their own robots

but using commercial robots.

And you can tell the robot dog like go to the fridge

and they can actually open the fridge

and they can probably pick up a can in the fridge

and stuff like that and bring it to you.

So it can navigate,

it can grab objects

as long as it's been trained to recognize them,

which vision systems work pretty well nowadays.

But it's not like a completely general robot

that would be sophisticated enough

to do things like clearing up the dinner table.

(laughs)

- Yeah, to me that's an exciting future

of getting humanoid robots.

Robots in general in the home more and more

because it gets humans

to really directly interact with AI systems

in the physical space.

And in so doing it allows us

to philosophically, psychologically explore

our relationships with robots.

It can be really, really interesting.

So I hope you make progress on the whole JEPA thing soon.

(laughs)

- Well, I mean, I hope things can work as planned.

I mean, again, we've been like kinda working on this idea

of self supervised learning from video for 10 years.

And only made significant progress in the last two or three.

- And actually you've mentioned

that there's a lot of interesting breakthroughs

that can happen without having access to a lot of compute.

So if you're interested in doing a PhD

in this kind of stuff,

there's a lot of possibilities still

to do innovative work.

So like what advice would you give

to a undergrad that's looking to go to grad school

and do a PhD?

- So basically, I've listed them already.

This idea of how do you train a world model by observation?

And you don't have to train necessarily

on gigantic data sets.

I mean, it could turn out to be necessary

to actually train on large data sets

to have emergent properties like we have with LLMs.

But I think there is a lot of good ideas that can be done

without necessarily scaling up.

Then there is how do you do planning

with a learn world model?

If the world the system evolves in

is not the physical world,

but is the world of let's say the internet

or some sort of world

of where an action consists

in doing a search in a search engine

or interrogating a database,

or running a simulation

or calling a calculator

or solving a differential equation,

how do you get a system

to actually plan a sequence of actions

to give the solution to a problem?

And so the question of planning

is not just a question of planning physical actions,

it could be planning actions to use tools

for a dialogue system

or for any kind of intelligence system.

And there's some work on this but not a huge amount.

Some work at FAIR,

one called Toolformer, which was a couple years ago

and some more recent work on planning,

but I don't think we have like a good solution

for any of that.

Then there is the question of hierarchical planning.

So the example I mentioned

of planning a trip from New York to Paris,

that's hierarchical,

but almost every action that we take

involves hierarchical planning in some sense.

And we really have absolutely no idea how to do this.

Like there's zero demonstration

of hierarchical planning in AI,

where the various levels of representations

that are necessary have been learned.

We can do like two level hierarchical planning

when we design the two levels.

So for example, you have like a dog legged robot, right?

You want it to go from the living room to the kitchen.

You can plan a path that avoids the obstacle.

And then you can send this to a lower level planner

that figures out how to move the legs

to kind of follow that trajectories, right?

So that works,

but that two level planning is designed by hand, right?

We specify what the proper levels of abstraction,

the representation at each level of abstraction have to be.

How do you learn this?

How do you learn that hierarchical representation

of action plans, right?

With com nets and deep learning,

we can train the system

to learn hierarchical representations of percepts.

What is the equivalent

when what you're trying to represent are action plans?

- For action plans.

Yeah.

So you want basically a robot dog or humanoid robot

that turns on and travels from New York to Paris

all by itself.

- [Yann] For example.

- All right.

It might have some trouble at the TSA but-

- No, but even doing something fairly simple

like a household task.

- [Lex] Sure.

- Like cooking or something.

- Yeah.

There's a lot involved.

It's a super complex task.

Once again, we take it for granted.

What hope do you have for the future of humanity?

We're talking about so many exciting technologies,

so many exciting possibilities.

What gives you hope when you look out

over the next 10, 20, 50, 100 years?

If you look at social media,

there's wars going on, there's division, there's hatred,

all this kind of stuff that's also part of humanity.

But amidst all that, what gives you hope?

- I love that question.

We can make humanity smarter with AI.

Okay?

I mean AI basically will amplify human intelligence.

It's as if every one of us

will have a staff of smart AI assistants.

They might be smarter than us.

They'll do our bidding,

perhaps execute a task

in ways that are much better than we could do ourselves

because they'd be smarter than us.

And so it's like everyone would be the boss

of a staff of super smart virtual people.

So we shouldn't feel threatened by this

any more than we should feel threatened

by being the manager of a group of people,

some of whom are more intelligent than us.

I certainly have a lot of experience with this.

(laughs)

Of having people working with me who are smarter than me.

That's actually a wonderful thing.

So having machines that are smarter than us,

that assist us in all of our tasks, our daily lives,

whether it's professional or personal,

I think would be an absolutely wonderful thing.

Because intelligence is the commodity

that is most in demand.

I mean, all the mistakes that humanity makes

is because of lack of intelligence, really,

or lack of knowledge, which is related.

So making people smarter which can only be better.

I mean, for the same reason

that public education is a good thing

and books are a good thing,

and the internet is also a good thing, intrinsically.

And even social networks are a good thing

if you run them properly.

(laughs)

It's difficult, but you can.

Because it helps the communication

of information and knowledge

and the transmission of knowledge.

So AI is gonna make humanity smarter.

And the analogy I've been using

is the fact that perhaps an equivalent event

in the history of humanity

to what might be provided by generalization of AI assistant

is the invention of the printing press.

It made everybody smarter.

The fact that people could have access to books.

Books were a lot cheaper than they were before.

And so a lot more people had an incentive to learn to read,

which wasn't the case before.

And people became smarter.

It enabled the enlightenment, right?

There wouldn't be an enlightenment

without the printing press.

It enabled philosophy, rationalism,

escape from religious doctrine,

democracy, science.

And certainly without this

there wouldn't have been the American Revolution

or the French Revolution.

And so we'll still be under feudal regimes perhaps.

And so it completely transformed the world

because people became smarter

and kinda learned about things.

Now, it also created 200 years

of essentially religious conflicts in Europe, right?

Because the first thing that people read was the Bible

and realized that

perhaps there was a different interpretation of the Bible

than what the priests were telling them.

And so that created the Protestant movement

and created a rift.

And in fact, the Catholic church

didn't like the idea of the printing press

but they had no choice.

And so it had some bad effects and some good effects.

I don't think anyone today

would say that the invention of the printing press

had an overall negative effect

despite the fact that it created 200 years

of religious conflicts in Europe.

Now compare this,

and I was very proud of myself

to come up with this analogy,

but realized someone else came with the same idea before me.

Compare this with what happened in the Ottoman Empire.

The Ottoman Empire banned the printing press for 200 years.

And it didn't ban it for all languages,

only for Arabic.

You could actually print books

in Latin or Hebrew or whatever in the Ottoman Empire,

just not in Arabic.

And I thought it was because

the rulers just wanted to preserve

the control over the population and the dogma,

religious dogma and everything.

But after talking with the UAE Minister of AI,

Omar Al Olama,

he told me no, there was another reason.

And the other reason was that

it was to preserve the corporation of calligraphers, right?

There's like an art form

which is writing those beautiful Arabic poems

or whatever religious text in this thing.

And it was very powerful corporation of scribes basically

that kinda run a big chunk of the empire.

And we couldn't put them out of business.

So they banned the bridging press

in part to protect that business.

Now, what's the analogy for AI today?

Like who are we protecting by banning AI?

Like who are the people who are asking that AI be regulated

to protect their jobs?

And of course, it's a real question

of what is gonna be the effect

of technological transformation like AI

on the job market and the labor market?

And there are economists

who are much more expert at this than I am,

but when I talk to them,

they tell us we're not gonna run out of job.

This is not gonna cause mass unemployment.

This is just gonna be gradual shift

of different professions.

The professions that are gonna be hot

10 or 15 years from now,

we have no idea today what they're gonna be.

The same way if we go back 20 years in the past,

like who could have thought 20 years ago

that like the hottest job,

even like 5, 10 years ago was mobile app developer?

# Chapter 12

Like who are the people who are asking that AI be regulated

to protect their jobs?

And of course, it's a real question

of what is gonna be the effect

of technological transformation like AI

on the job market and the labor market?

And there are economists

who are much more expert at this than I am,

but when I talk to them,

they tell us we're not gonna run out of job.

This is not gonna cause mass unemployment.

This is just gonna be gradual shift

of different professions.

The professions that are gonna be hot

10 or 15 years from now,

we have no idea today what they're gonna be.

The same way if we go back 20 years in the past,

like who could have thought 20 years ago

that like the hottest job,

even like 5, 10 years ago was mobile app developer?

Like smartphones weren't invented.

- Most of the jobs of the future

might be in the Metaverse. (laughs)

- Well, it could be.

Yeah.

- But the point is you can't possibly predict.

But you're right.

I mean, you've made a lot of strong points.

And I believe that people are fundamentally good,

and so if AI, especially open source AI

can make them smarter,

it just empowers the goodness in humans.

- So I share that feeling.

Okay?

I think people are fundamentally good. (laughing)

And in fact a lot of doomers are doomers

because they don't think that people are fundamentally good.

And they either don't trust people

or they don't trust the institution to do the right thing

so that people behave properly.

- Well, I think both you and I believe in humanity,

and I think I speak for a lot of people

in saying thank you for pushing the open source movement,

pushing to making both research and AI open source,

making it available to people,

and also the models themselves,

making that open source also.

So thank you for that.

And thank you for speaking your mind

in such colorful and beautiful ways on the internet.

I hope you never stop.

You're one of the most fun people I know

and get to be a fan of.

So Yann, thank you for speaking to me once again,

and thank you for being you.

- Thank you Lex.

- Thanks for listening to this conversation with Yann LeCun.

To support this podcast,

please check out our sponsors in the description.

And now let me leave you with some words

from Arthur C. Clarke,

"the only way to discover the limits of the possible

is to go beyond them into the impossible."

Thank you for listening and hope to see you next time.

