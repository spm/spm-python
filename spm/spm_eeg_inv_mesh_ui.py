from spm._runtime import Runtime


def spm_eeg_inv_mesh_ui(*args, **kwargs):
    r"""
      Cortical Mesh user interface  
        FORMAT D = spm_eeg_inv_mesh_ui(D, val, sMRI, Msize)  
          
        D        - input data struct (optional)  
        val      -   
        sMRI     -  0 - use template (default), or string with image file name  
        Msize    -   
          
        D        - same data struct including the meshing files and variables  
       __________________________________________________________________________  
         
        Invokes spatial normalisation (if required) and the computation of  
        the individual mesh.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_mesh_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_mesh_ui", *args, **kwargs)
