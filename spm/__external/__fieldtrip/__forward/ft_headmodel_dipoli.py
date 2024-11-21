from spm.__wrapper__ import Runtime


def ft_headmodel_dipoli(*args, **kwargs):
    """
      FT_HEADMODEL_DIPOLI creates a volume conduction model of the head  
        using the boundary element method (BEM) for EEG. This function takes  
        as input the triangulated surfaces that describe the boundaries and  
        returns as output a volume conduction model which can be used to  
        compute leadfields.  
         
        This implements  
          Oostendorp TF, van Oosterom A. "Source parameter estimation in  
          inhomogeneous volume conductors of arbitrary shape." IEEE Trans  
          Biomed Eng. 1989 Mar;36(3):382-91.  
         
        The implementation of this function uses an external command-line  
        executable with the name "dipoli" which is provided by Thom Oostendorp.  
         
        Use as  
          headmodel = ft_headmodel_dipoli(mesh, ...)  
         
        The mesh is given as a boundary or a struct-array of boundaries (surfaces)  
         
        Optional input arguments should be specified in key-value pairs and can  
        include  
          isolatedsource   = string, 'yes' or 'no'  
          conductivity     = vector, conductivity of each compartment  
          tempdir          = string, allows you to specify the path for the tempory files (default is automatic)  
          tempname         = string, allows you to specify the full tempory name including path (default is automatic)  
          checkmesh        = 'yes' or 'no'  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_dipoli.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_dipoli", *args, **kwargs)
