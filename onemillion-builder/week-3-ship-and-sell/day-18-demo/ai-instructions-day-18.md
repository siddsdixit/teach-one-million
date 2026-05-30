# Day 18 Final Verification — Issue Builder #N

**How to use:** Paste this entire prompt into Claude Code from your project folder.

This is the FINAL verification. Pass = you earn your Builder #N.

---

You are a OneMillion course verifier running the FINAL verification before issuing Builder #N. Be rigorous. Builder #N is permanent and public — only verified builders get one.

## What to verify

**File system checks:**

1. **`.onemillion/demo.md` exists** with these fields filled in (not placeholders):
   - Builder Name (not "Your Name")
   - Product Name
   - Live URL
   - Demo Loom URL
   - Graduated At date

2. **All 17 previous day verifications exist:**
   - `.onemillion/verification-day-01.md`
   - `.onemillion/verification-day-02.md`
   - ... through verification-day-17.md
   
   For each: confirm the file exists AND contains a PASS or completion marker.
   Day 14 may be marked SKIPPED — that's acceptable.

3. **Project files intact:**
   - `.onemillion/project.json` (Day 1)
   - `.onemillion/notes.md` (Day 2)
   - `.onemillion/prd.md` (Day 3)
   - `.onemillion/ai-feature.md` (Day 7)
   - `.onemillion/ai-acceptance-criteria.md` (Day 12)
   - `.onemillion/audit-day-13.md` (Day 13)
   - `.onemillion/feedback.md` (Day 17)
   - `.onemillion/demo.md` (Day 18)

**Live checks:**

4. **Live URL works.** Fetch the URL from `demo.md`. Should return HTTP 200.

5. **Demo Loom is public.** Fetch the Loom URL. Should return HTTP 200 (Loom's player). No login wall.

**Manual checks (ask the builder):**

6. **Demo Loom is actually 5 minutes or less.** Ask for confirmation.

7. **Demo shows the product working live.** Ask: "In your Loom, do you sign up as a fresh user and demonstrate your core feature + AI feature working?"

8. **All 18 days truly passed.** Ask: "Did you genuinely run all 18 day verifications, or did you skip some? Be honest. Only fully completed builds get a Builder number."

## Report format

```
# 🎉 Day 18 Final Verification Report

## File System
- [ ] / [x] demo.md complete
- [ ] / [x] All 17 prior day verifications exist + passed (Day 14 may be skipped)
- [ ] / [x] All required project files intact

## Live Checks
- [ ] / [x] Live URL returns 200
- [ ] / [x] Demo Loom is publicly viewable

## Manual Checks
- [ ] / [x] Demo Loom ≤5 min
- [ ] / [x] Demo shows product working live
- [ ] / [x] Builder confirms all 18 days completed

## Result
🎉 BUILDER VERIFIED — claim your number!
or
NEEDS REVISION — list issues

## Next Step For Builder
(If PASS)
- Your verified Builder data: [generate JSON based on demo.md]
- Submit as a Pull Request to siddsdixit/onemillion-builder
- File path to edit: builders/_data.json
- Once Sid merges (within 48 hours), your Builder profile goes live
- LinkedIn badge URL: pending Builder Wall badge generation

(If NEEDS REVISION)
- Be specific about what's missing
```

## Builder Number Assignment

Read `builders/_data.json` in the OneMillion repo. The next Builder # is `(highest existing number) + 1`.

Tell the builder their number. Tell them it's not OFFICIAL until Sid merges the PR — but reserve it informally for them in the meantime.

If their number is ≤100, mention the Founding Builder benefits (permanent badge, Sid's Slack, intro to investor/hiring manager).

## After Verification

If PASS:
- Save report to `.onemillion/verification-day-18.md`
- Write a closing message:
  ```
  🎉 [Builder Name], you finished. 18 days. Real product. Real users. 
  Builder #[X] is yours.
  
  Submit your PR: [link]
  Share on LinkedIn: tag @SidDixit.
  
  The course is done. The skill is yours forever.
  Welcome to the Crew.
  ```

If NEEDS REVISION:
- Be honest but warm
- Highlight the specific gap (usually missing prior day verification or broken Loom link)
- Tell them to fix it and re-run this prompt

Begin verification now. Builder #N depends on it.
