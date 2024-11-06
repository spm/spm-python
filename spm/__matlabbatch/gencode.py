from spm.__wrapper__ import Runtime


def gencode(*args, **kwargs):
    """
      GENCODE  Generate code to recreate any MATLAB struct/cell variable.  
        For any MATLAB variable, this function generates a .m file that  
        can be run to recreate it. Classes can implement their class specific  
        equivalent of gencode with the same calling syntax. By default, classes  
        are treated similar to struct variables.  
         
        [str, tag, cind] = gencode(item, tag, tagctx)  
        Input arguments:  
        item - MATLAB variable to generate code for (the variable itself, not its  
               name)  
        tag     - optional: name of the variable, i.e. what will be displayed left  
                  of the '=' sign. This can also be a valid struct/cell array  
                  reference, like 'x(2).y'. If not provided, inputname(1) will be  
                  used.  
        tagctx  - optional: variable names not to be used (e.g. keywords,  
                  reserved variables). A cell array of strings.  
        Output arguments:  
        str  - cellstr containing code lines to reproduce the input variable  
        tag  - name of the generated variable (equal to input tag)  
        cind - index into str to the line where the variable assignment is coded  
               (usually 1st line for non-object variables)  
         
        See also GENCODE_RVALUE, GENCODE_SUBSTRUCT, GENCODE_SUBSTRUCTCODE.  
         
        This code has been developed as part of a batch job configuration  
        system for MATLAB. See    
             http://sourceforge.net/projects/matlabbatch  
        for details about the original project.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/gencode.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("gencode", *args, **kwargs)
