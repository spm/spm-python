from spm.__wrapper__ import Runtime


def _volplot(*args, **kwargs):
    """
      VOLPLOT make 2D or 3D plot of volumetric data (e.g. MRI)  
        that is defined on a regular orthogonal grid  
          
        volplot(dat, sel) or  
        volplot(x, y, z, dat, sel)  
        volplot(x, y, z, dat, sel, caxis)  
         
        where sel is one of  
          [x, y, z]     intersection through the three orthogonal directions  
          index         linear index of the voxel of interest  
          'min'         intersection at the minimum  
          'max'         intersection at the maximum  
          'center'      intersect at the center of each axis  
          'interactive' intersect at the center, then go into interactive mode  
          'maxproject'  project the maximum value along each orthogonal direction  
          'sumproject'  integrated value along each orthogonal direction (glassbrain)  
          'montage'     show all slices  
        and caxis is the [min max] used for the color scaling  
          
        See also TRIPLOT, LINEPLOT (in ~roberto/matlab/misc)  
        See also NDGRID  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volplot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("volplot", *args, **kwargs)
