from spm.__wrapper__ import Runtime


def gencode_rvalue(*args, **kwargs):
    """
      GENCODE_RVALUE  Code for right hand side of MATLAB assignment  
        Generate the right hand side for a valid MATLAB variable  
        assignment. This function is a helper to GENCODE, but can be used on  
        its own to generate code for the following types of variables:  
        * scalar, 1D or 2D numeric, logical or char arrays  
        * scalar or 1D cell arrays, where each item can be one of the supported  
          array types (i.e. nested cells are allowed)  
         
        function [str, sts] = gencode_rvalue(item, cflag)  
        Input argument:  
         item  - value to generate code for  
         cflag - (optional) if true, try to generate 1-line code also for 2D  
                 arrays. This may reduce readability of the generated code.  
                 Defaults to false.  
        Output arguments:  
         str - cellstr with generated code, line per line  
         sts - true, if successful, false if code could not be generated  
         
        See also GENCODE, GENCODE_SUBSTRUCT, GENCODE_SUBSTRUCTCODE.  
         
        This code has been developed as part of a batch job configuration  
        system for MATLAB. See    
             http://sourceforge.net/projects/matlabbatch  
        for details about the original project.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/gencode_rvalue.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("gencode_rvalue", *args, **kwargs)
