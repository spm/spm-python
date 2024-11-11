from spm.__wrapper__ import Runtime


def ft_headmodel_singlesphere(*args, **kwargs):
    """
      FT_HEADMODEL_SINGLESPHERE creates a volume conduction model of the  
        head by fitting a spherical model to a set of points that describe  
        the head surface.  
         
        For MEG this implements Cuffin BN, Cohen D.  "Magnetic fields of a dipole in  
        special volume conductor shapes" IEEE Trans Biomed Eng. 1977 Jul;24(4):372-81.  
         
        For EEG this implements R. Kavanagh, T. M. Darccey, D. Lehmann, and D. H. Fender.  
        Evaluation of methods for three-dimensional localization of electric sources in the  
        human brain. IEEE Trans Biomed Eng, 25:421-429, 1978.  
         
        Use as  
          headmodel = ft_headmodel_singlesphere(mesh, ...)  
         
        Optional arguments should be specified in key-value pairs and can include  
          conductivity     = number, conductivity of the sphere  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_singlesphere.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_singlesphere", *args, **kwargs)
