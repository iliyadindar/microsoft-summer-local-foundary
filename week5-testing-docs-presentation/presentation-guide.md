# Demo Day Presentation Guide

Ten minutes per team: about six of slides/talking, three of live demo, one
for questions. Rehearse at least twice — the second run is always better.

## Structure

1. **Problem statement (1 min).** Who needs this and why does *local* matter
   for them? (Privacy? Offline? Cost?) Name your assistant — it helps more
   than you'd think.
2. **How it works (2 min).** One architecture diagram, walked through with
   one real question: "watch this question become a vector, find these two
   chunks, and land in this prompt." No code on slides — show code only if
   someone asks.
3. **Live demo (3 min).** Prepare exactly three questions:
   - one impressive answerable question (with citation),
   - one paraphrase that shares no words with the document (the embeddings
     party trick),
   - one unanswerable question it correctly declines. Say it out loud:
     *"declining to invent an answer is a feature we built."*
4. **Lessons learned (2 min).** Your best bug story — what broke, how you
   found it, what fixed it — lands better than any feature list.
5. **Questions (rest).**

## Demo hygiene

- Pre-flight 30 minutes before: service running, models cached (first load
  is slow — do it before, not during), database ingested, terminal font huge.
- Have a screenshot/recording of every demo answer as backup. If the live
  demo stumbles, narrate the backup without apology — that's professionalism,
  not cheating.
- Never type a demo question you haven't tried before. Improvise only in the
  Q&A, and frame it as the gamble it is.

## Questions the audience will ask (prepare answers)

- "What happens if you ask it something not in the documents?" (demo #3!)
- "How is this different from just using ChatGPT?" (grounding, privacy,
  offline, your own data)
- "Could this work with [my documents]?" (yes — that's the point; what would
  change is only the ingestion folder)
- "Why do answers take a few seconds?" (CPU inference; trade-off you chose
  deliberately)
