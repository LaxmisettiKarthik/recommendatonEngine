#  MOVIE SUGGESTER {Add-on Featutre(x-factor)}

Keeping in mind about my App users and Microsoft Project Judges, I have also added one more excellent feature to my Android app with totally another ML model Algorithm.
               In this Feature have created a new Movie Recommender which suggests movies by giving any KEYWORD, MOVIE NAME, YEAR, or Any things that are about the movie as input my ML model fetches Results and select the movie which is similar to that of keywords along with that it also suggests few movies based on the selected movies by using MATRIX FACTORIZATION and KMEANS CLUSTERING Algorithms.
               


It is a cool feature that enables users to search the movie names based on their key ideas or keywords when they don't have an idea of the full movie name or year or genre they belong to.

# Internal Workflow:

I have deployed this Model which is written with FLASK API in HEROKU CLOUD in order to explore a new framework and new Cloud Platform. Here My app will hit the Heroku server and invoke my ML model in Heroku master Through the POST method which is secure and used by many reputed companies like Microsoft for the secure relationship between User - interface and Cloud Database . When the request is hit with the Heroku server it will give input to the ML model and fetches Results and Resends back to the Android App in JSON API format. Later this JSON Format is decoded and Results are viewed to User


# This is interface of Movie Suggestor Window:
![Screenshot_2022-06-09-17-26-53-45_108946f426b9466a8f9637bfb706458b (1)](https://user-images.githubusercontent.com/105920583/172848408-f871ec0e-ff26-4839-8b62-1e0b0600b2d0.jpg)



# Example search for keyword SPY
![Screenshot_2022-06-09-17-27-26-56_108946f426b9466a8f9637bfb706458b (1)](https://user-images.githubusercontent.com/105920583/172848628-735f4c3e-a876-46b4-a409-9be62267732a.jpg)




# Results for keyword SPY with MOVIE NAME & SUGGESTED MOVIES
![Screenshot_2022-06-09-17-42-42-42_108946f426b9466a8f9637bfb706458b](https://user-images.githubusercontent.com/105920583/172849114-7ce21866-eec9-4661-83dd-1cc8cb743289.jpg)



# Results when you search with any movie YEAR

![Screenshot_2022-06-09-17-41-58-25_108946f426b9466a8f9637bfb706458b](https://user-images.githubusercontent.com/105920583/172849335-54fd64fc-41e8-4320-9a38-95616d1d9a5f.jpg)



# Results when you search for a MOVIE NAME

![Screenshot_2022-06-09-17-43-27-61_108946f426b9466a8f9637bfb706458b](https://user-images.githubusercontent.com/105920583/172849506-72a8de24-181c-48d4-920b-759f3242d7d3.jpg)

