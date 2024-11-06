from spm.__wrapper__ import Runtime


def spm_imcalc_ui(*args, **kwargs):
    """
      Perform algebraic functions on images  
        FORMAT Q = spm_imcalc_ui(P,Q,f,flags)  
        P             - matrix of input image filenames  
                        [user prompted to select files if arg missing or empty]  
        Q             - name of output image  
                        [user prompted to enter filename if arg missing or empty]  
        f             - expression to be evaluated  
                        [user prompted to enter expression if arg missing or empty]  
        flags         - cell vector of flags: {dmtx,mask,type,hold}  
        dmtx          - Read images into data matrix?  
                        [defaults (missing or empty) to 0 - no]  
        mask          - implicit zero mask?  
                        [defaults (missing or empty) to 0]  
        type          - data type for output image (see spm_type)  
                        [defaults (missing or empty) to 4 - 16 bit signed shorts]  
        hold          - interpolation hold (see spm_slice_vol)  
                        [defaults (missing or empty) to 0 - nearest neighbour]  
         
        Q (output)    - full pathname of image written  
        Vo            - structure containing information on output image (see spm_vol)  
       __________________________________________________________________________  
         
        This function is now deprecated, use spm_imcalc instead.  
       __________________________________________________________________________  
        Copyright (C) 1998-2011 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_imcalc_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_imcalc_ui", *args, **kwargs)
