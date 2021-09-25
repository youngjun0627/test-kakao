import numpy as np
import heapq

class WaitQ(object):
    def __init__(self, waitingline, users, n):
        self.q = []
        self.n = n
        self.MAX_TIME = 10
        self.users = []
        for line in waitingline:
            _id = line['id']
            _from = line['from']
            heapq.heappush(self.q, [_from, _id])
            self.users.append(users[_id])
        self.pairs = []
        self.visit = [False] * (n+1)

    def find_user(self, id):
        for user in self.users:
            if user.id==id:
                return user
        return -1


    def sort(self, time, total_visit):
        pair = []
        while self.q:
            from_time, id = heapq.heappop(self.q)
            if time-from_time>self.MAX_TIME:
                _min = 9999999
                A_id = id
                for B in self.q:
                    _, B_id = B
                    if A_id==B_id: continue
                    if total_visit[A_id][B_id]<=_min:
                        _min = total_visit[A_id][B_id]
                        temp = [A_id, B_id]
                self.pairs.append(temp) 
                total_visit[temp[0]][temp[1]]+=1
                total_visit[temp[1]][temp[0]]+=1
                self.visit[A_id] = True
                self.visit[B_id] = True
                continue
            A = self.find_user(id)
            B = A.search(self.users, self.visit, total_visit)
            if B==-1: continue
            self.pairs.append([A.id,B.id])
            total_visit[A.id][B.id]+=1
            total_visit[B.id][A.id]+=1
            self.visit[A.id] = True
            self.visit[B.id] = True
    def pop(self):
        return self.pairs.pop()

    def empty(self):
        return True if not self.pairs else False

def change_skill_grade(skills):
    q = []
    result = []
    for i, v in enumerate(skills):
        heapq.heappush(q, (-v, i+1))
    i = 1
    while q:
        _, id = heapq.heappop(q)
        result.append([id, i])
        i+=1
    return result
        
def create_random_skill(n):
    np.random.seed(42)
    grades = np.random.normal(40000, 20000, size=(n))
    grades = list(map(int, grades))
    grades = [40000 for _ in range(n)]
    return grades

class User(object):
    def __init__(self, user, skill):
        self.id = user['id']
        self.skill = skill
        self.grade = user['grade']
        self.MIN_GRADE = 1000
        self.MAX_GRADE = 100000
        self.from_time = user

    def get(self):
        return [self.id, self.skill]

    def change_taken(self, taken):
        diff = (40-taken)/35*99000
        time = 0
        if diff>50000:
            diff= 50000
        elif diff>25000:
            diff = 25000
        elif diff>12500:
            diff = 12500
        elif diff>6000:
            diff=6000
        elif diff>3000:
            diff=3000
        elif diff>1500:
            diff=1500
        elif diff>750:
            diff = 500
        else:
            diff=100
        return diff

    def win(self, taken):
        diff = self.change_taken(taken)
        diff = diff//4
        print('win', self.id, diff)
        self.skill += diff
        if self.skill > 100000:
            self.skill = 100000
        return self.skill

    def lose(self, taken):
        diff = self.change_taken(taken)
        diff = diff//4
        if diff==0:
            diff = self.skill/100
        print('lose', self.id, diff)
        self.skill -= diff
        if self.skill<1000:
            self.skill = 1000
        return self.skill
    


    def search(self, users, visit, total_visit):
        diff = 999999
        cand = -1
        for user in users[1:]:
            id = user.id
            if id==self.id: continue
            if visit[id]: continue
            if total_visit[self.id][id]<1: 
                cand = user
                break
            if diff>abs(self.skill-user.skill):
                diff = abs(self.skill-user.skill)
                cand = user
        return cand


if __name__=='__main__':
    print(create_random_grade(1))
