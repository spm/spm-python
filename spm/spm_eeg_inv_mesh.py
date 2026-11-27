from spm._runtime import Runtime


def spm_eeg_inv_mesh(*args, **kwargs):
    r"""
      Apply the inverse spatial deformation to the template mesh  
        to obtain the individual cortical mesh  
        save the individual GIFTI meshes  
         
        FORMAT mesh = spm_eeg_inv_mesh(sMRI, Msize)  
        Input:  
          sMRI - name of the sMRI file  
          Msize - size of the mesh (1-3)  
        Output:  
          mesh   - inverse - normalized canonical mesh  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_mesh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_mesh", *args, **kwargs)
