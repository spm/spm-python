from spm.__wrapper__ import Runtime


def _eegsynth_tsv(*args, **kwargs):
    """
      EEGSYNTH_TSV is called from FT_READ_EVENT to read the events from a tsv file  
        written by the recordtrigger module. The .tsv file should also contain a  
        synchronization trigger from the recordsignal module.  
         
        Use as  
          hdr = events_tsv(filename)  
          evt = events_tsv(filename, hdr)  
         
        Note that when reading the header, the number of channels in the actual data is unknown.  
         
        See https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/05-task-events.html  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/eegsynth_tsv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eegsynth_tsv", *args, **kwargs)
