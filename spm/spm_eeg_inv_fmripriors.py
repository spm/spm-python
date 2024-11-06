from spm.__wrapper__ import Runtime


def spm_eeg_inv_fmripriors(*args, **kwargs):
    """
      Generate fMRI priors for the M/EEG source reconstruction  
        FORMAT D = spm_eeg_inv_fmripriors(S)  
         
        S        - optional input struct  
        (optional) fields of S:  
         .D      - MEEG object or filename of M/EEG mat-file  
         .fmri   - filename of prior (SPM) image to be used  
         [.gm    - filename of grey matter (GM) image] {unused}  
         .space  - native (0) or MNI (1) space (must be same for SPM and GM images)  
         .hthr   - height threshold of prior image [defaults: 0.5]  
         .ethr   - extent threshold of clusters in prior image [default: 1]  
         .ncomp  - maximal number of priors component to be extracted [default: Inf]  
         .smooth - variance of the smoothing kernel onto the surface [default: 0.2] {unused}  
         .disp   - whether to display priors on mesh [default: 0]  
         
        D.inv{D.val}.inverse.fmri.priors   - MAT filename containing a variable 'pQ' that  
                   is a [ncomp] cell array of [nb vertices] vectors describing spatial priors  
        D.inv{D.val}.inverse.fmri.texture  - GIfTI texture filename containing all  
                   spatial priors  
        D.inv{D.val}.inverse.fmri.clusters - image filename containing clusters as labels  
       __________________________________________________________________________  
         
        Reference:  
         
        A Parametric Empirical Bayesian framework for fMRI-constrained MEG/EEG   
        source reconstruction. Henson R, Flandin G, Friston K & Mattout J.  
        Human Brain Mapping (in press).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_fmripriors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_fmripriors", *args, **kwargs)
