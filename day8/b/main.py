#!/bin/python3

# Ngl copy/pasted from here
# https://topaz.github.io/paste/#XQAAAQAWCAAAAAAAAAAyGEruliPhOB4Aq+vOBOZlVGo7z+etJSnpenGHLK67Uq2784xx9qvq18LMkRkp4wiVsiE4/MdXGHXFZ+BcAFZvowrxrL8fLdYaJnfs4UZEzzGGfYazw9MTK/uLIJiKu3jT0fNbqc/TH6UI47GQUoNghS+O+PUNkqKe0tFBXcBCDTcmoZud4Qs4XYwesrap7BZ57jq3HrXBuh0uFAzvaXu+SM2i8JywcIyiqONHEFerbPpftjNqGX+K2XgSbfA8FE94/r1nrY8YWSvPKCLc4CL/jAVMI3MfWjsfnN/GLqZCZfdeqId561ZJtjZsrdvQk0nXciCEVFOEhp1AJ85wyHosKwEORgf67Nko5M2ZODFxdv2Qrk9wc4i77NHng+4bS0X7sd1REaiGWFtilseN4UfODYNmhuqdYkA+zoFI9ZqX0Hhx+zdTAY+YhPoIs9bgPWPoVfdFajFZSeGV44CQrtgHFiZVOPQ3X5wWQ/98E31L9iiPf1qWO4QjMSPZk2DkPd1w3G29pMriAuDrG4G8aNI3GjBLYz3KKslXwZAJ5nS/6I/QuRZPb4D2U4zyXj5YeoWRbbUNEUiba/OMpw9Z8e5Rhb8Mz5ISoLHm+Bpr2zedCQ5RX9OZ5Rw3oqoxCPjGvRT4JlIvEuDkvOAhznlQJ5Hr8T408ztCOAYwXWiB4SYo7gsTUntrmy9mj4P2Dx8k2rIkXriobp9Fa71dQqj1EddNlnSka34dKh3XUJXE2ZcLuOAKi3DeYoQFzAEzUgNVmQFpgriZ7hFhAz69MeDsGPAHWPccbnGFbrzwDDFA1SZSfhNLBBH9Shb4Uesh/o6P6VMh/HM8RRL/BHXQ7ouU/6injPY=

# I was struggling to find intersections of digits. I might come back to it sometime
# but on to the next /shrug

data = [l.split(' | ') for l in open('input.txt')]

def find_top(l,r1,r7):
  for e in r7:
    if e not in r1:
      t = e
  return(t)

def find_tl_bl(l5):
  x,y,z= l5
  c=''
  for e in x:
    if e not in y+z:
      c+=e
  for e in y:
    if e not in x+z:
      c+=e
  for e in z:
    if e not in x+y:
      c+=e
  return(c)
    
def find_tr_br(l5,tl,r1):
  for letter in l5:
    if tl in letter:
      if r1[0] in letter:
        br = r1[0]
        tr = r1[1]
      else:
        br = r1[1]
        tr = r1[0]
  return(br,tr)

def part2():
  s=0
  for l,n in data:
    l = l.split()
    r1 = ''.join(sorted([i for i in l if len(i)==2][0]))
    r7 = ''.join(sorted([i for i in l if len(i)==3][0]))
    r4 = ''.join(sorted([i for i in l if len(i)==4][0]))
    r8 = ''.join(sorted([i for i in l if len(i)==7][0]))
    l5 = [i for i in l if len(i)==5]
    t = find_top(l,r1,r7) #The top
    tl_bl = find_tl_bl(l5) #Top-left - Bottom left
    mid = ''.join([e for e in r4 if e not in (r1+tl_bl)]) #mid
    tl = ''.join([e for e in r4 if e not in (r1+mid)]) #top left
    bl = ''.join([e for e in tl_bl if e !=tl]) #top bottom
    br,tr=find_tr_br(l5,tl,r1)
    b = ''.join([i for i in r8 if i not in (t+tr+tl+mid+br+bl)])
    r0 = ''.join(sorted([t,tl,tr,bl,br,b])) 
    r2 = ''.join(sorted([t,tr,mid,bl,b]))
    r3 = ''.join(sorted([t,tr,mid,br,b]))
    r5 = ''.join(sorted([t,tl,mid,br,b]))
    r6 = ''.join(sorted([t,tl,mid,bl,br,b]))
    r9 = ''.join(sorted([t,tl,tr,mid,br,b]))
    l = [r0,r1,r2,r3,r4,r5,r6,r7,r8,r9]
    n = n.split()
    c=''
    for e in n:
      e = ''.join(sorted(e))
      c+= str(l.index(e))
    s += int(c)
  print("Part 2: ",s)
  return()

part2()