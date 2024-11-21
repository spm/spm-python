from spm.__wrapper__ import Runtime


def spm_bwlabel(*args, **kwargs):
    """
      Label connected components in 2D or 3D binary images - a compiled routine  
         
        FORMAT [L,num] = spm_bwlabel(BW,n)  
        BW     - 2D or 3D binary image to perform labelling on.  
        n      - connectivity criterion: 6 (surface), 18 (edge) or 26 (corner).  
                 [Default: 18].  
                 (for a 2D image these correspond to 4, 8 and 8 respectively).  
         
        L      - connected component image, i.e. image where each non-zero voxel  
                 in BW will have a value corresponding to its label.  
        num    - number of connected components in L.  
       __________________________________________________________________________  
         
        The implementation is loosely based on:  
        Thurfjell et al. 1992, A new three-dimensional connected components  
        labeling algorithm with simultaneous object feature extraction  
        capability. CVGIP: Graphical Models and Image Processing 54(4):357-364.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bwlabel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bwlabel", *args, **kwargs)
