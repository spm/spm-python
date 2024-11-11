from spm.__wrapper__ import Runtime


def spm_sixel(*args, **kwargs):
    """
      Display or export images in sixel format  
        FORMAT spm_sixel(img,col,[filename])  
        img       - m x n indexed image or m x n x 3 RGB image  
        col       - colormap (three-column matrix of RGB triplets)  
        filename  - output filename [default: stdout]  
         
        See https://en.wikipedia.org/wiki/Sixel  
       __________________________________________________________________________  
         
        r = spm_read_vols(spm_vol(fullfile(spm('Dir'),'tpm','TPM.nii,1')));  
        g = spm_read_vols(spm_vol(fullfile(spm('Dir'),'tpm','TPM.nii,2')));  
        b = spm_read_vols(spm_vol(fullfile(spm('Dir'),'tpm','TPM.nii,3')));  
        [img,col] = rgb2ind(cat(3,r(:,:,50),g(:,:,50),b(:,:,50)),64);  
        spm_sixel(img,col);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sixel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sixel", *args, **kwargs, nargout=0)
