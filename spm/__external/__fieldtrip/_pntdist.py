from spm._runtime import Runtime


def _pntdist(*args, **kwargs):
    r"""
      PNTDIST returns the euclidian distance between two points  
         
         [dist] = pntdist(pnt1, pnt2)  
         
        where pnt1 and pnt2 must be Npnt x 3  
        or either one can be Npnt x 1  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/pntdist.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pntdist", *args, **kwargs)
