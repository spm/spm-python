from spm.__wrapper__ import Runtime


def spm_dcm_display(*args, **kwargs):
    """
      Region and anatomical graph display  
        FORMAT spm_dcm_display(xY,a,c,h)  
        xY    - cell of region structures (see spm_regions)  
        a     - connections of directed graph a(i,j,1) = p value;   
                                              a(i,j,2) = MAP estimate value  
        c     - node-specific inputs  
        h     - axis handle [default: gca from 'Graphics' window]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_display.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_display", *args, **kwargs, nargout=0)
