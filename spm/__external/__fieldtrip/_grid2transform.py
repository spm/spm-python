from spm.__wrapper__ import Runtime


def _grid2transform(*args, **kwargs):
    """
      GRID2TRANSFORM ensures that the volume contains a homogenous transformation  
        matrix. If needed, a homogenous matrix is constructed from the xgrid/ygrid/zgrid  
        fields and those fields are changed to 1:Nx, 1:Ny and 1:Nz  
         
        See also TRANSFORM2GRID  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/grid2transform.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("grid2transform", *args, **kwargs)
