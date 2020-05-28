def approxPatternMatching(Pattern, Text, d):
    patternArray = []
    for i in range(0,len(Text)-len(Pattern)+1):
        flag = 0
        for j in range(i,i+len(Pattern)):
            if Text[j] == Pattern[j-i]:
                flag+=1
        if flag >= len(Pattern)-d:
            patternArray.append(i)
    return patternArray
