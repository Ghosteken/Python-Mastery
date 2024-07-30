// Define the cards array
var cards = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen', 'King', 'Queen'];

// Define the ranking for each card
var getCardRanks = {
    2: 1,
    3: 2,
    5: 3,
    6: 4,
    8: 5,
    'Jack': 6,
    'Queen': 7,
    'King': 8
};

// Sort the cards based on their ranks
cards.sort(function(a, b) {
    return getCardRanks[a] - getCardRanks[b];
});

// Format the sorted cards using a single loop
var formattedOutput = [];
var currentCard = cards[0];
var count = 1;

for (let i = 1; i < cards.length; i++) {
    if (cards[i] === currentCard) {
        count++;
    } else {
        if (count > 1) {
            if (currentCard === 'King') {
                formattedOutput.push(currentCard + ' ' + currentCard);
            } else {
                formattedOutput.push(currentCard + ' ' + currentCard);
            }
        } else {
            formattedOutput.push(currentCard);
        }
        currentCard = cards[i];
        count = 1;
    }
}
// Add the last card(s) to the formatted output
if (count > 1) {
    if (currentCard === 'King') {
        formattedOutput.push(currentCard + ' ' + currentCard);
    } else {
        formattedOutput.push(currentCard + ' ' + currentCard);
    }
} else {
    formattedOutput.push(currentCard);
}

console.log('[' + formattedOutput.join(', ') + ']');
// Output: [2, 3, 5, 6, 8, 'Jack', 'Queen Queen', 'King King']
