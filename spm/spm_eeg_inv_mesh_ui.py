from spm.__wrapper__ import Runtime


def spm_eeg_inv_mesh_ui(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_mesh_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_mesh_ui", *args, **kwargs)
