from spm._runtime import Runtime


def _fiff_getpos_ctf(*args, **kwargs):
    r"""
      Copyright (c) 2016, Elekta Oy  
        ---------------------------------------  
          
        Redistribution and use of the Software in source and binary forms, with or without   
        modification, are permitted for non-commercial use.  
          
        The Software is provided "as is" without warranties of any kind, either express or  
        implied including, without limitation, warranties that the Software is free of defects,  
        merchantable, fit for a particular purpose. Developer/user agrees to bear the entire risk   
        in connection with its use and distribution of any and all parts of the Software under this license.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/TSSS/private/fiff_getpos_ctf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_getpos_ctf", *args, **kwargs)
