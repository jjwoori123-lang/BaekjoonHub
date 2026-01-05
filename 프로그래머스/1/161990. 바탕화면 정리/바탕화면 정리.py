def solution(wallpaper):
    answer = []
    lx, ly, rx, ry = int(1e9),int(1e9),0,0
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == "#":
                lx = min(lx, x)
                rx = max(rx, x)
                ly = min(ly, y)
                ry = max(ry, y)
    answer= [lx, ly, rx+1, ry+1]       
    return answer