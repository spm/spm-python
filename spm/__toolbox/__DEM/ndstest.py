from spm._runtime import Runtime


def ndstest(*args, **kwargs):
    r"""
     Performs numerous tests of ndSparse math operations,   
         
         ndstest(TOL)  
         
       TOL is a tolerance value on the percent error. Execution will pause in debug  
       mode for inspection if any one of the tests exhibits an error greater than  
       TOL.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ndstest.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ndstest", *args, **kwargs)
