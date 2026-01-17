movies = {
    "action": {
        "Avengers": 5,
        "Spider Man": 4,
        "Batman": 5
    },
    "comedy": {
        "Mr. Bean": 5,
        "Home Alone": 4,
        "Tom and Jerry": 5
    },
    "cartoon":{
        "Frozen": 4,
        "Toy Story": 5,
        "Kung Fu Panda": 4
    },
    "drama":{
        "The Shawshank Redemption": 5,
        "Forrest Gump": 5,
        "The Godfather": 5
    },
    "horror":{
        "The Conjuring": 4,
        "It": 4,
        "A Nightmare on Elm Street": 3
    },
    "series":{
        "Breaking Bad": 5,
        "Game of Thrones": 4,
        "Stranger Things": 2
    }
}

# logic to recommend movies based on genre

print("Welcome to Movie Recommender!")
while True:
    print("\nAvailable genres:")
    for category in movies:
        print(f"- {category}")           
    
    choice = input("\nEnter a genre to get recommendations (or type 'exit' to quit): ").lower()
    if choice == 'exit':
        print("Thank you for using Movie Recommender. Goodbye!")
        break
    if choice not in movies:
        print("Sorry, we don't have recommendations for that genre. Please choose from the available genres.")
        continue
    
    print("\n Movies and Ratings:")
    for movie, rating in movies[choice].items():
        print(f"{movie}: {rating}/5")
    
    liked_movies = input("\nEnter the names of movie you liked from the list above: ")
    if liked_movies in movies[choice]:
        print(f"Great! You liked: {liked_movies}. Enjoy watching!")

        for movie, rating in movies[choice].items():
            if movie != liked_movies and rating>=4:
                print(f"Based on your interest in {liked_movies}, you might also like: {movie} ({rating}/5)")
            else:
                print("No other recommendations available at the moment.")
            again = input("\nWould you like to choose another genre? (yes/no): ").lower()
            if again != 'yes':
                print("Thank you for using Movie Recommender. Goodbye!")
                break  
    