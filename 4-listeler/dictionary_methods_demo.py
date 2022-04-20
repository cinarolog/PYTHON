# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:32:24 2022

@author: cinar
"""

'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.

best_football_playersOf_All_History = {
    '1': 
        {
            'name': 'Cristiano Ronaldo',
            'yearOfBirth': '1985',
            'nationality': 'Portugal',
            'current_team': 'Portugal',
            'history': ['Juventus', 'Real Madrid', 'Portugal','ManUnited']
        },
        
    '2': 
        {
            'name': 'Lionel Messi',
            'yearOfBirth': '1987',
            'nationality': 'Argentina',
            'current_team': 'Barcelona',
            'history': ['Barcelona', 'Argentina', 'PSG']}
        }

id = input('oyuncu id: ')
name = input('oyuncu ad: ')
nationality = input("ülke: ")
yearOfBirth = input('doğum yılı: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

best_football_playersOf_All_History.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "yearOfBirth": yearOfBirth,
        "current_team": current_team,
        "history": history.split(',')
    }
})

id = input('oyuncu id: ')
name = input('oyuncu ad: ')
nationality = input("ülke: ")
yearOfBirth = input('doğum yılı: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

best_football_playersOf_All_History.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "yearOfBirth": yearOfBirth,
        "current_team": current_team,
        "history": history.split(',')
    }
})




# 2- id' e göre arama yapınız.
id = input('aramak istediğiniz oyuncu id: ')
best_football_playersOf_All_History = best_football_playersOf_All_History.get(id)
print(f'name: {best_football_playersOf_All_History.get("name")}')

# 3- id' e göre bilgi kayıt siliniz.

id = input('silmek istediğiniz oyun id: ')
best_football_playersOf_All_History.pop(id)

best_football_playersOf_All_History(best_football_playersOf_All_History)
