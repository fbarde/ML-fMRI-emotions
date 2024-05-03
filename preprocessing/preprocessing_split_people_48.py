import numpy as np
import math
import pandas as pd 



def combine_brain_emotions_per_movie(movies, emotion, output_path):
    ''' This function combines the preprocessed brain and emotion data 
        for one movie in a matrix of format (4*l) x (400 + 1 )
        -> 4 watches per movie, l = length after normalizing over several samplings
        -> 400 averages of brain regions, 1 column for emotions
        Input: 
            movies: array of strings with names of movies (should be 4 -> 4 views per movie), preprocessed
            emotion: string, name of preprocessed emotions file, for that specific movie
            output_path: string, name of location where the output should be saved
        Output:
            a .csv file combining the preprocessed emotion and brain data'''

    # load emotion data
    emotion_data = np.genfromtxt(emotion)
    l = emotion_data.shape[0]
    
    # putting the movie data together
    count = 0
    for idx, movie in enumerate(movies):
        # load movie data
        movie_data = np.genfromtxt(movie, delimiter=",")
        N = movie_data.shape[0] # number of samples
        #D = movie_data.shape[1] # number of features, i.e. brain regions, should be 400
        if N != l: 
            print ("Length of movie "+ str(movie) + " = " + str(N) + " doesn't match with length of preprocessed emotion") 
            break
        # no output data yet (1st iteration)
        if count == 0:
            out_movies = movie_data
        # concatenate movies
        else:
            out_movies = np.concatenate((out_movies, movie_data), axis=0)

        count = count + 1
    
    # putting the emotion data together
 
    out_emotions = np.tile(emotion_data, count)


    # putting everything together

    out_combined = np.concatenate((out_movies, out_emotions[:, None]), axis=1)

    # saving the output
    pd.DataFrame(out_combined).to_csv(output_path,header=None, index=None)
        
    return 0


def combine_brain_emotions(movies, output_path):
    ''' This function puts together the data (brain and emotion) from all movies in one big matrix
    Input: 
        movies: array of strings with names of movies (Combined_...)
        output_path: string, name of location where the output should be saved
    Output:
        a .csv file combining the data for all movies'''
    
    count = 0
    for idx, movie in enumerate(movies):
        # reading the data
        movie_data = np.genfromtxt(movie, delimiter=",")
        # no output data yet (1st iteration)
        if count == 0:
            out_movies = movie_data
        # concatenate movies
        else:
            out_movies = np.concatenate((out_movies, movie_data), axis=0)
        
        count = count + 1
    
    # saving the output
    pd.DataFrame(out_movies).to_csv(output_path,header=None, index=None)




    return 0

def split_people(split_range, final_output_test, final_output_train):
    ''' This function creates the big matrix used to train the model, but only for a subset of all movies
    Input: 
        split_range: percentage of data used for testing (i.e. split_range = 0.7 -> 70% used for testing)
        final_output_test: string, name of location where the test data should be saved
        final_output_train: string, name of location where the train data should be saved
    Output:
        a .csv file combining the data for all movies in the split range'''

     
    #################################################
    # TEST DATA
    #################################################


    ########################################
    # AFTER THE RAIN
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:

    movies_AfterTheRain = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_AfterTheRain.append("brain/AfterTheRain_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_AfterTheRain = "datas/Emotions_AfterTheRain.csv"

    # enter the output path
    output_path_AfterTheRain = "results/Combined_AfterTheRain.csv"

    combine_brain_emotions_per_movie(movies_AfterTheRain, emotion_AfterTheRain, output_path_AfterTheRain)
    print("After the rain done")

    ########################################
    # BETWEEN VIEWINGS
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_BetweenViewings = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_BetweenViewings.append("brain/BetweenViewings_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_BetweenViewings = "datas/Emotions_BetweenViewings.csv"

    # enter the output path
    output_path_BetweenViewings = "results/Combined_BetweenViewings.csv"

    combine_brain_emotions_per_movie(movies_BetweenViewings, emotion_BetweenViewings, output_path_BetweenViewings)
    print("Between Viewings done")

    ########################################
    # BICK BUCK BUNNY
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_BickBuckBunny = []

    for num in range(1,int(np.floor(split_range*17))):

        movies_BickBuckBunny.append("brain/BigBuckBunny_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_BickBuckBunny = "datas/Emotions_BigBuckBunny.csv"

    # enter the output path
    output_path_BickBuckBunny = "results/Combined_BickBuckBunny.csv"

    combine_brain_emotions_per_movie(movies_BickBuckBunny, emotion_BickBuckBunny, output_path_BickBuckBunny)

    print("Bick Buck Bunny done")

    ########################################
    # CHATTER
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Chatter = []

    for num in range(1,int(np.floor(split_range*18))):

        movies_Chatter.append("brain/Chatter_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Chatter = "datas/Emotions_Chatter.csv"

    # enter the output path
    output_path_Chatter = "results/Combined_Chatter.csv"

    combine_brain_emotions_per_movie(movies_Chatter, emotion_Chatter, output_path_Chatter)

    print("Chatter done")

    ########################################
    # FIRST BITE
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_FirstBite = []

    for num in range(1,int(np.floor(split_range*17))):

        movies_FirstBite.append("brain/FirstBite_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_FirstBite = "datas/Emotions_FirstBite.csv"

    # enter the output path
    output_path_FirstBite = "results/Combined_FirstBite.csv"

    combine_brain_emotions_per_movie(movies_FirstBite, emotion_FirstBite, output_path_FirstBite)

    print("First Bite done")

    ########################################
    # LESSONS LEARNED
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_LessonLearned = []
    for num in range(1,int(np.floor(split_range*17))):

        movies_LessonLearned.append("brain/LessonLearned_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_LessonLearned = "datas/Emotions_LessonLearned.csv"

    # enter the output path
    output_path_LessonLearned = "results/Combined_LessonLearned.csv"

    combine_brain_emotions_per_movie(movies_LessonLearned, emotion_LessonLearned, output_path_LessonLearned)

    print("Lesson Learned done")

    ########################################
    # PAYLOAD
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Payload = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_Payload.append("brain/Payload_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Payload = "datas/Emotions_Payload.csv"

    # enter the output path
    output_path_Payload = "results/Combined_Payload.csv"

    combine_brain_emotions_per_movie(movies_Payload, emotion_Payload, output_path_Payload)

    print("Payload done")


    ########################################
    # SINTEL
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Sintel = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_Sintel.append("brain/Sintel_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Sintel = "datas/Emotions_Sintel.csv"

    # enter the output path
    output_path_Sintel = "results/Combined_Sintel.csv"

    combine_brain_emotions_per_movie(movies_Sintel, emotion_Sintel, output_path_Sintel)

    print("Sintel done")

    ########################################
    # SPACEMAN
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Spaceman = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_Spaceman.append("brain/Spaceman_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Spaceman = "datas/Emotions_Spaceman.csv"

    # enter the output path
    output_path_Spaceman = "results/Combined_Spaceman.csv"

    combine_brain_emotions_per_movie(movies_Spaceman, emotion_Spaceman, output_path_Spaceman)

    print("Spaceman done")

    ########################################
    # SUPERHERO
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Superhero = []
    for num in range(1,int(np.floor(split_range*17))):

        movies_Superhero.append("brain/Superhero_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Superhero = "datas/Emotions_Superhero.csv"

    # enter the output path
    output_path_Superhero = "results/Combined_Superhero.csv"

    combine_brain_emotions_per_movie(movies_Superhero, emotion_Superhero, output_path_Superhero)

    print("Superhero done")

    ########################################
    # TEARS OF STEEL
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_TearsOfSteel = []
    for num in range(1,int(np.floor(split_range*17))):

        movies_TearsOfSteel.append("brain/TearsOfSteel_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_TearsOfSteel = "datas/Emotions_TearsOfSteel.csv"

    # enter the output path
    output_path_TearsOfSteel = "results/Combined_TearsOfSteel.csv"

    combine_brain_emotions_per_movie(movies_TearsOfSteel, emotion_TearsOfSteel, output_path_TearsOfSteel)

    print("Tears of Steel done")

    
    ########################################
    # THE SECRET NUMBER
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_TheSecretNumber = []
    for num in range(1,int(np.floor(split_range*17))):

        movies_TheSecretNumber.append("brain/TheSecretNumber_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_TheSecretNumber = "datas/Emotions_TheSecretNumber.csv"

    # enter the output path
    output_path_TheSecretNumber = "results/Combined_TheSecretNumber.csv"

    combine_brain_emotions_per_movie(movies_TheSecretNumber, emotion_TheSecretNumber, output_path_TheSecretNumber)

    print("The Secret Number done")

    ########################################
    # TO CLAIRE FROM SUNNY
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_ToClaireFromSunny = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_ToClaireFromSunny.append("brain/ToClaireFromSonny_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_ToClaireFromSunny = "datas/Emotions_ToClaireFromSonny.csv"

    # enter the output path
    output_path_ToClaireFromSunny = "results/Combined_ToClaireFromSunny.csv"

    combine_brain_emotions_per_movie(movies_ToClaireFromSunny, emotion_ToClaireFromSunny, output_path_ToClaireFromSunny)

    print("To Claire from Sonny done")

    ########################################
    # YOU AGAIN
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_YouAgain = []
    for num in range(1,int(np.floor(split_range*18))):

        movies_YouAgain.append("brain/YouAgain_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_YouAgain = "datas/Emotions_YouAgain.csv"

    # enter the output path
    output_path_YouAgain = "results/Combined_YouAgain.csv"

    combine_brain_emotions_per_movie(movies_YouAgain, emotion_YouAgain, output_path_YouAgain)

    print("You Again done")


    ########################################
    # TODO: put all output paths names in the list
    ########################################

    all_movies = [output_path_AfterTheRain,
                output_path_BetweenViewings,
                output_path_BickBuckBunny,
                output_path_Chatter,
                output_path_FirstBite,
                output_path_LessonLearned,
                output_path_Payload,
                output_path_Sintel,
                output_path_Spaceman,
                output_path_Superhero,
                output_path_TearsOfSteel,
                output_path_TheSecretNumber,
                output_path_ToClaireFromSunny,
                output_path_YouAgain]


    combine_brain_emotions(all_movies, final_output_test)

    print('Data for testing done')
 
    #################################################
    # TRAIN DATA
    #################################################

    
    ########################################
    # AFTER THE RAIN
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:

    movies_AfterTheRain = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_AfterTheRain.append("brain/AfterTheRain_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_AfterTheRain = "datas/Emotions_AfterTheRain.csv"

    # enter the output path
    output_path_AfterTheRain = "results/Combined_AfterTheRain.csv"

    combine_brain_emotions_per_movie(movies_AfterTheRain, emotion_AfterTheRain, output_path_AfterTheRain)
    print("After the rain done")

    ########################################
    # BETWEEN VIEWINGS
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_BetweenViewings = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_BetweenViewings.append("brain/BetweenViewings_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_BetweenViewings = "datas/Emotions_BetweenViewings.csv"

    # enter the output path
    output_path_BetweenViewings = "results/Combined_BetweenViewings.csv"

    combine_brain_emotions_per_movie(movies_BetweenViewings, emotion_BetweenViewings, output_path_BetweenViewings)
    print("Between Viewings done")

    ########################################
    # BICK BUCK BUNNY
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_BickBuckBunny = []

    for num in range(int(np.floor(split_range*17)),17):

        movies_BickBuckBunny.append("brain/BigBuckBunny_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_BickBuckBunny = "datas/Emotions_BigBuckBunny.csv"

    # enter the output path
    output_path_BickBuckBunny = "results/Combined_BickBuckBunny.csv"

    combine_brain_emotions_per_movie(movies_BickBuckBunny, emotion_BickBuckBunny, output_path_BickBuckBunny)

    print("Bick Buck Bunny done")

    ########################################
    # CHATTER
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Chatter = []

    for num in range(int(np.floor(split_range*18)),18):

        movies_Chatter.append("brain/Chatter_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Chatter = "datas/Emotions_Chatter.csv"

    # enter the output path
    output_path_Chatter = "results/Combined_Chatter.csv"

    combine_brain_emotions_per_movie(movies_Chatter, emotion_Chatter, output_path_Chatter)

    print("Chatter done")

    ########################################
    # FIRST BITE
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_FirstBite = []

    for num in range(int(np.floor(split_range*17)),17):

        movies_FirstBite.append("brain/FirstBite_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_FirstBite = "datas/Emotions_FirstBite.csv"

    # enter the output path
    output_path_FirstBite = "results/Combined_FirstBite.csv"

    combine_brain_emotions_per_movie(movies_FirstBite, emotion_FirstBite, output_path_FirstBite)

    print("First Bite done")

    ########################################
    # LESSONS LEARNED
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_LessonLearned = []
    for num in range(int(np.floor(split_range*17)),17):

        movies_LessonLearned.append("brain/LessonLearned_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_LessonLearned = "datas/Emotions_LessonLearned.csv"

    # enter the output path
    output_path_LessonLearned = "results/Combined_LessonLearned.csv"

    combine_brain_emotions_per_movie(movies_LessonLearned, emotion_LessonLearned, output_path_LessonLearned)

    print("Lesson Learned done")

    ########################################
    # PAYLOAD
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Payload = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_Payload.append("brain/Payload_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Payload = "datas/Emotions_Payload.csv"

    # enter the output path
    output_path_Payload = "results/Combined_Payload.csv"

    combine_brain_emotions_per_movie(movies_Payload, emotion_Payload, output_path_Payload)

    print("Payload done")


    ########################################
    # SINTEL
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Sintel = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_Sintel.append("brain/Sintel_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Sintel = "datas/Emotions_Sintel.csv"

    # enter the output path
    output_path_Sintel = "results/Combined_Sintel.csv"

    combine_brain_emotions_per_movie(movies_Sintel, emotion_Sintel, output_path_Sintel)

    print("Sintel done")

    ########################################
    # SPACEMAN
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Spaceman = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_Spaceman.append("brain/Spaceman_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Spaceman = "datas/Emotions_Spaceman.csv"

    # enter the output path
    output_path_Spaceman = "results/Combined_Spaceman.csv"

    combine_brain_emotions_per_movie(movies_Spaceman, emotion_Spaceman, output_path_Spaceman)

    print("Spaceman done")

    ########################################
    # SUPERHERO
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_Superhero = []
    for num in range(int(np.floor(split_range*17)),17):

        movies_Superhero.append("brain/Superhero_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_Superhero = "datas/Emotions_Superhero.csv"

    # enter the output path
    output_path_Superhero = "results/Combined_Superhero.csv"

    combine_brain_emotions_per_movie(movies_Superhero, emotion_Superhero, output_path_Superhero)

    print("Superhero done")

    ########################################
    # TEARS OF STEEL
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_TearsOfSteel = []
    for num in range(int(np.floor(split_range*17)),17):

        movies_TearsOfSteel.append("brain/TearsOfSteel_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_TearsOfSteel = "datas/Emotions_TearsOfSteel.csv"

    # enter the output path
    output_path_TearsOfSteel = "results/Combined_TearsOfSteel.csv"

    combine_brain_emotions_per_movie(movies_TearsOfSteel, emotion_TearsOfSteel, output_path_TearsOfSteel)

    print("Tears of Steel done")

    
    ########################################
    # THE SECRET NUMBER
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_TheSecretNumber = []
    for num in range(int(np.floor(split_range*17)),17):

        movies_TheSecretNumber.append("brain/TheSecretNumber_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_TheSecretNumber = "datas/Emotions_TheSecretNumber.csv"

    # enter the output path
    output_path_TheSecretNumber = "results/Combined_TheSecretNumber.csv"

    combine_brain_emotions_per_movie(movies_TheSecretNumber, emotion_TheSecretNumber, output_path_TheSecretNumber)

    print("The Secret Number done")

    ########################################
    # TO CLAIRE FROM SUNNY
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_ToClaireFromSunny = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_ToClaireFromSunny.append("brain/ToClaireFromSonny_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_ToClaireFromSunny = "datas/Emotions_ToClaireFromSonny.csv"

    # enter the output path
    output_path_ToClaireFromSunny = "results/Combined_ToClaireFromSunny.csv"

    combine_brain_emotions_per_movie(movies_ToClaireFromSunny, emotion_ToClaireFromSunny, output_path_ToClaireFromSunny)

    print("To Claire from Sonny done")

    ########################################
    # YOU AGAIN
    ########################################

    # enter all movies in the form results/(movie_name)_averaged.csv
    # List has to be in right order:
    # movie_1_person_1, movie_1_person_2, movie_1_person_4, movie_1_person_4
    movies_YouAgain = []
    for num in range(int(np.floor(split_range*18)),18):

        movies_YouAgain.append("brain/YouAgain_TC_48_average_" + str(num) +".csv")

    # enter the name of the preprocessed emotion file corresponding to the movie
    emotion_YouAgain = "datas/Emotions_YouAgain.csv"

    # enter the output path
    output_path_YouAgain = "results/Combined_YouAgain.csv"

    combine_brain_emotions_per_movie(movies_YouAgain, emotion_YouAgain, output_path_YouAgain)

    print("You Again done")


    ########################################
    # TODO: put all output paths names in the list
    ########################################

    all_movies = [output_path_AfterTheRain,
                output_path_BetweenViewings,
                output_path_BickBuckBunny,
                output_path_Chatter,
                output_path_FirstBite,
                output_path_LessonLearned,
                output_path_Payload,
                output_path_Sintel,
                output_path_Spaceman,
                output_path_Superhero,
                output_path_TearsOfSteel,
                output_path_TheSecretNumber,
                output_path_ToClaireFromSunny,
                output_path_YouAgain]


    combine_brain_emotions(all_movies, final_output_train)
    print('Data for training done')



def main():
    # Split 90 - 10
    final_output_test = "results/Split_data/Combined_All_Test_90.csv"
    final_output_train = "results/Split_data/Combined_All_Train_90.csv"
    split_range = 0.9
    split_people(split_range, final_output_train, final_output_test)


    # Split 80 - 20
    final_output_test = "results/Split_data/Combined_All_Test_80.csv"
    final_output_train = "results/Split_data/Combined_All_Train_80.csv"
    split_range = 0.8
    split_people(split_range, final_output_train, final_output_test)

    # Split 70 - 30
    final_output_test = "results/Split_data/Combined_All_Test_70.csv"
    final_output_train = "results/Split_data/Combined_All_Train_70.csv"
    split_range = 0.7
    split_people(split_range, final_output_train, final_output_test)
    
    # Split 60 - 40
    final_output_test = "results/Split_data/Combined_All_Test_60.csv"
    final_output_train = "results/Split_data/Combined_All_Train_60.csv"
    split_range = 0.6
    split_people(split_range, final_output_train, final_output_test)



if __name__ == "__main__":
    main()


