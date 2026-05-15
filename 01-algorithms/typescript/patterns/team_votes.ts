// Your engineering team is voting on a new team name. Each person submits exactly one vote.
// Find all names tied for the most votes, returned in the order they first appeared on the ballot.
//
// topVotes(["Phoenix", "Nexus", "Phoenix", "Nexus", "Blaze"]) → ["Phoenix", "Nexus"]
// topVotes(["Apollo", "Apollo", "Apollo"])                    → ["Apollo"]
// topVotes(["Red", "Blue", "Green"])                          → ["Red", "Blue", "Green"]
// topVotes(["Titan", "Titan", "Echo", "Titan"])               → ["Titan"]
//
// Constraints: votes.length >= 1, all non-empty strings, return tied winners in first-appearance order

const topVotes = (votes: string[]): string[] => {
  const numOfVoters = votes.length;
  if (numOfVoters <= 1) return [votes[0]];

  // hash map, loop over votes and count each vote
  const votesMap = new Map();
  for (const vote of votes) {
    // have we seen the vote? if so, add to its count
    votesMap.set(vote, (votesMap.get(vote) || 0) + 1);
  }

  // loop over votesMap to get the vote(s) with the most votes
  const maxValue = Math.max(...votesMap.values());

  const winners = Array.from(votesMap.entries())
    .filter(([_, value]) => value === maxValue)
    .map(([key]) => key);

  return winners;
};

// Tests
console.log(topVotes(["Phoenix", "Nexus", "Phoenix", "Nexus", "Blaze"])); // ["Phoenix", "Nexus"]
console.log(topVotes(["Apollo", "Apollo", "Apollo"])); // ["Apollo"]
console.log(topVotes(["Red", "Blue", "Green"])); // ["Red", "Blue", "Green"]
console.log(topVotes(["Titan", "Titan", "Echo", "Titan"])); // ["Titan"]
