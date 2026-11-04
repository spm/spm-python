from spm._runtime import Runtime


def keep(*args, **kwargs):
    r"""
      KEEP clears all the variables in the workspace except the ones you specify  
        after the keep command. It works just like clear, but only for variables  
         
        KEEP is a modified version of the KEEP M-file written by   
        Xiaoning (David) Yang (1998). It allows the use of the wildcard * as in the  
        clear command  
         
        Examples:  
          keep set1data set2data set3data  
          keep *data  
         
        Martin Barugel (mbarugel@utdt.edu)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/keep.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("keep", *args, **kwargs, nargout=0)
