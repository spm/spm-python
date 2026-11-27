from spm._runtime import Runtime


def _bids_tsv(*args, **kwargs):
    r"""
      BIDS_TSV reads time series data from a BIDS tsv and json file pair. This can for  
        example be used to read the header and data from physio and stim files.  
         
        Use as  
          hdr = bids_tsv(filename);  
          dat = bids_tsv(filename, hdr, begsample, endsample, chanindx);  
          evt = bids_tsv(filename, hdr);  
        to read either the header, the data or the events.  
         
        You should specify the name of the file containing the data as the filename, e.g.  
        the _physio.tsv or the _stim.tsv file.  
         
        See https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/06-physiological-and-other-continuous-recordings.html  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, QUSPIN_LVM, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/bids_tsv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bids_tsv", *args, **kwargs)
