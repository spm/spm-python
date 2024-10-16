from spm.__wrapper__ import Runtime


def ndstest(*args, **kwargs):
  """ Performs numerous tests of ndSparse math operations,   
     
     ndstest(TOL)  
     
   TOL is a tolerance value on the percent error. Execution will pause in debug  
   mode for inspection if any one of the tests exhibits an error greater than  
   TOL.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ndstest.m)
  """

  return Runtime.call("ndstest", *args, **kwargs)
