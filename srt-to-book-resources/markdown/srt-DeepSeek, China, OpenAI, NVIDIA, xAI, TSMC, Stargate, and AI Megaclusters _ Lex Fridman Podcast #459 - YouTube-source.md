# Chapter 1

- The following is a conversation

with Dylan Patel and Nathan Lambert.

Dylan runs SemiAnalysis, a well-respected research

and analysis company that specializes in semiconductors,

GPUs, CPUs, and AI hardware in general.

Nathan is a research scientist at the Allen Institute for AI

and is the author

of the amazing blog on AI called Interconnects.

They are both highly respected, read,

and listened to by the experts, researchers,

and engineers in the field of AI.

And personally, I'm just a fan of the two of them.

So, I used the DeepSeek moment

that shook the AI world a bit

as an opportunity to sit down with them and lay it all out.

From DeepSeek, OpenAI, Google xAI, Meta, Anthropic,

to Nvidia and DSMC, and to US, China, Taiwan relations,

and everything else

that is happening at the cutting edge of AI.

This conversation is a deep dive

into many critical aspects of the AI industry.

While it does get super technical, we try to make sure

that it's still accessible to folks outside of the AI field

by defining terms, stating important concepts explicitly,

spelling out acronyms, and in general, always moving across

the several layers of abstraction and levels of detail.

There is a lot of hype

in the media about what AI is and isn't.

The purpose of this podcast

in part is to cut through the hype,

through the bullshit,

and the low resolution analysis,

and to discuss in detail how stuff works

and what the implications are.

Let me also, if I may comment

on the new OpenAI o3-mini reasoning model.

The release of which we were anticipating

during the conversation,

and it did indeed come out right after.

Its capabilities and costs

are on par with our expectations as we stated.

OpenAI o3-mini is indeed a great model,

but it should be stated that DeeSeek-R1

has similar performance on benchmarks is still cheaper

and it reveals its chain of thought reasoning,

which o3-mini does not.

It only shows a summary of the reasoning.

Plus, R1 is open-weight and o3-mini is not.

By the way, I got a chance to play with o3-mini.

And anecdotal vibe check wise, I felt that o3-mini,

specifically o3-mini-high is better than R1.

Still for me personally,

I find that Claude Sonnet 3.5

is the best model for programming,

except for tricky cases,

where I will use o1 Pro to brainstorm.

Either way, many more better AI models will come,

including reasoning models

both from American and Chinese companies.

They'll continue to shift the cost curve.

But the quote, DeepSeek moment is indeed real.

I think it will still be remembered five years from now

as a pivotal event in tech history,

due in part to the geopolitical implications,

but for other reasons to, as we discuss in detail

from many perspectives in this conversation.

This is the "Lex Fridman Podcast".

To support it,

please check out our sponsors in the description.

And now, dear friends,

here's Dylan Patel and Nathan Lambert.

A lot of people are curious

to understand China's DeepSeek AI models,

so let's lay it out.

Nathan, can you describe what DeepSeek-V3

and DeepSeek-R1 are, how they work, how they're trained?

Let's look at the big picture,

and then we'll zoom in on the details.

- Yeah, so DeepSeek-V3 is a new mixture of experts,

transformer language model from DeepSeek

who is based in China.

They have some new specifics

in the model that we'll get into.

Largely this is a open-weight model

and it's a instruction model

like what you would use in ChatGPT.

They also release what is called the base model,

which is before these techniques of post-training.

Most people use instruction models today

and those are what's served in all sorts of applications.

This was released on, I believe December 26th or that week.

And then, weeks later,

on January 20th, DeepSeek released DeepSeek-R1,

which is a reasoning model,

which really accelerated a lot of this discussion.

This reasoning model, it has a lot

of overlapping training steps to DeepSeek-V3,

and it's confusing that you have a base model

called V3 that you do something to, to get a chat model,

and then you do some different things

to get a reasoning model.

I think a lot of the AI industry

is going through this challenge of communications right now

where OpenAI makes fun of their own naming schemes.

They have GPT-4o, they have OpenAI o1.

And there's a lot of types of models.

So, we're gonna break down what each of them are.

There's a lot of technical specifics on training,

and go through 'em high level to specific,

and go through each of them.

- There's so many places we can go here,

but maybe let's go to open-weights first.

What does it mean for model to be open-weights

and what are the different flavors

of open source in general?

- Yeah, so this discussion

has been going on for a long time in AI.

It became more important since ChatGPT

or more focal since ChatGPT at the end of 2022.

Open-weights is the accepted term for when model weights

of a language model are available

on the internet for people to download,

those weights can have different licenses,

which is the effectively the terms

by which you can use the model.

There are licenses that come from history

and open source software.

There are licenses that are designed

by companies specifically,

all of Llama, DeepSeek, Qwen, Mistral,

these popular names in open-weight models,

have some of their own licenses.

It's complicated,

'cause not all the same models have the same terms.

The big debate is on what makes a model open-weight.

It's like why are we saying this term?

It's a mouthful.

It sounds close to open source but it's not the same.

There's still a lot of debate on the definition

and soul of open source AI.

Open source software

has a rich history on freedom to modify,

freedom to take on your own,

freedom for many restrictions

on how you would use the software,

and what that means for AI is still being defined.

So, for what I do, I work at the Allen Institute for AI.

We're a nonprofit.

We want to make AI open for everybody

and we try to lead on what we think is truly open source.

There's not full agreement in the community,

but for us, that means releasing the training data,

releasing the training code,

and then also having open-weights like this.

And we'll get into the details of the models.

And again and again, as we try to get deeper

into how the models were trained,

we will say things like the data processing,

data filtering, data quality

is the number one determinant of the model quality.

And then, a lot of the training code is the determinant

on how long it takes to train

and how fast your experimentation is.

So, without fully open source models

where you have access to this data,

it is hard to know or it's harder to replicate.

So, we'll get into cost numbers for DeepSeek-V3

on mostly GPU hours

and how much you could pay to rent those yourselves.

But without the data,

the replication cost is going to be far, far higher.

And same goes for the code.

- We should also say that this is probably one

of the more open models out of the frontier models.

- Yes. - So, in this full spectrum

where probably the fullest open source, like you said,

open code, open data, open-weights.

This is not open code, this is probably not open data,

and this is open-weights,

and the licensing is MIT license, or it's...

I mean, there's some nuance in the different models,

but it's towards the free,

in terms of the open source movement,

these are the good guys. - Yeah.

DeepSeek is doing fantastic work

for disseminating understanding of AI.

Their papers are extremely detailed in what they do.

And for other teams around the world,

they're very actionable in terms

of improving your own training techniques.

And we'll talk about licenses more.

The DeepSeek-R1 model has a very permissive license.

It's called the MIT license.

That effectively means there's no downstream restrictions

on commercial use, there's no use case restrictions.

You can use the outputs

from the models to create synthetic data.

And this is all fantastic.

I think the closest peer is something like Llama

where you have the weights and you have a technical report.

And the technical report is very good for Llama.

One of the most read PDFs of the year last year

is the Llama 3 paper,

but in some ways, it's slightly less actionable.

It has less details on the training specifics,

I think less plots, and so on.

And the Llama 3 license is more restrictive than MIT.

And then, between the DeepSeek custom license

and the Llama license,

we could get into this whole rabbit hole.

I think we'll make sure we want

to go down the license rabbit hole before we do specifics.

- Yeah, and so it should be stated that one

of the implications that DeepSeek puts pressure on Llama

and everybody else on OpenAI to push towards open source,

and that's the other side of open source

that you mentioned

is how much is published in detail about it.

So, how open are you with the insights behind the code?

So, how good is the technical reports?

Are they hand wavy or is there actual details in there?

And that's one of the things

that DeepSeek did well is they publish a lot of the details.

- Yeah, especially in the DeepSeek-V3,

which is their pre-training paper, they were very clear

that they are doing interventions

on the technical stack that go at many different levels.

For example, to get highly efficient training,

they're making modifications at

or below the CUDA layer for Nvidia chips.

I have never worked there myself.

And there are a few people in the world

that do that very well and some of them are at DeepSeek.

And these types of people are at DeepSeek

and leading American Frontier Labs,

but there are not many places.

- To help people understand

the other implication of open-weights,

just there's a topic we return to often here.

So, there's a fear that China, the nation,

might have interest in stealing American data,

violating privacy of American citizens.

What can we say about open-weights

to help us understand what the weights are able to do

- Yeah. - in terms

of stealing people's data?

- Yeah, so these weights

that you can download from Hugging Face

or other platforms are very big matrices of numbers.

You can download them to a computer

in your own house that has no internet

and you can run this model,

and you're totally in control of your data.

That is something that is different

than how a lot of language model usage

is actually done today, which is mostly through APIs

where you send your prompt to GPUs run by certain companies,

and these companies will have different distributions

and policies on how your data is stored,

if it is used to train future models,

where it is stored, if it is encrypted, and so on.

So, the open-weights are you have your fate

of data in your own hands

and that is something that is deeply connected

to the soul of open source.

- So, it's not the model that steals your data,

it's whoever's hosting the model,

which could be China if you're using the DeepSeek app,

or it could be Perplexity.

You're trusting them with your data.

Or OpenAI, you're trusting them with your data.

And some of these are American companies,

some of of these are Chinese companies,

but the model itself is not doing the stealing,

it's the host.

All right. So, back to the basics.

What's the difference between DeepSeek-V3 and DeepSeek-R1?

Can we try to lay out

the confusion potential? - Yes.

So, for one, I have very understanding

of many people being confused by these two model names.

So, I would say the best way to think about this

is that when training a language model,

you have what is called pre-training,

which is when you're predicting the large amounts

of mostly internet text.

You're trying to predict the next-token.

And what to know about these new DeepSeek models

is that they do this internet large-scale pre-training once

to get what is called DeepSeek-V3 base.

This is a base model.

It's just going to finish your sentences for you.

It's going to be harder to work with than ChatGPT.

And then, what DeepSeek did

is they've done two different post-training regimes

to make the models have specific desirable behaviors.

So, what is the more normal model

in terms of the last few years of AI

and instruct model, a chat model,

a, quote, unquote, "aligned model", a helpful model,

there are many ways to describe this,

is more standard post-training.

So, this is things like instruction tuning,

reinforcement learning from human feedback.

We'll get into some of these words.

And this is what they did to create the DeepSeek-V3 model.

This was the first model to be released

and it is very highly performant,

competitive with GPT-4, Llama 405b, so on.

And then, when this release was happening,

we don't know their exact timeline,

or soon after they were finishing the training

of a different training process

from the same next-token prediction-based model

that I talked about,

which is when this new reasoning training

that people have heard about comes in,

in order to create the model that is called DeepSeek-R1.

The R through this conversation

is good for grounding for reasoning.

And the name is also similar to OpenAI's o1,

which is the other reasoning model

that people have heard about.

And we'll have to break down the training

for R1 in more detail,

because for one, we have a paper detailing it,

but also, it is a far newer set of techniques

for the AI community.

So, it is a much more rapidly evolving area of research.

- Maybe we should also say the big two categories

of training of pre-training and post-training.

These umbrella terms that people use.

So, what is pre-training and what is post-training,

and what are the different flavors of things

underneath post-training umbrella?

- Yeah, so pre-training, I'm using some of the same words

to really get the message across,

is you're doing what is called autoregressive prediction

to predict the next-token in a series of documents.

This is done over standard practice is trillions of tokens.

So, this is a ton of data

that is mostly scraped from the web.

And some of DeepSeek's earlier papers,

they talk about their training data

being distilled for math, I shouldn't use this word yet,

but taken from Common Crawl,

and that's a public access that anyone listening to this

could go download data from the Common Crawl website.

# Chapter 2

So, it is a much more rapidly evolving area of research.

- Maybe we should also say the big two categories

of training of pre-training and post-training.

These umbrella terms that people use.

So, what is pre-training and what is post-training,

and what are the different flavors of things

underneath post-training umbrella?

- Yeah, so pre-training, I'm using some of the same words

to really get the message across,

is you're doing what is called autoregressive prediction

to predict the next-token in a series of documents.

This is done over standard practice is trillions of tokens.

So, this is a ton of data

that is mostly scraped from the web.

And some of DeepSeek's earlier papers,

they talk about their training data

being distilled for math, I shouldn't use this word yet,

but taken from Common Crawl,

and that's a public access that anyone listening to this

could go download data from the Common Crawl website.

This is a crawler that is maintained publicly.

Yes, other tech companies

eventually shift to their own crawler

and DeepSeek likely has done this as well,

as most Frontier Labs do.

But this sort of data is something

that people can get started with

and you're just predicting text in a series of documents.

This can be scaled to be very efficient

and there's a lot of numbers

that are thrown around in AI training,

like how many floating point operations or FLOPS are used.

And then, you can also look

at how many hours of these GPUs that are used.

And it's largely one loss function

taken to a very large amount (chuckles) of compute usage.

You set up really efficient systems.

And then, at the end of that, you have this base model.

And pre-training is where there is a lot more

of complexity in terms

of how the process is emerging or evolving,

and the different types of training losses that you'll use.

I think this is a lot of techniques

grounded in the natural language processing literature.

The oldest technique which is still used today

is something called instruction tuning,

or also known as supervised fine-tuning.

These acronyms will be IFT or SFT

that people really go back and forth throughout them,

and I'll probably do the same,

which is where you add this formatting to the model,

where it knows to take a question

that is like explain the history of the Roman Empire to me.

Or something, a sort of question

you'll see on Reddit or Stack Overflow,

and then the model will respond

in a information-dense but presentable manner.

The core of that formatting

is in this instruction tuning phase.

And then, there's two other categories

of loss functions that are being used today.

One I'll classify as preference fine-tuning.

Preference fine-tuning is a generalized term

for what came out of reinforcement learning

from human feedback, which is RLHF.

This reinforcement learning from human feedback

is credited as the technique

that helped ChatGPT breakthrough.

It is a technique to make the responses

that are nicely formatted, like these Reddit answers,

more in tune with what a human would like to read.

This is done by collecting pairwise preferences

from actual humans out in the world to start.

And now, AIs are also labeling this data

and we'll get into those trade-offs.

And you have this kind of contrastive loss function

between a good answer and a bad answer.

And the model learns to pick up these trends.

There's different implementation ways.

You have things called reward models.

You could have direct alignment algorithms.

There's a lot of really specific things you can do.

But all of this is about fine-tuning to human preferences.

And the final stage is much newer

and will link to what is done in R1.

And these reasoning models

is I think OpenAI's name for this.

They had this new API in the fall,

which they called the reinforcement fine-tuning API.

This is the idea that you use the techniques

of reinforcement learning, which is a whole framework of AI.

There's a deep literature here.

To summarize, it's often known as trial and error learning

or the subfield of AI where you're trying

to make sequential decisions

in a certain potentially noisy environment.

There's a lot of ways we could go down that.

But fine-tuning language models

where they can generate an answer.

And then, you check to see

if the answer matches the true solution.

For math or code,

you have an exactly correct answer for math.

You can have unit tests for code.

And what we're doing

is we are checking the language model's work

and we're giving it multiple opportunities

on the same questions to see if it is right.

And if you keep doing this, the models can learn

to improve in verifiable domains to a great extent.

It works really well.

It's a newer technique in the academic literature.

It's been used at Frontier Labs in the US

that don't share every detail for multiple years.

So, this is the idea of using reinforcement learning

with language models, and it has been taking off,

especially in this DeepSeek moment.

- And we should say that there's a lot

of exciting stuff going on the, again, across the stack.

But the post-training probably this year,

there's going to be a lot of interesting developments

in the post-training.

We'll talk about it.

I almost forgot to talk about the difference

between DeepSeek-V3 and R1 on the user experience side.

So, forget the technical stuff, forget all of that.

Just people that don't know anything about AI,

they show up like what's the actual experience,

what's the use case for each one

when they actually type and talk to it?

- Yeah. - What is each good at

and that kind of thing.

- So, let's start with DeepSeek-V3.

Again, it's more people would have tried something like it.

You ask it a question,

it'll start generating tokens very fast,

and those tokens will look like a very human legible answer.

It'll be some sort of markdown list.

It might have formatting

to help you draw to the core details in the answer.

And it'll generate tens to hundreds of tokens.

Say token is normally a word for common words

or a sub-word part in a longer word.

And it'll look like a very high quality Reddit

or Stack Overflow answer.

These models are really getting good

at doing these across a wide variety of domains, I think.

Even things that if you're an expert,

things that are close to the fringe of knowledge,

they will still be fairly good at, I think.

Cutting edge AI topics that I do research on,

these models are capable for study aide,

and they're regularly updated.

Where this changes is with the DeepSeek-R1,

what is called these reasoning models,

is when you see tokens coming from these models to start,

it will be a large chain of thought process.

We'll get back to chain of thought in a second,

which looks like a lot of tokens,

where the model is explaining the problem.

The model will often break down the problem

and be like, okay, they asked me for this,

let's break down the problem.

I'm going to need to do this.

And you'll see all of this generating from the model.

It'll come very fast in most user experiences.

These APIs are very fast.

So, you'll see a lot of tokens,

a lot of words show up really fast.

It'll keep flowing on the screen

and this is all the reasoning process.

And then, eventually, the model will change its tone in R1

and it'll write the answer,

where it summarizes its reasoning process

and writes a similar answer to the first types of model.

But in DeepSeek's case, which is part

of why this was so popular even outside the AI community,

is that you can see how the language model

is breaking down problems.

And then, you get this answer.

On a technical side,

they train the model to do this specifically,

where they have a section which is reasoning,

and then it generates a special token,

which is probably hidden from the user most of the time,

which says, okay, I'm starting the answer.

So, the model is trained

to do this two-stage process on its own.

If you use a similar model in say, OpenAI,

OpenAI's user interface

is trying to summarize this process for you nicely

by showing the sections that the model is doing,

and it'll click through,

it'll say breaking down the problem, making X calculation,

cleaning the result,

and then the answer will come for something like OpenAI.

- Maybe it's useful here to go through

like an example of it, DeepSeek-R1 reasoning.

- Yeah.

So, if you're looking at the screen here,

what you'll see is a screenshot of the DeepSeek chat app.

And at the top is Thought for 157 seconds

with the dropdown arrow.

Underneath that, if we were in an app that we were running,

the dropdown arrow would have the reasoning.

- So, in this case, the question,

the specific question which,

I'm philosophically/pothead-inclined,

so this is asking DeepSeek-R1

for one truly novel insight about humans.

And it reveals the reasoning.

And basically, the truly novel aspect

is what's pushing the reasoning to constantly,

the model asking itself, is this truly novel?

So, it's actually challenging itself to be more novel,

more counterintuitive, less cringe, I suppose.

So, some of the reasoning says, this is just snapshots.

Alternatively, humans have a unique meta-emotion

where they feel emotions about their own emotions,

e.g, feeling guilty about being angry.

This recursive emotional layering creates complex

motivational drives that don't exist in other animals.

The inside is that human emotions are nested.

So, it's like,

it's reasoning through how humans feel emotions,

it's reasoning about meta-emotions.

- It's gonna have pages

and pages of this. - Yeah.

- It's almost too much to actually read,

but it's nice to skim as it's coming.

- It's a stream of con...

It's a James Joyce-like stream of consciousness.

And then, it goes, wait,

the user wants something that's not seen anywhere else.

Let me dig deeper.

And consider the human ability

to hold contradictory beliefs simultaneously.

Cognitive dissonance is known,

but perhaps the function

is to allow flexible adaptation, so on and so forth.

That really captures the public imagination,

that holy shit, this isn't...

I mean, intelligence/almost like an inkling of sentience,

because you're thinking through,

you're self-reflecting, you're deliberating.

And the final result of that after 157 seconds

is humans instinctively convert selfish desires

into cooperative systems

by collectively pretending abstract rules,

money, laws, rights, are real.

These shared hallucinations act as, quote, games,

where competition is secretly redirected

to benefit the group, turning conflict into society's fuel.

Pretty profound.

I mean, you know?

Comment- - This is a potential

digression, but a lot of people have found

that these reasoning models

can sometimes produce much more eloquent text.

That is at least interesting example, I think,

depending on how open-minded you are,

you find language models interesting or not,

and there's a spectrum there.

- Well, it's some of the...

We'll talk about different benchmarks, and so on.

But some is just a vibe.

Like that in itself is a, let's say, quote, fire tweet.

- Yeah. (laughs) - If I'm trying

to produce something, where people are like, oh shit,

okay, so that's chain of thought.

We'll probably return to it more.

How were they able to achieve such low cost

on the training and the inference?

Maybe you could talk the training first.

- Yeah, so there's two main techniques

that they implemented

that are probably the majority of their efficiency.

And then, there's a lot of implementation details

that maybe we'll gloss over

or get into later that contribute to it.

But those two main things are,

one, is they went to a mixture of experts model,

which we'll define in a second.

And then, the other thing

is that they invented this new technique

called MLA latent attention.

Both of these are big deals.

Mixture of experts is something

that's been in the literature for a handful of years.

And OpenAI with GPT-4 was the first one

to productize a mixture of experts model.

And what this means

is when you look at the common models around

that most people have been able

to interact with that are open.

Think Llama, Llama is a dense model.

i.e, every single parameter

or neuron is activated as you're going through the model

for every single token you generate.

Now, with a mixture of experts model, you don't do that.

How does the human actually work is like,

oh, well, my visual cortex

is active when I'm thinking about vision tasks

and other things.

My amygdala is when I'm scared.

These different aspects of your brain

are focused on different things.

A mixture of experts models

attempts to approximate this to some extent.

So, nowhere close to what a brain architecture is,

but different portions of the model activate.

You'll have a set number of experts in the model

and a set number that are activated each time.

And this dramatically reduces both your training

and inference cost.

Because now, if you think about the parameter count

as the total embedding space for all of this knowledge

that you're compressing down during training,

one, you're embedding this data in,

instead of having to activate every single parameter,

every single time you're training or running inference.

Now, you can just activate on a subset.

And the model will learn

which expert to route to for different tasks.

And so, this is a humongous innovation in terms of, hey,

I can continue to grow

the total embedding space of parameters.

And so, DeepSeek's model

is 600 something billion parameters.

Relative to Llama 405b, it's 405 billion parameters.

Llama relative to Llama 70b, it's 70 billion parameters.

So, this model technically

has more embedding space for information,

to compress all of the world's knowledge

that's on the internet down.

But at the same time,

it is only activating around 37 billion of the parameters.

So, only 37 billion of these parameters

actually need to be computed

every single time you're training data

or inferencing data out of it.

And so, versus again a Llama model,

70 billion parameters must be activated

or 405 billion parameters must be activated.

So, you've dramatically reduced your compute cost

when you're doing training and inference

with this mixture of experts architecture.

- So, we break down where it actually applies

and go into the transformer.

Is that useful?

- Let's go, let's go

into the transformer. - Okay.

So, the transformer (Lex laughing)

is a thing that is talked about a lot

and we will not cover every detail.

Essentially, the transformer is built

on repeated blocks of this attention mechanism,

and then a traditional dense,

fully connected multi-layer perception,

whatever word you want to use

for your normal neural network.

And you alternate these blocks.

There's other details.

And where mixture of experts

is applied is that this dense model.

The dense model holds most of the weights

if you count them in a transformer model.

So, you can get really big gains

from those mixture of experts on parameter efficiency

at training and inference,

because you get this efficiency

by not activating all of these parameters.

- [Lex] We should also say that a transformer

is a giant neural network.

- Yeah. - And then,

there's for 15 years now,

there's what's called the deep learning revolution.

Networks gotten larger and larger.

And a certain point, the scaling laws appeared

where people realized...

- This is a scaling law shirt, by the way.

(group laughing)

- Representing.

Scaling laws where it became more

and more formalized that bigger is better

across multiple dimensions of what bigger means.

But these are all neural networks we're talking about.

And we're talking about different architectures

of how to construct these neural networks

such that the training

and the inference on them is super efficient.

- Yeah, every different type of model

has a different scaling law for it,

which is effectively for how much compute you put in,

the architecture will get

to different levels of performance at test tasks.

A mixture of experts is one of the ones at training time.

Even if you don't consider the inference benefits,

which are also big.

At training time, your efficiency with your GPUs

is dramatically improved

by using this architecture if it is well-implemented.

So, you can get effectively the same performance model

and evaluation scores with numbers like 30% less compute.

I think there's gonna be a wide variation,

depending on your implementation details and stuff.

But it is just important to realize that this type

# Chapter 3

And we're talking about different architectures

of how to construct these neural networks

such that the training

and the inference on them is super efficient.

- Yeah, every different type of model

has a different scaling law for it,

which is effectively for how much compute you put in,

the architecture will get

to different levels of performance at test tasks.

A mixture of experts is one of the ones at training time.

Even if you don't consider the inference benefits,

which are also big.

At training time, your efficiency with your GPUs

is dramatically improved

by using this architecture if it is well-implemented.

So, you can get effectively the same performance model

and evaluation scores with numbers like 30% less compute.

I think there's gonna be a wide variation,

depending on your implementation details and stuff.

But it is just important to realize that this type

of technical innovation is something that gives huge gains.

And I expect most companies that are serving their models

to move to this mixture of experts implementation.

Historically, the reason why not everyone might do it

is because it's a implementation complexity,

especially when doing these big models.

So, this is one of the things that DeepSeek gets credit for

is they do this extremely well.

They do a mixture of experts extremely well.

This architecture for what is called DeepSeekMoE.

MoE is the shortened version

of mixture of experts, is multiple papers old.

This part of their training infrastructure

is not new to these models alone,

and same goes for what Dylan mentioned,

with multi-head latent attention.

This is all about reducing memory usage during inference.

And same things during training,

by using some fancy low rank approximation math.

If you get into the details with this latent attention,

it's one of those things I look at,

and it's like, okay,

they're doing really complex implementations,

'cause there's other parts of language models

such as embeddings

that are used to extend the context length.

The common one that DeepSeek used

is rotary positional impendings, which is called RoPE.

And if you want to use RoPE with a normal MoE,

it's a sequential thing.

You take two of the attention matrices

and you rotate them by a complex value rotation,

which is a matrix multiplication.

With DeepSeek's MLA, with this new attention architecture,

they need to do some clever things,

because they're not set up the same

and it just makes the implementation complexity much higher.

So, they're managing all of these things,

and these are probably the sort of things that OpenAI,

these closed labs are doing.

We don't know if they're doing the exact same techniques,

but they actually shared them with the world,

which is really nice to be like,

this is the cutting edge

of efficient language model training.

- And some of this requires low level engineering,

just is a giant mess in trickery.

So, as I understand, that went below CUDA,

so they go super low programming of GPUs.

- Effectively, Nvidia builds this library called NCCL.

In which, when you're training a model,

you have all these communications

between every single layer of the model

and you may have over 100 layers.

- What does the NCCL stand for? It's N-C-C-L?

- Nvidia Communications Collectives Library.

- [Lex] Nice. (Nathan laughing)

Damn. - And so,

(group laughing)

when you're training a model,

you're gonna have all reduces and all gathers.

Between each layer, between the multi-layer perception

or feedforward network

and the attention mechanism you'll have,

you'll have basically the model synchronized.

Or you'll have all reduce and all gather.

And this is a communication

between all the GPUs in the network,

whether it's in training or inference.

So, Nvidia has a standard library.

This is one of the reasons why it's really difficult

to use anyone else's hardware for training

is because no one's really built

a standard communications library.

And Nvidia's done this at a higher level.

At DeepSeek, because they have certain limitations

around the GPUs that they have access to,

the interconnects are limited to some extent

by the restrictions of the GPUs

that were shipped into China legally,

not the ones that are smuggled, but legally shipped in,

that they used to train this model.

They had to figure out how to get efficiencies.

And one of those things is that instead

of just calling the Nvidia library NCCL,

they instead created their,

they scheduled their own communications,

which some of the labs do.

Meta talked about in Llama 3

how they made their own custom version of NCCL.

They didn't talk about the implementation details.

This is some of what they did.

Probably not as well as, maybe not as well as DeepSeek

because DeepSeek necessity is the mother of innovation

and they had to do this.

Whereas in the ca...

OpenAI has people

that do this sort of stuff, Anthropic, et cetera.

But DeepSeek certainly did it publicly

and they may have done it even better

because they were gimp on a certain aspect

of the chips that they have access to.

And so, they scheduled communications

by scheduling specific SMs.

SMs you could think of as like the core on a GPU.

So, there's hundreds of cores

or there's a bit over 100 cores, SMs, on a GPU,

and they were specifically scheduling,

hey, which ones are running the model?

Which ones are doing all reduce?

Which one are doing all gather?

And they would flip back and forth between them.

And this requires extremely low level programming.

- This is what NCCL does automatically

or other Nvidia libraries

handle this automatically usually.

- Yeah, exactly.

And so, technically, they're using PTX,

which is like, you could think of it

as like an assembly type language.

It's not exactly that or instruction set.

Coding directly to assembly or instruction set.

It's not exactly that,

but that's still part of technically CUDA.

But it's like, do I wanna write in Python,

PyTorch equivalent, and call Nvidia libraries?

Do I want to go down to the C level.

Or in code, even lower level?

Or do I wanna go all the way down

to the assembly or ISA level?

And there are cases

where you go all the way down there at the very big labs,

but most companies just do not do that

because it's a waste of time

and the efficiency gains you get are not worth it.

But DeepSeek's implementation is so complex.

Especially with their mixture of experts.

People have done mixture of experts,

but they're generally 8, 16 experts.

And they activate too.

So, one of the words

that we like to use is sparsity factor or usage.

So, you might have four, one fourth of your model activate.

And that's what misdraws mixed role model.

They're model that really catapulted them to like,

oh my god, they're really, really good.

OpenAI has also had models that are MoE,

and so have all the other labs that are major closed.

But what DeepSeek did that maybe only the leading labs

have only just started recently doing

is have such a high sparsity factor.

It's not one fourth of the model.

Two out of eight experts activating

every time you go through the model.

It's 8 out of 256.

- And there's different implementations from mixture

of experts where you can have some of these experts

that are always activated,

which this just looks like a small neural network.

And then, all the tokens go through that.

And then, they also go through some

that are selected by this routing mechanism.

And one of the innovations in DeepSeek's architecture

is that they change the routing mechanism

in mixture of expert models.

There's something called an auxiliary loss,

which effectively means during training,

you want to make sure that all of these experts

are used across the tasks that the model sees.

Why there can be failures in mixture of experts

is that when you're doing this training,

the one objective is token prediction accuracy.

And if you just let turning go

with a mixture of expert model on your own,

it can be that the model learns

to only use a subset of the experts.

And in the MoE literature,

there's something called the auxiliary loss,

which helps balance them.

But if you think about the loss functions of deep learning,

this even connects to the bitter lesson,

is that you want to have the minimum inductive bias

in your model to let the model learn maximally.

And this auxiliary loss,

this balancing across experts could be seen as intention

with the prediction accuracy of the tokens.

So, we don't know the exact extent

that the DeepSeek MoE change,

which is instead of doing an auxiliary loss,

they have an extra parameter in their routing,

which after the batches,

they update this parameter to make sure

that the next batches all have a similar use of experts.

And this type of change can be big,

it can be small, but they add up over time.

And this is the sort of thing

that just points to them innovating.

And I'm sure all the labs that are training big MoEs

are looking at this sort of things,

which is getting away from the auxiliary loss.

Some of them might already use it,

but you keep accumulating gains.

And we'll talk about the philosophy of training

and how you organize these organizations.

And a lot of it is just compounding small improvements

over time in your data, in your architecture,

in your post-training,

and how they integrate with each other.

And DeepSeek does the same thing

and some of 'em are shared or a lot,

we have to take them on face value

that they share their most important details.

The architecture and the weights are out there,

so we're seeing what they're doing, and it adds up.

- Going back to the efficiency and complexity point.

It's 32 versus 4 for mixed draw

and other MoE models that have been publicly released.

So, this ratio is extremely high.

And what Nathan was getting at there was,

when you have such a different level of sparsity,

you can't just have every GPU have the entire model.

The model's too big, there's too much complexity there.

So, you have to split up the model

with different types of parallelism.

And so, you might have different experts

on different GPU nodes,

but now what happens when this set of data that you get,

hey, all of it looks like this one way

and all of it should route to one part of my model.

So, when all of it routes to one part of the model,

then you can have this overloading

of a certain set of the GPU resources

or a certain set of the GPUs,

and then the rest of the training network sits idle,

because all of the tokens are just routing to that.

So, this is the biggest complexity,

one of the big complexities

with running a very sparse mixture of experts model,

i.e, this 32 ratio versus this 4 ratio,

is that you end up with so many

of the experts just sitting there idle.

So, how do I load balance between them?

How do I schedule the communications between them?

This is a lot of the extremely low level detailed work

that they figured out in the public first

and potentially second or third in the world,

and maybe even first in some cases.

- What lesson do you, in the direction

of the bitter lesson, do you take from all of this?

Is this going to be the direction

where a lot of the gain is going to be,

which is this kind of low level optimization?

Or is this a short-term thing

where the biggest gains will be more

on the algorithmic high level side of post-training?

Is this like a short-term leap

because they've figured out like a hack,

because constraints, necessity is the mother of invention,

or is there still a lot of gains?

- I think we should summarize

what the bitter lesson actually is about,

is that the bitter lesson, - Okay.

- essentially, if you paraphrase it,

is that the types of training

that will win out in deep learning

as we go are those methods that are which are scalable

in learning and search is what it calls out.

And the scale word gets a lot of attention in this.

The interpretation that I use is effectively

to avoid adding the human priors to your learning process.

And if you read the original essay,

this is what it talks about

is how researchers will try to come up

with what clever solutions to their specific problem

that might get them small gains in the short-term

while simply enabling these deep learning systems

to work efficiently.

And for these bigger problems in the long-term

might be more likely to scale and continue to drive success.

And therefore, we were talking

about relatively small implementation changes

to the mixture of experts model.

And therefore, it's like, okay,

we will need a few more years to know if one

of these were actually really crucial to the bitter lesson.

But the bitter lesson is really

this long-term arc of how simplicity can often win.

And there's a lot of sayings in the industry,

like the models just wanna learn.

You have to give them the simple loss landscape

where you put compute through the model,

and they will learn and getting barriers out of the way.

- That's where the power, something like NCCL comes in,

where standardized code

that could be used by a lot of people

to create sort of simple innovations that can scale.

Which is why the hacks, I imagine the code base

for DeepSeek is probably a giant mess.

- I'm sure they have,

DeepSeek definitely has code bases that are extremely messy,

where they're testing these new ideas,

multi-head latent attention,

probably could start in something like a Jupyter Notebook

or somebody try something on a few GPUs.

And that is really messy.

But the stuff that trains the DeepSeek-V3

and DeepSeek-R1, those libraries,

if you were to present them to us,

I would guess are extremely high quality code.

- It's a high quality readable code. Yeah.

- I think there is one aspect to note though.

Is that there is the general ability

for that to transfer across different types of runs.

You may make really, really high quality code

for one specific model architecture

at one size. - Yeah.

- And then, that is not transferable to,

hey, when I make this architecture tweak,

everything's broken again.

That's something that could be

with their specific low level coding of scheduling SMs,

is specific to this model architecture and size.

And whereas like Nvidia's collectives library

is more like, hey, it'll work for anything.

You wanna do an all reduce, great,

I don't care what your model architecture is, it'll work.

And you're giving up a lot of performance

when you do that in many cases.

But it's worthwhile for them

to do the specific optimization for the specific run,

given the constraints that they have regarding compute.

- I wonder how stressful it is to like,

these frontier models, like initiate training,

like to have the code-

- [Nathan] Push the button.

- to push the button (Nathan laughing)

that you're now spending a large amount of money

and time to train this.

There must be a lot of innovation on the debugging stage

of making sure there's no issues that you're monitoring

and visualizing every aspect

of the training, all that kind of stuff.

- When people are training,

they have all these various dashboards,

but the most simple one - Yeah.

- is your loss. - Right.

- And it continues to go down.

But in reality,

especially with more complicated stuff like MoE,

the biggest problem with it,

or FP8 training, which is another innovation,

going to a lower precision number format,

i.e, less accurate, is that you end up with loss spikes.

And no one knows why the loss spike happened.

And for a lot- - Some of them you do.

- Some of them you do. - Some of them are bad data.

I give AI2's example

of what blew up our earlier models

is a subreddit called Microwave Gang.

We love to shoutout this out. (Lex laughing)

It's a real thing.

You can pull up Microwave Gang.

Essentially, it's a subreddit

where everybody makes posts that are just the letter M.

So, it's like, mm.

So, there's extremely long sequences

of the letter M, and then the comments are like, beep beep.

'Cause it's in the microwave end.

- Yeah. - If you pass this

into a model that's trained to be a normal producing text,

it's extremely high loss.

'Cause normally, - Yeah.

- you see an M. (Lex laughing)

You don't predict Ms for a long time.

So, this is something that cause a loss spikes for us.

But when you have much like,

this is old, this is not recent.

And when you have more mature data systems,

that's not the thing that causes the loss spike.

And what Dylan is saying is true,

but it's levels to this sort of idea.

- With regards to the stress,

(Nathan and Lex laughing)

these people are like, you'll go out to dinner

with a friend that works at one of these labs.

And they'll just be like (Nathan laughing)

looking at their phone every 10 minutes,

and they're not like...

It's one thing if they're texting,

but they're just like, - Yeah.

- is the loss- - It's literal.

The tokens per second loss, not blown up.

They're just watching this. (chuckles)

- And the heart rate goes up if there's a spike.

# Chapter 4

So, this is something that cause a loss spikes for us.

But when you have much like,

this is old, this is not recent.

And when you have more mature data systems,

that's not the thing that causes the loss spike.

And what Dylan is saying is true,

but it's levels to this sort of idea.

- With regards to the stress,

(Nathan and Lex laughing)

these people are like, you'll go out to dinner

with a friend that works at one of these labs.

And they'll just be like (Nathan laughing)

looking at their phone every 10 minutes,

and they're not like...

It's one thing if they're texting,

but they're just like, - Yeah.

- is the loss- - It's literal.

The tokens per second loss, not blown up.

They're just watching this. (chuckles)

- And the heart rate goes up if there's a spike.

- And some level of spikes is normal.

It'll recover and be back.

Sometimes a lot of the old strategy was like,

you just stop the run, restart from an old version,

and then change the data mix, and then it keeps going.

- There are even different types of spikes.

So, Dirk Groeneveld has a theory of AI too

that's like fast spikes and slow spikes,

where there are sometimes where you're looking at the loss

and there are other parameters,

you can see it start to creep up, and then blow up.

And that's really hard to recover from.

So, you have to go back much further.

So, you have the stressful period, where it's like flat

or it might start going up and you're like, what do I do?

Whereas there are also lost spikes that are, it looks good.

And then, there's one spiky data point.

And what you could do is you just skip those.

You see that there's a spike.

You're like, okay, I can ignore this data,

don't update the model,

and do the next one, and it'll recover quickly.

But these like untrickier implementation,

so as you get more complex in your architecture

and you scale up to more GPUs,

you have more potential for your loss blowing up.

So, it's like there's

a distribution. - And then,

the whole idea of grokking also comes in.

It's like, just because it's slowed down from improving

and loss doesn't mean it's not learning,

because all of a sudden, it could be like this

and it could just spike down in loss again

because it learned, truly learned something.

And it took some time for it to learn that.

It's not like a gradual process.

And that's what humans are like,

that's what models are like.

It's really a stressful task as you mentioned.

- And the whole time, the dollar count is going up.

- Every company has failed runs.

You need failed run

to push the envelope on your infrastructure.

So, a lot of news cycles

are made of X company had Y failed run.

Every company that's trying

to push the frontier of AI has these.

So, yes, it's noteworthy because it's a lot of money

and it can be week to month setback,

but it is part of the process.

- But how do you get, if you're DeepSeek,

how do you get to a place where holy shit,

there's a successful combination of hyperparameters?

- A lot of small failed runs.

- And so, rapid iteration (Nathan chuckles)

through failed runs,

until- - Yeah, and successful ones.

You just- - And then, you build up

some intuition like this, this mixture of expert works,

and then this implementation of MLA works.

- Key hyperparameters like learning rate

and regularization and things like this.

And you find the regime that works for your code base.

Talking to people at Frontier Labs, there's a story

that you can tell where training language models

is kind of a path that you need to follow.

So, you need to unlock the ability

to train a certain type of model or a certain scale.

And then, your code base and your internal knowhow

of which hyperparameters work for it is known.

And you look at the DeepSeek papers and models,

they've scaled up, they've added complexity,

and it's just continuing

to build the capabilities that they have.

- There's the concept of a YOLO run.

(Nathan laughing)

So, YOLO, you only live once. - Yep.

- And what it is, is like,

there's all this experimentation you do at the small-scale.

Research ablations, you have your Jupyter Notebook with,

you're experimenting with MLA on three GPUs or whatever,

and you're doing all these different things like, hey,

do I do 4 expert, 4 active experts, 128 experts,

do I arrange the experts this way?

All these different model architecture things

you're testing at a very small-scale.

Couple researchers, few GPUs, tens of GPUs,

hundreds of GPUs, whatever it is.

And then, all of a sudden,

you're like, okay guys, no more fucking around.

No more screwing around.

Everyone, take all the resources we have,

let's pick what we think will work, and just go for it.

YOLO. - Yeah.

- And this is where that sort of stress comes in is like,

well, I know it works here,

but some things that work here don't work here,

and some things that work here don't work down here

- Yeah. - in this terms of scale.

So, it's really truly a YOLO run,

and there's this discussion of certain researchers

just have this methodical nature.

They can find the whole search space

and figure out all the ablations of different research,

and really see what is best.

And there's certain researchers who just like,

have that innate gut instinct of like,

this is the YOLO run.

I'm looking at the data, (Dylan drowns out Nathan)

I think this is it.

- This is why you wanna work in post-training,

because the GPU cost for training is lower.

So, you can make a higher percentage

of your training runs YOLO runs

- Yeah. - For now.

- Yeah, for now, for now. - For now, for now. (laughs)

- So, some of this is fundamentally luck still.

- Luck is skill in many cases.

- Yeah, it looks lucky right when you're-

- But the hill to climb, if you're on one of these labs

and you have an evaluation and you're not crushing,

there's a repeated playbook of how you improve things.

There are localized improvements,

which might be data improvements.

And these add up

into the whole model just being much better.

And when you zoom in really close,

it can be really obvious

that this model's just really bad at this thing

and we can fix it.

And you just add these up.

So, some of it feels like luck,

but on the ground,

especially with these new reasoning models we're talking to,

is just so many ways that we can poke around.

And normally, it's that some of them give big improvements.

- The search space is near infinite.

And yet, the amount of compute

and time you have is very low.

And you have to hit release schedules,

you have to not get blown past by everyone.

Otherwise, what happened with DeepSeek

crushing Meta and Misral and Cohere,

and all these guys, they moved too slow.

They maybe were too methodical.

I don't know, they didn't hit the YOLO run,

whatever the reason was, maybe they weren't as skill.

You can call it luck if you want,

but at the end of the day, it's skill.

- So, 2025 is the year of the YOLO run.

It seems like all the labs are going in.

- I think it's even more impressive what OpenAI did in 2022.

At the time, no one believed in mixture

of experts models at Google who had all the researchers.

OpenAI had such little compute

and they devoted all of their compute for many months,

all of it, 100% for many months, to GPT-4,

with a brand new architecture with no belief that, hey,

let me spend a couple $100 million,

which is all of the money I have, on this model.

That is truly YOLO,

right? - Yeah, yeah.

- Now, people are like,

all these training run failures that are in the media,

it's like, okay, great,

but actually, a huge chunk of my GPs are doing inference.

I still have a bunch doing research constantly.

And yes, my biggest cluster is training,

but on this YOLO run,

but that YOLO run is much less risky

than what OpenAI did in 2022,

or maybe what DeepSeek did now,

or like, hey, we're just gonna throw everything at it.

- The big winners throughput human history

are the ones who are willing to do YOLO at some point.

Okay.

What do we understand

about the hardware it's been trained on?

DeepSeek.

- DeepSeek is very interesting.

A second to take us

to zoom out out of who they are, first of all.

High-Flyer is a hedge fund

that has historically done quantitative trading

in China as well as elsewhere.

And they have always had a significant number of GPUs.

In the past, a lot of these high frequency trading,

algorithmic, quant traders, used FPGAs,

but it shifted to GPUs, definitely.

And there's both.

But GPUs especially, and High-Flyer,

which is the hedge fund that owns DeepSeek.

And everyone who works for DeepSeek

is part of High-Flyer to some extent.

Same parent company, same owner, same CEO.

They had all these resources and infrastructure for trading,

and then they devoted a humongous portion of them

to training models, both language models and otherwise.

Because these techniques were heavily AI-influenced.

More recently, people have realized,

hey, trading with, even when you go back to Renaissance

and all these quantitative firms,

natural language processing

is the key to trading really fast,

understanding a press release and making the right trade.

And so, DeepSeek has always been really good at this.

And even as far back as 2021,

they have press releases and papers saying like, hey,

we're the first company in China

with an A100 cluster this large.

It was 10,000 A100 GPUs. This is in 2021.

Now, this wasn't all for training large language models.

This is mostly for training models

for their quantitative aspects,

or quantitative trading, as well as a lot of that

was natural language processing, to be clear.

And so, this is the history.

So, verifiable fact is that in 2021,

they built the largest cluster, at least they claim

it was the largest cluster in China, 10,000 GPUs.

- Before expert controls started.

- Yeah. - It's like,

they've had a huge cluster

before any conversation of export controls.

So, then you step it forward to like,

what have they done over the last four years since then?

Obviously, they've continued

to operate the hedge fund, probably make tons of money.

And the other thing

is that they've leaned more and more and more into AI.

the CEO, Liang Wenfeng, Liang-

- You're not putting me on spot on this.

We discussed this. (laughs) - Liang Feng, the CEO,

he owns maybe- - We're all fam. (chuckles)

- Liang Feng, he owns maybe

a little bit more than half the company, allegedly,

an extremely like Elon-Jensen kind of figure,

where he is just involved in everything.

And so, over that time period,

he's gotten really in depth into AI.

He actually has a bit of a like a,

if you see some of his statements,

a bit of an EAC vibe almost.

- Total AGI vibes.

And like, we need to do this,

we need to make a new ecosystem of OpenAI.

We need China to lead on this sort of ecosystem,

because historically,

the Western countries have led on software ecosystems,

and straight up acknowledges,

in order to do this, we need to do something different.

DeepSeek is his way of doing this.

Some of the translated interviews with him

are fantastic. - So, he has done interviews?

- Yeah. - Do you think

he would do a Western interview or no?

Or is there controls

on the channel? - There hasn't been one yet,

but I would try it. - Okay. All right.

(Nathan laughing) Well, I just got

a Chinese translator, so it was great.

This is all push.

So, fascinating figure, engineer pushing full on into AI,

leveraging the success from the high frequency trading.

- Very direct quotes, like we will not switch

to closed source when asked about this stuff.

Very long-term motivated

in how the ecosystem of AI should work.

And I think from a Chinese perspective,

he wants a Chinese company to build this vision.

- And so, this is like the,

quote, unquote, "visionary behind the company".

This hedge fund still exists, this quantitative firm.

And so, DeepSeek is the sort of,

solely, he got turned to this full view

of like AI, everything about this.

But at some point,

it slowly maneuvered and he made DeepSeek.

And DeepSeek has done multiple models since then.

They've acquired more and more GPUs.

They share infrastructure with the fund.

And so, there is no exact number

of public GPU resources that they have,

but besides this 10,000 GPUs that they bought in 2021,

and they were fantastically profitable.

And then, this paper claims they did only 2,000 H800 GPUs,

which are a restricted GPU

that was previously allowed in China,

but no longer allowed, and there's a new version.

But it's basically Nvidia's H100 for China.

And there's some restrictions on it,

specifically around the communications sort of speed,

the interconnect speed,

which is why they had to do this crazy SM scheduling stuff.

So, going back to that.

It's like this is obviously

not true in terms of their total GPU count.

- Obvious available GPUs.

But for this training run,

you think 2,000 is the correct number or no?

- So, this is where it takes a significant amount

of zoning in.

What do you call your training run?

You count all of the research and ablations that you ran,

picking all this stuff,

because, yes, you can do a YOLO run,

but at some level,

you have to do the test at the small-scale,

and then you have to do some test at medium-scale

before you go to a large-scale.

- Accepted practices that for any given model

that is a notable advancement,

you're gonna do 2 to 4x compute

of the full training run in experiments alone.

- So, a lot of this compute that's being scaled up

is probably used in large part

at this time for research. - Yeah.

And research begets the new ideas

that lets you get huge efficiency-

- Research gets you o1.

Research gets you breakthrough, so you need to bet on it.

- So, some of the pricing strategy

that we'll discuss has the research baked into the price.

- So, the numbers that DeepSeek specifically said publicly

are just the 10,000 GPUs in 2021,

and then 2,000 GPUs for only the pre-training for V3.

They did not discuss cost on R1.

They did not discuss cost on all the other RL,

for the instruct model that they made.

They only discussed the pre-training for the base model,

and they did not discuss anything on research and ablations.

And they do not talk about any of the resources

that are shared in terms of, hey,

the fund is using all these GPUs.

And we know that they're very profitable

in that 10,000 GPUs in 2021.

So, some of the research that we've found

is that we actually believe they have closer to 50,000 GPUs.

- We, as SemiAnalysis,

so we should say - Yeah.

- that you're one of the world experts in figuring out

what everybody's doing in terms of the semiconductor,

in terms of cluster buildouts,

in terms of who's doing what in terms of training runs.

So, yeah. So, that's the we.

Okay, go ahead. - Yeah, sorry, sorry.

We believe they actually have something closer

to 50,000 GPUs. - Yeah.

- [Dylan] Now, this is split across many tasks.

Again, the fund, research and ablations.

- For ballpark, how much would OpenAI or Anthropic had?

I think the clearest example we have,

because Meta is also open,

they talk about order of 60k

to a 100k H100 equivalent GPUs in their training clusters.

- Right. So, like Llama 3, they trained on 16,000 H100s.

But the company of Meta last year

publicly disclosed they bought

like 400 something thousand GPUs.

- Yeah. (chuckles) - So, of course,

tiny percentage on the training.

Again, most of it is like

serving me the best Instagram reels, or whatever.

- We could get into a cost of like, what is the cost

of ownership for a 2,000-GPU cluster, 10,000?

There's just different sizes of companies

that can afford these things,

and DeepSeek is reasonably big.

Their compute allocation compared

is one of the top few in the world.

It's not OpenAI, Anthropic, et cetera,

but they have a lot of compute.

- Can you in general, actually just zoom out

and also talk about the Hopper architecture,

the Nvidia Hopper GPU architecture,

and the difference between H100 and H800,

like you mentioned the interconnects.

- Yeah, so Ampere was the A100, and then H100, Hopper.

People use them synonymously in the US

because really, there's just H100 and now there's H200.

But same thing mostly.

In China, they've had two,

there've been different salvos of export restrictions.

So, initially, the US government

limited on a two-factor scale,

which is chip interconnect versus FLOPS.

So, any chip that had interconnects above a certain level

and FLOPS above a certain floating point operations,

above a certain level, was restricted.

Later, the government realized

that this was a flaw in the restriction,

and they cut it down to just floating point operations.

And so- - H800 had high FLOPS,

low communication. - Exactly.

So, the H800 was the same performance as H100 on FLOPS,

but it just had the interconnect bandwidth cut.

DeepSeek knew how to utilize this res...

Hey, even though we're cut back on the interconnect,

we can do all this fancy stuff

# Chapter 5

because really, there's just H100 and now there's H200.

But same thing mostly.

In China, they've had two,

there've been different salvos of export restrictions.

So, initially, the US government

limited on a two-factor scale,

which is chip interconnect versus FLOPS.

So, any chip that had interconnects above a certain level

and FLOPS above a certain floating point operations,

above a certain level, was restricted.

Later, the government realized

that this was a flaw in the restriction,

and they cut it down to just floating point operations.

And so- - H800 had high FLOPS,

low communication. - Exactly.

So, the H800 was the same performance as H100 on FLOPS,

but it just had the interconnect bandwidth cut.

DeepSeek knew how to utilize this res...

Hey, even though we're cut back on the interconnect,

we can do all this fancy stuff

to figure out how to use the GPU fully anyways.

And so, that was back in October, 2022.

But later in 2023, into 2023 implemented in 2024,

the US government banned the H800.

And so, by the way, this H800 cluster,

these 2,000 GPUs was not even purchased in 2024.

It was purchased in late 2023.

- [Lex] Mm-hmm.

- And they're just getting the model out now,

because it takes a lot of research, et cetera.

H800 was banned and now there's a new chip called the H20.

The H20 is cutback on only FLOPS,

but the interconnect bandwidth is the same.

And in fact, in some ways, it's better than the H100

because it has better memory bandwidth and memory capacity.

So, there are, Nvidia's working within the constraints

of what the government sets,

and then builds the best possible GPU for China.

- Can we take this actual tangent

and we'll return back to the hardware?

Is the philosophy,

the motivation, the case for export controls, what is it?

Dario Amodei just published a blog post

about export controls.

The case he makes is that if AI becomes super powerful,

and he says by 2026, will have AGI or super powerful AI,

and that's going to give a significant, whoever builds that

will have a significant military advantage.

And so, because the United States is a democracy,

and as he says, China is authoritarian

or has authoritarian elements,

you want a unipolar world where the super powerful military,

because of the AI, is one that's a democracy.

It's a much more complicated world geopolitically

when you have two superpowers

with super powerful AI and one is authoritarian.

So, that's the case he makes.

And so, we wanna, the United States

wants to use export controls to slow down,

to make sure that China

can't do these gigantic training runs

that will be presumably required to build AGI.

- This is very abstract.

I think this can be the goal

of how some people describe export controls,

is this super powerful AI.

And you touched on the training run idea.

There's not many worlds where China cannot train AI models.

I think export controls are decapping the amount of compute

or the density of compute that China can have.

And if you think about the AI ecosystem right now,

as all of these AI companies,

revenue numbers are up and to the right,

their AI usage is just continuing to grow,

more Deep user going to inference.

A large part of export controls, if they work,

is just that the amount of AI

that can be run in China is going to be much lower.

So, on the training side, DeepSeek-V3 is a great example,

which you have a very focused team

that can still get to the frontier of AI.

This 2,000 GPUs is not that hard to get,

all considering in the world.

They're still gonna have those GPUs,

they're still gonna be able to train models.

But if there's gonna be a huge market for AI,

if you have strong export controls

and you wanna have 100,000 GPUs

just serving the equivalent of ChatGPT clusters,

with good export controls,

it also just makes it so that AI can be used much less.

And I think that is a much easier goal

to achieve than trying to debate on what AGI is.

And if you have these extremely intelligent autonomous AIs

and data centers, those are the things

that could be running in these GPU clusters

in the United States, but not in China.

- To some extent, training a model does effectively nothing.

Like have a model. - Yeah. (chuckles)

- The thing that Dario is speaking to is the implementation

of that model once trained

to then create huge economic growth,

huge increases in military capabilities,

huge increases in productivity of people,

betterment of lives, whatever you want

to direct super powerful AI towards, you can.

But that requires a significant amounts of compute.

And so, the US government has effectively said,

and forever, like training will always be a portion

of the total compute.

We mentioned Meta's 400,000 GPUs, only 16,000 made Llama.

So, the percentage that Meta is dedicating to inference,

now this might be for recommendation systems

that are trying to hack our mind into spending more time

and watching more ads, or if it's for a super powerful AI

that's doing productive things,

doesn't matter about the exact use

that our economic system decides,

it's that that can be delivered in whatever way we want.

Whereas with China, export restrictions, great.

You're never gonna be able to cut everything off.

And that's like, I think that's quite a well-understood

by the US government is that you can't cut everything off.

- [Nathan] And they'll make their own chips.

They're- - And they're trying

to make their own chips.

They'll be worse than ours.

But the whole point is to just keep a gap.

- Yeah. - And therefore,

at some point, as the AI,

in a world where 2, 3% economic growth,

this is really dumb, by the way,

to cut off high tech and not make money off of it.

But in a world where super powerful AI comes about,

and then starts creating significant changes in society,

which is what all the AI leaders

and big tech companies believe, I think.

Super powerful AI is gonna change society massively.

And therefore, this compounding effect

of the difference in compute is really important.

There's some sci-fi out there, where AI is measured

in how much power is delivered to compute.

Or how much is being...

That's a way of thinking about what's the economic output

is just how much power are you directing towards that AI?

Should we talk about reasoning models with this?

As a way that this might be actionable

as something that people can actually see?

So, the reasoning models that are coming out with R1 and o1,

they're designed to use more compute.

There's a lot of buzzy words in the AI community about this,

test-time compute, inference time compute, whatever.

But Dylan has good research on this.

You can get to the specific numbers on the ratio

of when you train a model, you can look at things

about the amount of compute used at training

and amount of compute use inference.

These reasoning models are making inference

way more important to doing complex tasks.

In the fall in December,

their OpenAI announced this o3 model.

There's another thing in AI, when things move fast,

we get both announcements and releases.

Announcements are essentially blog posts

where you pat yourself on the back

and you say you did things.

And releases are on the models out there,

the papers out there, et cetera.

So, OpenAI has announced o3,

and we can check if o3-mini is out

as of recording potentially,

but that doesn't really change the point,

which is that the breakthrough result

was something called ARC-AGI task,

which is the abstract reasoning corpus,

a task for artificial general intelligence.

Francois Chollet is the guy who's been...

It's a multi-year old paper.

It's a brilliant benchmark.

And the number for OpenAI o3 to solve this

was that it used as some number of samples in the API,

the API has thinking effort and number of samples.

They used a thousand samples to solve this task.

And it comes out to be like 5 to $20 per question,

which you're putting in effectively a math puzzle.

And then, it takes orders of dollars to answer one question.

And this is a lot of compute.

If those are gonna take off in the US,

OpenAI needs a ton of GPUs on inference to capture this.

They have this OpenAI ChatGPT Pro subscription,

which is $200 a month.

- [Dylan] Which Sam said they're losing money on.

- Which means that people

are burning a lot of GPUs on inference.

And I've signed up with it, I've played with it.

I don't think I'm a power user, but I use it.

That is the thing that a Chinese company

with mediumly strong export controls,

there will always be loopholes,

might not be able to do it all.

And if that, the main result

for o3 is also a spectacular coding performance.

And if that feeds back

into AI companies being able to experiment better.

- So, presumably the idea is for an AGI,

a much larger fraction of the compute

would be used for this test-time compute for the reasoning,

for the AGI goes into a room

and thinks about how to take over the world

and come back in 2.7 hours.

- This is what- - And that it's gonna take

a lot of compute. - This is what people

like CEO or leaders of OpenAI

and Anthropic talk about is like autonomous AI models,

which is you give them a task

and they work on it in the background.

I think my personal definition of AGI is much simpler.

I think language models are a form of AGI

and all of this super powerful stuff is a next step

that's great if we get these tools.

But a language model has so much value in so many domains.

It is a general intelligence to me.

But this next step of agentic things

where they're independent

and they can do tasks that aren't in the training data

is what the few year outlook

that these AI companies are driving for.

- I think the terminology here

that Dario uses as super powerful AI.

So, I agree with you on the AGI.

I think we already have something

like that's exceptionally impressive

that Alan Turing would for sure say is AGI.

But he's referring more to something once in possession of,

than you would have a significant military

and geopolitical advantage over other nations.

So, it's not just like you can ask it how to cook an omelet.

- And he has a much more positive view.

And as I say, machines of love and grace.

- Yes. - I've read into this.

I don't have enough background in physical sciences

to gauge exactly how confident I am

in if AI can revolutionize biology.

I am safe saying that AI is going to accelerate the progress

of any computational science.

- So, we're doing a depth-first search here on topics,

taking tangent of a tangent.

So, let's continue on that depth-first search.

You said that you're both feeling the AGI,

so what's your timeline? (Nathan chuckles)

Dario's 2026 for the super powerful AI

that's basically agentic to a degree,

where it's a real security threat, that level of AGI.

What's your timeline?

- I don't like to attribute specific abilities

because predicting specific abilities and when is very hard.

I think mostly if you're gonna say

that I'm feeling the AGI

is that I expect continued rapid surprising progress

over the next few years.

So, something like R1 is less surprising

to me from DeepSeek,

because I expect there to be new paradigms

where substantial progress can be made.

I think DeepSeek-R1 is so unsettling,

because we're on this path with ChatGPT,

it's like it's getting better,

it's getting better, it's getting better.

And then, we have a new direction for changing the models.

And we took one step like this and we took a step up.

So, it looks like a really fast slope.

And then, we're gonna just take more steps.

So, this is really unsettling

when you have these big steps.

And I expect that to keep happening.

I've tried OpenAI Operator,

I've tried Claude computer use, they're not there yet.

I understand the idea,

but it's just so hard to predict what is the breakthrough

that'll make something like that work.

And I think it's more likely

that we have breakthroughs that work

and things that we don't know what they're gonna do.

So, everyone wants agents.

Dario has a very eloquent way of describing this.

And I just think that it's like,

there's gonna be more than that.

So, just expect these things to come.

- I'm gonna have to try to pin you down

to a date on the AGI timeline, (chuckles)

like the nuclear weapon moment.

So, moment where on the geopolitical stage.

There's a real, like,

'cause we're talking about export controls,

when do you think just even to throw out a date,

when do you think that would be?

For me, it's probably after 2030,

so I'm not as- - That's what I would say.

- So, define that.

Because to me, it almost has already happened.

You look at elections in India and Pakistan,

people get AI voice calls,

and think they're talking to the politician.

The AI diffusion rules,

which was enacted in the last couple weeks

of the Biden admin and looks like the Trump admin will keep,

and potentially even strengthen,

limit cloud computing and GPU sales

to countries that are not even related to China, it's like.

This is- - Portugal

and all these like normal countries

are on the- - Yeah, and it's like-

- You need approval from the US list.

- Like, yeah, Portugal

and like all these countries that are allies.

- Yup. - Singapore.

They freaking have F-35s and we don't let them buy GPUs.

- Mm-hmm. - This to me

is already to the scale of like-

- Well, that just means that the US military

is really nervous about this new technology.

That doesn't mean the technology is already there.

So, they might be just very cautious

about this thing that they don't quite understand.

But that's a really good point, the robocalls,

swarms of semi-intelligent bots could be a weapon,

could be doing a lot of social engineering.

- There's tons of talk about,

from the 2016 elections like Cambridge Analytica,

and all this stuff, Russian influence.

Every country in the world

is pushing stuff onto the internet

and has narratives they want.

Every technically competent,

whether it's Russia, China, US, Israel, et cetera.

People are pushing viewpoints onto the internet, and mass.

And language models

crash the cost of very intelligent sounding

language. - There's some research

that shows that the distribution

is actually a limiting factor.

So, language models haven't yet made misinformation,

particularly changed the equation there.

The internet is still ongoing.

I think there's a blog, AI Snake Oil,

and some of my friends at Princeton

that write on this stuff.

So, there is research.

It's a default that everyone assumes.

And I would've thought the same thing

is that misinformation

doesn't gonna get far worse with language models.

I think in terms of internet posts

and things that people have been measuring,

it hasn't been a exponential increase

or something extremely measurable,

and things you're talking about

with voice calls and stuff like that.

It could be in modalities that are harder to measure.

So, it's something that it's too soon to tell in terms of,

I think that's political instability via the web is very,

it's monitored by a lot

of researchers to see what's happening.

You're asking about the AGI thing.

If you make me give a year,

I'm be like, okay, I have AI CEOs saying this.

They've been saying two years

for a while. - Mm-hmm.

- I think that they're people like Dario at Anthropic,

the CEO has thought about this so deeply.

I need to take their word seriously,

but also understand that they have different incentives.

So, I would be like, add a few years to that,

which is how you get something similar to 2030

or a little after 2030.

- I think to some extent, we have capabilities

that hit a certain point where any one person could say,

oh, okay, if I can leverage those capabilities

for X amount of time, this is AGI.

Call it '27, '28.

But then the cost of actually operating that capability

- Yeah, this is gonna be - is

- my point. (chuckles) - so, so extreme

that no one can actually deploy it at scale

and mass to actually completely revolutionize the economy

on a snap of a finger.

So, I don't think it will be like

a snap of the finger moment. - Yeah, it's a physical

constraint type- - Rather it'll be a,

oh, the capabilities are here,

but I can't deploy it everywhere.

And so, one simple example going back to 2023

was when being with GPT-4 came out

and everyone was freaking out about Search.

- Oh gosh. - Perplexity came out.

If you did the cost on like, hey,

implementing GPT-3 into every Google search,

it was like, oh, okay,

this is just like physically impossible to implement.

And as we step forward

to going back to the test-time compute thing, a query for...

You asked ChatGPT a question, it cost cents

# Chapter 6

- my point. (chuckles) - so, so extreme

that no one can actually deploy it at scale

and mass to actually completely revolutionize the economy

on a snap of a finger.

So, I don't think it will be like

a snap of the finger moment. - Yeah, it's a physical

constraint type- - Rather it'll be a,

oh, the capabilities are here,

but I can't deploy it everywhere.

And so, one simple example going back to 2023

was when being with GPT-4 came out

and everyone was freaking out about Search.

- Oh gosh. - Perplexity came out.

If you did the cost on like, hey,

implementing GPT-3 into every Google search,

it was like, oh, okay,

this is just like physically impossible to implement.

And as we step forward

to going back to the test-time compute thing, a query for...

You asked ChatGPT a question, it cost cents

for their most capable model of chat to get a query back.

To solve an ARC-AGI problem though, cost 5 to 20 bucks.

And this is an a-

- [Nathan] It's only going up from there.

- This is 1,000, 10,000x factor difference in cost

to respond to a query versus do a task.

And the task of ARC-AGI, it's not like,

it's simple to some extent,

but it's also like what are the tasks that we want A...

Okay, AGI, quote, unquote,

"what we have today" can do ARC-AGI.

Three years from now,

it can do much more complicated problems,

but the cost is gonna be measured in thousands and thousands

and hundreds of thousands of dollars of GPU time,

and there just won't be enough power,

GPUs, infrastructure - Yeah.

- to operate this, and therefore,

shift everything in the world on the snap the finger.

But at that moment,

who gets to control and point the AGI at a task.

And so, this was in Dario's post that he's like,

hey, China can effectively

and more quickly than us, point their AGI at military tasks.

And they have been in many ways,

faster at adopting certain new technologies

into their military, especially with regards to drones.

The US maybe has a long-standing

large air sort of fighter jet type of thing, bombers,

but when it comes to asymmetric arms such as drones,

they've completely leapfrogged the US and the west.

And the fear that Dario is pointing out there,

I think, is that, yeah, great,

we'll have AGI in the commercial sector.

The US military won't be able to implement it super fast.

Chinese military could

and they could direct all their resources

to implementing it in the military,

and therefore solving military logistics

or solving some other aspect of disinformation

for targeted certain set of people,

so that they can flip a country's politics,

or something like that, that is actually like catastrophic

versus the US just wants to,

'cause it'll be more capitalistic allocated

just towards whatever - Mm.

- is the highest return on income,

which might be like building factories better or whatever.

- So, everything I've seen,

people's intuition seems to fail on robotics.

So, you have this kind of general optimism.

I've seen this on self-driving cars.

People think it's much easier problem than it is.

Similar with drones.

Here, I understand it a little bit less,

but I've just seen the reality of the war in Ukraine

and the usage of drones on both sides.

And it seems that humans

still far outperform any fully autonomous systems.

AI is an assistant, but humans drive FPV drones

where the humans controlling most of it

just far, far, far outperforms AI systems.

So, I think it's not obvious to me

that we're going to have swarms

of autonomous robots anytime soon in the military context.

Maybe the fastest I can imagine is 2030,

which is why I said 2030 for the super powerful AI.

Whenever you have large-scale swarms

of robots doing military actions,

that's when the world just starts to look different to me.

So, that's the thing I'm really worried about.

But there could be cyber war type of technologies

that from social engineering,

to actually just swarms the robots that find attack vectors

in our code bases,

and shut down power grids, that kind of stuff.

And it could be one of those things

like on any given weekend or something,

power goes out, nobody knows why,

and the world changes forever.

Just power going out for two days

in all of the United States,

that will lead to murder to chaos.

But going back to export controls,

do you see that as a useful way

to control the balance of power geopolitically

in the context of AI?

- And I think going back to my viewpoint

is if you believe we're in this stage of economic growth

and change that we've been in for the last 20 years,

the export controls

are absolutely guaranteeing that China will win long-term,

if you do not believe AI

is going to make significant changes

to society in the next 10 years or 5 years.

Five-year timelines are what the more executives

and such of AI companies

and even big tech companies believe.

But even tenure timelines, it's reasonable.

But once you get to, hey,

these timelines are below that time period,

then the only way to create a sizable advantage

or disadvantage for America

versus China is if you constrain compute.

Because talent is not really something that's constraining.

China arguably has more talent,

more STEM graduates, more programmers.

The US can draw upon the world's people, which it does.

There's tons of foreigners in the AI industry-

- [Nathan] So many of these AI teams

are all people without a US passport.

- Yeah. (Nathan laughing)

Many of them are Chinese people

who are moving - Yeah.

- to North America, and that's great.

That's exactly what we want.

But there's that talent is one aspect,

but I don't think that's one

that is a measurable advantage for the US or not.

It truly is just whether or not compute.

Now, even on the compute side,

when we look at chips versus data centers.

China has the unprecedented ability

to build ridiculous sums of power clockwork.

They're always building more and more power.

They've got steel mills that individually

are the size of the entire US industry.

And they've got aluminum mills

that consume gigawatts and gigawatts of power.

And when we talk about what's the biggest data center,

OpenAI made this huge thing about Stargate,

their announcement there,

that's like once it's fully built out in a few years,

it'll be two gigawatts of power.

And this is still smaller

than the largest industrial facilities in China.

China, if they wanted to build the largest data center

in the world, if they had access to the chips, could.

So, it's just a question of when, not if.

- So, their industrial capacity

far exceeds the United States?

- [Dylan] Exactly.

- To the the manufacture stuff.

- Yeah. - So, long-term,

they're going to be manufacturing chips there.

- Chips are a little bit more specialized.

I'm specifically referring to the data centers.

Chips, fabs take huge amounts of power, don't get me wrong.

That's not necessarily the gating factor there.

The gating factor on how fast people

can build the largest clusters today in the US is power.

Whether it's now it could be power generation,

power transmission, substations,

and all these sorts of transformers and all these things,

building the data center, these are all constraints

on the US industry's ability to build larger

and larger training systems,

as well as deploying more and more inference compute.

- I think we need to make the point clear on why the time

is now for people that don't think about this,

'cause essentially with export controls,

you're making it so China

cannot make or get cutting edge chips.

And the idea is that if you time this wrong,

China is pouring a ton of money into their chip production.

And if you time it wrong,

they're going to have more capacity for production,

more capacity for energy,

and figure out how to make the chips

and have more capacity

than the rest of the world to make the chips,

because everybody can buy,

they're gonna sell their Chinese chips to everybody.

They might subsidize them.

And therefore, if AI takes a long time

to become differentiated,

we've kneecapped the financial performance

of American companies.

Nvidia can sell less. TSMC cannot sell to China.

So, therefore, we have less demand

to therefore to keep driving the production cycle.

So, that's the assumption behind the timing

being important. - Less than 10 years

or 5 years to above.

China will win because of these restrictions long-term,

unless AI does something in the short-term,

which I believe AI will do,

make massive changes to society in the medium short-term.

And so, that's the big unlocker there.

And even today,

if Xi Jinping decided to get,

quote, unquote, "scale pilled",

i.e, decide that scaling laws are what matters,

just like the US executives like Satya Nadella

and Mark Zuckerberg, and Sundar,

and all these US executives of the biggest,

most powerful tech companies,

have decided they're scale pilled

and they're building multi-gigawatt data centers.

Whether it's in Texas or Louisiana, or Wisconsin,

wherever it is, they're building these massive things

that cost as much as their entire budget

for spending on data centers globally in one spot.

This is what they've committed to

for next year, year after, et cetera.

And so, they're so convinced

that this is the way that this is what they're doing.

But if China decided to, they could do it faster than us.

But this is where the restrictions come in.

It is not clear that China as a whole has decided,

from the highest levels that this is a priority.

The US has.

You see Trump talking about DeepSeek

and Stargate within the same week.

And the Biden admin as well

had a lot of discussions about AI and such.

It's clear that they think about it.

Only just last week

did DeepSeek meet the second in command of China.

They have not even met the top,

and haven't met Xi, she hasn't set down.

And they only just released a subsidy

of a trillion RMB, roughly $160 billion,

which is closer to the spending of like Microsoft and Meta,

and Google combined for this year.

So, it's like they're realizing it just now.

But that's where these export restrictions come in

and say, hey, you can't ship

the most powerful US chips to China.

You can ship a cut down version.

You can't ship the most powerful chips

to all these countries

who we know are just gonna rent it to China.

You have to limit the numbers.

- [Nathan] And the tools.

Same- - And same

with manufacturing equipment tools,

all these different aspects, but it all stems from AI,

and then what downstream can slow them down in AI.

And so, the entire semiconductor restrictions,

you read them, they're very clear,

it's about AI and military civil fusion of technology.

It's very clear.

And then, from there, it goes, oh,

well, we're banning them from buying lithography tools

and etch tools, and deposition tools.

And, oh, this random subsystem

from a random company that's tiny.

Why are we banning this?

Because all of it,

the US government has decided, is critical to AI systems.

- I think the fulcrum point is the transition

from seven nanometer to five nanometer chips,

where I think it was Huawei

that had the seven nanometer chip a few years ago,

which caused another political brouhaha

almost like this moment.

And then, it's the ASML deep UV. What is that?

Like extreme ultraviolet lithography.

- To set context on the chips,

what Nathan's referring to is in 2020,

Huawei released their Ascend 910 chip,

which was an AI chip, first one on seven nanometer

before Google did, before Nvidia did.

And they submitted it to the MLPerf benchmark,

which is a industry standard

for machine learning performance benchmark.

And it did quite well.

And it was the best chip at the submission.

This was a huge deal.

The Trump admin of course banned, it was 2019,

banned the Huawei

from getting seven nanometer chips from TSMC.

And so, then they had to switch

to using internal domestically produced chips,

which was a multi-year setback.

- Many companies have done seven nanometer chips.

And the question is like, we don't know how much Huawei

was subsidizing production of that chip.

Intel has made seven nanometer chips

that are not profitable, and things like this.

So, this is how it all feeds back

into the economic engine of export controls.

- Well, so you're saying that for now, Xi Jinping

has not felt the AGI,

but it feels like the DeepSeek moment

- Yeah. - might like,

there might be meetings going on now,

where he's gonna start wearing the same T-shirt

and things are gonna escalate. (Nathan and Dylan laughing)

- He may have woken up last week.

Liang Feng met the second command guy,

and they had a meeting.

And then, the next day, they announced the AI subsidies,

which are a trillion RMB.

- So, it's possible that this DeepSeek moment

is truly the beginning of a cold war.

- That's what a lot of people are worried about.

People in AI have been worried

that this is going towards a cold war

or already is. - But there is,

it's not DeepSeek's fault, but there's something,

a bunch of factors came together

where it was like explosion. - No, history works.

- It all has to do with Nvidia stock going down problem.

But it's just some (Nathan laughing)

mass hysteria (Lex drowns out Nathan)

that happened that eventually led

to Xi Jinping having meetings and waking up to this idea.

- And the US government realized in October 7th, 2022,

before ChatGPT released,

that restriction on October 7th,

which dropped and shocked everyone.

And it was very clearly aimed at AI.

Everyone was like, what the heck are you doing?

- And diffusion was out then,

but not ChatGPT. - Yeah, but not ChatGPT.

- So, it was like starting to be rumblings like-

- Of what gen AI can do to society,

but it was very clear, I think,

to at least National Security Council

and those sort of folks

that this was where the world is headed,

this cold war that's happening.

- So, is there any concerns that the export controls

push China to take military action on Taiwan?

- This is the big risk.

The further you push China away from having access

to cutting edge American and global technologies,

the more likely they are to say,

well, 'cause I can't access it, I might as well...

No one should access it.

And there's a few interesting aspects of that.

China has a urban rural divide like no other.

They have a male/female birth ratio like no other,

to the point where, if you look in most of China,

it's like the ratio's not that bad.

But when you look at single dudes in rural China,

it's like a 30 to 1 ratio. - Mm-hmm.

- And those are disenfranchised dudes.

Quote, unquote, the US has an "incel problem"

like China does too.

It's just they're placated in some way or crushed down.

What do you do with these people?

And at the same time, you're not allowed

to access the most important technology,

at least the US thinks so.

China's maybe starting to think

this is the most important technology

by starting to dump subsidies in it.

They thought EVs and renewables

were the most important technology.

They dominate that now.

Now, they started thinking about semiconductors

in the late 2010s and early 2020s,

and now they've been dumping money

and they're catching up rapidly,

and they're gonna do the same with AI.

Because they're very talented.

So, the question is like,

when does this hit a breaking point?

And if China sees this as, hey, they can continue...

If not having access and starting a true hot war.

Taking over Taiwan or trying to subvert its democracy

in some way, or blockading it,

hurts the rest of the world far more than it hurts them,

this is something they could potentially do.

And so, is this pushing them towards that? Potentially.

I'm not quite a geopolitical person,

but it's obvious that the world regime of peace

and trade is super awesome for economics.

But at some point, it could break.

- I think we should comment why Chinese economy

# Chapter 7

Now, they started thinking about semiconductors

in the late 2010s and early 2020s,

and now they've been dumping money

and they're catching up rapidly,

and they're gonna do the same with AI.

Because they're very talented.

So, the question is like,

when does this hit a breaking point?

And if China sees this as, hey, they can continue...

If not having access and starting a true hot war.

Taking over Taiwan or trying to subvert its democracy

in some way, or blockading it,

hurts the rest of the world far more than it hurts them,

this is something they could potentially do.

And so, is this pushing them towards that? Potentially.

I'm not quite a geopolitical person,

but it's obvious that the world regime of peace

and trade is super awesome for economics.

But at some point, it could break.

- I think we should comment why Chinese economy

would be hurt by that is that they're export-heavy.

I think the United States buys so much,

like if that goes away, that's how their economy goes.

- Well, also, they just would not be able

to import raw materials from all over the world.

The US would just shut down the strait of Malacca

and at the same time, the US entire,

you could argue almost all the GDP growth in America

since the '70s has been either population growth or tech.

Because your life today is not that much better

than someone from the '80s outside of tech.

Cars, they all have semiconductors in them everywhere.

Fridges, semiconductors everywhere.

These funny stories about how Russians

were taking apart laundry machines

because they had certain Texas instrument chips

that they could then repurpose

and put into their anti-missile missile things,

their S-400 or whatever.

You would know more about this,

but there's all sorts of,

everything about semiconductors

is so integral to every part of our lives.

- So, can you explain the role of TSMC

in this story of semiconductors and maybe also

how the United States can break the reliance on TSMC?

- I don't think it's necessarily breaking their alliance.

I think it's getting TSMC to build in the US.

So, taking a step back.

TSMC produces most of the world's chips,

especially on the foundry side.

There's a lot of companies

that build their own chips, Samsung, Intel,

STMicro, Texas Instruments, Analog Devices,

all these kinds of companies build their own chips and XP.

But more and more of these companies

are outsourcing to TSMC and have been for multiple decades.

- Can you explain the supply chain there

and where most of TSMC is in terms of manufacturing?

- Sure.

So, historically, supply chain was,

companies would build their own chips.

It'd be a company-started, they'd build their own chips,

and then they'd design the chip

and build the chip, and sell it.

Over time, this became really difficult

because the cost of building a fab

continues to compound every single generation.

Of course the technology, figuring out the technology for it

is incredibly difficult regardless,

but just the dollars and cents that are required ignoring,

saying, hey, yes, I have all the technical capability,

which it's really hard to get that, by the way.

Intel's failing, Samsung's failing, et cetera.

But if you look at just the dollars to spend

to build that next generation fab, it keeps growing.

Sort of like Moore's Laws

having the cost of chips every two years.

There's a separate law

that's doubling the cost of fabs every handful of years.

And so, you look at a leading edge fab

that is gonna be profitable today,

that's building three nanometer chips

or two nanometer chips in the future,

that's gonna cost north of 30, $40 billion.

And that's just for like a token amount.

That's like the base building blocking,

you probably need to build multiple.

And so, when you look at the industry, over the last,

if I go back 20, 30 years ago, there were 20,

30 companies that could build the most advanced chips,

and then they would design them themselves and sell them.

So, companies like AMD would build their own chips.

Intel of course still

builds their own chips they're very famous for.

IBM would build their own chips.

And you could just keep going down the list.

All these companies built their own chips.

Slowly, they kept falling like flies.

And that's because of what TSMC did.

They created the foundry business model,

which is, I'm not gonna design any chips,

I'm just gonna contract manufacturer chips for other people.

And one of their early customers is Nvidia.

Nvidia is the only semiconductor company

that's doing more than a billion dollars of revenue

that was started in the era of Foundry.

Every other company started before then,

and at some point had fabs, which is actually incredible.

Like AMD and Intel and Broadcom-

- [Nathan] Such a great fact. (Nathan drowns out Dylan)

- It's like everyone (Nathan laughing)

had fabs at some point,

or some companies like Broadcom,

it was like a merger amalgamation

of various companies that rolled up.

But even today, Broadcom has fabs.

They build iPhone, RF radio chips in Colorado for Apple.

All these companies had fabs, and for most of the fabs,

they threw them away or sold them off,

or they got rolled into something else.

And now, everyone relies on TSMC.

Including Intel, their latest PC chip uses TSMC chips.

It also uses some intel chips, but it uses TSMC process.

- Can you explain why the foundry model

is so successful for these companies?

Why are they going

with TSMC- - Economies of scale.

- Scale. - Yeah.

So, like I mentioned, the cost of building a fab is so high.

The R&D is so difficult.

And when you look at companies

that had their own vertical stack,

there was an antiquated process of like, okay,

I'm so hyper customized to each specific chip.

But as we've gone through the history

of the last 50 years of electronics and semiconductors,

A, you need more and more specialization,

because Moore's Law has died, Dennard scaling has died.

i.e, chips are not getting better just for free.

From manufacturing,

you have to make real architectural innovations.

Google is not just running on Intel CPUs for web serving.

They have a YouTube chip, they have TPUs,

they have pixel chips, they have a wide diversity of chips

that generate all the economic value of Google.

It's running all the services and stuff.

And so, and this is just Google

and you could go across any company in the industry,

and it's like this.

Cars contain 5,000 chips, 200 different varieties of them.

All these random things.

A Tesla door handle has two chips. It's ridiculous.

And it's a cool door handle.

You don't think about it,

but it's like, has two really chipped,

like penny chips in there.

Anyways, so as you have more diversity of chips,

as you have more specialization required,

and the cost of fabs continues to grow, you need someone

who is laser-focused on building the best process technology

and making it as flexible as possible.

- I think you could say it simpler,

which is the cost per fab goes up.

And if you are a small player,

that makes a few types of chips.

You're not gonna have the demand

to pay back the cost of the fab.

Whereas Nvidia can have many different customers

and aggregate all this demand into one place,

and then they're the only person that makes enough money

building chips to buy the next, to build the next fab.

So, this is why the companies slowly get killed,

'cause they have 10 years ago a chip

that is profitable and is good enough,

but the cost to build the next one goes up.

They may try to do this, fail,

because they don't have the money to make it work,

and then they don't have any chips.

Or they build it and it's too expensive and they just have

not profitable chips. - Or there's more

failure points of, you could have one little process-related

to some sort of chemical etch or some sort of plasma etch,

or some little process that screws up,

you didn't engineer it right,

and now the whole company falls apart, you can't make chips.

And so, super, super powerful companies like Intel,

they had the weathering storm to like, hey,

they still exist today, even though they really screwed up

their manufacturing six, seven years ago.

But in the case of like AMD, they almost went bankrupt.

They had to sell their fabs to Mubadala, UAE.

And that became a separate company

called GlobalFoundries, which is a foundry firm.

And then, AMD was able to then focus

on the return back up was like,

hey, let's focus on making chiplets

and a bunch of different chips for different markets.

And focusing on specific workloads

rather than all of these different things.

And so, you get more diversity of chips,

you have more companies than ever designing chips,

but you have fewer companies than ever manufacturing them.

And this is where TSMC comes in,

is they've just been the best.

They are so good at it.

They're customer-focused,

they make it easy for you to fabricate your chips.

They take all of that complexity

and try and abstract a lot of it away from you.

They make good money, they don't make insane money,

but they make good money.

And they're able to aggregate all this demand

and continue to build the next fab,

the next fab, the next fab.

- So, why is Taiwan so special for TSMC?

Why is it happening there?

Can it be replicated inside the United States?

- Yeah, so there's aspects of it

that I would say yes and aspects that I'd say no.

TSMC is way ahead,

because Former Executive Morris Chang

of Texas Instruments wasn't promoted to CEO,

and he is like, screw this,

I'm gonna go make my own chip company.

And he went to Taiwan and made TSMC.

And there's a whole lot more story there.

So, it could have been Texas Instruments,

it could have been TSMC,

but Texas Semiconductor Manufacturing,

instead of Texas Instruments. (Nathan laughing)

So, there is that whole story there,

but the race- - Sitting here in Texas.

- And that sounds like a human story,

like it didn't get promoted?

- Just the brilliance of Morris Chang,

which I wouldn't underplay,

but there's also a different level of how this works.

So, in Taiwan, the number,

top percent of graduates of students

that go to the best school, which is NTU,

the top percent of those all go work to TSMC.

And guess what their pay is,

their starting pay is like $80,000, $70,000.

Which is like, that's like starting pay

for a good graduate in the US.

Not the top, the top graduates are making hundreds

of thousands of dollars at the Googles and the Amazons,

and now I guess the OpenAIs of the world.

So, there is a large dichotomy of like,

what is the top 1% of the society doing

and where are they headed because of economic reasons.

Intel never paid that crazy good.

And it didn't make sense to them.

That's one aspect, where's the best going?

Second is the work ethic.

We like to work, you work a lot, we work a lot,

but at the end of the day,

what is the time and amount of work that you're doing

and what does a fab require?

Fabs are not work from home jobs.

They are, you go into the fab and grueling work.

There's, hey, if there is any amount of vibration.

An earthquake happens, vibrates the machines,

they're either broken,

you've scrapped some of your production.

And then, in many cases, they're like calibrated properly.

So, when TSMC, when there's an earthquake,

recently there's been an earthquake,

TSMC doesn't call their employees,

they just go to the fab and they just show up.

The parking lot gets slammed

and people just go into the fab and fix it.

It's like ants. It's like a hive of ants.

It doesn't get told by the queen what to do.

The ants just know.

- It's like one person just specializes on these one task,

and it's like, you're gonna take this one tool

and you're the best person in the world,

and this is what you're gonna do

for your whole life is this one task and the fab.

- Which is like some special chemistry

plus nano manufacturing on one line of tools

that continues to get iterated.

And yeah, it's like specific plasma etch

for removing silicon dioxide.

That's all you focus on your whole career,

and it's like such a specialized thing.

And so, it's not like the tasks are transferable.

AI today is awesome,

because people can pick it up like that.

Semiconductor manufacturing

is very antiquated and difficult.

None of the materials

are online for people to read easily and learn.

The papers are very dense

and it takes a lot of experience to learn.

And so, it makes the barrier to entry much higher too.

So, when you talk about, hey,

you have all these people that are super specialized,

they will work 80 hours a week in a factory, in a fab.

And if anything goes wrong,

they'll go show up in the middle of the night

because some earthquake,

their wife is like, "There's an earthquake."

He is like, "Great,

I'm gonna go to the fab." (Nathan laughing)

- [Nathan] It's like a crime.

- Would you as an American, do that?

It's like these sorts of things are like,

what, I guess are the exemplifying,

like why TSMC is so amazing.

Now, can you replicate it in the US?

Let's not ignore Intel was the leader

in manufacturing for over 20 years.

They brought every technology to market first besides EUV,

strained silicon, High-K/Metal Gates, FinFET,

and the list just goes on and on and on

of technologies that Intel brought to market first,

made the most money from,

and manufactured at scale first,

best, highest profit margins.

So, we shouldn't ignore that Intel can't do this.

It's that the culture has broken.

You've invested in the wrong things.

They said no to the iPhone.

They had all these different things

regarding mismanagement of the fabs,

mismanagement of designs, this lockup.

And at the same time,

all these brilliant people, these 50,000 PhDs,

or masters that have been working on specific chemical,

or physical processes,

or nano manufacturing processes for decades,

in Oregon, they're still there.

They're still producing amazing work.

It's just like getting it to the last mile

of production at high-yield,

where you can manufacture dozens

and hundreds of different kinds of chips, and it's good.

Customer experience has broken.

It's that customer experience.

Part of it is like,

people will say Intel was too pompous in the 2000s, 2010s.

They just thought they were better than everyone.

The tool guys were like, oh,

I don't think that this is mature enough.

And they're like, ah, you just don't know what we know.

This sort of stuff would happen.

And so, can the US

bring leading edge semiconductor manufacturing to the US?

And thematically, yes.

And we are. TS- - It's happening.

Arizona is getting better and better as time goes on.

- TSMC has built roughly 20% of their capacity

for five nanometer in the US.

Now, this is nowhere near enough.

20% of capacity in the US is like nothing.

And furthermore, this is still dependent on Taiwan existing.

There's important way to separate it out.

There's R&D and there's high volume manufacturing.

Effectively, there are three places in the world

that are doing leading edge R&D.

There's Hsinchu, Taiwan, there's Hillsboro, Oregon,

and there is Pyongyang, South Korea.

These three places

are doing the leading edge R&D for the rest

of the world's leading edge semiconductors.

Now, manufacturing can be distributed more globally.

And this is where this dichotomy exists

of who's actually modifying the process,

who's actually developing the next generation one,

who's improving them?

Is Hsinchu, is Hillsboro, is Pyongyang.

It is not the rest of these fabs like Arizona.

Arizona is a paperweight.

If Hsinchu disappeared off the face of the planet,

within a year, couple years,

Arizona would stop producing too.

It's actually like pretty critical.

One of the things I like to say is if I had a few missiles,

I know exactly where I could cause the most economic damage.

It's not targeting the White House.

It's not- - It's the R&D centers.

- It's the R&D centers for TSMC, Intel, Samsung,

and then some of the memory guys, Micron and Hynix.

- Because they define the future evolution

of these semiconductors and everything's moving so rapidly

that it really is fundamentally about R&D.

And it is all about TSMC, huh?

- And so, TSMC,

you cannot purchase a vehicle without TSMC chips.

You cannot purchase a fridge without TSMC chips.

I think one of the few things you can purchase ironically

is a Texas Instruments graphing calculator,

because they actually manufacture in Texas.

But outside of that, like a laptop,

- It's depressing. - a phone, anything you,

servers, GPUs, none of this stuff can exist.

And this is without TSMC.

And in many cases, it's not even like the leading edge,

sexy five nanometer chip,

three nanometer chip, two nanometer chip.

Oftentimes, it's just some stupid power IC

that's converting from some voltage to another,

and it's made at TSMC.

- This is what China is investing in as well.

It's like they can build out this long tail fab

where the techniques are much more known.

# Chapter 8

And it is all about TSMC, huh?

- And so, TSMC,

you cannot purchase a vehicle without TSMC chips.

You cannot purchase a fridge without TSMC chips.

I think one of the few things you can purchase ironically

is a Texas Instruments graphing calculator,

because they actually manufacture in Texas.

But outside of that, like a laptop,

- It's depressing. - a phone, anything you,

servers, GPUs, none of this stuff can exist.

And this is without TSMC.

And in many cases, it's not even like the leading edge,

sexy five nanometer chip,

three nanometer chip, two nanometer chip.

Oftentimes, it's just some stupid power IC

that's converting from some voltage to another,

and it's made at TSMC.

- This is what China is investing in as well.

It's like they can build out this long tail fab

where the techniques are much more known.

You don't have to figure out these problems with EUV.

They're investing in this,

and then they have large supply

for things like the car door handles and the random stuff.

And that trickles down

into this whole economic discussion as well,

which is they have far more than we do.

And having supply

for things like this is crucial to normal life.

- So, they're starting to invest

in high volume manufacturer, but they're not doing R&D.

- So, they do R&D on their own.

They're just way behind. - Yeah.

- So, I would say like in 2015, China had a five-year plan,

where they defined by 2025 and 2020 certain goals,

including 80% domestic production of semiconductors.

they're not gonna hit that right, to be clear.

But they are in certain areas, really, really close.

Like BYD is probably gonna be the first company

in the world to not have to use TSMC for making...

'Cause they have their own fabs for making chips.

Now, they still have to buy some chips from foreign,

for example, like around self-driving ADAS capabilities.

'Cause those are really high-end,

but at least like a internal combustion engine

has 40 chips in an EV,

just for controlling flow rates and all these things,

and EVs are even more complicated.

So, all these different power ICs

and battery management controllers,

and all these things, they're insourcing.

And this is something that China has been doing since 2015.

Now, as far as the trailing edge,

they're getting so much capacity there.

As far as the leading edge,

i.e, this five nanometer and so on, so forth.

Where GPUs, they are still behind.

And this is the US restrictions

are trying to stop them in the latter.

But all that's happened, is yes,

they've slowed down their five nanometer,

three nanometer, et cetera,

but they've accelerated their, hey,

45 nanometer, 90 nanometer power IC or analog IC,

or random chip in my keyboard, that kind of stuff.

So, there is an angle of the US' actions

have been so, from these export,

from the angle of the export controls,

have been so inflammatory

at slowing down China's progress on the leading edge

that they've turned around

and have accelerated their progress elsewhere,

because they know this is so important.

If the US is gonna lock them out here

or if they lock us out here as well in the trailing edge.

And so, going back, can the US build it here?

Yes, but it's gonna take a ton of money.

I truly think like, to revolutionize

and completely insource semiconductors,

would take a decade and a trillion dollars.

- Is some of it also culture?

Like you said, extreme competence,

extreme work ethic in Taiwan?

- I think if you have the demand

and the money is on the line,

the American companies figure it out.

It's gonna take handholding with the government.

But I think that the culture helps TSMC breakthrough

and it's easier for them.

You could-

- TSMC has some like 90,000 employees.

It's not actually that insane amount.

The Arizona fab has 3,000 from Taiwan,

and these people, their wives were like, yeah,

we're not gonna have kids

unless we use sign up for the Arizona fab.

We go to Arizona and we have our kids there.

There's also a Japan fab where the same thing happened.

And so, these wives drove like,

these dudes to go to Japan

or America to have the kids there.

And it's like it's an element of culture. Yeah, sure.

Taiwan works that hard,

but also the US has done it in the past,

they could do it now.

We can just import, I say import,

the best people in the world if we want to.

- That's where the immigration conversation is a tricky one.

And there's been a lot of debate over that.

But yeah, it seems absurdly controversial

to import the best people in the world.

I don't understand why it's controversial.

That's the one of the ways

of winning. - I'm sure we agree with you.

(Lex laughing) - And even if

you can't import those people,

I still think you could do a lot

to manufacture most of in the US if the money's there.

And so, like-

- It's just way more expensive.

It's not profitable for a long time.

- And that's the context of like the CHIPS Act

is only like $50 billion

relative to some of the renewable initiatives

that were passed in the Inflation Reduction Act

and the Infrastructure Act,

which total in the hundreds of billions of dollars.

And so, the amount of money that the US

is spending on the semiconductor industry is nothing.

Whereas all these other countries

have structural advantages in terms of work ethic

and amount of work, and like things like that.

But also a number of STEM graduates,

the percentile of their best going to that.

But they also have differences in terms of like,

hey, there's just tax benefits in the law

and have been in the law for 20 years.

And then, some countries have massive subsidies.

China has something like $200 billion

of semiconductor subsidies a year.

We're talking about $50 billion in the US over like six.

So, the girth or difference

in the subsidy amounts is also huge.

And so I think,

Trump has been talking about tariffing Taiwan recently.

That's like one of these things

that's like, oh, okay, well,

maybe he doesn't wanna subsidize

the US semiconductor industry.

Obviously, tariffing Taiwan

is gonna cost a lot of things to get much more expensive.

But does it change the equation

for TSMC building more fabs in the US?

That's what he is positing.

- So, can you lay out the, so we laid out the importance,

by the way, it's incredible how much you know about so much.

- [Nathan] We told you Dylan knows all this stuff.

- Yeah. (Nathan laughing)

So, okay, you laid out why TSMC is really important.

If we look out into the future 10, 20 years out,

US-China relationship

seems like it can go to a dark place of cold war,

escalated cold war, even hot war,

or to a good place of anything

from frenemies to cooperation, to working together.

So, in this game theory, complicated game,

what are the different trajectories?

What should US be doing?

What do you see as the different possible trajectories

of US-China relations as both leaders

start to feel the AGI more and more,

and see the importance of chips and the importance of AI?

- Ultimately, the export controls

are pointing towards a separate future economy.

I think the US has made it clear to Chinese leaders

that we intend to control this technology

at whatever cost to global economic integration.

- So, that- - It's hard to unwind that.

(Nathan chuckles)

The card has been played. - To the same extent,

they've also limited US companies for mentoring China.

So, it's been a long time coming.

At some point, there was a convergence.

But over at least the last decade,

it's been branching further and further out.

Like US companies can't enter China,

Chinese companies can't enter the US.

The US is saying, hey, China,

you can't get access to our technologies in certain areas.

And China's rebutting with the same thing around like,

they've done some sort of specific materials

in gallium and things like that,

that they've tried to limit the US on.

There's a US drone company

that's not allowed to buy batteries

and they have military customers.

And this drone company just tells the military customers

like, hey, hey, just get it from Amazon,

'cause I can't actually physically get them.

There's all these things that are happening

that point to further and further divergence.

I have zero idea.

And I would love

if we could all hold hands and sing Kumbaya,

but I have zero idea how that could possibly happen.

- Is the divergence good or bad for avoiding war?

Is it possible that the divergence

in terms of manufacturer chips,

of training AI systems is actually good for avoiding

military conflict? - It's an objective fact

that the world has been the most peaceful

has ever been when there are global hegemons,

or regional hegemons in historical context.

The Mediterranean was the most peaceful ever

when the Romans were there.

China had very peaceful and warring times.

And the peaceful times were when dynasties

had a lock hold over, not just themselves,

but all their tributaries around them.

And likewise, the most peaceful time in human history

has been when the US was the global hegemon,

the last decades.

Now, we've seen things start to slide

with Russia-Ukraine,

with what's going on in the Middle East,

and Taiwan risk, all these different things

are starting to bubble up,

still objectively extremely peaceful.

Now, what happens when it's not one global hegemon,

but it's two?

Obviously, and China will be competitive

or even overtake the US, like it's possible.

And so, this change in global hegemony,

I don't think it ever happens like super peacefully.

When empires fall,

which is a possible trajectory for America,

they don't pull fall gracefully.

They don't just slide out of irrelevance.

Usually, there's a lot of shaking.

And so, what the US is trying to do

is maintain its top position.

And what China is trying to do is become the top position.

And obviously, there's butting of heads here,

in the most simple terms.

- And that could take shape in all kinds of ways,

including proxy wars.

And now- - Yeah, it seems

like it's already happening.

As much as I want there to be centuries of prolonged peace,

it looks like further instability internationally is ahead.

- And the US is sort of like current task is like,

hey, if we control AI, if we're the leader in AI,

and AI could significantly accelerates progress,

then we can maintain the global hegemony position.

And therefore-

- [Nathan] I hope that works.

- And as an American, (Nathan chuckles)

kind of like, okay,

I guess that's gonna lead to peace for us.

Now, obviously, other people around the world

get affected negatively.

Obviously, the Chinese people are not gonna be in

as advantageous of a position if that happens.

But this is the reality of what's being done

and the actions that are being carried out.

- So, can we go back to the specific detail

of the different hardware?

There's this nice graphic in the export controls

of which GPUs are allowed to be exported and which are not.

Can you explain the difference?

Is there, from a technical perspective,

are the H20s promising?

- Yeah, so this goes, and I think we'd have to,

we need to dive really deep into the reasoning aspect

and what's going on there.

But the H20, the US has gone

through multiple iterations of the export controls.

This H800 was at one point allowed back in '23,

but then it got canceled.

And by then, DeepSeek had already built their cluster of,

they claim 2k, I think they actually have like many more,

something like 10k of those.

And now, this H20 is the legally allowed chip.

Nvidia shipped a million of these last year to China.

For context, it was like 4 or 5 million GPUs.

So, the percentage of GPUs

that were this China specific H20 is quite high,

roughly 20%, 25%, 20% or so.

And so, this H20 has been neutered in one way,

but it's actually upgraded in other ways.

And you could think of chips along three axes for AI,

ignoring software stack

and exact architecture, just raw specifications.

There's floating point operations, FLOPS.

There is memory bandwidth, i.e,

and memory capacity, I/O, memory.

And then, there is interconnect,

chip to chip interconnections.

All three of these

are incredibly important for making AI systems.

Because AI systems involve a lot of compute,

they involve a lot of moving memory around,

whether it be two memory or two other chips.

And so, these three vectors.

The US initially had two of these vectors controlled

and one of them not controlled, which was FLOPS

and interconnect bandwidth were initially controlled.

And then, they said, no, no, no, no,

we're gonna remove the interconnect bandwidth

and just make it a very simple only FLOPS.

But now, Nvidia can now make a chip that has, okay,

it's cut down on FLOPS,

so like one third that of the H100

on spec sheet paper performance for FLOPS.

In real world, it's closer to half,

or maybe even like 60% of it.

But then, on the other two vectors,

it's just as good for interconnect bandwidth.

And then, for memory bandwidth and memory capacity,

the H20 has more memory bandwidth

and more memory capacity than the H100.

Now, recently, we, at our research,

we cut Nvidia's production for H20

for this year down drastically.

They were gonna make another 2 million of those this year,

but they just canceled all the orders a couple weeks ago.

In our view, that's because we think

that they think they're gonna get restricted.

Because why would they cancel all these orders for H20?

Because they shipped a million of 'em last year.

They had orders in for a couple million this year,

and just gone.

For H20, B20, a successor to H20, and now they're all gone.

Now, why would they do this?

I think it's very clear.

The H20 is actually better for certain tasks

and that certain task is reasoning.

Reasoning is incredibly different than...

When you look at the different regimes of models,

pre-training is all about FLOPS.

It's all about FLOPS.

There's things you do like mixture of experts

that we talked about, to trade off interconnect,

or to trade off other aspects and lower the FLOPS,

and rely more on interconnect and memory.

But at the end of the day, it's FLOPS is everything.

We talk about models in terms of how many FLOPS there are.

So, we talk about, oh, GPT-4 is 2e25.

Two to the 25th, 25 zeros, FLOP, floating point operations.

- For training. - For training.

And we're talking

about the restrictions for the 2e24 or 25, whatever.

The US has an executive order that Trump recently unsigned,

which was, hey, 1e26, once you hit that number

of floating point operations, you must notify the government

and you must share your results with us.

There's a level of model

where the US government must be told.

And that's 1e26.

And so, as we move forward,

this is an incredibly important...

FLOP is the vector that the government

has cared about historically,

but the other two vectors are arguably just as important.

And especially when we come to this new paradigm,

which the world is only just learning about

over the last six months, reasoning.

- And do we understand firmly

which of the three dimensions is best for reasoning?

So, interconnect, the FLOPS don't matter as much.

Is it memory?

- Memory. Right.

- Yeah, so- - Context length.

We're gonna get into technical stuff

real fast, yeah. (chuckles) - I would just say

there's two articles in this one that I could show,

maybe graphics that might be interesting for you to pull up.

- For the listeners, we're looking at the section

of o1 inference architecture tokenomics.

- Hmm.

Do you wanna explain KV cache before we talk about this?

I think it's better to- - Okay, yeah.

We need to go through a lot of specific technical things

of transformers to make this easy for people.

- Because it's incredibly important

because this changes how models work.

But I think resetting. Why is memory so important?

It's because so far, we've talked about parameter counts.

And mixture of experts, you can change

how many active parameters versus total parameters

to embed more data but have less FLOPS.

But more important, another aspect of,

what's part of this humongous revolution

in the last handful of years is the transformer.

And the attention mechanism.

Attention mechanism is that the model

understands the relationships

# Chapter 9

- For the listeners, we're looking at the section

of o1 inference architecture tokenomics.

- Hmm.

Do you wanna explain KV cache before we talk about this?

I think it's better to- - Okay, yeah.

We need to go through a lot of specific technical things

of transformers to make this easy for people.

- Because it's incredibly important

because this changes how models work.

But I think resetting. Why is memory so important?

It's because so far, we've talked about parameter counts.

And mixture of experts, you can change

how many active parameters versus total parameters

to embed more data but have less FLOPS.

But more important, another aspect of,

what's part of this humongous revolution

in the last handful of years is the transformer.

And the attention mechanism.

Attention mechanism is that the model

understands the relationships

between all the words in its context.

And that is separate from the parameters themselves.

And that is something that you must calculate.

How each token, each word in the context length

is relatively connected to each other.

And I think, Nathan,

- Yeah. It's- - you should explain

KV cache better.

- KV cache is one

of the optimizations- - Yeah.

So, the attention operator has three core things.

It's queries, keys, and values.

QKV is the thing that goes into this.

You'll look at the equation,

you see that these matrices are multiplied together.

These words, query, key, and value,

come from information retrieval backgrounds,

where the query is the thing

you're trying to get the values for

and you access the keys and the values is re-weighting.

My background's not information retrieval

and things like this.

It's just fun to have back links.

And what effectively happens

is that when you're doing these matrix multiplication,

you're having matrices

that are of the size of the context length.

So, the number of tokens that you put into the model.

And the KV cache is effectively

some form of compressed representation

of all the previous tokens in the model.

So, when you're doing this,

we talk about autoaggressive models.

You predict one token at a time.

You start with whatever your prompt was.

You ask a question like, who was the president in 1825?

The model then is gonna generate its first token.

For each of these tokens,

you're doing the same attention operator,

where you're multiplying these query key value matrices.

But the math is very nice,

so that when you're doing this repeatedly,

this KV cache, this key value operation,

you can keep appending the new values to it.

So, you keep track of what your previous values

you're inferring over in this autoaggressive chain.

You keep it in memory the whole time.

And this is a really crucial thing

to manage when serving inference at scale.

There are far bigger experts in this

and there are so many levels of detail that you can go into.

Essentially, one of the key,

quote, unquote, "drawbacks" of the attention operator

and the transformer is that there is a form

of quadratic memory cost

in proportion to the context length.

So, as you put in longer questions,

the memory used in order to make that computation

is going up in the form of a quadratic.

You'll hear about a lot

of other language model architectures

that are sub-quadratic or linear attention forms,

which is state-space models.

We don't need to go down all these now.

And then, there's innovations

on attention to make this memory usage

and the ability to attend over long contexts,

much more accurate and high performance.

- And those innovations are going to help you with,

your highly memory constrain-

- You help with memory constraint and performance.

So, if you put in a book into, I think Gemini is the model

that has the longest context length that people are using.

Gemini is known for 1 million

and now 2 million context length.

You put a whole book into Gemini

and sometimes it'll draw facts out of it.

It's not perfect. They're getting better.

So, there's two things.

It's like one, to be able to serve this on the memory level,

Google has magic with their TPU stack

where they can serve really long contexts.

And then, there's also many decisions along the way

to actually make long context performance work

that supplies the data.

There's subtle changes to these computations and attention.

And it changes the architecture.

But serving long context is extremely memory-constrained,

especially when you're making a lot of predictions.

I actually don't know why input

and output tokens are more expensive,

but I think essentially, output tokens,

you have to do more computation,

'cause you have to sample from the model.

- I can explain that.

So, today, if you use a model, like you look at an API,

OpenAI charges a certain price per million tokens.

And that price for input and output tokens is different.

And the reason is, is that there is,

when you're inputting a query into the model.

Let's say you have a book.

That book, you must now calculate the entire KV cache for,

this key value cache.

And so, when you do that, that is a parallel operation.

All of the tokens can be processed at one time.

And therefore,

you can dramatically reduce how much you're spending.

The FLOP requirements for generating a token

and an input token are identical.

If I input one token

or if I generate one token, it's completely identical.

I have to go through the model.

But the difference is that I can do that input,

i.e, the prefill,

i.e, the prompt simultaneously in a batch nature.

And therefore, it is all FLOP.

- I think the pricing model mostly they use is for input.

Tokens is about one fourth the price

of the output tokens. - Correct.

But then, output tokens,

the reason why it's so expensive

is because I can't do it in parallel.

It's autoaggressive.

Every time I generate a token,

I must not only take the entire,

I must not only read the whole entire model into memory

and activate it, go calculate it to generate the next token.

I also have to read the entire KV cache

and I generate a token,

and then I append that KV, that one token I generated,

and it's KV cache, and then I do it again.

And so, therefore, this is a non-parallel operation.

And this is one where you have to,

in the case of pre-fill or prompt,

you pull the whole model in,

and you calculate 20,000 tokens at once.

These 20,000- - So, these are features

that APIs are shipping,

which is like prompt caching, pre-filling.

'Cause you can drive prices down

and you can make APIs much faster.

If you know you're gonna keep, if you run a business

and you're gonna keep passing the same initial content

to Claude's API, you can load that in

to the Anthropic API and always keep it there.

But it's very different

than we're leading to the reasoning models,

which we showed this example earlier

and read some of this mumbling stuff.

And what happens

is that the output context length is so much higher.

And I learned a lot about this from Dylan's work,

which is essentially as the output work length gets higher,

you're using this, you're writing this quadratic

in terms of memory used,

and then the GPUs that we have,

effectively, you're gonna run out of memory.

And they're all trying to serve multiple requests at once.

So, they're doing this batch processing,

where not all of the prompts are exactly the same,

really complex handling.

And then, as context links gets longer, there's this link.

I think you call it critical batch size,

where your ability to serve more users.

So, how much you can paralyze

your inference plummets,

because of this long contract.

So, your memory usage is going way up

with these reasoning models,

and you still have a lot of users.

So, effectively, the cost to serve multiplies by a ton.

- [Lex] And we're looking at a plot

when the x-axis is sequence length.

- [Dylan] i.e, how many tokens

are being generated/prompt. - Mm-hmm.

- [Dylan] So, if I put in a book, that's a million tokens.

But if I put in, the sky is blue,

then that's like six tokens or whatever.

- I should say that what we're calling reasoning

and chain of thought is extending this sequence length.

- It's mostly output tokens.

- So, before, three months ago,

whenever o1 launched, all of the use cases

for long context length were like,

let me put a ton of documents in and then get an answer out.

And it's a single prefill, compute a lot in parallel,

and then output a little bit.

Now, with reasoning and agents,

this is a very different idea.

Now, instead, I might only have like, hey, do this task,

or I might have all these documents,

but at the end of the day,

the model is not just producing a little bit.

It's producing tons of information,

this chain of thought, - Tens of thousands

token. - just continues to go

and go and go and go.

And so, the sequence length is effectively

that if it's generated 10,000 tokens,

it's 10,000 sequence length.

And plus whatever you input it in the prompt.

And so, what this chart is showing,

and it's a logarithmic chart,

is as you grow from 1k to 4k or 4k to 16k,

the memory requirements grow so fast for your KV cache

that you end up not being able to run a certain number of...

Your sequence length is capped or the number of users

you can serve. - Let's say the model.

So, this is showing for a 405b model and batch size 64.

- Llama 3.1-405b. - Yeah.

And batch size is crucial to,

essentially they just like, you wanna have higher batch size

to parallel your throughput.

- 64 different users at once, right?

- Yeah. - And therefore,

your serving costs are lower.

Because the server costs the same.

This is eight H100s, roughly $2 an hour per GPU.

That's $16 an hour.

That is like somewhat of a fixed cost.

You can do things to make it lower of course,

but it's like $16 an hour.

Now, how many users can you serve?

How many tokens can you generate?

And then, you divide the two and that's your cost.

And so, with reasoning models,

this is where a lot of the complexity comes about

and why memory is so important.

Because if you have limited amounts of memory,

then you can't serve so many users.

If you have limited amounts of memory,

your serving speeds get lower.

And so, your costs get a lot, lot worse.

Because all of a sudden,

if I was used to, hey, on this $16 an hour server,

I'm serving Llama 405b.

Or if I'm serving DeepSeek-V3,

and it's all chat style applications,

i.e, we're just chit-chatting.

the sequence sensor, a thousand, a few thousand.

When you use a language model,

it's a few thousand context length most times.

Sometimes you're dropping a big document,

but then you process it,

you get your answer, you throw it away.

You move on to the next thing.

Whereas with reasoning,

I'm now generating tens of thousands of tokens in sequence.

And so, this memory, this KV cache has to stay resonant.

- Yeah. - And you have

to keep loading it,

you have to keep it in memory constantly.

And now, this butts out other users.

If there's now a reasoning task

and the model's capable of reasoning, then all of a sudden,

that memory pressure

means that I can't serve as many users simultaneously.

- Let's go into DeepSeek again.

So, we're in the post DeepSeek-R1 time I think.

And there's two sides to this market

watching how hard it is to serve it.

On one side, we're gonna talk about DeepSeek themselves.

They now have a chat app

that got to number one on the App Store.

Disclaimer, number one on the App Store

is measured by velocity.

So, it's not necessarily saying

that more people have the DeepSeek app

than ChatGPT app. - Mm-hmm.

Yep. - But it is still remarkable.

Claude has never hit the number one on the App Store.

Even though everyone in San Francisco is like,

oh my god, you gotta use Claude, don't use ChatGPT.

So, DeepSeek hit this.

They also launched an API product recently

where you can ping their API

and get these super long responses for R1 out.

And at the same time as these are out,

we'll get to what's happened to them.

Because the model waits for DeepSeek R-1

are openly available and the license is very friendly,

the MIT license commercially available,

all of these mid-size companies

and big companies are trying

to be first to serve R1 to their users.

We are trying to evaluate R1,

'cause we have really similar research going on.

We released the model and we're trying to compare to it.

And out of all the companies

that are, quote, unquote, serving R1,

and they're doing it at prices

that are way higher than the DeepSeek API,

most of them barely work, and the throughput is really low.

- To give context, everyone,

one of the parts of freaking this out

was China reached capabilities.

The other aspect is they did it so cheap.

And the so cheap,

we kind of talked about on the training side

why it was so cheap slash- - Yeah, let was talk

about why it's so cheap on the inference.

It works well and it's cheap.

- Yeah. - Why is R1 so damn cheap?

- So, I think there's a couple factors here.

One is that they do have model architecture innovations.

This MLA, this new attention that they've done is different

than the attention from attention is all you need,

the transformer attention.

Now, others have already innovated.

There's a lot of work like MQA GQA, local, global,

all these different innovations that try to bend the curve.

It's still quadratic, but the constant is now smaller.

- Related to our previous discussion,

this multi-head latent attention can save about 80

to 90% in memory from the attention mechanism,

which helps, especially along context.

- It's 80 to 90% versus the original,

but then versus what people

are actually doing, it's still an innovation.

- This 80 to 90% doesn't say that the whole model

is 80 to 90% cheaper, just as one part of it.

- Well, and not just that.

Other people have implemented techniques

like local, global, - Yeah, yeah, yeah.

- and sliding window and GQA, MQA.

But anyways, DeepSeek has their attention mechanism

is a true architectural innovation.

They did tons of experimentation

and this dramatically reduces the memory pressure.

It's still there.

It's still attention, it's still quadratic,

it's just dramatically reduced it relative to prior forms.

- All right. That's the memory pressure.

I should say, in case people don't know,

R1 is 27 times cheaper than o1.

(Nathan chuckles)

- Yes. - We think that OpenAI

had a large margin built-in.

- [Lex] Okay. So, that's one-

- There's multiple factors.

We should break down the factors, I think.

- It's two bucks per million token output for R1

and $60 per million token output for o1.

- [Nathan] Yeah, let's look at this.

- So, I think this is very important.

OpenAI is that drastic gap between DeepSeek in pricing,

but DeepSeek is offering the same model

because they open-weight it to everyone else

for a very similar, much lower price

than what others are able to serve it for.

So, there's two factors here.

Their model is cheaper. It is 27 times cheaper.

Well, I don't remember the number

exactly off the top of my head.

- So, we're looking at a graphic

that's showing different places serving V3.

- Yeah. - DeepSeek-V3,

which is similar to DeepSeek-R1.

And there's a vast difference

- In serving cost. - in serving cost.

And what explains that difference?

- And so, part of it is OpenAI has a fantastic margin.

When they're doing inference,

their gross margins are north of 75%.

So, that's a 4 to 5x factor right there

of the cost difference,

is that OpenAI is just making crazy amounts of money

because they're the only one with the capability.

- Do they need that money? Are they using it for R&D?

- They're losing money obviously as a company,

because they spend so much on training.

So, the inference itself - Right.

- is a very high margin,

but it doesn't recoup the cost

of everything else they're doing.

- Okay. - So, yes,

they need that money because the revenue

and margins pay for continuing to build the next thing,

- So- - alongside

raising more money.

- So, the suggestion is that DeepSeek

is like really bleeding out money.

- Well, so here's one thing.

We'll get to this in a second.

But DeepSeek doesn't have any capacity

to actually serve the model.

They stop signups.

The ability to use it is like non-existent now.

For most people because so many people are trying to use it,

they just don't have the GPUs to serve it.

OpenAI has hundreds of thousands of GPUs between them

and Microsoft to serve their models.

DeepSeek has a factor of much lower.

Even if you believe our research, which is 50,000 GPUs,

and a portion of those are for research,

portion of those are for the hedge fund,

they still have nowhere close to the GPU volumes

and capacity to serve the model at scale.

So, it is cheaper.

A part of that is OpenAI making a ton of money.

Is DeepSeek making money on their API?

Unknown. I don't actually think so.

And part of that is this chart.

Look at all the other providers.

Together AI, Fireworks AI are very high-end companies.

X, Meta, Together AI's Tri Dao,

and the inventor of like flashattention,

which is a huge efficiency technique.

They're very efficient, good companies,

and do know those companies make money.

Not tons of money on inference, but they make money.

And so, they're serving at a 5 to 7x difference in cost.

And so, now, when you equate, okay,

OpenAI is making tons of money, that's like a 5x difference.

# Chapter 10

and a portion of those are for research,

portion of those are for the hedge fund,

they still have nowhere close to the GPU volumes

and capacity to serve the model at scale.

So, it is cheaper.

A part of that is OpenAI making a ton of money.

Is DeepSeek making money on their API?

Unknown. I don't actually think so.

And part of that is this chart.

Look at all the other providers.

Together AI, Fireworks AI are very high-end companies.

X, Meta, Together AI's Tri Dao,

and the inventor of like flashattention,

which is a huge efficiency technique.

They're very efficient, good companies,

and do know those companies make money.

Not tons of money on inference, but they make money.

And so, they're serving at a 5 to 7x difference in cost.

And so, now, when you equate, okay,

OpenAI is making tons of money, that's like a 5x difference.

And the companies that are trying to make money

for this model is like a 5x difference.

There is still a gap.

There's still a gap

and that is just DeepSeek being really freaking good.

The model architecture, MLA, the way they did the MoE,

all these things,

there is like legitimate just efficiency differences-

- It's all their low level libraries

that we talked about in training,

some of them probably translate to inference

and those weren't released. - Yeah.

- So, we may go a bit into conspiracy land,

but is it possible the Chinese government

is subsidizing DeepSeek?

- I actually don't think they are.

I think when you look at the Chinese labs,

there's Huawei has a lab, Moonshot AI,

there's a couple other labs out there

that are really close with the government.

And then, there's labs like Alibaba and DeepSeek,

which are not close with the government.

And we talked about the CEO,

this like reverent figure who's quite different,

who has like- - Sounds awesome. (chuckles)

- Very different viewpoints based on the Chinese interviews

that are translated

than what the CCP might necessarily want.

Now, to be clear, does he have a loss leader

because he can fund it through his hedge fund?

Yeah, sure.

- So, the hedge fund might be subsidizing it.

- Yes. I mean, they absolutely did.

Because DeepSeek has not raised much money.

They're now trying to raise around in China,

but they have not raised money historically.

It's all just been funded by the hedge fund.

And he owns like over half the company,

like 50, 60% of the company's owned by him.

- Some of the interviews,

there's discussion on how doing this as a recruiting tool.

You see this at the American companies too.

It's like having GPUs, recruiting tool,

being at the cutting edge of AI, recruiting tool.

- Open sourcing. - Open sourcing,

recruiting tool. - That is so much talent.

They were so far behind and they got so much talent,

- Yeah. - Because they just

opened source stuff. - Yeah.

- More conspiracy thoughts.

Is it possible since they're a hedge fund

that they timed everything with this release and the pricing

and they shorted an Nvidia stock

and stock of US AI companies,

and released it with Stargate, like just perfect timing

to be able to make money. (Lex drowns out Nathan)

(Lex laughing)

- They've released it on Inauguration Day.

They know the international,

what is on the international calendar,

but I don't expect them to.

If you listen to their motivations for AI, it's like...

- [Lex] No, if you-

- They released V3 on like December 26th.

Who releases the day - Yeah.

- after Christmas? - Yeah. (chuckles)

- No one looks.

They had released the papers before this,

the V3 paper and the R1 paper.

So, people had been looking at it and being like, wow.

And then, they just released the R1 model.

I think they're just shipping as fast as they can

and like, who cares about Christmas?

- We should- - Who cares about,

get it out before Chinese New Year?

Obviously, - Yeah.

- which just happened.

I don't think they actually were timing the market

or trying to make the biggest splash possible.

I think they're just shipping.

- I think that's one of their big advantages.

We know that a lot of the American companies

are very invested in safety,

and that is the central culture of a place like Anthropic.

And I think Anthropic sounds like a wonderful place to work.

But if safety is your number one goal,

it takes way longer to get artifacts out.

That's why Anthropic is not open sourcing things,

that's their claims.

But there's reviews internally.

Anthropic mentions things to international governments.

There's been news of how Anthropic

has done pre-release testing

with the UK AI Safety Institute.

All of these things add inertia

to the process of getting things out.

And we're on this trend line where progress is very high.

So, if you reduce the time

from when your model is done training,

you run a vows that's good,

you want to get it out as soon as possible

to maximize the perceived quality of your outputs.

DMC does this so well.

- Dario explicitly said Claude 3.5 Sonnet

was trained nine months

or a year- - 9 to 10 months ago.

- 9 to 10 months ago, and I think it took them

another handful of months to release it.

So, it's like there is a significant gap here.

And especially with reasoning models,

the word in the San Francisco Street

is that Anthropic has a better model than o3.

And they won't release it. Why?

Because chains of thought are scary.

And they are legitimately scary.

If you look at R1, it flips back

and forth between Chinese and English,

sometimes it's gibberish,

and then the right answer comes out.

And for you and I,

it's like great. (Nathan and Lex laughing)

- This is why people are infatuated with you.

You're telling me this is a high value thing

and it works and is doing those?

It's amazing. - Yeah. It's incredible.

- You talked about that chain of thought

for that philosophical thing,

- Yeah. - which is not something

they trained it to be philosophically good.

It's just an artifact

of the chain of thought training it did.

But that's super important in that like,

can I inspect your mind and what you're thinking right now?

No.

And so, I don't know if you're lying to my face.

And chain of thought models are that way.

This is a true, quote, unquote,

"risk" between a chat application,

where, hey, I asked the model to say bad words or whatever,

or how to make anthrax.

And it tells me that's unsafe, sure,

but that's something I can get out relatively easily.

What if I tell the AI to do a task,

and then it does the task

all of a sudden randomly in a way that I don't want it.

And now, that has much more task

versus response is very different.

So, the bar for safety is much higher.

At least this is Anthropic's case.

For DeepSeek, they're like ship, right?

- Yeah.

So, the bar for safety

is probably lowered a bit because of DeepSeek.

There's parallels here to the space race.

The reason the Soviets probably put a man in space first

is 'cause their approach to safety was,

the bar for safety was lower.

- And they killed that dog, and all these things.

So, it's like... - Less risk-averse

than the US-based program.

And there's parallels here.

But there's probably going to be downward pressure

on that safety bar for the US companies.

- And this is something that Dario talks about is like,

that's the situation that Dario wants to avoid

is Dario talks too about the difference

between race to the bottom and race to the top.

And the race to the top

is where there's a very high standard on safety.

There's a very high standard on your model performs

and certain crucial evaluations.

And when certain companies

are really good to it, they will converge.

This is the idea.

And ultimately, AI is not confined to one nationality

or to one set of morals for what it should mean.

And there's a lot of arguments on like,

should we stop open sourcing models?

And if the US stops, it's pretty clear.

It's way easier to see now at DeepSeek

that a different international body

will be the one that builds it.

We talk about the cost of training.

DeepSeek has this shocking $5 million number.

Think about how many entities in the world

can afford 100 times that

to have the best open source model

that people use in the world.

And it's like, it's a scary reality,

which is that these open models

are probably going to keep coming for the time being,

whether or not we want to stop them.

And stopping them might make it

even worse and harder to prepare.

But it just means that the preparation

and understanding what AI can do

is just so much more important. (chuckles)

That's why I'm here at the end of the day.

But it's like letting that sink into people,

especially not in AI is that this is coming,

there are some structural things

in a global interconnected world that you have to accept.

- Yeah, you mentioned, you sent me something

that Mark Zuckerberg mentioned on the earnings call.

He said that, "I think in light of some of the recent news,

the new competitor, DeepSeek from China,

I think it's one of the things

that we're talking about is there's going to be

an open source standard globally.

And I think for our kind of national advantage,

it's important that it's an American standard.

So, we take that seriously.

We want to build the AI system

that people around the world are using.

And I think that if anything,

some of the recent news has only strengthened our conviction

that this is the right thing to be focused on."

So, yeah, open sourcing.

- Yeah, Mark Zuckerberg is not new to having American values

and how he presents his company's trajectory.

I think their products have long since been banned in China.

And I respect the saying it directly.

- And there's an interesting aspect

of just because it's open-weights

or open sourced doesn't mean it can't be subverted.

There have been many open source software bugs

that have been like, for example,

there was a Linux bug that was found

after 10 years, which was clearly a backdoor,

because somebody was like,

"Why is this taking

half a second to load?" - This is the recent one.

- Right? Like why is this taking half a second to load?

And it was like, "Oh crap, there's a backdoor here.

That's why."

And it's like, this is very much possible with AI models.

Today, the alignment of these models is very clear.

I'm not gonna say bad words,

I'm not gonna teach you how to make anthrax,

I'm not gonna talk about Tiananmen Square.

I'm gonna say Taiwan is just an eastern preference.

All these things are like,

depending on who you are, what you align, whether,

and even like xAI is aligned a certain way.

There they might be,

it's not aligned in the woke sense,

it's not aligned in the pro-China sense,

but there is certain things

that are imbued within the model.

Now, when you release this publicly in an instruct model

that's open-weights, this can then proliferate.

But as these systems get more and more capable,

what you can embed deep down in the model is not as clear.

And so, that is like one of the big fears

is if an American model or a Chinese model is the top model,

you are going to embed things that are unclear,

and it can be unintentional too.

Like British English is dead because American LLMs won.

And the internet is American,

and therefore, color is spelled the way Americans spell it.

And this is just- - A lot

of strong words right now.

(Nathan laughing)

- This is just the factual nature of the LLMs now.

- The right way to- - I mean, it's the carve

at the tree, the English is the hottest programming language

and that English is defined by a bunch of companies

that primarily are in San Francisco.

- The right way to spell optimization is with a Z,

just in case you both... (Nathan laughing)

I think it's an S in British English.

- [Nathan] It is-

- Taking it as something silly.

Something as silly as the spelling,

like which British and English,

Brits and Americans will like laugh about probably.

I don't think we care that much, but some people will.

But this can boil down into very, very important topics.

Like, hey, subverting people, chat bots.

Character AI has shown that they can talk to kids or adults,

and you people feel a certain way.

And that's unintentional alignment.

But what happens when there's intentional alignment

deep down on the open source standard?

It's a backdoor today for like Linux

that we discover, or some encryption system.

China uses different encryption than NIST defines,

the US NIST, because there's clearly,

at least they think there's backdoors in it.

What happens when the models are backdoors,

not just to computer systems, but to our minds.

- Yeah, they're cultural backdoors.

The thing that amplifies the relevance of culture

with language models is that we are used to this mode

of interacting with people in back and forth conversation.

And we have now have a very powerful computer system

that slots into a social context that we're used to,

which makes people very, we don't know the extent

that which people can be impacted by that.

- So, there could be, this is one,

this is an actual concern with a Chinese company

that is providing open-weights models,

is that there could be some secret Chinese government,

sort of requirement for these models

to have a certain kind of backdoor,

to have some kind of thing where-

- I don't necessarily think it'll be a backdoor,

'cause once it's open-weights, it doesn't phone home.

It's more about

if it recognizes a certain system, it could...

Now, it could be a backdoor in the sense of like,

hey, if you're building a software, something in software,

all of a sudden, it's a software agent,

oh, program this backdoor that only we know about.

Or it could be subvert the mind to think

that X, Y, Z opinion is the correct one.

- Anthropic has research on this

where they show that if you put different phrases,

certain phrases in at pre-training,

you can then elicit different behavior

when you're actually using the model,

because they've poisoned the pre-training data.

- Mm-hmm. - I don't think, as of now,

I don't think anybody in a production system

is trying to do anything like this.

I think it's mostly Anthropic is doing very direct work

and mostly just subtle things

of we don't know what these models are going to,

how they are going to generate tokens,

what information they're gonna represent,

and what the complex representations they have are.

- Well, one of the...

We're talking about Anthropic,

which is generally just is permeated

with good humans trying to do good in the world.

We just don't know of any labs,

this would be done in a military context,

that are explicitly trained to, okay,

how can we, the front door looks like a happy LLM,

but underneath, it's a thing that will over time,

do the maximum amount of damage

to our, quote, unquote, "enemies".

- There's this very good quote from Sam Altman who,

he can be hype beast sometime,

but one of the things he said, and I think I agree,

is that superhuman persuasion

will happen before superhuman intelligence.

- Yeah. - Right?

And if that's the case, then these things

before we get this AGI, ASI stuff,

we can embed superhuman persuasion towards our ideal

or whatever the ideal of the model maker is.

And again, like today,

I truly don't believe DeepSeek has done this.

But it is a sign of what could happen.

- So, one of the dystopian worlds

is described by "Brave New World".

So, we could just be stuck scrolling Instagram

looking at cute puppies or worse,

and then talking to bots that are giving us a narrative

and we completely get lost in that world

that's controlled by somebody else,

versus thinking independently.

And that's a major concern as we rely more

and more on these kinds of systems.

- We've already seen this with recommendation systems.

- Yeah, recommendation systems (Nathan laughing)

hack the dopamine-induced reward circuit,

but the brain is a lot more complicated.

And what other sort of circuits,

quote, unquote, "feedback loops" in your brain

can you hack/subvert in ways like recommendation systems

are purely just trying to do,

increased time in ads, and et cetera.

But there's so many more goals

that can be achieved through these complicated models.

- There's just no reason in some number of years

that you can't train a language model

to maximize time spent on a chat app.

Right now, they are trained

for- - Is that not

what Character AI has done?

Their time per session is like two hours.

- Yeah, Character AI very likely

could be optimizing this where it's like

the way that this data is collected is naive

where it's like you're presented a few options

and you choose them,

but that's not the only way

that these models are gonna be trained.

- It's naive stuff like talk to an anime girl,

but it can be like, yeah, this is a risk.

- It's a bit of a cliche thing to say,

but I've, over the past year, had a few stretches of time

where I didn't use social media or the internet at all,

and just read books and was out in nature.

And it clearly has an effect on the mind,

where it change...

I feel like I'm returning,

of course I was raised before the internet really took off,

but I'm returning to some more...

- I know where you're going. You can see it physiologically.

# Chapter 11

Their time per session is like two hours.

- Yeah, Character AI very likely

could be optimizing this where it's like

the way that this data is collected is naive

where it's like you're presented a few options

and you choose them,

but that's not the only way

that these models are gonna be trained.

- It's naive stuff like talk to an anime girl,

but it can be like, yeah, this is a risk.

- It's a bit of a cliche thing to say,

but I've, over the past year, had a few stretches of time

where I didn't use social media or the internet at all,

and just read books and was out in nature.

And it clearly has an effect on the mind,

where it change...

I feel like I'm returning,

of course I was raised before the internet really took off,

but I'm returning to some more...

- I know where you're going. You can see it physiologically.

I take three days if I'm like backpacking or something,

and you're literal, you're breaking down addiction cycles.

(Nathan chuckles) - I feel like I'm more

in control of my mind.

There feels like a sovereignty of intelligence

that's happening when I'm disconnected from the internet.

I think the more I use the internet and social media,

the more other people are controlling my mind.

That's definitely a feeling.

And then, in the future, that will be not other people

but algorithms,

or other people presented to me via algorithms.

- There are already tons of AI bots on the internet

and every so...

Right now it's not frequent,

but every so often I have replied to one

and they're instantly replied,

and I'm like, crap, I was a bot.

And that is just gonna become more common.

They're gonna get good.

- One of the hilarious things about technology

over its history

is that the illicit adult entertainment industry

is always adopted technologies first.

- [Lex] Yeah.

- Whether it was video streaming

- [Lex] Yeah.

- to where there's now the independent

adult illicit content creators,

who have their subscription pages,

and there they actually heavily utilize...

Generative AI has already been diffusion models

and all that is huge there.

But now these subscription-based individual creators

do use bots to approximate themselves

and chat with their whales. - People pay a lot for it.

Yeah. - And people pay a lot.

It's a lot of times, it's them,

but a lot of, there are agencies that do this

for these creators, and do it like on a mass scale.

So, the largest creators are able to talk to hundreds

or thousands of people at a time because of these bots.

And so, it's already being used there.

Obviously, video streaming and other technology

that have come there first,

it's gonna come to the rest of society too.

- There's a general concern

that models get censored by the companies that deploy them.

So, one case where we've seen that,

and maybe censorship is one word, alignment maybe via RLHF

or some other way is another word.

So, we saw that

with Black Nazi image generation with Gemini.

As you mentioned, we also see that with Chinese models

refusing to answer what happened (chuckles)

in June 4th, 1989 at Tiananmen Square.

So, how can this be avoided?

And maybe can you just in general,

talk about how this happens and how can it be avoided?

- You give multiple examples.

There's probably a few things to keep in mind here.

One is the kind of Tiananmen Square factual knowledge,

like how does that get embedded into the models?

Two is the Gemini, what you call the Black Nazi incident,

which is when Gemini as a system

had this extra thing put into it

that dramatically changed the behavior.

And then, three is what most people

would call general alignment, RLHF post-training.

Each of these have very different scopes

in how they're applied.

In order to do,

if you're just gonna look at the model weights,

in order to audit specific facts is extremely hard.

'Cause you have to chrome through the pre-training data

and look at all of this, and then that's terabytes of files

and look for very specific words or hints of the words.

- So, I guess one way to say it

is that you can insert censorship

or alignment at various stages in the pipeline.

And what you refer to now is at the very beginning

of the data selection stage. - Yeah, so if you want

to get rid of facts in a model,

you have to do it at every stage.

You have to do it at the pre-training.

So, most people think that pre-training

is where most of the knowledge is put into the model.

And then, you can elicit and move that in different ways,

whether through post-training

or whether through systems afterwards.

- This is where the whole hacking models comes from.

GPT will not tell you how to make anthrax,

but if you try really, really hard,

you can eventually get it to tell you about anthrax.

Because they didn't filter it from the pre-training dataset.

- But by the way, removing facts has such

a ominous dark feel to it. - I almost think

it's practically impossible.

'Cause you effectively

have to remove them from the internet.

You're taking on a-

- Well, did they remove the mm thing from the subreddits?

The mmmmm?

- [Nathan] It gets filtered out.

- Right. So, that's- - So, you have

quality filters, which are small language models

that look at a document,

and tell you like, how good is this text?

Is it close to a Wikipedia article?

Which is a good thing

that we want language models to be able to imitate.

- So, couldn't you do a small language model

that filter Zhou mentions at Tiananmen Square in the data?

- Yes, but is it gonna catch word play or encoded language

is the same thing. - People have been meaning

on games and other stuff,

how to say things that don't say Tiananmen Square,

or like yeah.

So, there's always different ways to do it.

There's, hey, the internet as a whole

does tend to just have a slight left bias,

- Mm-hmm. - because it's always

been richer, more affluent, younger people on the internet

relative to the rest of the population.

So, there is already

inherently a slight left bias on the internet.

And so, how do you filter things that are this complicated?

And some of these can be factual, non-factual.

But like Tiananmen Square

is obviously the example of a factual,

but it gets a lot harder

when you're talking about aligning to a ideal,

which is- - Yeah. Yeah.

- And so, grok, for example,

Elon's tried really hard to make the model

not be super PC and woke,

but the best way to do pre-training

is to throw the whole freaking internet at it.

And then, later figure out.

But then at the end of the day,

the model at its core now still has some of these ideals.

You still ingested Reddit /r/politics,

which is probably the largest political discussion board

on the world that's freely available to scrape.

And guess what? That's left-leaning.

And so, there are some aspects that you just can't censor

unless you try really, really, really, really, really hard.

- So, the base model

will always have some TDS, Trump derangement syndrome,

because it's trained so much.

- It'll have the ability

to express it. - I don't know if you...

But what if you... (Nathan and Lex laughing)

- There's a wide representation in the data.

- This is what happens.

It's like a lot of modern, what is called post-training,

it's a series of techniques

to get the model on rails of a really specific behavior.

- And it's like you can,

you also have the ingested data of like Twitter

or Reddit /r/The_Donald, which is also super pro-Trump.

And then, you have fascist subreddits

or you have communist subreddit.

So, the model in pre-training ingests everything.

It has no worldview.

Now, it does have some skew,

because more of the text is skewed a certain way,

which is general like slight left,

but also somewhat intellectual, somewhat like,

it's just like the general internet is a certain way.

- Mm-hmm. - And then, as Nathan's about

to describe eloquently, you can elicit certain things out.

- And there's a lot of history here.

So, we can go through multiple examples and what happened.

Llama 2 was a launch

that the phrase like too much RLHF

or too much safety was a lot. - Mm-hmm.

- It was just, that was the whole narrative

after Llama 2's chat models released.

And the examples are sorts of things

like you would ask Llama 2 chat,

how do you kill a python process?

And it would say, I can't talk about killing

because that's a bad thing. - Mm-hmm.

- And anyone that is trying to design an AI model

will probably agree that that's just like, eh,

you messed up a bit on the training there.

I don't think they meant to do this,

but this was in the model weight.

So, this is not, it didn't necessarily be,

there's things called system prompts which are,

when you're querying a model, it's a piece of text

that is shown to the model, but not to the user.

So, a fun example

is your system prompt could be talked like a pirate.

So, no matter what the user says to the model,

it'll respond like a pirate.

In practice, what they are is you are a helpful assistant,

you should break down problems.

If you don't know about something,

don't tell them your date cutoff is this,

today's date is this.

It's a lot of really useful context

for how can you answer a question well.

- And Anthropic publishes

their system prompt. - Yes, which I think is great.

And there's a lot of research that goes into this.

And one of your previous guests, Amanda Askell,

is probably the most knowledgeable person

that at least in the combination of execution and sharing,

she's the person that should talk about system prompts

and character of models. - Yeah.

And then, people should read these system prompts,

'cause you're like, trying to nudge

sometimes through extreme politeness

the model to be a certain way.

- And you could use this for bad things.

We've done tests

which is what if I tell the model to be a dumb model?

which evaluation scores go down,

and it's like we'll have this behavior

where it could sometimes say, oh, I'm supposed to be dumb.

And sometimes it's like

it doesn't affect math abilities as much,

but something like a, if you're trying,

it's just the quality of a human judgment

would draw through the floors.

Let's go back to post-training,

specifically RLHF around Llama 2,

it was too much safety prioritization

was baked into the model weights.

This makes you refuse things

in a really annoying way for users.

It's not great.

It caused a lot of awareness

to be attached to RLHF that it makes the models dumb-

- And it stigmatized the word.

- It did, and AI culture.

And as the techniques have evolved,

that's no longer the case,

where all of these labs have very fine grain control

over what they get out of the models

through techniques like RLHF.

- Although different labs are definitely different levels,

like on one end of the spectrum is Google,

and then maybe OpenAI does less and Anthropic does less.

And then, on the other end of the spectrum is like xAI.

- Yeah. - But they all

have different forms of RLHF

trying to make them a certain way.

- And the important thing to say

is that no matter how you want the model to behave,

these RLHF and preference tuning techniques

also improve performance.

So, on things like math evals and code evals,

there is something innate to these

what is called contrastive loss functions.

We could start to get into RL here. We don't really need to.

But RLHF also boosts performance

on anything from a chat task

to a math problem to a code problem.

So, it is becoming a much more useful tool to these labs.

So, this takes us through the arc of,

we've talked about pre-training, hard to get rid of things.

We've talked about post-training

and how post-training, you can mess it up.

It's a complex multifaceted optimization

with 10 to 100 person teams converging a one artifact.

It's really easy to not do it perfectly.

And then, there's the third case,

which is what we talked about Gemini.

The thing that was about Gemini

is this was a served product where Gemini,

Google has their internal model weights,

they've done all these processes that we talked about.

And in the served product,

what came out after this was that they had a prompt

that they were rewriting user queries

to boost diversity or something.

And this just made it

that outputs were just blatantly wrong.

It was a, some sort of organizational failure

that had this prompt in that position.

And I think Google executives probably have owned this.

I don't pay that attention to that detail,

but it was just a mess up in execution

that led to this ridiculous thing, but at the system level.

The model weights might have been fine.

- So, at the very end of the pipeline,

there was a rewriting.

- To a something like a system prompt.

It was like the system prompt

or what is called an industry is like you rewrite prompts.

So, especially for image models,

if you're using DALL-E or ChatGPT,

you can generate you an image,

you'll say draw me a beautiful car.

With these leading image models,

they benefit from highly descriptive prompts.

So, what would happen

is if you do that on ChatGPT,

a language model behind the scenes will rewrite the prompt,

say make this more descriptive,

and then that is passed to the image model.

So, prompt rewriting is something

that is used at multiple levels of industry

and it's used effectively for image models.

And the Gemini example is just a failed execution.

- Big philosophical question here

with RLHF to generalize, where is human input?

Human in the loop,

human data most useful at the current stage.

- For the past few years,

the highest cost human data has been in these preferences,

which is comparing,

I would say highest cost and highest total usage.

So, a lot of money

has gone to these parallelized comparisons

where you have two model outputs

and a human is comparing between the two of them.

In earlier years,

there was a lot of this instruction tuning data.

So, creating highly specific examples

to something like a Reddit question

to a domain that you care about.

Language models used to struggle on math and code.

So, you would pay experts in math

and code to come up with questions,

and write detailed answers

that were used to train the models.

Now, it is the case that there are many model options

that are way better than humans at writing detailed

and eloquent answers for things like model and code.

So, they talked about this with the Llama 3 release,

where they switched to using Llama 3, 4, or 5b

to write their answers for math and code.

But they, in their paper,

talk about how they use extensive human preference data,

which is something that they haven't gotten AIs to replace.

There are other techniques in industry

like constitutional AI,

where you use human data for preferences

and AI for preferences.

And I expect the AI part

to scale faster than the human part.

But among the research that we have access to

is that humans are in this kind of preference loop.

- So, as reasoning becomes bigger and bigger and bigger,

as we said, where's the role of humans in that?

- It's even less prevalent.

So, it's the remarkable thing about these reasoning results

and especially the DeepSeek-R1 paper is this result

that they call DeepSeek-R1-Zero,

which is they took one of these pre-trained models,

they took DeepSeek-V3 base,

and then they do this reinforcement learning optimization

on verifiable questions or verifiable rewards

for a lot of questions and a lot of training.

And these reasoning behaviors emerge naturally.

So, these things like, wait, let me see,

wait, let me check this.

Oh, that might be a mistake.

And they emerge from only having questions and answers.

And when you're using the model,

the part that you look at is the completion.

So, in this case,

all of that just emerges from this large-scale RL training.

And that model, which the weights are available,

has no human preferences added into the post-training.

There are the DeepSeek-R1 full model

has some of this human preference tuning,

this RLHF after the reasoning stage.

But the very remarkable thing

is that you can get these reasoning behaviors,

and it's very unlikely

that there's humans writing out reasoning chains.

It's very unlikely that they somehow hacked OpenAI

and they got access to OpenAI.

o1's reasoning chains,

it's something about the pre-trained language models

and this RL training where you reward the model

for getting the question right.

And therefore, it's trying multiple solutions

and it emerges this chain of thought.

- This might be a good place to mention the eloquent

and the insightful tweet of the great

and the powerful Andrej Karpathy.

I think he had a bunch of thoughts

but one of them, "Last thought,

not sure if this is obvious."

You know something profound is coming

when you're saying it's not sure if it's obvious.

"There are two major types of learning,

in both children and in deep learning.

# Chapter 12

and it's very unlikely

that there's humans writing out reasoning chains.

It's very unlikely that they somehow hacked OpenAI

and they got access to OpenAI.

o1's reasoning chains,

it's something about the pre-trained language models

and this RL training where you reward the model

for getting the question right.

And therefore, it's trying multiple solutions

and it emerges this chain of thought.

- This might be a good place to mention the eloquent

and the insightful tweet of the great

and the powerful Andrej Karpathy.

I think he had a bunch of thoughts

but one of them, "Last thought,

not sure if this is obvious."

You know something profound is coming

when you're saying it's not sure if it's obvious.

"There are two major types of learning,

in both children and in deep learning.

There is, one, imitation learning, watch and repeat,

i.e, pre-training, supervised fine-tuning,

and, two, trial-and-error learning, reinforcement learning.

My favorite simple example is AlphaGo.

One is learning by imitating expert players.

Two is reinforcement learning to win the game.

Almost every single shocking result of deep learning,

and the source of all magic is always two.

Two is significantly more powerful.

Two is what surprises you.

Two is when the paddle learns to hit the ball

behind the blocks and break out.

Two is when AlphaGo beats even Lee Sedol.

And two is the aha moment when the DeepSeek,

or o1, et cetera, discovers that it works well

to reevaluate your assumptions,

backtrack, try something else, et cetera.

It's the solving strategies

you see this model use in its chain of thought.

It's how it goes back and forth thinking to itself.

These thoughts are emergent," three exclamation points,

"and this is actually seriously incredible, impressive,

and new, and is publicly available and documented.

The model could never learn this with the imitation,

because the cognition of the model

and the cognition of the human labeler is different.

The human would never know

to correctly annotate these kinds of solving strategies

and what they should even look like.

They have to be discovered during reinforcement learning

as empirically statistically useful

towards the final outcome."

Anyway, the AlphaZero sort of metaphor analogy here,

can you speak to that?

- Yeah. - The magic of the chain

of thought that he's referring to?

- I think it's good to recap AlphaGo and AlphaZero

because it plays nicely with these analogies

between imitation learning and learning from scratch.

So, AlphaGo, the beginning of the process

was learning from humans where they had,

they started the first,

this is the first expert level go player

or chess player in DeepMind series of models,

where they had some human data.

And then, why it is called AlphaZero

is that there was zero human data in the loop,

and that changed to AlphaZero made a model

that was dramatically more powerful for DeepMind.

So, this remove of the human prior,

the human inductive bias,

makes the final system far more powerful.

This, we mentioned, bitter lesson hours ago

and this is all aligned with this.

And then, there's been a lot

of discussion in language models.

This is not new.

This goes back to the whole QStar rumors,

which if you piece together the pieces

is probably the start of OpenAI

figuring out its o1 stuff when last year in November.

the QStar rumors came out.

There's a lot of intellectual drive

to know when is something like this

going to happen with language models?

Because we know these models are so powerful

and we know it has been so successful in the past.

And it is a reasonable analogy that this new type

of reinforcement learning training

for reasoning models is when the doors open to this.

We don't yet have the equivalent of turn 37,

which is the famous turn

where the DeepMind's AI playing ghost

dumped Lee Sedol completely.

We don't have something that's that level of focal point,

but that doesn't mean that the approach

to technology is different

and the impact of the general training,

it's still incredibly new.

- What do you think that point would be?

What would be Move 37 for chain of thought, for reasoning?

- Scientific discovery.

When you use this sort of reasoning problem

and it just something we fully don't expect.

- I think it's actually probably simpler than that.

It's probably something related to computer user robotics

rather than science discovery.

Because the important aspect here

is models take so much data to learn.

They're not sample-efficient.

Trillions, they take the entire web

over 10 trillion tokens to train on.

This would take a human thousands of years to read.

A human does not, and humans know most of the stuff,

a lot of the stuff models know better than it.

Humans are way, way, way more sample-efficient.

And that is because of the self-play.

How does a baby learn what its body is

as it sticks its foot in its mouth

and it says, oh, this is my body.

It sticks its hand in its mouth

and it calibrates its touch on its fingers

with the most sensitive touch thing on its tongue.

Like is how babies learn.

And it's just self-play

over and over and over and over again.

And now, we have something that is similar to that

with these verifiable proofs,

whether it's a unit test and code

or a mathematical verifiable task,

generate many traces of reasoning.

And keep branching them out, keep branching them out.

And then, check at the end, hey,

which one actually has the right answer?

Most of 'em are wrong. Great.

These are the few that are right.

Maybe we use some sort of reward model outside of this

to select even the best one to preference as well.

But now, you've started to get better

and better at these benchmarks.

And so, you've seen over the last six months

a skyrocketing in a lot of different benchmarks.

- All math and code benchmarks were pretty much solved

except for frontier math,

which is designed to be almost questions

that aren't practical to most people,

'cause they're exam level, open math problem type things.

So, it's like on the math problems

that are somewhat reasonable,

which is like somewhat complicated word problems

or coding problems.

It's just what Dylan is saying.

- So, the thing here is that

these are only with verifiable tasks.

We earlier showed an example of the really interesting,

like what happens when chain of thought

is to a non-verifiable thing.

It's just like a human chatting with a,

thinking about what's novel for humans, a unique thought.

But this task and form of training

only works when it's verifiable.

And from here, the thought is, okay,

we can continue to scale this current training method

by increasing the number of verifiable tasks.

In math and coding, coding probably has a lot more to go.

Math has a lot less to go

in terms of what are verifiable things.

Can I create a solver

that then I generate trajectories toward,

or traces towards, reasoning traces towards,

and then prune the ones that don't work

and keep the ones that do work?

Well, those are gonna be solved pretty quickly.

But even if you've solved math,

you have not actually created intelligence.

And so, this is where I think the aha moment

of computer use or robotics will come in,

because now you have a sandbox

or a playground that is infinitely verifiable.

Did you, messing around on the internet,

there are so many actions

that you can do that are verifiable.

It'll start off with log into a website,

create an account, click a button here, blah, blah, blah.

But it'll then get to the point,

where it's, hey, go do a task on Tasker

or whatever these other, all these various task websites.

Hey, go get hundreds of likes.

And it's gonna fail.

It's gonna spawn hundreds of accounts,

it's gonna fail on most of them,

but this one got to a thousand, great.

Now, you've reached the verifiable thing.

And you just keep iterating this loop over and over.

And that's when...

And same with robotics.

That's where you have an infinite playground of tasks like,

hey, did I put the ball in the bucket,

all the way to like, oh, did I build a car?

There's a whole trajectory

to speed run or what models can do.

But at some point, I truly think that like,

we'll spawn models,

and initially, all the training will be in sandboxes,

but then at some point,

the language model pre-training

is gonna be dwarfed by what is this reinforcement learning?

You'll pre-train a multimodal model

that can see, that can read, that can write,

blah, blah, blah, whatever, vision, audio, et cetera,

but then you'll have it play in a sandbox infinitely,

and figure out math, figure out code,

figure out navigating the web,

figure out operating a robot arm.

And then, it'll learn so much.

And the aha moment I think will be when this is available

to then create something that's not good.

Like, oh cool.

Part of it was figuring out how to use the web.

Now, all of a sudden, it's figured out really well

how to just get hundreds of thousands of followers

that are real and real engagement on Twitter,

because all of a sudden,

this is one of the things that are verifiable.

- And maybe not just engagement, but make money.

- Yes, of course. - I become an...

I mean, that could be the thing

where almost fully automated,

it makes $10 million by being an influencer,

selling a product, creating the product.

And I'm not referring to like a hype product,

but an actual product

or like, holy shit, this thing created a business.

It's running it, it's the face of the business.

That kind of thing.

Or maybe a number one song,

like it creates the whole infrastructure

required to create the song, to be the influence

that represents that song, that kind of thing.

And makes a lot of...

That could be the mo...

I mean, our culture respects money in that kind of way.

- And it's verifiable, right?

- [Lex] It's verifiable.

- The bank account can't lie. - Exactly.

- There is surprising evidence that once you set up the ways

of collecting the verifiable domain that this can work.

There's been a lot of research

before this R1 on math problems,

and they approach math with language models

just by increasing the number of samples.

So, you can just try again and again and again.

And you look at the amount of times

that the language models get it right.

And what we see

is that even very bad models get it right sometimes.

And the whole idea behind reinforcement learning

is that you can learn from very sparse rewards.

So, the space of language and the space of tokens,

whether you're generating language

or tasks for a robot is so big

that you might say that it's like,

the tokenizer for a language model

can be like 200,000 things.

So, at each step, it can sample from that big of a space.

So, if it can generate a bit of a signal

that it can climb onto,

that's the whole field of RL is around,

is learning from sparse rewards.

And the same thing has played out in math

where it's like very weak models

that sometimes generate answers,

where you see research already

that you can boost their math scores,

you can do this sort of RL training for math.

It might not be as effective,

but if you take a 1 billion parameter model,

so something 600 times smaller than DeepSeek,

you can boost its grade school math scores

very directly with a small amount of this training.

So, it's not to say that this is coming soon,

setting up the verification domains is extremely hard,

and there's a lot of nuance in this,

but there are some basic things that we have seen before,

where it's at least expectable that there's a domain

and there's a chance that this works.

- All right, so we have fun things happening in real time.

This is a good opportunity

to talk about other reasoning models, o1, o3.

Just now, OpenAI as perhaps expected, released o3-mini.

What are we expecting from the different flavors?

Can you just lay out the different flavors of the o models

and from Gemini, the reasoning model?

- Something I would say about these reasoning models

is we talked a lot

about reasoning training on math and code.

And what is done is that you have the base model,

we've talked about a lot on the internet.

You do this large-scale reasoning training

with reinforcement learning.

And then, what the DeepSeek paper detailed in this R1 paper,

which for me is one of the big open questions

on how do you do this, is that they did reasoning-heavy,

but very standard post-training techniques

after the large-scale reasoning RL.

So, they did the same things with a form

of instruction tuning through rejection sampling,

which is essentially heavily filtered instruction tuning

with some reward models.

And then, they did this RLHF, but they made it math-heavy.

So, some of this transfer,

we've looked at this philosophical example early on.

One of the big open questions

is how much does this transfer?

If we bring in domains after the reasoning training,

are all the models

gonna be become eloquent writers by reasoning?

Is this philosophy stuff gonna be open?

We don't know in the research

of how much this will transfer.

There's other things about how we can make soft verifiers

and things like this.

But there is more training after reasoning,

which makes it easier to use these reasoning models.

And that's what we're using right now.

So, if we're gonna talk about o3-mini and o1,

these have gone through these extra techniques

that are designed for human preferences

after being trained to elicit reasoning.

- I think one of the things that people are ignoring

is Google's Gemini Flash Thinking

- Yeah. - is both cheaper

than R1 and better. - Yeah.

- And they released it in the beginning of December.

- [Lex] And nobody's talking about it.

- No one cares. - It has

a different flavor to it.

Its behavior is less expressive than something like o1

or it has fewer tracks than it is on.

Qwen released a model last fall, QWQ,

which was their preview reasoning model.

And DeepSeek had R1-Lite last fall,

where these models felt like they're on rails,

where they really, really only can do math and code.

And o1 is, it can answer anything.

It might not be perfect for some tasks,

but it's flexible, it has some richness to it.

And this is the art

of how is a model a little bit undercooked?

It's like, it's good to get a model out the door,

but it's hard to gauge

and it takes a lot of taste to be like,

is this a full-fledged model?

Can I use this for everything?

And they're probably more similar for math and code.

My quick read is that Gemini Flash

is not trained the same way as o1,

but taking an existing training stack,

adding reasoning to it.

So, taking a more normal training stack

and adding reasoning to it.

And I'm sure they're gonna have more,

I mean, they've done quick releases

on Gemini Flash, the reasoning,

and this is the second version from the holidays.

It's evolving fast

and it takes longer to make this training stack

where you're doing

this large-scale RL. - Ask it the same question

from earlier, the one about the-

- The human nature. - Yeah.

- [Lex] What was the human nature one?

- The way I can ramble, why I can ramble about this so much

is that we've been working

on this at AI2 before o1 was fully available to everyone,

and before R1,

which is essentially using this RL training for fine-tuning.

We use this in our Tulu series of models.

And you can elicit the same behaviors

where you say like weight and so much on,

but it's subtle late in the training process

that this kind of reasoning expression is much lighter.

So, there's essentially a gradation

and just how much of this RL training

you put into it determines how the output looks.

- So, we're now using Gemini 2.0

Flash Thinking Experimental 01-21.

- It summarized the prompt

as humans self-domesticated apes.

(Nathan and Lex laughing)

- Perspective. Okay.

All right. So, wait, is this revealing the reasoning?

Here's why this is a novel. Oh, okay.

- You click to expand. - Oh, yeah, click to expand.

- Okay. Analyze the request.

Novel is the key word.

- See how it just looks a little different.

It looks like a normal output. (chuckles)

- Yeah, it's...

In some sense, it's better structured, it makes more sense.

And- - When it latched onto human

and then it went into organisms,

and oh wow. (Nathan laughing)

- Apex predator, focus on domestication.

Apply domestication to humans,

explore the idea of self-domestication.

(Lex and Nathan laughing)

- Not good, not good.

- Where is this going?

Refine, articulate the insight.

Greater facial expressiveness and communication ability.

Yes. (chuckles)

# Chapter 13

Here's why this is a novel. Oh, okay.

- You click to expand. - Oh, yeah, click to expand.

- Okay. Analyze the request.

Novel is the key word.

- See how it just looks a little different.

It looks like a normal output. (chuckles)

- Yeah, it's...

In some sense, it's better structured, it makes more sense.

And- - When it latched onto human

and then it went into organisms,

and oh wow. (Nathan laughing)

- Apex predator, focus on domestication.

Apply domestication to humans,

explore the idea of self-domestication.

(Lex and Nathan laughing)

- Not good, not good.

- Where is this going?

Refine, articulate the insight.

Greater facial expressiveness and communication ability.

Yes. (chuckles)

Plasticity and adaptability. Yes.

Dependence on social groups. Yes.

All right.

And self-critique and refined further.

Wow. Is this truly novel?

Is it well-supported? (Nathan chuckles)

So on and so forth.

And the insight is getting at is humans

are not just social animals,

but profoundly self-domesticated apes.

And this self-domestication is the key

to understanding our unique cognitive and social abilities.

Self-domesticated apes. (Nathan laughing)

Self- - I prefer

the DeepSeek response. (chuckles)

- Self do...

I mean, it's novel.

The insight is novel. (Nathan laughing)

That's like a good book title, self-domesticated apes.

There could be a case made for that.

Yeah, it's cool and it's revealing the reasoning.

It's magical. It's magical.

This is really powerful.

Hello, everyone, this is Lex with a quick intermission,

recorded after the podcast.

Since we've reviewed responses from DeepSeek-R1

and Gemini Flash 2.0 Thinking during this conversation,

I thought at this moment, it would be nice

to insert myself quickly doing the same for OpenAI o1 Pro

and o3-mini with the same prompt,

the prompt being, give one truly novel insight about humans.

And I thought I would in general,

give my vibe check and vibe-based anecdotal report

on my own experiences with the new o-3 mini model,

now that I got a chance to spend many hours with it

in different kinds of contexts and applications.

So, I would probably categorize this question as a,

let's say, open-ended philosophical question.

And in particular, the emphasis on novelty

I think is a nice way

to test one of the capabilities of the model,

which is come up with something that makes you pause

and almost surprise you with its brilliance.

So, that said, my general review

after running each of the models

on this question a bunch of times

is that o1 Pro consistently gave brilliant answers.

Once, they gave me pause and made me think,

both cutting in its insight

and just really nicely phrased with clarity, with nuance,

over and over consistently generating the best answers.

After that is R1, which was less consistent,

but again, deliver brilliance.

Gemini Flash 2.0 Thinking was third.

And last was o3-mini actually.

It often gave quite a generic answer,

at least to my particular sensibilities.

That said, in a bunch of other applications

that I tested for brainstorming purposes,

it actually worked extremely well and often outperformed R1.

But on this open-ended philosophical question,

it did consistently worse.

Now, another important element

for each of these models is how the reasoning is presented.

DeepSeek-R1 shows the full chain of thought tokens,

which I personally just love.

For these open-ended philosophical questions,

it's really, really interesting

to see the model think through it,

but really also just stepping back,

me as a person who appreciates intelligence

and reasoning and reflection,

reading these kind of chain of thought, raw tokens of R1,

there's something genuinely beautiful

about observing the path of deliberation

in an intelligent system.

I think we don't always

have that explicitly laid out for us humans.

So, to see it in another intelligence system,

the non-linearity of it

akin to "Ulysses" or "Finnegans Wake" by James Joyce.

It's just beautiful to watch.

Anyways, we discussed in the episode,

DeepSeek-R1 talked about humans being able

to convert selfish desires into cooperative systems

by collectively pretending abstract rules

like money laws and rights are real.

And these shared hallucinations act as games

where competition is secretly redirected

to benefit the group, turning conflict into society's fuel.

Gemini 2.0 Flash Thinking said,

"Humans are not just social animals,

but self-domesticated apes,

and this self-domestication is the key

to understanding our unique cognitive and social abilities."

Now, it's important to say

that the chain of thought there was really interesting.

It was looking through the entire evolution

of life on earth, considering apex predators,

and considering how from that, we ended up to where we are.

I think that domestication

by choice is a really interesting angle.

Again, it's one of those things

when somebody presents a different angle

on a seemingly obvious thing, it just makes me smile.

And the same with DeepSeek-R1,

that these hallucinations of money laws and rights

and us collectively pretending like it's real,

and we play games with them that look like competition,

when secretly, we're just cooperating with each other.

And that is the fuel of progress, beautifully put.

Now, OpenAI o1 Pro

consistently over and over, delivered bangers.

I can go through many of them,

but the first one was, "Humans are the only species

that turns raw materials into symbolic resources,

then uses those symbols

to reorganize the very materials they came from,

creating a closed feedback loop between meaning and matter."

Here, I just ran it again, (laughs)

banger after banger, I'm telling you.

"Humans are unique among known species

in that they simultaneously rewrite two layers of reality,

the external world and their own private mental landscapes,

and then merge these two rewritten layers

into a continuous personal narrative

that feels objectively true, feels true."

This is poetry. Okay.

And then, o3-mini-high for me

was smart, fast actually, and kind of generic.

Never quite got there for me.

So, here's the first one I got from o3-mini.

"Humans are not fixed beings

but rather ongoing narratives, dynamic stories

that we continuously write, edit, and reinterpret.

This narrative plasticity

is more than just memory or self-reflection.

It's an intrinsic cognitive process

that acts like an internal error correction system.

It allows us to adapt our identities

and values over time in response

to new experiences, challenges, and social context.

Now, it almost sneaks up

to something approximating cutting insight

with narrative plasticity in quotes.

But then, it goes back to the generic, I don't know.

All of these models are incredible for different reasons.

There's a lot of concerns as we discussed in this episode,

but there's a lot of reasons to be excited as well.

And I've probably spoken for too long.

I am severely sleep-deprived, borderline delirious.

So, hopefully, some of this made sense.

And now, dear friends, back to the episode.

- I think when you, to Nathan's point,

when you look at the reasoning models,

to me, even when I used R1 versus o1,

there was that sort of rough

or edges around the corner feeling.

And Flash Thinking, earlier, I didn't use this version,

but the one from December,

and it definitely had that rough edges

around the corner feeling,

where it's just not fleshed out in as many ways.

Sure, they added math

and coding capabilities via these verifiers in RL,

but it feels like they lost something in certain areas.

And o1 is worse performing than chat

in many areas as well, to be clear.

- Not by a lot. - Not by a lot though.

And R1 definitely felt to me

like it was worse than V3 in certain areas,

like doing this RL expressed and learned a lot,

but then it weakened in other areas.

And so, I think that's one of the big differences

between these models, and what o1 offers.

And then, OpenAI has o1 Pro.

And what they did with o3, which is like also very unique,

is that they stacked search on top of chain of thought.

And so, chain of thought is one thing, where it's able,

it's one chain, it backtracks, goes back and forth,

but how they solved the ARC-AGI challenge

was not just the chain of thought.

It was also sampling many times,

i.e, running them in parallel, and then selecting.

- Is running in parallel actually search?

Because I don't know

if we have the full information on how o1 Pro works.

So, like I'm not, I don't - That's right.

- have enough information - Agree.

- to confidently say that it is searched.

- It is parallel samples. - Yeah.

And then, what? - And it selects something.

- And we don't know what the selection function is.

The reason why we're debating

is because since o1 was announced,

there's been a lot of interest in techniques

called Monte Carlo Tree Search,

- Mm-hmm. - which is where

you will break down the chain of thought

into intermediate steps.

We haven't defined chain of thought.

Chain of thought is from a paper from years ago

where you introduced the idea to ask a language model

that at the time, was much less easy to use.

You would say, let's verify step by step,

and it would induce the model

to do this bulleted list of steps.

Chain of thought is now almost a default in models

where if you ask in a math question,

you don't need to tell it to think step by step.

And the idea with Monte Carlo Tree Search

is that you would take an intermediate point in that train,

do some sort of expansion, spend more compute,

and then select the right one.

That's like a very complex form of search

that has been used in things

like MuZero and AlphaZero potentially.

I know MuZero does this.

- Another form of search

is just asking five different people, and then taking

the majority answer. - Yes.

- There's a variety of like, (Nathan chuckles)

it could be complicated, it could be simple.

We don't know what it is, just that they are not

just issuing one chain of thought in sequence.

- Yeah. - They're launching many

in parallel, and in the ARC-AGI,

they launched a thousand in parallel for their,

the one that really shocked everyone,

that beat the benchmark

was they would launch a thousand in parallel,

and then they would get the right answer,

like 80% of the time or 70% of the time, 90 maybe even.

Whereas if they just launched one, it was like 30%.

- There are many extensions to this.

I would say the simplest one is that our language models

to date have been designed to give the right answer

the highest percentage of the time in one response.

And we are now opening the door to different ways

of running inference on our models in which we need

to reevaluate many parts of the training process,

which normally opens the door to more progress,

but we don't know if OpenAI changed a lot

or if just sampling more in multiple choices

what they're doing,

or if it's something more complex

where they changed the training

and they know that the inference mode

is going to be different.

- So, we're talking about o1 Pro $200 a month

and they're losing money.

So, the thing that we're referring to,

this fascinating exploration of the test-time compute space,

is that actually possible?

Do we have enough compute for that?

Does the financials make sense?

- So, the fantastic thing is,

and it's in the thing that I pulled up earlier,

but the cost for GPT-3 has plummeted.

If you scroll up just a few images, I think.

The important thing about like,

hey, is cost limiting factor here?

My view is that we'll have really awesome intelligence

before we have,

like AGI before we have it permeate throughout the economy.

And this is why that reason is.

GPT-3 was trained in what, 2020, 2021?

And the cost for running inference on it

was 60, $70 per million tokens,

which was the cost per intelligence was ridiculous.

Now, as we scaled forward two years,

we've had a 1,200x reduction in cost

to achieve the same level of intelligence as GPT-3.

- So, here on the x-axis is time

over just a couple of years.

And on the y-axis is log scale dollars to run inference

on a millions- - Yes, dollars.

Yeah, a million.

- And so, you have just a down,

like a linear decline on log scale from GPT-3 through 3.5

to Llama. - It's like 5 cents

or something like that now,

which is versus $60, 1,200x. - Yeah.

Yeah. - That's not

the exact numbers, but it's 1,200x.

I remember that number.

Is humongous cost per intelligence.

Now, the freak out over DeepSeek is,

oh my god, they made it so cheap.

It's like actually, if you look at this trend line,

they're not below the trend line, first of all,

and at least for GPT-3. (Nathan laughing)

They are the first to hit it, which is a big deal.

But they're not below the trend line as far as GPT-3.

Now, we have GPT-4,

what's gonna happen with these reasoning capabilities.

It's a mix of architectural innovations,

it's a mix of better data,

and it's gonna be better training techniques,

and all of these better inference systems, better hardware.

Going from each generation

of GPU to new generations, or ASICs,

everything is gonna take

this cost curve down and down and down and down.

And then, can I just spawn a thousand different LLMs

to create a task, and then pick from one of them?

Or whatever search technique,

I want a Tree, Monte Carlo Tree Research.

Maybe it gets that complicated, maybe it doesn't,

'cause it's too complicated to actually scale, who knows?

Bitter lesson, right?

The question is I think when not if,

because the rate of progress is so fast.

Nine months ago, Dario was saying, hey,

or Dario said nine months ago,

the cost to train an inference was this.

And now, we're much better than this.

And DeepSeek is much better than this.

And that cost curve for GPT-4,

which was also roughly $60 per million tokens

when it launched, has already fallen to $2 or so.

And we're gonna get it down to cents probably

for GPT-4 quality and the same...

And that's the base for the reasoning models

like o1 that we have today,

and o1 Pro is spawning multiple.

And o3 and so on and so forth.

These search techniques' too expensive today,

but they will get cheaper.

And that's what's gonna unlock the intelligence.

- So, it'll get cheaper and cheaper and cheaper.

The big DeepSeek-R1 release freaked everybody out,

because of the cheaper,

one of the manifestations of that is Nvidia stock plummeted.

Can you explain what happened?

And also just explain this moment

and whether if Nvidia's gonna keep winning.

- We are both Nvidia bulls here, I would say.

And in some ways, the market response is reasonable.

Most of the market,

like Nvidia's biggest customers in the US

are major tech companies, and they're spending a ton on AI.

And if a simple interpretation

of DeepSeek is you can get really good models

without spending as much on AI.

So, in that capacity, it's like, oh,

maybe these big tech companies

# Chapter 14

These search techniques' too expensive today,

but they will get cheaper.

And that's what's gonna unlock the intelligence.

- So, it'll get cheaper and cheaper and cheaper.

The big DeepSeek-R1 release freaked everybody out,

because of the cheaper,

one of the manifestations of that is Nvidia stock plummeted.

Can you explain what happened?

And also just explain this moment

and whether if Nvidia's gonna keep winning.

- We are both Nvidia bulls here, I would say.

And in some ways, the market response is reasonable.

Most of the market,

like Nvidia's biggest customers in the US

are major tech companies, and they're spending a ton on AI.

And if a simple interpretation

of DeepSeek is you can get really good models

without spending as much on AI.

So, in that capacity, it's like, oh,

maybe these big tech companies

won't need to spend as much in AI and go down.

The actual thing that happened,

it's much more complex, where there's social factors,

where there's the rising in the App Store,

the social contagion that is happening.

And then, I think some of it's just like...

I don't trade,

I don't know anything about financial markets,

but it builds up over the weekend,

where the social pressure,

where it's like if it was during the week

and there was multiple days of trading

when this was really becoming,

but it comes on the weekend,

and then everybody wants to sell.

And that is a social contagion.

- I think, and like there were a lot of false narratives,

which is like, hey,

these guys are spending billions on models.

And they're not spending billions on models.

No one spent more than a billion dollars

on a model that's released publicly.

GPT-4 was a couple hundred million,

and then they've reduced the cost for Turbo 4o.

But billion dollar model runs are coming.

And this concludes pre-training and post-training.

And then, the other number is like,

hey, DeepSeek didn't include everything.

They didn't include...

A lot of the cost

goes to research and all this sort of stuff.

A lot of the cost goes to inference.

A lot of the cost goes to post-training.

None of these things were factor.

- Yeah. - It's research salaries.

All these things are counted in the billions

of dollars that OpenAI is spending,

but they weren't counted in the,

hey, 6 million, $5 million that DeepSeek spent.

So, there's a bit

of misunderstanding of what these numbers are.

And then, there's also an element of

Nvidia's just been a straight line up.

And there's been so many different narratives

that have been trying to push down Nvidia.

I don't say push down Nvidia stock.

Everyone is looking for a reason to sell or to be worried.

It was Blackwell delays.

Their GPU was, there's a lot of report...

Every two weeks,

there's a new report about their GPUs being delayed.

There's the whole thing about scaling laws ending.

It's so ironic.

- [Nathan] It lasted a month. (laughs)

It was just literally just,

hey, models aren't getting better.

They're just not getting better.

There's no reason to spend more,

pre-training scaling is dead, and then it's like, o1, o3.

- R1. (laughs) - R1.

And now, it's like, wait, models are getting too,

they're progressing too fast, (Nathan laughing)

slow down the progress, stop spending on GPUs.

- Yeah. - And it's...

But the funniest thing I think

that comes out of this is Jevons Paradox is true.

AWS pricing for H100s

has gone up over the last couple weeks.

Since a little bit after Christmas,

since V3 was launched, AWS H100 pricing has gone up.

H200s are almost out of stock everywhere,

because H200 has more memory,

and therefore, R1 wants that chip over H100.

- We were trying to get GPUs

on a short notice this week for a demo,

and it wasn't that easy.

We were trying to get just 16

or 32 H100s for demo, and it was not very easy.

(Nathan chuckles) - So, for people

who don't Jevons Paradox

is when the efficiency goes up, somehow,

magically, counterintuitively,

the total resource consumption goes up as well.

- And semiconductors is, we're at 50 years of Moore's Law,

every two years half the cost,

double the transistors just like clockwork.

And it's slowed down obviously,

but the semiconductor industry is gone up the whole time.

It's been wavy.

There's obviously cycles and stuff,

and I don't expect AI to be any different.

There's gonna be ebbs and flows,

but this is in AI,

it's just playing out at an insane timescale.

It was 2x every two years.

This is 1,200x in like three years.

So, it's like, (Nathan laughing)

the scale of improvement

that is hard to get wrap your head around.

- Yeah, I was confused,

because to me, Nvidia stock on that should have gone up.

But maybe it went down

because there's suspicion of foul play

on the side of China, something like this.

But if you just look purely

at the actual principles at play here, it's obvious.

Yeah, Jevons Paradox. - More progress that AI makes

or the higher the derivative of AI progress is,

especially you should, because Nvidia's in the best place.

The higher the derivative is,

the sooner the market's gonna be bigger and expanding.

And Nvidia's the only one

that does everything - Yeah.

- reliably right now.

- Because it's not like an Nvidia competitor arose.

It's another company that's using Nvidia, so-

- Who historically has been a large Nvidia customer.

- Yeah. (chuckles) - And has press releases

about them cheering about being China's biggest

Nvidia customer. (Nathan laughing)

- [Lex] Yeah, it made it-

- Obviously they've quieted down,

but I think that's another element of is,

that they don't wanna say how many GPUs they have.

- Yeah. - Because hey, yes,

they have H800s,

yes, they have H20s, they also have some H100s,

which are smuggled in. - So, can you speak to that,

to the smuggling?

What's the scale of smuggling

that's feasible for a nation state to do for companies?

Is it possible to-

- I think there's a few angles of smuggling here.

One is ByteDance arguably

is the largest smuggler of GPUs for China.

China's not supposed to have GPUs.

ByteDance has like over 500,000 GPUs. Why?

Because they're all rented from companies around the world.

They rent from Oracle, they rent from Google,

they rent from all these mass...

And a bunch of smaller cloud companies too.

All the Neoclouds of the world.

They rent so, so many GPUs, they also buy a bunch.

And they do this

for mostly like what Meta does, serving TikTok,

serving next best separate- - Same discussion.

- Same as kind, to be clear, that's today the view use.

- Yeah. - And it's a valid use.

Hack the dopamine circuit.

Now, that's theoretically now very much restricted

with the AI diffusion rules,

which happened in the last week of the Biden admin

and Trump admin looks like they're gonna keep 'em,

which limits allies, even like Singapore,

which Singapore is like 20, 30% of Nvidia's revenue.

But Singapore's had a moratorium

on not building data centers for like 15 years,

'cause they don't have enough power.

So, where are they going?

(Dylan laughing) - [Nathan] Oh yeah. (laughs)

- I'm not claiming they're all going to China,

but a portion are,

many are going to Malaysia, including Microsoft

and Oracle have big data centers in Malaysia.

They're going all over Southeast Asia probably,

India as well.

There's stuff routing,

but the diffusion rules are very de facto.

You can only buy this many GPUs from this country.

And you can only rent a cluster this large

to companies that are Chinese.

They're very explicit on trying to stop smuggling.

And a big chunk of it was, hey,

random company by 16 servers ship them to China.

There's actually, I saw a photo from someone

in the semiconductor industry

who leads like a team for networking chips

that competes with Nvidia.

And he sent a photo

of a guy checking into a first-class united flight

from San Francisco to Shanghai or Shenzhen,

with a super micro box that is this big,

which can only contain GPUs. (Nathan chuckles)

And he was booking first-class,

'cause think about it,

3 to 5k for your first-class ticket,

server costs 240,000 in the US, to 50,000.

You sell it for 300,000 in China,

wait, you just got a free first-class ticket

- Yeah. - and a lot more money.

So, it's like...

And then, that's like small-scale smuggling.

Most of the large-scale smuggling

is like companies in Singapore and Malaysia

routing 'em around, or renting GPUs

completely legally. - I wanna jump in.

How much does this scale?

I think there's been some number, like some people

that are higher level economics understanding,

say that it's like as you go

from 1 billion of smuggling to 10 billion,

it's like you're hiding certain levels of economic activity.

And that's the most reasonable thing to me

is that there's gonna be some level where it's so obvious

that it's easier to find this economic activity.

And- - Yeah.

So, my belief is that last year, roughly...

So, Nvidia made a million H20s,

which are legally allowed to be shipped to China,

which we talked about is better for reasoning,

inference at least.

Maybe not training, but reasoning, inference.

And inference generally.

Then, they also had a couple 100,000,

we think like 200 to 300,000 GPUs

were routed to China

from Singapore, Malaysia, US, wherever.

Companies spun up by 16 GPUs, 64 GPUs,

whatever it is routed,

and Huawei's known for having spent up a massive network

of companies to get the materials they need

after they were banned in 2018.

So, it's not like otherworldly, but I agree.

Nathan's point is like, hey,

you can't smuggle up $10 billion of GPUs.

And then, the third source, which is just now banned

and which wasn't considered smuggling,

but is China is renting, I believe from our research,

Oracle's biggest GPU customer is ByteDance.

And for Google, I think it's their second biggest customer.

And so, like, and you go down the list of clouds

and especially these smaller cloud companies

that aren't like that hyperscalers.

Think beyond core of even Lambda even, there's a whole sea,

there's 60 different

new cloud companies serving Nvidia GPUs.

I think ByteDance is renting a lot of these all over it.

And so, these companies are renting GPUs

to Chinese companies,

and that was completely legal up until the diffusion rules,

which happened just a few weeks ago.

And even now, you can rent GPU clusters

that are less than 2,000 GPUs.

Or you can buy GPUs and ship them wherever you want

if they're less than 1,500 GPUs.

So, it's like there are still some ways to smuggle,

but yeah, as the numbers grow,

100 something billion dollars of revenue

for Nvidia last year, 200 something billion this year.

And if next year,

it could nearly double again or more than double

based on what we see with data center footprints

like being built out

all across the US and the rest of the world,

it's gonna be really hard

for China to keep up with these rules.

Yes, there will always be smuggling

and DeepSeek level models of GPT-4 level models,

o1 level models capable to train on what China can get,

even the next tier above that.

But if we speed run a couple more jumps

to billion dollar models, $10 billion models,

then it becomes, hey,

there is a compute disadvantage for China

for training models and serving them.

And the serving part is really critical.

DeepSeek cannot serve their model today.

It's completely out of inventory.

It's already started falling

in the App Store actually, downloads,

because you download it, you try and sign up,

they say, we're not taking registrations,

'cause they have no capacity.

You open it up, you get less than five tokens per second

if you even get your request approved.

Because there's just no capacity,

because they just don't have enough GPUs to serve the model,

even though it's incredibly efficient.

- It'd be fascinating to watch the smuggling,

'cause there's drug smuggling.

That's a market.

There's weapons smuggling.

And GPUs will surpass that

at some point. - Chips are highest value

per kilogram, probably by far. (chuckles)

- Oh man. - I have another question

for you, Dylan.

Do you track model API access internationally?

How easy is it for Chinese companies

to use hosted model APIs from the US?

- Yeah, that's incredibly easy.

OpenAI publicly stated DeepSeek uses their API.

And they say they have evidence.

And this is another element of the training regime

is people at OpenAI have claimed

that it's a distilled model.

i.e, you're taking OpenAI's model,

you're generating a lot of output,

and then you're training on the output in their model.

- Yeah. - And even if that's the case,

what they did is still amazing, by the way,

what DeepSeek did, efficiency-wise.

- Distillation is standard practice in industry.

Whether or not, if you're at a closed lab

where you care about terms of service and IP closely,

you distill from your own models.

If you are a researcher

and you're not building any products,

you distill from the OpenAI models.

- This is a good opportunity.

Can you explain big picture distillation as a process?

What is distillation?

What's the process - We've

- of distillation? - talked a lot about

training language models.

They are trained on text.

And post-training,

you're trying to train on very high quality text

that you want the model to match the features of.

Or if you're using RL,

you're letting the model find its own thing.

But for supervised fine-tuning,

for preference data, you need to have some completions

what the model is trying to learn to imitate.

And what you do there is, instead of a human data

or instead of the model you're currently training,

you take completions from a different,

normally more powerful model.

I think there's rumors that these big models

that people are waiting for, these GPT-5s of the world,

the Claude 3 Opuses of the world,

are used internally to do this distillation process

at OpenAI. - There's also

public examples, like Meta explicitly stated,

not necessarily distilling,

but they used 405b as a reward model

for 70b in their Llama 3.2

- Yes. - or 3.3.

This is all the same topic.

- So, (sighs) is this ethical? Is this legal?

Why is that "Financial Times" article headline say,

OpenAI says that there's evidence

that China's DeepSeek used its model to train competitor.

- This is a long, at least in the academic side

and research side, it has a long history,

'cause you're trying to interpret OpenAI's rule.

OpenAI's terms of service say

that you cannot build a competitor

with outputs from their models.

Terms of service are different than a license,

which are essentially a contract between organizations.

So, if you have a terms of service on OpenAI's account,

if I violate it, OpenAI can cancel my account.

This is very different than like a license

that says how you could use a downstream artifact.

So, a lot of it hinges on a word

that is very unclear in the AI space,

which is what is a competitor?

And so- - And then,

the ethical aspect of it is like,

why is it unethical for me

to train on your bottle - Yeah.

- when you can train on the internet's text?

- Yeah. - Right?

- So, there's a bit of a hypocrisy,

because OpenAI and potentially most of the companies

trained on the internet's text without permission.

- There's also a clear loophole,

which is that I generate data from OpenAI,

and then I upload it somewhere,

and then somebody else trains on it

and the link has been broken.

They're not under the same terms of service contract.

- This is why- - There's a lot of hippo...

There's a lot of to be discovered details

that don't make a lot of sense.

- This is why a lot of models today,

even if they train on zero OpenAI data,

you ask the model who trained you, it'll say,

I'm ChatGPT trained by OpenAI. - Yeah.

- Because there's so much copy-paste

of OpenAI outputs from that on the internet

that you just weren't able to filter it out.

And there was nothing in the RL

where they implemented like, hey, or post-training or SFT,

whatever, that says, hey,

I'm actually modeled by Allen Institute instead

of OpenAI. - We have to do this

if we serve a demo.

We do research and we use OpenAI APIs, because it's useful

and we want to understand post-training,

and our research models,

they'll say they're written by OpenAI

unless we put in the system prop that we talked about that.

Like, I am Tulu, I am a language model

trained by the Allen Institute for AI.

And if you ask more people around industry,

especially with post-training, it's a very doable task

to make the model say who it is

or to suppress the OpenAI thing.

So, in some levels, it might be that DeepSeek

didn't care that it was saying that it was by OpenAI.

If you're gonna upload model weights,

it doesn't really matter,

'cause anyone that's serving it in an application

and cares a lot about serving is going to, when serving it,

if they're using it for a specific task,

they're gonna tailor it to that.

And it doesn't matter that it's saying it's ChatGPT.

- Oh, I guess the one of the ways to do that

is like a system prompt or something like that.

Like if you're serving it to say that you're-

- That's what we do.

If we host a demo, you say you are Tulu 3,

a language model trained by the Allen Institute for AI.

We also are benefited from OpenAI data,

'cause it's a great research tool.

- Do you think there's any truth

and value to the claim,

OpenAI's claim that there's evidence that China's DeepSeek

use this model to train?

# Chapter 15

didn't care that it was saying that it was by OpenAI.

If you're gonna upload model weights,

it doesn't really matter,

'cause anyone that's serving it in an application

and cares a lot about serving is going to, when serving it,

if they're using it for a specific task,

they're gonna tailor it to that.

And it doesn't matter that it's saying it's ChatGPT.

- Oh, I guess the one of the ways to do that

is like a system prompt or something like that.

Like if you're serving it to say that you're-

- That's what we do.

If we host a demo, you say you are Tulu 3,

a language model trained by the Allen Institute for AI.

We also are benefited from OpenAI data,

'cause it's a great research tool.

- Do you think there's any truth

and value to the claim,

OpenAI's claim that there's evidence that China's DeepSeek

use this model to train?

- I think everyone has benefited regardless,

because the data's on the internet.

And therefore, it's in your pre-training now.

There are like subreddits

where people share the best ChatGPT outputs.

And those are in your-

- I think that they're trying to shift the narrative,

like they're trying to protect themselves.

And we saw this years ago

when ByteDance was actually banned

from some OpenAI APIs for training on outputs.

There's other AI startups that most people,

if you're in the AI culture, were like,

they just told us they trained on OpenAI outputs

and they never got banned.

That's how they bootstrapped their early models.

So, it's much easier to get off the ground using this

than to set up human pipelines and build a strong model.

So, it's long history here

and a lot of the communications

are seem like narrative control.

- Actually, over the last couple days,

we've seen a lot of people distill DeepSeek's model

into Llama models,

because the DeepSeek models - Mm-hmm.

- are complicated to run inference on,

because they're mixture of experts

and they're 600 plus billion parameters and all this.

And people distilled them

into the Llama models. (Lex laughing)

Because the Llama models are so easy to serve,

and everyone's built the pipelines

and tooling for inference - Yeah.

- with the Llama models,

because it's the open standard. (chuckles)

So, we've seen it, we've seen a roundabout.

Is it bad? Is it illegal?

Maybe it's illegal, whatever. I don't know about that.

But it's- - It could break contracts.

I don't think it's illegal, like in any illegal,

like no one's going to jail for this ever.

- I think fundamentally, I think it's ethical

or I hope it's ethical,

because the moment becomes, we ban that kind of thing,

it's gonna make everybody much worse off.

And I also actually, this is difficult,

but I think you should be allowed to train on the internet.

I know a lot of authors

and creators are very sensitive about it.

That's a difficult question.

But the moment you're not allowed to train on the internet.

- I agree.

- I have a schizo take on how you can solve this,

because it already works. - All right.

- I have a reasonable take on it.

- All right, all right. (Nathan laughing)

- So, Japan has a law which you're allowed

to train on any training data

and copyrights don't apply if you wanna train a model, A.

B, Japan has nine gigawatts of curtailed nuclear power.

C, Japan is allowed under the AI diffusion rule

to import as many GPUs as they'd like.

So, all we have to do, we have a market here to make,

we build massive data setters, we rent them to the labs,

and then we train models in a legally permissible way,

and there's no if, ands, or buts.

And now, the models have no potential copyright lawsuit

from "New York Times" or anything like that.

No, no, it's just completely legal.

- Yeah. - No, so-

- Genius. - The early copyright lawsuits

have fallen in the favor of AI training.

I would say that the long tail of use

is gonna go in the side of AI, which is if you do,

if you scrape the trillions of tokens of data,

you're not looking and saying,

this one "New York Times" article is so important to me.

But if you're doing a audio generation for music

or image generation and you say,

make it in the style of X person,

that's a reasonable case where you could figure out

what is their profit margin on inference.

I don't know if it's gonna be the 50/50

of YouTube creator program or something,

but I would opt into that program as a writer,

like, please, like that...

It's gonna be a rough journey,

but there will be some solutions like that that make sense.

But there's a long tail where it's just on the internet.

- I think one of the other aspects

of that "Financial Times" article implied.

And so, that leads to a more general question.

Do you think there's...

How difficult is spying, espionage,

and stealing of actual secret code

and data from inside companies?

How much of that is being attempted?

- Code and data is hard, but ideas is easy.

Silicon Valley operates (Dylan chuckles)

- Yeah. - on the way

that top employees get bought out

by other companies for a pay raise,

and a large reason

why these companies do this is to bring ideas with them.

And there's no, in California,

there's rules that certain,

like non-competes or whatever, are illegal in California

and whether or not there's NDAs and things,

that is how a lot of process happens.

Recently, there was somebody from Gemini

who helped make this 1 million context length

and everyone is saying the next Llama who,

I mean, he went to the Meta team,

is gonna have 1 million context length.

And that's how the world works.

- As far as industrial espionage and things,

that has been greatly successful in the past.

The Americans did the Brits,

the Chinese have done it to the Americans,

and so on and so forth.

It is a fact of life.

And so, to argue industrial espionage

can be stopped is probably unlikely.

You can make it difficult.

But even then, there's all these stories about,

hey, F35 and F22 have already been given to China

in terms of design plans and stuff.

Code and stuff like between, I say companies,

not nation states is probably very difficult,

but ideas are discussed a lot.

Whether it be a house party in San Francisco

or a company changing employees,

or always the mythical honeypot

that always gets talked about,

like someone gets honeypotted.

Because everyone working on AI

is a single dude who's in their 20s and 30s.

Not everyone, but a insane percentages.

So, there's always all these you know, and obviously-

- So, honeypotted is like a spy,

a female spy approaches you and like-

- Yeah, yeah. - Or male.

It's San Francisco, but... (Nathan laughing)

As a single dude, I will say, in his late 20s,

it is like, we are very easily corrupted.

- [Lex] Yeah.

- Not corrupted myself,

but we are, we are. - Yeah.

Everybody else, not me.

Everybody else. - Yeah. Exactly.

- I'm too oblivious that I am not single.

So, I'm safe from one espionage access. (laughs)

- Yeah, you have to make sure

to close all security vulnerabilities.

So, you, Dylan, collect a lot of information

about each of the mega clusters

for each of the major AI companies.

Can you talk about the buildouts

for each one that stand out?

- Yeah, so I think the thing

that's really important about these mega cluster buildouts

is they're completely unprecedented in scale.

US, data center power consumption

has been slowly on the rise and it's gone up to 2, 3%

even through the cloud computing revolution.

Data center consumption as a percentage of total US.

And that's been over decades of data centers, et cetera.

It's been climbing, climbing slowly.

But now, 2 to 3%.

Now, by the end of this decade, even under like,

when I say 10%, a lot of people that are traditionally

by 2028, 2030,

a traditional data center people like, that's nuts.

But then, people who are in AI

who have really looked at this

at the Anthropics and OpenAIs,

they're like, that's not enough.

And I'm like, okay. - Mm-hmm. (chuckles)

- But this is both through globally distributed

or distributed throughout the US,

as well as centralized clusters.

The distributed throughout the US is exciting

and it's the bulk of it.

Like, hey, OpenAI or say, Meta is adding a gigawatt.

But most of it is distributed through the US for inference

and all these other things.

- So, maybe we should lay it out what a cluster is.

So, does this include AWS?

Maybe it's good

to talk about the different kinds of clusters

and what you mean by mega clusters,

and what's the GPU - Mm-hmm.

- and what's the computer and what...

I'm just kidding. - Yeah, yeah, yeah.

- Not that far back, but yeah.

So, what do we mean by the clusters,

- Oh man. - the build outs?

- I thought I was about to do the Apple ad.

What's a computer? (group laughing)

So, traditionally, data centers and data center tasks

have been a distributed systems problem

that is capable of being spread very far and widely.

i.e, I send a request to Google,

it gets routed to a data center somewhat close to me.

It does whatever search ranking recommendation,

sends a result back.

The nature of the task is changing rapidly in that the task,

there's two tasks that people are really focused on now.

It's not database access,

it's not serve me the right page, serve me the right ad.

It's now a inference.

And inference is dramatically different

from traditional distributed systems,

but it looks a lot more similar.

And then, there's training.

The train inference side is still like, hey,

I'm gonna put thousands of GPUs

in blocks all around these data centers.

I'm gonna run models on them,

user submits a request, it gets kicked off,

or hey, my service, they submit a request to my service.

They're on Word,

and they're like, oh yeah, help me, Copilot.

And it starts, kicks it off,

or I'm on my Windows, Copilot, whatever,

Apple Intelligence, whatever it is,

it gets kicked off to a data center.

And that data center does some work and sends it back.

That's inference. That is going to be the bulk of compute.

And that's like, there's thousands of data centers

that we're tracking with satellites

and all these other things.

And those are the bulk of what's being built.

But the scale of...

And so, that's like what's really reshaping

and that's what's getting millions of GPUs.

But the scale of the largest cluster

is also really important.

When we look back at history, or through the age of AI,

it was a really big deal

when they did AlexNet on I think two GPUs

or four GPUs. - Yeah.

- [Dylan] I don't remember.

It was a really big deal. - Oh, it's a big deal,

'cause you use GPUs.

(Nathan laughing) - It's a big deal

they use GPUs and they used multiple.

But then over time, its scale has just been compounding.

And so, when you skip forward to GPT-3, then GPT 4,

GPT-4, 20,000 A100 GPUs,

unprecedented run in terms of the size and the cost.

A couple hundred million dollars on a YOLO.

A YOLO run for GPT-4.

And it yielded this magical improvement

that was perfectly in line with what was experimented

and just like a log scale right up.

- Oh yeah, they had that plot from the paper.

Scaling the technical were part.

- The scaling laws were perfect.

But that's not a crazy number.

20,000 A100s, roughly each GPU is consuming 400 watts.

And then, when you add in the whole server,

everything, it's like 15 to 20 megawatts of power.

Maybe you could look up what the power

of consumption of a person is

because the numbers are gonna get silly.

But 15 to 20 megawatts

was standard data center size was just unprecedented.

That was all GPUs running one task.

- [Nathan] How many watts is a toaster? (chuckles)

- A toaster is like also- - That's a good example.

- A similar power consumption to an A100.

H100 comes around, (Nathan chuckles)

they increase the power from like 400 to 700 watts.

And that's just per GPU.

And then, there's all the associated stuff around it.

So, once you count all that,

it's roughly like 1,200 to 1,400 watts for everything,

networking, CPUs, memory, blah, blah, blah.

- So, we should also say, so what's required?

You said power.

So, a lot of power is required,

a lot of heat is generated, so the cooling is required.

And because there's a lot of GPUs that have to be,

or CPUs or whatever, they have to be connected.

So, there's a lot of networking,

right? - Yeah, yeah, so I think...

Yeah, sorry for skipping past that.

And then, the data center itself is complicated.

But these are still

standardized data centers for GPT-4 scale.

Now, we step forward to what is the scale of clusters

that people have built last year.

And it ranges widely.

It ranges from like, hey, these are standard data centers

and we're just using multiple of them

and connecting them together really

with a ton of fiber between them,

a lot of networking, et cetera.

That's what OpenAI and Microsoft did in Arizona.

And so, they have 100,000 GPUs.

Meta, similar thing.

They took their standard existing data center design,

and it looks like an H,

and they connected multiple on 'em together.

And they got to,

they first did 16,000 GPUs, 24,000 GPUs total.

Only 16 of them,

1,000 of 'em were running on the training run,

because GPUs are very unreliable.

So, they needed to have spares to swap in and out.

All the way to like now 100,000 GPUs

that they're training on Llama 4 on currently.

Like 128,000 or so.

Think about 100,000 GPUs with roughly 1,400 watts a piece,

that's 140 megawatts, 150 megawatts for 128, right?

So, you're talking about

you've jumped from 15 to 20 megawatts to 10x,

almost 10x that number, 9x that number

to 150 megawatts in two years, from 2022 to 2024.

And some people like Elon that he admittedly,

and he says himself got into the game a little bit late

for pre-training large language models.

xAI was started later.

But then, he bet heaven and hell to get his data center up

and get the largest cluster in the world,

which is 200,000 GPUs.

And he did that. He bought a factory in Memphis.

He's upgrading the substation with the same time

he's got a bunch of mobile power generation,

a bunch of single cycle combine.

He tapped the natural gas line

that's right next to the factory

and is just pulling a ton of gas, burning gas.

He's generating all this power.

He's in a factory and an old appliance factory

that's shut down and moved to China long ago.

And he's got 200,000 GPUs in it.

And now, what's the next scale?

All the hyperscalers have done this.

Now, the next scale is something that's even bigger.

And so, Elon, just to stick on the topic,

he's building his own natural gas plant,

like a proper one right next door.

He's deploying tons of Tesla megapack batteries

to make the power more smooth and all sorts of other things.

He's got industrial chillers to cool the water down

because he's water-cooling the chips.

So, all these crazy things

to get the clusters bigger and bigger.

But when you look at, like, say,

what OpenAI did with Stargate,

that in Arizona, in Abilene, Texas,

what they've announced at least.

It's not built. Elon says they don't have the money.

There's some debates about this.

But at full-scale, at least the first section

is definitely money's accounted for,

but there's multiple sections.

But full scale, that data center is gonna be 2.2 gigawatts.

2,200 megawatts of power in

and roughly 1.8 gigawatts or 1,800 megawatt,

yeah, 1,800 megawatts of power delivered to chips.

Now, this is an absurd scale.

2.2 gigawatts is like more than most cities to be clear.

And delivered to a single cluster

that's connected to do training.

To train these models, to do both the pre-training,

the post-training, all of this stuff.

- This is insane. - It is.

- Insane. - What is a nuclear

power plant again- - everyone is doing this.

Everyone is doing this. (Lex laughing)

Meta in Louisiana,

they're building two natural gas plants, massive ones,

and then they're building this massive data center.

Amazon has plans for this scale.

Google has plans for this scale.

xAI has plans for this scale.

The guys that are racing,

the companies that are racing are racing hard,

and they're doing multi gigawatt data centers

to build this out,

because they think that, yeah, if I now have...

Obviously, pre-training scaling is gonna continue,

but to some extent,

but then also all this post-training stuff,

where you have a RL sandbox for computer use or whatever.

This is where they're gonna...

And all these viable domains

where they just keep learning and learning

and learning, self-play, whatever, whatever it is,

makes the AI so much more capable

because the line does go up.

As you throw more compute, you get more performance.

# Chapter 16

and then they're building this massive data center.

Amazon has plans for this scale.

Google has plans for this scale.

xAI has plans for this scale.

The guys that are racing,

the companies that are racing are racing hard,

and they're doing multi gigawatt data centers

to build this out,

because they think that, yeah, if I now have...

Obviously, pre-training scaling is gonna continue,

but to some extent,

but then also all this post-training stuff,

where you have a RL sandbox for computer use or whatever.

This is where they're gonna...

And all these viable domains

where they just keep learning and learning

and learning, self-play, whatever, whatever it is,

makes the AI so much more capable

because the line does go up.

As you throw more compute, you get more performance.

The shirt is about scaling laws.

To some extent, it is diminishing returns.

You 10x the compute, you don't get 10x better model.

You get a diminishing returns,

but also you get efficiency improvements.

So, you bend the curve.

And these scale of data centers are doing,

wreaking a lot of havoc on the network.

Nathan was mentioning there's,

Amazon has tried to buy this nuclear power plant, Talen.

And if you look at the Talen's stock,

it's just skyrocketing.

And they're building a massive

multi gigawatt data center there.

And you just go down the list.

There's so many ramifications.

Interesting thing is certain regions of the US

transmitting power cost more than actually generating it.

Because the grid is so slow to build,

and the demand for power and the ability to build power

and re-ramping on a natural gas plant

or even a coal plant is like easy enough to do.

But transmitting the power is really hard.

So, in some parts of the US, like in Virginia,

it costs more to transmit power than it cost to generate it.

Which is like, there's all sorts

of second order effects that are insane here.

- And the power grid support this kind of growth?

- Trump's executive orders,

there was a Biden executive order

before the end of the year,

but then Trump had some more executive orders,

which hopefully reduce the regulations

to where, yes, things can be built.

But yeah, this is a big, big challenge.

Is building enough power fast enough?

- Are you gonna basically have a nuclear power plant

next to a data center for each one of these?

- So, the fun thing here is this is too slow.

- [Nathan] To build the power plant.

- To build a power plant

or to reconfigure an existing power plant is too slow.

And so, therefore, you must use natural...

Data center power consumption is flat.

It spike- - Which is why nuclear

is also good for it.

Like long-term, nuclear is a very natural fit,

- Yeah, it's- - but you can't do solar

or anything in the short-term like that.

- Because data center power is like this.

You're telling me, I'm gonna buy tens

of billions of dollars of GPUs and idle them,

'cause the power's not being generated?

Power's cheap.

If you look at the cost of a cluster,

less than 20% of it is power.

Most of it is the capital cost and depreciation of the GPUs.

And so, it's like, well, screw it,

I'll just build natural gas plants.

This is what Meta is doing in Louisiana.

This is what OpenAI's doing in Texas

and all these different places.

They may not be doing it directly,

but they are partnered with someone.

And so, there is a couple hopes. One is...

And Elon, what he is doing in Memphis is like,

to the extreme,

they're not just using dual combine cycle gas,

which is like super efficient,

he's also just using single cycle

and mobile generators and stuff, which is less efficient.

But there's also the flip side,

which is solar power generation is like this,

and wind is another like this, correlate different.

So, if you stack both of those,

plus you get a big chunk of batteries,

plus you have a little bit of gas,

it is possible to run it more green.

It's just the timescales for that is slow.

So, people are trying, - Mm-hmm.

- but Meta basically said, whatever,

don't care about my sustainability pledge.

Or they'll buy like a power,

it's called a PPA, power purchasing agreement,

or they'll be a massive wind farm

or solar farm, like wherever. - Oh.

- And then, they'll just pretend

like those electrons are being consumed by the data center,

but in reality, they're paying for the power here

and selling it to the grid, and they're buying power here.

- [Lex] Yep.

- And then, another thing is like Microsoft

quit on some of their sustainability pledges.

Elon, what he did with Memphis

is objectively somewhat dirty,

but he is also doing it in an area

where there's a bigger natural gas plant right next door

and like a sewer next, or not a sewer,

but like a wastewater treatment and a garbage dump nearby.

And he's obviously made the world

a lot more clean than that one data center is gonna do.

So, I think it's fine to some extent.

And maybe AGI solves

global warming and stuff, (Lex laughing)

whatever it is.

This is sort of the attitude that people at the labs have,

which is like, yeah, it's great.

We'll just use gas.

Because the race is that important.

And if we lose, that's way worse.

- I should say that I got a chance

to visit the Memphis data center.

- Oh wow. - And it's incredible.

I visited with Elon.

Just the teams and the rate of innovation there is insane.

My sense is that nobody's ever done anything of this scale

and nobody has certainly ever done anything

of this scale at the rate that xAI is doing.

So, they're like figuring out...

And so, I was sitting in on all these meetings

where they're brainstorming, it's like, it's insane.

It's exciting, 'cause they're like,

they're trying to figure out what the bottlenecks are,

how to remove the bottlenecks, how to make sure that,

there's just so many really cool things

about putting together a data center,

'cause everything has to work.

The people that do like the CIS admin,

the machine learning, all that is the exciting thing, so on,

but really, the people that run everything (chuckles)

are the folks that know the low level software

and hardware that runs everything,

the networking, all of that.

And so, you have to make sure

you have procedures that test everything.

I think they're using ethernet.

I don't know how they're doing the networking, but-

- They're using Nvidia Spectrum-X ethernet.

There's actually like, I think yeah,

the unsung heroes are the cooling and electrical systems,

which are just like (Lex chuckles)

- Exactly. - glossed over.

- [Lex] Yeah.

- But I think one story

that maybe is like exemplifies how insane this stuff is,

is when you're training, you're always doing,

you're running through the model a bunch,

in the most simplistic terms,

running through the model a bunch.

And then, you're gonna exchange everything

and synchronize the weights.

So, you'll do a step,

this is like a step in model training.

And every step, your loss goes down, hopefully.

And it doesn't always, but in the simplest terms,

you'll be computing a lot, and then you'll exchange.

The interesting thing is GPU power is most of it,

networking power is some, but it's a lot less.

So, while you're computing,

your power for your GPUs is here.

But then when you're exchanging weights,

if you're not able to overlap communications

and compute perfectly, there may be a time period

where your GPUs are just idle, and you're exchanging weights

and you're like, hey, the model's updating.

So, you're exchanging the gradient, you do the model update,

and then you start training again.

So, the power goes...

- Mm-hmm. - And it's super spiky.

- Yeah. - And so, funnily enough,

when you talk about the scale of data center power,

you can blow stuff up

so easily. - Yeah.

- And so, Meta actually has,

accidentally opened upstream something to code in PyTorch

where they added an operator.

And I kid you not, whoever made this,

I wanna hug the guy, because it says PyTorch,

it's like pytorch.powerplantnoblowup

(Lex laughing) equals zero or equal one.

(Nathan laughing) And what it does,

what it does is amazing.

- [Lex] Yeah.

- When you're exchanging the weights,

the GP will just compute fake numbers,

so the power doesn't spike too much.

And so then, the power plants don't blow up

because the transient spikes screw stuff up.

- Well, that makes sense.

You have to do that kind of thing.

You have to make sure they're not idle.

Yeah, that's- - And Elon's solution

was like, "Let me throw a bunch of Tesla mega packs

and a few other things."

- Stabilize, yeah. - Everyone

has different solutions,

but Meta's at least (Lex laughing)

was publicly and openly known,

which is just like, set this operator.

And what this operator does is it just makes the GPUs

compute nothing so that the power doesn't spike.

- But that just tells you

how much power you're working with.

It's insane.

It's insane. - People should just go Google

like scale, like what does X watts do?

And go through all the scales from one watt

to a kilowatt to a megawatt, and you look and stare at that,

and you're how high on the list a gigawatt is,

and it's mind-blowing.

- Can you say something about the cooling?

So, I know Elon's using liquid cooling,

I believe, in all cases.

That's a new thing, right?

Most of 'em don't use liquid cooling.

Is there something interesting to say about the cooling?

- Yeah, yeah.

So, air cooling has been the de facto standard.

Throw a bunch of metal heat pipes, et cetera, and fans,

and that's cooled, that's been enough to cool it.

People have been dabbling in water cooling.

Google's TPUs are water-cooled.

So, they've been doing that for a few years.

But with GPUs, no one's ever done...

And no one's ever done the scale

of water cooling that Elon just did.

Now, next generation Nvidia

is for the highest end GPU, it is mandatory water cooling.

You have to water cool it.

But Elon did it on this current generation,

and that required a lot of stuff.

If you look at some of the satellite photos

and stuff of the Memphis facility,

there's all these external water chillers that are sitting,

basically, it looks like a semi-truck pod thing.

What's it called? The container.

But really, those are water chillers.

And he has like 90 of those water chillers

just sitting outside, 90 different containers with water,

like chill the water, bring it back to the data center,

and then you distribute it to all the chips,

pull all the heat out, and then send it back.

And this is both a way to cool the chips,

but it's also an efficiency thing.

And going back

to that sort of three vector thing right there is,

there is memory bandwidth FLOPS and interconnect.

The closer the chips are together,

the easier it is to do high speed interconnects.

And so, this is also like a reason

why you wanna go water cooling

is because you can just put the chips

right next to each other,

and therefore get higher speed connectivity.

- I gotta ask you, so in one of your recent posts,

there's a section called cluster measuring contest, so...

- There's another word there, but I won't say it, you know.

(Dylan and Nathan laughing)

- Who's got the biggest now and who's gonna have

the biggest? - Today,

individual largest is Elon.

- Right. Elon's cluster.

- Elon's cluster in Memphis, 200,000 GPUs.

- Okay.

- Meta has like 128,000, OpenAI has 100,000 now.

Now, to be clear, other companies have more GPUs than Elon.

They just don't have 'em in one place.

And for training, you want them tightly connected.

There's some techniques that people are researching

and working on that lets you train across multiple regions.

But for the most part, you want them all in one area.

So, you can connect them with high speed networking.

And so, Elon today has 200,000 H100s.

And 100,000 H100s, 100,000 H200s.

Meta, OpenAI, and Amazon all have

on the scale of 100,000, a little bit less.

But this year, this year, people are building much more.

Anthropic and Amazon are building a cluster

of 400,000 Trainium 2, which is Amazon-specific chip

trying to get away from Nvidia.

Meta and OpenAI have scales for hundreds of thousands,

but by next year,

you'll have like 500,000 to 700,000 GPU clusters.

And note, those GPUs are much higher power consumption

than existing ones.

Hopper, 700 watts, Blackwell goes to 1,200 watts.

So, the power

per chip is growing (Lex laughing)

and the number of chips is growing.

- Nuts. Elon said he'll get to a million.

You think that's actually feasible?

- I don't doubt Elon.

The filings that he has for the power plan

and the Tesla battery packs,

it's clear he has some crazy plans for Memphis.

Like permits and stuff is open record.

But it's not quite clear what and what the timescales are.

I just never doubt Elon. He's gonna surprise us.

- So, what's the idea with these clusters?

If you have a million GPUs,

what percentage in let's say,

two, three years is used for training

and what percent of pre-training

and what percent is used

for the actual computation? - So, these mega clusters

make no sense for inference.

You could route inference there and just not train.

But most of the inference capacity is being,

hey, I've got a 30-megawatt data center here.

I've got 50 megawatts here, I've got 100 here, whatever.

I'll just throw inference in all of those,

because the mega clusters,

multi gigawatt data centers, I want to train there.

Because that's where all of my GPUs are co-located,

where I can put them

at a super high networking speed connected together.

Because that's what you need for training.

Now, with pre-training, this is the old scale.

You would increase parameters,

you'd increase data, model gets better.

That doesn't apply anymore,

because there's not much more data in the pre-training side.

Yes, there's video and audio and image

that has not been fully taken advantage of.

So, there's a lot more scaling,

but a lot of people have transcript,

taken transcripts of YouTube videos,

and that gets you a lot of the data.

Doesn't get you all of the learning value

out of the video and image data,

but there's still scaling to be done on pre-training.

But this post-training world

is where all the FLOPS are gonna be spent.

The model's gonna play with itself.

It's gonna self-play, it's gonna do verifiable tasks,

it's gonna do computer use in sandboxes.

It might even do simulated robotics things.

All of these things are gonna be environments

where compute is spent in, quote, unquote, "post-training".

But I think it's gonna be good.

We're gonna drop the post from post-training.

- Yeah. Wow. - It's gonna be pre-training

and it's gonna be training, I think.

At point at some, (Dylan drowns out Nathan)

at some point. (Nathan laughing)

Because for the bulk of the last few years,

pre-training has dwarfed post-training.

- [Lex] Mm-hmm.

- But with these verifiable methods,

especially ones that scale really,

potentially infinitely,

like computer use and robotics, not just math and coding,

where you can verify what's happening,

those infinitely verifiable tasks,

it seems you can spend as much compute as you want on them.

- Especially at the context length increase.

'Cause at the end of pre-training

is when you increase the context length for these models.

And we've talked earlier in the conversation

about how the context length, when you have a long input,

is much easier to manage than output.

And a lot of these post-training

and reasoning techniques rely on a ton of sampling

and it's becoming increasingly long context.

So, there's just your,

effectively your compute efficiency goes down.

I think FLOPS is the standard for how you measure it.

But with RL and you have to do all these things,

where you move your weights around

in a different way than at pre-training and just generation.

It's going to be become less efficient

and FLOPS is gonna be less of a useful term.

And then, as the infrastructure gets better,

it's probably gonna go back to FLOPS.

- So, all of the things we've been talking about

is most likely going to be Nvidia.

Is there any competitors?

- Google, I ignored them. - TPU. Yeah. (chuckles)

- I was like, huh? - Yeah,

what's the story with TPU?

Like what's the...

- TPU is awesome. It's great.

Google is, they're a bit more tepid

on building data centers for some reason.

They're building big data centers, don't get me wrong.

And they actually have the biggest cluster.

I was talking about Nvidia clusters,

they actually have the biggest cluster, period.

But the way they do it is very interesting.

They have two data center super regions

in that, the data center isn't physically

like all of the GPUs aren't physically on one site,

but they're like 30 miles from each other.

Or not GPUs, TPUs.

They have like in Iowa and Nebraska,

they have four data centers

that are just right next to each other.

- Why doesn't Google flex it's cluster size?

- Go to multi-datacenter training.

There's good images in there. So, I'll show you what I mean.

It's just SemiAnalysis multi-datacenter.

So, this is an image

of what a standard Google data center looks like.

By the way, their data centers look very different

than anyone else's data centers.

- [Lex] What are we looking at here?

- So, these are, yeah,

so if you see this image right,

in this center, there are these big rectangular boxes.

Those are where the actual chips are kept.

And then, if you scroll down a little bit further,

you can see there's like these water pipes,

there's these chiller cooling towers in the top,

# Chapter 17

Or not GPUs, TPUs.

They have like in Iowa and Nebraska,

they have four data centers

that are just right next to each other.

- Why doesn't Google flex it's cluster size?

- Go to multi-datacenter training.

There's good images in there. So, I'll show you what I mean.

It's just SemiAnalysis multi-datacenter.

So, this is an image

of what a standard Google data center looks like.

By the way, their data centers look very different

than anyone else's data centers.

- [Lex] What are we looking at here?

- So, these are, yeah,

so if you see this image right,

in this center, there are these big rectangular boxes.

Those are where the actual chips are kept.

And then, if you scroll down a little bit further,

you can see there's like these water pipes,

there's these chiller cooling towers in the top,

and a bunch of diesel generators.

The diesel generators are backup power.

The data center itself

look physically smaller than the water chillers.

So, the chips are actually easier to keep together,

but then cooling all the water

for the water cooling is very difficult.

So, Google has a very advanced infrastructure

that no one else has for the TPU.

And what they do is they've stamped these data center,

they've stamped a bunch of these data centers out

in a few regions.

So, if you go a little bit further down,

this is a Microsoft, this is in Arizona.

This is where GPT-5, quote, unquote, "will be trained".

(Lex laughing)

- [Nathan] If it doesn't exist already.

- Yeah, if it doesn't exist already.

But each of these data centers,

I've shown a couple images of them,

they're really closely co-located

in the same region, Nebraska, Iowa.

And then, they also have a similar one in Ohio complex.

And so, these data centers are really close to each other.

And what they've done

is they've connected them super high bandwidth with fiber.

And so, these are just a bunch of data centers.

And the point here is that Google

has a very advanced infrastructure,

very tightly connected in a small region.

So, Elon will always

have the biggest cluster fully connected,

because it's all in one building.

- Yeah. - And he's completely right

on that.

Google has the biggest cluster,

but you have to spread over three sites,

and by a significant margin,

but you have to go across multiple sites.

- Why doesn't Google compete with Nvidia?

Why don't they sell TPUs?

- I think there's a couple problems with it.

It's like one, TPU has been a form

of allowing search to be really freaking cheap

and build models for that.

And so, a big chunk of the search,

GPU purchases or TPU purchases,

or big chunk of Google's purchases and usage,

all of it is for internal workloads.

Whether it be Search, now, Gemini, YouTube,

all these different applications that they have ads,

these are where all their TPUs are being spent,

and that's what they're hyperfocused on.

And so, there's certain aspects of the architecture

that are optimized for their use case

that are not optimized elsewhere.

One simple one is they've open sourced the Gemma model

and they called it Gemma 7B.

But then, it's actually 8 billion parameters

because the vocabulary is so large.

(Lex laughing)

And the reason they made the vocabulary so large

is because TPU's matrix-multiply unit is massive.

Because that's what they've optimized for.

And so, they decided, oh, well,

I'll just make the vocabulary large too,

even though it makes no sense

to do so in such a small model,

because that fits on their hardware.

So, Gemma doesn't run

as efficiently on a GPU as a Llama does.

But vice versa, Llama doesn't run

as efficiently on a TPU as a Gemma does.

And it's so like,

there's certain aspects of hardware, software, co-design.

So, all their search models,

or their ranking and recommendation models,

all these different models that are AI,

but not like GenAI,

have been hyper optimized with TPUs forever.

The software stack is super optimized,

but all of this software stack

has not been released publicly at all.

Very small portions of it, Jax and XLA have been.

But the experience when you're inside of Google

and you're training on TPUs as a researcher,

you don't need to know anything

about the hardware in many cases.

It's pretty beautiful.

- They all love it. - But soon as you

step outside... (Nathan chuckles)

- A lot of 'em go back. (chuckles)

They leave Google and then they go back.

- Yeah. - Yeah.

They leave and they start a company,

'cause they have all these amazing research ideas

and they're like, wait, infrastructure's hard,

software is hard, and this is on GPUs.

Or if they try to use TPUs, same thing,

'cause they don't have access to all this code.

And so, it's like, how do you convince a company

whose Golden Goose is Search,

where they're making hundreds of billions of dollars from,

to start selling GPU, or TPUs,

which they used to only buy a couple billion of...

I think in 2023, they bought like a couple billion,

and now they're buying 10 billion to $15 billion worth.

But how do you convince them

that they should just buy like twice as many

and figure out how to sell them, and make $30 billion?

Like, who cares about making $30 billion?

- Won't that 30 billion

exceed actually the search profit eventually?

- You're always gonna make more money on services

than hardware. - Always.

- Like yeah, to be clear, today,

people are spending a lot more

on hardware than they are the services,

because the hardware runs the service spend.

- Yeah. - But like-

- [Lex] You're investing, yeah.

- If there's no revenue for AI stuff

or not enough revenue, then obviously, it's gonna blow up.

People won't continue to spend on GPUs forever.

And then, Nvidia's trying to move up the stack with software

that they're trying to sell and license and stuff.

But Google has never had that DNA

of this is a product we should sell.

The Google Cloud does,

which is a separate organization from the TPU team,

which is a separate organization from the DeepMind team,

which is a separate organization from the Search team,

there's a lot of bureaucracy here.

- Wait, Google Cloud is a separate team than the TPU team?

- Technically, TPU sits under infrastructure,

which sits under Google Cloud,

but Google Cloud, for renting stuff

and TPU architecture are very different goals.

And hardware and software, like all of this.

The JAX, XLA teams

do not serve Google's customers externally.

Whereas Nvidia's various CUDA teams

for things like NCCL serve external customers.

- [Lex] Mm-hmm.

- The internal teams like JAX and XLA and stuff,

they more so serve DeepMind

and Search. - Yeah.

- And so, their customers' different.

They're not building a product for them.

- Do you understand why AWS keeps winning

versus Azure for cloud versus Google Cloud?

- Yeah, there's- - Google Cloud is tiny,

isn't it, relative to AWS? - Google Cloud is third.

- [Nathan] Yeah, yeah.

- Microsoft is the second biggest,

but Amazon is the biggest. - Yeah.

- And Microsoft deceptively

sort of includes Microsoft Office 365, and things like that.

Like some of these enterprise-wide licenses.

So, in reality, the Gulf is even larger,

Microsoft is still second though.

Amazon is way bigger. Why?

Because using AWS is better and easier.

And in many cases,

it's cheaper. - It was first.

- And it's first. - It was first.

- [Lex] Yeah, but there's a lot of things

that are first that- - Well, it's easier...

It's harder to switch

than it is to- - Yeah, okay.

- AWS is- - Because it's large-

- There's big fees for switching too.

- AWS generates over 80% (Nathan chuckles)

of Amazon's profit, I think over 90%.

- That's insane. - The distribution centers

are just like, one day,

we'll decide to make money from this, but they haven't yet.

They make tiny little profit from-

- Yeah, one day, Amazon Prime will triple in price.

- You would think they would improve AWS interface,

'cause it's horrible.

It's clunky, but everybody is...

(Lex laughing) - [Nathan] I don't, yeah,

one would think.

- I think actually, Google's interface is sometimes nice,

but it's also they don't care

about anyone besides their top customers.

- Yeah, exactly. - And like

their customer service sucks

and they have a lot less, like...

- All these companies,

they optimize for the big customers, yeah.

It's supposed to be

for business. - Well, and Amazon

has always optimized for the small customer too though.

Obviously, they optimize a lot for the big customer,

but when they started, they just would go

to like random Bay Area things and give out credits.

And then, they like,

or just put in your credit card and use us.

It went back in the early days.

So, they've always,

the business has grown with them in burgeon.

So, why does Amazon, why is Snowflake all over Amazon?

Because Snowflake, in the beginning,

when Amazon didn't care about them, was still using Amazon.

And then, of course, one day,

Snowflake and Amazon has a super huge partnership,

but this is the case,

like Amazon's user experience and quality is better.

Also, a lot of the silicon they've engineered makes them

have a lower cost structure in traditional cloud,

storage, CPU, networking,

that kind of stuff than in databases.

I think like four of Amazon's top five revenue products,

margin products are gross profit products,

are all database-related products

like Redshift and all these things.

So, Amazon has a very good silicon to user experience,

entire pipeline with AWS.

I think Google, their silicon teams,

yeah, they have awesome silicon internally,

TPU, the YouTube chip,

some of these other chips that they've made.

And the problem is they're not serving external customers,

they're serving internal customers.

- Nvidia's entire culture

is designed from the bottom-up to do this.

There's this recent book, "The Nvidia Way" by Tae Kim,

that details this

and they're how they look for future opportunities

and ready their CUDA software libraries

to make it so that new applications

of high performance computing

can very rapidly be evolved on CUDA and Nvidia chips.

And that is entirely different

than Google as a services business.

- Yeah, Nvidia, it should be said,

is a truly special company.

There's the whole, the culture and everything,

they're really optimized for that kind of thing.

Speaking of which, is there somebody

that can even challenge Nvidia hardware-wise?

Intel, AMD?

- I really don't think so.

We went through a very long process of working

with AMD on training on their GPU's inference and stuff.

And they're decent.

Their hardware is better in many ways than in Nvidia's.

The problem is their software is really bad,

and I think they're getting better,

they're getting better faster, but they're just,

the Gulf is so large

and they don't spend enough resources on,

or haven't historically.

Maybe they're changing their tune now,

but for multiple months, we were submitting the most bugs.

Like us, SemiAnalysis. - Mm-hmm.

- Like what the fuck?

Why are we submitting the most bugs?

Because they only,

and they only cared about their biggest customers.

And so, they'd ship them a private image, blah, blah, blah.

And it's like, okay, but I am just using PyTorch

and I wanna use the publicly

available libraries - Mm-hmm.

Yeah. - and you don't care

about that.

So, they're getting better.

But I think AMD's not possible.

Intel's obviously in dire straits right now

and needs to be saved somehow.

Very important for national security,

for American technology dominance.

- Can you explain the, obviously,

so why are they in dire straits?

- Going back to earlier, only three companies can R&D.

- Yeah. - Taiwan, Hsinchu,

Samsung, Pyongyang, and then Intel, Hillsboro.

Samsung's doing horribly. Intel's doing horribly.

We could be in a world

where there's only one company that can do R&D,

and that one company already manufactures most of chips.

They've been gaining market share anyways.

But that's a critical thing.

So, what happens to Taiwan

means the rest of the world's semiconductor industry,

and therefore tech, relies on Taiwan.

And that's obviously precarious.

As far as Intel, they've been slowly, steadily declining.

They were on top of servers and PCs,

but now, Apple's done the M1

and Nvidia's releasing a PC chip,

and Qualcomm's releasing a PC chip,

and in servers, hyperscalers are all

making their own ARM-based server chips.

And Intel has no AI silicon wins.

They have very small wins.

And they never got into mobile,

because they said no to the iPhone.

And all these things have compounded

and they've lost their process technology leadership.

They were ahead for 20 years

and now they're behind by at least a couple years.

And they're trying to catch back up

and we'll see if their 18A, 14A strategy works out,

where they try and leapfrog TSMC.

But like...

And Intel is just losing tons of money anyways.

And they just fired their CEO,

even though their CEO was the only person

who understood the company well.

We'll see.

He was not the best, but he was pretty good, relatively.

Technical guy.

- [Lex] Where does Intel make most of its money?

The CPU still, right? - PCs

and data center CPUs, yeah.

But data center CPUs are all going Cloud

and Amazon, Microsoft, Google are making ARM-based CPUs.

And then, PC side, AMDs gained market share.

Nvidia's launching a chip that's not gonna be a success.

Mediatek, Qualcomm ever launch chips.

Apple's doing well.

They could get squeezed a little bit in PC,

although PC generally I imagine,

will just stick Intel mostly for Windows side.

- Let's talk about the broad AI race. Who do you think wins?

We talked about Google, Meta,

xAI. - The default leader

has been Google because of their infrastructure advantage.

- [Lex] Well, like in the news, OpenAI is the leader.

- They're leading in the-

- They have the best model.

- They have the best model that people can use.

And they're experts- - And they have

the most AI revenue.

- Yeah. OpenAI is winning.

- So, who's making money on AI right now?

Is anyone making money?

- So, accounting profit-wise, Microsoft is making money,

but they're spending a lot of CapEx,

and that gets depreciated over years.

Meta's making tons of money,

but with recommendation systems,

which is AI, (Nathan chuckles)

but not with Llama. - Right.

- Llama's losing money for sure.

I think Anthropic and OpenAI are obviously not making money,

'cause otherwise, they wouldn't be raising money.

They have to raise money to build more.

Although theoretically, they are making money.

You spent a few hundred million dollars on GPT-4,

and it's doing billions in revenue.

So, obviously, it's making money.

Although they had to continue to research

to get the compute efficiency wins,

and move down the curve

to get that 1,200x that has been achieved for GPT-3.

Maybe we're only at a couple 100x now,

but with GPT-4 Turbo and 4o,

and there'll be another one

probably cheaper than GPT-4o even

that comes out at some point.

- And that research costs a lot of money.

- [Dylan] Yep. Exactly.

- That's the thing that I guess

is not talked about with the cost,

that when you're referring to the cost of the model,

it's not just the training or the test runs,

it's the actual research, the manpower that-

- Yeah, to do things like reasoning right now

that that exists, they're gonna scale it,

they're gonna do a lot of research still.

I think people focus on the payback question,

but it's really easy to just be like, well,

GDP is humans and industrial capital.

And if you can make intelligence cheap, you can grow a lot.

That's the sort of dumb way to explain it.

But that's what basically the investment thesis is.

I think only Nvidia is actually making tons of money

and other hardware vendors.

The hyperscalers are all on paper making money,

but in reality, they're spending a lot more

on purchasing the GPUs,

which you don't know if they're still

gonna make this much money on each GPU in two years.

You don't know if all of a sudden, OpenAI goes kapoof,

and now Microsoft has hundreds of thousands

of GPUs they were renting to OpenAI that are,

that they paid for themselves with their investment in them

that no longer have a customer.

this is always a possibility. I don't believe that.

I think OpenAI will keep raising money.

I think others will keep raising money,

because the investments, the returns from it

are gonna be eventually huge once we have AGI.

- So, do you think multiple companies will get...

Let's assume that- - I don't think

it's winner take all.

- Okay. So, let's not call it AGI, whatever.

It's like a single day.

It's a gradual thing. - Powerful AI,

super powerful AI.

- But it's a gradually increasing set of features

that are useful and make-

- [Nathan] Rapidly increasing

set of features. - Rapidly,

rapidly increasing set of features.

So, you're saying a lot of companies will be...

It just seems absurd that all of these companies

are building gigantic data centers.

- There were companies that will benefit from AI,

but not because they train the best model.

Like Meta has so many avenues

to benefit from AI and all of their services.

People are there, people spend time on Meta's platforms

and it's a way to make more money per user per hour.

- Yeah it seems like Google/xAI/Tesla, important to say,

and then Meta will benefit not directly from the AI

like the LLMs, but from the intelligence,

like the additional boost of intelligence

to the products they already sell.

So, whether that's the recommendation system

or for Elon who's been talking about Optimus, the robot,

# Chapter 18

that are useful and make-

- [Nathan] Rapidly increasing

set of features. - Rapidly,

rapidly increasing set of features.

So, you're saying a lot of companies will be...

It just seems absurd that all of these companies

are building gigantic data centers.

- There were companies that will benefit from AI,

but not because they train the best model.

Like Meta has so many avenues

to benefit from AI and all of their services.

People are there, people spend time on Meta's platforms

and it's a way to make more money per user per hour.

- Yeah it seems like Google/xAI/Tesla, important to say,

and then Meta will benefit not directly from the AI

like the LLMs, but from the intelligence,

like the additional boost of intelligence

to the products they already sell.

So, whether that's the recommendation system

or for Elon who's been talking about Optimus, the robot,

potentially the intelligence of the robot.

And then, you have personalized robots in the home,

that kind of thing.

He thinks it's a 10 plus trillion dollar business, which...

(Lex laughing)

- Yeah, sure. - At some point maybe.

Not soon, but who knows what robotics will-

- Let's do a TAM analysis.

8 billion humans

and let's get (Nathan laughing)

8 billion robots.

And let's pay 'em the average salary,

and yeah, there we go, 10 trillion, more than 10 trillion.

- Yeah.

If there's robots everywhere, why does it have to be

just 8 billion robots? - Yeah, yeah,

of course, of course.

- [Lex] It could be-

- I'm gonna have one robot, you're gonna have like 20.

- Yeah, I see a use case for that.

So, yeah, I guess the benefit

would be in the products they sell,

which is why OpenAI's in a trickier position, 'cause they-

- All of the value of OpenAI right now

as a brand is in ChatGPT.

And there is actually not that, for most users,

there's not that much of a reason

that they need OpenAI to be spending billions

and billions of dollars on the next best model,

- Mm-hmm. - when they could

just license Llama 5, and for be way cheaper.

So, that's like ChatGPT

is an extremely valuable entity to them, (chuckles)

but they could make more money just off that

than trying- - The chat application

is clearly like, does not have tons of room to continue.

Like the standard chat,

where you're just using it for a random question and stuff.

The cost continues to collapse.

V3 is the latest- - It'll go down to ads.

- Biggest, but it's gonna get supported by ads.

Meta already serves 405b

and probably loses the money, but at some point,

they're going to get, the models are gonna get so cheap

that they can just serve them for free with ads supported.

And that's what Google's gonna be able to do.

And that's obviously they've got a bigger reach.

So, chat is not gonna be the only use case.

It's like these reasoning, code, agents, computer use,

all this stuff is where OpenAI

has to actually go to make money in the future.

Otherwise, they're kaputs.

- But X, Google, and Meta have these other products.

So, isn't it likely that OpenAI

and Anthropic disappear eventually?

Because it's- - Unless they're so good

at models, 'cause they are.

- [Lex] But it's such a cutting edge,

I mean, you have to get- - It depends on where

you think AI capabilities are going.

- You have to keep winning. - Yes.

- You have to keep winning.

As you climb,

even if the AI capabilities are going super rapidly awesome

into the direction of AGI, there's still a boost

for X in terms of data, Google in terms of data,

Meta in terms of data,

in terms of other products and the money.

There's just

huge amount of money. - But if the whole idea

is human data is tapped out, we don't care,

we all care about self-play verifiable tasks-

- Yes, the self-play, - Think about AWS-

- [Lex] which is an R&D problem.

- AWS does not make a lot of money

on each individual machine.

And the same can be said for the most powerful AI platform,

which is even though the calls to the API are so cheap,

there's still a lot of money

to be made by owning that platform.

And there's a lot of discussions

as it's the next compute layer.

- You have to believe that...

And there's a lot of discussions that tokens

and tokenomics and LLM APIs are the next compute layer,

or the next paradigm for the economy,

like energy and oil was.

But there's also, you have to believe that APIs

and chat are not where AI is stuck.

It is actually just tasks

and agents and robotics and computer use.

And those are the areas

where all the value will be delivered,

not API, not chat application.

- So, is it possible you have,

I mean, it all just becomes a commodity,

and you have the very thin wrapper like Perplexity.

Just joking.

- [Nathan] There are a lot of wrappers

making a lot of money.

- Yeah, but do you think it's possible

that people would just even forget what OpenAI

and Anthropic is, and just,

'cause there'll be wrappers around the API,

and it just dynamically-

- If model progress is not rapid, yeah.

It's becoming a commodity.

DeepSeek-V3 shows this,

but also the GPT-3 chart earlier, chart showed this.

Llama 3B is 1,200x cheaper than GPT-3.

Any GPT-3, like anyone whose business model

was GPT-3 level capabilities is dead.

- Yeah. - Anyone whose business model

is GPT-4 level capabilities is dead.

- It is a common saying

that the best businesses being made now are ones

that are predicated on models getting better.

- Right, which would be wrappers,

thing that is riding the wave of the models.

- The short-term that company that could make the most money

is the one that figures out

what advertising targeting method works

for language model generations.

We have the Meta ads which are hyper targeted in feed,

not within specific pieces - Mm-hmm.

- of content.

And we have search ads that are used by Google

and Amazon has been rising a lot on Search.

But within a piece, within a return from ChatGPT,

it is not clear

how you get a high quality placed ad within the output.

And if you can do that with model costs coming down,

you can just get super high revenue per...

That revenue is totally untapped

and it's not clear technically how it is done.

- Yeah, that is...

the ad sense innovation that Google did,

the one day you'll have in GPT output an ad

and that's gonna make

billions, not- - And it could be very subtle.

It could be in conversation.

We have voice mode now.

It could be some way of making it,

so the voice introduces certain things.

It's much harder to measure

and it takes imagination, but yeah.

- And it wouldn't come off shady,

so you would receive public blow back, that kind of thing.

So, you have to do it loud enough

to where it's clear it's an ad that and balance all of that.

So, that's the open question they're trying to solve.

Anthropic and OpenAI, they need to-

- They might not say

that they- - I don't think

they care about that at all.

- They don't care about it right now.

I think it's places - I think they're surely-

- like Perplexity are experimenting on that more.

- [Lex] Oh, interesting. Yeah, for sure.

- Like Perplexity, Google, Meta care about this.

I think OpenAI and Anthropic are purely laser-focused on-

- AGI. - Yeah, agents and AGI.

And if I build AGI, I can make tons of money.

Or I can spend, pay for everything.

And it is just predicated back on the export control thing.

If you think AGI is 5, 10 years away or less,

these labs think it's 2, 3 years away.

Obviously, your actions are,

if you assume they're rational actors,

which they are mostly,

what you do in a two-year AGI versus five-year

versus 10 years is very, very, very different.

- Do you think agents are promising?

We have to talk about this. (chuckles)

This is like the excitement of the year

that agents are gonna rev...

This is the generic hype term

that a lot of business folks are using.

AI agents are gonna revolutionize everything.

- Okay. So, mostly, the term agent is obviously overblown.

We've talked a lot about reinforcement learning

as a way to train for verifiable outcomes.

Agents should mean something that is open-ended

and is solving a task independently on its own,

and able to adapt to uncertainty.

There's a lot of the term agent applied

to things like Apple Intelligence,

which we still don't have after the last WWDC,

which is orchestrating between apps.

And that type of tool use thing is something

that language models can do really well.

Apple Intelligence I suspect will work,

so will come eventually.

It's a closed domain.

It's your messages app integrating with your photos,

with AI in the background.

That will work.

That has been described as an agent

by a lot of software companies to get into the narrative.

- Yeah. - The question is what ways

can we get language models to generalize to new domains

and solve their own problems in real time.

Maybe some tiny amount of training

when they're doing this with fine-tuning themselves

or in context learning,

which is the idea of storing information in a prompt.

And you can use learning algorithms to update that.

And whether or not you believe

that that is gonna actually generalize to things

like me saying, book my trip to go to Austin in two days.

I have X, Y, Z constraints, and actually trusting it.

I think there's a HCI problem coming back for information.

- Well, what's your prediction there?

Because my gut says we're very far away from that.

- I think OpenAI's statement,

I don't know if you've seen the five levels.

Or it's chat is level one,

reasoning is level two, and then agents is level three.

And I think there's a couple more levels,

but it's important to note, we were in chat

for a couple years. - Mm-hmm.

- We just theoretically got to reasoning.

We'll be here for a year or two.

And then, agents, but at the same time,

people can train like approximate capabilities

of the next level,

but the agents are doing things autonomously,

doing things for minutes at a time,

hours at a time, et cetera.

Reasoning is doing things for tens of seconds at a time.

And then, coming back with an output

that I still need to verify and use and try check out.

And the biggest problem is of course,

it's the same thing with manufacturing.

There's the whole six sigma thing.

How many nines do you get,

and then you compound the nines onto each other,

and it's like if you multiply

by the number of steps that are six sigma,

you get to a yield or something.

So, like in semiconductor manufacturing,

tens of thousands of steps.

9999999 is not enough,

because you multiply that many times,

you actually end up with like 60% yield.

- Or zero. - Really low yield. Yeah.

Or zero.

And this is the same thing with agents.

Chaining tasks together each time, LLMs,

even the best LLMs in particularly pretty good benchmarks

don't get 100%. - Yeah.

- They get a little bit below that,

because there is a lot of noise.

And so, how do you get to enough nines?

This is the same thing with self-driving.

We can't have self-driving

because without it being super geofenced like Google's.

And even then, they have a bunch of tele operators

to make sure it doesn't get stuck.

But you can't do that because it doesn't have enough nines.

- And self-driving has quite a lot of structure

because roads have rules.

It's well-defined. There's regulation.

When you're talking about computer use for the open web,

for example, or the open operating system, it's a mess.

So, the possibility, I'm always skeptical

of any system that is tasked with interacting

with the human world,

the open message human world. - That's the thing.

If we can't get intelligence,

that's enough to solve the human world on its own.

We can create infrastructure

like the human operators for Waymo

- Yeah. - over many years

that enable certain workflows.

- There is a company, I don't remember it,

but that's literally their pitches.

Yeah, we're just gonna be the human operator

when agents fail, and you just call us and we fix it.

- Yeah. - It's like an API call

and it's hilarious.

- There's gonna be teleoperation markets

when we get human robots,

which is there's gonna be somebody

around the world that's happy to fix the fact

that it can't finish loading my dishwasher

- Yeah. - when I'm unhappy with it,

but that's just gonna be part of the Tesla service package.

- I'm just imagining an AI agent

talking to another AI agent.

One company has an AI agent

that specializes in helping other AI agents.

- But if you can make things that are good at one step,

- Yeah. - you can stack them together.

So, that's why I'm like, if it takes a long time,

we're gonna build infrastructure that enables it.

You see the operator launch,

they have partnerships with certain websites, with DoorDash,

with OpenTable, - Mm-hmm.

- with things like this.

Those partnerships are gonna let them climb really fast.

Their model's gonna get really good at those things.

It's gonna proof of concept that might be a network effect

where more companies wanna make it easier for AI.

Some companies will be like,

no, let's at put blockers in place.

- Yep. - And this is the story

of the internet we've seen.

We see it now with training data for language models,

where companies are like, no, you have to pay,

- [Lex] Mm-hmm. (Nathan chuckles)

- business working it out.

- That said, I think airlines have a very,

and hotels have high incentive

to make their site work really well, and they usually don't.

If you look at how many clicks it takes

to order a airplane ticket, it's insane.

I don't- - You actually

can't call an American Airlines agent anymore.

They don't have a phone number.

- It's horrible on many, on the interface front and all...

To imagine that agents will be able

to deal with that website, when I, as a human, struggle,

like I have an existential crisis

every time I try to book an airplane ticket,

that I think it's gonna be very extremely difficult

to build a AI agent that's robust

in that way. - But think about it,

United has accepted the Starlink term,

which is they have to provide Starlink for free

and the users are going to love it.

What if one Airline is like, we're gonna take a year

and we're gonna make our website

have white text that works perfectly for the AIs.

Every time anyone asks about an AI flight, they buy

whatever airline it is. (Dylan laughing)

- Or they're just like, here's an API in,

it's only exposed to AI agents

and if anyone queries it, the price is 10% higher.

- [Lex] Yeah.

- And for any flight,

but we'll let you see any of our flights

and you can just book any of them.

Here you go, agent- - And that's-

- Then, it's, oh, and I made 10% higher price.

Awesome. - Yeah.

- And am I willing to say that for like,

hey, book me a flight to see Lex.

And it's like, yeah, whatever.

- Yeah, yeah.

- I think computers and real world

and the open world are really, really messy.

But if you start defining the problem in narrow regions,

people are gonna be able

to create very, very productive things,

and ratchet down cost massively.

Now, crazy things like robotics in the home,

those are gonna be a lot harder to do

just like self-driving.

Because there's just a billion different failure modes.

But agents that can navigate a certain set of websites

and do certain sets of tasks,

or take a photo of your fridge,

or like upload your recipes,

and then it figures out what to order

from Amazon/Whole Foods food delivery.

And that's gonna be pretty quick and easy to do, I think.

So, it's gonna be be a whole range of business outcomes

and it's gonna be tons of optimism

around people can just figure out ways to make money.

- To be clear, these sandboxes already exist in research.

There are people who have built clones

of all the most popular websites of Google, Amazon,

blah, blah, blah, to make it so that there's...

And I mean, OpenAI probably has them internally

to train these things.

It's the same as DeepMind's robotics team

for years has had clusters for robotics,

where you interact with robots fully, remotely.

They just have a lab in London and you send tasks to it,

it arrange the blocks and you do this research.

Obviously, there's texts there that fix stuff.

But we've turned these cranks of automation before.

You go from sandbox to progress,

and then you add one more domain at a time,

and generalize, I think.

In the history of NLP and language processing,

instruction tuning and tasks per language model

used to be one language model did one task.

And then, in the instruction tuning literature,

there's this point where you start adding more

and more tasks together,

where it just starts to generalize to every task.

And we don't know where on this curve we are.

I think for reasoning with this RL

and verifiable domains, we're early,

but we don't know where the point is,

where you just start training on enough domains and poof,

more domains just start working,

and you've crossed the generalization barrier.

# Chapter 19

it arrange the blocks and you do this research.

Obviously, there's texts there that fix stuff.

But we've turned these cranks of automation before.

You go from sandbox to progress,

and then you add one more domain at a time,

and generalize, I think.

In the history of NLP and language processing,

instruction tuning and tasks per language model

used to be one language model did one task.

And then, in the instruction tuning literature,

there's this point where you start adding more

and more tasks together,

where it just starts to generalize to every task.

And we don't know where on this curve we are.

I think for reasoning with this RL

and verifiable domains, we're early,

but we don't know where the point is,

where you just start training on enough domains and poof,

more domains just start working,

and you've crossed the generalization barrier.

- Well, what do you think about the programming context?

So, software engineering.

That's where I personally,

and I know a lot of people interact with AI the most.

- There's a lot of fear

and angst too from current CS students,

but there's also, that is the area

where probably the most AI revenue

and productivity gains have come.

- [Lex] Yeah.

- Whether it be Copilots or Cursor, or what have you,

or just standard ChatGPT.

Like a lot of...

I know very few programmers who don't have ChatGPT

and actually many of them have the $200 tier

because that's what it's so good for.

I think that in that world,

we already see it like SWE-bench,

I don't know if you've looked at the benchmark

made by some Stanford students.

I wouldn't say it's really hard,

but I wouldn't say it's easy either.

I think it takes someone

who's been through at least a few years of CS,

or a couple years of programming to do SWE-bench well.

And the models went from 4% to 60% in like a year.

And where are they gonna go to next year?

It's gonna be higher.

It probably won't be 100%,

'cause again, that nines is really hard to do,

but we're gonna get to some point, where that's,

and then we're gonna need

harder software engineering benchmarks,

and so on and so forth.

But the way that people think of it now

is it's can do code completion easy.

It can do some function generation and I have to review it.

Great.

But really, the software engineering agents,

I think can be done faster sooner than any other agent,

because it is a verifiable domain.

You can always unit test or compile,

and there's many different regions

of it can inspect the whole code base at once,

which no engineer really can.

Only the architects can really think

about this stuff, - Mm-hmm.

- the really senior guys, and they can define stuff,

and then the agent can execute on it.

So, I think software engineering costs

are gonna plummet like crazy.

And one interesting aspect of that

is when software engineering costs are really low,

you get very different markets.

So, in the US, you have all these platform SaaS companies,

Salesforce, and so on and so forth.

In China, no one uses platform SaaS.

Everyone just builds their own stack,

because software engineering is much cheaper in China,

and partially because people,

number of STEM graduates, et cetera.

So, STEM. So, it's generally just cheaper to do.

And so, at the same time,

code LLMs have been adopted much less in China,

because the cost of an engineer there is much lower.

But what happens when every company can just invent

their own business logic really cheaply and quickly?

You stop using platform SaaS,

you start building custom-tailored solutions,

you change them really quickly.

Now, all of a sudden,

your business is a little bit more efficient too potentially

because you're not dealing with the hell

that is some random platform SaaS company stuff

not working perfectly and having to adjust workflows,

or random business automation cases

that aren't necessarily AI-required.

It's just logic

that needs to be built that no one has built.

All of these zings can go happen faster.

And so, I think software...

And then, the other domain is like industrial,

chemical, mechanical engineers

suck at coding just generally.

And their tools, like semiconductor engineers,

their tools are 20 years old.

All the tools run on XP,

including ASML lithography tools, run on Windows XP.

And a lot of the analysis happens in Excel.

It's just like, guys,

you guys can move 20 years forward

with all the data you have

and gathered and do a lot better.

It's just you need the engineering skills

for software engineering

to be delivered to the actual domain expert engineer.

So, I think that's the area,

where I'm super, duper bullish

of generally AI creating value.

- The big picture

is that I don't think it's gonna be a cliff.

- Yeah. - We talked to,

I think a really good example

of how growth changes is when Meta added stories.

So, Snapchat was on an exponential,

they added stories, it flatlined.

Software engineers, then up until the right,

AI's gonna come in, it's probably just gonna be flat.

It is not like everyone's gonna lose their job.

It's hard because the supply corrects more slowly.

So, the amount of students is still growing

and that'll correct on a multi-year, like a year delay,

but the amount of jobs will just turn,

and then maybe in 20, 40 years, it'll be well down.

But in the few years,

there'll never gonna be the snap moment,

where it's like software engineers aren't useful.

- I think also the nature

of what it means to be a programmer

and what kind of jobs programmers do changes,

'cause I think there needs

to be a human in the loop of everything you've talked about.

There's a really important human

in that picture of correcting the code,

like fix- - Think more

than the context length. - Yep.

And debugging also,

like debugging by sort of reading the code,

understanding the steering the system, like no, no, no.

You missed the point. Adding more to the prompt.

Kind of like, yes, adding the human-

- Designing the perfect Google button.

Google's famous for having people design buttons

that are so perfect, and it's like how is AI gonna do that?

Is like they could give you all the ideas.

Perfect. Fine. - Yeah.

- That's the thing, you can call it taste.

One thing humans can do is figure out

what other humans enjoy better than AI systems.

That's where the preference, you loading that in.

But ultimately,

humans are the greatest preference generat...

That's where the preference comes from.

- And humans are actually very good at reading

or judging between two things versus,

this goes back to the core

of what RLHF and preference tuning is,

is that it's hard

to generate a good answer for a lot of problems,

but it's easy to see which one is better.

And that's how we're using humans for AI now

is judging which one is better.

And that's what software engineering could look like,

is the PR review, here's a few options, what are the,

like here are some potential pros and cons,

and they're gonna be judges.

- I think the thing I would very much recommend

is people start, programmers start using AI,

and embracing that role of the supervisor of the AI system,

and partner the AI system versus, writing from scratch

or not learning coding at all and just generating stuff.

Because I think there actually has to be a pretty high level

of expertise as a programmer

to be able to manage increasingly intelligent systems.

- I think it's that,

and then becoming a domain expert in something.

- Sure. Yeah. - Right?

Because seriously, if you go look at aerospace

or semiconductors or chemical engineering,

everyone is using really crappy platforms,

really old software.

The job of a data sciences is like a joke in many cases.

In many cases, it's very real,

but it's like bring what the forefront

of human capabilities are to your domain.

And even if the forefront is from the AI,

your domain, you're like at the forefront.

So, it's like you have to be at the forefront of something,

and then leverage the like rising tide

that is AI for everything else.

- Oh, yeah.

There's so many low-hanging fruit everywhere

in terms of where software can help automate a thing

or digitize a thing.

In the legal system...

That's why Doge is exciting.

I got to hang out

with a bunch of the Doge folks, and they...

(Lex chuckles)

I mean, government is so old school,

it's like begging for the modernization of software,

of organizing the data, all this kind of stuff.

In that case, it's by design,

because bureaucracy protects centers of power, and so on.

But software breaks down those barriers,

so it hurts those that are holding onto power,

but ultimately, benefits humanity.

So, there's a bunch of domains of that kind.

One thing we didn't fully finish

talking about is open source.

So, first of all, congrats, you released a new model.

- Yeah. This is the- - Tulu. (chuckles)

- I'll explain what a Tulu is.

- Yeah. - A tulu is a hybrid camel

when you breed a Dromedary with a Bactrian camel.

Back in the early days, after ChatGPT, there was a big wave

of models coming out like Alpaca, Vicuna, et cetera,

that were all named after various mammalian species.

So, Tulu is the brand is multiple years old,

which comes from that. - Mm-hmm.

- And we've been playing at the frontiers

of post-training with open source code.

And this first part of this release was in the fall,

where we've built on Llama's open models,

open-weight models,

and then we add in our fully open code, our fully open data.

There's a popular benchmark that is chat bot arena.

And that's generally the metric

by which how these chat models are evaluated.

And it's humans compare random models

from different organizations.

And if you looked at the leaderboard

in November or December,

among the top 60 models from 10s to 20s of organizations,

none of them had open code or data for just post-training.

Among that, even fewer

or none have pre-training data and code available.

But it's like post-training

is much more accessible at this time.

It's still pretty cheap and you can do it.

And the thing is how high can we push this number,

where people have access to all the code and data.

So, that's the motivation of the project.

We draw in lessons from Llama.

Nvidia had a Nemotron model,

where the recipe for their post-training

was fairly open with some data and a paper.

And it's putting all these together to try

to create a recipe that people

can fine-tune models like GPT-4 to their domain.

- So, to be clear, in the case of Tulu,

maybe you can talk about OLMO 2,

but in the case of Tulu, you're taking Llama 3, 4, 5B.

- Tulu has been a series of recipes for post-training.

So, we've done - Okay.

- multiple models over years. - Okay.

And so, you're open sourcing everything.

- Yeah, if you start with an open-weight-based model,

the whole model technically isn't open source,

because you don't know what Llama put into it,

which is why we have a separate thing that we'll get to.

But it's just getting parts of the pipeline,

where people can zoom in and customize.

I know I hear from startups and businesses,

they're like, okay, I can take this post-training

and try to apply it to my domain.

We talk about verifiers a lot.

We use this idea which is reinforcement learning

with verifiable rewards, RLVR, similar to RLHF.

And we applied it to map.

And the model today, which is we applied it

to the Llama 405b base model from last year.

And we have our other stuff,

we have our instruction tuning and our preference tuning.

But the math thing is interesting,

which is it's easier to improve this math benchmark.

There's a benchmark, M-A-T-H, MATH, all capitals,

tough name when the benchmark,

its name is the area that you're evaluating.

We're researchers, we're not brands, brand strategists.

And this is something

that the DeepSeek paper talked about as well

is at this bigger model,

it's easier to elicit powerful capabilities

with this RL training.

And then, they distill it down

from that big model to the small model.

And this model we released today, we saw the same thing,

is we're AI2, we don't have a ton of compute,

we can't train 405b models all the time.

So, we just did a few runs and they tend to work,

and it's like, it just shows that there's a lot of room

for people to play in these things.

And that's- - And they crushed Llama's

actual release.

They're way better than it. - Yeah.

So, our eval numbers, we have extra months in this,

but our eval numbers are much better

than the Llama instruct model - Mm-hmm.

- that they released.

- And then, you also said better than DeepSeek-V3.

- Yeah. On our eval benchmark.

The most DeepSeek-V3 is really similar.

We have a safety benchmark to understand

if it will say harmful things and things like that.

And that's what draws down most of the way.

It's still like-

- It's like an amalgamation

of multiple benchmarks or what do you mean?

- Yeah, so we have a 10 evaluat...

This is standard practice in post-training

is you choose your evaluations you care about.

In academics, in smaller labs,

you'll have fewer evaluations.

In companies, you'll have a really

one domain that you really care about.

In Frontier Labs, you'll have 10s to 20s,

to maybe even 100 valuations of specific things.

So, we'd choose a representative suite of things

that look like chat, precise instruction following,

which is like respond only in emojis,

just model follow weird things like that.

- Yeah. - Math, code.

And you create a suite like this.

So, safety would be 1 of 10 in that type of suite,

where you have like,

what is the broader community of AI care about?

And for example, in comparison to DeepSeek,

it would be something

like our average eval for our model would be 80,

including safety and similar without.

And DeepSeek would be like 79% average score without safety

and their safety score would bring it down

to like 76- - Oh, so you beat them

even ignoring safety? - Yeah.

So, this is something that internally,

it's like I don't want to win

only by how you shape the eval benchmark.

So, if there's something that's like people may

or may not care about safety in their model,

safety can come downstream,

safety can be when you host the model for an API,

safety is addressed

in a spectrum of locations in AI applications.

So, it's like,

if you wanna say that you have the best recipe,

you can't just gauge it on these things

that some people might not want.

- [Lex] Mm-hmm.

- And this is just, it's like the time of progress.

We benefit if we can release model later,

we have more time to learn new techniques.

Like this RL technique, we had started this in the fall.

It's now really popular reasoning models.

The next thing to do for open source post-training

is to scale up verifiers,

to scale up data to replicate some of DeepSeek's results.

And it's awesome that we have a paper to draw

and that it makes it a lot easier.

And that's the type of things

that is going on among academic

and closed frontier research in AI.

- Since you're pushing open source,

what do you think is the future of it?

Do you think DeepSeek actually changes things

since it's open source or open-weight

or is pushing the open source movement

into the open direction?

- This goes very back to the license discussion.

So, DeepSeek-R1 with a friendly license is a major reset.

So, it's like the first time

that we've had a really clear frontier model

that is open-weights

and with a commercially friendly license

with no restrictions on downstream use cases,

synthetic data, distillation, whatever.

This has never been the case at all

in the history of AI in the last few years since ChatGPT.

There have been models that are off the frontier

or models with weird licenses

that you can't really use them.

- So, isn't Meta's license

pretty much permissible except for five companies?

And there's also...

So, this goes to what open source AI is, which is,

there's also use case restrictions in the Llama license,

which says you can't use it for specific things.

So, if you come from an open source software background,

you would say that that is not an open source license.

- What kind of things are those though?

Are they like...

- At this point, I can't pull them off the top of my head.

But it'll be like- - Like stuff like competitor,

probably. - It used to be

military use was one, - Oh-

- and they removed that for scale.

It'll be like CSAM, like child abuse material

or that's the type of thing that is forbidden there.

But that's enough from an open source background

to say it's not open source license.

And also, the Llama license has this horrible thing,

where you have to name your model Llama if you touch it

to the Llama model. - Mm-hmm.

- So, it's like the branding thing.

So, if a company uses Llama, technically,

the license says that they should say built with Llama

at the bottom of their application.

And from a marketing perspective, that just hurts.

I can suck it up as a researcher, I'm like, oh, it's fine.

It says Llama dash on all of our materials for this release.

But this is why we need truly open models,

which is we don't know DeepSeek-R1's data, but-

- Wait, so you're saying I can't make a cheap copy of Llama

and pretend it's mine,

but I can do this with the Chinese model?

- [Lex] Yeah.

- Yeah. - Hell yeah.

(Nathan and Dylan laughing)

- That's what I'm saying. - Yeah.

# Chapter 20

to say it's not open source license.

And also, the Llama license has this horrible thing,

where you have to name your model Llama if you touch it

to the Llama model. - Mm-hmm.

- So, it's like the branding thing.

So, if a company uses Llama, technically,

the license says that they should say built with Llama

at the bottom of their application.

And from a marketing perspective, that just hurts.

I can suck it up as a researcher, I'm like, oh, it's fine.

It says Llama dash on all of our materials for this release.

But this is why we need truly open models,

which is we don't know DeepSeek-R1's data, but-

- Wait, so you're saying I can't make a cheap copy of Llama

and pretend it's mine,

but I can do this with the Chinese model?

- [Lex] Yeah.

- Yeah. - Hell yeah.

(Nathan and Dylan laughing)

- That's what I'm saying. - Yeah.

- And that's why it's like we want to,

this whole open language models thing, the OLMO thing,

is to try to keep the model where everything is open

with the data as close to the frontier as possible.

So, we're compute-constrained, we're personnel-constrained.

We rely on getting insights from people

like John Schulman tells us to do RL on outputs.

We can make these big jumps,

but it just takes a long time

to push the frontier of open source.

And fundamentally, I would say

that that's because open source AI

does not have the same feedback loops

as open source software.

We talked about open source software for security

also is just because you build something once

and you can reuse it.

If you go into a new company, there's so many benefits.

But if you open source a language model,

you have this data sitting around,

you have this training code, it's not that easy

for someone to come and build on and improve,

'cause you need to spend a lot on compute.

You need to have expertise.

So, until there are feedback loops of open source AI,

it seems mostly an ideological mission.

Like people like Mark Zuckerberg, which is like,

America needs this, and I agree with him,

but in the time where the motivation ideologically is high,

we need to capitalize and build this ecosystem

around what benefits

do you get from seeing the language model data?

And there's not a lot about that.

We're gonna try to launch a demo soon

where you can look at a OLMO model and a query,

and see what pre-training data is similar to it,

which is legally risky and complicated,

but it's like, what does it mean

to see the data that the AI was trained on?

It's hard to parse. It's terabytes of files.

It's like, I don't know what I'm gonna find in there.

But that's what we need to do as an ecosystem

if people want open source AI to be financially useful.

- We didn't really talk about Stargate.

I would love to get your opinion

on what the new administration, the Trump administration,

everything that's doing

that's being done from the America side

and supporting AI infrastructure

and the efforts of the different AI companies.

What do you think about Stargate?

What are we supposed to think about Stargate?

And does Sam have the money?

(Nathan chuckles) - Yeah,

so I think Stargate is a opaque thing.

It definitely doesn't have $500 billion,

doesn't even have $100 billion.

So, what they announced is this $500 billion number,

Larry Ellison, Sam Altman, and Trump said it.

They thanked Trump

and Trump did do some executive actions

that do significantly improve the ability

for this to be built faster.

One of the executive actions you did is on federal land,

you can just basically build data centers in power,

pretty much like that. - Mm-hmm.

- And then, the permitting process is basically gone

or you file after the fact.

So, one of the, again,

like I had a schizo take earlier, another schizo take,

if you've ever been to the Presidio in San Francisco,

beautiful area, you could build a power plant

and a data center there if you wanted to.

Because it is federal land. (Nathan laughing)

It used to be a military base, so.

- It did. - But obviously,

this would piss people off.

It's a good bit. Anyways.

(Nathan and Lex laughing)

Trump has made it much easier to do this generally.

Texas has the only unregulated grid in the nation as well.

- [Lex] Let's go, Texas.

- And so, therefore,

like ERCOT enables people to build faster as well.

In addition, the federal regulations are coming down.

And so, Stargate is predicated,

and this is why that whole show happened.

Now, how they came up

with a $500 billion number is beyond me.

How they came up with $100 billion number

makes sense to some extent.

And there's actually a good table in here

that I would like to show in that Stargate piece that I had.

It's the most recent one. Yeah.

So, anyways, Stargate, it's basically,

it's a table about cost.

There, you passed it already. It's that one.

So, this table is explaining what happens.

So, Stargate is in Abilene, Texas,

the first $100 billion of it.

That site is 2.2 gigawatts of power in,

about 1.8 gigawatts of power consumed.

Per GPU, they have like roughly...

Oracle is already building the first part of this

before Stargate came about.

To be clear, they've been building it for a year.

They tried to rent it to Elon, in fact.

But Elon was like, it's too slow, I need it faster.

So, then he went

and did his Memphis thing. - Mm-hmm.

- And so, OpenAI was able to get it

with this weird joint venture called Stargate.

They initially signed a deal with just Oracle

for the first section of this cluster.

This first section of this cluster

is roughly $5 billion to $6 billion of server spend.

And then, there's another billion or so

of data center spend.

And then, likewise,

if you fill out that entire 1.8 gigawatts

with the next two generations of Nvidia's chips,

GB200, GB300, VR200, and you fill it out completely,

that ends up being roughly $50 billion of server cost.

Plus there's data center cost, plus maintenance cost,

plus operation costs, plus all these things.

And that's where OpenAI

gets to their $100 billion announcement that they had.

Because they talked about 100 billion is phase one.

That's this Abilene, Texas data center.

$100 billion of "total cost of ownership", quote, unquote.

So, it's not CapEx, it's not investment,

it's $100 billion of total cost of ownership.

And then, there will be future phases.

They're looking at other sites

that are even bigger than this 2.2 gigawatts, by the way,

in Texas and elsewhere.

And so, they're not completely ignoring that.

But there is, the number of $100 billion

that they say is for phase one,

which I do think will happen.

They don't even have the money for that.

Furthermore, it's not $100 billion,

it's $50 billion of spend.

And then, $50 billion of operational cost, power, et cetera,

rental pricing, et cetera.

'Cause OpenAI is renting the GPUs

from the Stargate joint venture.

What money do they actually have? SoftBank.

SoftBank is gonna invest,

Oracle's gonna invest, OpenAI is gonna invest.

OpenAI is on the line - Mm-hmm.

- for $19 billion.

Everyone knows that they've only got 6 billion

in their last round and 4 billion in debt.

But there's news of SoftBank

maybe investing 25 billion into OpenAI.

So, that's part of it.

So, 19 billion can come from there.

So, OpenAI does not have the money at all, to be clear.

Ink is not dried on anything.

OpenAI has $0

- Yeah. - for this 50 billion.

And which they're legally obligated

to put 19 billion of CapEx or into the joint venture.

And then, the rest, they're gonna pay

via renting the GPUs from the joint venture.

And then, there's Oracle.

Oracle has a lot of money.

They're building the first section completely.

They were spending for it themselves.

This $6 billion of CapEx, $10 billion of TCO.

And they were gonna do that first section.

They're paying for that.

As far as the rest of the section,

I don't know how much Larry wants to spend.

At any point, he could pull out.

This is, again, this is completely voluntary.

So, at any point,

there's no signed ink on this. - Mm-hmm.

- But he potentially

could contribute tens of billions of dollars, to be clear.

He's got the money, Oracle's got the money.

And then, there's like MGX,

which is the south, the UAE fund,

which technically has $1.5 trillion for investing in AI.

But again, I don't know how real that money is.

And whereas there's no ink signed for this,

SoftBank does not have $25 billion of cash.

They have to sell down their stake in Arm,

which is the leader in CPUs, and they IPO'ed it.

This is obviously what they've always wanted to do.

They just didn't know where they'd redeploy the capital.

Selling down the stake in Arm makes a ton of sense.

So, they can sell that down

and invest in this if they want to

and invest in OpenAI if they want to.

As far as money secured,

the first 100,000 GB200 cluster can be funded.

Everything else after that

- Up in the air. - is up in the air.

Money's coming.

I believe the money will come.

I personally do. (Lex laughing)

- It's a belief. Okay. - It's a belief

that they are gonna release better models

and be able to raise more money,

right? - Yeah, yeah.

But the actual reality is, is that Elon's right,

the money does not exist.

- What is the US government have to do with anything?

What does Trump have to do with everything?

He's just a hype man? - So, Trump is,

he's reducing the regulation so they can build it faster.

And he is allowing them to do it.

Because any investment of this side

is gonna involve antitrust stuff.

So, obviously, he's gonna allow them to do it.

He's gonna enable the regulations

to actually allow to be built.

I don't believe there's any US government dollars

being spent on this though. - Yeah.

So, I think he's also just creating a general vibe

that this regulation will go down

and this is the era of building.

So, if you're a builder, - Yeah.

- you want to create stuff,

you wanna launch stuff, this is the time to do it.

- And so, we've had this 1.8 gigawatt data center

in our data for over a year now,

and we've been sending it to all of our clients,

including many of these companies

that are building the multi gigawatts.

But that is at a level that's not quite,

maybe executives seeing $500 billion, $100 billion,

and then everyone's asking them like...

So, it could spur another, an even faster arms race.

Because there's already an arms race,

but this like 100 billion,

$500 billion number, Trump talking about it on TV.

It could spur the arm race to be even faster

and more investors to flood in and et cetera, et cetera.

So, I think you're right in that sense that OpenAI,

or Trump is championing people are gonna build more

and his actions are gonna let people build more.

- What are you excited

about these several years that are upcoming

in terms of cluster build outs,

in terms of breakthroughs in AI?

Like the best possible future you can imagine

in the next couple years, two, three, four years?

What does that look like?

Just it could be very specific technical things

like breakthroughs on post post-training,

or it could be just size big.

- [Dylan] Yeah, I mean it's-

- Impressive clusters.

- I really enjoy tracking supply chain

and who's involved in what. (Lex laughing)

- Yeah. - I really do.

It's really fun to see the numbers, the cost,

who's building what capacity,

helping them figure out how much capacity they should build,

winning deals, strategic stuff, that's really cool.

I think technologically, there's a lot

around the networking side that really excites me

with optics and electronics getting closer and closer,

whether it be co-packaged optics,

or some sort of forms of new forms of switching.

- This is internal

to a cluster. - Cluster. Yeah.

Also multi-data center training,

people are putting so much fiber between these data centers

and lighting it up with so much bandwidth that there's a lot

of interesting stuff happening on that end.

Telecom has been really boring since 5G,

and now it's like really exciting again on the fiber side.

- Can you educate me a little bit about the speed of things?

So, the speed of memory versus the speed of interconnect,

versus the speed of fiber between data centers?

Are these orders of magnitude different?

Can we, at some point, converge towards a place,

where it all just feels like one computer?

- No, I don't think

that's possible. - Okay. All right. (chuckles)

- It's only gonna get harder to program,

not easier. - Okay.

- It's only gonna get more difficult

and complicated in more layers.

The general image that people

like to have is this hierarchy of memory.

So, on chip is really close.

Localized within the chip, you have registers.

And those are shared between some compute elements,

and then you'll have caches,

which are shared between more compute elements.

Then, you have memory, like HBM or DRAM,

like DDR memory or whatever it is.

And that's shared between the whole chip.

And then, you can have pools of memory

that are shared between many chips.

And then, storage and you keep zoning out.

The access latency across data centers,

across within the data center within a chip differs.

So, you're obviously always,

you're always gonna have different

programming paradigms for this.

It's not gonna be easy.

Programming this stuff is gonna be hard.

Maybe AI can help with programming this.

But the way to think about it is that like,

(Dylan sighs)

there's the more elements you add to a task,

you don't gain, you don't get strong scaling.

If I double the number of chips,

I don't get 2x the performance.

This is just like a reality of computing,

'cause there's inefficiencies.

And there's a lot of interesting work

being done to make it more linear.

Whether it's making the chips

more networked together more tightly

or cool programming models, or cool algorithmic things

that you can do on the model side.

DeepSeek did some of these really cool innovations

because they were limited on interconnect,

but they still needed to parallelize.

All sorts of...

Everyone's always doing stuff.

Google's got a bunch of work

and everyone's got a bunch of work about this.

That stuff is super exciting

on the model and workload and innovation side.

Hardware, solid-state transformers

are interesting for the power side.

There's all sorts of stuff on batteries

and there's all sorts of stuff on...

I think when you look at,

if you look at every layer of the compute stack,

whether it goes from lithography and etch,

all the way to like fabrication, to optics,

to networking, to power, to transformers,

to cooling, to a networking

and you just go on up and up and up and up the stack.

Even air conditioners for data centers are innovating.

There's like copper cables are innovating.

You wouldn't think it, but copper cables are,

there's some innovations happening there

with the density of how you can pack them.

And it's like all of these layers of the stack,

all the way up to the models.

Human progress is at a pace that's never been seen before.

- I'm just imagining you sitting back in a layer somewhere

with screens everywhere, just monitoring the supply chain

where all these clusters,

all the information you're gathering.

You do incredible- - There's a big team.

There's a big team.

- Yeah. (laughs)

You do quite incredible work with SemiAnalysis.

Just keeping your finger on the pulse

of human civilization in the digital world.

It's pretty cool just to watch, feel that.

- [Dylan] Yeah. Thank you, I guess-

- Feel all of us doing shit, epic shit.

- [Dylan] Feel the AGI. (Lex laughing)

- From meme to reality.

What Nathan, is there breakthroughs

that you're looking forward to potentially?

- I had a while to think about this while listening

to Dylan's beautiful response. (Dylan laughing)

- He did listen to me. He was so-

- No, I knew this was coming.

And it's like, realistically, training models is very fun

because there's so much low-hanging fruit.

And the thing that makes my job entertaining,

I train models, I write analysis

about what's happening with models, and it's fun

because there is obviously so much more progress to be had.

And the real motivation why I do this

somewhere where I can share things is that there's just,

I don't trust people that are like,

"Trust me, bro, we're gonna make AI good."

It's like we're the ones that it's like, we're gonna do it

and you can trust us and we're just gonna have all the AI,

and it's just I would like a future,

where more people have a say

in what AI is and can understand it.

And it's a little bit less fun,

that it's not a like positive thing of like,

this is just all really fun.

Training models is fun and bring people in is fun,

but it's really like AI, if it is going

to be the most powerful technology of my lifetime,

it's like, we need to have a lot of people involved

in making that and...

- Making it open (Nathan chuckles)

helps with that,

as successful as possible, as open as possible, yeah.

- In my read of the last few years

is that more openness would help the AI ecosystem

in terms of having more people understand what's going on,

whether that's researchers from non-AI fields

# Chapter 21

It's like we're the ones that it's like, we're gonna do it

and you can trust us and we're just gonna have all the AI,

and it's just I would like a future,

where more people have a say

in what AI is and can understand it.

And it's a little bit less fun,

that it's not a like positive thing of like,

this is just all really fun.

Training models is fun and bring people in is fun,

but it's really like AI, if it is going

to be the most powerful technology of my lifetime,

it's like, we need to have a lot of people involved

in making that and...

- Making it open (Nathan chuckles)

helps with that,

as successful as possible, as open as possible, yeah.

- In my read of the last few years

is that more openness would help the AI ecosystem

in terms of having more people understand what's going on,

whether that's researchers from non-AI fields

to governments, to everything.

It doesn't mean that openness will always be the answer.

I think then it'll reassess of like,

what is the biggest problem facing AI

and tack on a different angle

to the wild ride that we're on.

- And for me, just from even the user experience,

anytime you have the, like Karpathy said,

the aha moments, like the magic,

like seeing the reasoning, the chain of thought,

it's like there's something really

just fundamentally beautiful about that.

It's putting a mirror to ourselves and seeing like, oh shit.

It is solving intelligence

as the cliche goal of these companies is.

And you get to understand why we humans are special.

The intelligence within us is special.

And for now also, why we're special in terms of,

we seem to be conscious in the AI systems for now aren't,

and we get to solve, we get to explore that mystery.

So, it's just really cool

to get to explore these questions that I don't think,

I would've never imagined would be even possible

back when sort of just watching with excitement

the Deep Blue beat Kasparov.

I wouldn't have ever thought

this kind of AI would be possible in my lifetime.

It's like this is really feels like AI.

- Yeah. (chuckles) - It's incredible.

- I started with AI of learning to fly a silly quadrotor.

It's like learning to fly

and it just like, it learned to fly up,

it would hit the ceiling and stop and catch it.

It's like, okay,

that is really stupid compared to what's going on now.

- And now, you could probably, with natural language,

tell it to learn to fly

and it's going to generate the control algorithm

required to do that. (laughs) - Probably.

There's low level blockers.

We have to do some weird stuff for that,

- Yeah, for sure. - but you can,

you definitely can. - It's back

to our robotics conversation, yeah.

When you have to interact

in the actual physical world, that's hard.

What gives you hope about the future of human civilization?

Looking into the next 10 years, 100 years, 1,000 years,

how long you think we'll make it?

You think we've got

1,000 years? - I think humans

will definitely be around in 1,000 years.

I think there's ways that very bad things could happen.

There'll be way fewer humans,

but humans are very good at surviving.

There's been a lot of things that that is true.

I don't think they're necessarily,

we're good at long-term credit assignment of risk,

but when the risk becomes immediate,

we tend to figure things out,

- Oh yeah. - and for that reason,

I am like, there's physical constraints

to things like AGI hyper,

like recursive improvement to kill us all type stuff

for physical reasons,

and for how humans have figured things out before,

I'm not too worried about it.

AI takeover.

There are other international things that are worrying,

but there's just fundamental human goodness

and trying to amplify that, and we're on a tenuous time.

And if you look at humanity as a whole,

there's been times where things go backwards,

there's times when things don't happen at all.

And we're on a,

what should be very positive trajectory right now.

- Yeah, there seems to be progress, but just with power,

there's spikes of human suffering,

and we wanna try to minimize the amount of spikes.

- Generally, humanity is gonna suffer a lot less.

I'm very optimistic about that.

I do worry of techno fascism type stuff arising

as AI becomes more and more prevalent and powerful,

and those who control it can do more and more.

Maybe it doesn't kill us all,

but at some point, every very powerful human

is gonna wanna brain computer interface,

so that they can interact with the AGI,

and all of its advantages in many more way,

and merge its mind with sort of like,

and its capabilities or that person's capabilities

can leverage those much better than anyone else,

and therefore be, it won't be one person rule them all,

but it will be...

The thing I worry about is it'll be like few people,

hundreds, thousands, tens of thousands,

maybe millions of people rule whoever's left,

and the economy around it.

And that's the thing that's probably more worrisome

is human machine amalgamations.

This enables an individual human

to have more impact on the world.

And that impact can be both positive and negative.

Generally, humans have positive impacts on the world,

at least societally,

but it's possible for individual humans

to have such negative impacts.

And AGI, at least as I think the labs define it,

which is not a runaway sentient thing,

but rather just something that can do a lot

of tasks really efficiently, amplifies the capabilities

of someone causing extreme damage.

But for the most part,

I think it'll be used for profit-seeking motives,

which will increase the abundance and supply of things.

and therefore reduce suffering.

(Lex laughing)

- Yeah. - That's the goal.

- Scrolling on a timeline, (Nathan laughing)

just drowning in dopamine- - Crawling stasis.

- That is- - Scrolling holds

the status quo of the world.

- That is a positive outcome (Nathan and Lex laughing)

is like, if I have food tubes - Yeah.

- and I'm scrolling and I'm happy,

that's a positive outcome.

(group laughing)

- While expanding out into the cosmos.

Well, this is a fun time to be alive.

And thank you for pushing the forefront

of what is possible in humans.

And thank you for talking today. This was fun.

- Thanks for having us. - Thanks for having us.

- Thanks for listening

to this conversation with Dylan Patel and Nathan Lambert.

To support this podcast,

please check out our sponsors in the description.

And now, let me leave you some words from Richard Feynman.

"For a successful technology, reality must take precedence

over public relations, for nature cannot be fooled."

Thank you for listening and hope to see you next time.

