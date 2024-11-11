from spm.__wrapper__ import Runtime


def _snirf(*args, **kwargs):
    """
      SNIRF reads data from a SNIRF file and returns it in a format that FieldTrip understands.  
         
        See https://github.com/fNIRS/snirf/blob/master/snirf_specification.md  
         
        Use as  
          hdr = snirf(filename);  
          dat = snirf(filename, hdr, begsample, endsample, chanindx);  
          evt = snirf(filename, hdr);  
         
        The SNIRF format allows for multiple blocks of data channels anx aux channels, each  
        with a different sampling frequency. That is not allowed in this code; all channels  
        must have the same sampling rate and be sampled at the same time.  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, SNIRF2OPTO  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/snirf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("snirf", *args, **kwargs)
