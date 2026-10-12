import sys,json
sys.path.insert(0,'/sessions/rcw-019owdimvnztyf9h1uucwxop/mnt/GamblingLawyers.com/_diag_to_delete')
from arts_12oct import A
def esc(t): return t.replace('\\','\\\\').replace('"','\\"')
ents=[];bods=[]
for a in A:
    ents.append('    {slug:"%s",title:"%s",category:"%s",excerpt:"%s",author:"GamblingLawyers.com Editorial Team",author_slug:"",publish_date:"%s",related_jurisdictions:%s,related_firms:%s,related_lawyers:[]},\n'%(a['slug'],esc(a['title']),a['category'],esc(a['excerpt']),a['time'],json.dumps(a['j']),json.dumps(a['f'])))
    bods.append('  "%s":[%s],\n'%(a['slug'],", ".join('"%s"'%esc(p) for p in a['body'])))
    assert len(a['title'])<=60 and len(a['excerpt'])<=145,(a['slug'],len(a['title']),len(a['excerpt']))
    assert 6<=len(a['body'])<=8
base='/Users/cg/Documents/Claude/Projects/GamblingLawyers.com/'
import os
base=os.environ['HOME']+'/mnt/GamblingLawyers.com/'
for f in ['_source.html','app.js']:
    s=open(base+f,encoding='utf-8').read()
    assert a['slug'] not in s
    k='articles: [\n'; i=s.index(k)+len(k); s=s[:i]+''.join(ents)+s[i:]
    k='const ARTICLE_BODIES = {\n'; i=s.index(k)+len(k); s=s[:i]+''.join(bods)+s[i:]
    open(base+f,'w',encoding='utf-8').write(s)
print('ok')
