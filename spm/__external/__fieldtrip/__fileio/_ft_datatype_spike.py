from spm.__wrapper__ import Runtime


def _ft_datatype_spike(*args, **kwargs):
    """
      FT_DATATYPE_SPIKE describes the FieldTrip MATLAB structure for spike data  
         
        Spike data is obtained using FT_READ_SPIKE to read files from a Plexon,  
        Neuralynx or other animal electrophysiology data acquisition system. It  
        is characterised as a sparse point-process, i.e. each neuronal firing is  
        only represented as the time at which the firing happened. Optionally,  
        the spike waveform can also be represented. Using this waveform, the  
        neuronal firing events can be sorted into their single units.  
         
        A required characteristic of the SPIKE structure is a cell-array with the  
        label of the (single or multi) units.  
         
                label: {'unit1'  'unit2'  'unit3'}  
         
        The fields of the SPIKE structure that contain the specific information  
        per spike depends on the available information. A relevant distinction  
        can be made between the representation of raw spikes that are not related  
        to the temporal structure of the experimental design (i.e trials), and  
        the data representation in which the spikes are related to the trial.  
         
        For a continuous recording the SPIKE structure must contain a cell-array  
        with the raw timestamps as recorded by the hardware system. As example,  
        the original content of the .timestamp field can be  
         
                timestamp:  {[1x504 uint64]  [1x50 uint64]  [1x101 uint64]}  
         
        An optional field that is typically obtained from the raw recording  
        contains the waveforms for every unit and label as a cell-array. For  
        example, the content of this field may be  
         
                waveform:   {[1x32x504 double] [1x32x50 double] [1x32x101 double]}  
         
        If the data has been organised to reflect the temporal structure of the  
        experiment (i.e. the trials), the SPIKE structure should contain a  
        cell-array with the spike times relative to an experimental trigger. The  
        FT_SPIKE_MAKETRIALS function can be used to reorganise the SPIKE  
        structure such that the spike times are expressed relative to a trigger  
        instead of relative to the acquisition devices internal timestamp clock.  
        The time field then contains only those spikes that occurred within one of  
        the trials . The spike times are now expressed on seconds relative to the  
        trigger.  
         
                time:       {[1x504 double] [1x50 double] [1x101 double]}  
         
        In addition, for every spike we register in which trial the spike was  
        recorded:  
         
                trial:      {[1x504 double] [1x50 double] [1x101 double]}  
         
        To fully reconstruct the structure of the spike-train, it is required  
        that the exact start- and end-point of the trial (in seconds) is  
        represented. This is specified in a nTrials x 2 matrix.  
         
                trialtime:  [100x2 double]  
         
        As an example, FT_SPIKE_MAKETRIALS could result in the following  
        SPIKE structure that represents the spikes of three units that were  
        observed in 100 trials:  
         
                label:           {'unit1'  'unit2'  'unit3'}  
                timestamp:       {[1x504 double] [1x50 double] [1x101 double]}  
                timestampdimord: '{chan}_spike'  
                time:            {[1x504 double] [1x50 double] [1x101 double]}  
                trial:           {[1x504 double] [1x50 double] [1x101 double]}  
                trialtime:       [100x2 double]  
                sampleinfo:      [100x2 double]  
                waveform:        {[1x32x504 double] [1x32x50 double] [1x32x101 double]}  
                waveformdimord: '{chan}_lead_time_spike'  
         
        For analysing the relation between the spikes and the local field  
        potential (e.g. phase-locking), the SPIKE structure can have additional  
        fields such as fourierspctrm, lfplabel, freq and fourierspctrmdimord.  
         
        For example, from the structure above we may obtain  
         
                label:               {'unit1'  'unit2'  'unit3'}  
                time:                {[1x504 double] [1x50 double] [1x101 double]}  
                trial:               {[1x504 double] [1x50 double] [1x101 double]}  
                trialtime:           [100x2 double]  
                timestamp:           {[1x504 double] [1x50 double] [1x101 double]}  
                timestampdimord:     '{chan}_spike'  
                waveform:            {[1x32x504 double] [1x32x50 double] [1x32x101 double]}  
                waveformdimord:      '{chan}_lead_time_spike'  
                fourierspctrm:       {504x2x20, 50x2x20, 101x2x20}  
                fourierspctrmdimord: '{chan}_spike_lfplabel_freq'  
                lfplabel:            {'lfpchan1', 'lfpchan2'}  
                freq:                [1x20 double]  
         
        Required fields:  
          - label  
          - timestamp  
         
        Optional fields:  
          - time, trial, trialtime  
          - timestampdimord  
          - unit, unitdimord  
          - waveform, waveformdimord  
          - fourierspctrm, fourierspctrmdimord, freq, lfplabel (these are extra outputs from FT_SPIKETRIGGEREDSPECTRUM and FT_SPIKE_TRIGGEREDSPECTRUM)  
          - hdr  
          - cfg  
         
        Deprecated fields:  
          - origtime, origtrial  
         
        Obsoleted fields:  
          - <unknown>  
         
        Revision history:  
         
        (2020/latest) Add an explicit xxxdimord for each of the known fields.  
         
        (2012) Changed the dimensionality of the waveform to allow both  
        stereotrode and tetrode data to be represented.  
         
        (2011) Defined a consistent spike data representation that can  
        also contain the Fourier spectrum and other fields. Use the xxxdimord  
        to indicate the dimensions of the field.  
         
        (2010) Introduced the time and the trialtime fields.  
         
        (2007) Introduced the spike data representation.  
         
        See also FT_DATATYPE, FT_DATATYPE_RAW, FT_DATATYPE_FREQ, FT_DATATYPE_TIMELOCK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_datatype_spike.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_spike", *args, **kwargs)
