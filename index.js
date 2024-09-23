var maxProfit = function (prices) {
    let left = 0;
    let right = 1;
    let maxProfit = 0;

    while (right < prices.length) {
        if (prices[right] > prices[left]) {
            let profit = prices[right] - prices[left];
            if (maxProfit < profit) {
                maxProfit = profit;
            }
        } else {
            left = right;
        }

        right++;
    }

    return maxProfit;

};

console.log(maxProfit([7, 1, 5, 3, 6, 4])); // 5
// console.log(maxProfit([7, 6, 4, 3, 1])); // 0