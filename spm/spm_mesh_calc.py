from spm.__wrapper__ import Runtime


def spm_mesh_calc(*args, **kwargs):
    """
      Evaluate a function on a mesh's data  
        FORMAT Mo = spm_mesh_calc(Mi,Mo,f,opts)  
        Mi   - input filenames (char array or cellstr)  
               or cell array of gifti objects or patch structures  
        Mo   - output filename  
               if empty, a gifti object is returned and not saved on disk  
        f    - MATLAB expression to be evaluated (string or function handle)  
               (e.g., f = '(s1.*s2).^2' or f = @(s1,s2) (s1.*s2).^2)  
        opts - optional list of pairs of property names and values  
               dmtx - read images into data matrix X [default: false]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_calc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_calc", *args, **kwargs)
