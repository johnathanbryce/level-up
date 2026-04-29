// Best Time to Buy and Sell Stock
//
// You're given an array of stock prices where prices[i] is the price on day i.
// You want to maximize profit by choosing a single day to buy and a different
// (later) day to sell.
//
// Return the maximum profit you can achieve. If no profit is possible, return 0.
//
// Constraints:
//   - You must buy BEFORE you sell.
//   - One buy, one sell — not multiple transactions.
//   - 1 <= prices.length <= 10^5
//   - 0 <= prices[i] <= 10^4

function maxProfit(prices: number[]): number {
  let cheapestPrice = prices[0];
  let bestProfit = 0;

  for (const price of prices) {
    if (price < cheapestPrice) cheapestPrice = price;
    const profitIfSoldToday = price - cheapestPrice;
    bestProfit = Math.max(bestProfit, profitIfSoldToday);
  }

  return bestProfit;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4])); // expected: 5
console.log(maxProfit([7, 6, 4, 3, 1]));    // expected: 0
console.log(maxProfit([2, 4, 1]));          // expected: 2
console.log(maxProfit([1]));                // expected: 0
