import json
from cases import CASES, WHY
pub = {}; key={}; qtext={}; info={}
for cid,c in CASES.items():
    pub[cid] = {k:c[k] for k in ("dept","title","subtitle","story","exhibits")}
    pub[cid]["parts"] = {p:[{"id":q["id"],"text":q["text"],"options":q["options"]} for q in qs] for p,qs in c["parts"].items()}
    key[cid] = {q["id"]:q["answer"] for qs in c["parts"].values() for q in qs}
    qtext[cid] = {q["id"]:q["text"] for qs in c["parts"].values() for q in qs}
    info[cid] = {"dept":c["dept"],"title":c["title"],"debrief":c["debrief"]}
j=lambda o: json.dumps(o, ensure_ascii=False, indent=1)
open("../index.html","w").write(open("template.html").read().replace("__CASES__", j(pub)))
open("../Code.gs","w").write(open("template.gs").read().replace("__KEY__", j(key)).replace("__QTEXT__", j(qtext)).replace("__INFO__", j(info)).replace("__WHY__", j(WHY)))
print("built")

# ---- teacher answer key (static, stays on the teacher's laptop — never uploaded)
import os
full = {cid:{k:c[k] for k in ("dept","title","subtitle","story","exhibits","debrief")} for cid,c in CASES.items()}
for cid,c in CASES.items():
    full[cid]["parts"] = {p:[{"id":q["id"],"text":q["text"],"options":q["options"],"answer":q["answer"]} for q in qs] for p,qs in c["parts"].items()}
KEY_OUT = "../teacher/AnswerKey.html"
os.makedirs(os.path.dirname(KEY_OUT), exist_ok=True)
open(KEY_OUT,"w").write(open("template_key.html").read().replace("__CASES__", j(full)).replace("__WHY__", j(WHY)))
print("built answer key")
