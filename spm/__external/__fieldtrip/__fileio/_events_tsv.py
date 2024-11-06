from spm.__wrapper__ import Runtime


def _events_tsv(*args, **kwargs):
    """
      EVENTS_TSV is called from FT_READ_EVENT to read the events from a BIDS _events.tsv  
        file. Although this function also reads the header for the sampling rate, it cannot  
        be used to read data. Please see BIDS_TSV for reading data.  
         
        Use as  
          hdr = events_tsv(filename)  
          evt = events_tsv(filename, hdr)  
        to read the header or the event information.  
         
        You should specify the _events.tsv file as the filename, the corresponding header  
        file (with the sampling rate) will automatically be located in the same directory.  
         
        See https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/05-task-events.html  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/events_tsv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("events_tsv", *args, **kwargs)
