# Unit 5 Case Study — setup and classroom guide

Same structure as `coa_avps`: three files, two Google steps and one GitHub step, about 15 minutes in all. You only paste one URL into one place.

```
[ index.html on GitHub Pages ]  --POST-->  [ Code.gs Web App ]  -->  [ Google Sheet: Responses + Summary ]
        the case + questions                 scores each submission      your marks + class debrief view
```

| File | What it is |
| --- | --- |
| `index.html` | The student page: identity → read the case → Parts A–D (13 MCQs, all auto-scored — nothing to correct by hand) |
| `Code.gs` | Apps Script backend: scores out of 13, writes the row, rebuilds the Summary tab |
| `SETUP.md` | This guide |
| `source/cases.py`, `source/build.py`, `source/template.*` | The editable source. Change a case or a question in `cases.py`, run `python build.py`, and both `index.html` and `Code.gs` are regenerated so the answer key always matches the options. |

---

## Step 1 — Sheet + backend (5 min)
1. Create a new Google Sheet, e.g. **COA Unit 5 Case Study Responses**.
2. **Extensions → Apps Script**, delete the starter code, paste all of `Code.gs`, and save.

## Step 2 — Publish as a Web App (3 min)
1. **Deploy → New deployment → Web app**.
2. **Execute as: Me**, **Who has access: Anyone**. Click Deploy and authorize (*Advanced → Go to … → Allow*).
3. Copy the Web app URL (`https://script.google.com/macros/s/…/exec`).

## Step 3 — Wire the URL (1 min)
In `index.html`, replace `PASTE_YOUR_APPS_SCRIPT_WEB_APP_URL_HERE` with that URL.

## Step 4 — GitHub Pages (5 min)
Push this folder to a new **public** repo (e.g. `coa_unit5_case`). Then go to **Settings → Pages → Deploy from branch → main / root**. Share the link it gives you.

**One link per department (recommended).** Add `?case=` to fix the case so students can't pick the wrong one:
- Cyber Security & IoT: `…/coa_unit5_case/?case=cyber`
- AI & ML: `…/coa_unit5_case/?case=aiml`
- ECE: `…/coa_unit5_case/?case=ece`

Without `?case=`, students choose their department from a dropdown.

## Step 5 — Test it yourself
Open the link, use a fake register number, finish all parts and submit. Check that a row appears in **Responses** and that the **Summary** tab has filled in. Then delete your test row and use the menu **Case study → Refresh summary**.

---

## Running the class (case-method flow, about 50 minutes)

| Time | Stage | What happens |
| --- | --- | --- |
| 0–5 min | Set the scene | Tell the story in two lines: "Priya's factory was hacked on Monday morning…". Share the link. |
| 5–30 min | Individual work | Students read the case and answer Parts A–D on their phones or laptops. The **View case** button lets them reopen the case at any time. |
| 30–35 min | Pair check (optional) | Each student explains their Part C decisions to a neighbour. |
| 35–50 min | Debrief | Project the **Summary** tab. Start with any question marked **⚠ discuss in class** (below 60% correct). Ask, "What did the case tell us? Which concept explains it?" End on Q13 (Part D): ask why each wrong recommendation is wrong. |

**Reading the Summary tab:** Part A low means students didn't read the case or exhibits carefully. Part B low means the concept is weak, so reteach it. Part C low means they know the concept but can't apply it to a decision.

## Sheet columns
- Identity: `submittedAt, regno, name, dept, caseId`
- Answers: `A1–A4, B1–B4, C1–C4` (the option text the student chose)
- Scores: `score_A, score_B, score_C` (each out of 4), `score_D` (out of 1), `total_score` (out of 13)
- Per-question correctness: `ok_A1 … ok_D1` (1 or 0; the Summary is built from these)
- Timing: `readSeconds` (time until the student clicked "I have read the case"), `totalSeconds`

## Good to know
- **Shuffling:** question order within each part and the order of options are shuffled per register number. The shuffle is stable on refresh, so neighbours see different orders.
- **Duplicates:** if a student submits twice, both rows are kept, but the Summary counts only their latest one.
- **If you edit `Code.gs` later:** Deploy → Manage deployments → Edit → *New version* → Deploy.
