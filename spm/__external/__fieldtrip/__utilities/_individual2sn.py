from spm._runtime import Runtime


def _individual2sn(*args, **kwargs):
    r"""
      INDIVIDUAL2SN warps the input coordinates (defined as Nx3 matrix) from  
        individual headspace coordinates into normalised MNI coordinates, using the  
        (inverse of the) warp parameters defined in the structure spmparams.  
         
        this is code inspired by nutmeg and spm: nut_mri2mni, nut_spm_sn2def and  
        nut_spm_invdef which were themselves modified from code originally written  
        by John Ashburner:  
        http://www.sph.umich.edu/~nichols/JohnsGems2.html  
         
        Use as  
          [warped] = individual2sn(P, input)  
         
        Input parameters:  
          P     = structure that contains the contents of an spm generated _sn.mat  
                  file, or the representation of the parameters as of SPM12  
          input = Nx3 array containing the input positions  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/individual2sn.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("individual2sn", *args, **kwargs)
