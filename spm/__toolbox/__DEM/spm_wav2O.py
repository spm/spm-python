from spm._runtime import Runtime


def spm_wav2O(*args, **kwargs):
    r"""
      WAV image format to discrete outcomes (O)  
        FORMAT [O,L,WAV] = spm_wav2O(I,WAV)  
          
        I    - WAV image (frequency bins x time)  
         
        WAV.nd  - Size of tiles in frequency bins       [default: 4]  
        WAV.nb  - Number of discrete singular variates  [9]    
        WAV.mm  - Maximum number of singular modes      [32]  
        WAV.su  - Singular value (normalised) threshold [16]  
        WAV.R   - temporal resampling                   [512]  
         
        O    - Cell array of probabilistic outputs for partition  
        L    - Location of each probabilistic output modality  
         
        WAV  - structure containing image size, pixel locations, singular vectors  
               and bins for singular variates  
         
        WAV.M   - locations of groups  
        WAV.N   - image size  
        WAV.G   - cell array of outcome indices  
        WAV.V   - singular vectors  
        WAV.A   - singular variates  
        WAV.O   - group index  
         
        This routine effectively learns a basis set or receptive fields for a  
        sequence of images supplied in WAV like format. It uses singular value  
        decomposition, retaining the principal singular vectors for subsequent  
        compression and reconstruction. The singular variates discretised over  
        the range of each variate. The ensuing amortisation is saved in WAV  
        structure for sonogram reconstruction. This version uses overlapping  
        receptive fields during the grouping and applies a Gaussian window around  
        the centroid of each group location.  
         
        Crucially, these spatial grouping operators can be generalised to  
        spatiotemporal grouping by specifying a temporal resampling rate. In  
        other words, one can discretise short sequences. This version is  
        specialised for one-dimensional images; namely, frequency bins times  
        time bins.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_wav2O.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_wav2O", *args, **kwargs)
