from spm.__wrapper__ import Runtime


def gencode_substructcode(*args, **kwargs):
    """
      GENCODE_SUBSTRUCTCODE  Create code for a subscript structure  
        Generate MATLAB code (using SUBSTRUCT) to create subscript structure  
        subs. See help on SUBSTRUCT, SUBSASGN and SUBSREF for details how  
        subscript structures are used.  
         
        str = gencode_substructcode(subs, name)  
        Input arguments:  
         subs - a subscript structure  
         name - optional: name of variable  
        Output arguments:  
         str  - a one-line cellstr containing a call to SUBSTRUCT that returns  
                an substruct equivalent to subs.  
        If name is supplied as input argument, the generated code will assign  
        the output of SUBSTRUCT to the variable 'name'.  
        then only the rhs of the expression will be returned.  
        For '()' and '{}' also pseudo subscripts are allowed: if subs.subs{...}  
        is a string, it will be printed literally, even if it is not equal to  
        ':'. This way, one can create code snippets that contain e.g. references  
        to a loop variable by name.  
         
        See also GENCODE, GENCODE_RVALUE, GENCODE_SUBSTRUCT.  
         
        This code has been developed as part of a batch job configuration  
        system for MATLAB. See    
             http://sourceforge.net/projects/matlabbatch  
        for details about the original project.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/gencode_substructcode.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("gencode_substructcode", *args, **kwargs)
