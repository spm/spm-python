from spm.__wrapper__ import Runtime


def ft_headcircumference(*args, **kwargs):
    """
      FT_HEADCIRCUMFERENCE determines the head circumference from a triangulated mesh of  
        the scalp in the same way as it would be measured using a measuring tape for  
        fitting an EEG cap.  
         
        Use as  
          circumference = ft_headcircumference(cfg, mesh)  
        where the input mesh corresponds to the output of FT_PREPARE_MESH.  
         
        The configuration should contain  
          cfg.fiducial.nas   = 1x3 vector with coordinates  
          cfg.fiducial.ini   = 1x3 vector with coordinates  
          cfg.fiducial.lpa   = 1x3 vector with coordinates  
          cfg.fiducial.rpa   = 1x3 vector with coordinates  
          cfg.feedback       = string, can be 'yes' or 'no' for detailed feedback (default = 'yes')  
         
        See also FT_ELECTRODEPLACEMENT, FT_PREPARE_MESH, FT_VOLUMESEGMENT, FT_READ_HEADSHAPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_headcircumference.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headcircumference", *args, **kwargs)
