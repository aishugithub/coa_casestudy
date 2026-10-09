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
| `teacher/AnswerKey.html` | **Your** answer key for projecting in class. Keep it on your laptop and never upload it (it's in `.gitignore`) |
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
| 35–50 min | Debrief | Open `teacher/AnswerKey.html` on the projector and keep the **Summary** tab open beside it. Start with any question marked **⚠ discuss in class** (below 60% correct). Ask, "What did the case tell us? Which concept explains it?" End on Q13 (Part D): ask why each wrong recommendation is wrong. |

**Reading the Summary tab:** Part A low means students didn't read the case or exhibits carefully. Part B low means the concept is weak, so reteach it. Part C low means they know the concept but can't apply it to a decision.

## Sheet columns
- Identity: `submittedAt, regno, name, dept, caseId`
- Answers: `A1–A4, B1–B4, C1–C4` (the option text the student chose)
- Scores: `score_A, score_B, score_C` (each out of 4), `score_D` (out of 1), `total_score` (out of 13)
- Per-question correctness: `ok_A1 … ok_D1` (1 or 0; the Summary is built from these)
- Timing: `readSeconds` (time until the student clicked "I have read the case"), `totalSeconds`

## What students see after submitting
- Their **score only**: out of 13, with Part A–D scores. No answers and no review, so early finishers can't pass answers to others.
- The answer key exists only in `Code.gs` (on Google's side) and in your teacher file below. It is **not** in the student page.

## Teacher answer key (project it in class)
- `teacher/AnswerKey.html` is a static page for **your laptop only**. Double-click to open it in a browser; no internet or server needed.
- It has tabs for Cyber Security & IoT, AI & ML and ECE. Each question has a **Show answer** button that highlights the correct option and shows a one-line reason. There are also **Reveal all** and **Hide all** buttons, plus the debrief points and the full case (collapsed at the top).
- Students' phones show the options in a shuffled order, so talk about the **answer text**, not the letter.
- ⚠ **Never upload the `teacher` folder to GitHub.** It is listed in `.gitignore`, so `git push` skips it. If you upload files by drag-and-drop on the GitHub website instead, upload only `index.html`.

(Advanced: `Code.gs` has a switch `REVEAL_ANSWERS`, set to `false`. Leave it that way.)

## Good to know
- **Shuffling:** question order within each part and the order of options are shuffled per register number. The shuffle is stable on refresh, so neighbours see different orders.
- **Duplicates:** if a student submits twice, both rows are kept, but the Summary counts only their latest one.
- **If you edit `Code.gs` later:** Deploy → Manage deployments → Edit → *New version* → Deploy.
