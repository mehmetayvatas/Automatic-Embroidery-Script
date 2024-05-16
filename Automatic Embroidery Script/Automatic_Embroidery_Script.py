import subprocess
import pyautogui
import pyodbc
import time
import pyperclip

def Start_Program():
    program_yolu = r"C:\Program Files (x86)\G7Solutions\FlorianiTotalControl\FlorianiPro.exe"  
    subprocess.Popen(program_yolu, shell=True)
    time.sleep(10) 
    pyautogui.click(x=734, y=798) #Programda Açýlýþ Koordinatlarý
    pyautogui.click(x=24, y=94)
    pyautogui.click(x=682, y=564)

def sql_veri_cek():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.1.10.2;DATABASE=URUNYONETIMI;UID=sa;PWD=Sa1234')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM MONOGRAM_DETAY')
    
    for row in cursor.fetchall():
        if not row.YAPILDI: 
            
            
            
             if row.FONT not in ["Angelic Curls", "Arial", "Bamboo", "Bauhaus", "Benquiat", "Bordeaux", "Brush", "Diana-Vs", "Freehand", "Giddyup", "Impress", "Jester Pro", "Kids", "Manila", "Old_Engl", "Pepita", "Ribbon Love", "Swiss", "Tango", "Times", "Trad_Scr", "Univeri"]:
                continue
                
             pyperclip.copy(row.YAZI)
             pyautogui.click(x=1625, y=172)  #Text Alaný Koordinatlarý
             pyautogui.hotkey('ctrl', 'a') 
             pyautogui.hotkey('ctrl', 'v')

             font_harfleri = { "Angelic Curls": ("a", 1),
                               "Arial": ("a", 4),
                               "Athletic": ("a", 10),
                               "Bamboo": ("b", 0),
                               "Bauhaus": ("b", 1),
                               "Benquiat": ("b", 3),
                               "Bordeaux": ("b", 10),
                               "Brush": ("b", 14),
                               "Diana-Vs": ("d", 5),
                               "Freehand": ("f", 8),
                               "Giddyup": ("g", 1),
                               "Impress": ("i", 1),
                               "Jester Pro": ("j", 1),
                               "Kids": ("k", 1),
                               "Manila": ("m", 0),
                               "Old_Engl": ("o", 2),
                               "Pepita": ("p", 2),
                               "Ribbon Love": ("r", 3),
                               "Swiss": ("s", 12),
                               "Tango": ("t", 1),
                               "Times": ("t", 3),
                               "Trad_Scr": ("t", 4),
                               "Univeri": ("u", 0),
                             }

             if row.FONT in font_harfleri:
                font_harf, adim_sayisi = font_harfleri[row.FONT]

                pyautogui.click(x=1825, y=236)
                pyautogui.press('home')
                pyautogui.press(font_harf)
                for _ in range(adim_sayisi):
                      pyautogui.press('down')
                pyautogui.press('enter') 

                
             pyperclip.copy(row.SIZE)
             pyautogui.click(x=1846, y=143) #Size bölümü koordinatlarý
             pyautogui.click(x=1732, y=200) #Size bölümü koordinatlarý
             pyautogui.click(x=1732, y=200)
             pyautogui.hotkey('ctrl', 'a')
             pyautogui.hotkey('ctrl', 'v')
             pyautogui.press('enter')
             pyautogui.click(x=1615, y=144)
                
             pyautogui.click(x=1872, y=386) 
             pyautogui.click(x=86, y=67) 
            
             isim= f"{row.SIPNO}-{row.YAZI}-{row.FONT}"
             pyperclip.copy(isim)
             time.sleep(0.5)
             pyautogui.click(x=864, y=543)  #Katýt Yeri Koordinatlarý
             pyautogui.click(x=864, y=543)
             pyautogui.hotkey('ctrl', 'a')
             pyautogui.hotkey('ctrl', 'v')
             pyautogui.press('tab')
             pyautogui.press('t')
             pyautogui.press('enter')
             pyautogui.press('left')
             pyautogui.press('enter')
             pyautogui.press('enter')
             
             cursor.execute("UPDATE MONOGRAM_DETAY SET YAPILDI = ? WHERE ID = ?", (True, row.ID))
             conn.commit()
             time.sleep(1)            
    conn.close()

if __name__ == "__main__":
    Start_Program()
    time.sleep(5)  
    sql_veri_cek()