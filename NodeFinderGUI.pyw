ó
o
KWc           @ s°  d  Z  d d l m Z m Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 m
 Z
 m Z e j d d k rÀ d d l Z d d l Z d d l Z d d l Z d d l Z nm e j d d k r!d d l Z d d l m Z d d	 l m Z d d
 l m Z d d l j Z n e d   d Z d Z d a e d d d d d d d d d d g
  Z e d d d g  Z e d d d d d d d d d g	  Z  e d d d g  Z! e d d d d d d d d d d g
  Z" e d d d d d d d d g  Z# e d d d d d g  Z$ d Z% e d d d d d d g  Z& e d d g  Z' d Z( d  Z) d! d" Z* d# d" Z+ e j,   Z- d$ Z. d% Z/ d& Z0 d' e( e f Z1 d( e( e f Z2 i  a3 d)   Z4 d* e5 f d+     YZ6 d, e5 f d-     YZ7 d. e5 f d/     YZ8 d0 e j9 f d1     YZ: d2   Z; d3   Z< d4   Z= d5   Z> d6   Z? d7   Z@ d8   ZA d9   ZB d:   ZC d;   ZD d<   ZE d=   ZF d>   ZG eH d? k r¬eG   n  d S(@   sD   
NodeFinder: Do calibration or add Branch Label or add Clade Label.
iÿÿÿÿ(   t   with_statementt   print_functionN(   t   Popent   PIPEi    t   2t   3(   t   ttk(   t
   messagebox(   t
   filedialogs$   Cannot identify your Python version.s   0.5.0t   Jini   t   ,t   ;t   )t   "t   't   #t   $t   @t   >t   <t   0t   1t   :s   [^(),;]+t   /s   \s   NodeFinder GUIt   1200x700t   ~i2   t   =t   Windowst   Linuxt   Darwins§   
%s, GUI implementation of NodeFinder
    Version  :  %s
    URL (GUI):  https://github.com/zxjsdp/NodeFinderGUI
    URL (C)  :  https://github.com/zxjsdp/NodeFinderC
s~  
Documentation of %s (Ver. %s)

[Basic Usage]

    1. Open Newick tree file
    2. Input calibration configs
    3. Press "Execute All" button to execute

[Config Syntax]

    name_a, name_b, calibration_infomation_1
    name_c, name_d, calibration_infomation_2
    name_a, name_b, clade_label_information
    name, branch_label_information
    ..., ..., ...

[Simple Example]

    Given a Newick tree like this:

        ((a ,((b, c), (d, e))), (f, g));

    Use this calibration config (blanks are OK) (fake data):

        c, b, >0.05<0.07
        a, e, >0.1<0.2
        c, f, >0.3<0.5
        d, e, $1
        a, #1

    We will get output tree like this:

        ((a #1 , ((b, c)>0.05<0.07, (d, e)$1))>0.1<0.2, (f, g))>0.3<0.5;

    Topology (ASCII style):

                +---------- a #1
                |
                | >0.1<0.2
            +---|       +-- b
            |   |   +---| >0.05<0.07
            |   |   |   +-- c
            |   +---|
            |       |   +-- d
            |       +---| $1
        ----|>0.3<0.5   +-- e
            |
            |           +-- f
            +-----------|
                        +-- g
c           C s   t  j d t  j    S(   s3   Return a formatted time string: Hour:Minute:Second.s   %H:%M:%S(   t   timet   strftimet	   localtime(    (    (    s    nodefinder_gui/nodefinder_gui.pyt   time_now   s    t   RightClickMenuc           B s_   e  Z d  Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d	   Z RS(
   s5  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenu(some_entry_widget)
    some_entry_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c          sQ   |   _    j  j d   f d   d d   j  j d   f d   d d d  S(   Ns   <Control-a>c          s
     j    S(   N(   t   _select_all(   t   e(   t   self(    s    nodefinder_gui/nodefinder_gui.pyt   <lambda>¨   s    t   addt   +s   <Control-A>c          s
     j    S(   N(   R#   (   R$   (   R%   (    s    nodefinder_gui/nodefinder_gui.pyR&   ©   s    (   t   parentt   bind(   R%   R)   (    (   R%   s    nodefinder_gui/nodefinder_gui.pyt   __init__¢   s    	"c         C s:   |  j  j d  d k r d  S|  j  j   |  j |  d  S(   Nt   statet   disable(   R)   t   cgett   focus_forcet
   build_menu(   R%   t   event(    (    s    nodefinder_gui/nodefinder_gui.pyt   __call__«   s    c         C sD  t  j |  j d d } |  j j   sV | j d d d d  | j d d d d  n2 | j d d d |  j  | j d d d |  j  |  j   r° | j d d	 d |  j  n | j d d	 d d  |  j j   sî | j d d
 d d  n | j d d
 d |  j	  | j
   | j d d d |  j  | j | j | j  d S(   s   Build right click menut   tearoffi    t   labelt   CutR,   R-   t   Copyt   commandt   Pastet   Deletes
   Select AllN(   t   tkt   MenuR)   t   selection_presentt   add_commandt   _cutt   _copyt   paste_string_statet   _pastet   _cleart   add_separatorR#   t   postt   x_roott   y_root(   R%   R1   t   menu(    (    s    nodefinder_gui/nodefinder_gui.pyR0   ´   s    
c         C s   |  j  j d  d  S(   Ns   <<Cut>>(   R)   t   event_generate(   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR>   Ö   s    c         C s   |  j  j d  d  S(   Ns   <<Copy>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR?   Ù   s    c         C s   |  j  j d  d  S(   Ns	   <<Paste>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRA   Ü   s    c         C s   |  j  j d  d  S(   Ns	   <<Clear>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRB   ß   s    c         C s'   |  j  j d d  |  j  j d  d S(   Ni    t   endt   break(   R)   t   selection_ranget   icursor(   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR#   â   s    c         C s(   y |  j  j d d  } Wn t SXt S(   s,   Returns true if a string is in the clipboardt	   selectiont	   CLIPBOARD(   R)   t   selection_gett   Falset   True(   R%   t	   clipboard(    (    s    nodefinder_gui/nodefinder_gui.pyR@   ë   s
    (   t   __name__t
   __module__t   __doc__R+   R2   R0   R>   R?   RA   RB   R#   R@   (    (    (    s    nodefinder_gui/nodefinder_gui.pyR"      s   					"						t   RightClickMenuForScrolledTextc           B sh   e  Z d  Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d	   Z d
   Z RS(   s>   Simple widget to add basic right click menus to entry widgets.c          sQ   |   _    j  j d   f d   d d   j  j d   f d   d d d  S(   Ns   <Control-a>c          s
     j    S(   N(   R#   (   R$   (   R%   (    s    nodefinder_gui/nodefinder_gui.pyR&     s    R'   R(   s   <Control-A>c          s
     j    S(   N(   R#   (   R$   (   R%   (    s    nodefinder_gui/nodefinder_gui.pyR&     s    (   R)   R*   (   R%   R)   (    (   R%   s    nodefinder_gui/nodefinder_gui.pyR+   û   s    	"c         C s=   |  j  j d  t j k r d  S|  j  j   |  j |  d  S(   NR,   (   R)   R.   R:   t   DISABLEDR/   R0   (   R%   R1   (    (    s    nodefinder_gui/nodefinder_gui.pyR2     s    c         C s÷   t  j |  j d d } | j d d d |  j  | j d d d |  j  |  j   rr | j d d d |  j  n | j d d d d	  | j d d
 d |  j  | j	   | j d d d |  j
  | j d d d |  j  | j | j | j  d S(   s
   build menuR3   i    R4   R5   R7   R6   R8   R,   R-   R9   s
   Select Alls	   Clear AllN(   R:   R;   R)   R=   R>   R?   t   _paste_string_statet   _paste_if_string_in_clipboardt   _deleteRC   R#   t
   _clear_allRD   RE   RF   (   R%   R1   RG   (    (    s    nodefinder_gui/nodefinder_gui.pyR0     s    
c         C s   |  j  j d  d  S(   Ns   <<Cut>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR>   .  s    c         C s   |  j  j d  d  S(   Ns   <<Copy>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR?   1  s    c         C s   |  j  j d  d  S(   Ns	   <<Clear>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRZ   4  s    c         C s   |  j  j d  d  S(   Ns	   <<Paste>>(   R)   RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRY   7  s    c         C s=   |  j  j d d d  |  j  j d d  |  j  j d  d S(   s
   select allt   sels   1.0s   end-1ct   insertRJ   (   R)   t   tag_addt   mark_sett   see(   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR#   :  s    c         C s(   y |  j  j d d  } Wn t SXt S(   s,   Returns true if a string is in the clipboardRM   RN   (   R)   RO   RP   RQ   (   R%   RR   (    (    s    nodefinder_gui/nodefinder_gui.pyRX   A  s
    c         C sA   t  j d d d |  j d d } | r= |  j j d d  n  d S(	   s	   Clear alls	   Clear Alls   Erase all text?R)   t   defaultt   oks   1.0RI   N(   t   tkMessageBoxt   askokcancelR)   t   delete(   R%   t   isok(    (    s    nodefinder_gui/nodefinder_gui.pyR[   M  s
    		(   RS   RT   RU   R+   R2   R0   R>   R?   RZ   RY   R#   RX   R[   (    (    (    s    nodefinder_gui/nodefinder_gui.pyRV   ø   s   					!						t   TextEmitc           B s#   e  Z d  Z d d  Z d   Z RS(   s)   Redirect stdout and stderr to tk widgets.t   stdoutc         C s   | |  _  | |  _ d S(   s=   Initialize widget which stdout and stderr were redirected to.N(   t   widgett   tag(   R%   Ri   Rj   (    (    s    nodefinder_gui/nodefinder_gui.pyR+   Y  s    	c         C sr   |  j  j d d  |  j  j d | |  j f  |  j  j d d d d d |  j  j d d	  |  j  j d  d
 S(   s   Proceed Redirection.R,   t   normalRI   t   stderrt
   foregroundt   redt
   backgroundt   yellowt   disabledN(   Ri   t	   configureR]   Rj   t   tag_configureR`   (   R%   t   out_str(    (    s    nodefinder_gui/nodefinder_gui.pyt   write^  s    (   RS   RT   RU   R+   Ru   (    (    (    s    nodefinder_gui/nodefinder_gui.pyRg   V  s   t   Appc           B s  e  Z d  Z d d  Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d   Z d	   Z d
   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z  RS(   sj   The main class for GUI application.

    [Example]
        >>> app = App()
        >>> app.mainloop()
    c         C s¢   t  j j |  |  |  j j t  |  j j t  d |  _ g  |  _	 d |  _
 |  j   |  j   |  j   |  j   |  j   |  j   |  j   |  j   d  S(   Nt    i    (   R:   t   FrameR+   t   mastert   titlet	   GUI_TITLEt   geometryt   INIT_WINDOW_SIZEt
   final_treet   file_path_history_listt   combo_line_countt	   set_stylet   create_widgetst   configure_gridt   row_and_column_configuret   create_right_menut	   bind_funct   display_infot   create_menu_bar(   R%   Ry   (    (    s    nodefinder_gui/nodefinder_gui.pyR+   p  s    			






c         C s±   t  j   } | j d d d | j d d d | j d d d f | j d	 d d
 | j d d d | j d  | j d d d d d | j d d d d d d S(   s   Set custom style for widget.t   TButtont   paddingi   s   execute.TButtonRm   Rn   s   newline.TButtoni   s   clear.TButtons   #2AA198t	   TComboboxs   config.TComboboxs   title.TLabeli
   t   fontt	   helveticai   t   bolds   config.TLabeli   t   ariali	   N(   R   i   R   (   R   i	   (   R   t   StyleRr   (   R%   t   s(    (    s    nodefinder_gui/nodefinder_gui.pyR     s*    
c         C sJ  t  j |  j d d |  _ t  j |  j d d |  _ t  j |  j d d |  _ t  j |  j d d |  _ t  j |  j d d d d |  _ t  j	 |  j d d |  _
 t  j	 |  j d d d d	 |  _ t j   |  _ t  j |  j d
 |  j |  _ t  j	 |  j d d |  _ t j |  j  |  _ t  j |  j d d d d |  _ t  j	 |  j d d d d |  _ t  j	 |  j d d d d	 |  _ t  j	 |  j d d |  _ t  j	 |  j d d |  _ t  j |  j d d d d |  _ t  j |  j d d d d |  _ t  j |  j d d d d |  _ t  j	 |  j d d d d |  _ t  j |  j d d |  _ t  j |  j d d |  _ t  j |  j d d |  _  t j |  j  |  _! t  j |  j d d d d |  _" t  j	 |  j d d |  _# t  j	 |  j d d |  _$ t  j	 |  j d d |  _% t  j	 |  j d d d d	 |  _& |  j& j' d d d d d  d!  t j |  j d" d# |  _( t  j |  j d d$ d d |  _) t  j |  j d d% d d |  _* t  j |  j d d |  _+ |  j+ j, t-  t  j	 |  j d d& |  _. t  j	 |  j d d d d	 |  _/ t j |  j d' d( d" d) d* d+ |  _0 d, S(-   s¸   Create widgets in the main window.

        There are four main panes:
            1. tree_pane
            2. config_pane
            3. out_tree_pane
            4. log_pane
        R   i   t   texts   Origin Treet   styles   title.TLabels   Open Tree File...t   Clears   clear.TButtont   textvariables   Load Historyt   Configurations   Execute Alls   execute.TButtons   Read Config File...s   Save Config to File...s   Name As   config.TLabels   Name Bt   Infos   Add News   newline.TButtons   config.TComboboxs   Tree Outputs   View As ASCIIs
   Quick Saves   Save New Tree As...t   rowi    t   columni   t   stickyt   wet   bgs   #FAFAFAs   Results and Logs   Display widths   Save Log As...t   fgs   #FDF6E3s   #002B36R,   Rq   N(1   R   Rx   Ry   t	   tree_panet   config_panet   out_tree_panet   log_panet   Labelt   choose_tree_labelt   Buttont   open_tree_file_buttont   clear_tree_inputR:   t	   StringVart	   tree_namet   Comboboxt   choose_tree_boxt   load_history_buttont   stt   ScrolledTextt   tree_paste_areat   config_labelt   execute_buttont   clear_config_area_buttont   read_config_file_buttont   save_config_to_file_buttont   name_a_labelt   name_b_labelt
   info_labelt   add_newline_buttont   name_a_comboboxt   name_b_comboboxt   info_comboboxt   config_lines_areat   out_tree_labelt   view_as_ascii_buttont   save_current_dir_buttont   save_as_buttont   clear_out_tree_buttont   gridt   out_tree_areat	   log_labelt   cali_display_width_lablet   cali_display_width_comboboxt   sett   INSERT_POSITION_HALF_SIZEt   save_log_buttont   clear_log_buttont   log_area(   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR   ¦  sÂ    																	c      	   C sM  |  j  j   |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d	 d d  |  j	 j d d d d d
 d	 d d  |  j
 j d d d d	 d d  |  j j d d	 d d d
 d d d  |  j j d d d d d d  |  j j d d d d	 d d  |  j j d d d d d d  |  j j d d d d	 d d  |  j j d d d d d d  |  j j d d	 d d d d  |  j j d d	 d d	 d d  |  j j d d	 d d d d  |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d	 d d  |  j j d d d d d d  |  j j d d d d d
 d d d  |  j j d d d d d d  |  j j d d d d d d  |  j j d d d d	 d d  |  j j d d d d d d  |  j j d d d d d
 d d d  |  j j d d d d d d  |  j j d d d d d d  |  j  j d d d d	 d d  |  j! j d d d d d d  |  j" j d d d d	 d d  |  j# j d d	 d d d
 d d d  d  S(   NR   i    R   R   t   wensi   t   wR   i   t
   columnspanR$   i   t   wsi   i   ($   Ry   RÁ   R   R   R    R¡   R£   R¥   R¦   Rª   R«   R®   R¯   R°   R±   R²   R³   R´   Rµ   R¶   R·   R¸   R¹   Rº   R»   R¼   R½   R¾   R¿   RÂ   RÃ   RÈ   RÉ   RÄ   RÅ   RÊ   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR     sL    %c         C sÆ  |  j  j d d d d d |  j  j d d d d d |  j  j d d d d d |  j  j d d d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d d  S(	   Ni    t   weighti   t   uniformt   fredi   i   i   (   Ry   t   rowconfiguret   columnconfigureR   R   R    R¡   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR   Ä  s>    c   	      C sæ   d   } t  |  j  } | |  j |  t |  j  } | |  j |  t  |  j  } | |  j |  t  |  j  } | |  j |  t  |  j  } | |  j |  t |  j  } | |  j |  t |  j  } | |  j |  d  S(   Nc         S s6   t  t f k r" |  j d |  n |  j d |  d  S(   Ns
   <Button-2>s
   <Button-3>(   t   CURRENT_PLATFORMt   MAC_PLATFORMR*   (   Ri   t   right_menu_obj(    (    s    nodefinder_gui/nodefinder_gui.pyt"   _bind_right_menu_for_all_platformsü  s    (	   R"   Rª   RV   R®   R¸   R¹   Rº   R»   RÂ   (	   R%   R×   t   right_menu_tree_chooset   right_menu_inputt   right_menu_name_at   right_menu_name_bt   right_menu_info_comboboxt   right_menu_configt   right_menu_out(    (    s    nodefinder_gui/nodefinder_gui.pyR   û  s.    								c          sö     j    j d <  f d     j d <  j   j d <  f d     j d <  j   j d <  j   j	 d <  j
   j d <  j   j d <  j   j d <  j   j d <  j   j d <  f d     j d <  j   j d <  j   j d <d  S(   NR7   c            s     j  j d d  S(   Ns   1.0RI   (   R®   Re   (    (   R%   (    s    nodefinder_gui/nodefinder_gui.pyR&   &  s    c            s     j  j d d  S(   Ns   1.0RI   (   R»   Re   (    (   R%   (    s    nodefinder_gui/nodefinder_gui.pyR&   *  s    c            s     j  j d d  S(   Ns   1.0RI   (   RÂ   Re   (    (   R%   (    s    nodefinder_gui/nodefinder_gui.pyR&   7  s    (   t   _ask_open_fileR¥   R¦   t   _load_history_fileR«   R±   t   _read_config_from_fileR²   t   _save_config_to_fileR³   t   _set_value_to_textareaR·   t
   _main_workR°   t   _view_as_ascii_commandR½   t   _save_new_tree_to_current_dirR¾   t   _ask_save_out_as_fileR¿   RÀ   t   _ask_save_log_as_fileRÈ   t
   _clear_logRÉ   (   R%   (    (   R%   s    nodefinder_gui/nodefinder_gui.pyR   "  s    c         C s=  t  j |  j  } t  j | d d } | j d d d |  j  | j   | j d d d |  j  | j d d d |  j  | j   | j d d d |  j  | j	 d d	 d
 |  t  j | d d } | j d d d |  j
  | j d d d |  j  | j	 d d d
 |  t  j | d d } | j d d d |  j  | j d d d |  j  |  j   r| j d d d |  j  n | j d d d d    | j d d d |  j  | j	 d d d
 |  t  j | d d } | j d d d |  j  | j d d d |  j  | j	 d d d
 |  |  j j d
 |  d S(   s!   Create Menu Bar for NodeFinderGUIR3   i    R4   s   Open input tree file...R7   s   Save output tree to file...s   Save log to file...t   Exitt   FileRG   s   Open config file...s   Save config to file...t   ConfigsR5   R6   R8   c           S s
   t  d  S(   Ns   No string in clipboard!(   t   print(    (    (    s    nodefinder_gui/nodefinder_gui.pyR&   c  s    R9   t   Editt   Documentationt   Aboutt   HelpN(   R:   R;   Ry   R=   Rß   RC   Rç   Rè   t   quitt   add_cascadeRá   Râ   R>   R?   RX   RA   RZ   t   display_documentationt   display_aboutt   config(   R%   t   menu_bart	   file_menut   configs_menut	   edit_menut	   help_menu(    (    s    nodefinder_gui/nodefinder_gui.pyR   =  sD    






	

c         C s"   t  t  t  t  t  t  d S(   s0   Display documentation for menu bar about button.N(   Rí   t   LONG_BARt   DOCUMENTATION(   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRô   p  s    

c         C s"   t  t  t  t  t  t  d S(   s4   Display about information for menu bar about button.N(   Rí   Rü   t   ABOUT(   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRõ     s    

c         C s|   t  |  j d  t _ t  |  j d  t _ t t  t d t t f  t t	 j
 d t	 j     t t  t d  d  S(   NRh   Rl   s     %s (Ver %s)s     %d %b %Y,  %a %H:%M:%SsH   
If you need help, please check the menu bar:

   Help -> Documentation
(   Rg   RÊ   t   sysRh   Rl   Rí   Rü   R{   t   __version__R   R   R    (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR     s    

c         C s   |  j  j   j d  d  S(   Ns   <<Copy>>(   Ry   t	   focus_getRH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR?     s    c         C s   |  j  j   j d  d  S(   Ns   <<Cut>>(   Ry   R  RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyR>     s    c         C s   |  j  j   j d  d  S(   Ns	   <<Paste>>(   Ry   R  RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRA     s    c         C s   |  j  j   j d  d  S(   Ns	   <<Clear>>(   Ry   R  RH   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRZ   ¢  s    c         C s(   y |  j  j d d  } Wn t SXt S(   s,   Returns true if a string is in the clipboardRM   RN   (   Ry   RO   RP   RQ   (   R%   RR   (    (    s    nodefinder_gui/nodefinder_gui.pyRX   ¥  s
    c         C sß   i  } t  j d d |  } y | j   } |  j j d d  |  j j d |  | j } t j j	 |  } t
 d t   | f  |  j j d |  |  j |  j d <|  j j d  Wn" t k
 rÚ t
 d	 t    n Xd
 S(   s   Dialog to open file.t   modet   rs   1.0RI   s    [ INFO | %s ] Open tree file: %si    t   valuesR   s   [ INFO | %s ] No file choosedN(   t   tkFileDialogt   askopenfilet   readR®   Re   R]   t   namet   ost   patht   basenameRí   R!   R   Rª   t   currentt   AttributeError(   R%   t   file_optt   ct   orig_tree_strt   abs_patht	   base_name(    (    s    nodefinder_gui/nodefinder_gui.pyRß   ±  s    	c         C sº   |  j  j   } | s/ t j j d t    n t j j |  s[ t j j d t    n[ t	 | d   } | j
   } Wd QX|  j j d d  |  j j d |  t d t    d S(   s   Load file from history.s)   [ ERROR | %s ] History file bar is blank
s   [ ERROR | %s ] No such file
R  Ns   1.0RI   s   [ INFO | %s ] Load file(   Rª   t   getRÿ   Rl   Ru   R!   R	  R
  t   isfilet   openR  R®   Re   R]   Rí   (   R%   t	   file_patht   ft   content(    (    s    nodefinder_gui/nodefinder_gui.pyRà   Ä  s    c         C s   i  } t  j d d |  } | d k r+ d S| j   } |  j j d d  |  j j d |  | j } t j	 j
 |  } t d t   | f  d S(   s!   Read calibration config from fileR  R  Ns   1.0RI   s'   [ INFO | %s ] Read from config file: %s(   R  R  t   NoneR  R»   Re   R]   R  R	  R
  R  Rí   R!   (   R%   R  R  t   config_contentR  R  (    (    s    nodefinder_gui/nodefinder_gui.pyRá   Ó  s    	c         C s^   t  j d d d d  } | d k r( d St |  j j d d   } | j |  | j   d S(   s/   Save current calibration config content to fileR  RÌ   t   defaultextensions   .txtNs   1.0s   end-1c(   R  t   asksaveasfileR  t   strR»   R  Ru   t   close(   R%   R  t   text_to_save(    (    s    nodefinder_gui/nodefinder_gui.pyRâ   ã  s    c         C sø   |  j  j   |  j j   |  j j   } } } t d   | | | g  } t |  d k  sc | r· t j j d t	    t j j d  t j j d  t j j d  t
 d  n= d j |  } |  j j d	 | d
  t
 d t	   | f  d S(   s   Value to textarea.c         S s
   |  d k S(   NRw   (    (   t   x(    (    s    nodefinder_gui/nodefinder_gui.pyR&   ñ  s    i   s   [ ERROR | %s ]
[Usage]
s,       Calibration:  name_a, name_b, cali_info
s'       Branch Label: name_a, branch_label
s.       Clade Label:  name_a, name_b, clade_label
Rw   s   , RI   s   
s,   [ INFO - %s ]  Added one configure line (%s)N(   R¸   R  R¹   Rº   t   filtert   lenRÿ   Rl   Ru   R!   Rí   t   joinR»   R]   (   R%   t   name_at   name_bt   infot   config_listt   one_line(    (    s    nodefinder_gui/nodefinder_gui.pyRã   í  s     #			c         C s  |  j  j d d  } | sE t j j d t    t j d d  n  y t d d   } | j |  Wd QXt	 d	 d
 d g d t
 d t
 } t | j   d  | j   d rÏ t j j | j   d  n  Wn- t k
 rÿ } t j d d d d |  n Xd S(   s#   View tree using ascii tree program.s   1.0s   end-1cs1   [ ERROR | %s] No content in out tree area to viewt
   ValueErrors'   No content in Tree Output area to view.s   tmp_file_for_ascii_view.nwkRÌ   Nt   pythons   tree_ascii_view.pywRh   Rl   i    i   Rz   s
   File Errort   messages'   Cannot write temporary file to disk.
%s(   RÂ   R  Rÿ   Rl   Ru   R!   Rc   t	   showerrorR  R   R   Rí   t   communicatet   IOError(   R%   t   new_tree_strR  t   pR$   (    (    s    nodefinder_gui/nodefinder_gui.pyRå     s.    
		!	c         C s[   |  j  j d d  } d } t | d  + } | j |  t d t   | f  Wd QXd S(   s)   Quick save Newick tree to current folder.s   1.0s   end-1cs   New_tree.nwkRÌ   s   [ INFO | %s ] Quick save: (%s)N(   RÂ   R  R  Ru   Rí   R!   (   R%   t   new_tree_contentt   new_tree_nameR  (    (    s    nodefinder_gui/nodefinder_gui.pyRæ     s    c         C s^   t  j d d d d  } | d k r( d St |  j j d d   } | j |  | j   d S(   s   Dialog to save as file.R  RÌ   R  s   .txtNs   1.0s   end-1c(   R  R  R  R  RÂ   R  Ru   R  (   R%   R  R  (    (    s    nodefinder_gui/nodefinder_gui.pyRç   (  s    c         C s^   t  j d d d d  } | d k r( d St |  j j d d   } | j |  | j   d S(   s   Dialog to save as file.R  RÌ   R  s   .txtNs   1.0s   end-1c(   R  R  R  R  RÊ   R  Ru   R  (   R%   R  R  (    (    s    nodefinder_gui/nodefinder_gui.pyRè   3  s    c         C s=   |  j  j d d  |  j  j d d  |  j  j d d  d S(   s&   Clear all contents in log widget area.R,   Rk   s   1.0RI   Rq   N(   RÊ   Rr   Re   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyRé   =  s    c         C s4   t  t |  j j     } | t k r0 | a n  d  S(   N(   t   intt   floatRÅ   R  RÇ   (   R%   t   insert_position_half_size_now(    (    s    nodefinder_gui/nodefinder_gui.pyt   _apply_values_from_widgetsC  s    c         C s¤   |  j    t |  j j d d   } t |  j j d d   } | sY t j j d  nG t	 | |  |  _
 |  j
 r  |  j j d d  |  j j d |  j
  n  d S(   s   Do main job.s   1.0s   end-1cs/   No valid config lines or error in config lines!RI   N(   R6  t   get_tree_strR®   R  t   get_cali_listR»   Rÿ   Rl   Ru   t   multi_calibrationR~   RÂ   Re   R]   (   R%   t   tree_strt   calibration_list(    (    s    nodefinder_gui/nodefinder_gui.pyRä   J  s    
	c         C s   t  d  d S(   s&   Simple hello function for testing use.s   Hello NodeFinderGUI!N(   Rí   (   R%   (    (    s    nodefinder_gui/nodefinder_gui.pyt   helloY  s    N(!   RS   RT   RU   R  R+   R   R   R   R   R   R   R   Rô   Rõ   R   R?   R>   RA   RZ   RX   Rß   Rà   Rá   Râ   Rã   Rå   Ræ   Rç   Rè   Ré   R6  Rä   R<  (    (    (    s    nodefinder_gui/nodefinder_gui.pyRv   h  s<   	"	á	=	7	'		3												
			
		
			c         C s&   g  |  D] } | j    j  d  ^ q S(   sT  Strip each element in list and return a new list.
    [Params]
        orig_list: Elements in original list is not clean, may have blanks or
                   newlines.
    [Return]
        clean_list: Elements in clean list is striped and clean.

    [Example]
        >>> clean_elements(['a ', '	b	', 'c; '])
        ['a', 'b', 'c']
    R   (   t   strip(   t	   orig_listt   _(    (    s    nodefinder_gui/nodefinder_gui.pyt   clean_elements^  s    c         C s(   |  j  d d  j  d d  j  d d  S(   s   Remove all blanks and return a very clean tree string.
    >>> get_clean_tree_str('((a ,((b, c), (d, e))), (f, g));')
    '((a,((b,c),(d,e))),(f,g));'
    t    Rw   s   
s   	(   t   replace(   R:  (    (    s    nodefinder_gui/nodefinder_gui.pyt   get_clean_tree_strm  s    c         C s4   |  j  |  } x |  | t k r/ | d 7} q W| S(   s#  Get the right index of givin name.
    #                                      111111111122222222
    #                            0123456789012345678901234567
    #                                           |
    >>> get_right_index_of_name('((a,((b,c),(ddd,e))),(f,g));', 'ddd')
    15
    i   (   t   findt   NONE_TREE_NAME_SYMBOL_SET(   t   clean_tree_strt   one_namet   left_index_of_name(    (    s    nodefinder_gui/nodefinder_gui.pyt   get_right_index_of_nameu  s
    
	c         C s   g  } |  j  |  } g  } t |   } xq | | k  r |  | d k rV | j d  n7 |  | d k r | s | j | d  q | j   n  | d 7} q* W| S(   s   Get insertion list
    t   (R   i   (   RD  R"  t   appendt   pop(   RF  R  t   insertion_listt   current_indext   stackt   str_len(    (    s    nodefinder_gui/nodefinder_gui.pyt   get_insertion_list  s    c         C s  t  |  |  } t  |  |  } | d d d  | d d d  } } t |  t |  k  rc | n | } | | k r{ | n | } x_ t |  D]Q \ } } | t |  d k r¹ | }	 n  | | | | k r | | d }	 Pq q Wt |   }
 t d |	  |	 t k  o|
 |	 k n rDt d d t |	 |  |	 t  f  n¨ |	 t k o_|
 |	 k n rt d |  |	 t |	 |
 |	 ! nd |	 t k  rÏ|
 |	 t k  rÏt d d t |	 |  |	 |
 |	  f  n t d |  |	 t |	 t ! t d d t d	  t d
 d t d	  |	 S(   s,   Get index of the most recent common ancestorNiÿÿÿÿi   s   [Common]:   %s
s   [Insert]:   %s%sRA  s   [Insert]:   %ss   [Insert]:   %s  ->||<-i   s   [Insert]:   %sInsert Here(   RQ  R"  t	   enumerateRí   RÇ   (   RF  R$  R%  t   insertion_list_at   insertion_list_bt   shorter_listt   longer_listt   it   each_in_shorter_listt
   cali_pointt   tree_len(    (    s    nodefinder_gui/nodefinder_gui.pyt   get_index_of_tmrca  sJ    		  
c         C sA  t  |   } t | | |  } d | | | f } | t k rJ | t | <n" t d  t d t | | f  | | t k r¢ | |  | | } } | | | }	 n | | t k r)t j d  }
 | |  | | } } |
 j |  d } t d | d  t d | d	  | j	 |  } | | | }	 n t
 d
 | |   |	 S(   s9   Do single calibration. If calibration exists, replace it.s
   %s, %s, %ss5   
[Warning]   Duplicate calibration:           [ !!! ]s   [Exists]:   %s
[ Now  ]:   %s
s   ^[^,);]+i    s   [Calibration Exists]:          s	     [- Old]s   [Calibration Replaced By]:     s	     [+ New]s	   Unknown: (   RC  R[  t   global_insertion_list_cacheRí   t   NO_CALI_EXISTS_SYMBOL_SETt   WITH_CALI_EXISTS_SYMBOL_SETt   ret   compilet   findallt   lstripR)  (   R:  R$  R%  t	   cali_infoRF  RY  t   current_infot	   left_partt
   right_partt   clean_str_with_calit   re_find_left_calit	   left_calit   final_right_part(    (    s    nodefinder_gui/nodefinder_gui.pyt   single_calibrationÌ  s0    
c         C s1  t  |   } t | |  } t |  } t d |  | t k  oP | | k n r| t d d t | | | t  f  n¨ | t k o | | k n rÀ t d | | t | | | ! nd | t k  r| | t k  rt d d t | | | | |  f  n t d | | t | t ! t d d t d  t d d t d  | | t k r| |  | | } } | d | | } n£ | | t k rt j d	  }	 | |  | | } } |	 j	 |  d
 }
 t d |
 d  t d | d  | j
 |
  } | d | | } n t d | |   | S(   s£   Add single label right after one name.
    >>> add_single_branch_label('((a ,((b, c), (d, e))), (f, g));', c, '#1')
    '((a ,((b, c #1 ), (d, e))), (f, g));'
    s   [Common]:   %s
s   [Insert]:   %s%sRA  s   [Insert]:   %ss   [Insert]:   %s  ->||<-i   s   [Insert]:   %sInsert Heres    %s s   ^[^,);]+i    s   [Label Exists]:          s	     [- Old]s   [Label Replaced By]:     s	     [+ New]s   [Error] [Unknown Symbol]: (   RC  RI  R"  Rí   RÇ   t   NO_LABEL_EXISTS_SYMBOL_SETt   WITH_LABEL_EXISTS_SYMBOL_SETR_  R`  Ra  Rb  R)  (   R:  R$  t   branch_labelRF  t   insert_pointRZ  Re  Rf  Rg  Rh  Ri  Rj  (    (    s    nodefinder_gui/nodefinder_gui.pyt   add_single_branch_labelý  sV      

c   
      C sF  i  a  t |   } t d  t d t    t d  t d  x; t |  D]- \ } } t d | d d j |  f  qN Wt |  |  r.xt |  D]y\ } } t |  d k rg| \ } } } t d	  t t  t d
 | d d j |  f  t t  t d |  t d |  t d |  | d t	 k rOt d |  n  t
 |  | | |  }  q t |  d k r | \ } } t d	  t t  t d
 | d d j |  f  t t  t d |  t d |  | d t k rÿt d |  n  t |  | |  }  q q W|  j d d  }	 |	 St j j d  d Sd S(   s1   Do calibration for multiple calibration requests.s6   

====================================================s                   [ New Job: %s]s4   ====================================================s   
[Valid Calibrations]
s	   %4d |  %si   s   , i   s   
s	   [%d]:  %ss   [Name A]:  s   [Name B]:  s   [ Info ]:  i    s2   
[Warning]: Is this valid symbel?  %s     [ !!! ]
i   s   [ Name ]:  R
   s   Please check config lines!
N(   R\  t   get_species_names_from_tree_strRí   R!   RR  R#  t   check_all_names_in_newick_treeR"  t   THIN_BARt%   WARNING_CALI_OR_LABEL_INFO_SYMBOL_SETRk  t   WARNING_BRANCH_LABEL_SYMBOL_SETRp  RB  Rÿ   Rl   Ru   R  (
   R:  t   cali_tuple_listt   species_names_from_tree_strRW  t   each_cali_tupleR$  R%  t   cali_or_clade_infoRn  R~   (    (    s    nodefinder_gui/nodefinder_gui.pyR9  H  sR    


%

!
	

!
c         C sÙ   g  } g  |  j  d  D] } | j   r | j   ^ q } x t |  D] \ } } | j   } | d d d h k r{ qG n  t | j  d   } t |  d
 k rÄ t j j d | d	 | f  g  S| j |  qG W| S(   s   Get calibration list.s   
i    R   s   //R
   i   i   s#   Invalid config line (Line: %d): %s
i   (   i   i   (	   t   splitR=  RR  R@  R"  Rÿ   Rl   Ru   RK  (   t   raw_cali_contentt   tmp_cali_listR?  t   linesRW  t   linet   elements(    (    s    nodefinder_gui/nodefinder_gui.pyR8  {  s    4c         C s   d } t  } |  j d  } xj | D]b } | j   } | j d  rL t } n  | sX q" n  | j d  sv | j d  rz Pq" | | 7} q" W| S(   s0   Read tree content, parse, and return tree stringRw   s   
RJ  s   //R   (   RP   Rz  R=  t
   startswithRQ   (   t   raw_tree_contentt   tmp_tree_strt   tree_start_flagR}  R~  (    (    s    nodefinder_gui/nodefinder_gui.pyR7    s    	c         C s<  t  |   }  |  s g  St j t  } | j |   } g  } xÅ t |  D]· \ } } | j   } | sk qG n  | d t k r qG n  d | k rª | j | j	 d  d  n  d | k rÓ | j | j	 d  d  qG t
 | j	    d k rñ qG qG | j |  qG Wx3 t D]+ } g  | D] } | | k r| ^ q} q	W| S(   s<   Parse Newick tree string and return a list of species names.i    R   R   i   (   RC  R_  R`  t   RE_FIND_ALL_SPECIESRa  RR  R=  t"   NON_SPECIES_NAME_STARTING_CHAR_SETRK  Rz  R"  (   R:  t   re_all_namest	   all_namest   species_namesRW  R  t	   each_charR?  (    (    s    nodefinder_gui/nodefinder_gui.pyRq    s,    )c   	      C s  t  |   } xð t |  D]â \ } } t |  d k r¨ g  | d  D] } | j   ^ qB \ } } x | | f D]4 } | | k rm t j j d | | d f  t Sqm Wq t |  d k r | d j   } | | k rû t j j d | | d f  t Sq q Wt S(   s=   Check whether all names from config lines are in Newick tree.i   i   s-   Name not found in Newick tree: %s (Line: %s)
i   i    (	   Rq  RR  R"  R=  Rÿ   Rl   Ru   RP   RQ   (	   R:  Rv  t   all_names_from_tree_strt   indext
   each_tupleR?  R$  R%  R  (    (    s    nodefinder_gui/nodefinder_gui.pyRr  »  s$    )		c          C s   t    }  |  j   d S(   s   Main GUI Application.N(   Rv   t   mainloop(   t   app(    (    s    nodefinder_gui/nodefinder_gui.pyt   mainÑ  s    	t   __main__(I   RU   t
   __future__R    R   R	  R_  Rÿ   R   t   platformt
   subprocessR   R   t   versiont   TkinterR:   R   Rc   R  R­   R¬   t   tkinterR   R   t   tkinter.scrolledtextt   scrolledtextt   ImportErrorR   t
   __author__RÇ   RÆ   RE  R]  R^  Rl  Rm  Rt  Ru  R  R  t    NON_SPECIES_NAME_MIDDLE_CHAR_SETR{   R}   Rs  Rü   t   systemRÔ   t   WINDOWS_PLATFORMt   LINUX_PLATFORMRÕ   Rþ   Rý   R\  R!   t   objectR"   RV   Rg   Rx   Rv   R@  RC  RI  RQ  R[  Rk  Rp  R9  R8  R7  Rq  Rr  R  RS   (    (    (    s    nodefinder_gui/nodefinder_gui.pyt   <module>   s   '$'!

5	c^ÿ ÿ ø					4	1	K	3					