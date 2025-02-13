with open('26_19752.txt') as f:
    d_points = {}

    d_ans ={}
    for i in f:
        tmp = list(map(int,i.strip().split()))
        d_points[tmp[0]] = tmp[1:]
    for k in d_points:
        d_ans[k] = [sum(d_points[k]), len([x for x in d_points[k] if x > 0]),len([x for x in d_points[k] if x != 0])]
    d_ans.pop(9588)
    sorted_d_ans = dict(sorted(d_ans.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True))
    d1 = {k: sorted_d_ans[k] for k in sorted_d_ans if sorted_d_ans[k][0] > 0}


