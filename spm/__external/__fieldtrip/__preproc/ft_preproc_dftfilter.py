from spm.__wrapper__ import Runtime


def ft_preproc_dftfilter(*args, **kwargs):
    """
      FT_PREPROC_DFTFILTER reduces power line noise (50 or 60Hz) using a   
        discrete Fourier transform (DFT) filter, or spectrum interpolation.  
         
        Use as  
          [filt] = ft_preproc_dftfilter(dat, Fsample)  
        or   
          [filt] = ft_preproc_dftfilter(dat, Fsample, Fline)  
        or  
          [filt] = ft_preproc_dftfilter(dat, Fsample, Fline, 'dftreplace', 'zero')  
        or  
          [filt] = ft_preproc_dftfilter(dat, Fsample, Fline, 'dftreplace', 'neighbour')  
        where  
          dat        data matrix (Nchans X Ntime)  
          Fsample    sampling frequency in Hz  
          Fline      frequency of the power line interference (if omitted from the input  
                     the default European value of 50 Hz is assumed)  
          
        Additional optional arguments are to be provided as key-value pairs:  
          dftreplace = 'zero' (default), 'neighbour' or 'neighbour_fft'.  
          
        If dftreplace = 'zero', the powerline component's amplitude is estimated by  
        fitting a sine and cosine at the specified frequency, and subsequently  
        this fitted signal is subtracted from the data. The longer the sharper  
        the spectral notch will be that is removed from the data.  
        Preferably the data should have a length that is an integer multiple of the  
        oscillation period of the line noise (i.e. 20ms for 50Hz noise). If the  
        data is of different length, then only the first N complete periods are  
        used to estimate the line noise. The estimate is subtracted from the  
        complete data.  
         
        If dftreplace = 'neighbour' the powerline component is reduced via  
        spectrum interpolation (Leske & Dalal, 2019, NeuroImage 189,  
        doi: 10.1016/j.neuroimage.2019.01.026), estimating the required signal  
        components by fitting sines and cosines. The algorithmic steps are  
        described in more detail below. % Preferably the data should have a length   
        that is an integer multiple of the oscillation period of the line noise  
        (i.e. 20ms for 50Hz noise). If the data is of different length, then only  
        the first N complete periods are used to estimate the line noise. The   
        estimate is subtracted from the complete data. Due to the possibility of  
        using slightly truncated data for the estimation of the necessary signal  
        components, this method is more forgiving with respect to numerical  
        issues with respect to the sampling frequency, and suboptimal epoch  
        lengths, in comparison to the method below.  
         
        If dftreplace = 'neighbour_fft' the powerline component is reduced via spectrum   
        interpolation, in its original implementation, based on an algorithm that  
        uses an FFT and iFFT for the estimation of the spectral components. The signal is:  
        I)   transformed into the frequency domain via a fast Fourier  
              transform (FFT),  
        II)  the line noise component (e.g. 50Hz, dftbandwidth = 1 (±1Hz): 49-51Hz) is  
              interpolated in the amplitude spectrum by replacing the amplitude  
              of this frequency bin by the mean of the adjacent frequency bins  
              ('neighbours', e.g. 49Hz and 51Hz).  
              dftneighbourwidth defines frequencies considered for the mean (e.g.  
              dftneighbourwidth = 2 (±2Hz) implies 47-49 Hz and 51-53 Hz).  
              The original phase information of the noise frequency bin is  
              retained.  
        III) the signal is transformed back into the time domain via inverse FFT  
              (iFFT).  
        If Fline is a vector (e.g. [50 100 150]), harmonics are also considered.  
        Preferably the data should be continuous or consist of long data segments  
        (several seconds) to avoid edge effects. If the sampling rate and the  
        data length are such, that a full cycle of the line noise and the harmonics  
        fit in the data and if the line noise is stationary (e.g. no variations  
        in amplitude or frequency), then spectrum interpolation can also be  
        applied to short trials. But it should be used with caution and checked  
        for edge effects.  
         
        When using spectral interpolation, additional arguments are:  
         
          dftbandwidth      half bandwidth of line noise frequency bands, applies to spectrum interpolation, in Hz  
          dftneighbourwidth width of frequencies neighbouring line noise frequencies, applies to spectrum interpolation (dftreplace = 'neighbour'), in Hz  
          
        If the data contains NaNs, the output of the affected channel(s) will be  
        all(NaN).  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_dftfilter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_dftfilter", *args, **kwargs)
