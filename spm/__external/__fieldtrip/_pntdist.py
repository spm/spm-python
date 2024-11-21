from spm.__wrapper__ import Runtime


def _pntdist(*args, **kwargs):
    """
      PNTDIST returns the euclidian distance between two points  
         
         [dist] = pntdist(pnt1, pnt2)  
         
        where pnt1 and pnt2 must be Npnt x 3  
        or either one can be Npnt x 1  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/pntdist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pntdist", *args, **kwargs)
