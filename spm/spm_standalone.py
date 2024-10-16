from spm.__wrapper__ import Runtime


def spm_standalone(*args, **kwargs):
  """  Gateway function for standalone SPM  
     
    References:  
     
      SPM Standalone:  https://www.fil.ion.ucl.ac.uk/spm/docs/installation/standalone/  
      MATLAB Compiler: http://www.mathworks.com/products/compiler/  
     
    See also: config/spm_make_standalone.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_standalone.m)
  """

  return Runtime.call("spm_standalone", *args, **kwargs, nargout=0)
