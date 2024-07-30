var cards = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen', 'King', 'Queen'];
var getCardRanks = { 2: 1, 3: 2, 5: 3, 6: 4, 8: 5, 'Jack': 6, 'Queen': 7, 'King': 8 };
cards.sort((a, b) => getCardRanks[a] - getCardRanks[b]);
var formattedOutput = [];
for (let i = 0, count = 1; i < cards.length; i++, count++) {
    if (cards[i] !== cards[i + 1]) {
        formattedOutput.push(count > 1 ? cards[i] + ' '.repeat(count - 1) + cards[i] : cards[i]);
        count = 0;
    }
}
console.log('[' + formattedOutput.join(', ') + ']');
//output is [2, 3, 5, 6, 8, Jack, Queen Queen, King King]


// Sort the array as per the rules of card game using generic method.
// var cards = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen']
// <!-- Requried Output = [2,3,5,6,8,'Jack','Queen','King']
// Q: Sort the array as per the rules of card game using generic method.
// Choose language of your choice.
// Sample output is attached.
// The code test is based on the rules of Deck card game. Just like we assign numbers to the strings and arrange the strings and integers in ascending order,
// we need to assign the lowest number to Jack and highest number to King. Queen comes in between. So if you arrange them in ascending order the required output will be [2,3,5,6,8,'Jack','Queen','King']