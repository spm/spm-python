from spm.__wrapper__ import Runtime


def ft_headmodel_simbio(*args, **kwargs):
    """
      FT_HEADMODEL_SIMBIO creates a volume conduction model of the head  
        using the finite element method (FEM) for EEG. This function takes  
        as input a volumetric mesh (hexahedral or tetrahedral) and  
        returns as output a volume conduction model which can be used to  
        compute leadfields.  
         
        This implements  
              ...  
         
        Use as  
          headmodel = ft_headmodel_simbio(mesh,'conductivity', conductivities, ...)  
         
        The mesh is given as a volumetric mesh, using ft_datatype_parcellation  
          mesh.pos = vertex positions  
          mesh.tet/mesh.hex = list of volume elements  
          mesh.tissue = tissue assignment for elements  
          mesh.tissuelabel = labels correspondig to tissues  
         
        Required input arguments should be specified in key-value pairs and have  
        to include  
          conductivity   = vector containing tissue conductivities using ordered  
                           corresponding to mesh.tissuelabel  
         
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
         
        To run this on Windows the following packages are necessary:  
         
        Microsoft Visual C++ 2008 Redistributable  
         
        Intel Visual Fortran Redistributables  
         
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_simbio.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_simbio", *args, **kwargs)
