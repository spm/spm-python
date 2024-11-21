from spm.__wrapper__ import Runtime


def ft_freqanalysis(*args, **kwargs):
    """
      FT_FREQANALYSIS performs frequency and time-frequency analysis  
        on time series data over multiple trials  
         
        Use as  
          [freq] = ft_freqanalysis(cfg, data)  
         
        The input data should be organised in a structure as obtained from  
        FT_PREPROCESSING or FT_MVARANALYSIS. The configuration depends on the  
        type of computation that you want to perform.  
         
        The configuration should contain:  
          cfg.method      = different methods of calculating the spectra  
                            'mtmfft', analyses an entire spectrum for the entire data  
                              length, implements multitaper frequency transformation.  
                            'mtmconvol', implements multitaper time-frequency  
                              transformation based on multiplication in the  
                              frequency domain.  
                            'wavelet', implements wavelet time frequency  
                              transformation (using Morlet wavelets) based on  
                              multiplication in the frequency domain.  
                            'tfr', implements wavelet time frequency  
                              transformation (using Morlet wavelets) based on  
                              convolution in the time domain.  
                            'mvar', does a fourier transform on the coefficients  
                              of an estimated multivariate autoregressive model,  
                              obtained with FT_MVARANALYSIS. In this case, the  
                              output will contain a spectral transfer matrix,  
                              the cross-spectral density matrix, and the  
                              covariance matrix of the innovation noise.  
                            'superlet', combines Morlet-wavelet based  
                              decompositions, see below.  
                            'irasa', implements Irregular-Resampling Auto-Spectral  
                              Analysis (IRASA), to separate the fractal components  
                              from the periodicities in the signal.  
                            'hilbert', implements the filter-Hilbert method, see  
                              below.  
          cfg.output      = 'pow'       return the power-spectra  
                            'powandcsd' return the power and the cross-spectra  
                            'fourier'   return the complex Fourier-spectra  
                            'fractal'   (when cfg.method = 'irasa'), return the  
                              fractal component of the spectrum (1/f)  
                            'original'  (when cfg.method = 'irasa'), return the  
                              full power spectrum  
                            'fooof'     returns a smooth power-spectrum,  
                              based on a parametrization of a mixture of aperiodic and periodic  
                              components (only works with cfg.method = 'mtmfft')  
                            'fooof_aperiodic' returns a power-spectrum with the  
                              fooof based estimate of the aperiodic part of the signal.  
                            'fooof_peaks' returns a power-spectrum with the fooof  
                              based estimate of the aperiodic signal removed,  
                              it's expressed as  
                              10^(log10(fooof)-log10(fooof_aperiodic))  
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),  
                              see FT_CHANNELSELECTION for details  
          cfg.channelcmb  = Mx2 cell-array with selection of channel pairs (default = {'all' 'all'}),  
                              see FT_CHANNELCOMBINATION for details  
          cfg.trials      = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.keeptrials  = 'yes' or 'no', return individual trials or average (default = 'no')  
          cfg.keeptapers  = 'yes' or 'no', return individual tapers or average (default = 'no')  
          cfg.pad         = number, 'nextpow2', or 'maxperlen' (default), length  
                              in seconds to which the data can be padded out. The  
                              padding will determine your spectral resolution. If you  
                              want to compare spectra from data pieces of different  
                              lengths, you should use the same cfg.pad for both, in  
                              order to spectrally interpolate them to the same  
                              spectral resolution.  The new option 'nextpow2' rounds  
                              the maximum trial length up to the next power of 2.  By  
                              using that amount of padding, the FFT can be computed  
                              more efficiently in case 'maxperlen' has a large prime  
                              factor sum.  
          cfg.padtype     = string, type of padding (default 'zero', see  
                              ft_preproc_padding)  
          cfg.polyremoval = number (default = 0), specifying the order of the  
                              polynome which is fitted and subtracted from the time  
                              domain data prior to the spectral analysis. For  
                              example, a value of 1 corresponds to a linear trend.  
                              The default is a mean subtraction, thus a value of 0.  
                              If no removal is requested, specify -1.  
                              see FT_PREPROC_POLYREMOVAL for details  
         
         
        METHOD SPECIFIC OPTIONS AND DESCRIPTIONS  
         
        MTMFFT performs frequency analysis on any time series trial data using a  
        conventional single taper (e.g. Hanning) or using the multiple tapers based on  
        discrete prolate spheroidal sequences (DPSS), also known as the Slepian  
        sequence.  
          cfg.taper     = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss')  
                            For cfg.output='powandcsd', you should specify the channel combinations  
                            between which to compute the cross-spectra as cfg.channelcmb. Otherwise  
                            you should specify only the channels in cfg.channel.  
          cfg.foilim    = [begin end], frequency band of interest  
              OR  
          cfg.foi       = vector 1 x numfoi, frequencies of interest  
          cfg.tapsmofrq = number, the amount of spectral smoothing through  
                            multi-tapering. Note that 4 Hz smoothing means  
                            plus-minus 4 Hz, i.e. a 8 Hz smoothing box.  
         
        MTMCONVOL performs time-frequency analysis on any time series trial data using  
        the 'multitaper method' (MTM) based on Slepian sequences as tapers.  
        Alternatively, you can use conventional tapers (e.g. Hanning).  
          cfg.tapsmofrq  = vector 1 x numfoi, the amount of spectral smoothing  
                             through multi-tapering. Note that 4 Hz smoothing means  
                             plus-minus 4 Hz, i.e. a 8 Hz smoothing box.  
           cfg.foi       = vector 1 x numfoi, frequencies of interest  
           cfg.taper     = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss')  
                             For cfg.output='powandcsd', you should specify the channel combinations  
                             between which to compute the cross-spectra as cfg.channelcmb. Otherwise  
                             you should specify only the channels in cfg.channel.  
           cfg.t_ftimwin = vector 1 x numfoi, length of time window (in seconds)  
           cfg.toi       = vector 1 x numtoi, the times on which the analysis  
                             windows should be centered (in seconds), or a string  
                             such as '50%' or 'all'. Both string options  
                             use all timepoints available in the data, but 'all'  
                             centers a spectral estimate on each sample, whereas  
                             the percentage specifies the degree of overlap between  
                             the shortest time windows from cfg.t_ftimwin.  
         
        WAVELET performs time-frequency analysis on any time series trial data using the  
        'wavelet method' based on Morlet wavelets. Using mulitplication in the frequency  
        domain instead of convolution in the time domain.  
          cfg.foi    = vector 1 x numfoi, frequencies of interest  
              OR  
          cfg.foilim = [begin end], frequency band of interest  
          cfg.toi    = vector 1 x numtoi, the times on which the analysis  
                         windows should be centered (in seconds)  
          cfg.width  = 'width', or number of cycles, of the wavelet (default = 7)  
          cfg.gwidth = determines the length of the used wavelets in standard  
                         deviations of the implicit Gaussian kernel and should  
                         be chosen >= 3; (default = 3)  
         
        The standard deviation in the frequency domain (sf) at frequency f0 is  
        defined as: sf = f0/width  
        The standard deviation in the temporal domain (st) at frequency f0 is  
        defined as: st = 1/(2*pi*sf)  
         
        SUPERLET performs time-frequency analysis on any time series trial data using the  
        'superlet method' based on a frequency-wise combination of Morlet wavelets of varying cycle  
        widths (see Moca et al. 2021, https://doi.org/10.1038/s41467-020-20539-9).  
          cfg.foi     = vector 1 x numfoi, frequencies of interest  
              OR  
          cfg.foilim  = [begin end], frequency band of interest  
          cfg.toi     = vector 1 x numtoi, the times on which the analysis  
                          windows should be centered (in seconds)  
          cfg.width   = 'width', or number of cycles, of the base wavelet (default = 3)  
          cfg.gwidth  = determines the length of the used wavelets in standard  
                          deviations of the implicit Gaussian kernel and should  
                          be chosen >= 3; (default = 3)  
          cfg.combine = 'additive', 'multiplicative' (default = 'multiplicative')  
                          determines if cycle numbers of wavelets comprising a superlet  
                          are chosen additively or multiplicatively  
          cfg.order   = vector 1 x numfoi, superlet order, i.e. number of combined  
                          wavelets, for individual frequencies of interest.  
         
        The standard deviation in the frequency domain (sf) at frequency f0 is  
        defined as: sf = f0/width  
        The standard deviation in the temporal domain (st) at frequency f0 is  
        defined as: st = 1/(2*pi*sf)  
         
        HILBERT performs time-frequency analysis on any time series data using a frequency specific  
        bandpass filter, followed by the Hilbert transform.  
          cfg.foi       = vector 1 x numfoi, frequencies of interest  
          cfg.toi       = vector 1 x numtoi, the time points for which the estimates will be returned (in seconds)  
          cfg.width     = scalar, or vector (default: 1), specifying the half bandwidth of the filter;  
          cfg.edgartnan = 'no' (default) or 'yes', replace filter edges with nans, works only for finite impulse response (FIR) filters, and  
                            requires a user specification of the filter order  
         
        For the bandpass filtering the following options can be specified, the default values are as in FT_PREPROC_BANDPASSFILTER, for more  
        information see the help of FT_PREPROCESSING  
          cfg.bpfilttype  
          cfg.bpfiltord        = (optional) scalar, or vector 1 x numfoi;  
          cfg.bpfiltdir  
          cfg.bpinstabilityfix  
          cfg.bpfiltdf  
          cfg.bpfiltwintype  
          cfg.bpfiltdev  
         
        TFR performs time-frequency analysis on any time series trial data using the  
        'wavelet method' based on Morlet wavelets. Using convolution in the time domain  
        instead of multiplication in the frequency domain.  
          cfg.foi    = vector 1 x numfoi, frequencies of interest  
              OR  
          cfg.foilim = [begin end], frequency band of interest  
          cfg.width  = 'width', or number of cycles, of the wavelet (default = 7)  
          cfg.gwidth = determines the length of the used wavelets in standard  
                         deviations of the implicit Gaussian kernel and should  
                         be choosen >= 3; (default = 3)  
         
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a  
        *.mat file on disk and/or the output data will be written to a *.mat  
        file. These mat files should contain only a single variable,  
        corresponding with the input/output structure.  
         
        See also FT_FREQSTATISTICS, FT_FREQDESCRIPTIVES, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqanalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqanalysis", *args, **kwargs)
