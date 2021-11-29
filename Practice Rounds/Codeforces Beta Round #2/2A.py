def main():
    n = int(input())
    scores = {}
    rounds = []
    for i in range(n):
        round = input()
        rounds.append(round)
        name, val = round.split()
        if name in scores:
            scores[name] += int(val)
        else:
            scores[name] = int(val)


    max_score =  max(scores.values())
    count = 0
    for name in scores:
        if scores[name] == max_score:
            count +=1
            lead = name
    if count == 1:
        print(lead)
        return

    recount = {}
    for i in range(n):
        round = rounds[i]
        name, val = round.split()
        if name in recount:
            recount[name] += int(val)
        else:
            recount[name] = int(val)
        if recount[name] >= max_score and scores[name] == max_score:
            print(name)
            return

if __name__ == "__main__":
    main()
