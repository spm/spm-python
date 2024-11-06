from spm.__wrapper__ import Runtime


def ft_headmodel_fns(*args, **kwargs):
    """
      FT_HEADMODEL_FNS creates the volume conduction structure to be used  
        in the FNS forward solver.  
         
        Use as  
          headmodel = ft_headmodel_fns(seg, ...)  
         
        Optional input arguments should be specified in key-value pairs and  
        can include  
          tissuecond       = matrix C [9XN tissue types]; where N is the number of  
                             tissues and a 3x3 tensor conductivity matrix is stored  
                             in each column.  
          tissue           = see fns_contable_write  
          tissueval        = match tissues of segmentation input  
          transform        = 4x4 transformation matrix (default eye(4))  
          sens             = sensor information (for which ft_datatype(sens,'sens')==1)  
          deepelec         = used in the case of deep voxel solution  
          tolerance        = scalar (default 1e-8)  
         
        Standard default values for conductivity matrix C are derived from  
        Saleheen HI, Ng KT. New finite difference formulations for general  
        inhomogeneous anisotropic bioelectric problems. IEEE Trans Biomed Eng.  
        1997  
         
        Additional documentation available at:  
        http://hunghienvn.nmsu.edu/wiki/index.php/FNS  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_fns.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_fns", *args, **kwargs)
