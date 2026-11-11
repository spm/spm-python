from spm._runtime import Runtime


def spm_standalone(*args, **kwargs):
    r"""
      Gateway function for standalone SPM  
         
        References:  
         
          SPM Standalone:  https://www.fil.ion.ucl.ac.uk/spm/docs/installation/standalone/  
          MATLAB Compiler: http://www.mathworks.com/products/compiler/  
         
        See also: config/spm_make_standalone.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_standalone.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_standalone", *args, **kwargs, nargout=0)
