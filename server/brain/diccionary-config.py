ACC_go_ACC = ['pone','activa','abri','abrite','abre','encend','enciende','ejecuta','reproduc','prende']
ACC_stop_ACC = ['cerrar','cerrame','cierra','detene','detiene','apaga','cortar','cortame','corta']
ACC_up_ACC = ['aumenta','incrementa','subi','subeme','intensifica']
ACC_down_ACC = ['disminuir','baja','atenua']
ACC_search_ACC = ['busca','dame','quiero','mostra','muestrame','decime','como']
OBJ_music_OBJ = ['musica','cancion','album','disco','spotify']
OBJ_volume_OBJ = ['volumen']
OBJ_light_OBJ = ['luz','iluminacion','luces']
OBJ_inet_OBJ = ['internet','google']
OBJ_time_OBJ = ['hora']
OBJ_video_OBJ = ['youtube','videos']
OBJ_window_OBJ = ['ventana','programa']
OBJ_monitor_OBJ = ['monitor','pantalla']
MOD_up_MOD = ['arriba','superior']
MOD_down_MOD = ['abajo','inferior']
MOD_outside_MOD = ['afuera','exterior'] 
MOD_inside_MOD= ['adentro','interior'] 
EXT_hi_EXT= ['hola']
EXT_goodbye_EXT= ['chau','chao','adios']
OBJ_browser_OBJ = ['firefox','navegador']
ACC_search_ACC = ['busca','dame','quiero','mostra','muestrame','decime','decir','como','que']
OBJ_images_OBJ = ['imagen','foto']



diccionario_principal = {
    'MUSIC':['musica','cancion','album','disco','spotify'],
    'LIGHT':['luz','iluminacion','luces'],
    'INTERNET':['internet','google','navegador'],
    'TIME':['hora','horario'],
    'VIDEO':['youtube','videos'],
    'IMAGES':['imagen','fotos'], 
    'MONITOR':['monitor','pantalla'],
    'VOLUME':['volumen','sonido'],
    'HI':['hola'],
    'BYE':['chau','chao','adios'],
}

diccionarios_secundarios = {
    'MUSIC':{
        ACC_go_ACC,
        ACC_stop_ACC,
        ACC_up_ACC, 
        ACC_down_ACC,
        ACC_search_ACC, 
        OBJ_music_OBJ,
        OBJ_volume_OBJ,
    },
    'LIGHT':{
        ACC_go_ACC, 
        ACC_stop_ACC,
        ACC_up_ACC,
        ACC_down_ACC,
        ACC_search_ACC, 
        OBJ_music_OBJ,
        OBJ_light_OBJ,
        OBJ_inet_OBJ,
        OBJ_time_OBJ, 
        OBJ_video_OBJ,
        OBJ_window_OBJ, 
        OBJ_monitor_OBJ,
        OBJ_volume_OBJ,
        MOD_up_MOD,
        MOD_down_MOD,
        MOD_outside_MOD, 
        MOD_inside_MOD, 
        EXT_hi_EXT,
        EXT_goodbye_EXT,
    },
    'INTERNET':{
        ACC_go_ACC,
        ACC_stop_ACC,
        ACC_up_ACC, 
        ACC_down_ACC,
        ACC_search_ACC, 
        OBJ_inet_OBJ,
        OBJ_browser_OBJ,
    },
    'TIME':{
        ACC_go_ACC, 
        ACC_stop_ACC,
        ACC_search_ACC,
        OBJ_time_OBJ, 
    },
    'VIDEO':{
        ACC_go_ACC, 
        ACC_stop_ACC,
        ACC_up_ACC, 
        ACC_down_ACC,
        ACC_search_ACC, 
        OBJ_music_OBJ,
        OBJ_light_OBJ,
        OBJ_inet_OBJ,
        OBJ_time_OBJ, 
        OBJ_video_OBJ,
        OBJ_window_OBJ, 
        OBJ_monitor_OBJ,
        OBJ_volume_OBJ,
        MOD_up_MOD,
        MOD_down_MOD, 
        MOD_outside_MOD, 
        MOD_inside_MOD, 
        EXT_hi_EXT,
        EXT_goodbye_EXT,
    },
    'IMAGES':{
        ACC_go_ACC, 
        ACC_search_ACC, 
        OBJ_images_OBJ,
    },
    'MONITOR':{
        ACC_go_ACC, 
        ACC_stop_ACC,
        ACC_up_ACC, 
        ACC_down_ACC,
        OBJ_monitor_OBJ,
        MOD_up_MOD,
        MOD_down_MOD, 
    },
    'VOLUME':{
        ACC_go_ACC,
        ACC_stop_ACC,
        ACC_up_ACC,
        ACC_down_ACC,
        ACC_search_ACC, 
        OBJ_volume_OBJ,
        MOD_up_MOD,
        MOD_down_MOD, 
        MOD_outside_MOD, 
        MOD_inside_MOD, 
    },
    'HI':{
        EXT_hi_EXT,
    },
    'BYE':{
        EXT_goodbye_EXT,
    }
}










