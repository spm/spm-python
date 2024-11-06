from spm.__wrapper__ import Runtime


def _sn2individual(*args, **kwargs):
    """
      SN2INDIVIDUAL warps the input coordinates (defined as Nx3 matrix) from  
        normalised MNI coordinates to individual headspace coordinates, using the  
        warp parameters defined in the structure spmparams.  
         
        this is modified from code from nutmeg: nut_mni2mri, which was itself  
        modified from code originally written by John Ashburner:  
        http://www.sph.umich.edu/~nichols/JG2/get_orig_coord2.m  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/sn2individual.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sn2individual", *args, **kwargs)
