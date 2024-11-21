from spm.__wrapper__ import Runtime


def spm_eeg_morlet(*args, **kwargs):
    """
      Generate Morlet wavelets  
        FORMAT M = spm_eeg_morlet(Rtf, ST, f, ff)  
          
        Rtf - 'wavelet factor', see [1]  
        ST  - sample time [ms]  
        f   - vector of frequencies [Hz]  
        ff  - frequency to fix Gaussian envelope (sigma = Rtf/(2*pi*ff))  
              Default is ff = f, ie.e, a Morlet transform  
              NB: FWHM = sqrt(8*log(2))*sigma_t;  
         
        M   - cell vector, where each element contains the filter for each  
              frequency in f  
       __________________________________________________________________________  
          
        spm_eeg_morlet generates morlet wavelets for specified frequencies f with  
        a specified ratio Rtf, see [1], for sample time ST (ms). One obtains the  
        wavelet coefficients by convolution of a data vector with the kernels in  
        M. See spm_eeg_tf how one obtains instantaneous power and phase estimates  
        from the wavelet coefficients.  
         
        [1] C. Tallon-Baudry, O. Bertrand, F. Peronnet and J. Pernier, 1998.  
        Induced gamma-Band Activity during the Delay of a Visual Short-term  
        memory Task in Humans. The Journal of Neuroscience (18): 4244-4254.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_morlet.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_morlet", *args, **kwargs)
