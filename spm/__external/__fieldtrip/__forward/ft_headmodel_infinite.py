from spm.__wrapper__ import Runtime


def ft_headmodel_infinite(*args, **kwargs):
    """
      FT_HEADMODEL_INFINITE returns an infinitely large homogenous  
        volume conduction model. For EEG the volume conductor can be used  
        to compute the leadfield of electric current dipoles, for MEG it  
        can be used for computing the leadfield of magnetic dipoles.  
         
        Use as  
          headmodel = ft_headmodel_infinite;  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_infinite.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_infinite", *args, **kwargs)
