from spm._runtime import Runtime


def ft_headmodel_infinite(*args, **kwargs):
    r"""
      FT_HEADMODEL_INFINITE returns an infinitely large homogenous  
        volume conduction model. For EEG the volume conductor can be used  
        to compute the leadfield of electric current dipoles, for MEG it  
        can be used for computing the leadfield of magnetic dipoles.  
         
        Use as  
          headmodel = ft_headmodel_infinite;  
         
        See also FT_PREPARE_HEADMODEL, FT_COMPUTE_LEADFIELD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/ft_headmodel_infinite.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_headmodel_infinite", *args, **kwargs)
