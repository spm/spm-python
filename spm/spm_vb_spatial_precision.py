from spm._runtime import Runtime


def spm_vb_spatial_precision(*args, **kwargs):
    r"""
      Compute spatial precision matrix appropriate to prior  
        FORMAT [S] = spm_vb_spatial_precision(prior_type,vxyz,img)  
         
        prior_type - type of prior {'Spatial - UGL','Spatial - GMRF',...  
                                    'Spatial - LORETA','Spatial - WGL'}  
        vxyz       - list of voxels  
        img        - used to construct weights of WGL  
         
        S          - spatial precision matrix  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_spatial_precision.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_spatial_precision", *args, **kwargs)
