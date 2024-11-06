from spm.__wrapper__ import Runtime


def spm_input(*args, **kwargs):
    """
      Comprehensive graphical and command line input function  
        FORMATs (given in Programmers Help)  
       _______________________________________________________________________  
         
        spm_input handles most forms of interactive user input for SPM.  
        (File selection is handled by spm_select.m)  
         
        There are five types of input: String, Evaluated, Conditions, Buttons  
        and Menus:  These prompt for string input; string input which is  
        evaluated to give a numerical result; selection of one item from a  
        set of buttons; selection of an item from a menu.  
         
        - STRING, EVALUATED & CONDITION input -  
        For STRING, EVALUATED and CONDITION input types, a prompt is  
        displayed adjacent to an editable text entry widget (with a lilac  
        background!). Clicking in the entry widget allows editing, pressing  
        <RETURN> or <ENTER> enters the result. You must enter something,  
        empty answers are not accepted. A default response may be pre-specified  
        in the entry widget, which will then be outlined. Clicking the border  
        accepts the default value.  
         
        Basic editing of the entry widget is supported *without* clicking in  
        the widget, provided no other graphics widget has the focus. (If a  
        widget has the focus, it is shown highlighted with a thin coloured  
        line. Clicking on the window background returns the focus to the  
        window, enabling keyboard accelerators.). This enables you to type  
        responses to a sequence of questions without having to repeatedly  
        click the mouse in the text widgets. Supported are BackSpace and  
        Delete, line kill (^U). Other standard ASCII characters are appended  
        to the text in the entry widget. Press <RETURN> or <ENTER> to submit  
        your response.  
         
        A ContextMenu is provided (in the figure background) giving access to  
        relevant utilities including the facility to load input from a file  
        (see spm_load.m and examples given below): Click the right button on  
        the figure background.  
         
        For EVALUATED input, the string submitted is evaluated in the base  
        MatLab workspace (see MatLab's `eval` command) to give a numerical  
        value. This permits the entry of numerics, matrices, expressions,  
        functions or workspace variables. I.e.:  
          i)  - a number, vector or matrix        e.g. "[1 2 3 4]"  
                                                       "[1:4]"  
                                                       "1:4"  
         ii)  - an expression                     e.g. "pi^2"  
                                                       "exp(-[1:36]/5.321)"  
        iii)  - a function (that will be invoked) e.g. "spm_load('tmp.dat')"  
                (function must be on MATLABPATH)       "input_cov(36,5.321)"  
         iv)  - a variable from the base workspace  
                                                  e.g. "tmp"  
         
        The last three options provide a great deal of power: spm_load will  
        load a matrix from an ASCII data file and return the results. When  
        called without an argument, spm_load will pop up a file selection  
        dialog. Alternatively, this facility can be gained from the  
        ContextMenu. The second example assumes a custom function called  
        input_cov has been written which expects two arguments, for example  
        the following file saved as input_cov.m somewhere on the MATLABPATH  
        (~/matlab, the matlab subdirectory of your home area, and the current  
        directory, are on the MATLABPATH by default):  
         
              function [x] = input_cov(n,decay)  
              % data input routine - mono-exponential covariate  
              % FORMAT [x] = input_cov(n,decay)  
              % n     -  number of time points  
              % decay - decay constant  
              x = exp(-[1:n]/decay);  
         
        Although this example is trivial, specifying large vectors of  
        empirical data (e.g. reaction times for 72 scans) is efficient and  
        reliable using this device. In the last option, a variable called tmp  
        is picked up from the base workspace. To use this method, set the  
        variables in the MatLab base workspace before starting an SPM  
        procedure (but after starting the SPM interface). E.g.  
        >> tmp=exp(-[1:36]/5.321)  
         
        Occasionally a vector of a specific length will be required: This  
        will be indicated in the prompt, which will start with "[#]", where  
        # is the length of vector(s) required. (If a matrix is entered then  
        at least one dimension should equal #.)  
         
        Occasionally a specific type of number will be required. This should  
        be obvious from the context. If you enter a number of the wrong type,  
        you'll be alerted and asked to re-specify. The types are i) Real  
        numbers; ii) Integers; iii) Whole numbers [0,1,2,3,...] & iv) Natural  
        numbers [1,2,3,...]  
         
        CONDITIONS type input is for getting indicator vectors. The features  
        of evaluated input described above are complimented as follows:  
          v)  - a compressed list of digits 0-9   e.g. "12121212"  
         ii)  - a list of indicator characters    e.g. "abababab"  
                a-z mapped to 1-26 in alphabetical order, *except* r ("rest")  
                which is mapped to zero (case insensitive, [A:Z,a:z] only)  
        ...in addition the response is checked to ensure integer condition indices.  
        Occasionally a specific number of conditions will be required: This  
        will be indicated in the prompt, which will end with (#), where # is  
        the number of conditions required.  
         
        CONTRAST type input is for getting contrast weight vectors. Enter  
        contrasts as row-vectors. Contrast weight vectors will be padded with  
        zeros to the correct length, and checked for validity. (Valid  
        contrasts are estimable, which are those whose weights vector is in  
        the row-space of the design matrix.)  
         
        Errors in string evaluation for EVALUATED & CONDITION types are  
        handled gracefully, the user notified, and prompted to re-enter.  
         
        - BUTTON input -  
        For Button input, the prompt is displayed adjacent to a small row of  
        buttons. Press the appropriate button. The default button (if  
        available) has a dark outline. Keyboard accelerators are available  
        (provided no graphics widget has the focus):  <RETURN> or <ENTER>  
        selects the default button (if available). Typing the first character  
        of the button label (case insensitive) "presses" that button. (If  
        these Keys are not unique, then the integer keys 1,2,...  "press" the  
        appropriate button.)  
         
        The CommandLine variant presents a simple menu of buttons and prompts  
        for a selection. Any default response is indicated, and accepted if  
        an empty line is input.  
         
         
        - MENU input -  
        For Menu input, the prompt is displayed in a pull down menu widget.  
        Using the mouse, a selection is made by pulling down the widget and  
        releasing the mouse on the appropriate response. The default response  
        (if set) is marked with an asterisk. Keyboard accelerators are  
        available (provided no graphic widget has the focus) as follows: 'f',  
        'n' or 'd' move forward to next response down; 'b', 'p' or 'u' move  
        backwards to the previous response up the list; the number keys jump  
        to the appropriate response number; <RETURN> or <ENTER> slelects the  
        currently displayed response. If a default is available, then  
        pressing <RETURN> or <ENTER> when the prompt is displayed jumps to  
        the default response.  
         
        The CommandLine variant presents a simple menu and prompts for a selection.  
        Any default response is indicated, and accepted if an empty line is  
        input.  
         
         
        - Combination BUTTON/EDIT input -  
        In this usage, you will be presented with a set of buttons and an  
        editable text widget. Click one of the buttons to choose that option,  
        or type your response in the edit widget. Any default response will  
        be shown in the edit widget. The edit widget behaves in the same way  
        as with the STRING/EVALUATED input, and expects a single number.  
        Keypresses edit the text widget (rather than "press" the buttons)  
        (provided no other graphics widget has the focus). A default response  
        can be selected with the mouse by clicking the thick border of the  
        edit widget.  
         
         
        - Command line -  
        If YPos is 0 or global CMDLINE is true, then the command line is used.  
        Negative YPos overrides CMDLINE, ensuring the GUI is used, at  
        YPos=abs(YPos). Similarly relative YPos beginning with '!'  
        (E.g.YPos='!+1') ensures the GUI is used.  
         
        spm_input uses the SPM 'Interactive' window, which is 'Tag'ged  
        'Interactive'. If there is no such window, then the current figure is  
        used, or an 'Interactive' window created if no windows are open.  
         
       -----------------------------------------------------------------------  
        Programmers help is contained in the main body of spm_input.m  
       -----------------------------------------------------------------------  
        See      : input.m     (MatLab Reference Guide)  
        See also : spm_select.m   (SPM file selector dialog)  
                 : spm_input.m (Input wrapper function - handles batch mode)  
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_input.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_input", *args, **kwargs)
