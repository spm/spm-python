from spm.__wrapper__ import Runtime


def _read_ctf_hc(*args, **kwargs):
    """
      READ_CTF_HC reads the MEG headcoil marker positions from an ascii file  
        and computes the coordinate transformation required to get from from  
        dewar to head-coordinates  
         
        the definition of head coordinates is according to CTF standard:  
        - the origin is exactly between LPA and RPA  
        - the positive x-axis goes throught NAS  
        - the positive y-axis goes (approximately) through LPA  
        - the positive z-axis goes up, orthogonal to the x- and y-axes  
         
        hc = read_ctf_hc(filename)  
         
        returns a structure with the following fields  
          hc.dewar.nas    marker positions relative to dewar   
          hc.dewar.lpa  
          hc.dewar.rpa  
          hc.head.nas     marker positions relative to head (measured)   
          hc.head.lpa  
          hc.head.rpa  
          hc.standard.nas marker positions relative to head (expected)  
          hc.standard.lpa  
          hc.standard.rpa  
        and  
          hc.affine       parameter for affine transformation (1x12)  
          hc.homogenous   homogenous transformation matrix (4x4, see warp3d)  
          hc.translation  translation vector (1x3)  
          hc.rotation     rotation matrix (3x3)  
          
        Gradiometer positions can be transformed into head coordinates using the   
        homogeneous transformation matrix, or using the affine parameters and  
        the warp3d function from the WARPING toolbox  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_hc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_hc", *args, **kwargs)
