

TO DO LIST
- Règle à suivre
    - Faire chacune des tâches dans l'ordre énoncé
    - Faire exactement la tâches ni plus ni moins
    - Créer une nouvelle branch depuis la main branch nommée: "feature-numéro de la tâche" (feature-1, feature-2, etc..)
    - Une fois la tâche fini , revenir ici et inscrire "DONE" à côté
    - Push la feature branch
    - Créer une pull request
    - Merge la branch dans main

Pour info les audio

0 - Variable -> DONE
    - Créer des variables global pour les chemins
        AUDIO_PATH
          AUDIO_MOTIVATION_PATH
          AUDIO_SHORT_QUOTES_PATH
        VIDEO_PATH
            VIDEO_FULL_CLIP_PATH
            VIDEO_SUB_CLIP_PATH
            VIDEO_COMPOSITE_CLIP_PATH
        FINAL


1 - Gérer le convertion au format Rééls -> DONE 

    a - Créer une function qui transforme une vidéo au format Rééls ( 1080px x 1920px with a 9:16 aspect ratio )

    b - Modifier la function create_composite_clip avec une variable d'entrée type :
        Type peut être équal à "reels" ou "landscape"
        la valeur par defaut si rien n'est spécifier est : "reels"

    c - Vérifier si l'affiche de la video composite est bonne
        il peut y avoir des problèmes du au format initial de la vidéo ( ex : de bande noir apparaisse )
        la vidéo de sorti doit être sans bande et en plein écran peut importe le type

2 - Transition -> DONE 

    - Modifier la function create_composite_clip pour y ajouter une transition fade entre chaque video:
      Fin du subclib = Fade OUT
      Debut du subclip = Fade IN

4 - Selection automatique des itération par theme

    a - Créer une function qui liste les catégories de theme et sous-theme automatiquement
        - l'objectif est qu'un thème soit proposer si un nouveau dossier theme est ajouter ( subclip )

    b - Modifier la function create_composite_clip pour que le nombre d'itération par theme soit automatiquement générer
      ex: Forest,River = Random Number of clip per theme = 2 forest, 3 river
      ajouter un mode auto pour skip les entrée utilisateur

3 - Identifier une vidéo

    a - Créer une function qui renome tout les fullclip avec un UUID v4 ( id )
        - cette function doit être lancé à chaque fois en premier au cas ou une nouvelle vidéo à été ajouté
        - un fichier log nommée "full_clip_renamed" doit être présent dans fullclip folder at root level (if not exist create one)
          il va référencer toutes les vidéos déja rénomé avec leur ancien nom et le nouveau nom (UUID v4 ( id ))
        - ne pas renomé les vidéo déjà faite
        - si une nouvelle video à le nom d'un ancien nom de video supprimer la video
            ex: j'ai renomé une video anciennement nommée forest_23 et j'ai une nouvelle video nommé forest_23 je vais vérifié les logs pour voir si une video avait ce nom au quel cas je supprime la nouvelle.
        - Vérifier si l'UUID v4 ( id ) est unique via les logs , sinon trouver un nouvelles id

    b - Modifier la function create_composite_clip pour que le nom de la vidéo soit un UUID v4 ( id )
        pas besoin de rentrer un nom

    c - Faire un logs des OUTPUT nommée generated_composite_clip (video composite) à chaque nouvelles vidéo enregistrer :
        - le nom de la videos de sorti
        - les theme utiliser "Forest,River,etc"
        - la durer de la video
        - la liste des nom des subclip utiliser "video1,video2"

    d - Ne plus mettre le nom des theme dans le dossier de sorti d'un composite vu qu'on l'a dans les logs
        Mettre la video de sorti dans le theme parent superieur
        ex : au lieux d'un dossier "Forest-Mountain-River-15" mettre la video dans "Nature"

4 - Get Audio Duration
    - Créer une function qui récupère la durée d'un fichier audio ( WAV & MP3)
      input = audio file
      output = duration in second

5 - Get Video or Audio by name
  a - Create a function that will get a video by its name ( option pass subfolder)
    - if no subfolder is give it should search on VIDEO_PATH
      else seach on subfolder directly

  b - Create a function that will get a audio by its name ( option pass subfolder)
    - if no subfolder is give it should search on VIDEO_PATH
      else seach on subfolder directly

  c - handle Error ( not found folder or file )

6 - Get Audio Language

  a - Create a function that will get audio language by its name
     audio_name_en = en language

7 - Merge Audio and Video

  a - Create a function that will merge an audio and video file
      input :
          audio file name ( not required if audio is provided )
          video file name ( not required if video is provided )
          audio file
          video file
      use previous function to retreive each file
      else proceed with given file

8 - Final Result - Wrapping all together

    - Create a function make_video that will take as input :
        list of audio file name: audio_fr,audio_en
        list of theme : Forest,River
        topics : Motivaltion speech
        output_path : Default Final Folder
        list of corresponding audio text (optionall may be useful for subtitles)

    A terme les info viendrons d'un csv ( next main step )
    Voici Le format des columns du fichier excel pour aider a la construction de la function make_video

    ID, Topic, Theme, text_en , text_fr , text_es , text_pt , text_tr , text_de , text_da , text_it , text_hr, text_jp, text_ko,
    audio_name_en , audio_name_fr , audio_name_es , audio_name_pt , audio_name_tr , audio_name_de , audio_name_da , audio_name_it , audio_name_hr, audio_name_jp, audio_name_ko


    - first it will search for all audio file
    - get duration of all audio and store it
    - get all language from audio
    - if not created yet create language subfolder in output_path folder
    - create the composite video from the theme list
    - keep the name
    - merge the SAME video for every audio
    - store the video in output_path in language subfolder ( video name is index_language)
      if 2 audio it will be 1_fr en fr subfolder and 1_en in en subfolder in output_path folder
    - store in logs ( video name , audio name , topics)

9 - AUTOMATE ALL
  - create a function that will get all info to make all video
  - Generate all video from a csv file thanks to the previous function make_video

BONUS

9 - Add subtitle
  - Modify the merge_audio_video add subtittles of the video from input in make_video function (list of corresponding audio text)

10 - Add Custom Water Mark

11 - Add Custom Logo overlay
















