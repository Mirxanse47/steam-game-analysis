# Steam Game Analysis

This project analyzes the relationship between game price, playtime, and player satisfaction using Steam data.

## Dataset
- Total filtered games: 5594
- Story-like games: 4444

## Method
The dataset was cleaned by removing missing values, games with zero playtime, and games with very few reviews.  
A story-like subset was approximated using RPG, Adventure, and Indie genres.

## Results
- Price vs Playtime: 0.323
- Playtime vs Rating: 0.100
- Price vs Rating: 0.220

## Conclusion
The analysis suggests that game price and playtime are not strong predictors of player satisfaction.  
Players appear to value the overall experience more than duration or cost.

## Tools
- Python
- Pandas
- Matplotlib