from collections import deque

STANDARD_LAYOUT = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ "
#STANDARD_LAYOUT = "abcdefghijklmnopqrstuvwxyz" 

def encode(msg):
    keyboard = deque(STANDARD_LAYOUT)
    output = []
    for char in msg:
        key_idx = STANDARD_LAYOUT.index(char)
        output_char = keyboard[key_idx]
        output.append(output_char)
        keyboard.remove(char)
        keyboard.appendleft(char)
    return "".join(output) 

def decode(msg):
    keyboard = deque(STANDARD_LAYOUT)
    output = []
    for char in msg:
        key_idx = keyboard.index(char)
        output_char = STANDARD_LAYOUT[key_idx]
        output.append(output_char)
        keyboard.remove(output_char)
        keyboard.appendleft(output_char)
    return "".join(output) 

def compare(str1, str2):
    i = 0
    while i < len(str1) and i < len(str2):
        char1, char2 = str1[i], str2[i]
        if char1 != char2:
            print(char1, char2, "mismatch")
        else:
            print(char1, char2)
        i += 1

print(decode(r"liw=m wt]0b/]0h05/y96/wb24n/'6x-pk1p13`/0=464-k4zw/m]3`b/9194o'0299o/a`18/32r,,1,2a/kgy`az/6/21.gg`g1./;myy6x/81;sh/vq/'6gv`7/7`v/6'pv/'60;6/`;,lp8q'/y1k`.pq6z/ha6cqj,w,;/q5f,wq6/wdfg,6/rp,6/`dk5.v/1bwwbk.b6cgbz/5w,og5;/5ffg;65k/5f/kopgo/6,v/5;ov/b0,k\d5z/dj,84p/pjdq3l/3--pjem7pjvn4q3q/3-v.p3;/\d;;d5v/htk3/;3]hk.3/e[/3]y0ybh3d.y;/3.b/2koy/3h00.].yg4.j/jgj]/\.0bxh2r'/4bjm]/5sr5r1m/1s[,/6pj3lpl,v/xl.v,mk/]f2o,\.9ok'/k,h\f/q61dvnd1/jf2f/ld/k1wgkc2/k19o2c131'/jcj[/h5r2p12/ro/9v\xrf/jd[/1[[pk21j'"))
