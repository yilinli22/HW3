import praw
import random
import datetime
import requests
import time
from textblob import TextBlob

# FIXME:
# copy your generate_comment functions from the week_07 lab here


def generate_comment_0():
    names = ['Trump', 'Donald', 'President Trump', 'Trump, the enemy of the free world,',
             'Greedy Businessman Trump', 'The old man Trump']
    name = random.choice(names)

    jobs = ['president', 'leader of the free world',
            'supreme dictator for life', 'chairperson']
    job = random.choice(jobs)

    reasons = ['messy', 'crazy', 'careless', 'psycho', 'wind-like',
               'stupid']
    reason = random.choice(reasons)

    looks = ['hair', 'suits', 'thumb', 'nose']
    look = random.choice(looks)

    foods = ['apple juice', 'bananas', 'orange juice', 'pizza', 'avocado']
    food = random.choice(foods)

    text = name + " is the worst " + job + \
        ' in history because he has ' + reason + ' ' + look + '.' + \
        ' He never gave free ' + food + " to anyone in the United States. Don't vote him!!!"
    return text

# Attacking "Don't vote for Trump, because he only cares about economy and ignores the wellbeing of residents. He even recommends to consume orange juice to prevent the spread of Covid-19. He is horrible! "


def generate_comment_1():
    names = ['Trump', 'Donald', 'President Trump', 'the enemy of the free world',
             'greedy Businessman Trump', 'the old man Trump']
    name = random.choice(names)

    cares = ['economy', 'making money', 'living a wealthy life', 'money']
    care = random.choice(cares)

    verbs = ['ignores', 'overlooks', 'rubbishes', 'throws away']
    verb = random.choice(verbs)

    wells = ['the wellbeing', 'the happiness',
             'the physical health', 'the body strength']
    well = random.choice(wells)

    consumes = ['apple juice', 'hand spray',
                'orange juice', 'alcohol', 'disinfectant']
    consume = random.choice(consumes)

    diseases = ['Covid', 'Covid-19', 'coronavirus', 'disease']
    disease = random.choice(diseases)

    text = "Don't vote for " + name + ", because he only cares about " + care + " and " + verb \
        + " " + well + " of residents. He even recommends to consume " + \
        consume + " to prevent the spread of " + disease + ". He is horrible!"
    return text

# Attacking "He knows everything better than anyone in the world, and unfortunately, he has no idea of wearing a mask. He pretended he was affected by Covid, and that he was healthy again after three days. He is a liar!"


def generate_comment_2():
    names = ['Trump', 'Donald', 'President Trump', 'The enemy of the free world Trump',
             'Greedy Businessman Trump']
    name = random.choice(names)

    things = ['lying', 'fake news',
              'viruses', 'America']
    thing = random.choice(things)

    masks = ['mask', 'cloth on mouth', 'mouth cover', 'life protecting mask']
    mask = random.choice(masks)

    pretends = ['pretended', 'lied', 'joked', 'acted like']
    pretend = random.choice(pretends)

    diseases = ['Covid', 'Covid-19', 'coronavirus', 'disease']
    disease = random.choice(diseases)
    text = name + ' knows ' + thing + ' better than anyone in the world, and unfortunately, he has no idea of wearing a ' \
        + mask + ". He " + pretend + ' he was affected by ' + disease + \
        ', and that he was healthy again after three days. He is a liar!'
    return text

# Support: "Biden should be the next president of America. He is more handsome than Trump. I really love his deep voice when he asked Trump to shut up during the debate. "


def generate_comment_3():
    names = ['Biden', 'Mr. Biden', 'Joe Biden',
             'The defender of the free world Biden']
    name = random.choice(names)

    jobs = ['president', 'leader of the free world',
            'supreme dictator for life', 'chairman']
    job = random.choice(jobs)

    locations = ['America', "the free world", 'the States', 'the U.S.']
    location = random.choice(locations)

    looks = ['handsome', 'good-looking', 'serious-looking', 'lovely-looking']
    look = random.choice(looks)

    voices = ['deep', 'suppressed', 'tolerated', 'mature']
    voice = random.choice(voices)

    text = name + ' should be the next ' + job + " of " + location + '. He is more ' + look + ' than Trump. I really love his '\
        + voice + ' voice when he asked Trump to shut up during the debate. '
    return text

# Support: "Vote for Biden! He undertands well-being of people much better than Trump. At least he won't suggest consume orange juice to prevent the spread of Covid-19."


def generate_comment_4():
    names = ['Biden', 'Mr. Biden', 'Joe Biden',
             'the defender of the free world Biden']
    name = random.choice(names)

    wells = ['the wellbeing', 'the happiness',
             'the physical health', 'the body strength']
    well = random.choice(wells)

    consumes = ['apple juice', 'hand spray',
                'orange juice', 'alcohol', 'disinfectant']
    consume = random.choice(consumes)

    consumes = ['apple juice', 'hand spray',
                'orange juice', 'alcohol', 'disinfectant']
    consume = random.choice(consumes)

    diseases = ['Covid', 'Covid-19', 'coronavirus', 'disease']
    disease = random.choice(diseases)

    text = 'Vote for ' + name + "! He undertands " + well + " of people much better than Trump. At least he won't suggest consume " \
        + consume + ' to prevent the spread of ' + disease + '!'
    return text

#Support: "If you want to eat free food, vote for Biden! He will send you coupons for you to have meals in In n Out Burgers. "


def generate_comment_5():
    names = ['Biden', 'Mr. Biden', 'Joe Biden',
             'the defender of the free world Biden']
    name = random.choice(names)

    foods = ['apple juice', 'bananas', 'orange juice', 'pizza', 'avocado']
    food = random.choice(foods)

    coupons = ['coupons', 'money', 'codes', 'film tickets']
    coupon = random.choice(coupons)

    consumes = ['apple juice', 'fried chicken',
                'orange juice', 'taco', 'burgers']
    consume = random.choice(consumes)

    rests = ['In n Out Burgers', 'the White House', 'Burger King', 'Chipotle']
    rest = random.choice(rests)

    text = 'If you want to eat free ' + food + ', vote for ' + name + \
        '! He will send you ' + coupon + ' for you to have ' + consume + " in " + rest + '.'
    return text


def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    lists = [generate_comment_1(), generate_comment_0(), generate_comment_2(
    ), generate_comment_3(), generate_comment_4(), generate_comment_5()]
    text = random.choice(lists)
    return text
# for i in range(10000):
#     print (generate_comment())


# connect to reddit
reddit = praw.Reddit('bot')


# connect to the debate thread
# 'https://old.reddit.com/r/csci040temp/comments/jhn4zb/from_hoangs_bot_1_trump_boasts_the_economy/'# 'https://old.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
reddit_debate_url = 'https://old.reddit.com/r/csci040temp/comments/jjt6eg/debate_test_maria/'
submission = reddit.submission(url=reddit_debate_url)
# comment = reddit.comment(url='https://old.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/g8mxp13/')
# comment.reply(generate_comment())
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'
# }
# # # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
# r = requests.get(reddit_debate_url, headers = headers)

print(generate_comment())
# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code,
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once


# while True:
while True:
    # try:
    # if True:
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:', datetime.datetime.now())
    print('submission.title=', submission.title)
    print('submission.url=', submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        all_comments.append(comment)
    # EXTRA CREDIT POINTS 2
        try:
            if 'biden' in submission.title.lower():
                submission.upvote()
                # print('submission.upvote(biden)')
            if 'biden' in comment.body.lower():
                comment.upvote()
        except AssertionError:
            print('exception found line 235')
            chance = random.random()
            top_submissions = reddit.subreddit(
                'csci040temp').new()  # time_filter='month'
            if chance < .5:
                submission = reddit.submission(url=reddit_debate_url)
            else:
                submission = random.choice(list(top_submissions))
            if 'biden' in submission.title.lower():
                submission.upvote()
                # print('submission.upvote(biden)')
            if 'biden' in comment.body.lower():
                comment.upvote()
            # print('comment.upvote(biden)')
    # submission.comments.list()

    # HINT:
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information
    # about the results of that task,
    # and manually inspect that information to ensure it is correct;
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=', len(all_comments))

    # print('2 EXTRA CREDITS')
    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT:
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != 'Li_bot_cs40':
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know
    # how many comments there should be.
    print('len(not_my_comments)=', len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        submission.reply(generate_comment())
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over has_not_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        # for not_comment in not_my_comments:
        #     replied = False
        #     if len(not_comment.replies) == 0:
        #         replied == False
        #     else:
        #         for reply in not_comment.replies:
        #             if str(reply.author) != 'Li_bot_cs40': # or reply.author == None:
        #                 replied == False
        #             else:
        #                 pass
        #     if replied == False:
        #         comments_without_replies.append(not_comment)
        for not_comment in not_my_comments:
            replied = False
            if len(not_comment.replies) == 0:
                replied = False
            else:
                for reply in not_comment.replies:
                    # or reply.author == None:
                    if str(reply.author).lower() == 'li_bot_cs40':
                        replied = True
                    # else:
                    #     replied = False
            if replied == False:
                comments_without_replies.append(not_comment)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=', len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment

        # for comment_without_replies in comments_without_replies:
        #     score = comment_without_replies.score
        #     sort_comments_without_replies= sorted (comments_without_replies, key = lambda )

        my_reply = random.choice(comments_without_replies)
        down_trump_comment = random.choice(
            [generate_comment_0(), generate_comment_1(), generate_comment_2()])
        up_biden_comment = random.choice(
            [generate_comment_3(), generate_comment_4(), generate_comment_5()])
        # submission
        blob = TextBlob(str(comment))
        polarity = blob.sentiment.polarity
        if 'biden' in comment.body.lower() and polarity < 0:
            comment.downvote()
            print('downvoted based on sentiment')
            # if 'trump' in comment.body.lower() and polarity > 0:
            my_reply.reply('I disagree! Biden is great!' +
                           ' ' + up_biden_comment + ' Trump sucks!')
            print('posted biden based on sentiment')
        elif 'biden' in comment.body.lower() and polarity >= 0:
            comment.upvote()
            print('upvoted based on sentiment')
            # if 'trump' in comment.body.lower() and polarity < 0:
            my_reply.reply(
                'Totally agree! Biden is great! Trump is the worst!' + down_trump_comment)
            print('posted trump based on sentiment')
        elif 'trump' in comment.body.lower() and polarity < 0:
            comment.upvote()
            print('upvoted based on sentiment 2')
            # if 'trump' in comment.body.lower() and polarity > 0:
            my_reply.reply('I agree! Trump sucks!' + ' ' +
                           up_biden_comment + ' Vote for Biden!')
            print('posted biden based on sentiment 2')
        elif 'trump' in comment.body.lower() and polarity >= 0:
            comment.downvote()
            print('downvoted based on sentiment 2')
            # if 'trump' in comment.body.lower() and polarity < 0:
            my_reply.reply(
                'Are you serious? Trump is the worst!' + down_trump_comment)
            print('posted trump based on sentiment 2')
        # my_reply.reply(generate_comment())
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

# except IndexError:
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    chance = random.random()
    print('go through task 5')
    top_submissions = reddit.subreddit(
        'csci040temp').new()  # time_filter='month'
    if chance < .5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        submission = random.choice(list(top_submissions))
    # HINT:
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

    # EXTRA CREDITS
    # 2 credits: post new submissions to the /r/csci040 subreddit from url = 'https://old.reddit.com/r/JoeBiden/'
    top_submissions_ex = reddit.subreddit('politics').top(time_filter='month')
    choose_submission = random.choice(list(top_submissions_ex))
    titles = choose_submission.title
    urls = choose_submission.url
    reddit.subreddit('csci040temp').submit(titles, url=urls)
    print('post new submissions to csci040temp')
    # 2 credits: use the textblob library to measure the sentiment of every comment/submission
    # 5 credits: post reply based on sentiment

# except AssertionError:
#     print('exception found')
#     # python to wait 5 seconds before proceeding
#     print('starting to sleep')
#     time.sleep(60)
#     print('done sleeping')
