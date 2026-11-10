import json,os,sys,shutil
BASE=os.path.expanduser(sys.argv[1]); J=json.load(open(sys.argv[2]))
A=J["A"]; E=J["entries"]
for f in ["_source.html","app.js"]:
    p=os.path.join(BASE,f); s=open(p,encoding="utf-8").read()
    if A[0]["slug"] in s: print("already",f); continue
    for a in A:
        for fs in a["firms"]: assert 'slug:"%s",firm_name'%fs in s, fs
        for j in a["juris"]: assert 'slug:"%s"'%j in s, j
    shutil.copy(p,p+".pre_09nov.bak")
    i=s.index("articles: [")
    j=s.index("\n  ]\n};", i)
    s=s[:j]+",\n"+",\n".join(E)+s[j:]
    k=s.index("const ARTICLE_BODIES = {\n")+len("const ARTICLE_BODIES = {\n")
    s=s[:k]+"".join("  %s:%s,\n"%(json.dumps(a["slug"]),json.dumps(a["body"],ensure_ascii=False)) for a in A)+s[k:]
    open(p,"w",encoding="utf-8").write(s); print("ok",f)
