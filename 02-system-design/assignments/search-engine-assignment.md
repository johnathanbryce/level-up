You're designing a Stack Overflow-style Q&A platform. Users post questions and answers with tags, vote on content, and search for existing questions before posting new ones. Daily stats: 50K new questions/day, 200K searches/day. The product team wants search to handle typos, rank by relevance, and match partial phrases.

Walk me through your search architecture:

Where does the source-of-truth data live?
Do you add Elasticsearch? Why or why not?
How do the two systems stay in sync?
What's the consistency trade-off and why is it acceptable here?

## My Answer

Source of truth data remains in our postgres database. It contains the structured and original data. We would add both Elasticsearch, but we could also leverage pgvector in tandem with the structured data in our postgres database - a hybrid approach. We would need to ensure a robust and accurate embeddings process for our user post data to ensure pgvector could translate NLQ's into results from our data. ES would allow us to use BM25 to match partial phrases and typos as well as relevance ranking. Elasticsearch would be read-only from our database. If any writes are made, there could be a very brief window in which Elasticsearch lags behind the updated postgres data, but it is a decent trade-off given how unlikely it is for a user to create a new post and then have someone query it right away (in under 1 - 2 seconds). This is eventual consistency. 


## Claude's Answer

Source of truth lives in Postgres — questions, answers, votes, tags, user data. Add Elasticsearch as a read-optimized search layer since the requirements (typo tolerance, relevance ranking, partial phrase matching) map directly to what BM25 and ES analyzers provide — SQL LIKE can't rank or handle typos. Sync: writes go to Postgres first, then an event stream (or CDC) copies the data to ES asynchronously. Reads for search hit ES; reads for a specific question's detail page hit Postgres directly. The trade-off is eventual consistency — a new question may not appear in search results for 1-2 seconds — which is acceptable because users rarely search for content that was just posted in the same breath.