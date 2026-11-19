import json,os,sys,urllib.request as u,urllib.error as e
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("no env")
V={"p":100,"n":320,"b":330,"r":500,"q":900,"k":0}
P={"p":100,"n":320,"b":330,"r":500,"q":900,"k":0}
def post(p,b):
 r=u.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with u.urlopen(r)as x:return json.load(x)
 except e.HTTPError as x:sys.exit(f"{p}:{x.code}")
def bd(f):
 b={}
 for i,r in enumerate(f.split()[0].split("/")):
  c=0
  for ch in r:
   if ch.isdigit():c+=int(ch)
   else:b["abcdefgh"[c]+str(8-i)]=ch;c+=1
 return b
def ev(b):
 s=0
 for sq,pc in b.items():
  v=V.get(pc.lower(),0)
  s+=v if pc.isupper() else -v
 return s
def ab(b,d,a,bta,mx):
 if d==0 or not mx:return ev(b),None
 bs=min(mx,key=lambda m:bd(m[0:2]+m[2:4]+m[4:] if len(m)>4 else m[0:2]+m[2:4]))
 best=-9999;bm=None
 for m in mx:
  nb=dict(b)
  mv=m[0:2];tw=m[2:4]
  nb.pop(mv,None)
  if tw in nb:nb.pop(tw)
  if len(m)>4:nb[tw]=m[4].upper() if b[mv].isupper() else m[4]
  else:nb[tw]=b[mv]
  sc,_=ab(nb,d-1,-bta,-a,[])
  sc=-sc
  if sc>best:best=sc;bm=m
 return best,bm
def pick(f,lg):
 b=bd(f)
 if len(lg)==1:return lg[0]
 best=-9999;bm=lg[0]
 for m in lg:
  nb=dict(b)
  mv=m[0:2];tw=m[2:4]
  nb.pop(mv,None)
  if tw in nb:nb.pop(tw)
  if len(m)>4:nb[tw]=m[4].upper() if b[mv].isupper() else m[4]
  else:nb[tw]=b[mv]
  sc,_=ab(nb,2,-9999,9999,lg[1:])
  sc=-sc
  if sc>best:best=sc;bm=m
 return bm
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  g=post("/move",{"game":g["game"],"move":pick(g["fen"],g["legal_moves"])})
 print(f"{g['game']}:{g['outcome']}",file=sys.stderr)
print(f"{g.get('wins',0)}w/{g.get('draws',0)}d/{g.get('losses',0)}l",file=sys.stderr)