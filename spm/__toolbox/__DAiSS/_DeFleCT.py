from spm.__wrapper__ import Runtime


def _DeFleCT(*args, **kwargs):
    """
      function w=DeFleCT(passband,SVDpassband,force_passband_flag,stopband,SVDstopband,...  
            LFM,C,SNR2,Csvdtrunc)  
        function w=DeFleCT(passband,SVDpassband,force_passband_flag,stopband,SVDstopband,...  
            LFM,[],SNR2,Whitener)  
         
        Makes a DeFleCT spatial filter with given passband and stopband.   
        passband:     indices to sources for which the targeted output is 1  
        SVDpassband:  how many components represent the passband (optional)  
        force_passband_flag:  forces the output for all passband components to 1  
        stopband:             indices to sources for which the output is 0  
        SVDstopband:  how many components represent the stopband (optional)  
        LFM:  forward model  
        C:    noise covariance matrix (or measurement covariance matrix)  
        SNR2: assumed signal-to-noise ratio (for setting regularization)  
        Csvdtrunc: number of truncated singular values for the inversion of C.  
        Whitener:  the whitener that is applied to the leadfields (optional; if C  
                   is given, the whitener is built from C)  
         
        L, C, SNR2, Csvdtrunc/Whitener need to be given only, when any of these  
        parameters changes  
         
        This function is implemented according to:  
        Hauk and Stenroos: A Framework for the Design of Flexible Cross-Talk  
        Functions for Spatial Filtering of EEG/MEG Data: DeFleCT. HBM 2013.  
         
        Copyright (c) 2012--2013 Matti Stenroos (matti.stenroos@aalto.fi)  
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
                       !! There is no warranty of any kind !!  
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
        17 Oct 2013  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/DeFleCT.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DeFleCT", *args, **kwargs)
