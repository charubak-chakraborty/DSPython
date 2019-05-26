#   out of 0-200 tv channels channels that need to be traversed:
#   input sample: 
#   012,044,045,125,126,128,199,001
#   any channels that are banned skips to the next channel(+1) when traversed,
#   banned channels:
#   126,129,199
#   start channel: 
#   1
#   o/p:
#   3,3,1,3,1,1,3,0

allChannels = range(1,200)
channelsToTraverse = [12,44,45,125,126,128,199,1]
bannedChannels = [126,129,199]
sequence = []
current = 1

def skipToNext(curr):
    if allChannels.index(curr) == allChannels.index(199):
        curr = allChannels[0]
    else:
        curr = curr + 1
    return curr

def skipToPrevious(curr):
    if allChannels.index(curr) == allChannels.index(1):
        curr = allChannels[len(allChannels)-1]
    else:
        curr = curr - 1
    return curr

def isNextOrPrevious(curr, target):
    if skipToNext(curr) == target:
        return {"isNextOrPrevious":True,"val":"Next"}
    elif skipToPrevious(curr) == target:
        return {"isNextOrPrevious":True,"val":"Previous"}
    else:
        return {"isNextOrPrevious":False,"val":""}

def skipBannedChannels(curr):
    if curr in bannedChannels:
        print("== banned : {0} ==".format(curr))
        return skipBannedChannels(skipToNext(curr))
    else:
        return curr

# execute traversal
for targetChannel in channelsToTraverse:
    print("== current: {0} target: {1} ==".format(current,targetChannel))
    state = isNextOrPrevious(current,targetChannel)
    # no click needed to traverse
    if current == targetChannel:
        print(0)
        sequence.append(0)
        continue    
    # one click needed to traverse
    elif state["isNextOrPrevious"]:
        print(1)
        sequence.append(1)
        if state["val"] == "Next":
            current = skipToNext(current)
        else:
            current = skipToPrevious(current)
        current = skipBannedChannels(current)
    # three clicks needed to traverse
    else:
        print(3)
        sequence.append(3)
        current = skipBannedChannels(targetChannel)
print(sequence)


