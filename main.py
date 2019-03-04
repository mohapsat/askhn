import time
import requests
import operator
import json

# hn_topstory_uri = 'https://hacker-news.firebaseio.com/v0/topstories.json'

hn_topasks_uri = 'https://hacker-news.firebaseio.com/v0/askstories.json'


# Get top 10 stories
# r_topstory_10 = requests.get(hn_topstory_uri).json()[:10]

r_topasks = requests.get(hn_topasks_uri).json()[:200]

score = list()
ask = list()

for r_topask_id in r_topasks:
    # 2. Get contents of the r_topstory_id from https://hacker-news.firebaseio.com/v0/item/<id>.json
    topask_dtl_uri = 'https://hacker-news.firebaseio.com/v0/item/' + str(r_topask_id) + '.json'
    # topstory_dtl_title = requests.get(topstory_dtl_uri).json()['title']
    try:
        topask_text = requests.get(topask_dtl_uri).json()['title'].replace('Ask HN: ', '')
        topask_score = requests.get(topask_dtl_uri).json()['score']
        # topask_url = requests.get(topask_dtl_uri).json()['']

        if topask_score >= 10:
            # print(f'SCORE:{topask_score} ASK: {topask_text}')
            score.append(topask_score)
            ask.append(topask_text)
        else:
            pass
    except Exception as e:
        print(f'ERROR: {str(e)}')

questions = dict(zip(score, ask))


# q_sorted_by_score = sorted(questions.items(), key=operator.itemgetter(0))

print(json.dumps(questions, indent=4, sort_keys=True))
    # time.sleep(2) # sleep 2s
print('completed!')




# Tweeted top 10



