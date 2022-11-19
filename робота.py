'''Завдання
Написати програму використовуючи умовний оператор if, цикли for та/aбо while. Програма запитує прізвище англійською перетворює і виводить літерами що складаються із знаку:
 “*” - якщо номер за журналом парний;
“#” - якщо номер за журналом непарний.
Літери формуються знаками згідно варіанту розміром 7 знаків у висоту і 5 знаків у ширину.
зразок літер у додатку 1

приклад виконання програми:
input: PYTHON
output:
****
*   *
*   *
****
*
*                                                                     *

*     *
 *   *
  * *
   *
   *
   *
   *
 *****
   *
   *
   *
   *
   *
   *

 *   *
 *   *
 *   *
 *****
 *   *
 *   *
 *   *

  ***
 *   *
 *   *
 *   *
 *   *
 *   *
  ***

  *    *
  *    *
  **   *
  * *  *
  *  * *
  *   **
  *    *

Оцінка задовільно - вивести 3 перші літери введені з клавіатури
Оцінка добре - вивести до 8-ї літери включно, якщо прізвище довше 8 літер. І доповнити літерами імені якщо менше.
Оцінка відмінно - універсальна програма для виведення будь якого слова введеного з клавіатури.
'''
#texta = str(input("Ввадіть англ.букви: ").lower())
#a=[]
#for a:
letters_list_text = list(map(str, input("Ввадіть англ.букви: ").lower()))

letters_spis_1 = {
    "a":  # A
        '''
         ### 
        #   #
        #   #
        #####
        #   #
        #   #
        #   #
        '''
    ,
    "b":  # B
        '''
        ####
        #   #
        #   #
        ####
        #   #
        #   #
        ####
        '''
    ,
    "c":  # C
        '''
         ###
        #   #
        #
        #
        #
        #   #
         ###
        '''
    ,
    "d":  # D
        '''
        ####         
        #   #   
        #   #
        #   #     
        #   #     
        #   # 
        ####
        '''
    ,
    "e":  # E
        '''
        #####
        #
        #
        ###
        #
        #
        #####
        '''
    ,
    "f":  # F
        '''
        #####
        #
        #
        ###
        #
        #
        #
        '''
    ,
    "g":  # G
        '''
         ###
        #   #
        #
        #  ##
        #   #
        #   #
         ###
        '''
    ,
    "h":  # H
        '''
        #   #           
        #   #    
        #   #   
        #####       
        #   #        
        #   #    
        #   #
        '''
    ,
    "i":  # I
        '''
        ###
         # 
         # 
         # 
         # 
         # 
        ###
        '''
    ,
    "j":  # J
        '''
         ###
          # 
          # 
          # 
          # 
          # 
        ##  
        '''
    ,
    "k":  # K
        '''
        #   #
        #  #
        # #  
        ##   
        # #  
        #  # 
        #   #
        '''
    ,
    "l":  # L
        '''
        #
        #
        #
        #
        #
        #
        #####
        '''
    ,
    "m":  # M
        '''
        #   #
        #   #
        ## ##
        # # #
        #   #
        #   #
        #   #
        '''
    ,
    "n":  # N
        '''
        #   #
        #   #
        ##  #
        # # #
        #  ##
        #   #
        #   #
        '''
    ,
    "o":  # O
        '''
         ### 
        #   #
        #   #
        #   #
        #   #
        #   #
         ### 
        '''
    ,
    "p":  # P
        '''
        ####
        #   #
        #   #
        ####
        #
        #
        #
        '''
    ,
    "q":  # Q
        '''
         ### 
        #   #
        #   #
        #   #
        #   #
        #  # 
         ## #
        '''
    ,
    "r":  # R
        '''
        #### 
        #   #
        #   #
        #### 
        # # 
        #  # 
        #   #
        '''
    ,
    "s":  # S
        '''
         ####
        #    
        #    
         ### 
            #
            #
         ### 
        '''
    ,
    't':  # T
        '''
        #####
          #  
          #  
          #  
          #  
          #  
          #
        '''
    ,
    "u":  # U
        '''
        #   #
        #   #
        #   #
        #   #
        #   #
        #   #
         ###
        '''
    ,
    "v":  # V
        '''
        #   #
        #   #
        #   #
        #   #
        #   #
         # # 
          #  
        '''
    ,
    "w":  # W
        '''
        #   #
        #   #
        #   #
        # # #
        ## ##
        #   #
        #   #
        '''
    ,
    "x":  # X
        '''
        #   #
        #   #
         # # 
          #  
         # # 
        #   #
        #   #
        '''
    ,
    "y":  # Y
        '''
        #   #
        #   #
         # #
          #
          #
          #
          #
        '''
    ,
    "z":  # Z
        '''
        #####
            #
           #
          #
         #
        #
        #####
        '''
}

for bukva_i in letters_list_text:
    print(letters_spis_1.get(bukva_i))

