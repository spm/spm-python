from spm.__wrapper__ import Runtime


def spm_standalone(*args, **kwargs):
    """
      Gateway function for standalone SPM  
         
        References:  
         
          SPM Standalone:  https://www.fil.ion.ucl.ac.uk/spm/docs/installation/standalone/  
          MATLAB Compiler: http://www.mathworks.com/products/compiler/  
         
        See also: config/spm_make_standalone.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_standalone.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_standalone", *args, **kwargs, nargout=0)
