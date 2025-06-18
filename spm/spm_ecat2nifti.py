from mpython import Runtime


def spm_ecat2nifti(*args, **kwargs):
    """
      Import ECAT 7 images from CTI PET scanners
        FORMAT N = spm_ecat2nifti(fname,opts)
        fname    - name of ECAT file
        opts     - options structure

        N        - NIfTI object (written in current directory)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ecat2nifti.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ecat2nifti", *args, **kwargs)
