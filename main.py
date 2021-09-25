from API import startAPI, waitinglineAPI, gameresultAPI, userinfoAPI, matchAPI, changegradeAPI, scoreAPI
from helper import WaitQ, User, create_random_skill, change_skill_grade
import numpy as np

def main(problem_id):
    url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
    token = startAPI(url, problem_id)
    time = 0
    n = 30 if problem_id==1 else 900
    total_visit = [[0] *(n+1) for _ in range(n+1)]
    #users = [User(i, grades[i]) for i in range(n)]
    skills = [-1] + create_random_skill(n)
    while time<50000:
        waiting_line = waitinglineAPI(url, token)
        users = userinfoAPI(url, token)
        game_result = gameresultAPI(url, token)
        users = [None] +[User(user, skills[user['id']]) for user in users]
        for result in game_result:
            win, lose, taken = result['win'], result['lose'], result['taken']
            if skills[win]<skills[lose] and (3<=taken<=10) and np.random.randn(1)<0.2 and problem_id==2:
                skill = users[lose].win(taken)
                skills[lose] = skill
                skill = users[win].lose(taken)
                skills[win] = skill
            else:
                skill = users[win].win(taken)
                skills[win] = skill
                skill = users[lose].lose(taken)
                skills[lose] = skill
        wait_q = WaitQ(waiting_line, users, n)
        wait_q.sort(time, total_visit)
        '''
        while not wait_q.empty():
            from_time, id = wait_q.pop()
            pair.append(id)
            if len(pair)==2:
                pairs.append(pair[:])
                pair.clear()
        '''
        pairs = []
        if not wait_q.empty(): 
            pairs = wait_q.pairs
        result = matchAPI(url, token, pairs)
        print(result)
        if result['status']=='finished':
            break
        commands = []
        for idx, value in change_skill_grade(skills[1:]):
            commands.append({'id':idx, 'grade':value})
        result = changegradeAPI(url, token, commands)
        if result['status']=='finished':
            break
        time+=1
        with open('output{}.txt'.format(problem_id), 'w') as f:
            f.write(str(skills))
    print(scoreAPI(url, token))
    
if __name__=='__main__':
    main(1)
