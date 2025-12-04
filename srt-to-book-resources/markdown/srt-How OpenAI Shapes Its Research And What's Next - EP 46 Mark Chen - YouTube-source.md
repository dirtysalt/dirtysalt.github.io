# Chapter 1

Speaker 1: On the recruitment wars, I mean, there's

got a lot of attention clearly, and it looked like  Meta was quite aggressive. What exactly does this

tit for tat look like? What stage are we Speaker 2:

At? Yeah, I mean, there is a pool of talent and  everyone kind of knows who they are, and I think

many companies have realized that one of the key  ingredients, not the only important ingredient,

but one of the key ingredients [00:00:30] to  building a great AI lab is to get the best talent.

And I think not a surprise that Meta has been  aggressively employing the strategy. We haven't

sat back idly, and I actually want to tell the  story from Open AI's point of view. I think that

a lot has been made in the media of, oh, there's  this unidirectional flow of talent over to Meta,

but the way that I've seen it is no meta. They've  gone after a lot of people quite unsuccessfully.

So [00:01:00] just to give you context, within my  staff, within my direct reports, before they hired

anyone from opening, I think they went after half  of my direct reports and they all declined. And of

course, if they have something like 10 billion  of capital per year to deploy towards talent,

they're going to get someone. So I actually feel  like we've been fairly good about protecting our

top talent and it's been interesting and fun  to see it escalate [00:01:30] over time.

Some interesting stories here are Zuck  actually went and hand delivered soup

to people that he was trying to recruit  from us just to show how far he would,

yeah, I think he hand cooked the soup  and it was shocking to me at the time,

but over time I've kind of updated towards these  things can be effective in their own way. And

I've also delivered soup to people that we've been  [00:02:00] recruiting from Meta. You're doing a

Speaker 1: Soup, soup counting.

Speaker 2: I've thought

of if I had an offsite, the next offsite  for my staff, I'm going to take them to a

cooking class. Speaker 1:

Okay. Speaker 2:

Yeah. I mean it's just been, but I do think  there's something I've learned about recruiting.

Did you cook your soup? It's better if you get Speaker 1:

Michelin star soup. You know what I mean? Speaker 2:

Yeah. No, no, no. I think Dejo is very, very good  and probably better than any soup I could cook.

But [00:02:30] yeah, I do think there is something  I've learned about just how to go aggressively

after top talent. And I think the thing I've  been actually very inspired by is that at OpenAI,

even among people who have offered meta, I haven't  heard anyone say a GI is going to be developed at

Meta first. Everyone is very confident in the  research program at OpenAI. And [00:03:00] one

thing that I've made very clear to my staff to the  whole research org is we don't counter dollar for

dollar with meta and the multiples that below what  meta is offering that people are very happy to

stay at OpenAI gives me so much conviction that  people really believe in the upside and believe

that we're going to do it. Speaker 1:

And Alex Wang, he used to  be one of the math, the,

Speaker 2: I'm

Speaker 1: Sure you guys hung

Speaker 2: Out. Well, yeah, I mean I have hung

out with [00:03:30] Alex a handful of times, but  we don't do much anymore. Yeah, I mean, yeah,

Speaker 1: Why did soup become the thing? It just,

Speaker 2: I don't know.

There's been soup, there's been flowers, there's  been anything you can think of under the sun,

but I dunno, I think life's an  adventure. I play into the meme.

Speaker 1: Is there any poker strategy

to employ is your thinking? Speaker 2:

Well again, I think it really goes  back to what I've said about the

media narrative. [00:04:00] The game is not  to retain every single person in the org,

it's to trust in this pipeline that we have for  developing talent and to understand who the key

people we need to keep are and to keep those. And  I think we've done a phenomenal job at that.

Speaker 1: [00:04:30]

We have a special treat today. I'm excited. Mark  Chen is here from OpenAI. He's the chief research

officer. He is somebody I've gotten to know over  the last couple of years. Thank you so much for

Speaker 2: Getting that. Yeah, no,

it's been great to know you for so long. Speaker 1:

I feel like there's a handful of people in this  world working on this very important project and

I mean, you're right at the top of it, so it's so  cool to have a chance [00:05:00] to chat. Yeah,

Speaker 2: Thanks for having me on.

Speaker 1: It is my pleasure. And I mean there's

a bunch of things that I want to talk to you about  because I've gotten to know you, like we said over

those last couple of years. I want people to know  a bit more about your biography, but I also know

there's going to be AI enthusiasts who want us  to go deep on a couple of things there. So we

will try to do everything. I wanted to start just  by giving people a feel for your job, which in my

[00:05:30] head, I mean just correct me if I get  any of this wrong, but Sam has been, he's really

into research. He's the boss, he's at the top of  the food chain, but then you and Jakob are working

together to shape open AI's research direction.  And then you're in this additional part of this

role is actually deciding which compute goes where  [00:06:00] onto these projects. So you kind of

have to chart where OpenAI is heading and then the  mechanics of how you're going to get there. And

this always strikes me as a horrible job because I  picture people doing everything in their power to

get GPUs from Houston. It's true. People are Speaker 2:

Very creative in the ways that they try to make  backroom deals to get the GPUs they need. But

yeah, I mean it is a big part of the job figuring  out the priorities for the research org and also

being accountable for execution. So [00:06:30]  really to that first point, there's this exercise

that Jakob and I do every one to two months where  we take stock of all the projects at OpenAI and

it's this big spreadsheet, about 300 projects,  and we go and try to deeply understand each one

as best as we can and really rank them. And  I think for a company of 500 people, it's

important for people to understand what the core  priorities are and for those to be communicated

clearly both explicitly, verbally [00:07:00] and  also through the way that we allocate compute.

Speaker 1: Alright, what do we do at Core Memory?

We cover innovative, fast moving forward thinking  companies, which is why Core Memory is sponsored

by Brex because Brex is the intelligent finance  platform for many of these companies. 30,000

companies from startups to the world's largest  corporations rely on Brex is technology for

their finances. They've got smart corporate cards,  high [00:07:30] yield business banking and expense

automation tools that are fantastic. I hate doing  my expenses. And Brex is ais software run right

through those expenses, figure out where we're  spending money and take care of so much stuff

for you so you don't have to waste your time on it  yourself. Go to brex.com/core memory to learn more

and just get with the program. Let's get going.  Let's get out of this archaic finance software

and move toward [00:08:00] the future core memory  and Brex. So you've got, when you're talking about

the 500, these are the 500. This is the heart of  the research team in an organization now that's

thousands of people. Yeah. Okay. And then in  that, when you're talking about this 300 projects

I imagine mean obviously some of those are the  giant frontier models and then some are probably

experiments the people are working on. And so how  do you possibly keep track of all [00:08:30] that

and then come to some sort of conclusion  about what merits GPUs and what doesn't?

Speaker 2: Absolutely. So I think it is very important when

doing this exercise to keep the core roadmap in  focus. And one thing that differentiates, I think

OpenAI with other big labs out there is OpenAI has  always had core exploratory research. At its core.

We are not in the business of replicating the  results of other labs, of catching up to other

labs in terms of [00:09:00] benchmarks that isn't  really our bread and butter. We're always trying

to figure out what that next paradigm is and we're  willing to invest the resources to make sure that

we find that right. And I think most people  might be surprised at this, but more compute

goes into that endeavor of doing exploration  than it is to training the actual artifact.

Speaker 1: It's still got to be

how do you stop yourself from being persuaded  by someone because everybody's going to put,

when I think about this, sometimes I picture  [00:09:30] when I was at the New York Times, you

would have this page one meeting where everybody  wants to be on page one. Everybody thinks their

story is the most important story. They're all  doing their very best job to tell you why this

thing is so important. Everybody in that room has  worked weeks, months on whatever they're pitching.

And so it feels like life and death and that.  Yeah, I mean it seems so difficult for me.

Speaker 2: Yeah, no, it is also a difficult

process and I think [00:10:00] the hardest cause  you have to make are this is a project that we

just can't fund right now. But I also think that's  good leadership. You need to clearly communicate

that, hey, these are the priorities, this is what  we're going to talk about. These are the types of

results that we think move the research program.  And there can be other things, but those have to

be clearly number two. Speaker 1:

When you were talking about not being reactive  to your competitors. When I was looking through

my notes, I don't know if I could go to the line  [00:10:30] quick enough, but I mean this was a

point of pride that I saw that you feel like some  of the other companies are, well, you guys were

in this position where you were ahead and setting  the bar for others, so they were reactive right to

what you had coming out. We happened to be doing  this interview a few days after Gemini three came

out, and there is a degree to which your rivals  at times. [00:11:00] I mean, there's this back

and forth going on and I know the benchmarks are  sort of controversial, how valuable they are,

but people go ahead on these things. So how do  you also as time has gone on maintain that luxury

or that intellectual position where you feel like  we're just going to do what we're going to do?

Speaker 2: Yeah, I think AI research today,

the landscape is much more competitive than it's  ever been. And the important thing is to not

get [00:11:30] caught up in that competitive  dynamic because you can always say, Hey,

I'm going to ship an incremental update that puts  me in front of my competitor for a couple weeks

or a couple months. And I don't think that's the  long-term sustainable way to do research because

if you crack that next paradigm, that's just going  to matter so much more, you're going to shape the

evolution of it. You're going to understand all  the side research directions around that sphere of

ideas. And so when you think about our RO program  as an example [00:12:00] of this, right? We bet

more than two years ago that we're really going  to crack RO on language models. And this was a

very unpopular bet at the time. Right now it seems  obvious, but back then the environment was, Hey,

there's this pre-training machine that's working  great, there's this post-training machine that's

working great. Why invest in something else? And  I think today everyone would tell you thinking

and language models, it's just a primitive you  can't have, can't live without. And so we're

really [00:12:30] there to make these bold  bets and to figure out how we can scale and

build the algorithms to really scale to orders  of magnitude more compute than we have today.

Speaker 1: And I get that intellectually in my,

it gets harder as you guys started, as basically  a pure research company. When you look at OpenAI

today, I mean you have product line, there's  parts of OpenAI that look much more familiar

to a mature Microsoft or a Google where you  have product lines, you've got all these

different [00:13:00] things that you have to serve  typically. I feel like you guys are still young

enough, so maybe you don't have these exact  pressures yet, but as those companies go on,

it always becomes, well, we're more focused  on the things that are serving the bottom

line than spending a ton of money on research  always seems to get dwindled down over time.

Speaker 2: And I think that's really

one of the most special things about OpenAI  at its core. We're pure AI research company,

and I don't think you can say that of  [00:13:30] many other companies out there.

And we were founded as a nonprofit and I joined  during that era. And I think the spirit is build

a GI advance a GI research at all costs and do it  in a safe way, of course. But yeah, I actually do

think that's the best head fake to really creating  value. If you focus and you win at the research,

the value is easy to create. So I think there's a  trap of getting too lost into like, oh, [00:14:00]

let's strive up the bottom line. When in reality  if you do the best research, that part of the

picture is very easy. Speaker 1:

And you started in 2018. In 2018, and  so you feel like that soul, that

Speaker 2: That core culture and that core nucleus,

it's really persistent. It's still there. Speaker 1:

What does Elon says? What is he? He says, we  shouldn't call any of you guys researchers. It's

just engineering, right? Speaker 2:

Yeah, no, I think, yeah, no, it's true because I  feel like once you have this hierarchy [00:14:30]

and you elevate, let's say research science as  a thing beyond engineering, you've completely

already lost the game. Because when you're  building a big model, so much is in the practice

of optimizing all of those little percentages of  how you make your kernels that much faster. How

do you make sure the numerics all work? And that's  a deep engineering practice. And if you don't have

that part of [00:15:00] the picture, you can't  scale to the number of GPUs we use today

# Chapter 2

Speaker 2: And I think that's really

one of the most special things about OpenAI  at its core. We're pure AI research company,

and I don't think you can say that of  [00:13:30] many other companies out there.

And we were founded as a nonprofit and I joined  during that era. And I think the spirit is build

a GI advance a GI research at all costs and do it  in a safe way, of course. But yeah, I actually do

think that's the best head fake to really creating  value. If you focus and you win at the research,

the value is easy to create. So I think there's a  trap of getting too lost into like, oh, [00:14:00]

let's strive up the bottom line. When in reality  if you do the best research, that part of the

picture is very easy. Speaker 1:

And you started in 2018. In 2018, and  so you feel like that soul, that

Speaker 2: That core culture and that core nucleus,

it's really persistent. It's still there. Speaker 1:

What does Elon says? What is he? He says, we  shouldn't call any of you guys researchers. It's

just engineering, right? Speaker 2:

Yeah, no, I think, yeah, no, it's true because I  feel like once you have this hierarchy [00:14:30]

and you elevate, let's say research science as  a thing beyond engineering, you've completely

already lost the game. Because when you're  building a big model, so much is in the practice

of optimizing all of those little percentages of  how you make your kernels that much faster. How

do you make sure the numerics all work? And that's  a deep engineering practice. And if you don't have

that part of [00:15:00] the picture, you can't  scale to the number of GPUs we use today

Speaker 1: Because I think there, well, okay, but there

is a mystique that surrounds a researcher versus  an engineer. You know what I mean? So do you feel

like it is better to stay levelheaded on that?  Is that kind of what you're saying, or? Well,

Speaker 2: I just feel like researchers,

they come in so many different shapes.  Some of our best researchers, they're

the type that [00:15:30] they come up with a  billion ideas and many of them are not good,

but just when you're about to be like, ah, is this  person really worth it? They come up with some

phenomenal idea. Some of them are just so good at  executing on the clear path ahead. And so there's

just so many different shapes of researchers  and I think it's hard to just lump it into one

stereotypical type that works Speaker 1:

Box. That makes sense. Okay. I won't belabor  you with too many competitive [00:16:00] rival

questions. It's just since Gemini three did come  out, I did wonder what happens with you personally

or the team when one of your rivals puts it, does  everybody go and look and see what it can do? Is

there a prompt or a question that you often throw  at these new models to see what they can do?

Speaker 2: Yeah, so to speak to Gemini

three specifically, it's a pretty good [00:16:30]  model. And I think one thing we do is try to

book consensus. The benchmarks only tell you so  much, and just looking purely at the benchmarks,

we actually felt quite confident. We have models  internally that perform at the level of Gemini

three, and we're pretty confident that we will  release them soon and we can release successor

models that are even better. But yeah, again,  kind of the benchmarks only tell you so much,

and [00:17:00] I think everyone probes the models  in their own way. There is this math problem,

I like to give the models. I think so far, none  of them has quite cracked it, even the thinking

models. So yeah, I'll wait for that. Speaker 1:

Is this like a secret math problem? Speaker 2:

Oh, no, no, no. Well, if I now announce it  here, maybe it gets trained on, but yeah,

I do think it's one of the nice puzzles of last  year. It's this, the 42 problem. So you want to

create this random number generator mod [00:17:30]  42, and you have access to a bunch of primitives,

which are random number generators, modular  primes less than 42, and you want to make as

few calls on expectation to these sub generators  as possible. So it's a very cute puzzle, but

the language models, they get pretty close to  the optimal solution. But I haven't seen one

quite crack it. Speaker 1:

Okay. We're heading down a  direction I want to ask you about

Speaker 2: Absolutely.

Speaker 1: Just before we get there. So I know I've seen you,

you're very competitive. You've also told me Speaker 2:

Yes. Speaker 1:

I think I found I Speaker 2:

Love [00:18:00] competition. Speaker 1:

I hate to fucking lose Speaker 2:

Somewhere. I really hate losing. I Speaker 1:

Hate losing. Yeah. So I'm picturing, I'm  just curious if this is at all right. I mean,

if we know Gemini three or whatever  is coming out on a Thursday, I mean,

are you up at midnight throwing that problem  at it? Or is it not quite that drastic?

Speaker 2: No, I mean, I think it's in long arcs

and any endeavor, I am kind of a person who has  obsessions. [00:18:30] I think any endeavor you

have to play the long game. And we've actually  been focusing on pre-training, specifically

supercharging our pre-training efforts for the  last half year. And I think it's a result of some

of those efforts together with Jacob focusing and  building that muscle of pre-training at OpenAI,

crafting a really superstar team around it,  making sure that all of the important areas

and aspects of pre-training are emphasized.  [00:19:00] That's what creates the artifacts

today that feels like we can go head to head  with Gemini through easily on pre-training.

Speaker 1: Okay. I want to ask about the pre-training,

because I've been talking to all you guys about  this a lot. Okay. But you're saying that you're

less obsessed about lobbying problems at these  new models just when they appear and more at

this long journey? Speaker 2:

Absolutely. Yeah. Okay. Speaker 1:

Okay. The reason I wanted to talk about the  puzzle [00:19:30] that you were at. I mean,

I first met Jaka before OpenAI ever started when  he was doing a coding competition. And I got super

into coding competitions for a while. There's this  guy, Kennedy, I don't know if he's still famous,

but he was like the Michael Jordan of these  coding competitions. And so I went to watch

one at Facebook, used to, I don't know if  they still do, but they had an annual

Speaker 2: Hacker cup.

Speaker 1: Yeah. Hacker cup. And that's

where I saw Jacob for the first time. And then I  know you, I think did [00:20:00] math competitions

in high school, probably grade school through  high school. And then did you also do i I

Speaker 2: Stuff. So I got into coding

really late in life. It was a roommate in college  that convinced me to take my first coding class,

and I had all the hubris of a mathematician  at that time. Whereas math is the purest

and hard of science, and that's where you really  prove your worth. I mean, I think I was probably

too into the competition back then, but yeah, I  mean, it became this super [00:20:30] rewarding

endeavor and it started out as purely a way to  keep in touch with my friends from college.

Speaker 1: You went to MIT?

Speaker 2: Yeah, I went to MITI graduated, and every

weekend we would just log on and do these contests  just to keep in with each other. And over time,

I've found myself having a talent for it. I  started competing fairly well and then writing

problems for contests like the USA coding Olympiad  eventually started coaching that [00:21:00] team.

And yeah, it's been a great community where  I've met people like Scott that you know.

Speaker 1: Yeah. Okay. So I think lots of people might be

familiar with math competitions. They probably see  kids going through that. The i I and these coding

competitions are a little bit different. I mean,  it's so much better, but when I saw them, I mean,

it looks like it's almost like a word problem  that's a puzzle, and you are trying to find the

most efficient and correct way to solve [00:21:30]  that. And you're in this race against everybody

and everybody's writing code on their computer.  And then some people try to get there really fast,

but then their thing kind of doesn't solve the  problem and there's this trade off, right?

Speaker 2: Yeah, absolutely.

Speaker 1: Right. And so you actually

were on the MIT team? No, Speaker 2:

No. It's something I did after college. After Speaker 1:

College, okay. But today you are  the coach of the US National?

Speaker 2: Yeah, one of the coaches.

Speaker 1: One of the coaches,

okay. And was it last year or the year before  [00:22:00] the us? We hadn't won one in a

long time, Speaker 2:

Right? Yeah, yeah. Speaker 1:

Didn't we? Speaker 2:

Yeah, yeah, yeah. So the team, you can  never predict what the makeup of top

talent looks like every year, but we had a  very spiky team, I think two years ago.

Speaker 1: And

Speaker 2: Yeah, I believe they won the olympiad

Speaker 1: Because I feel like usually it's like China

or Russia or Belarus and Poland, I mean, right?  Yeah. So the big competition [00:22:30] takes

place in a different country every year. What  does it look like? How many people show up?

Speaker 2: So they take the

top four students from every single country. It  is as much of a competition as it is a social

event. This is a tight knit community. They  all go on to do phenomenal things. And yeah,

it's this intense two day contest where each day  you get just three problems, five hours to solve

them, and you can really feel the adrenaline and  [00:23:00] all the pressure in the room. But it's

also great fun. I think people settle down and  they make lifetime friends through it. And as

Speaker 1: A coach, I mean,

you're so freaking busy, man. How much time do  you spend on this? What does that look like?

Speaker 2: Honestly, the kids are, so sometimes it's

really about just managing their performance and  strategy. I think you're going to have good days,

you're going to have bad days, you're going to  have good hours within the contest, bad hours,

and you can't let [00:23:30] that get into your  head. There's a lot of similarities between

managing contestants and managing researchers.  It's on a much longer timescale, but researchers

have good months, bad months. You can't really  let those strings of failures get into your head

because that's just the nature of research. And I  think a lot of it's morale management at a certain

point. Yeah. I think one other interesting thing  that contests [00:24:00] have helped me realize

lately is when you put the models and deploy them  towards solving these contest problems, which

they're quite good at these days. Absolutely. Speaker 3:

Yeah, I was going to Speaker 2:

Ask you about that. They work in a very  different way from humans. We typically think

of these machines as they're very good at pattern  recognition. You can take any problem if it maps

to a previous problem, which is probably going  to be able to solve it. But what I've noticed is

in some of the previous iis, there's this problem  message is very ad hoc. [00:24:30] I didn't think

the models would solve it at all, but actually one  of the easier problems for the ai. So yeah, I mean

this has given me the sense that AI is plus humans  in Frontier research, it's going to do something

amazing just because the AI has a different  intuition for what's easy and what's not.

Speaker 1: Okay. Is it vaguely, when D minded,

the whole Alpha go thing, there was that moment  where it was doing things human, it was playing

in ways humans hadn't played before. So kind  of vaguely similar [00:25:00] to that or

Speaker 2: I think so. I think

really with g PT five Pro, there's been  an inflection point in frontier research,

and one of the best anecdotes I have for  this is I think three days after the launch,

I met up with a friend who was a physicist and  he had been playing around with the models,

felt like they were cute but not super useful.  [00:25:30] And I challenged him with the ProModel,

just try something ambitious. And he put in his  latest paper, it thought for 30 minutes and just

got it. And I would say that that reaction in that  moment, it was kind of seeing Lisa at all during

that move 37, move 38. And I just think that is  just going to keep happening more and more for

frontier mathematics, for science, for biology,  material science. The models [00:26:00] have

really gotten to that point. Speaker 1:

I was going to ask you this question, which is  not very original because I think we've been doing

this ever since Big Blue and all the chess stuff.  But yeah, just as somebody who had followed all

these competitions, if, I don't know, there's  a sadness when you start seeing these models,

solving these things that were like this  height of these achievement for these very

unique human minds. Speaker 2:

Well, yes and no. I mean, I was good at  competitive programming. I was never at

the absolute top, [00:26:30] and maybe this is a  way to get revenge, but I do think, no, there's

certainly a moment for myself. We tracked coding  conscious performance while we were developing

reasoning models for a while. And at the start  of the program, they were not super great at

the level of any average competitor going to the  contest. And over time they just started creeping

up and [00:27:00] up in terms of capability. And  you still remember that moment when you walk into

the meeting and they have where your performance  is, and then the models exceeded that. Man, that

was also a shock to me. It's just like, wow, we've  automated to this level of capability so fast. And

of course, Yako was there still a bit smug, but  within one or two months it was also surpassing

him. So yeah, no, the models are at the frontier  today. It's so clear by even through the results

we've done this summer [00:27:30] at Coder, right  top optimization competitive programmers in the

world, I think it achieved second place there.  And so really it's jumped from hundredth place

last year to top five this year. Do you think  we'll still be doing these competitions

Speaker 1: In 10 years?

Speaker 2: I think so. I mean,

they're just fun. I mean, certainly a bunch  of people who use it to had their resume or

going to drop off from doing it, but I think the  people who've always excelled [00:28:00] at it

the most are people who just do it for the fun  of it. And I don't think that'll go away.

Speaker 1: When I was doing this story, I mean,

they were telling me that if you're from Russia  or I don't, which countries that you basically

get an automatic free ride to any university that  you want. I mean, I see the guys on the US team

go to Harvard and MIT, so they seem to be doing  okay, but it doesn't seem like the US has a

Speaker 2: Yeah, don't you think? Yeah. I mean interviews,

right? They're going to be kind of broken going  forward, and everyone's seeing this a little bit,

and even [00:28:30] college exams or college  homework, it's all broken at this point. And I

do think we're going to need new ways of assessing  and gauging who's performing what, who's learned

the material where somebody's actually Speaker 1:

At. Speaker 2:

Yeah. Yeah. So I mean, I've had this idea  here where maybe for our interviews we

should just have candidates talk to chat  GPT, and it's a special kind of chat GPT,

where the model's trying to gauge whether you know  the material [00:29:00] or whether you're at the

capability level to work at OpenAI. And you have  to have this conversation with it that convinces

it deeply you along at OpenAI. And of course you  can't be allowed to jailbreak it, and we look at

the transcript after, but maybe tests like this  will more accurately reflect in the future.

Speaker 1: So you don't do that yet,

but you're thinking about Speaker 2:

Just creative ways to revamp the interviews. Speaker 1:

Yeah. Well, I mean, Silicon Valley is  famous for doing the brain teasers during

Speaker 3: The interviews

Speaker 1: And everything. Yeah. [00:29:30]

So you were very good at math growing up, and  I think, were you born on the East Coast?

Speaker 2: Yeah, born on the east coast.

Speaker 1: And then you lived on the West Coast too,

Speaker 2: On the west coast,

Speaker 1: And then you lived in Taiwan for

grade school to high school Speaker 2:

Four years, yeah. Speaker 1:

Okay. And your parents worked at Bell Labs? Speaker 2:

Yep. Speaker 1:

So you come from engineering Speaker 2:

Stock.

