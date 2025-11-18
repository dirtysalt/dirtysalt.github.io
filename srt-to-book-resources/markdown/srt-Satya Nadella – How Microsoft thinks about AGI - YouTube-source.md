# Chapter 1

Maybe after the Industrial Revolution, this is the biggest thing.

But at the same time, I'm a little grounded in the fact that this is still early innings.

If you're a model company, you may have a winner's curse.

You may have done all the hard work

done unbelievable innovation, except it's kind of like one copy away from that being commoditized.

We didn't want to just be a host star for one company and have just a massive book of business with one customer.

That- that's not a business.

You can't build an infrastructure that's optimized for one model.

If you do that, you're one tweak away from some MoE

like, breakthrough that happens when your entire network topology goes out of the window.

Then that's a scary thing.

Our business, which today is an end user tools business

will become essentially an infrastructure business in support of agents doing work.

The thing that you have to think through is not what you do in the next five years

but what do you do for the next 50?

Today, we are interviewing Satya Nadella, we being me and Dilin Patel

who is founder of SemiAnalysis.

Satya, welcome.

Thank you.

It's great.

Thanks for coming over to Atlanta.

Yeah.

Thank you for giving us the tour of

uh, the new facility.

It's been really cool to see.

Absolutely.

Satya and Scott Guthrie, Microsoft's EVP of Cloud and AI

give us a tour of their brand new Fairwater 2 data center

the current most powerful in the world.

We try to 10X the training capacity every 18 to 24 months.

And so this would be effectively a 10X increase

10X from what GPT-5 was trained with.

And so to put it in perspective, the number of optics

the network optics in this building, is almost as much as all of Azure across all our data centers two and a half years ago.

It's kind of, what, five million network connections.

You've got all this bandwidth between different sites in the region and between the two regions.

So is this like a big bet on scaling in the future that you anticipate in the future there's gonna be some huge model that needs to require two whole different regions to train?

Uh- The goal is to be able to kind of aggregate these FLOPs for a large training job

and then put these things together across sites.

Right.

And the reality is, you'll use it for

uh, training  and then you'll use it for data gen

you'll use it for inference in all sort of ways.

Yeah.

It's not like it's going to be used only for one workload forever.

Fairwater 4, which you're going to see under construction nearby- Mm-hmm.

.

..

yeah, will also be on that one peta- petabits network.

Yep.

So that we can actually link the two at a very high rate.

And then basically, we do the AI WAN connecting to Milwaukee

where we have multiple other Fairwaters being built.

Literally, you can see the- the model parallelism and the data parallelism.

And it's kind of built for, um

essentially the training jobs, the pods, the super pods

across this campus.

And then with the WAN, you can go to the Wisconsin data center

and you literally run a training job with all of them getting aggregated.

And what we're seeing right here is this is a cell with no servers in it yet

no racks.

How many, uh, racks are in a cell?

We think about, uh, we don't necessarily share that per se

but- but we- we.

..

Let me- That's the reason I asked.

 No, no, no.

Uh, you'll see upstairs.

I'll start counting.

I'll start counting.

You can start counting.

We'll let you start counting.

How many cells are there in this building?

That part also I can't tell you.

Division is easy, right?

My god, it's kinda loud.

Are you looking at this like, "Now I see where my money is going"?

 It's kind of like, "I run a software company.

Welcome to the software company.

" How big is the design space once you've decided to use GB200s and NVLINK?

How many other decisions are there to be made?

There is coupling from the model architecture to what is the physical plan- Yeah.

.

..

that's optimized.

And it's also scary in that sense, which is

A, there's gonna be a new chip that will come out.

Yeah.

Which obviously, I mean, you take Vera Rubin Ultra.

I mean, that's gonna have power density that's going to be so different

but with cooling requirements that are going to be so different.

Right.

Right?

So you kind of don't want to just build all to one spec.

So that goes back a little bit to I think the dialogue we'll have

which is you want to be scaling- Yeah.

.

..

in time.

Yeah.

As opposed to scale once- Yeah.

.

.

and then be stuck with it.

Yeah.

When you look at all the past technological transitions

whether it be, you know, railroads or the internet or

you know, replaceable parts, industrialization, uh

the cloud, all of these things, each revolution has gotten much faster in the time it goes from technology discover to ramp- Yeah.

.

.

and pervasiveness through the economy.

Many folks who have been on Dark Ashes podcast believe this is sort of the final

uh, technological revolution or transition, and that this time is very

very different.

Um, and at least so far in the markets

it's sort of, you know, in three years

we've already skyrocketed to, you know, hyperscalers are doing $500 billion of CapEx next year

which is a scale that's un- unmatched to prior revolutions in terms of speed.

And the end state seems to be quite different.

How- how do you.

..

Your- your framing of this seems quite different than sort of the

I would say, the AI bro, who is-  .

..

who is quite, um, you know, AGI is coming.

And, you know, I- I'd like to understand that more.

Yeah, I mean, look, I- I start with the excitement that I also feel for maybe after the Industrial Revolution

this is the biggest thing.

Um, and so therefore, I- I- I- I start with that premise.

Uh, but at the same time, I'm a little grounded in the fact that

uh, this is still early innings.

Uh, we built some very useful things.

We're seeing some great properties.

The scaling laws seem to be working.

Um, and I'm optimistic that they'll continue to work

right?

Some of it is, um, you know

it does require real science breakthroughs, but it's also a lot of engineering and what have you.

But that said, I also sort of take the view that

you know, even what has been happening in the last 70 years of computing

uh, has also been a march, uh

that has helped us move, um, you know

with, as I said, you- you know

I- I like one of the things that Raj Reddy.

..

..

. uh, has as a metaphor for what AI is

right?

He's a, he's a Turing Award winner out of

uh, CMU, um, and he's always .

..

And he had this even pre-AGI, uh

but he had this metaphor of, uh

AI should either be a guardian angel or a cognitive amplifier.

I love that.

Uh, it's a simple way to think about what this is.

Ultimately, what is its u- human utility?

It is going to be a cognitive amplifier

uh, and a guardian angel.

And so if I sort of view it that way

I view it as a tool.

But then you can also go very mystical about it and say

"Well, this is, you know, more than a tool.

It does all these things which only humans did so far.

" But that has been the case with many technologies in the past.

Only humans did a lot of things, and then we add tools that did them.

Mm.

I guess, uh, we don't have to get wrapped up in the definition here

but maybe one way to think about it is like may- maybe it takes five years

10 years, 20 years.

At some point, eventually a machine is producing Satya tokens

right?

And the Microsoft board thinks that Satya tokens are worth a lot.

 How much, how much are you wasting of this

uh-  .

..

of, of, like, economic value by interviewing Satya?

 I could not afford the API cost of Satya tokens.

Um, but so, you know, whatever you wanna call it is that

are the Satya tokens a tool or an agent

whatever, um, right now if you have models that cost on the order of dollars or cents per million tokens

there's just an enormous room for expansion, uh

a margin expansion there where Satya to- a million tokens of Satya are

like, worth a lot.

Um, and where does that margin go

and what level of that margin is Microsoft involved in is the question I have?

So I think, um, in, in some sense this goes back again to essentially what's the

uh, economic growth picture gonna really look like.

Um, what's the firm gonna look like?

What's productivity gonna look like?

Yeah.

And that to me is where, again

if the Industrial Revolution created after, whatever

70 years of diffusion is when you started seeing the economic growth

right?

It took .

..

That's the other thing to remember is, um

even if the tech is diffusing fast, uh

this time around, for true economic growth to appear

it has to sort of diffuse to a point where the work

the work artifact and the workflow has to change.

And so that's kinda one place where I think

uh, the change management required for a corporation to truly change I think is something we shouldn't discount.

So, I think going forward, do humans and the tokens they produce

uh, get higher leverage, right?

Uh, whether it's the Dwarkesh or the Dylan tokens of the future.

I mean, think about the amount of technolo- would you be able to run SemiAnalysis or this podcast without technology?

No chance.

Yeah.

Right?

I mean, the f- scale that you would be able to achieve

no chance.

So the question is what's that scale?

Is it gonna be ten x-ed with something that comes through?

Uh, absolutely.

Uh, and therefore with it you'll ramp to some revenue number

or you'll ramp to some audience number or what have you.

And so that I think is what's going to happen

right?

Yeah.

I mean, the, the point is, uh

that s- whatever, what took 70 years

maybe 150 years for the Industrial Revolution may happen in 20 years

25 years.

That's a better way to f- Like, I would love to compress what happened in 200 years of the Industrial Revolution into 20-year period

if you're lucky.

Mm.

So Microsoft historically has been perhaps, you know

the greatest software company, the largest software as a service company.

You know, you've gone through a transition in the past where you used to sell Windows licenses and discs of Windows or Microsoft

and now you sell, you know, subscriptions to 365 or

um .

..

A- as, as we go from sort of

you know, that transition to wh- where your business is today

um, there's also a transition going after that

right?

Uh, software as a service, incredibly low incremental cost per user.

Uh, there's a lot of R&D, there's a lot of customer acquisition cost.

This is why, not Microsoft, but the SaaS companies have m- underperformed massively in the markets because the cogs of AI is just so high.

Yeah.

And that just completely breaks how these business models work.

H- how do you as a, as

as a, as perhaps the greatest software company

um, software as a service company transition Microsoft to this new age where cogs matters a lot

um, and, and the incremental cost per users is different

right?

Because right now you're charging, "Hey, it's 20 bucks for Copilot.

" Yeah.

So I think that this is a .

..

 it's a great question because in some sense

the business models themselves, I think the levers are gonna remain similar

right?

Which is if I look at the, the

if, if you look at the menu of models

uh, starting from, like, say, consumer all the way

right, there will be some ad unit

uh, there will be some transaction, there will be some device gross margin for somebody who builds an AI device.

Um, uh, there will be subscriptions, consumer and enterprise.

Uh, and then there'll be consumption, right?

So I still think that that's kinda how .

..

Those are all the meters.

To your point, what is a subscription?

Up to now, people like subscriptions because they can budget for them

right?

They are essentially entitlements to some consumption rights that come encapsulated in a subscription.

So that, I think, is what .

..

In some sense it becomes a pricing decision.

Uh, so how much consumption is en- you are entitled to is .

..

If you look at all the coding subscriptions

that's kinda what they are, right?

Yeah.

And they kinda have the pro tier, the standard tier

and what have you.

And so I think that's how the pricing will ha- uh

you know, and the margin structures will get tiered.

Um, the interesting thing is having .

..

At Microsoft, the good news for us is we kinda are in that business

uh, all, in across all those meters.

In fact, at, at a, as a portfolio level

uh, we pretty much have consumption, subscriptions

uh, to all of the other consumer levers as well.

Um, and then I think time will tell which of these models make sense in what categories.

Um, one thing on the SaaS side

since you brought up, which I think a lot about is .

..

Uh, take Office 365 or Microsoft 365.

I mean, man, having a low ARPU is great because h- here's an interesting thing

right?

During the transition from server to cloud, one of the questions we used to ask ourselves is

"Oh my God, if all we did was just basically move the same users who were using

let's call it, our office licenses and our servers at that time

office servers, right, to the cloud.

".

..

and we had cogs, this is going to basically not only shrink our margins

uh, but we'll be fundamentally a non-profitable or even less profitable company.

Except what happened was the move to the cloud expanded the market like crazy

uh, right?

I mean, we sold a few servers in India

didn't sell much.

Whereas in the cloud, suddenly everybody in India also could afford fractionally buying

uh, servers.

The IT cost.

I mean, in fact the biggest thing I had not realized

for example, was the amount of money people were spending buying storage underneath SharePoint.

In fact, EMC's biggest segment may have been storage servers for SharePoint.

All that sort of dropped in the cloud because nobody had to go buy

in fact it was working capital, I mean

basically it was cash flow out, right?

And so it expanded the market massively.

So this AI thing will be that, right?

So if you take coding, um, lit- what we built with GitHub and VSCode and over whatever

decades, uh, suddenly the coding assistant is that big in one year.

And so that, I think, is what's going to happen as well which is the market expands massively.

Mm.

I guess there's a question of the market will expand but will the parts of the revenue that touch Microsoft expand?

So Copilot is an example where if you look

uh, early this year, I think, uh

I guess according to Dylan's numbers, um

the Copilot revenue, GitHub Copilot revenue, was like 500 million or something like that.

And then, uh, there were like no close competitors.

Whereas now you have Claude Code, Cursor

and Copilot with around similar revenue, around a billion.

And then Codex is catching up around 700

800 million.

And so the question is across all the services that Microsoft has access to

what is the advantage that Microsoft's equivalents of Copilot have?

Yeah.

By the way, I love this chart.

You know, I love this chart for so many reasons.

One is we're still on the top.

  Um, second is all these companies that are listed here are all companies that have been born in the last four

five years.

Yeah.

Yeah.

That to me is the best sign, right?

Which is if you have new competitors, new existential problems when you say man who is it now?

Oh, Claude's going to kill you.

Cursor's going to kill you.

Yeah.

It's not boring, right?

So thank God.

Like that means we are in the right direction.

But this is it, right?

The fact that we went from nothing to this scale is the market expansion.

So this is like the cloud-like stuff.

This, uh, fundamentally this category of coding and AI is probably going to be one of the biggest categories

# Chapter 2

Yeah.

By the way, I love this chart.

You know, I love this chart for so many reasons.

One is we're still on the top.

  Um, second is all these companies that are listed here are all companies that have been born in the last four

five years.

Yeah.

Yeah.

That to me is the best sign, right?

Which is if you have new competitors, new existential problems when you say man who is it now?

Oh, Claude's going to kill you.

Cursor's going to kill you.

Yeah.

It's not boring, right?

So thank God.

Like that means we are in the right direction.

But this is it, right?

The fact that we went from nothing to this scale is the market expansion.

So this is like the cloud-like stuff.

This, uh, fundamentally this category of coding and AI is probably going to be one of the biggest categories

right?

It is a software factory category.

Yeah.

In fact it may be bigger than knowledge work.

Yeah.

So I kind of want to keep myself open-minded about

I mean, we want to have tough competition.

I think that's your point- Yeah.

.

.

which I think is a great one.

Uh, but man, like I'm glad we have

we parlayed, uh, what we had into this and now we have to compete.

And so in the compete side, uh

even in the last quarter, we just fin- we did our quarterly announcement

I think we grew from 20 to 26 million subs

right?

So I feel good about our sub growth

uh, and where the direction of travel on that is.

But the more interesting thing that has happened is guess where all the repos of all these other guys

uh, who are generating lots and lots of code go to?

They go to GitHub.

So i- GitHub is at an all-time high in terms of repo creation

PRs, everything.

So that, in some sense, we want to keep that open by the way.

That means we want to have that, right?

Because we don't want to conflate that with our own growth

right?

The, interestingly enough, we're getting one developer joining GitHub a second or something.

Mm.

That is the stat I think.

And then 80% of them just fall into some GitHub Copilot

uh, workflow just because there are.

And by the way many of these things will even use some of our coding

uh, code review agents which are by default on just because you can use it.

So we'll have many, many structural shots at this.

The thing that we're also going to do is what we did with Git

Git, the primitives of GitHub whether starting with Git

to issues, to actions, these are powerful lovely things because they kind of are all built around your repo.

So we want to extend that.

At EA- last week at GitHub Universe that's kind of what we did

right?

So we said Agent HQ was the conceptual thing that we said we are going to build out.

This is where, for example, you have a thing called Mission Control and you go to Mission Control and now I can fire off

sometimes I describe it as the cable TV of all these AI agents

because I'll have essentially packaged into one subscription Codex

Claude, um, you know, cognition stuff

anyone's agents, Grok, all of them will be there.

So I get one package and then I can literally go issue a task

steer them so they'll all be working in their independent branches.

Uh, I can monitor them, uh, so I literally have

because I think that's going to be one of the biggest places of innovation

right?

Because right now I want to be able to use multiple agents

I want to be able to then digest the output of the multiple agents

I want to be able to then keep a ha- a handle on my repo so if there's some- some kind of a heads up display that needs to be built and then for me to quickly steer and triage what the coding agents have generated.

That to me between VSCode, GitHub, and all of these new primitives we'll build

uh, as mission control I think, uh

with a control plane observability, I mean think about everyone who is going to deploy all this

will require a whole host of observability of what agent did what at what time to what code base.

So I feel that's the opportunity, uh

and at the end of the day your point is well taken which is we better be competitive and innovate and if we don't

yes, we'll get toppled but I like the chart at least as long as we're on the top even with competition.

The key point here is sort of that GitHub will keep growing irregardless of whose coding agent wins but that

that market only grows at, you know

call it 10, 15, 20% which is way above GDP.

It's a great compounder but these AI coding agents have grown from you know call it $500 million run rate at the end of last year which was basically just GitHub Copilot to now the current run rate across

you know, GitHub Copilot, Claude Code, Cursor

Cognition, Windsurf, Replit, uh, Codex, OpenAI Codex

that's, that's, that's run rating at five

$6 billion now.

..

. um, for the, for the Q4 of

of this year.

That's a 10X, right?

And, and when you look at, hey

what's the TAM of, of software agents?

Is it, is it the $2 trillion of wages you pay people

or is it, is it, is it something beyond that

uh, because every company in the world will now be able to- Absolutely.

.

.

you know, develop software more?

No question Microsoft takes a slice of that

but you've gone from near 100% or certainly way above 50% to

you know, sub 25% market share in just one year.

What is the sort of confidence that people can get that Microsoft will be- No

no, I mean, there's no.

..

Again, I- it goes back a little bit

Dylan, to sort of there's no birthright here that we should have any confidence other than to say

"Hey, we should go innovate.

" And knowing the, the lucky break we have in some sense is that

uh, this category is gonna be a lot bigger than anything we had high share in.

Let's, let me say it that way

right?

Mm-hmm.

In some sense, you could say, well

we kind of had high share in VS Code.

We had high share in the repos for

with GitHub.

Uh, and that was a good market

but the point is even having a decent share in what is a much more expansive market

right?

I mean, you could say we had a high share in client server

server computing.

We are much lower share than that in hyper-scale

but is it a much bigger business?

By orders of magnitude.

So at least there's existence proof that Microsoft is doing okay

uh, even if our share position has not been as strong as it was

uh, as long as the markets we're competing in are creating more value

uh, and there are multiple winners.

Uh, so I think that's the stuff.

But I w- I, I take your point

that ultimately it all means you have to get competitive

so I watch that every quarter.

And so that's why I think we're.

..

I'm very optimistic that, uh, what we're going to do with GitHub HQ and

uh, or Agent HQ, turning GitHub into a place where all these agents come.

Uh, as I said, we'll have multiple shots on goal on there

right?

It need, it need not be that

hey, some of these guys can succeed along with us

uh, and so it n- doesn't need to be just one winner

uh, and one subscription.

Hmm.

I, I guess the reason to focus on this question is that it's not just about GitHub

but fundamentally about Office and all the other software that Microsoft offers

which is that one vision you could have about how AI proceeds is that

look, the models are c- going to keep being hobbled

and you'll need this direct, visible, um

observability all the time.

And another vision is over time, these models can.

..

now they're doing tasks that take two minutes.

In the future, they'll be doing tasks that.

..

Next they're gonna be doing tasks that take 10

30 minutes.

In the future, maybe they're doing days worth of work autonomously

and then the model companies are charging thousands of dollars maybe for access to

uh, really, a coworker, which could use any UI to communicate with their human and

uh, so forth and migrate between platforms.

So w- if we were getting closer to that

why aren't the model companies that are, uh

just getting more and more profitable the ones that are taking all the margin?

Why is the, the place where the scaffolding happens

which becomes less and less relevant as AIs become more capa- capable

gonna be that important?

And that goes to, you know, Office as it exists now versus coworkers that are just doing knowledge work autonomously.

And so- I think that's a great point.

I mean, I think that's a gr-.

..

I mean, for example, I mean, this is where

you know, does all the m- value migrate just to

uh, the model, um, and, uh

or does the mo- you know, the.

..

does it get split between the scaffolding, um

and, uh, the model and what have you?

I, I think that, uh, time will tell

but my, my fundamental point also is the incentive structure gets clear

right?

Which is if you take, um.

..

let's take, uh, let's take information work

or take even coding.

Um, already, in fact, one of the favorite settings I have

uh, in GitHub Copilot is called Auto

um, right, which will just optimize.

In fact, I buy a subscription, the Auto one will start picking and optimizing for what I am asking it to do

uh, and it could even be fully autonomous

and it could sort of arbitrage the tokens available across multiple models to go get a task done.

So if that is the.

..

that, that mean, that.

..

if you take that argument, the commodity there will be models.

Uh, and especially with open source models

you can pick a checkpoint, and you can take a bunch of your data

and you're seeing it, right?

I think all of us will start u- whether it's from Cursor or from Microsoft

uh, we will start seeing some in-house models even

uh, which will.

..

and then you'll offload most of your, uh

tasks to it.

So, I think that one argument is if you win the scaffolding

uh, which today is dealing with all the hobbling problems or the

uh, the jaggedness of these intelligence problems

which you kind of have to.

Um, if you win that, then you will vertically integrate yourself into the model just because you will have the liquidity of the data and what have you

and there are enough and more checkpoints that are gonna be available.

Uh, that's the other thing, right?

So structurally, I think there will always be an open-source model

uh, that will be fairly capable in the world that you could then use as long as you have something that you can use that

uh, with, which is data, uh

and a scaffolding, right?

So I can make the argument that, oh

my God, uh, if you're a model company

you may be, uh, you may have a winner's curse.

You may have done all the hard work

done unbelievable innovation, except it's kind of like one copy

uh, away from that being commoditized, and then the person who has the data for grounding and context engineering

um, and the liquidity of data can then go take that checkpoint and train it.

So, I think the argument can be made both ways.

Un- unpacking sort of what you said, there's two views of the world

right?

One is that models.

..

there's so many different models out there, open source exists.

There will be differences between the models that will drive some level of

you know, who wins and who doesn't

but the scaffolding is what enables you to win.

Yeah.

The other view is that actually models are the key IP

and yes, we're in a very.

..

everyone's in a tight race, and there's some

you know, "Hey, I can use Anthropic or OpenAI

" and you can see this in the revenue charts

right?

Like OpenAI's revenue started skyrocketing once they finally had a code model similar capabilities to Anthropic

although in different ways.

Um-.

..

th- th- there's a view that, like

the model companies are actually the ones that garner all the margin

right?

Because, you know, if you look across this year

at least on Anthropic, their gross margins on inference went from

you know, well below 40% to north of 60

right- Yeah.

.

.

by the end of the year.

Um, the- these- the margins aren't- Yeah.

.

.

expanding there despite, hey, more Chinese open-source models than ever.

Yeah.

Hey, OpenAI's competitive.

Hey, Google's competitive.

Hey, xGrok is now competitive, right?

All these- all these companies are now competitive.

And yet despite this, the margins have expanded at the model layer significantly.

Yeah.

Um, h- h- how do you think about the.

..

It's a gr- it's a great question.

I mean, it- it- I- I think the- the one thing is perhaps a few years ago people were saying

"Oh, I can just wrap a model and build a successful company.

" Uh, and that, I think, is- probably gotten debunked just because the model capabilities

uh.

..

and the tools used in particular.

But the interesting thing is there's no- like when I look at Office 365

let's take even this little thing we built called Excel Agent.

It's interesting, right?

Excel Agent is not a UI-level wrapper.

It's actually a model that is in the middle tier.

Uh, in this case, because we have all the IP from the- the GPT family

uh, we are taking that and putting it into the core middle tier of the Office system to both teach it what it means to natively understand Excel

everything in it.

So it's not just, hey, I just have a pixel-level understanding.

I have a n- full understanding of all the native artifacts of Excel

uh, both when I see it- like because if you think about it

if I'm going to give it some reasoning task

right, I need to even fix the reasoning mistakes I make.

And so that means I need to both not just see the pixels.

I need to be able to see, oh

I got that formula wrong, and I need to understand that.

And then- so to some degree, that's all being done not at the UI wrapper level with some prompt

but it's being done in the middle tier by teaching it all the tools of Excel

right?

So I'm giving it even- essentially a markdown to teach it the skills of what it means to be a sophisticated Excel user.

So it's a weird thing that- it goes back a little bit to AI brain

right?

Which is you're building not just Excel.

You are now business logic in its traditional sense.

You're taking the Excel business logic in the traditional sense and wrapping essentially a cognitive layer to it using this model which knows how to use the tool.

Mm-hmm.

So in some sense, Excel will come with an analyst bundled in and with all the tools used.

Mm-hmm.

That's the type of stuff that'll get built by everybody.

So even for the model companies, they're allowed to compete

right?

So if they price stuff high, uh

guess what?

If I'm a builder of a tool like this

I'll substitute you.

I may use you for a while, and so as long as there's competition

there's always a winner-take-all thing, right?

If there's going to be one model that is better than everybody else with massive distance

yes, that's a winner take all.

As long as there's gonna be competition where there's multiple models

just like hyperscale competition, and there's an open-source check

uh, there is enough room here, uh

to go build value on top of models.

Mm-hmm.

Uh, but at Microsoft, the way I look at it and say is

uh, we are going to be in the hyperscale business which will support multiple models.

We will have access to OpenAI models for

uh, uh, you know, seven more years which we will innovate on top of

so royalty f- uh, essentially, I think of ourselves as having a frontier-class model

uh, that we can use and innovate on with full

uh, flexibility.

And we'll build our own models, uh

with MAI, um, and- and so we will always have a model level.

And then we'll build these, whether it's in security

whether it's in knowledge work, whether it's in coding

or in signs, we will build our own application scaffolding- Mm-hmm.

.

..

which will be model-forward, right?

Mm-hmm.

It won't be a wrapper on a model

but the model will be wrapped into, uh

the application.

I have so many questions about th- the other things you mentioned.

But before we move on to those topics

um, I still wonder whether this is

like, not forward-looking on AI capabilities, where you're imagining models like they exist today

where, yeah, I can- you have this

like- it takes a screenshot of your screen

but it can't, like, look inside each cell and what the formula is.

And I think the better m- mental model here is

like, look, a human- just imagine that these models actually will be able to actually use a computer as well as a human.

100%, yeah.

And a human knowledge worker who is using Excel can look into the formulas

can, you know, use alternative software, can migrate data between Office 365 and another piece of software if the migration is necessary

et cetera.

So what is- That's kind of what I'm saying.

So what- what- But if that's the case

then the integration with Excel doesn't matter that much- No

no, no.

no, no.

no, no.

because then- And- and don't worry about the Excel integration.

After all, Excel was built as a tool for analysts.

Great.

So whoever is this AI that is an analyst should have tools that they can use.

Uh, that they have a computer, right?

That- that- just the way a human can use a computer

that's their tool.

The- the- the- the tool is the computer.

Right.

Right, so that- so all I'm saying is I'm building an analyst as- as essentially an AI agent

# Chapter 3

100%, yeah.

And a human knowledge worker who is using Excel can look into the formulas

can, you know, use alternative software, can migrate data between Office 365 and another piece of software if the migration is necessary

et cetera.

So what is- That's kind of what I'm saying.

So what- what- But if that's the case

then the integration with Excel doesn't matter that much- No

no, no.

no, no.

no, no.

because then- And- and don't worry about the Excel integration.

After all, Excel was built as a tool for analysts.

Great.

So whoever is this AI that is an analyst should have tools that they can use.

Uh, that they have a computer, right?

That- that- just the way a human can use a computer

that's their tool.

The- the- the- the tool is the computer.

Right.

Right, so that- so all I'm saying is I'm building an analyst as- as essentially an AI agent

uh, which happens to come with a- an a priori knowledge of how to use all of these analytical tools.

Uh, but is- is it something- well

maybe just- just to make sure we're talking about the same thing

um, is it a thing that a hu- like me using Excel as a podcaster.

No, no, no, no.

I'm not proficient in Excel, but like.

..

It'll be an auton- a completely autonomous.

So just imagine I work- like so we should now maybe sort of lay out how I think the future of the company is

right?

Yeah.

Uh, the future of the company would be the tools business which I have a computer.

Yeah.

I use Excel.

And in fact, in the future, I'll even have a copilot.

Right.

Uh, and that copilot will also have agents

right?

That still I am- I- you know, it's still me steering everything.

Yeah.

And everything is coming back.

So that's kind of one world.

Yeah.

Then the second world is the company just literally provisions a computing resource for an AI agent.

Yeah.

And that is working fully autonomously.

Yeah.

That fully autonomous agent will have essentially embodied set of those same tools- Right.

.

..

uh, that are available to it, right?

So this AI tool that comes in also has not just a raw computer

uh, because it's gonna be more token-efficient to use tools to get stuff done.

In fact, I kinda look at it and say our business

which today is an end-user tools business, will become essentially an infrastructure business in support of agents doing work.

Okay.

..

. is another way to think about it

right?

So if one of the things that you'll see us do .

..

In, in, in fact, like, all the stuff we built underneath the M365 still is going to be very relevant.

Uh, you need some place to store it

some place to do archival, some place to do discovery

some place to manage all of these activities

e- even if you're an AI agent.

Mm-hmm.

So that's .

..

So it's kind of a new infrastructure.

S- so just to make sure I understand

you're saying, like, look, theoretically, a future AI that has actual computer use

which is .

..

all these companies are working on, model companies are working on right now

could use, even if it's not partnered with Microsoft or under our umbrella

could use Microsoft software.

But you're saying we're gonna give them .

..

if, if you're working with our infrastructure

we're gonna give you, like, lower-level access that makes it more efficient for you to do the same things you could have otherwise done anyways.

100%.

100%.

I mean, so the entire thing in

in fact, the way th- you know

like, what happened is we had servers

then there was virtualization, and then we had many more servers.

So that's another way to think about this

which is, hey, don't think of this .

..

the tool as the end thing.

What is the entire substrate underneath that tool that humans use?

And that entire substrate is the bootstrap for the AI agent as well because the AI agent needs a computer.

That's kind of one.

Like, you know, so in fact, one of the fascinating things we are seeing a significant amount of growth is all these guys who are doing these o- office artifacts and

and what have you as autonomous agents and so on want to provision Windows 365

right?

They really want to be able to provision a computer for these agents.

Uh, and so .

..

absolutely, and that's where I think we're gonna have essentially an end user computing infrastructure business

which I think is going to just keep growing because guess what?

It's going to grow faster than the number of users.

So in fact, that's kind of one of the other questions people ask me

is, "Hey, what happens to the per-user business?

" At least the early signs may be the way to think about the per-user business is not just per user

it's per agent, and if you sort of say it's per user and per agent

the key is what's the stuff to provision for every agent?

A computer?

Um, a set of security things around it?

An identity around it?

Uh, and all those things, our observability and so on

are the management layers, and that's, I think

all going to get baked into that.

The way to frame it, at least the way I currently think about it

and I'd like to hear your, you know

your view, is that, uh, these model companies are all building environments to- Yep.

.

..

train their models to use Excel- Yep.

.

..

or Amazon shopping or whatever, whatever it is

book flights.

Um, but at the same time, they're also training these models to do migration from .

..

because that, that is probably the most immediate

uh, valuable thing, right?

Converting mainframe-based systems to- Yep.

.

..

standard cloud systems, converting, um, Excel databases into real databases- Yep.

.

.

uh, with SQL.

Yep.

Right?

Or, or converting, um, you know

w- what is done in Word and Excel to something that is more programmatic and more efficient in a classical sense- Absolutely.

.

.

that can actually be done by humans as well.

It's just not cost-effective for the software developer to do that.

That seems to be what everyone is going to do with AI for the next

you know, few years at least to massively drive value.

Um, h- h- how does Microsoft fit into that if the models can utilize the tools themselves to migrate to something?

And yes, Microsoft has, you know, a leadership position in databases and in storage and

and in all these other categories, but the use of

say, a office ecosystem is going to be significantly less just like potentially the use of a mainframe ecosystem could be potentially less.

Now mainframes have grown for the last two decades actually

even though no one talks about them anymore.

They've still grown.

100%.

I agree with that.

How does that, how does that flow forward?

Yeah.

I mean, at the end of the day

this is not about sort of, hey

um, there is going to be a significant amount of time where there's going to be a hybrid world

right?

Because people are gonna be using the tools that are gonna be working with agents that have to use tools

and by the way, they have to communicate with each other.

What's the artifact to generate that then a human needs to see?

So, like, all of these things will be real considerations in any place.

So the outputs, inputs.

So I don't think it'll just be about how I migrate it off

right?

But the bottom line is I have to live in this hybrid world.

So let .

..

but that doesn't fully answer your question because there can be a real new efficient frontier where I stress agents working with agents

uh, and completely optimizing.

Mm-hmm.

And even when agents are working with agents

what are the primitives that are needed?

Uh, do you need a storage system?

Uh, does that storage system need to have e-discovery?

Does that e-discover- uh, do you need to have observability?

Do you need to have an identity system that is going to use multiple models with all having one identity system?

So these are all the core underlying rails we have today for what our office systems or what have you

uh, and that's what I think we will have in the future as well.

You talked about databases, right?

I mean take .

..

you know, man, I would love all of Excel to have a database backend

right?

In fact, I would love for all that to happen immediately.

Mm-hmm.

Uh, and that database is a good database.

I mean, databases in fact will be a big thing that will grow.

Uh, in fact, if I think about all of the office artifacts

uh, being structured better, the ability to do the joins between structured and unstructured better because of the agenting

well, that'll grow the underlying what is infrastructure business.

It happens the consumption of that is all being driven by agents.

You could say all that is just in time generated software by a model company.

That could also be true.

If we .

..

we will be one such model company too.

Uh, and so we will build in .

..

so the competition could be, uh, that we will build a model plus all the infrastructure and provision it

and then there will be competition between a bunch of those folks who can do that.

Hmm.

Um, I guess speaking of model companies

you say, okay, we will also be one of the .

..

not only we'll have the infrastructure, we'll have the model itself.

Right now, Microsoft AI's most recent model that was released two months ago is 36 in Chatbot Arena and there's a q- I mean

you obviously have the IP rights to OpenAI

so there's a question of .

..

..

. first, to the extent you agree w- that l- it seems to be behind

why is that the case?

Especially given the fact that you could, um

you theoretically have the right to just, like

fork OpenAI's mono repo or distill on their models.

Um, y- yeah, es- especially if it's a big part of your strategy that we need to have a leading model company.

Yeah, I mean, f- so first of all

we are g- absolutely going to use the OpenAI models

uh, to the maximum, uh, across all of our products

right?

I mean, that's, I think, the core thing that we're gonna continue to do all the way for the next seven years.

Uh, and not just use it, uh

but then add value to it.

That's kinda w- where the analyst and this Excel agent

and these are all things that we will do where

you know, we'll do r- you know

RL fine-tuning, we'll do some mid-training runs on top of a GPT family where we have unique data assets and build capability.

Um, the MAI model, the way I think we're gonna think about it is the

the good news here, in fact, with the new agreement

is even we can be very, very clear that we're gonna build a world-class superintelligence team and go after it with high ambition.

But th- at the same time, we're also gonna use this time to be smart about how to use both these things.

So that means we will, on one end

be very product-focused or, on the other end

be very research-focused.

In other words, uh, because we have access

aha, to the GPT family, the last thing I don't want to do is use my flops in a way that is just duplicative and doesn't add much value.

So I want to be able to take

uh, the flops that we use to generate a GPT family and maximize its value while my MAI flops are being used for.

..

Let's take the image model that we launched

which I think this launched, uh, is a number nine in the

uh, image arena.

You know, we're using it, you know

both for cost optimization.

It's on Copilot, it's in Bing, and we're gonna use that.

We have a, a audio model in Copilot

which really it's got personality and what have you.

We optimized it for our product.

So we will do those.

Even on the LM arena, we started on the text one

I think it was, it debuted at night 13.

And by the way, it was v- it was done only on

whatever, 15,000, uh, H100s?

And so it was a very small model.

And, uh, so it was, again

to prove out, uh, the core capability

the instruction-following and everything else, which b- you know

we wanted to make sure we can match what was state-of-the-art.

And so that shows us, given scaling laws

what we are capable of doing if it gave more flops to it

right?

So the next thing we will do is an omni model where we will take sort of the work we have done in audio

what we have done in image, and what we have done in text.

That'll be the next pit stop on the MAI side.

So when I think about the MAI roadmap

we're gonna build a first-class superintelligence team.

We are gonna continue to drop and do on

in the open some of these models.

They will either be in our products being used because they're going to be latency-friendly

cogs-friendly, or what have you, or they'll have some special capability.

And we will do real research in order to be ready for some next five

six, seven, eight brea- breakthroughs, uh

that are all needed on this march towards superintelligence.

So I think that's.

..

And while exploiting the advantage we have of having the GPT family that we can work on top of as well.

Mm-hmm.

S- say we roll forward seven years, uh

you no longer have access to OpenAI models.

What does one get confidence, or what does Microsoft do to make sure they are leading or have a leading AI lab

right?

Today, you know, it's, it's all OpenAI has developed many of the breakthroughs

whether it be scaling or reasoning, or Google's developed all the breakthroughs like Transformers.

Uh, but, but it- it is also a big talent game

right?

You know, you've seen Meta spend, you know

north of $20 billion on talent, right?

Uh, you've seen Anthropic pr- uh, poach the entire Blueshift reasoning team from Google last year.

You've seen Meta poach a large reasoning and post-training team from Google more recently.

These, these sorts of talent wars are very capital-intensive.

They're the ones that, you know, arguably

you know, if you're spending $100 billion on infrastructure

you should also spend, you know, X amount of money on

on the people using the infrastructure so that they're more efficiently making these new breakthroughs.

What, what confidence can one get that

you know, hey, Microsoft will have a team that's world-class that can make these breakthroughs?

And, you know, once you decide to turn on the money faucet

you know, you're, you're being a bit capital-efficient right now

which is, which is smart, it seems

uh, to not waste money d- doing duplicative work.

But once you decide you need to, you know

how, how can one say, "Oh, yeah

now you can shoot up to, we're the top five model"?

Well, look, I mean, at the e- eh

the end of the day, we are gonna build a world-class team

and we, uh, already have a world-class team that's beginning to be sort of a sample

right?

With Moustafa coming in, we have Karen

we have Amar Subramanian who did a l- lot of the post-training at Gemini

Tufai, who's at Microsoft, Nando, who did a lot of the multimedia s- work at DeepMind is there.

And so we're gonna build a world-class team.

And in fact, I think later this week

even Moustafa published some, you know, a little more clarity on what our lab is going to go do.

Um, I think the thing that I want

uh, the world to know, perhaps, uh

is we are gonna build the infrastructure that'll support multiple models.

Uh, you know, uh, we.

..

Because from a hyperscale perspective, we wanna build the most scaled infrastructure fleet that's capable of supporting all the models the world needs

whether it's from open source or whether it's obviously from OpenAI and others.

And so that's kinda one job.

..

. second is in our own model capability

we will absolutely use the OpenAI model in our products

and we'll start building our own models.

And we may, like in- in GitHub Copilot

Anthropic is used, so we will even have other frontier models that are gonna be wrapped into our products as well.

So, I think that that's kind of how at least each time

at the end of the day, the eval of the product as it meets a particular task or a job is what matters.

And we'll sort of back from there into the vertical integration needed

uh, knowing that as long as you're a service

you know, you're serving the market well with the product

you can always cost optimize.

Mm.

Th- th- there's a question going forward.

So right now, we have models that have this distinction between training an inference

and one could argue that there's, like

a s- smaller and smaller difference between the different models.

Um, going forward, if you're really expecting something like human-level intelligence

humans learn on the job.

H- you know, if you think about your last 30 years

wha- what makes Satya tokens so valuable?

It's the last 30 years of wisdom and experience you've gained at Microsoft.

Um, and w- we will eventually have models

if they get to human level, which will have this ability to continuously learn on the job

and that will drive so much value to the model company that is ahead

at least in my view.

Because you have copies of one model broadly deployed through the economy

learning how to do every single job, and unlike humans

they can amalgamate their learnings to that model.

So, there's this sort of continuous learning sort of exponential feedback loop

um, which almost looks like a sort of intelligence explosion.

Uh, if that happens and Microsoft isn't the leading model company by that time

doesn't then the s- uh, you know

you were saying, well, we substitute one model for another

et cetera, matter less, 'cause it's just

like, this one model knows how to do every single job of the economy.

The other long tail don't.

Yeah.

No, I think that your point about if there's one model that is the only model that's most broadly deployed in the world and it sees all the data and it has continuous learning- Yeah.

.

.

that's game, set, match- Yeah.

.

.

and, you know, you're such sharp, right?

I mean, the- the reality, at least I see

um, is the world, even today, for all the dominance of any one model

it's not the case.

Um, a- is t- take any.

..

take coding.

There's multiple models.

In fact, every day it's less the case

where there is not one model that is getting deployed broadly.

# Chapter 4

et cetera, matter less, 'cause it's just

like, this one model knows how to do every single job of the economy.

The other long tail don't.

Yeah.

No, I think that your point about if there's one model that is the only model that's most broadly deployed in the world and it sees all the data and it has continuous learning- Yeah.

.

.

that's game, set, match- Yeah.

.

.

and, you know, you're such sharp, right?

I mean, the- the reality, at least I see

um, is the world, even today, for all the dominance of any one model

it's not the case.

Um, a- is t- take any.

..

take coding.

There's multiple models.

In fact, every day it's less the case

where there is not one model that is getting deployed broadly.

In fact, there's multiple models that are getting deployed.

It's kind of like databases, right?

You- it's always the thing is, like

hey, can one database be the one that just is used everywhere?

Except it's not.

Uh, there are multiple types of databases that are getting deployed

uh, for different use cases.

So, I think that there is going to be some network effects of continual learning or data

y- you know, I'll call liquidity, that any one model has.

Uh, is it gonna happen in all domains?

I don't think so.

Is it gonna happen in all GOs?

I don't think so.

Is it gonna happen in all segments?

I don't think so.

It'll happen in all categories at the same time?

I don't think so.

So therefore, I feel like the design space is so large

uh, that there's plenty of opportunity.

But your fundamental point is having a capability which is at the infrastructure layer

model layer, and at the scaffolding layer

and then to be able to compose these things not just as a vertical stack

but to be able to compose each thing for what its purpose is

right?

You can't build an infrastructure that's optimized for one model.

If you do that, what if you go fall behind?

In fact, all the infrastructure you built will be a waste

right?

You kind of need to build an infrastructure that's capable of supporting multiple sort of families and lineages of models.

Otherwise, the capital you put in, which is optimized for one model architecture

you- that means you're one tweak away from some MOE-like breakthrough that happens with somebody else and your entire network topology goes out of the window.

Then that's a scary thing, right?

So therefore, you kind of want the infrastructure to support whatever may come

in fact, in your own model family and other model families

and you got to be open.

If you're- if you're serious about the hyperscale business

you got to be serious about that, right?

Um, if you're serious about being a model company

you've got to basically say, "Hey, what are the ways people can actually do things on top of the model so that I can have an ISV ecosystem?

" Unless I'm thinking I'll own every category.

That just can't be.

Then- then you won't have an API business

and that by definition will mean you'll never be

uh, a platform company that's gonna be successfully deployed everywhere

right?

So therefore, the industry structure is s- such that it will

uh, really force people to specialize, and that.

..

in that specialization, a company like Microsoft should compete in each layer by its merits

uh, but not think that this is all about all a road to game

set, match where I just compose vertically all these layers.

That's- that just doesn't happen.

So, according to Dylan's numbers, there's gonna be half a trillion in AI CapEx next year alone

and labs are already spending billions of dollars to snag top researcher talent.

But none of that matters if there's not enough high quality data to train on.

Without the right data, even the most advanced infrastructure and world-class talent won't translate into end value for the user.

That's where Labobox comes in.

Labobox produces high quality data at massive scale

powering any capability that you want your model to have.

It doesn't matter whether you need a coding agent that needs detailed feedback on multi-hour trajectories or a robotics model that needs thousands of samples on everyday tasks

or a voice agent that can also perform real world actions for the user

like booking them a flight.

To be clear, this isn't just off-the-shelf data.

Labobox can design and launch a custom production scale data pipeline in 48 hours

and they can get you tens of thousands of targeted examples in weeks.

Reach out at labobox.

com/dwarkesh.

All right, back to Satya.

So, last year, Microsoft was o- on path to be the largest infrastructure provider

uh, by far.

You were the earliest in '23, so you

you went out there, you acquired all the resources in terms of leasing data centers

starting construction, securing power, everything.

You guys were on pace to beat Amazon in '26 or '27.

Um, but certainly by '28, you were gonna beat them.

Um, since then, you, you know

in, let's call it the second half of last year

Microsoft did this big pause, right, where they let go of a bunch of leasing sites that they were gonna take

which then Google, Meta, um, Amazon in some cases

Oracle, uh, took these sites.

We're sitting in one of the largest data centers in the world

so obviously it's not everything.

You guys are expanding like crazy, uh

but there are sites that you just stopped working on.

Hmm.

Wh- why, why did you do this

right?

Yeah, I mean, the fundamental thing we .

..

This goes back a little bit to what is the hyperscale business all about

right?

Which is one of the key decisions we made was that if you're gonna build out Azure to be fantastic for all sort of stages of AI

uh, from training to mid-training, to data gen

to inference, we just need fungibility, uh

of the fleet.

Um, and, and so that entire thing caused us not to basically go build a

a whole lot of capacity with a particular set of generations.

Uh, because the other thing that you got to realize is having actually for up to now 10Xed every 18 months enough training capacity for the various OpenAI models

uh, we realized that, um, the key is to stay on that path.

But the more important thing is to actually have a balance to not just train

but to be able to serve these models all around the world.

Because at the end of the day, the rate of monetization is what then will allow us to even keep

uh, funding.

And then the infrastructure was going to need us to support

as I said, multiple models and what have you.

So once we said that that's the case

since then, we just course corrected to where .

..

the path we are on, right?

If I look at the path we are on is we are doing a lot more starts now.

Uh, we are also buying up as managed capacity as we can

whether it's to build, whether it's to lease

or even GPUs as a service.

But we are building it for where we see the demand

uh, and the serving needs and our training needs.

And we didn't want to just be a host stop for one company

uh, and have just a massive book of business with one customer.

That, that's not a business, right?

That is sort of, uh, you know

you should be vertically integrated with that company.

Yeah.

Uh, and so given the, the thing that OpenAI was going to be a successful independent company

which is fantastic, right?

I think it makes sense, right?

And even Meta may use third-party capacity, but ultimately they're all going to be first party

uh, for anyone who has large scale

they'll be, you know, they'll be a hyperscaler on their own.

And so to me, was to build out a hyperscale fleet and our own research compute.

Uh, and that's what the adjustment was.

Um, you know, and then, and so I feel very

very good.

Oh, by the way, the other thing is I didn't want to get stuck with massive scale of one generation.

I mean, we just saw the, the GB200s.

I mean, the GB300s are coming, right?

And by the time I get to Vera Rubin

Vera Rubin Ultra, guess what?

The data center is gonna look very different because the power per rack

power per row is gonna be so different.

Uh, the cooling requirements are gonna be so different.

And that, that means I don't want to just go build out like a whole number of gigawatts that are only for a one generation

one family.

And so I think the pacing matters and the fungibility and the location matters.

Uh, the workload diversity matters, customer diversity matters

and that's what we're building towards.

The other thing that we've learned a lot is

um, every AI workload does require not only the AI accelerator

but it requires a whole lot of other things

right?

And in fact, a lot of the margin structure for us will be in those other things.

And so therefore, we want to build out Azure as being fantastic for the long tail of the workloads because that's the hyperscale business while knowing that we've got to be super competitive starting with the bare metal for the highest end training.

And, but that can't crowd out the rest of the business

right?

Because we're not in the business of just doing five contracts with five customers

being their bare metal service.

That's not a, a Microsoft business.

That may be a business for someone else

and that's a good thing.

What we have said is we are in the hyperscale business

which is at the end of the day

a long tail business, uh, for AI workloads.

And in order to do that, we will have some leading bare metal as a service capabilities for a set of models

including our own.

Uh, and that I think is the balance you see.

The, another sort of question that comes around this whole fungibility topic is

okay, it's not where you want it

right?

You would rather have it in a good population center like Atlanta as you're- we're here.

Um, there, there's, there's also the question of like

well, how much does that matter if as the horizon of AI tasks grows?

Well, actually- It's a great question.

.

..

you know, 30 seconds for a reasoning prompt or

you know, 30 minutes for a deep research or

you know, it's gonna be hours for software agents at some point

um, and days and so on and so forth

the time to human interaction.

Why does it matter if it's- Yeah.

.

.

if it's- It's a great, it's a great question.

.

..

uh, location A, B, or C?

That's exactly right.

So in fact, that's one of the other reasons why we want to think about like

hey, what does an Azure region look like and what is the

in fact the networking between Azure regions?

So this is where, uh, I think as the model capabilities evolve

and I think the usage of these tokens

whether it's synchronously or asynchronously evolves, and in fact you don't want to be out of position

right?

Then on top of that, by the way

what are the data residency laws, right?

What, where do I .

..

Like, I mean, the entire EU thing

uh, for us where we literally had to create an EU data boundary

uh, basically meant that you can't just round-trip a call to wherever

even if it's asynchronous.

And so therefore you need to have maybe regional things that are high density and then the power costs and so on.

But you're 100% right in bringing up that the topology as we build out

uh, will have to evolve, one, for tokens per dollar of a watt.

Uh, what are the economics?

So, overlay that with what is the usage pattern

um, usage pattern in terms of synchronous

asynchronous, but also what is the compute storage because the latencies may matter for certain things.

Uh, the storage better be there.

If I have a Cosmos DB close to this for session data or even for an autonomous thing

then that also has to be somewhere close to it

and so on.

So I think that all of those considerations is what will shape

uh, the hyperscale business.

Mm-hmm.

You know, prior to the pause, you were- you were- you're

you know, versus, you know, what we had forecasted for you by '28

you were going to be, like, 12

13 gigawatts.

Yeah.

And now we're at, you know, nine and a half or so

right?

But, you know, something that's even more relevant

right, and it's- it's, you know, I just want you to

like, more concretely state that this is the business you don't want to be in.

But, like, Oracle's going from like one-fifth your size to bigger than you by end of 2027 and while it's not a Microsoft level quality of return on invested capital

right?

They're still making 35% gross margins, right?

So sort of the question is like does it- is it- isn't it- is it- is it

you know, hey, it's not Microsoft's business to maybe do this

but you've created a hyperscaler now- Yeah.

.

.

by refusing this business, by giving away the right of- Look

I- I- .

..

first refusal, et cetera.

I'm not.

..

First of all, I don't, I don't want to take away anything from the success Oracle has had- Yeah.

.

..

uh, in building their business, and I wish them well.

And so the thing that I think I've answered for you is

it didn't make sense for us, uh

to go be a host, uh, for one model company

uh, with limited time horizon RPO.

Let's- Yeah.

Let's just put it that way, right?

The thing that you have to think through is not what you do in the next five years

but what do you do for the next 50?

Uh, because that's kind of what I- we made our set of decisions

um, I feel very good about our OpenAI partnership and what we're doing.

We have a decent book, book of business.

We wish them a lot of success.

In fact, we are buyers even of Oracle capacity

we wish them- Yep.

.

.

success.

But, you know, at this point, I think the industrial logic for what we are trying to do is pretty clear

which is, it's not about, like, chasing.

..

I mean, first of all, I track

by the way, your, uh, things

whe- whether it's the AWS or the Google and ours

which I think is super useful.

Uh, but doesn't mean I got to chase those.

Yeah.

Uh, I have to chase them for not just

uh, the gross margin that they may represent in a period of time.

You know, does Mi- what, what is this book of business that Microsoft uniquely can go clear which makes sense for us to clear?

And that's what we'll do.

I, I, I guess I have a question

even stepping back from this, of, okay

I, I take your point that it's a better business to be in

all else equal, to have a long tail of customers you can have higher margin from

right?

 That when you're serving bare metal to a few labs.

But then there's a question of, okay

which way is the industry evolving?

And so if we believe we're on the path to smarter and smarter AIs

then why isn't the shape of the industry that the OpenAIs and Anthropics and DeepMinds are the platform which the long tail of enterprises are actually doing business with

where they need bare metal, but, like

they are the platform?

What is the long tail that is directly using Azure

um, 'cause, you know, you, you want to use the general cognitive core- But those models are gonna be available on Azure

right?

So any workload that says, "Hey, I want to use

um, you know, some open source model and an OpenAI model

" like, I mean, if you go to Azure Foundry today

you have all these models that you can provision by PTUs

get a Cosmos DB, get a SQL DB

get some storage, get some compute.

That's what a real workload looks like.

A real workload is not just, "Hey

I called in an API call to a model.

" A real workload needs all of these things to go build an app

uh, or instantiate an application.

In fact, the model companies need that

right, to build anything.

It's just not like, "I have a token factory.

" I have to have all of these things.

That's the hyperscale business.

Uh, and it's not even any one model

but all these models.

And so if you want Grok plus, let's say

uh, OpenAI plus an open source model

come to Azure Foundry, provision them, build your application

here is a database.

That's kind of what the business is.

Uh, you, there is a separate business called just selling raw bare metal services to model companies and that's the argument about how much of that business you want to be in and not be in and what is that.

..

It's a very different segment of the business

which, uh, we are in and we also have limits to how much of it is going to crowd out the rest of it.

Uh, but that's kind of at least the way I look at it.

So, so there's, there's sort of two questions here

right?

Like, why, why couldn't you just do both is one

and then the other one is, um

given, you know, our, our estimates on what your capacity is in 2028 is three and a half gigawatts lower

sure, you could have dedicated that to OpenAI training and inference capacity

but you could have also dedicated that to

hey, th- this three and a half gigawatts is actually just running Azure

it's running Microsoft 365, it's running GitHub Copilot.

It doesn't actually.

..

I could have built it and not given it to OpenAI.

Or, or I may want to build it in a different location.

I may want to build it in UAE

I may want to build it in India

I may want to build it in Europe

# Chapter 5

..

It's a very different segment of the business

which, uh, we are in and we also have limits to how much of it is going to crowd out the rest of it.

Uh, but that's kind of at least the way I look at it.

So, so there's, there's sort of two questions here

right?

Like, why, why couldn't you just do both is one

and then the other one is, um

given, you know, our, our estimates on what your capacity is in 2028 is three and a half gigawatts lower

sure, you could have dedicated that to OpenAI training and inference capacity

but you could have also dedicated that to

hey, th- this three and a half gigawatts is actually just running Azure

it's running Microsoft 365, it's running GitHub Copilot.

It doesn't actually.

..

I could have built it and not given it to OpenAI.

Or, or I may want to build it in a different location.

I may want to build it in UAE

I may want to build it in India

I may want to build it in Europe

right?

So one of the other things is, as I said

like, where we have real capacity constraints right now are

given the regulatory needs and the data sovereignty needs

we got to build all over the world.

Uh, it's, first of all, state-side capacity is super important and we're going to build everything.

But one of the things is, when I look out to 2030

uh, I have a sort of a global view of what is Microsoft shape of business by first party and third party.

Third party segmented by the Frontier labs and how much they want versus the inference capacity we want to build for multiple models

um, and our own research compute needs

right?

So that's all what's going into my calculus versus saying

"Hey," uh, I think you're rightfully pointing out the pause

but the pause was not done because we said

"Oh my God, we don't want to build that.

" We realized that, oh, we want to build what we want to build slightly differently

uh, by both workload type as well as geo type and timing as well.

Like, we'll keep ramping up our gigawatts and the question is

at what pace and in what location and in what sort of

how do I write even the Moore's Law on it

right?

Yep.

Which is, do I really want to overbuild three and a half in '27 or do I want to spread that in '27

'28, knowing even.

..

One of the biggest learnings we had even with NVIDIA is their pace increased

uh, in terms of their model mi- I mean

their migrations.

So that was a-.

..

a big factor.

I didn't want to go get stuck for four years

five years of depreciation on one, uh

generation.

And I wanted to just basically buy like

in fact, Jensen's a- advice to me was two things.

One is, "Hey, get on the speed of light execution.

" That's why I think even the execution in this Atlanta data center

I mean, like, in 90 days, right?

Right, between when we get it and do a handoff to a real workload

that's sort of real speed of light execution on their front.

And so I wanted to get good on that.

And then that way, then I'm building this each generation and scaling.

Uh, and then every five years, then you have a much more balanced.

..

So it becomes really literally like a flow

uh, for a n- large-scale industrial operation like this

where you suddenly are not lopsided, where you built up a lot in one time and then you take a ma- massive hiatus because you're stuck with all this

to your point, in one location, which may be great for training

may not be great for inference.

Because I can't serve even if it, like

is all asynchronous, but Europe ain't gonna let me round trip to U- Texas.

So that's all of the things.

How do I rationalize this statement with what you've done over the last few weeks?

You've announced deals with Iris Energy, um

with Nebious, um, and Lambda Labs, and there's a few more coming as well.

Uh, you're, you're going out there and securing capacity that you're renting from the neo-clouds

um, rather than having built it yourself.

What was the, what was- I think it's f- it's fine for us because we now have it

you know, when you have line of sight to demand

which can be so where people are building it

it's great.

In fact, we'll even have, I would say

you know, we will take leases, we will take build-to-suit

we'll take even GPU-as-a-service where we don't have capacity

but we need capacity and someone else has that.

Uh, and by the way, I would even sort of welcome every neo-cloud to just be part of our marketplace.

Uh, because again, g- guess what?

If they, if they go bring their capacity into our marketplace

that customer who comes through Azure will use the neo-cloud

which is a great win for them, and we'll use compute storage databases

all the rest from Azure.

So I'm not at all thinking of this as just a

you know, "Hey, I should just go gobble up all of that myself.

" Hmm.

Um, uh, so you mentioned the co- how

the, you know, you're depreciating this asset that's five

six years, and this is the majority of the

you know, 75% of the TCO of a data center

and Jensen is taking a 75% margin on that.

So what all the hyperscalers are trying to do is develop their own accelerator so that they can reduce this overwhelming cost for

um, uh, equipment to increase their margins.

Yeah.

And then, and then like, you know

when you look at where they are, right?

Google's way ahead of everyone else, right?

They've been doing it for the longest.

They're gonna make something like five to seven million chips

right?

Of their own TPUs.

You look at Amazon, they're trying to make three to five million.

Uh, but when we look at what

you know, Microsoft is, is ordering of their own chips

it's, it's, it's way below that number.

Um, you've had a program for just as long

what's going on with your internal chips?

Yeah.

That's a good question.

So, so the couple of things, one is the thing that is the biggest competitor for any new accelerator is kind of even the previous generation of NVIDIA

right?

I mean, in a fleet, what I'm going to look at is the overall TCO.

So the bar I have even for our own

and which by the way, you know

just looking at the data for Maia 200

which looks great, um, e- e- except that one of the things that we learned even on the compute side

right?

Which is we had a lot of Intel

then we introduced AMD, and then we introduced Cobalt.

And so that's kind of how we scaled it.

And so we have good, um, sort of existence proof of at least in core compute on how to build your own silicon and then manage a fleet where all three are at play in some balance.

Uh, because by the way, even Google's buying NVIDIA and so is

uh, Amazon.

And it makes sense because NVIDIA is innovating and it's the general-purpose thing.

All models run on it, uh, and customer demand is there

because if you build your own vertical thing

you better have your own model, uh

which is, you know, either going to use it for training or inference

and you have to generate your own demand for it or subsidize the demand for it.

So therefore, you want to, uh, make sure

um, you scale it appropriately.

So the way we are going to go do it is

um, have a closed loop between our own MAI models and our silicon because I feel like that's the re- that

that's what gives you the birthright to really do your own silicon

right?

Where you literally have, uh, designed the microarchitecture with what you're doing

and then you keep pace with your own models.

Um, in our case, the good, the good news here is OpenAI has a program

uh, which we have access to.

Um, and so therefore, to think that Microsoft is not going to have something that's sca- What level of access do you have to that?

All of it.

You just get the IP for all of that?

Yeah, yeah.

So the only IP you don't have is a consumer hardware?

That's it.

Oh, wow.

Okay.

 Yeah.

Interesting.

 Yeah.

Oh, and by the way, we gave them a

a bunch of IP as well to bootstrap them

right?

So this is one of the reasons why they had a mass.

..

Because we built all these supercomputers together, uh

rebuilt it for them, and they, uh

benefited from it, rightfully so.

And, uh, and now as they innovate even at the system level

we get access to all of it.

Uh, and, uh, we first wants to in- e- want to instantiate what they build

uh, for them.

Uh, but then we'll extend it.

And so to think that we don't have.

..

And so if anything, the way I

I think about to your question is,  uh

Microsoft wants to be a fantastic, I'll call it

speed of light execution partner for NVIDIA, because quite frankly

that fleet, uh, is life itself.

I'm not worried about.

..

I mean, obviously, Jensen's doing super well with his margins

but the TCO has many dimensions to it

and I want to be great at that TCO.

Uh, on top of that, I want to be able to sort of really work with the OpenAI lineage

uh, and the MAI lineage, and the system design knowing that we have the IP rights on both ends.

 Hmm.

Um, uh, sp- speaking of rights, one thing

you know, you had an interview a couple of days ago

uh, where you said that we have rights to the

the, the new agreement you made with OpenAI

you have rights to, the exclusivity to-.

..

the stateless API calls that OpenAI makes.

And we were sort of confused about if there's any state whatsoever.

I mean, you were just mentioning a second ago that all these complicated workloads that are coming up are gonna require memory and databases and storage and so forth.

And is that now not stateless?

Or ChatGPT is storing stuff, run sessions- No

but that's the reason why.

So the, the thing, the business, the strategic decision we made

and also accommodating for the flexibility OpenAI needed in order to be able to procure compute for.

..

Essentially, think of O- OpenAI having, um

a PasS business and a SaaS business.

SaaS business is ChatGPT, their PasS business is their API.

Yeah.

That API is Azure-exclusive.

The SaaS business, they can run it anywhere.

And they can partner with anyone they want to to build SaaS products?

They, so if they want a partner

and this partner wants to use a s- a stateless API

then Azure is the place where they can get the stateless API.

I- it seems like there's a way for them to make you

you, you know, build the product together and

and it's a stateful thing.

No, even that, they'll have to come to Azure.

Okay.

So if it is any partner.

..

And so, so fundamentally, you know, so l- again

this is done in the spirit of, what is it that we valued as part of our partnership?

And we made sure while at the same time we were good partners to OpenAI

given all the flexibility they need.

So, so for example, Salesforce wants to integrate OpenAI.

It's not through an API.

They actually work together, train a model together

deploy it on, let's say, Amazon now.

Is that, is that allowed?

Or, uh, or do they have to use your- No

for any custom agreement like that, they will have to come run it.

There, there are some few exceptions to US government and so on that we made

but other than that, they'll have to come to Azure.

So as Satya explained, as AI agents get more capable

you're gonna need more and more observability into what they're doing.

You're gonna need to catch them when they're making mistakes

you're gonna need high-level summaries of what they're doing

and you're gonna need a picture of how everything that they're doing fits together.

This is exactly what CodeRabbit provides.

You just make a normal pull request and CodeRabbit automatically reviews the PR.

It generates a summary of changes so you can understand exactly what the PR's author was intending

and it uses the context from your full code base to provide line-by-line feedback on how things could be improved.

This is helpful whether you're viewing a PR from a coworker or an agent.

In either case, CodeRabbit will write up its thoughts and flag any issues so that your teammate or your agent can go fix them.

I've noticed that when I'm coding with agents

CodeRabbit catches a lot of mistakes that the models make by default.

For example, the models have a bad habit of using old versions of libraries.

So in one session, I watched CodeRabbit catch a call to a

an old model, figure out what the new version was

and then suggest that improvement.

Go to coderabbit.

ai/thwarkash to learn more.

Stepping back, a question I have is

you know, when we were t- uh

w- walking back and forth, uh, at the factory

one of the things you were talking about is

you know, uh, Microsoft, you can think of it as a software business

but now it's really becoming an industrial business.

Uh, there's all this capex, there's all this construction.

And if you just look over the last two y- t- um

two years, your sort of capex has

like, tripled.

And maybe you extrapolate that forward, it just actually just becomes this huge industrial

uh, explosion.

U- Other hyperscalers are taking loans, right?

Meta's, Meta's done a $20 billion loan at Louisiana.

They've taken, they've done a corporate loan.

It s- seems clear everyone's free cash flow is going to zero.

 Um, which is, which is, I'm sure Amy is

like, gonna beat you up for-  .

..

for even, if you even try to do that.

But, like, uh, what- what- what's happening?

I mean, I think, uh, I think the structural change

um, is what you're referencing, which I think is massive

right?

Which is, I, I describe it as we are now a

a capital-intensive business and a knowledge-intensive business.

And in fact, we have to use our knowledge to increase the ROIC on the capital spent

right?

Because that's gonna.

..

You know, look, the hardware guys have done a great job

uh, of marketing the Moore's Law, which I think is unbelievable and it's great.

But if you even look, I think some of the stats I even did in my earnings call

which is for a given GPT family, right?

Uh, the improvement, software improvements of really throughput in terms of tokens per dollar per watt that we're able to get

uh, y- you know, quarter over quarter

year over year, is massive.

Uh, right?

So it's 5X, 10X, maybe 40X in some of these cases

right?

Just because how you can optimize.

That's s- sort of knowledge intense- Yeah.

.

..

intensity coming to bring out capital efficiency.

So that, at, at some level, the

that's what we have to master.

What does it mean?

Like, so many people ask me, "What is the difference between

uh, you know, a classic, old-time host

uh, and a hyperscaler?

" It is software.

So yes, it is capital-intensive, but as long as you have systems

know-how, software capability to optimize by workload

by fleet.

That's why I think when, when we say fungibility

there's so much software in it.

It's just not about the fleet, right?

It's kind of the ability to evict a workload

uh, you know, and then schedule another workload.

Can I, like, manage the, that algorithm of scheduling around?

Uh, that is the type of stuff that we have to be world-class at.

And so yes, so I think we'll still remain a software company.

Mm-hmm.

Uh, but yes, this is a different business.

Um, and we're gonna manage.

Look, I think at the end of the day

uh, the cash flow that Microsoft has allows us to have

um, both these arms firing on, you know

uh, well.

Mm.

I- it seems like in the short term

you have more sort of, um, credence on things taking a while

being more jagged.

But in the, maybe in the long term

you think, like, the people who say

talk about AGI and ASI are correct.

Like Sam, Sam will be right, but eventually.

Um, and I, I have a broader question about what makes sense for a hyperscaler to do

given that you have to invest massively in this thing which depreciates over five years.

So s- uh, so if you, if you have 20

40 timelines for the kind of thing that somebody like Sam anticipates in three years

um, you know, what- what is a reasonable thing for you to do in that world?

There needs to be an allocation, uh

to I'll call it research compute.

..

Mm-hmm.

..

. that needs to be done like you did R&D.

Yeah.

Right?

So, that's the best way to even account for it

quite frankly.

We should think of it as just R&D expense.

And you should say, "Hey, what's the research computing or how do you want to scale it?

" Yeah.

Um, and let's even say it's an order of magnitude scale

um, in some period.

Pick your thing.

Yeah.

Is it two years?

Is it 16 months?

What have you, right?

So, that's sort of one piece, which is kind of

that's kind of table stakes.

That's R&D expenses.

And the rest is all demand driven, right?

I mean, ultimately you can, you don't have to build ahead of demand

but you better have a demand, uh

uh, plan, uh, that doesn't go completely off-kilter.

Do you buy.

..

So, these labs are now projecting revenues of 100 billion in '27

'28, uh, and they're projecting, you know

revenue keeps growing at this rate of, like

3X, 2X a year.

So there's lo-.

..

In the marketplace, right, there's all kinds of incentives right now and

and rightfully so, right?

I mean, what, what do you expect an independent lab that is sort of trying to raise money to do

right?

They have to put some numbers out there such that they can actually go raise money so that they can pay their bills for compute- Yeah.

.

.

and what have you.

And it's, and it's good thing.

I mean, someone's going to take some risk and put it in there

and they've shown traction.

Yeah.

It's not like it's all risk without seeing the fact that they've been performing.

# Chapter 6

..

So, these labs are now projecting revenues of 100 billion in '27

'28, uh, and they're projecting, you know

revenue keeps growing at this rate of, like

3X, 2X a year.

So there's lo-.

..

In the marketplace, right, there's all kinds of incentives right now and

and rightfully so, right?

I mean, what, what do you expect an independent lab that is sort of trying to raise money to do

right?

They have to put some numbers out there such that they can actually go raise money so that they can pay their bills for compute- Yeah.

.

.

and what have you.

And it's, and it's good thing.

I mean, someone's going to take some risk and put it in there

and they've shown traction.

Yeah.

It's not like it's all risk without seeing the fact that they've been performing.

Yeah.

Whether it's OpenAI, whether it's Anthropic, so I feel great about what they've done.

Uh,  and we have massive book of business with these chaps.

Yeah.

So, therefore, uh, that's all good.

But overall, ultimately, there's two simple things.

One is you got to allocate for R&D.

You brought up even talent, you got to sp-.

..

Like, the talent for AI- Yeah.

.

..

is at a premium.

You got to spend there.

You got to spend on compute, so in some sense

researcher to GPU  ratios have to be high.

Uh, that is sort of what it takes to be a leading R&D company in this world

uh, and that's something that needs to scale

um, and you have to have a balance sheet that allows you to scale that long before it's conventional wisdom and so on.

So, that's kind of one thing.

But the other is all about sort of knowing how to forecast.

A- as we look across the world, right

America has dominated many tech stacks, right?

Um, the US owns Windows, right, through Microsoft

which is deployed even in China, right?

That's the main operating system.

Um, of course, there's Linux, which is open source

but, you know, Windows is deployed everywhere in China on personal computers.

Um, you look at, you look at Word

it's, it's deployed everywhere.

You look at all these various technologies, it's deployed everywhere.

The thing that is quite unique and, and

and Microsoft and other companies have grown elsewhere

right?

They've built, they're building data centers in Europe and in India and then

and then all these other, you know

in Southeast Asia and in LATAM and Africa

right?

All of these different places you're building capacity

but this seems quite different, right?

You know, t- today the political aspect of technology

of comput-.

..

You know, you know, the, the US administration didn't care about the dot-com bubble

right?

Um, it seems like the US administration as well as every other administration around the world cares a lot about AI.

And the question is, you know, we've.

..

we're in a sort of a bipolar world

at least with US and China, but Europe and

and India and all these other countries are

are saying, "No, actually, we're going to have sovereign AI as well.

" How does Microsoft navigate, you know, the difference of the '90s where it's like there's one country in the world that matters

right?

It's America.

And we do.

..

Our companies sell everywhere, and therefore Microsoft benefits massively

to a world where it is bipolar, where

hey, Microsoft can't just necessarily have the right to win all of Europe or India or

you know, Singapore.

There's actually sovereign AI efforts.

What, what is your thought process here?

That's a great- How do you think about this?

It's, it's, I think, a, a super

 you know, critical, um, piece

which is.

..

Um, I think that the key, key priority for the US tech sector and the US government is to ensure that we not only do leading innovative work

but we also collectively build trust around the world on our tech stack

right?

Because I always say the United States is just an unbelievable place

it's just unique in history, right?

It's 4% of the world's population, 25% of the GDP

and 50% of the market cap, and I think you should think about those ratios and

uh, really,  and reflect on it.

That 50% happens because, quite frankly, the trust the world has in the United States

whether it's its capital markets or whether it's its technology and

and its stewardship of what matters at any given time in terms of leading

uh, sector.

So, if that is broken, uh, then that's not a good day for the United States.

And so, if we start with that

which I think the, you know, President Trump gets

the White House, David Sachs, everyone, uh

really, I think gets it.

Uh, and so therefore, I applaud anything that the United States government and the tech sector jointly does to

quite frankly, for example, put our own capital at risk collectively as an industry in every part of the world

right?

So, I would like, in fact, the USG to take credit for foreign direct investment by American companies all over the world

right?

It's kind of like, uh, least talked about but the best marketing  that the United States should be doing is.

It's not just about all the foreign direct investment coming into the United States

but the most leading sector, which is these AI factories

are all being created all over the world by whom?

By America, uh, and American companies.

And so you start there, and then you even build other agreements around it

which are around their continuity, their legitimate sovereignty concerns around whether it's data residency

whether it's even what happens, um, uh-.

..

uh, for them to have real agency and guarantees

uh, on privacy and so on.

And so the.

..

In fact, our European commitments, I think

are worth reading, right?

So we made a series of commitments to Europe on how we will really govern our hyperscale investment there

uh, such that really European, uh, Union and the European countries have sovereignty.

We're also building sovereign clouds in, in France and in Germany.

We have something called Sovereign Services on Azure

which literally give people key management services along with confidential computing

including confidential computing in GPUs, which we have done great innovative work with NVIDIA.

Um, and so I think.

..

I feel very, very good about being able to build both technically

and through policy, this trust in the American tech stack.

Mm-hmm.

H- and how do you see this shaking out as

you know, you do have this, uh

network effect with continual learning and things on the model level

maybe you have equivalent things at the hyperscaler level as well

and do you expect that the countries will say

"Look, it's clear that one model or a couple models are the best and so we're gonna use them

but we're gonna have some laws around, well

the weights have to be hosted in our country.

" Or do you expect that there will be

uh, this push to have.

..

it has to be a model trained in our country?

Maybe an analogy here is like people would l- uh

you know, semiconductors are very important to the economy and people would like to have their sort of sovereign semiconductors

but, like, TSMC is just better and so semiconductors are so important to the economy that you will just go to Taiwan and buy the semiconductors.

You have to.

Will it be like that with AI or is there.

..

Um, ultimately, I think what matters is the use of AI in their economy to create economic value

right?

I mean, that's the, uh, the diffusion theory which is ultimately.

..

it's not the leading sector, but it's the ability to use the leading technology to create your own comparative advantage.

Yeah.

Right?

So that, I think, will fundamentally be the core driver.

But that said, they will want continuity of that

right?

So in some sense, that's one of the reasons why I believe there's always going to be a check

a little bit, to sort of some of your points on

hey, can this one model have all the runaway deployment?

I- that's why open source is always gonna be there.

There will be, by definition, uh, multiple models.

That'll be one way.

Like, it's kind of the, you know.

..

that's one way for people to sort of demand continuity and not have concentration risk

is another way to say it.

Yeah.

It is, right?

Um, and so you say, "Hey, I want multiple models and then I want an open source.

" So I feel, uh, as long as that's there

every country will feel like, okay, I don't have to worry about deploying the best model and broadly diffusing

because I can always take, uh, what is my data and my liquidity and move it

uh, to another model, whether it's open source or on

uh, from another country or what have you.

Mm-hmm.

So concentration risk, um, and sovereignty, right?

Which is really agency.

Those are the two things I think that'll drive the market structure.

The, the thing about this is that this doesn't exist for semiconductors

right?

Exactly.

You know, all refrigerators, cars have chips made in Taiwan.

It didn't exist until now.

Until now, everyone is now.

..

like, you know, like- Even, even then

right?

America, you know, if Taiwan is cut off

there is, there are no more cars

there are no more refrigerators.

TSMC Arizona is not replacing any real fraction of the production.

Like, they're.

..

it is, it, it.

..

they're.

..

the sovereignty is a bit of like a

a scam if you will, right?

 I mean, it's, it's worthwhile having it

it's important to have it, but it's not a real.

..

it's not real sovereignty, right?

And we're a global economy.

We don't.

..

we.

..

I think it's kind of like Dylan saying

"Hey, at this point, we've not learned anything about sort of

uh, res- what resilience means and what one needs to do

" right?

So it's kind of.

..

Any nation state, including the United States

at this point, will do what it takes to be more self-sufficient on some of these critical supply chains.

So I, as a multinational company, have to think about that as a first-class requirement

right?

If I don't, then I'm not respecting what is in the sort of policy interests of that country long term

right?

And I'm not saying they won't make practical decisions in the short term

right?

Absolutely.

I mean, the globalization can't just be rewound

right?

I mean, all these capital investments cannot be made

uh, in, in a way, at the pace at which.

..

But at the same time, you have to kind of.

..

Like, if I.

..

l- like, think about it, right?

If somebody showed up in Washington and said

"Hey, you know, you know what?

We're not gonna build any semiconductor plants.

" They're gonna be kicked out of the United States.

Um, and, and the same thing is gonna be

uh, true in every other country too.

Uh, and so therefore, I think we have to

as companies, respect what the lessons learned are

um, you know, whether it's, you know

you could say the pandemic woke us up or whatever.

But.

..

and nevertheless, people are saying, "Look, globalization was fantastic.

Uh, it helped supply chains be globalized and be super efficient.

But there's such a thing called resilience and we are happy.

..

you know, we want resilience.

" And so therefore, that feature will get built.

At what pace I think is the point you're making.

It can't be like you can't snap your fingers and say

"All the TSMC plants now are all in Arizona and with all of the capability.

" They're not going to be.

But is there a plan?

There will be a plan.

And should we respect that?

Absolutely.

And so I, I feel that's the world.

..

I wanna meet the world where it is and what it wants to do going forward

as opposed to say, "Hey, we have a point of view that doesn't respect your view.

" Mm-hmm.

So j- just to make sure I understand

th- the idea here is each country will want some kind of data residency

privacy, et cetera, and Microsoft is especially privileged here because you have relationships with these countries

you have expertise in setting up these kinds of sovereign data centers

and.

..

therefore, Microsoft is uniquely fit for a world with

um, more sovereignty requirements?

Yeah, I mean, like, I, I

I don't wanna sort of describe it as somehow we are uniquely privileged.

Yeah.

Uh, I would just say I think of that as a business requirement- I see.

.

.

that we have been doing all the hard work all these decades- Yeah.

.

..

and we will plan to.

And so my answer to Dylan's previous question was

I take these re-.

..

you know, whether it's in the United States

quite frankly, or, or when, you know

when the White House and the USG says

"Hey, we want you to allocate more of your

" I don't know, "wafer starts to, uh

uh, fabs in the US.

" We take that seriously.

Uh, or whether it is data center in the EU boundary

we take that seriously.

Yeah.

So to me, um, ma- respecting what I think are legitimate reasons why countries care about sovereignty- Yeah.

.

.

and building for it as a software and a physical plant is what I

I would say we are going to do.

Mm-hmm.

Uh, a- and as we go to

like, the bipolar world, right?

US, China- Yeah.

.

..

um, there is, there is a lot around

you know, American tech does not.

..

you know, it's not just you versus Amazon

um, or you versus, you know, Anthropic

or you versus Google.

Yeah.

There is a whole host of competi- com- competition.

How does, how does America rebuild the trust?

Great point.

What do you do to rebuild the trust to say

"Actually, no, American companies will be the main provider for you?

" Um, and how do you think about competition with up-and-coming Chinese companies

whether it be, you know, ByteDance and Alibaba

or DeepSeek and Moonshot?

And this is ju- just to add to the question

one concern is, look, we're talking about how AI is becoming this sort of industrial CapEx race

uh, where you're just rapidly having to build quickly across all those supply chain.

When you hear that, at least up until now

you just think about China, right?

This is, like, their comparative advantage.

Very much.

And especially if we're not gonna m- moonshot to ASI next year

but we.

..

it's gonna be this decades of build outs

and infrastructure- It's a great point.

.

.

and so forth, how do you deal with Chinese competition

and are they privileged in that world?

Yeah, so it's a great que-.

..

I mean, in fact, you just made the point of why I think trust in American tech is probably the most important feature.

It's not even the model capability, maybe.

It is, like, can I trust you

the company?

Can I trust you, your country, and its institutions- Mm-hmm.

.

..

to be a long-term supplier may be the thing that wins the world.

I think it's a good note to end on.

Yeah.

Satya, thank you for doing this.

 Thank you so much.

Thank you.

Yes.

Thanks.

Such a pleasure.

Yeah.

Such a pleasure.

It's awesome.

It's like, man, you two guys are

like-  .

..

quite the team.

  Hey, everybody.

I hope you enjoyed that episode.

If you did, the most helpful thing you can do is just share it with other people who you think might enjoy it.

It's also helpful if you leave a rating or a comment on whatever platform you are listening on.

If you're interested in sponsoring the podcast, you can reach out at dwarkesh.

com/advertise.

Otherwise, I'll see you in the next one.

