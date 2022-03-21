import pandas as pd
df = pd.read_csv('weather.csv')

def secondMethod(regressionResult,regressionDay):
    weather = ""
    recommandationMessage = ""
    if regressionResult < 6:
        weather = "cold"
    elif regressionResult >= 6 and regressionResult < 15:
        weather = "warm"
    elif regressionResult >= 15 and regressionResult < 25:
        weather = "hot"
    elif regressionResult >= 25:
        weather = "too hot"

    clothes = {
        1: 'jeans',
        2: 'socks',
        3: 'dress',
        4: 'skirt',
        5: 't-shirt'
    }
    selectedClothes = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
    }

    counter = 0
    for i in range(0, regressionDay-1):
        if df.iloc[i][4] == weather:
            counter +=1

    if counter > 0 and counter < 10:

        for i in selectedClothes:
            index = regressionDay - 2
            count = 0
            while (True):
                if counter == count:
                    break
                if df.iloc[index][4] == weather:
                    for k in range(5, 10):
                        if df.iloc[index][k] == i:
                            selectedClothes[i] += 1
                    count += 1
                index -= 1

    elif counter == 0:
        recommandationMessage = "Unfortunately, the dataset has not data for previous datas about weather"

    else:

        for i in selectedClothes:
            index = regressionDay - 2
            count = 0
            while (True):
                if count == 10:
                    break
                if df.iloc[index][4] == weather:
                    for k in range(5, 10):
                        if df.iloc[index][k] == i:
                            selectedClothes[i] += 1
                    count += 1
                index -= 1


    max_key = max(selectedClothes, key=selectedClothes.get)
    print("Weather : " + weather ,"\n" + "----------------------------------------------------")
    if counter == 0:
        print(recommandationMessage)
    else:
        a = selectedClothes[max_key]
        count = 0
        array = []
        for i in selectedClothes:
            if(selectedClothes[i] == a):
                count += 1
                array.append(clothes[i])

        if count < 3:
            message = "Nowadays, users prefer "
            for i in range(len(array)):
                message = message+"" + array[i]+ " "
            print(message+"about this",weather,"weather")

        else:
            print("Nowadays, users have been ambivalent about this",weather,"weather")

