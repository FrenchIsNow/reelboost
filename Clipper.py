# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os, math, random
# Import everything needed to edit video clips
from moviepy.editor import VideoFileClip, concatenate_videoclips, ipython_display
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout



#Keywords
theme_nature: str          = "Nature"
theme_lifestyle: str        = "LifeStyle"
log_file: str               = "Edit.log"

#List of clip various category
base_path: str              ="./Videos/FullClip/"
clip_category_nature: list = os.listdir(base_path + theme_nature)

full_clip_cat_list: list    = list(clip_category_nature)
full_clip_category_str: str = f"\t- Nature: {clip_category_nature}\n"

def verification_folder_information(parent_folder:str = None, mode:int = 0o777) -> set :
    """
    Name
    ----
    verification_folder_information

    Description
    -----------
    Verify the information given for folder creation.

    Parameters
    ----------
    parent_folder : str, optional
        Name of the video main topic folder (Example: Nature, Lifestyle etc). The default is None.
    mode : int, optional
        Operation permitted on this folder. The default is 0o777.

    Returns
    -------
    set
        - Parent folder path (string)
        - Mode (int)

    """
    #Correct the parent folder path, if not given.
    if parent_folder is None or parent_folder.strip() == "" or not parent_folder.strip() in os.listdir("./Videos/FullClip/") :
        parent_folder   = os.path.abspath(".")

    #Correct error on folder mode and force it at readable, writable and executable for all.
    if type(mode) is not int or not ("0o" in str(mode)) or mode > 0o777 :
        mode            = 0o777

    return parent_folder, mode



def create_video_folder(folder_name : (str | list[str]), parent_folder:str = "Anything", mode:int = 0o777) -> None :
    """
    Name
    ----
    create_video_folder

    Description
    -----------
    Create one or various folder which will contain various sub-Clip of different subject.

    Parameters
    ----------
    folder_name : (str | list[str])
        One or various name of folder to create.
    parent_folder : str, optional
        Absoluate or relative path to the new folder. The default is Anything.
    mode : int, optional
        Operation permitted on this folder. The default is 0o777.


    Returns
    -------
    None
        DESCRIPTION.

    """


    full_clip_dir           = "./Videos/FullClip/"
    sub_clip_dir            = "./Videos/SubClip/"

    #Correct error on folder mode and force it at readable, writable and executable for all.
    if type(mode) is not int or not ("0o" in str(mode)) or mode > 0o777 :
        mode            = 0o777




    if type(folder_name) is str:
        #Concatenate parent folder and new folder to create new path.
        if parent_folder.strip() == "":
            parent_folder = "Anything"

        #Main topic folder path in full clip folder.
        full_clip_path  = os.path.join(full_clip_dir, parent_folder)

        #Main topic folder path in sub clip folder.
        sub_clip_path   = os.path.join(sub_clip_dir, parent_folder)

        #Correct the parent folder path, if not given or does not exist.
        if not parent_folder.strip() in os.listdir(full_clip_dir) :
            #Create Main topic (parent) directory in full clip folder.
            os.mkdir(full_clip_path, mode)
            print(f"INFO: Path {full_clip_path} with mode {mode} is created.")

            #Create Main topic (parent) directory in full clip folder.
            os.mkdir(sub_clip_path, mode)
            print(f"INFO: Path {sub_clip_path} with mode {mode} is created.")

        #Create the category folder, if it does not exist
        if not folder_name in os.listdir(full_clip_path):

            print(os.listdir(full_clip_path))

            # Create topic folder in full clip folder
            full_final_path     = os.path.join(full_clip_path, folder_name)
            os.mkdir(full_final_path, mode)
            print(f"INFO: Path {full_final_path} with mode {mode} is created.")


            # Create topic folder in sub clip folder
            for n in range(3, 6):
                sub_final_path      = os.path.join(sub_clip_path, folder_name) + f"_{n}s"
                os.mkdir(sub_final_path, mode)
                print(f"INFO: Path {sub_final_path} with mode {mode} is created.")

    #Create a list of
    elif type(folder_name) is list:
        for fd in folder_name :
            create_video_folder(fd, parent_folder, mode)

def check_duration(msg:str, min_duration:int = 3, max_duration:int = 720, possible_value_list: list = None) -> int :
    """
    Name
    ----
    check_user_selection

    Description
    -----------
    Verify the value given by the user for the clip and sub-clip duration.

    Parameters
    ----------
    msg : str
        Print message for user interaction.
    min_duration : int, optional
        Clip min length in seconds. The default is 3.
    max_duration : int, optional
        Clip max length in seconds. The default is 720.
    possible_value_list : list, optional
        List of accpeted values. The default is None.

    Returns
    -------
    int
        DESCRIPTION.

    """
    confirmation: bool      = False
    res: int                = 0
    while(not confirmation):
        var                 = input(msg).strip()

        if not var.isdigit():
            print(f"The given number {var} is not digital number, please try again!")
            continue
        elif not possible_value_list is None and not int(var) in possible_value_list:
            print(f"The given number {var} is not in the accepted value list: {possible_value_list}, please a correct number!")
        elif int(var) > max_duration:
            print(f"The given number {var} is bigger than the clip maximum length: {max_duration}, please give a smaller number!")
        elif int(var) < min_duration:
            print(f"The given number {var} is smaller than the clip  minimum length: {min_duration}, please give a bigger number!")

        else:
            res             = int(var)
            confirmation    = True

    return res


def check_user_selection(full_clip_cat_list: list, full_clip_category_str: str) -> set:
    """
    Name
    ----
    check_user_selection

    Description
    -----------
    Verify user choices of sub-clip theme, time and occurences.

    Parameters
    ----------
    full_clip_cat_list : list
        List of theme.
    full_clip_category_str : str
        Theme slection message.

    Returns
    -------
     set
         total_length (int)
             Total length in seconds of the comoposite clip.
         sub_length (int)
             Length of each subclip in seconds.
         number_of_clip (int)
             Number of subclip contain in the full clip.
        sub_clip_info (dict)
            Key: Sub-clip theme
            Value: Number of occurences.

    """

    # Ask user for each sub-clip duration
    total_length: int           =  check_duration("How long the whole clip must be (in seconds) ? ")
    # Ask user for each sub-clip duration
    sub_length: int             = check_duration("How long each separated clip must be between 3, 4 and 5 seconds ? ", possible_value_list=[3,4,5])

    #Calculate number of clip needed to create the full video
    number_of_clip = int(math.ceil(total_length/sub_length))
    msg                         = f"Total Clip length: {total_length}\n"
    msg                         += f"Sub-clip length: {sub_length}\n"
    msg                         += f"Number of Clips: {number_of_clip}"
    print(msg)

    sub_clip_info               = dict()
    confirmation_cat            = False
    number_of_occurrence_left   = number_of_clip
    #Check category given by user
    while not confirmation_cat :
        msg                         = "Please select a category from this list:\n" + full_clip_category_str
        cat                         = input(msg).capitalize().strip()

        #User input must be a word in the list of possible categories.
        if cat not in full_clip_cat_list : #Input is not in the category list given to the user
            print(f"The given category, {cat}, does not exist!")
            continue

        else : #Input is in the category list.
            #Check number of occurrence for each category.
            confirmation_occurrence_cat = False

            while not confirmation_occurrence_cat:
                msg                 = f"Please select the number of occurrence of the category: {cat}\n"
                msg                 += f"Number of occurrence left: {number_of_occurrence_left}\n"
                num_occ             = input(msg).strip()

                if not num_occ.isdigit() or int(num_occ) > number_of_occurrence_left  or int(num_occ) < 1: #User input is not an integer or not between 1 and the number max of sub-clip.
                    print(f"The given number must an integer between 1 and {number_of_occurrence_left}")
                    continue
                else:
                    num_occ         = int(num_occ)
                    #Check if category is already used for the clip
                    if cat in sub_clip_info:
                        sub_clip_info[cat]  = sub_clip_info.get(cat) + num_occ
                    else :
                        sub_clip_info.setdefault(cat, num_occ)

                    number_of_occurrence_left -= num_occ
                    confirmation_occurrence_cat = True

            if number_of_occurrence_left <= 0 :
                confirmation_cat = True
    return total_length, sub_length, number_of_clip, sub_clip_info

def create_sub_clip() -> None :
    """
    Name
    ----
    create_sub_clip

    Description
    -----------
    Create sub-clip videos of 3, 4 and 5 seconds from longer video.

    Parameters
    ----------
    None.

    Returns
    -------
    None.

    """

    theme_list          = [main_theme + "/" + sub_theme for main_theme in os.listdir(base_path) for sub_theme in os.listdir(base_path + "/" + main_theme)]
    short_theme_dict    = {i: theme.split("/")[-1] for i, theme in enumerate(theme_list)}

    #User select a theme by choosing a number
    msg                 = "Please select a theme inside this list:"
    for key, val in short_theme_dict.items():
        msg             += "\n\t" + str(key) + ". " + val
    #Checking user input
    theme_confirmation  = False
    while not theme_confirmation:
        theme           = input(msg + "\n")
        if theme.isdigit() and int(theme) >= 0 and int(theme) < len(short_theme_dict):
            path                = os.path.join(base_path, theme_list[int(theme)]) + "/"
            theme               = short_theme_dict.get(int(theme))
            theme_confirmation  = True
            print(path)

        else :
            print(f"Incorrect value : {theme}")


    #Fetch list of already decompose videos:
    with open(file=path + log_file, mode="r" , encoding="utf-8") as edit_file:
        edited_vid_list = edit_file.readlines()
    print(edited_vid_list)

    #Retrive each video to edit into clip
    for vid in os.listdir(path):
        #Ignore already cut videos
        print()
        if (vid + "\n") in edited_vid_list or vid == log_file:
            continue


        clip            = VideoFileClip(path + vid)
        vid_name        = os.path.basename(clip.filename)

        #Fix the size of clip from 3 to 5 seconds
        for step in range(3, 6):
            for i, n in enumerate(range(1, math.ceil(clip.duration), step), start=1):
                #Add currently video into the list of edited videos.
                if not (vid_name + "\n") in edited_vid_list:
                    edited_vid_list.append(vid_name + "\n")

                #Creating sub-clip with the correct length, if the length is too short, the sub-clip will not be created.
                if n+step < clip.duration:
                    subclip_name    = str(i) + "_" + vid_name
                    subclip_path    = path.replace("FullClip", "SubClip").replace(theme, theme + "_"+ str(step) + "s")
                    sub_clip        = clip.subclip(n, n+step)
                    sub_clip.write_videofile(filename=subclip_path + subclip_name, fps=90)

    #Rewrite list of edited videos
    with open(file=path + log_file, mode="r+" , encoding="utf-8") as edited_videos_file:
            edited_videos_file.writelines(edited_vid_list)


def create_composite_clip(output_clip_name: str , output_clip_format:str) -> None:

    tLength, sLength, nClip, clip_component      = check_user_selection(full_clip_cat_list, full_clip_category_str)

    # Random subclip selection
        # List of subclip and subclip's theme
    list_subclip        = list()
    list_subclip_theme  = sorted(set(clip_component))


    #Check or create output composite clip folder
    output_path         = "./Videos/Output/"
    for i, theme in enumerate(list_subclip_theme, start=1):
        if i == len(list_subclip_theme):
            output_path += theme
        else :
            output_path += theme + "-"
    output_path         += "-" + str(tLength) + "/"

    #Create directionary, if it does not exist
    if not os.path.exists(output_path) :
        os.mkdir(path= output_path, mode=0o777)


    fade_duration   = 1
    clip_number     = 1
    while clip_component :
        element_chosen  = random.choice(list(clip_component))
        clip_component[element_chosen] -= 1
        if clip_component[element_chosen] < 1 :
            clip_component.pop(element_chosen)

        #Launch random clip selection.
          #Indicate the chosen theme's main category
        main_theme                  = None
        for theme in os.listdir(base_path):
            if element_chosen in os.listdir(base_path + theme):
                main_theme      = theme
                break

        chosen_element_path     = base_path.replace("FullClip", "SubClip") + main_theme + "/" + element_chosen + "_" + str(sLength) + "s/"
        random_subclip          = chosen_element_path + random.choice(os.listdir(chosen_element_path))
        if clip_number == 1:
            clip                = VideoFileClip(filename=random_subclip).fx(fadeout, fade_duration)
        elif clip_number == nClip:
            clip                = VideoFileClip(filename=random_subclip).fx(fadein, fade_duration)
        else :
            start_time          = clip_number * sLength
            end_time            = start_time + sLength
            clip                = VideoFileClip(filename=random_subclip).fx(fadein, fade_duration)
            # clip                = VideoFileClip(filename=random_subclip).fx(fadeout, fade_duration)
        clip_number     += 1
        list_subclip.append(clip)

    final_clip                  = concatenate_videoclips(list_subclip,  method='compose')
    final_clip.write_videofile(filename=output_path + output_clip_name + "." + output_clip_format, fps=60)



if __name__ == "__main__" :

    create_composite_clip("Test", "mp4")



