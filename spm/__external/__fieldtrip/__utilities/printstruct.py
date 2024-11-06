from spm.__wrapper__ import Runtime


def printstruct(*args, **kwargs):
    """
      PRINTSTRUCT converts a MATLAB structure into a multiple-line string that, when  
        evaluated by MATLAB, results in the original structure. It also works for most  
        other standard MATLAB classes, such as numbers, vectors, matrices, and cell-arrays.  
         
        Use as  
          str = printstruct(val)  
        or  
          str = printstruct(name, val)  
        where "val" is any MATLAB variable, e.g. a scalar, vector, matrix, structure, or  
        cell-array. If you pass the name of the variable, the output is a piece of MATLAB code  
        that you can execute, i.e. an ASCII serialized representation of the variable.  
         
        Example  
          a.field1 = 1;  
          a.field2 = 2;  
          s = printstruct(a)  
         
          b = rand(3);  
          s = printstruct(b)  
         
          s = printstruct('c', randn(10)>0.5)  
         
        See also DISP, NUM2STR, INT2STR, MAT2STR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/printstruct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("printstruct", *args, **kwargs)
