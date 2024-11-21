from spm.__wrapper__ import Runtime


def gencode_substruct(*args, **kwargs):
    """
      GENCODE_SUBSTRUCT  String representation of subscript structure.  
        Generate MATLAB code equivalent to subscript structure subs. See help  
        on SUBSTRUCT, SUBSASGN and SUBSREF for details how subscript structures  
        are used.  
         
        str = gencode_substruct(subs, name)  
        Input arguments:  
         subs - a subscript structure  
         name - optional: name of variable to be dereferenced  
        Output arguments:  
         str  - a one-line cellstr containing a string representation of the  
                subscript structure  
        If name is given, it is prepended to the string.  
        For '()' and '{}' also pseudo subscripts are allowed: if subs.subs{...}  
        is a string, it will be printed literally, even if it is not equal to  
        ':'. This way, it is possible create code snippets that contain  
        e.g. references to a loop variable by name.  
         
        See also GENCODE, GENCODE_RVALUE, GENCODE_SUBSTRUCTCODE.  
         
        This code has been developed as part of a batch job configuration  
        system for MATLAB. See    
             http://sourceforge.net/projects/matlabbatch  
        for details about the original project.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/gencode_substruct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("gencode_substruct", *args, **kwargs)
