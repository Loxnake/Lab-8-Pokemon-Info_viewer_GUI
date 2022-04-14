from tkinter import*
from tkinter import ttk
from turtle import st
from PokiAPI import retrieveMon

def main():

    root = Tk()#making the window
    root.title('Pokemon Info Viewer')
    root.iconbitmap('Pokeball.ico')
    root.resizable(False,False)

    #making the frames
    frame_input = ttk.Frame(root)
    frame_input.grid(row=0, column=0, columnspan=2)

    frame_info = ttk.LabelFrame(root, text ='Info')
    frame_info.grid(row=1, column=0,padx=(10,5),pady=(0,10),sticky=N)

    frame_stats = ttk.LabelFrame(root, text='Stats')
    frame_stats.grid(row=1, column=1,padx=(5,10),pady=(0,10),sticky=N)

    #populate user input frame
    label_name = ttk.Label(frame_input, text="Name of the Pokemon:")
    label_name.grid(row=0, column=0, padx=10, pady=10)

    entry_name = ttk.Entry(frame_input, width= 25)
    entry_name.grid(row=0,column=1, padx=10, pady=10)

    def button_name_click():
        name = entry_name.get()
        pokeDict = retrieveMon(name)
        if pokeDict:
            label_height_val['text'] = str(pokeDict['height']) + 'dm'
            label_weight_val['text'] = str(pokeDict['weight']) + 'hg'
            types_list = (t['type']['name']for t in pokeDict['types'])#making a tuple of the types
            label_type_val['text'] = ', '.join(types_list)#using a weird lookin join() thing to make a string out of a tuple

            progbar_hp['value'] = pokeDict['stats'][0]['base_stat']
            progbar_atk['value'] = pokeDict['stats'][1]['base_stat']
            progbar_def['value'] = pokeDict['stats'][2]['base_stat']
            progbar_spatk['value'] = pokeDict['stats'][3]['base_stat']
            progbar_spdef['value'] = pokeDict['stats'][4]['base_stat']
            progbar_spd['value'] = pokeDict['stats'][5]['base_stat']
            

    button_name = ttk.Button(frame_input, text="Get Info", command=button_name_click)
    button_name.grid(row=0,column=2, padx=10, pady=10)


    #populate Stats frame
    label_hp = ttk.Label(frame_stats,text="HP:")
    label_hp.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    progbar_hp = ttk.Progressbar(frame_stats, length=200, maximum=255.0)
    progbar_hp.grid(row=0,column=1,padx=5,pady=5)

    label_atk = ttk.Label(frame_stats,text="Attack:")
    label_atk.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    progbar_atk = ttk.Progressbar(frame_stats, length=200, maximum=255.0)
    progbar_atk.grid(row=1,column=1,padx=5,pady=5)

    label_def = ttk.Label(frame_stats,text="Defence:")
    label_def.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    progbar_def = ttk.Progressbar(frame_stats, length=200, maximum=255.0)
    progbar_def.grid(row=2,column=1,padx=5,pady=5)

    label_spatk = ttk.Label(frame_stats,text="Special Attack:")
    label_spatk.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    progbar_spatk = ttk.Progressbar(frame_stats, length=200, maximum=255.0)
    progbar_spatk.grid(row=3,column=1,padx=5,pady=5)

    label_spdef = ttk.Label(frame_stats,text="Special Defence:")
    label_spdef.grid(row=4,column=0,padx=5,pady=5,sticky=E)

    progbar_spdef = ttk.Progressbar(frame_stats, length=200, maximum=255.0)
    progbar_spdef.grid(row=4,column=1,padx=5,pady=5)

    label_spd = ttk.Label(frame_stats,text="Speed:")
    label_spd.grid(row=5,column=0,padx=5,pady=5,sticky=E)

    progbar_spd = ttk.Progressbar(frame_stats, length=200, maximum=255.0)
    progbar_spd.grid(row=5,column=1,padx=5,pady=5)



    #pupolate info frame
    label_height = ttk.Label(frame_info, text="Height:")
    label_height.grid(row=0,column=0,padx=10,pady=10,sticky=E)
    
    label_height_val = ttk.Label(frame_info, text="---")
    label_height_val.grid(row=0,column=1,padx=10,pady=10,sticky=W)

    label_weight = ttk.Label(frame_info, text="Weight:")
    label_weight.grid(row=1,column=0,padx=10,sticky=E)
    
    label_weight_val = ttk.Label(frame_info, text="---")
    label_weight_val.grid(row=1,column=1,padx=10,sticky=W)

    label_type = ttk.Label(frame_info, text="Type:")
    label_type.grid(row=2,column=0,padx=10,pady=10,sticky=E)
    
    label_type_val = ttk.Label(frame_info, text="---")
    label_type_val.grid(row=2,column=1,padx=10,pady=10,sticky=W)


    








    root.mainloop()





main()