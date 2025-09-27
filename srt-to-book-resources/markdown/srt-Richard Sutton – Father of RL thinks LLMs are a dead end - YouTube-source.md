# Chapter 1

Today I'm chatting with Richard Sutton,  who is one of the founding fathers of

reinforcement learning and inventor of  many of the main techniques used there,

like TD learning and policy gradient methods. For that, he received this year's Turing Award

which, if you don’t know, is the Nobel Prize  for computer science. Richard, congratulations.

Thank you, Dwarkesh. Thanks for coming on the podcast.

It's my pleasure. First question. My audience and I are

familiar with the LLM way of thinking about AI. Conceptually, what are we missing in terms of

thinking about AI from the RL perspective? It's really quite a different point of view.

It can easily get separated and lose  the ability to talk to each other.

Large language models have become such a big  thing, generative AI in general a big thing.

Our field is subject to bandwagons and  fashions, so we lose track of the basic things.

I consider reinforcement learning to  be basic AI. What is intelligence?

The problem is to understand your world. Reinforcement learning is about understanding

your world, whereas large language  models are about mimicking people,

doing what people say you should do. They're not about figuring out what to do.

You would think that to emulate the trillions  of tokens in the corpus of Internet text,

you would have to build a world model. In fact, these models do seem to have

very robust world models. They're the best world models

we've made to date in AI, right? What do you think is missing?

I would disagree with most  of the things you just said.

To mimic what people say is not really  to build a model of the world at all.

You're mimicking things that have  a model of the world: people.

I don't want to approach the question in an  adversarial way, but I would question the

idea that they have a world model. A world model would enable you

to predict what would happen. They have the ability to predict

what a person would say. They don't have the

ability to predict what will happen. What we want, to quote Alan Turing, is a machine

that can learn from experience, where experience  is the things that actually happen in your life.

You do things, you see what happens,  and that's what you learn from.

The large language models  learn from something else.

They learn from "here's a situation,  and here's what a person did".

Implicitly, the suggestion is you  should do what the person did.

I guess maybe the crux, and I'm curious if  you disagree with this, is that some people

will say that imitation learning has given us a  good prior, or given these models a good prior,

of reasonable ways to approach problems. As we move towards the era of experience, as

you call it, this prior is going to be the basis  on which we teach these models from experience,

because this gives them the opportunity  to get answers right some of the time.

Then on this, you can train them on experience. Do you agree with that perspective?

No. I agree that it's the large  language model perspective.

I don't think it's a good perspective. To be a prior for something,

there has to be a real thing. A prior bit of knowledge should be

the basis for actual knowledge. What is actual  knowledge? There's no definition of actual

knowledge in that large-language framework. What makes an action a good action to take?

You recognize the need for continual learning. If you need to learn continually,

continually means learning during the  normal interaction with the world.

There must be some way during the  normal interaction to tell what's right.

Is there any way to tell in the large language  model setup what's the right thing to say?

You will say something and you will not get  feedback about what the right thing to say is,

because there's no definition of what  the right thing to say is. There's no

goal. If there's no goal, then there's  one thing to say, another thing to say.

There's no right thing to say. There's no  ground truth. You can't have prior knowledge

if you don't have ground truth, because the  prior knowledge is supposed to be a hint or

an initial belief about what the truth is. There  isn't any truth. There's no right thing to say.

In reinforcement learning, there is a right thing  to say, a right thing to do, because the right

thing to do is the thing that gets you reward. We have a definition of what's the right thing

to do, so we can have prior knowledge  or knowledge provided by people about

what the right thing to do is. Then we can check it to see,

because we have a definition of what  the actual right thing to do is.

An even simpler case is when you're  trying to make a model of the world.

When you predict what will happen, you predict  and then you see what happens. There's ground

truth. There's no ground truth in large  language models because you don't have

a prediction about what will happen next. If you say something in your conversation,

the large language models have no prediction  about what the person will say in response

to that or what the response will be. I think they do. You can literally ask them,

"What would you anticipate a user might say  in response?" They’ll have a prediction.

No, they will respond to that question right. But they have no prediction in the substantive

sense that they won't be  surprised by what happens.

If something happens that isn't what you  might say they predicted, they will not

change because an unexpected thing has happened. To learn that, they'd have to make an adjustment.

I think a capability like  this does exist in context.

It's interesting to watch a  model do chain of thought.

Suppose it's trying to solve a math problem. It'll say, "Okay, I'm going to approach this

problem using this approach first." It'll write this out and be like,

"Oh wait, I just realized this is the wrong  conceptual way to approach the problem.

I'm going to restart with another approach." That flexibility does exist in context, right?

Do you have something else in mind  or do you just think that you need

to extend this capability across longer horizons? I'm just saying they don't have in any meaningful

sense a prediction of what will happen next. They will not be surprised by what happens next.

They'll not make any changes if  something happens, based on what happens.

Isn't that literally what  next token prediction is?

Prediction about what's next and  then updating on the surprise?

The next token is what they should  say, what the actions should be.

It's not what the world will give  them in response to what they do.

Let's go back to their lack of a goal. For me, having a goal is

the essence of intelligence. Something is intelligent if it can achieve goals.

I like John McCarthy's definition that  intelligence is the computational part

of the ability to achieve goals. You have to have goals or you're

just a behaving system. You're not anything special,

you're not intelligent. You agree that large language

models don't have goals? No, they have a goal.

What's the goal? Next token prediction.

That's not a goal. It doesn't change  the world. Tokens come at you,

and if you predict them, you don't influence them. Oh yeah. It's not a goal about the external world.

It's not a goal. It's not a substantive goal.  You can't look at a system and say it has a goal

if it's just sitting there predicting and being  happy with itself that it's predicting accurately.

The bigger question I want to understand  is why you don't think doing RL on

top of LLMs is a productive direction. We seem to be able to give these models

the goal of solving difficult math problems. They are in many ways at the very peaks of

human-level in the capacity to solve math  Olympiad-type problems. They got gold at

IMO. So it seems like the model which got  gold at the International Math Olympiad does

have the goal of getting math problems right. Why can't we extend this to different domains?

The math problems are different. Making a  model of the physical world and carrying

out the consequences of mathematical assumptions  or operations, those are very different things.

The empirical world has to be learned. You have to learn the consequences.

Whereas the math is more computational,  it's more like standard planning.

There they can have a goal to find  the proof, and they are in some way

given that goal to find the proof. It's interesting because you wrote

this essay in 2019 titled "The Bitter  Lesson," and this is the most influential

essay, perhaps, in the history of AI. But people have used that as a justification for

scaling up LLMs because, in their view, this is  the one scalable way we have found to pour ungodly

amounts of compute into learning about the world. It's interesting that your perspective is that

the LLMs are not "bitter lesson"-pilled. It's an interesting question whether large

language models are a case of the bitter lesson. They are clearly a way of using massive

computation, things that will scale with  computation up to the limits of the Internet.

But they're also a way of putting in lots of  human knowledge. This is an interesting question.

It's a sociological or industry question. Will they reach the limits of the data and

be superseded by things that can get more data  just from experience rather than from people?

In some ways it's a classic  case of the bitter lesson.

The more human knowledge we put into the  large language models, the better they

can do. So it feels good. Yet, I expect there  to be systems that can learn from experience.

Which could perform much better  and be much more scalable.

In which case, it will be another instance of the  bitter lesson, that the things that used human

knowledge were eventually superseded by things  that just trained from experience and computation.

I guess that doesn't seem like the crux to me. I think those people would also agree that the

overwhelming amount of compute in the future  will come from learning from experience.

They just think that the scaffold or the basis of  that, the thing you'll start with in order to pour

in the compute to do this future experiential  learning or on-the-job learning, will be LLMs.

I still don't understand why this is  the wrong starting point altogether.

Why do we need a whole new architecture to  begin doing experiential, continual learning?

Why can't we start with LLMs to do that? In every case of the bitter lesson you

could start with human knowledge and then do the  scalable things. That's always the case. There's

never any reason why that has to be bad. But in fact, and in practice,

it has always turned out to be bad. People get locked into the human

knowledge approach, and they psychologically…  Now I'm speculating why it is, but this is

what has always happened. They get their lunch eaten

by the methods that are truly scalable. Give me a sense of what the scalable method is.

The scalable method is you learn from experience. You try things, you see what works.

No one has to tell you. First of all, you have a goal.

Without a goal, there's no sense of  right or wrong or better or worse.

Large language models are trying to get by without  having a goal or a sense of better or worse.

That's just exactly starting in the wrong place. Maybe it's interesting to compare this to humans.

In both the case of learning from imitation  versus experience and on the question of goals,

I think there's some interesting analogies. Kids will initially learn from imitation.

You don't think so? No, of course not.

Really? I think kids just watch people. They try to say the same words…

How old are these kids? What  about the first six months?

I think they're imitating things. They're  trying to make their mouth sound the way

they see their mother's mouth sound. Then they'll say the same words without

understanding what they mean. As they get older, the complexity

of the imitation they do increases. You're imitating maybe the skills that

people in your band are using to  hunt down the deer or something.

Then you go into the learning  from experience RL regime.

But I think there's a lot of imitation  learning happening with humans.

It's surprising you can have  such a different point of view.

When I see kids, I see kids just  trying things and waving their

# Chapter 2

by the methods that are truly scalable. Give me a sense of what the scalable method is.

The scalable method is you learn from experience. You try things, you see what works.

No one has to tell you. First of all, you have a goal.

Without a goal, there's no sense of  right or wrong or better or worse.

Large language models are trying to get by without  having a goal or a sense of better or worse.

That's just exactly starting in the wrong place. Maybe it's interesting to compare this to humans.

In both the case of learning from imitation  versus experience and on the question of goals,

I think there's some interesting analogies. Kids will initially learn from imitation.

You don't think so? No, of course not.

Really? I think kids just watch people. They try to say the same words…

How old are these kids? What  about the first six months?

I think they're imitating things. They're  trying to make their mouth sound the way

they see their mother's mouth sound. Then they'll say the same words without

understanding what they mean. As they get older, the complexity

of the imitation they do increases. You're imitating maybe the skills that

people in your band are using to  hunt down the deer or something.

Then you go into the learning  from experience RL regime.

But I think there's a lot of imitation  learning happening with humans.

It's surprising you can have  such a different point of view.

When I see kids, I see kids just  trying things and waving their

hands around and moving their eyes around. There's no imitation for how they move their

eyes around or even the sounds they make. They may want to create the same sounds,

but the actions, the thing that the infant  actually does, there's no targets for that.

There are no examples for that. I agree. That doesn't explain everything infants

do, but I think it guides a learning process. Even an LLM, when it's trying to predict the next

token early in training, it will make a guess. It'll be different from what it actually sees.

In some sense, it's very short-horizon  RL, where it's making this guess,

"I think this token will be this." It's this other thing, similar to how a kid

will try to say a word. It comes out wrong. The large language models are learning

from training data. It's not learning from  experience. It's learning from something that

will never be available during its normal life. There's never any training data that says you

should do this action in normal life. I think this is more of a semantic

distinction. What do you call  school? Is that not training data?

School is much later. Okay,  I shouldn't have said never.

I don’t know, I think I would  even say that about school.

But formal schooling is the exception. But there are phases of learning where

there’s the programming in your biology  early on, you're not that useful.

Then why you exist is to understand the  world and learn how to interact with it.

It seems like a training phase. I agree that then there's a more

gradual… There's not a sharp cutoff  to training to deployment, but there

seems to be this initial training phase right? There's nothing where you have training of what

you should do. There's nothing. You see things  that happen. You're not told what to do. Don't

be difficult. I mean this is obvious. You're literally taught what to do.

This is where the word training  comes from, from humans.

I don't think learning is really about training. I think learning is about learning,

it's about an active process. The child tries things and sees what happens.

We don't think about training when  we think of an infant growing up.

These things are actually rather well understood. If you look at how psychologists think about

learning, there's nothing like imitation. Maybe there are some extreme cases where humans

might do that or appear to do that, but there's  no basic animal learning process called imitation.

There are basic animal learning processes for  prediction and for trial-and-error control.

It's really interesting how sometimes the  hardest things to see are the obvious ones.

It's obvious—if you look at animals and how  they learn, and you look at psychology and our

theories of them—that supervised learning  is not part of the way animals learn.

We don't have examples of desired behavior. What we have are examples of things that happen,

one thing that followed another. We have examples of,

"We did something and there were consequences." But there are no examples of supervised learning.

Supervised learning is not  something that happens in nature.

Even if that were the case with school,  we should forget about it because that's

some special thing that happens in people. It doesn't happen broadly in nature. Squirrels

don't go to school. Squirrels  can learn all about the world.

It's absolutely obvious, I would say, that  supervised learning doesn't happen in animals.

I interviewed this psychologist  and anthropologist, Joseph Henrich,

who has done work about cultural evolution,  basically what distinguishes humans and

how humans pick up knowledge. Why are you trying to distinguish

humans? Humans are animals. What we  have in common is more interesting.

What distinguishes us, we should  be paying less attention to.

We're trying to replicate intelligence. If you  want to understand what it is that enables humans

to go to the moon or to build semiconductors,  I think the thing we want to understand is what

makes that happen. No animal can go

to the moon or make semiconductors. We want to understand what makes humans special.

I like the way you consider that obvious,  because I consider the opposite obvious.

We have to understand how we are animals. If we understood a squirrel, I think we'd

be almost all the way there to  understanding human intelligence.

The language part is just a small veneer on the  surface. This is great. We're finding out the

very different ways that we're thinking. We're  not arguing. We're trying to share our different

ways of thinking with each other. I think argument is useful.

I do want to complete this thought. Joseph Henrich has this interesting

theory about a lot of the skills that humans  have had to master in order to be successful.

We're not talking about the last  thousand years or the last 10,000 years,

but hundreds of thousands of years. The world  is really complicated. It's not possible to

reason through how to, let’s say, hunt  a seal if you're living in the Arctic.

There's this many, many-step, long process of  how to make the bait and how to find the seal,

and then how to process the food in a way  that makes sure you won't get poisoned.

It's not possible to reason through all of that. Over time, there's this larger process of whatever

analogy you want to use—maybe RL, something  else—where culture as a whole has figured out

how to find and kill and eat seals. In his view, what is happening when

this knowledge is transmitted through  generations, is that you have to imitate

your elders in order to learn that skill. You can't think your way through how to

hunt and kill and process a seal. You have to watch other people,

maybe make tweaks and adjustments,  and that's how knowledge accumulates.

The initial step of the cultural  gain has to be imitation.

But maybe you think about it a different way? No, I think about it the same way.

Still, it's a small thing on top of basic  trial-and-error learning, prediction learning.

It's what distinguishes us, perhaps,  from many animals. But we're an animal

first. We were an animal before we had  language and all those other things.

I do think you make a very interesting  point that continual learning is a

capability that most mammals have. I guess all mammals have it.

It's quite interesting that we have something that  all mammals have, but our AI systems don't have.

Whereas the ability to understand math and  solve difficult math problems—depends on how

you define math—is a capability that our  AIs have, but that almost no animal has.

It's quite interesting what ends up being  difficult and what ends up being easy.

Moravec's paradox. That’s right, that’s right.

This alternative paradigm that you're imagining… The experiential paradigm. Let's

lay it out a little bit. It says that experience, action,

sensation—well, sensation, action, reward—this  happens on and on and on for your life.

It says that this is the foundation  and the focus of intelligence.

Intelligence is about taking that  stream and altering the actions to

increase the rewards in the stream. Learning then is from the stream,

and learning is about the stream. That second part is particularly telling.

What you learn, your  knowledge, is about the stream.

Your knowledge is about if you  do some action, what will happen.

Or it's about which events will follow other  events. It's about the stream. The content of

the knowledge is statements about the stream. Because it's a statement about the stream,

you can test it by comparing it to the  stream, and you can learn it continually.

When you're imagining this  future continual learning agent…

They're not "future". Of  course, they exist all the time.

This is what the reinforcement learning  paradigm is, learning from experience.

Yeah, I guess what I meant to  say is a general human-level,

general continual learning agent. What is the  reward function? Is it just predicting the world?

Is it then having a specific effect on it? What would the general reward function be?

The reward function is arbitrary. If you're  playing chess, it's to win the game of chess.

If you're a squirrel, maybe the  reward has to do with getting nuts.

In general, for an animal, you would say the  reward is to avoid pain and to acquire pleasure.

I think there also should be a  component having to do with your

increasing understanding of your environment. That would be sort of an intrinsic motivation.

I see. With this AI, lots of people would want  it to be doing lots of different kinds of things.

It's performing the task people want,  but at the same time, it's learning

about the world from doing that task. Let’s say we get rid of this paradigm

where there's training periods and  then there's deployment periods.

Do we also get rid of this paradigm where there's  the model and then instances of the model or

copies of the model that are doing certain things? How do you think about the fact that we'd

want this thing to be doing different things? We'd want to aggregate the knowledge that it's

gaining from doing those different things. I don't like the word "model"

when used the way you just did. I think a better word would be "the network"

because I think you mean the network. Maybe  there are many networks. Anyway, things would

be learned. You'd have copies and many instances. Sure, you'd want to share knowledge across the

instances. There would be

lots of possibilities for doing that. Today, you have one child grow up and

learn about the world, and then every  new child has to repeat that process.

Whereas with AIs, with a digital intelligence,  you could hope to do it once and then copy it

into the next one as a starting place. This would be a huge savings.

I think it'd be much more important  than trying to learn from people.

I agree that the kind of thing you're  talking about is necessary regardless

of whether you start from LLMs or not. If you want human or animal-level intelligence,

you're going to need this capability. Suppose a human is trying to make a startup.

This is a thing which has a  reward on the order of 10 years.

Once in 10 years you might have an exit  where you get paid out a billion dollars.

But humans have this ability to make intermediate  auxiliary rewards or have some way of…Even when

they have extremely sparse rewards, they  can still make intermediate steps having an

understanding of what the next thing they're  doing leads to this grander goal we have.

How do you imagine such a  process might play out with AIs?

This is something we know very well. The basis of it is temporal difference

learning where the same thing  happens in a less grandiose scale.

When you learn to play chess, you have  the long-term goal of winning the game.

Yet you want to be able to learn from shorter-term  things like taking your opponent's pieces.

You do that by having a value function  which predicts the long-term outcome.

Then if you take the guy's pieces, your  prediction about the long-term outcome is changed.

It goes up, you think you're going to win. Then that increase in your belief immediately

reinforces the move that led to taking the piece. We have this long-term 10-year goal of making a

startup and making a lot of money. When we make progress, we say, "Oh,

I'm more likely to achieve the long-term goal,"  and that rewards the steps along the way.

You also want some ability for  information that you're learning.

One of the things that makes humans quite  different from these LLMs is that if you're

onboarding on a job, you're picking  up so much context and information.

That's what makes you useful at the job. You're learning everything from how your

client has preferences to how  the company works, everything.

Is the bandwidth of information that you  get from a procedure like TD learning high

# Chapter 3

But humans have this ability to make intermediate  auxiliary rewards or have some way of…Even when

they have extremely sparse rewards, they  can still make intermediate steps having an

understanding of what the next thing they're  doing leads to this grander goal we have.

How do you imagine such a  process might play out with AIs?

This is something we know very well. The basis of it is temporal difference

learning where the same thing  happens in a less grandiose scale.

When you learn to play chess, you have  the long-term goal of winning the game.

Yet you want to be able to learn from shorter-term  things like taking your opponent's pieces.

You do that by having a value function  which predicts the long-term outcome.

Then if you take the guy's pieces, your  prediction about the long-term outcome is changed.

It goes up, you think you're going to win. Then that increase in your belief immediately

reinforces the move that led to taking the piece. We have this long-term 10-year goal of making a

startup and making a lot of money. When we make progress, we say, "Oh,

I'm more likely to achieve the long-term goal,"  and that rewards the steps along the way.

You also want some ability for  information that you're learning.

One of the things that makes humans quite  different from these LLMs is that if you're

onboarding on a job, you're picking  up so much context and information.

That's what makes you useful at the job. You're learning everything from how your

client has preferences to how  the company works, everything.

Is the bandwidth of information that you  get from a procedure like TD learning high

enough to have this huge pipe of  context and tacit knowledge that

you need to be picking up in the way  humans do when they're just deployed?

I’m not sure but I think at the crux of this,  the big world hypothesis seems very relevant.

The reason why humans become useful on  the job is because they are encountering

their particular part of the world. It can't have been anticipated and

can't all have been put in in advance. The world is so huge that you can't.

The dream of large language models, as I see  it, is you can teach the agent everything.

It will know everything and won't have to  learn anything online, during its life.

Your examples are all, "Well, really  you have to" because you can teach it,

but there's all the little idiosyncrasies of  the particular life they're leading and the

particular people they're working with and what  they like, as opposed to what average people like.

That's just saying the world is really big, and  you're going to have to learn it along the way.

It seems to me you need two things. One is some way of converting this long-run

goal reward into smaller auxiliary predictive  rewards of the future reward, or the future

reward that leads to the final reward. But initially, it seems to me,

I need to hold on to all this context that  I'm gaining as I'm working in the world.

I'm learning about my clients, my  company, and all this information.

I would say you're just doing regular  learning. Maybe you're using "context"

because in large language models all that  information has to go into the context window.

But in a continual learning setup,  it just goes into the weights.

Maybe context is the wrong word to use  because I mean a more general thing.

You learn a policy that's specific to the  environment that you're finding yourself in.

The question I'm trying to ask is, you need some  way of getting…How many bits per second is a human

picking up when they're out in the world? If you're just interacting over Slack

with your clients and everything. Maybe you're trying to ask the question of,

it seems like the reward is too small of a  thing to do all the learning that we need to do.

But we have the sensations, we have all  the other information we can learn from.

We don't just learn from the reward. We learn from all the data.

What is the learning process which  helps you capture that information?

Now I want to talk about the base common  model of the agent with the four parts. We

need a policy. The policy says, "In the  situation I'm in, what should I do?" We

need a value function. The value function is  the thing that is learned with TD learning,

and the value function produces a number. The number says how well it's going.

Then you watch if that's going up and  down and use that to adjust your policy.

So you have those two things. Then there's also the perception

component, which is construction of your state  representation, your sense of where you are now.

The fourth one is what we're really  getting at, most transparently anyway.

The fourth one is the  transition model of the world.

That's why I am uncomfortable just calling  everything "models," because I want to

talk about the model of the world,  the transition model of the world.

Your belief that if you do this, what will happen? What will be the consequences of what you do?

Your physics of the world. But it's not  just physics, it's also abstract models,

like your model of how you traveled from  California up to Edmonton for this podcast.

That was a model, and that's a transition  model. That would be learned. It's not

learned from reward. It's learned from,  "You did things, you saw what happened,

you made that model of the world." That will be learned very richly

from all the sensation that you  receive, not just from the reward.

It has to include the reward as well,  but that's a small part of the whole

model, a small, crucial part of the whole model. One of my friends, Toby Ord, pointed out that if

you look at the MuZero models that Google DeepMind  deployed to learn Atari games, these models were

initially not a general intelligence itself,  but a general framework for training specialized

intelligences to play specific games. That is to say that you couldn't,

using that framework, train a policy to  play both chess and Go and some other game.

You had to train each one in a specialized way. He was wondering whether that implies

that with reinforcement learning generally,  because of this information constraint,

you can only learn one thing at a time? The density of information isn't that high?

Or whether it was just specific  to the way that MuZero was done.

If it's specific to AlphaZero, what needed  to be changed about that approach so that

it could be a general learning agent? The idea is totally general. I do use

all the time, as my canonical example,  the idea of an AI agent is like a person.

People, in some sense, have  just one world they live in.

That world may involve chess and it  may involve Atari games, but those are

not a different task or a different world. Those are different states they encounter.

So the general idea is not limited at all. Maybe it would be useful to explain what was

missing in that architecture, or that approach,  which this continual learning AGI would have.

They just set it up. It was not their  ambition to have one agent across those games.

If we want to talk about transfer, we should  talk about transfer not across games or

across tasks, but transfer between states. I guess I’m curious if historically, have we

seen the level of transfer using RL techniques  that would be needed to build this kind of…

Good. Good. We're not seeing transfer anywhere.  Critical to good performance is that you can

generalize well from one state to another state. We don't have any methods that are good at that.

What we have are people trying different things  and they settle on something, a representation

that transfers well or generalizes well. But we have very few automated techniques

to promote transfer, and none of them  are used in modern deep learning.

Let me paraphrase to make sure  that I understood that correctly.

It sounds like you're saying that when we  do have generalization in these models,

that is a result of some sculpted… Humans did it. The researchers did it.

Because there's no other explanation. Gradient  descent will not make you generalize well.

It will make you solve the problem. It will not make you, if you get

new data, generalize in a good way. Generalization means to train on one thing

that'll affect what you do on other things. We know deep learning is really bad at this.

For example, we know that if you train on some new  thing, it will often catastrophically interfere

with all the old things that you knew. This  is exactly bad generalization. Generalization,

as I said, is some kind of influence of  training on one state on other states.

The fact that you generalize  is not necessarily good or bad.

You can generalize poorly,  you can generalize well.

Generalization always will happen, but  we need algorithms that will cause the

generalization to be good rather than bad. I'm not trying to kickstart this initial

crux again, but I'm just genuinely curious because  I think I might be using the term differently.

One way to think about these LLMs is  that they’re increasing the scope of

generalization from earlier systems, which  could not really even do a basic math problem,

to now where they can do anything in this  class of Math Olympiad-type problems.

You initially start with them being able  to generalize among addition problems.

Then they can generalize among problems which  require use of different kinds of mathematical

techniques and theorems and conceptual categories,  which is what the Math Olympiad requires.

It sounds like you don't think of being  able to solve any problem within that

category as an example of generalization. Let me know if I'm misunderstanding that.

Large language models are so complex. We don't really know what

information they have had prior. We have to guess because they've been fed so much.

This is one reason why they're  not a good way to do science.

It's just so uncontrolled, so unknown. But if you come up with an entirely new…

They're getting a bunch of things right, perhaps.  The question is why. Well maybe that they don't

need to generalize to get them right, because  the only way to get some of them right is to

form something which gets all of them right. If there's only one answer and you find it,

that's not called generalization. It's just it's the only way to solve it,

and so they find the only way to solve it. But generalization is when it could be this way,

it could be that way, and they do it the good way.

My understanding is that this is working more  and more, better and better, with coding agents.

With engineers, obviously if you're trying  to program a library, there are many

different ways you could achieve the end spec. An initial frustration with these models has

been that they'll do it in a way that's sloppy. Over time they're getting better and better at

coming up with the design architecture and the  abstractions that developers find more satisfying.

It seems like an example of  what you're talking about.

There's nothing in them which  will cause it to generalize well.

Gradient descent will cause them to find  a solution to the problems they've seen.

If there's only one way to  solve them, they'll do that.

But if there are many ways to solve it, some which  generalize well, some which generalize poorly,

there's nothing in the algorithms that  will cause them to generalize well.

But people, of course, are evolved and if  it's not working out they fiddle with

it until they find a way, perhaps until  they find a way which generalizes well.

I want to zoom out and ask about being in the  field of AI for longer than almost anybody who

is commentating on it, or working in it now. I'm curious about what the

biggest surprises have been. How much new stuff do you feel like is coming out?

Or does it feel like people are  just playing with old ideas?

Zooming out, you got into this even  before deep learning was popular.

So how do you see the trajectory of this field  over time and how new ideas have come about and

everything? What's been surprising? I thought a little bit about this.

There are a handful of things. First, the large language models are surprising.

It's surprising how effective artificial  neural networks are at language tasks.

That was a surprise, it wasn't expected. Language  seemed different. So that's impressive. There's a

long-standing controversy in AI about simple  basic principle methods, the general-purpose

methods like search and learning, compared to  human-enabled systems like symbolic methods.

In the old days, it was interesting because  things like search and learning were called

weak methods because they're just using  general principles, they're not using

the power that comes from imbuing a system with  human knowledge. Those were called strong. I think

the weak methods have just totally won. That's the biggest question from the

old days of AI, what would happen. Learning and search have just won the day.

There's a sense in which that was not surprising  to me because I was always hoping or rooting

for the simple basic principles. Even with the large language models,

it's surprising how well it worked,  but it was all good and gratifying.

AlphaGo was surprising, how well that was  able to work, AlphaZero in particular.

But it's all very gratifying because again,  simple basic principles are winning the day.

Whenever the public conception has been  changed because some new application was

developed— for example, when AlphaZero became  this viral sensation—to you as somebody who

has literally came up with many of the  techniques that were used, did it feel

# Chapter 4

So how do you see the trajectory of this field  over time and how new ideas have come about and

everything? What's been surprising? I thought a little bit about this.

There are a handful of things. First, the large language models are surprising.

It's surprising how effective artificial  neural networks are at language tasks.

That was a surprise, it wasn't expected. Language  seemed different. So that's impressive. There's a

long-standing controversy in AI about simple  basic principle methods, the general-purpose

methods like search and learning, compared to  human-enabled systems like symbolic methods.

In the old days, it was interesting because  things like search and learning were called

weak methods because they're just using  general principles, they're not using

the power that comes from imbuing a system with  human knowledge. Those were called strong. I think

the weak methods have just totally won. That's the biggest question from the

old days of AI, what would happen. Learning and search have just won the day.

There's a sense in which that was not surprising  to me because I was always hoping or rooting

for the simple basic principles. Even with the large language models,

it's surprising how well it worked,  but it was all good and gratifying.

AlphaGo was surprising, how well that was  able to work, AlphaZero in particular.

But it's all very gratifying because again,  simple basic principles are winning the day.

Whenever the public conception has been  changed because some new application was

developed— for example, when AlphaZero became  this viral sensation—to you as somebody who

has literally came up with many of the  techniques that were used, did it feel

to you like new breakthroughs were made? Or did it feel like, "Oh, we've had these

techniques since the '90s and people are  simply combining them and applying them now"?

The whole AlphaGo thing had a  precursor, which is TD-Gammon.

Gerry Tesauro did reinforcement learning, temporal  difference learning methods, to play backgammon.

It beat the world's best players  and it worked really well.

In some sense, AlphaGo was merely  a scaling up of that process.

But it was quite a bit of scaling up and  there was also an additional innovation

in how the search was done. But it made  sense. It wasn't surprising in that sense.

AlphaGo actually didn't use TD learning. It waited to see the final outcomes. But

AlphaZero used TD. AlphaZero was applied to  all the other games and it did extremely well.

I've always been very impressed by the  way AlphaZero plays chess because I'm a

chess player and it just sacrifices  material for positional advantages.

It's just content and patient to sacrifice  that material for a long period of time.

That was surprising that it worked so well, but  also gratifying and it fit into my worldview.

This has led me where I am. I'm in some sense a contrarian or

someone thinking differently than the field is. I'm personally just content being out of sync

with my field for a long period  of time, perhaps decades, because

occasionally I have been proved right in the past. The other thing I do—to help me not feel I'm out

of sync and thinking in a strange way—is to look  not at my local environment or my local field,

but to look back in time and into history and to  see what people have thought classically about

the mind in many different fields. I don't feel I'm out of sync with

the larger traditions. I really view myself as

a classicist rather than as a contrarian. I go to what the larger community of thinkers

about the mind have always thought. Some sort of left-field questions

for you if you'll tolerate them. The way I read the bitter lesson is

that it's not necessarily saying that human  artisanal researcher tuning doesn't work,

but that it obviously scales much worse than  compute, which is growing exponentially.

So you want techniques which leverage the latter. Yep.

Once we have AGI, we'll have researchers  which scale linearly with compute.

We'll have this avalanche of  millions of AI researchers.

Their stock will be growing as fast as compute. So maybe this will mean that it is rational

or it will make sense to have  them doing good old-fashioned

AI and doing these artisanal solutions. As a vision of what happens after AGI in

terms of how AI research will evolve, I wonder  if that's still compatible with a bitter lesson.

How did we get to this AGI? You want to presume that it's been done.

Suppose it started with general  methods, but now we've got the AGI.

And now we want to go… Then we're done.

Interesting. You don't think  that there's anything above AGI?

But you're using it to get AGI again. Well, I'm using it to get superhuman levels

of intelligence or competence at different tasks. These AGIs, if they're not superhuman already,

then the knowledge that they might  impart would be not superhuman.

I guess there are different gradations. I'm not sure your idea makes sense because

it seems to presume the existence of AGI  and that we've already worked that out.

Maybe one way to motivate this is, AlphaGo was  superhuman. It beat any Go player. AlphaZero

would beat AlphaGo every single time. So there are ways to get more

superhuman than even superhuman. It was also a different architecture.

So it seems possible to me that the agent that's  able to generally learn across all domains,

there would be ways to give it better architecture  for learning, just the same way that AlphaZero was

an improvement upon AlphaGo and MuZero  was an improvement upon AlphaZero.

And the way AlphaZero was an improvement was that  it did not use human knowledge but just went from

experience. Right.

So why do you say, "Bring in other  agents' expertise to teach it",

when it's worked so well from experience  and not by help from another agent?

I agree that in that particular case that  it was moving to more general methods.

I meant to use that particular example  to illustrate that it's possible to go

superhuman to superhuman++, to superhuman+++. I'm curious if you think those gradations will

continue to happen by just  making the method simpler.

Or, because we'll have the capability of these  millions of minds who can then add complexity

as needed, will that continue to be a false path,  even when you have billions of AI researchers or

trillions of AI researchers? It’s more interesting

just to think about that case. When you have many AIs, will they help each

other the way cultural evolution works in people? Maybe we should talk about that.

The bitter lesson, who cares about that? That's an empirical observation about a particular

period in history. 70 years in history, it doesn't  necessarily have to apply to the next 70 years.

An interesting question is, you're an  AI, you get some more computer power.

Should you use it to make yourself  more computationally capable?

Or should you use it to spawn off a copy of  yourself to go learn something interesting

on the other side of the planet or on some  other topic and then report back to you?

I think that's a really interesting  question that will only arise in

the age of digital intelligences. I'm not sure what the answer is.

More questions, will it be possible to really  spawn it off, send it out, learn something new,

something perhaps very new, and then will it  be able to be reincorporated into the original?

Or will it have changed so much  that it can't really be done?

Is that possible or is that not? You could carry this to its limit as I saw

one of your videos the other night. It suggests  that it could. You spawn off many, many copies,

do different things, highly decentralized,  but report back to the central master.

This will be such a powerful thing. This is my attempt to add something to this view.

A big issue will become corruption. If you really could just get information

from anywhere and bring it into your central  mind, you could become more and more powerful.

It's all digital and they all speak  some internal digital language.

Maybe it'll be easy and possible. But it will not be as easy as you're

imagining because you can lose your mind this way. If you pull in something from the outside

and build it into your inner thinking, it  could take over you, it could change you,

it could be your destruction rather  than your increment in knowledge.

I think this will become a big concern,  particularly when you're like, "Oh,

he's figured out all about how to play  some new game or he's studied Indonesia,

and you want to incorporate that into your mind." You could think, "Oh, just read it all in,

and that'll be fine." But no, you've just read a whole

bunch of bits into your mind, and they could have  viruses in them, they could have hidden goals,

they can warp you and change you. This will become a big thing.

How do you have cybersecurity in the age  of digital spawning and re-reforming again?

I guess this brings us to  the topic of AI succession.

You have a perspective that's quite  different from a lot of people that

I've interviewed and a lot of people generally. I also think it's a very interesting perspective.

I want to hear about it. I do think succession to digital

intelligence or augmented humans is inevitable.  I have a four-part argument. Step one is,

there's no government or organization  that gives humanity a unified point of

view that dominates and that can arrange... There's no consensus about how the world

should be run. Number two,

we will figure out how intelligence works. The researchers will figure it out eventually.

Number three, we won't stop just  with human-level intelligence. We

will reach superintelligence. Number four, it's  inevitable over time that the most intelligent

things around would gain resources and power. Put all that together and it's sort of inevitable.

You're going to have succession to AI  or to AI-enabled, augmented humans.

Those four things seem clear and sure to happen. But within that set of possibilities,

there could be good outcomes as well  as less good outcomes, bad outcomes.

I'm just trying to be realistic about where  we are and ask how we should feel about it.

I agree with all four of those  arguments and the implication.

I also agree that succession contains  a wide variety of possible futures.

Curious to get more thoughts on that. I do encourage people to

think positively about it. First of all, it's something we humans have

always tried to do for thousands of years, try  to understand ourselves, trying to make ourselves

think better, just understanding ourselves. This is a great success for science, humanities.

We're finding out what this essential part of  humanness is, what it means to be intelligent.

Then what I usually say is  that this is all human-centric.

But if we step aside from being a human and  just take the point of view of the universe,

this is I think a major stage in the universe, a  major transition, a transition from replicators.

We humans and animals,  plants, we're all replicators.

That gives us some strengths and some limitations. We're entering the age of design

because our AIs are designed. Our physical objects are designed, our buildings

are designed, our technology is designed. We're designing AIs now, things that can

be intelligent themselves and that  are themselves capable of design.

This is a key step in the  world and in the universe.

It's the transition from the  world in which most of the

interesting things that are, are replicated. Replicated means you can make copies of them,

but you don't really understand them. Right now we can make more intelligent beings,

more children, but we don't really  understand how intelligence works.

Whereas we're reaching now to  having designed intelligence,

intelligence that we do understand how it works. Therefore we can change it in different

ways and at different speeds than otherwise. In our future, they may not be replicated at all.

We may just design AIs, and those  AIs will design other AIs, and

everything will be done by design and  construction rather than by replication.

I mark this as one of the four  great stages of the universe.

First there's dust, it ends with stars. Stars  make planets. The planets can give rise to life.

Now we're giving rise to designed entities. I think we should be proud that we are giving

rise to this great transition in the universe.  It's an interesting thing. Should we consider them

part of humanity or different from humanity? It's  our choice. It's our choice whether we should say,

"Oh, they are our offspring and we should  be proud of them and we should celebrate

their achievements."Or we could say, "Oh no,  they're not us and we should be horrified."

It's interesting that it  feels to me like a choice.

Yet it's such a strongly held thing  that, how could it be a choice?

I like these sort of contradictory  implications of thought.

It is interesting to consider if we are  just designing another generation of humans.

Maybe design is the wrong word. But we know a future generation of humans is going

to come up. Forget about AI. We just know in the  long run, humanity will be more capable and more

numerous, maybe more intelligent. How do we feel about that?

I do think there are potential worlds with future  humans that we would be quite concerned about.

# Chapter 5

Whereas we're reaching now to  having designed intelligence,

intelligence that we do understand how it works. Therefore we can change it in different

ways and at different speeds than otherwise. In our future, they may not be replicated at all.

We may just design AIs, and those  AIs will design other AIs, and

everything will be done by design and  construction rather than by replication.

I mark this as one of the four  great stages of the universe.

First there's dust, it ends with stars. Stars  make planets. The planets can give rise to life.

Now we're giving rise to designed entities. I think we should be proud that we are giving

rise to this great transition in the universe.  It's an interesting thing. Should we consider them

part of humanity or different from humanity? It's  our choice. It's our choice whether we should say,

"Oh, they are our offspring and we should  be proud of them and we should celebrate

their achievements."Or we could say, "Oh no,  they're not us and we should be horrified."

It's interesting that it  feels to me like a choice.

Yet it's such a strongly held thing  that, how could it be a choice?

I like these sort of contradictory  implications of thought.

It is interesting to consider if we are  just designing another generation of humans.

Maybe design is the wrong word. But we know a future generation of humans is going

to come up. Forget about AI. We just know in the  long run, humanity will be more capable and more

numerous, maybe more intelligent. How do we feel about that?

I do think there are potential worlds with future  humans that we would be quite concerned about.

Are you thinking like, maybe we are like the  Neanderthals that give rise to Homo sapiens.

Maybe Homo sapiens will give  rise to a new group of people.

Something like that. I'm basically  taking the example you're giving.

Even if we consider them part of humanity, I don't  think that necessarily means that we should feel

super comfortable. Kinship.

Like Nazis were humans, right? If we thought,  "Oh, the future generation will be Nazis,

I think we'd be quite concerned about  just handing off power to them."

So I agree that this is not super dissimilar  to worrying about more capable future humans,

but I don't think that addresses a lot of  the concerns people might have about this

level of power being attained this fast  with entities we don't fully understand.

I think it's relevant to point  out that for most of humanity,

they don't have much influence on what happens. Most of humanity doesn't influence who can control

the atom bombs or who controls the nation states. Even as a citizen, I often feel that we don't

control the nation states very much.  They're out of control. A lot of it

has to do with just how you feel about change. If you think the current situation is really good,

then you're more likely to be suspicious of  change and averse to change than if you think

it's imperfect. I think it's imperfect.  In fact, I think it's pretty bad. So I’m

open to change. I think humanity has  not had a super good track record.

Maybe it's the best thing that there  has been, but it's far from perfect.

I guess there are different varieties of change. The Industrial Revolution was change,

the Bolshevik Revolution was also change. If you were around in Russia in the 1900s and

you were like, "Look, things aren't going well,  the tsar is kind of messing things up, we need

change", I'd want to know what kind of change  you wanted before signing on the dotted line.

Similarly with AI, where I'd want to  understand, and, to the extent that it's

possible, change the trajectory of AI  such that the change is positive for humans.

We should be concerned about  our future, the future.

We should try to make it good. We should also though recognize

the limit, our limits. I think we want to avoid

the feeling of entitlement, avoid the  feeling of, "Oh, we are here first,

we should always have it in a good way." How should we think about the future?

How much control should a particular  species on a particular planet have over it?

How much control do we have? A counterbalance to our limited control

over the long-term future of humanity should be  how much control do we have over our own lives.

We have our own goals. We have our families.  Those things are much more controllable than

trying to control the whole universe. I think it's appropriate for us to

really work towards our own local goals. It's kind of aggressive for us to say, "Oh, the

future has to evolve this way that I want it to." Because then we'll have arguments where different

people think the global future should  evolve in different ways, and then they

have conflict. We want to avoid that. Maybe a good analogy here would be this.

Suppose you are raising your own children. It might not be appropriate to have extremely

tight goals for their own life, or also have  some sense of like, "I want my children to go out

there in the world and have this specific impact. My son's going to become president and my daughter

is going to become CEO of Intel. Together they're going to have

this effect on the world." But people do have the sense—and

I think this is appropriate—of saying, "I'm  going to give them good robust values such

that if and when they do end up in positions of  power, they do reasonable, prosocial things."

Maybe a similar attitude towards AI makes sense,  not in the sense of we can predict everything that

they will do, or we have this plan about what  the world should look like in a hundred years.

But it's quite important to give them  robust and steerable and prosocial values.

Prosocial values? Maybe that's the wrong word.

Are there universal values  that we can all agree on?

I don't think so, but that doesn't prevent us  from giving our kids a good education, right?

Like we have some sense of wanting  our children to be a certain way.

Maybe prosocial is the wrong word. High integrity is maybe a better word.

If there's a request or if there's a goal that  seems harmful, they will refuse to engage in it.

Or they'll be honest, things like that. We have some sense that we can teach our

children things like this, even if we don't  have some sense of what true morality is,

where everybody doesn't agree on that. Maybe that's a reasonable target for AI as well.

So we're trying to design the  future and the principles by

which it will evolve and come into being. The first thing you're saying is, "Well,

we try to teach our children general principles  which will promote more likely evolutions."

Maybe we should also seek  for things to be voluntary.

If there is change, we want it to be  voluntary rather than imposed on people.

I think that's a very important point. That's  all good. I think this is the big or one of

the really big human enterprises to design society  that's been ongoing for thousands of years again.

The more things change, the  more things they stay the same.

We still have to figure out how to be. The children will still come up with different

values that seem strange to their parents  and their grandparents. Things will evolve.

"The more things change, the more  they stay the same" also seems like

a good capsule into the AI discussion. The AI discussion we were having was

about how techniques, which were invented  even before their application to deep

learning and backpropagation was evident,  are central to the progression of AI today.

Maybe that's a good place  to wrap up the conversation.

Okay. Thank you very much. Awesome. Thank you for coming on.

My pleasure.

