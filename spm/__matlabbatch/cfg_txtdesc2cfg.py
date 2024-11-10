from spm.__wrapper__ import Runtime


def cfg_txtdesc2cfg(*args, **kwargs):
    """
      Create a cfg_item tree from a short-hand text description  
        cfg = cfg_txtdesc2cfg(fname)  
        This utility reads a text file from fname and creates a configuration  
        object tree according to the following grammar rules.  
          
        Each line in the file has the form  
         
         TAGNAME = RIGHTHANDSIDE  
         
        where TAGNAME is a valid tag name for a cfg_item object. For each line, a  
        cfg_item object with tag TAGNAME will be created. Its class is determined  
        by the format of RIGHTHANDSIDE. RIGHTHANDSIDE can be one of  
          
         (TAGNAME_1 TAGNAME_2 ... TAGNAME_N) - cfg_branch  
         
         {TAGNAME_1 TAGNAME_2 ... TAGNAME_N} - cfg_repeat  
         
         [TAGNAME_1 TAGNAME_2 ... TAGNAME_N] - cfg_mchoice  
         
         |TAGNAME_1 TAGNAME_2 ... TAGNAME_N| - cfg_choice  
         
        with .val (for cfg_branch) or .values (all other cases) fields set to the  
        cfg_item objects referenced by TAGNAME_1 ... TAGNAME_N.  
         
         TAGNAME_1 - same type as TAGNAME_1, but with tag TAGNAME instead of  
                     TAGNAME_1  
         
         'some_matlab_code' - this MATLAB code will be evaluated. Its return  
                              value should be a cfg_* object. The tag of this  
                              object will be set to 'TAGNAME'  
         
        The cfg_item object returned will be the one defined in the first line of  
        the file. The depth of the substitutions is not limited, but all  
        substitutions must finally be resolvable to 'some_matlab_code'.  
         
        A valid description would be  
         
         toplevel = {mychoice mybranch}  
         mychoice = |myrepeat myconst|  
         myrepeat = {mymenu}  
         mybranch = (mymchoice myentry)  
         mymchoice = [myfiles myfiles1]  
         myfiles1 = myfiles  
         myfiles  = 'cfg_files'  
         myconst  = 'cfg_const'  
         myentry  = 'cfg_entry'  
         mymenu   = 'cfg_menu'  
         
        The resulting object tree will need further adjustment, but it can serve  
        as a good starting point for modifying program code. The sequence  
         
         cfg = cfg_txtdesc2cfg('mygrammar.txt');  
         cfgstr = gencode(cfg);  
         cfgchr = sprintf('%s\n',cfgstr{:});  
         clipboard('copy', cfgchr)  
         
        will create a cfg_item tree as defined in 'mygrammar.txt', convert it  
        into MATLAB code lines, print them into a newline-separated string and  
        copy this string into the clipboard. From there, it can be pasted into  
        any application (MATLAB editor, external editor ...) where it can be  
        processed further.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_txtdesc2cfg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_txtdesc2cfg", *args, **kwargs)
