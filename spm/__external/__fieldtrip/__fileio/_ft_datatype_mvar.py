from spm.__wrapper__ import Runtime


def _ft_datatype_mvar(*args, **kwargs):
    """
      FT_DATATYPE_MVAR describes the FieldTrip MATLAB structure for multi-variate  
        autoregressive model data.  
         
        The mvar datatype represents multivariate model estimates in the time- or  
        in the frequency-domain. This is usually obtained from FT_MVARANALYSIS,  
        optionally in combination with FT_FREQANALYSIS.  
         
        The following is an example of sensor level MVAR model data in the time domain  
         
               dimord: 'chan_chan_lag'     defines how the numeric data should be interpreted  
                label: {3x1 cell}          the channel labels  
               coeffs: [3x3x5 double]      numeric data (MVAR model coefficients 3 channels x 3 channels x 5 time lags)  
             noisecov: [3x3 double]        more numeric data (covariance matrix of the noise residuals 3 channels x 3 channels)  
                  dof: 500  
          fsampleorig: 200  
                  cfg: [1x1 struct]  
         
        The following is an example of sensor-level MVAR model data in the frequency domain  
         
               dimord: 'chan_chan_freq'    defines how the numeric data should be interpreted  
                label: {3x1 cell}          the channel labels  
                 freq: [1x101 double]      the frequencies, expressed in Hz  
             transfer: [3x3x101 double]  
            itransfer: [3x3x101 double]  
             noisecov: [3x3 double]  
            crsspctrm: [3x3x101 double]  
                  dof: 500  
                  cfg: [1x1 struct]  
         
        Required fields:  
          - label, dimord, freq  
         
        Optional fields:  
          - too many to mention  
         
        Deprecated fields:  
          - <none>  
         
        Obsoleted fields:  
          - <none>  
         
        Revision history:  
         
        (2011/latest) The description of the sensors has changed, see FT_DATATYPE_SENS  
        for further information.  
         
        (2008) The initial version was defined.  
         
        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP, FT_DATATYPE_FREQ,  
        FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, FT_DATATYPE_SPIKE,  
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_datatype_mvar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_mvar", *args, **kwargs)
