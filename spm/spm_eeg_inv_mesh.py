from spm.__wrapper__ import Runtime


def spm_eeg_inv_mesh(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_mesh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_mesh", *args, **kwargs)
