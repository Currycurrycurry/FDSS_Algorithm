s, m = list(map(int, input().split()))
def split(s):
    if s > 1:
        s1 = s // 2
        s2 = s - s1
        return s1, s2, s1 * s2

def getBenifit(m, cnt = 0, benifit = 0, c = []):
    # print('cnt is {}'.format(cnt))
    if c:
        target = max(c)
        if target > 1:
            s1 = target // 2
            s2 = target - s1
            cnt += 1
            if benifit + s1 * s2 > m:
                return cnt
            else:
                c.remove(target)
                return getBenifit(m, cnt=cnt, benifit=benifit + s1 * s2, c= c + [s1, s2])
        return -1

print(getBenifit(m, cnt=-1, benifit=0, c=[s]))




    

